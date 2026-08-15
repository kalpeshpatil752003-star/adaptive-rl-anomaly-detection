"""
Small standalone test/demo for src/rl/trainer.py.

Run with:
    python tests/test_trainer.py
"""

import json
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.rl.state import STATE_DIM
from src.rl.action import ActionProjector
from src.rl.environment import AnomalyEnsembleEnv
from src.rl.agent import PPOAgent, PPOConfig
from src.rl.trainer import Trainer, TrainerConfig


def make_synthetic_states_and_labels(n: int, seed: int = 0):
    rng = np.random.default_rng(seed)
    scores = rng.uniform(0.0, 1.0, size=(n, 4)).astype(np.float32)
    disagreement = np.column_stack(
        [
            scores.mean(axis=1),
            scores.std(axis=1),
            scores.min(axis=1),
            scores.max(axis=1),
            scores.max(axis=1) - scores.min(axis=1),
        ]
    ).astype(np.float32)
    traffic = rng.exponential(scale=200.0, size=(n, 5)).astype(np.float32)
    states = np.concatenate([scores, disagreement, traffic], axis=1)
    # Attack label correlated with mean score -- a learnable signal so we
    # can sanity-check that training moves metrics in a sensible direction.
    y_true = (scores.mean(axis=1) + rng.normal(0, 0.1, size=n) > 0.5).astype(int)
    return states, y_true


def main():
    train_states, train_y = make_synthetic_states_and_labels(3000, seed=1)
    val_states, val_y = make_synthetic_states_and_labels(600, seed=2)

    train_env = AnomalyEnsembleEnv(
        states=train_states, y_true=train_y, threshold=0.5,
        action_projector=ActionProjector(method="softmax"),
        episode_length=300, shuffle=True, seed=10,
    )
    val_env = AnomalyEnsembleEnv(
        states=val_states, y_true=val_y, threshold=0.5,
        action_projector=ActionProjector(method="softmax"),
        episode_length=300, shuffle=False, seed=11,
    )

    agent_config = PPOConfig(rollout_steps=300, batch_size=64, n_epochs=4, lr=3e-4)
    agent = PPOAgent(agent_config)

    with tempfile.TemporaryDirectory() as tmpdir:
        checkpoint_dir = Path(tmpdir) / "checkpoints"
        log_path = Path(tmpdir) / "train_log.jsonl"

        trainer_config = TrainerConfig(
            total_timesteps=300 * 6,   # 6 rollouts/updates
            eval_every_updates=2,
            eval_episodes=1,
            checkpoint_dir=str(checkpoint_dir),
            checkpoint_every_updates=3,
            log_path=str(log_path),
            verbose=False,
            seed=123,
        )
        trainer = Trainer(agent, train_env, val_env, trainer_config)

        # 1. Trainer initializes cleanly and pre-creates checkpoint/log dirs.
        assert checkpoint_dir.exists()
        assert log_path.parent.exists()
        print("[OK] Trainer initialized, checkpoint/log directories created")

        # 2. collect_rollout() produces a correctly-sized, finished buffer.
        #    Use a throwaway trainer so this doesn't consume timesteps that
        #    `trainer` will need for the exact-update-count check below.
        scratch_trainer = Trainer(agent, train_env, val_env, trainer_config)
        buffer = scratch_trainer.collect_rollout()
        assert len(buffer) == agent_config.rollout_steps
        assert np.all(np.isfinite(buffer.advantages))
        assert np.all(np.isfinite(buffer.returns))
        print(f"[OK] collect_rollout() -> buffer size {len(buffer)}, finite GAE outputs")

        # 3. evaluate() on val_env returns the expected metric keys with sane ranges.
        val_metrics = trainer.evaluate(val_env, n_episodes=1)
        for key in ("mean_reward", "total_reward", "n_steps", "tp", "tn", "fp", "fn",
                    "precision", "recall", "f1"):
            assert key in val_metrics, f"missing key {key}"
        assert 0.0 <= val_metrics["precision"] <= 1.0
        assert 0.0 <= val_metrics["recall"] <= 1.0
        assert 0.0 <= val_metrics["f1"] <= 1.0
        assert val_metrics["n_steps"] == 300
        print(f"[OK] evaluate() metrics well-formed -> "
              f"f1={val_metrics['f1']:.3f}, precision={val_metrics['precision']:.3f}, "
              f"recall={val_metrics['recall']:.3f}, mean_reward={val_metrics['mean_reward']:+.3f}")
        if "roc_auc" in val_metrics:
            assert 0.0 <= val_metrics["roc_auc"] <= 1.0
            assert 0.0 <= val_metrics["pr_auc"] <= 1.0
            print(f"[OK] sklearn metrics present -> roc_auc={val_metrics['roc_auc']:.3f}, "
                  f"pr_auc={val_metrics['pr_auc']:.3f}")

        # 4. Full train() run.
        history = trainer.train()
        assert len(history) == 6, f"expected 6 updates, got {len(history)}"
        assert trainer._n_updates == 6
        assert trainer._n_timesteps == 300 * 6
        print(f"[OK] train() ran {len(history)} updates, "
              f"{trainer._n_timesteps} total timesteps")

        # 5. Validation metrics appear on every 2nd update (eval_every_updates=2).
        val_updates = [h["update"] for h in history if "val_mean_reward" in h]
        assert val_updates == [2, 4, 6], val_updates
        print(f"[OK] validation ran on the expected updates -> {val_updates}")

        # 6. Checkpointing: "best.pt" exists (val ran at least once), and
        #    periodic checkpoints exist at update 3 and 6 (checkpoint_every_updates=3).
        assert (checkpoint_dir / "best.pt").exists()
        assert (checkpoint_dir / "update_3.pt").exists()
        assert (checkpoint_dir / "update_6.pt").exists()
        print("[OK] best.pt and periodic checkpoints (update_3.pt, update_6.pt) were saved")

        # 7. Log file has one JSON line per update, each parseable.
        with open(log_path) as f:
            lines = f.readlines()
        assert len(lines) == 6
        parsed = [json.loads(line) for line in lines]
        assert all("policy_loss" in p and "train_mean_reward" in p for p in parsed)
        print(f"[OK] log file has {len(lines)} valid JSON-lines entries")

        # 8. load_checkpoint() restores agent weights (deterministic action matches).
        eval_state = val_env.reset()
        action_before = trainer.agent.select_action(eval_state, explore=False)

        fresh_agent = PPOAgent(agent_config)
        fresh_trainer = Trainer(fresh_agent, train_env, val_env, trainer_config)
        fresh_trainer.load_checkpoint(checkpoint_dir / "update_6.pt")
        action_after = fresh_trainer.agent.select_action(eval_state, explore=False)

        np.testing.assert_allclose(action_before, action_after, atol=1e-5)
        assert fresh_trainer._n_updates == 6
        assert fresh_trainer._n_timesteps == 300 * 6
        print("[OK] load_checkpoint() restores identical policy behavior and progress counters")

        # 9. best_val_reward is a real float and matches the max observed val mean_reward.
        observed_best = max(h["val_mean_reward"] for h in history if "val_mean_reward" in h)
        assert abs(trainer._best_val_reward - observed_best) < 1e-6
        print(f"[OK] best_val_reward ({trainer._best_val_reward:.4f}) matches "
              f"max observed validation reward")

    print("\nAll trainer.py checks passed.")


if __name__ == "__main__":
    main()