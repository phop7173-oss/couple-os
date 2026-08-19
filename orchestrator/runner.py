#!/usr/bin/env python3

from pathlib import Path
import json
import subprocess
import sys
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent

CONFIG_FILE = ROOT / "orchestrator" / "config.json"
PRODUCT_FILE = ROOT / "docs" / "PRODUCT.md"
TEAM_FILE = ROOT / "docs" / "ai" / "TEAM.md"
WORKFLOW_FILE = ROOT / "docs" / "ai" / "WORKFLOW.md"
TASK_CONTRACT_FILE = ROOT / "docs" / "ai" / "TASK_CONTRACT.md"


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    return path.read_text(encoding="utf-8")


def run_command(command: list[str]) -> str:
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    output = result.stdout.strip()

    if result.stderr.strip():
        output += "\n" + result.stderr.strip()

    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({result.returncode}): "
            f"{' '.join(command)}\n{output}"
        )

    return output


def load_config() -> dict:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_context(task_file: Path) -> str:
    task = read_file(task_file)
    product = read_file(PRODUCT_FILE)
    team = read_file(TEAM_FILE)
    workflow = read_file(WORKFLOW_FILE)
    contract = read_file(TASK_CONTRACT_FILE)

    git_status = run_command(["git", "status", "--short"])
    git_branch = run_command(
        ["git", "branch", "--show-current"]
    )
    git_log = run_command(
        ["git", "log", "--oneline", "--max-count=5"]
    )

    timestamp = datetime.now().isoformat(timespec="seconds")

    return f"""
# COUPLE OS — ORCHESTRATOR EXECUTION CONTEXT

Generated:
{timestamp}

Repository:
{ROOT}

Current branch:
{git_branch}

Current Git status:
{git_status or "(clean)"}

Recent commits:
{git_log}

---

# PRODUCT REQUIREMENTS

{product}

---

# AI TEAM CONTRACT

{team}

---

# AI WORKFLOW

{workflow}

---

# TASK CONTRACT

{contract}

---

# CURRENT TASK

{task}

---

# ORCHESTRATOR INSTRUCTION

This is an execution-context generation stage.

DO NOT modify application source code.

DO NOT modify product requirements.

DO NOT expand the task scope.

DO NOT claim implementation has been completed.

Analyze the task and repository context.

Prepare the information required for the next engineering stage.

The next stage will independently inspect the repository and create an implementation plan.

END OF EXECUTION CONTEXT
""".strip()


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python3 orchestrator/runner.py "
            "<task-file>"
        )
        return 1

    task_path = ROOT / sys.argv[1]

    if not task_path.exists():
        print(f"Task file not found: {task_path}")
        return 1

    try:
        config = load_config()

        if config.get("allow_autonomous_implementation") is not True:
            print("Autonomous implementation is disabled.")

        context = build_context(task_path)

        output_dir = ROOT / "reports"
        output_dir.mkdir(exist_ok=True)

        task_id = task_path.stem

        output_file = (
            output_dir /
            f"{task_id}-execution-context.md"
        )

        output_file.write_text(
            context,
            encoding="utf-8",
        )

        print("ORCHESTRATOR CONTEXT CREATED")
        print()
        print(f"Task: {task_id}")
        print(f"Context: {output_file.relative_to(ROOT)}")
        print()
        print("No application source code was modified.")
        print("Execution stopped before implementation.")

        return 0

    except Exception as error:
        print(f"ORCHESTRATOR ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
