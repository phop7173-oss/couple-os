#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")


def run_opencode(message: str, context_file: Path) -> str:
    command = [
        "opencode",
        "run",
        message,
        "-f",
        str(context_file),
        "--dir",
        str(ROOT),
        "--format",
        "default",
    ]

    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    output = result.stdout.strip()

    if result.stderr.strip():
        output += "\n\n[stderr]\n" + result.stderr.strip()

    if result.returncode != 0:
        raise RuntimeError(
            f"OpenCode exited with code {result.returncode}\n\n"
            f"{output}"
        )

    return output


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python3 orchestrator/opencode_bridge.py "
            "<task-file>"
        )
        return 1

    task_path = ROOT / sys.argv[1]

    if not task_path.exists():
        print(f"Task not found: {task_path}")
        return 1

    try:
        REPORTS.mkdir(exist_ok=True)

        task_id = task_path.stem
        task = read_file(task_path)

        context_file = (
            REPORTS / f"{task_id}-execution-context.md"
        )

        if not context_file.exists():
            print(
                "Execution context does not exist.\n"
                "Run the orchestrator runner first."
            )
            return 1

        prompt = f"""
You are the ANALYST / ARCHITECT stage of the Couple OS AI development team.

You are working inside the Couple OS repository.

THIS IS A PLANNING-ONLY STAGE.

You have permission to inspect the repository.

You DO NOT have permission to modify application source code.

You DO NOT have permission to modify product requirements.

You DO NOT have permission to install dependencies.

You DO NOT have permission to perform destructive operations.

Your task is to analyze the current repository and produce an implementation-ready technical plan.

The complete project execution context is attached to this message.

CURRENT TASK:

{task}

REQUIRED PROCESS:

1. Inspect the repository yourself.
2. Inspect the existing implementation relevant to this task.
3. Identify the current architecture.
4. Identify the smallest correct implementation.
5. Identify the exact files that are likely to change.
6. Identify API, backend, frontend, database, and realtime implications where applicable.
7. Identify edge cases.
8. Identify security and data-integrity concerns.
9. Identify the required automated tests.
10. Identify required manual verification.
11. Identify any Product Owner decisions that are still unclear.
12. Produce a structured implementation plan.

IMPORTANT:

Do not implement the feature.

Do not modify application source files.

Do not create migrations.

Do not install packages.

Do not change configuration.

Do not commit or push anything.

If the repository already contains partial implementation, analyze it accurately rather than assuming the feature is missing.

REQUIRED OUTPUT FORMAT:

# Analysis

Describe the relevant existing implementation.

# Current Architecture

Describe how the current system handles the relevant behavior.

# Proposed Solution

Describe the smallest appropriate solution.

# Files To Change

List files likely to be modified or created and explain why.

# Data Flow

Describe important state and data flow.

# API / Realtime

Describe relevant API or realtime changes.

# UI

Describe required user-facing behavior.

# Testing Plan

Describe automated and manual tests.

# Risks And Edge Cases

List important risks and edge cases.

# Scope Check

Explicitly list functionality that should NOT be implemented as part of this task.

# Human Decisions

List anything that requires Product Owner clarification.

If there are no required decisions, write:

No blocking Product Owner decisions identified.

# Implementation Sequence

Give an ordered implementation sequence.

# Verification Criteria

Define the evidence required before the implementation can be considered verified.

# Final Recommendation

State whether the task is ready for implementation.

Do not claim implementation has been completed.
""".strip()

        prompt_file = (
            REPORTS / f"{task_id}-planning-prompt.md"
        )

        prompt_file.write_text(
            prompt,
            encoding="utf-8",
        )

        print("OPENING OPENCODE PLANNING STAGE...")
        print()
        print("Mode: PLANNING ONLY")
        print(f"Task: {task_id}")
        print()

        output = run_opencode(
            prompt,
            context_file,
        )

        report_file = (
            REPORTS / f"{task_id}-opencode-plan.md"
        )

        report = f"""# {task_id} — OpenCode Planning Report

Generated:
{datetime.now().isoformat(timespec="seconds")}

Stage:
ANALYSIS / ARCHITECTURE

Mode:
PLANNING ONLY

## OpenCode Output

{output}

## Orchestrator Result

The OpenCode planning stage completed.

No implementation authority was granted by this bridge.

The implementation plan must be reviewed before the next stage.
"""

        report_file.write_text(
            report,
            encoding="utf-8",
        )

        print("OPEN_CODE PLANNING COMPLETE")
        print()
        print(
            f"Report: "
            f"{report_file.relative_to(ROOT)}"
        )
        print()
        print(
            "Implementation was not requested."
        )

        return 0

    except Exception as error:
        print(f"OPENCODE BRIDGE ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
