"""
src/rl/environment.py

RL environment module for the Adaptive RL Network Anomaly Detection
project. Implements the full per-sample cycle described in master handoff
section 26:

    state -> action (weights) -> ensemble score -> prediction -> reward -> next_state

Design note -- why this is a per-sample "bandit-style" MDP, not a classic
sequential-control MDP: each network traffic flow is an independent sample.
The agent's chosen weights for one flow have no causal effect on the next
flow's traffic characteristics. So `next_state` here means "the state built
from the next flow in the (optionally shuffled) dataset", not a
consequence of the action just taken. This matches the linear pipeline
diagram in master handoff section 26 and is a standard formulation for
applying RL to a fixed, i.i.d.-ish supervised dataset.

Score combination reuses S3's own normalized-score columns rather than
duplicating normalization logic: the first ACTION_DIM columns of every S3
state (built by S3StateBuilder, see state.py) are the percentile-normalized
per-detector scores, in the same DETECTOR_NAMES / MODEL_ORDER used by
action.py. The environment simply takes a weighted dot product of those
columns with the agent's projected action.

This module does NOT:
    - train models or fit normalizers (state.py's job, done beforehand)
    - implement the RL algorithm itself (agent.py's job)
    - decide the reward scheme (reward.py's job, imported here)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from .state import STATE_DIM
from .action import ActionProjector, ACTION_DIM, validate_weights
from .reward import compute_reward_scalar, FINAL_REWARD_SCHEME, RewardScheme


@dataclass
class StepResult:
    """Result of a single environment step."""

    next_state: Optional[np.ndarray]
    reward: float
    done: bool
    info: dict


def _validate_states(states: np.ndarray) -> np.ndarray:
    states = np.asarray(states, dtype=np.float32)
    if states.ndim != 2 or states.shape[1] != STATE_DIM:
        raise ValueError(f"states must have shape (n, {STATE_DIM}), got {states.shape}")
    return states


def _validate_binary_labels(y_true: np.ndarray, n_expected: int) -> np.ndarray:
    y_true = np.asarray(y_true)
    if y_true.shape != (n_expected,):
        raise ValueError(f"y_true must have shape ({n_expected},), got {y_true.shape}")
    unique = np.unique(y_true)
    if not np.all(np.isin(unique, [0, 1])):
        raise ValueError(f"y_true must contain only 0/1 values, got unique={unique}")
    return y_true.astype(np.int64)


def ensemble_predict(states, weights, threshold: float = 0.5):
    """
    Vectorized ensemble scoring: combine each state's percentile-normalized
    detector scores (columns [0:ACTION_DIM]) with weights, then threshold.

    Parameters
    ----------
    states : array of shape (n, STATE_DIM), built by S3StateBuilder.build().
    weights : either a single weight vector of shape (ACTION_DIM,), applied
        to every row (e.g. evaluating one fixed/static policy over a
        dataset), or a per-row weight matrix of shape (n, ACTION_DIM)
        (e.g. replaying a trained agent's chosen action at each row).
    threshold : ensemble-score cutoff for predicting attack (1) vs benign
        (0). Percentile-normalized scores and weights summing to 1 keep the
        ensemble score in [0, 1], so 0.5 is a reasonable default -- but it
        should be tuned on validation data, never on the final test set
        (master handoff section 32), before being used for real evaluation.

    Returns
    -------
    (ensemble_scores, y_pred) : both np.ndarray of shape (n,)
    """
    states = _validate_states(states)
    scores = states[:, :ACTION_DIM]

    weights = np.asarray(weights, dtype=np.float64)
    if weights.ndim == 1:
        validate_weights(weights)
        ensemble_scores = scores @ weights
    elif weights.ndim == 2:
        if weights.shape != (states.shape[0], ACTION_DIM):
            raise ValueError(
                f"per-row weights must have shape {(states.shape[0], ACTION_DIM)}, "
                f"got {weights.shape}"
            )
        validate_weights(weights)
        ensemble_scores = np.sum(scores * weights, axis=1)
    else:
        raise ValueError(f"weights must be 1D or 2D, got shape {weights.shape}")

    y_pred = (ensemble_scores >= threshold).astype(np.int64)
    return ensemble_scores, y_pred


class AnomalyEnsembleEnv:
    """
    Episodic environment cycling through a fixed, precomputed S3 state
    dataset. At each step:

        1. The caller supplies a raw action (the agent's unconstrained
           output for the CURRENT state).
        2. The action is projected into valid weights (action.py).
        3. Those weights are combined with the current state's normalized
           detector scores into an ensemble score, then thresholded into a
           prediction.
        4. Reward is computed from (y_true, y_pred) using the frozen R1
           scheme (reward.py).
        5. The environment advances to the next sample (shuffled order,
           optionally wrapping) and returns its state.

    This class does not implement or hold an RL agent -- it only manages
    data iteration, scoring, and reward. `agent.py` is expected to call
    reset()/step() and drive its own policy.
    """

    def __init__(
        self,
        states: np.ndarray,
        y_true: np.ndarray,
        threshold: float = 0.5,
        action_projector: Optional[ActionProjector] = None,
        reward_scheme: RewardScheme = FINAL_REWARD_SCHEME,
        episode_length: Optional[int] = None,
        shuffle: bool = True,
        seed: Optional[int] = None,
    ) -> None:
        self.states = _validate_states(states)
        self.y_true = _validate_binary_labels(y_true, n_expected=self.states.shape[0])
        self.threshold = threshold
        self.action_projector = action_projector or ActionProjector(method="softmax")
        self.reward_scheme = reward_scheme
        self.episode_length = (
             self.states.shape[0]
             if episode_length is None
             else episode_length
        )
        if self.episode_length <= 0:
            raise ValueError("episode_length must be positive")
        self.shuffle = shuffle
        self._rng = np.random.default_rng(seed)

        self._order: Optional[np.ndarray] = None
        self._pos = 0
        self._episode_step = 0

    @property
    def n_samples(self) -> int:
        return self.states.shape[0]

    def reset(self) -> np.ndarray:
        """Start a new episode: (re)shuffle iteration order and return the
        first state."""
        self._order = (
            self._rng.permutation(self.n_samples) if self.shuffle else np.arange(self.n_samples)
        )
        self._pos = 0
        self._episode_step = 0
        return self._current_state()

    def _current_index(self) -> int:
        # Modulo wrap allows episode_length to exceed the dataset size,
        # cycling back through the same shuffled order.
        return int(self._order[self._pos % self.n_samples])

    def _current_state(self) -> np.ndarray:
        return self.states[self._current_index()]

    def step(self, raw_action) -> StepResult:
        """
        Advance one step using `raw_action` (the agent's raw output for the
        state most recently returned by reset()/step()).
        """
        if self._order is None:
            raise RuntimeError("Call reset() before step()")

        idx = self._current_index()
        state = self.states[idx]

        weights = self.action_projector.project(raw_action)
        normalized_scores = state[:ACTION_DIM]
        ensemble_score = float(np.dot(normalized_scores, weights))
        y_pred = int(ensemble_score >= self.threshold)
        y_true = int(self.y_true[idx])

        reward = compute_reward_scalar(y_true, y_pred, scheme=self.reward_scheme)

        info = {
            "index": idx,
            "ensemble_score": ensemble_score,
            "weights": weights,
            "y_true": y_true,
            "y_pred": y_pred,
        }

        self._pos += 1
        self._episode_step += 1
        done = self._episode_step >= self.episode_length

        next_state = None if done else self._current_state()
        return StepResult(next_state=next_state, reward=reward, done=done, info=info)

    def run_episode(self, agent_fn) -> dict:
        """
        Convenience driver for testing the full cycle without a real RL
        agent. `agent_fn(state) -> raw_action` is called once per step.

        Returns a summary dict: total_reward, mean_reward, n_steps, and the
        per-step info dicts (for inspection in tests/notebooks).
        """
        state = self.reset()
        total_reward = 0.0
        steps = []
        done = False
        while not done:
            raw_action = agent_fn(state)
            result = self.step(raw_action)
            total_reward += result.reward
            steps.append(result.info)
            state = result.next_state
            done = result.done

        n_steps = len(steps)
        return {
            "total_reward": total_reward,
            "mean_reward": total_reward / n_steps if n_steps else 0.0,
            "n_steps": n_steps,
            "steps": steps,
        }