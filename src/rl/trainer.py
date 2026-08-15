"""
src/rl/trainer.py

Training loop for the Adaptive RL Network Anomaly Detection PPO agent.
Coordinates environment.py (state -> action -> ensemble -> prediction ->
reward -> next_state) with agent.py (PPOAgent: rollout collection + PPO
updates), and handles the remaining responsibilities listed in master
handoff section 28: episodes/steps, experience collection, training,
validation, checkpointing, logging.

DATA-LEAKAGE DISCIPLINE (master handoff section 32)
-----------------------------------------------------------------------------
Trainer takes a `train_env` and an optional `val_env`, both explicitly
supplied by the caller. It never touches a "test" set by name or default --
there is no `test_env` parameter here on purpose. The final test set must
be evaluated exactly once, after training is finished, by calling
`Trainer.evaluate()` directly against a test-set environment built outside
this training loop. Do not wire a test environment into `val_env` -- that
IS the leakage this module is structured to make awkward to do by
accident.

ROLLOUT / BOOTSTRAP CORRECTNESS NOTE
-----------------------------------------------------------------------------
RolloutBuffer.compute_returns_and_advantages(last_value, done) expects
`done` to describe whether the LAST transition added to the buffer was
itself terminal (i.e. self.dones[-1] as recorded by buffer.add()) -- not
whether the state the trainer happens to be standing on afterward is
terminal. Because collect_rollout() auto-resets AnomalyEnsembleEnv
mid-rollout on episode boundaries, "the state we stopped at" is always a
fresh, non-terminal state (either an env.reset() result or a genuine
next_state) regardless of whether the rollout happened to end exactly on a
done step. Passing the wrong flag here would silently corrupt the GAE
bootstrap on any rollout that ends mid-episode. See collect_rollout()
below for where this is threaded through correctly.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import torch

from .agent import PPOAgent, RolloutBuffer
from .environment import AnomalyEnsembleEnv
from .reward import confusion_counts

try:
    from sklearn.metrics import roc_auc_score, average_precision_score

    _SKLEARN_AVAILABLE = True
except ImportError:  # pragma: no cover - sklearn is an expected project dep
    _SKLEARN_AVAILABLE = False


@dataclass
class TrainerConfig:
    total_timesteps: int = 100_000
    rollout_steps: Optional[int] = None  # defaults to agent.config.rollout_steps

    eval_every_updates: int = 10
    eval_episodes: int = 1

    checkpoint_dir: Optional[str] = None       # None disables checkpointing
    checkpoint_every_updates: Optional[int] = None  # periodic; independent of "best" checkpoint

    log_path: Optional[str] = None             # None disables file logging (JSON-lines)
    verbose: bool = True

    seed: Optional[int] = None


class Trainer:
    """
    Drives PPO training of an AnomalyEnsembleEnv-compatible agent.

    Usage
    -----
    >>> agent = PPOAgent(PPOConfig(rollout_steps=2048))
    >>> trainer = Trainer(agent, train_env, val_env, TrainerConfig(
    ...     total_timesteps=200_000,
    ...     checkpoint_dir="evaluation_results/rl_checkpoints",
    ...     log_path="evaluation_results/rl_training_log.jsonl",
    ... ))
    >>> history = trainer.train()
    >>> # ... only once, after training is fully finished:
    >>> test_metrics = trainer.evaluate(test_env, n_episodes=1)
    """

    def __init__(
        self,
        agent: PPOAgent,
        train_env: AnomalyEnsembleEnv,
        val_env: Optional[AnomalyEnsembleEnv] = None,
        config: Optional[TrainerConfig] = None,
    ):
        self.agent = agent
        self.train_env = train_env
        self.val_env = val_env
        self.config = config or TrainerConfig()

        if self.config.eval_every_updates <= 0:
            raise ValueError("eval_every_updates must be positive")

        if self.config.eval_episodes <= 0:
            raise ValueError("eval_episodes must be positive")

        self.rollout_steps = (
            self.config.rollout_steps
            or self.agent.config.rollout_steps
        )
        if self.rollout_steps is None:
            raise ValueError(
                "rollout_steps must be set via TrainerConfig.rollout_steps or "
                "agent.config.rollout_steps"
            )

        self.history: list[dict] = []
        self._best_val_reward = -np.inf
        self._n_updates = 0
        self._n_timesteps = 0
        self._rng = np.random.default_rng(self.config.seed)

        self._state = self.train_env.reset()

        if self.config.checkpoint_dir is not None:
            Path(self.config.checkpoint_dir).mkdir(parents=True, exist_ok=True)
        if self.config.log_path is not None:
            Path(self.config.log_path).parent.mkdir(parents=True, exist_ok=True)

    # -- rollout collection -------------------------------------------------

    def collect_rollout(self, rollout_steps: Optional[int] = None) -> RolloutBuffer:
        """Collect exactly `rollout_steps` transitions from train_env under
        the current stochastic policy, auto-resetting on episode
        boundaries, then compute GAE advantages/returns."""
        rollout_steps = self.rollout_steps if rollout_steps is None else rollout_steps
        buffer = RolloutBuffer(
            buffer_size=rollout_steps,
            state_dim=self.agent.config.state_dim,
            action_dim=self.agent.config.action_dim,
            gamma=self.agent.config.gamma,
            gae_lambda=self.agent.config.gae_lambda,
        )

        state = self._state
        last_transition_done = False

        for _ in range(rollout_steps):
            action, log_prob, value = self.agent.step(state)
            result = self.train_env.step(action)

            buffer.add(state, action, log_prob, result.reward, value, result.done)
            self._n_timesteps += 1
            last_transition_done = result.done

            state = self.train_env.reset() if result.done else result.next_state

        self._state = state

        # Bootstrap value of the state we're standing on after the loop.
        # `last_transition_done` -- NOT any property of `self._state` --
        # is what compute_returns_and_advantages needs; see module
        # docstring for why these are different things here.
        last_value = self.agent.get_value(self._state)
        buffer.compute_returns_and_advantages(last_value, last_transition_done)
        return buffer

    @staticmethod
    def _rollout_summary(buffer: RolloutBuffer) -> dict:
        n = len(buffer)
        rewards = buffer.rewards[:n]
        return {
            "mean_reward": float(rewards.mean()),
            "total_reward": float(rewards.sum()),
            "n_steps": n,
        }

    # -- evaluation -----------------------------------------------------

    def evaluate(self, env: AnomalyEnsembleEnv, n_episodes: int = 1) -> dict:
        """
        Run the CURRENT policy deterministically (explore=False, i.e. the
        policy mean -- no sampling noise) through `env` for n_episodes full
        episodes, and report metrics in the same format used for the
        project's baseline comparisons (master handoff sections 8, 12, 20,
        31): precision, recall, F1, ROC-AUC, PR-AUC, plus RL mean/total
        reward and the underlying confusion counts.

        Caller controls which env this runs against. To respect section 32,
        only ever pass a genuine test-set environment here ONCE, after
        training is complete -- never inside the training loop (that's what
        val_env / eval_every_updates are for).
        """
        all_y_true, all_y_pred, all_scores, all_rewards = [], [], [], []

        for _ in range(n_episodes):
            state = env.reset()
            done = False
            while not done:
                action = self.agent.select_action(state, explore=False)
                result = env.step(action)
                all_y_true.append(result.info["y_true"])
                all_y_pred.append(result.info["y_pred"])
                all_scores.append(result.info["ensemble_score"])
                all_rewards.append(result.reward)
                state = result.next_state
                done = result.done

        y_true = np.asarray(all_y_true)
        y_pred = np.asarray(all_y_pred)
        scores = np.asarray(all_scores)
        rewards = np.asarray(all_rewards)

        counts = confusion_counts(y_true, y_pred)
        precision = counts.tp / (counts.tp + counts.fp) if (counts.tp + counts.fp) > 0 else 0.0
        recall = counts.tp / (counts.tp + counts.fn) if (counts.tp + counts.fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        metrics = {
            "mean_reward": float(rewards.mean()),
            "total_reward": float(rewards.sum()),
            "n_steps": int(len(rewards)),
            "tp": counts.tp,
            "tn": counts.tn,
            "fp": counts.fp,
            "fn": counts.fn,
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
        }

        if _SKLEARN_AVAILABLE and len(np.unique(y_true)) > 1:
            metrics["roc_auc"] = float(roc_auc_score(y_true, scores))
            metrics["pr_auc"] = float(average_precision_score(y_true, scores))

        return metrics

    # -- training loop -------------------------------------------------------

    def train(self, total_timesteps: Optional[int] = None) -> list:
        """Run PPO training until `total_timesteps` env steps have been
        collected (defaults to config.total_timesteps). Returns the full
        history list (also accumulated on self.history)."""
        total_timesteps = (
            self.config.total_timesteps
            if total_timesteps is None
            else total_timesteps
        )
        start_time = time.time()

        while self._n_timesteps < total_timesteps:
            remaining_timesteps = total_timesteps - self._n_timesteps
            buffer = self.collect_rollout(min(self.rollout_steps, remaining_timesteps))
            losses = self.agent.train_step(buffer)
            self._n_updates += 1

            log_entry = {
                "update": self._n_updates,
                "timesteps": self._n_timesteps,
                "elapsed_sec": time.time() - start_time,
                **losses,
                **{f"train_{k}": v for k, v in self._rollout_summary(buffer).items()},
            }

            if self.val_env is not None and self._n_updates % self.config.eval_every_updates == 0:
                val_metrics = self.evaluate(self.val_env, n_episodes=self.config.eval_episodes)
                log_entry.update({f"val_{k}": v for k, v in val_metrics.items()})

                if val_metrics["mean_reward"] > self._best_val_reward:
                    self._best_val_reward = val_metrics["mean_reward"]
                    if self.config.checkpoint_dir is not None:
                        self.save_checkpoint(Path(self.config.checkpoint_dir) / "best.pt")

            if (
                self.config.checkpoint_dir is not None
                and self.config.checkpoint_every_updates is not None
                and self._n_updates % self.config.checkpoint_every_updates == 0
            ):
                self.save_checkpoint(
                    Path(self.config.checkpoint_dir) / f"update_{self._n_updates}.pt"
                )

            self.history.append(log_entry)
            if self.config.log_path is not None:
                self._append_log(log_entry)
            if self.config.verbose:
                self._print_progress(log_entry)

        return self.history

    # -- logging -----------------------------------------------------------

    def _append_log(self, entry: dict) -> None:
        with open(self.config.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    @staticmethod
    def _print_progress(entry: dict) -> None:
        msg = (
            f"[update {entry['update']:4d}] timesteps={entry['timesteps']:7d} "
            f"train_mean_reward={entry['train_mean_reward']:+.4f} "
            f"policy_loss={entry['policy_loss']:.4f} value_loss={entry['value_loss']:.4f}"
        )
        if "val_mean_reward" in entry:
            msg += f" | val_mean_reward={entry['val_mean_reward']:+.4f}"
            if "val_f1" in entry:
                msg += f" val_f1={entry['val_f1']:.4f}"
        print(msg)

    # -- checkpointing -----------------------------------------------------

    def save_checkpoint(self, path) -> None:
        """Save agent weights + trainer progress. `path` is caller-supplied
        (no hardcoded location)."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "agent_state": self.agent.state_dict(),
                "n_updates": self._n_updates,
                "n_timesteps": self._n_timesteps,
                "best_val_reward": self._best_val_reward,
            },
            path,
        )

    def load_checkpoint(self, path) -> None:
        """Restore agent weights + trainer progress from a checkpoint saved
        by save_checkpoint(). Does NOT restore the training env's internal
        iteration position -- resumed training continues with a fresh
        env.reset()."""
        checkpoint = torch.load(path, map_location=self.agent.device)
        self.agent.load_state_dict(checkpoint["agent_state"])
        self._n_updates = checkpoint["n_updates"]
        self._n_timesteps = checkpoint["n_timesteps"]
        self._best_val_reward = checkpoint["best_val_reward"]
        self._state = self.train_env.reset()