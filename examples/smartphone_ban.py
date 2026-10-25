#!/usr/bin/env python3
"""Worked example for the Nyx README: 'Should we ban smartphones in
schools?' — 6 agents, seed 42, 8 rounds.

Run from the repository root:  python examples/smartphone_ban.py
Prints the world metrics per round, the final outcome vector, and the
final agent states as JSON. Deterministic: the same seed always gives
the same numbers (see docs/demo.gif for the animated version).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "public"))

from nyx_kernel import run_simulation  # noqa: E402

SCENARIO = {
    "question": "Should we ban smartphones in schools?",
    "agents": [
        {"name": "Maya", "role": "Student",
         "initial_state": {"self_worth": 0.6, "anxiety": 0.4, "consistency": 0.7}},
        {"name": "Mr. Rao", "role": "Teacher",
         "initial_state": {"self_worth": 0.7, "anxiety": 0.2, "consistency": 0.8}},
        {"name": "Mrs. Khan", "role": "Parent",
         "initial_state": {"self_worth": 0.5, "anxiety": 0.6, "consistency": 0.5}},
        {"name": "Principal", "role": "Principal",
         "initial_state": {"self_worth": 0.8, "anxiety": 0.2, "consistency": 0.6}},
        {"name": "Dev", "role": "Student",
         "initial_state": {"self_worth": 0.4, "anxiety": 0.7, "consistency": 0.4}},
        {"name": "Dr. Iyer", "role": "Researcher",
         "initial_state": {"self_worth": 0.7, "anxiety": 0.3, "consistency": 0.9}},
    ],
    "influence_network": {
        "Principal": {"Mr. Rao": 0.8, "Mrs. Khan": 0.6},
        "Mr. Rao": {"Maya": 0.5, "Dev": 0.5},
        "Dr. Iyer": {"Principal": 0.7, "Mrs. Khan": 0.4},
        "Mrs. Khan": {"Principal": 0.5},
        "Maya": {"Dev": 0.6},
        "Dev": {"Maya": 0.4},
    },
}


def main():
    result = run_simulation(SCENARIO, rounds=8, seed=42)
    print(json.dumps({"question": SCENARIO["question"], **result}, indent=2))


if __name__ == "__main__":
    main()
