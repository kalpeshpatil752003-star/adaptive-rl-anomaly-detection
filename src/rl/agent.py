"""
src/rl/agent.py

RL algorithm module for the Adaptive RL Network Anomaly Detection project.

ALGORITHM: PPO (Proximal Policy Optimization)
-----------------------------------------------------------------------------
PPO is an on-policy actor-critic algorithm utilizing clipped surrogate
objective updates. The policy parameterizes an unconstrained Gaussian
distribution over latent action logits:
    pi(a_raw | s) ~ N(mu(s), diag(sigma^2))

LATENT ACTION SPACE & SIMPLEX PROJECTION
-----------------------------------------------------------------------------
- Policy Domain: The stochastic policy lives in the raw logit space R^ACTION_DIM.
  PPO evaluates log_prob and entropy directly on these unconstrained logits.
- Mean Bounding: `max_action` (default 5.0) limits the policy mean mu(s) via
  tanh to keep the distribution well-centered, while raw sampled instances
  can span the real line.
- Environment Projection: `action.ActionProjector` applies a deterministic
  softmax transformation w = softmax(a_raw) downstream in the environment
  to project logits onto the 4-dim probability simplex (w >= 0, sum(w) = 1).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.distributions.normal import Normal

from .state import STATE_DIM
from .action import ACTION_DIM


# ---------------------------------------------------------------------------
# Rollout Buffer with Generalized Advantage Estimation (GAE)
# ---------------------------------------------------------------------------


class RolloutBuffer:
    """Fixed-capacity on-policy trajectory buffer storing transitions, log-probs,
    and value estimates for GAE computation."""

    def __init__(
        self,
        buffer_size: int,
        state_dim: int = STATE_DIM,
        action_dim: int = ACTION_DIM,
        gamma: float = 0.99,
        gae_lambda: float = 0.95,
    ):
        if buffer_size <= 0:
            raise ValueError("buffer_size must be positive")
        self.buffer_size = buffer_size
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.gae_lambda = gae_lambda

        self.states = np.zeros((buffer_size, state_dim), dtype=np.float32)
        self.actions = np.zeros((buffer_size, action_dim), dtype=np.float32)
        self.log_probs = np.zeros((buffer_size,), dtype=np.float32)
        self.rewards = np.zeros((buffer_size,), dtype=np.float32)
        self.values = np.zeros((buffer_size,), dtype=np.float32)
        self.dones = np.zeros((buffer_size,), dtype=np.float32)

        self.advantages = np.zeros((buffer_size,), dtype=np.float32)
        self.returns = np.zeros((buffer_size,), dtype=np.float32)

        self._ptr = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def add(
        self,
        state: np.ndarray,
        action: np.ndarray,
        log_prob: float,
        reward: float,
        value: float,
        done: bool,
    ) -> None:
        if self._size >= self.buffer_size:
            raise RuntimeError("RolloutBuffer is full. Compute returns and reset before adding more.")

        self.states[self._ptr] = np.asarray(state, dtype=np.float32)
        self.actions[self._ptr] = np.asarray(action, dtype=np.float32)
        self.log_probs[self._ptr] = float(log_prob)
        self.rewards[self._ptr] = float(reward)
        self.values[self._ptr] = float(value)
        self.dones[self._ptr] = float(done)

        self._ptr += 1
        self._size += 1

    def compute_returns_and_advantages(self, last_value: float, done: bool) -> None:
        """Compute generalized advantages and value targets."""
        last_gae = 0.0
        for t in reversed(range(self._size)):
            if t == self._size - 1:
                next_non_terminal = 1.0 - float(done)
                next_value = last_value
            else:
                next_non_terminal = 1.0 - self.dones[t]
                next_value = self.values[t + 1]

            delta = self.rewards[t] + self.gamma * next_value * next_non_terminal - self.values[t]
            last_gae = delta + self.gamma * self.gae_lambda * next_non_terminal * last_gae
            self.advantages[t] = last_gae

        self.returns[: self._size] = self.advantages[: self._size] + self.values[: self._size]

        advantages = self.advantages[: self._size]
        self.advantages[: self._size] = (advantages - advantages.mean()) / (
            advantages.std() + 1e-8
        )

    def get_batches(
        self, batch_size: int, rng: Optional[np.random.Generator] = None
    ) -> Generator[dict, None, None]:
        """Generate randomized mini-batches over the collected rollout."""
        if self._size < batch_size:
            raise ValueError(f"batch_size {batch_size} exceeds collected rollout size {self._size}")

        rng = rng or np.random.default_rng()
        indices = np.arange(self._size)
        rng.shuffle(indices)

        for start in range(0, self._size, batch_size):
            batch_idx = indices[start : start + batch_size]
            yield {
                "states": self.states[batch_idx],
                "actions": self.actions[batch_idx],
                "log_probs": self.log_probs[batch_idx],
                "returns": self.returns[batch_idx],
                "advantages": self.advantages[batch_idx],
                "values": self.values[batch_idx],
            }

    def reset(self) -> None:
        self._ptr = 0
        self._size = 0


# ---------------------------------------------------------------------------
# Networks
# ---------------------------------------------------------------------------


def layer_init(layer: nn.Linear, std: float = np.sqrt(2), bias_const: float = 0.0) -> nn.Linear:
    """Orthogonal initialization for stable policy gradient training."""
    nn.init.orthogonal_(layer.weight, std)
    nn.init.constant_(layer.bias, bias_const)
    return layer


class Actor(nn.Module):
    """Gaussian policy: state (14) -> action distribution over logits (4)."""

    def __init__(
        self,
        state_dim: int = STATE_DIM,
        action_dim: int = ACTION_DIM,
        hidden_dim: int = 128,
        max_action: float = 5.0,
    ):
        super().__init__()
        self.max_action = max_action
        self.net = nn.Sequential(
            layer_init(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, action_dim), std=0.01),
        )
        self.log_std = nn.Parameter(torch.zeros(action_dim))

    def forward(self, state: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        mean = self.max_action * torch.tanh(self.net(state))
        std = torch.exp(
            torch.clamp(self.log_std, -5.0, 2.0)
        )
        return mean, std

    def get_action(
        self, state: torch.Tensor, deterministic: bool = False
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        mean, std = self.forward(state)
        if deterministic:
            return mean, torch.zeros(state.size(0), device=state.device)
        dist = Normal(mean, std)
        action = dist.sample()
        log_prob = dist.log_prob(action).sum(dim=-1)
        return action, log_prob

    def evaluate_action(
        self, state: torch.Tensor, action: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        mean, std = self.forward(state)
        dist = Normal(mean, std)
        log_prob = dist.log_prob(action).sum(dim=-1)
        entropy = dist.entropy().sum(dim=-1)
        return log_prob, entropy


class Critic(nn.Module):
    """State-Value function V(s): state (14) -> baseline value (1)."""

    def __init__(
        self,
        state_dim: int = STATE_DIM,
        hidden_dim: int = 128,
    ):
        super().__init__()
        self.net = nn.Sequential(
            layer_init(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, 1), std=1.0),
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        return self.net(state)


# ---------------------------------------------------------------------------
# Configuration and Agent
# ---------------------------------------------------------------------------


@dataclass
class PPOConfig:
    state_dim: int = STATE_DIM
    action_dim: int = ACTION_DIM
    hidden_dim: int = 128
    max_action: float = 5.0

    lr: float = 3e-4
    gamma: float = 0.99
    gae_lambda: float = 0.95
    clip_coef: float = 0.2
    ent_coef: float = 0.01
    vf_coef: float = 0.5
    max_grad_norm: float = 0.5

    n_epochs: int = 10
    batch_size: int = 64
    rollout_steps: int = 2048

    device: str = "cpu"


class PPOAgent:
    """
    Proximal Policy Optimization (PPO-Clip) Agent operating on latent
    action logits.
    """

    def __init__(self, config: Optional[PPOConfig] = None):
        self.config = config or PPOConfig()
        c = self.config
        self.device = torch.device(c.device)

        self.actor = Actor(c.state_dim, c.action_dim, c.hidden_dim, c.max_action).to(self.device)
        self.critic = Critic(c.state_dim, c.hidden_dim).to(self.device)

        self.optimizer = torch.optim.Adam(
            list(self.actor.parameters()) + list(self.critic.parameters()),
            lr=c.lr,
            eps=1e-5,
        )

        self._total_updates = 0

    # -- inference & rollouts ----------------------------------------------

    def select_action(self, state: np.ndarray, explore: bool = True) -> np.ndarray:
        """Return a single raw action vector for evaluation/testing."""
        state_t = torch.as_tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
        with torch.no_grad():
            action, _ = self.actor.get_action(state_t, deterministic=not explore)
        return action.cpu().numpy()[0].astype(np.float32)

    def step(self, state: np.ndarray) -> Tuple[np.ndarray, float, float]:
        """Perform action sampling with state-value estimation during rollouts."""
        state_t = torch.as_tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
        with torch.no_grad():
            action, log_prob = self.actor.get_action(state_t, deterministic=False)
            value = self.critic(state_t)

        return (
            action.cpu().numpy()[0].astype(np.float32),
            float(log_prob.cpu().item()),
            float(value.cpu().item()),
        )

    def get_value(self, state: np.ndarray) -> float:
        """Get baseline value estimate V(s) for bootstrapping terminal step."""
        state_t = torch.as_tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
        with torch.no_grad():
            value = self.critic(state_t)
        return float(value.cpu().item())

    # -- training -----------------------------------------------------------

    def train_step(self, buffer: RolloutBuffer) -> dict:
        """Update Actor and Critic networks across multiple epochs of mini-batches."""
        c = self.config

        policy_losses = []
        value_losses = []
        entropy_losses = []

        for _ in range(c.n_epochs):
            for batch in buffer.get_batches(c.batch_size):
                b_states = torch.as_tensor(batch["states"], dtype=torch.float32, device=self.device)
                b_actions = torch.as_tensor(batch["actions"], dtype=torch.float32, device=self.device)
                b_log_probs = torch.as_tensor(batch["log_probs"], dtype=torch.float32, device=self.device)
                b_returns = torch.as_tensor(batch["returns"], dtype=torch.float32, device=self.device)
                b_advantages = torch.as_tensor(batch["advantages"], dtype=torch.float32, device=self.device)

                # Evaluate actions under updated policy
                new_log_probs, entropy = self.actor.evaluate_action(b_states, b_actions)
                new_values = self.critic(b_states).squeeze(-1)

                # Policy Loss (PPO clipped surrogate)
                log_ratio = new_log_probs - b_log_probs
                ratio = torch.exp(log_ratio)

                surr1 = ratio * b_advantages
                surr2 = torch.clamp(ratio, 1.0 - c.clip_coef, 1.0 + c.clip_coef) * b_advantages
                policy_loss = -torch.min(surr1, surr2).mean()

                # Value Loss
                value_loss = 0.5 * ((new_values - b_returns) ** 2).mean()

                # Entropy Bonus
                entropy_loss = entropy.mean()

                # Total Loss
                loss = policy_loss - c.ent_coef * entropy_loss + c.vf_coef * value_loss

                self.optimizer.zero_grad()
                loss.backward()
                nn.utils.clip_grad_norm_(
                    list(self.actor.parameters()) + list(self.critic.parameters()),
                    c.max_grad_norm,
                )
                self.optimizer.step()

                policy_losses.append(policy_loss.item())
                value_losses.append(value_loss.item())
                entropy_losses.append(entropy_loss.item())

        self._total_updates += 1

        return {
            "policy_loss": float(np.mean(policy_losses)),
            "value_loss": float(np.mean(value_losses)),
            "entropy": float(np.mean(entropy_losses)),
            "total_updates": self._total_updates,
        }

    # -- persistence ------------------------------------------------------

    def state_dict(self) -> dict:
        """Return a picklable dict of network weights and optimizer state."""
        return {
            "actor": self.actor.state_dict(),
            "critic": self.critic.state_dict(),
            "optimizer": self.optimizer.state_dict(),
            "total_updates": self._total_updates,
        }

    def load_state_dict(self, state: dict) -> None:
        self.actor.load_state_dict(state["actor"])
        self.critic.load_state_dict(state["critic"])
        self.optimizer.load_state_dict(state["optimizer"])
        self._total_updates = state["total_updates"]