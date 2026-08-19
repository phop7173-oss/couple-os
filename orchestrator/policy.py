#!/usr/bin/env python3

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent
POLICY_FILE = ROOT / "orchestrator" / "policy.json"


class PolicyError(Exception):
    pass


def load_policy() -> dict:
    if not POLICY_FILE.exists():
        raise PolicyError(
            f"Policy file not found: {POLICY_FILE}"
        )

    with POLICY_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def get_mode_policy(mode: str) -> dict:
    policy = load_policy()

    if mode not in policy:
        raise PolicyError(
            f"Unknown execution mode: {mode}"
        )

    return policy[mode]


def allowed(mode: str, capability: str) -> bool:
    mode_policy = get_mode_policy(mode)

    return bool(
        mode_policy.get(capability, False)
    )


def require(mode: str, capability: str) -> None:
    if not allowed(mode, capability):
        raise PolicyError(
            f"Policy denied capability "
            f"'{capability}' in mode '{mode}'."
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print(
            "Usage: python3 orchestrator/policy.py "
            "<mode> <capability>"
        )
        raise SystemExit(1)

    mode = sys.argv[1]
    capability = sys.argv[2]

    try:
        require(mode, capability)
        print("ALLOWED")
    except PolicyError as error:
        print(f"DENIED: {error}")
        raise SystemExit(2)
