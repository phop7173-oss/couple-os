#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
from datetime import datetime


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"


REQUIRED_SECTIONS = [
    "# Analysis",
    "# Current Architecture",
    "# Proposed Architecture",
    "# Technology Decisions",
    "# Repository Structure",
    "# Data Architecture",
    "# Realtime Architecture",
    "# Media Architecture",
    "# Security Architecture",
    "# Testing Architecture",
    "# Development Environment",
    "# Deployment Strategy",
    "# Risks And Tradeoffs",
    "# Implementation Sequence",
    "# Verification Criteria",
    "# Human Decisions",
    "# Final Recommendation",
]


def read_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")


def run_opencode(message: str, context_file: Path) -> tuple[int, str]:
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

    return result.returncode, output


def validate_plan(output: str) -> list[str]:
    missing = []

    for section in REQUIRED_SECTIONS:
        if section not in output:
            missing.append(section)

    return missing


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

TASK:
{task}

The complete project execution context is attached to this message.

MODE: PLANNING ONLY

You may inspect the repository.

You must NOT:
- modify application source code
- create application files
- modify product requirements
- install dependencies
- modify configuration
- create database migrations
- commit
- push
- deploy
- perform destructive operations

IMPORTANT OUTPUT RULE:

Your final response MUST be a plain-text Markdown architecture document.

Do NOT use repository write tools to create the report.

Do NOT create a report file yourself.

Do NOT return JSON.

Do NOT return tool-call output as the final answer.

After inspecting the repository, return ONLY the final architecture document.

The final document MUST contain ALL of these headings exactly:

# Analysis

# Current Architecture

# Proposed Architecture

# Technology Decisions

# Repository Structure

# Data Architecture

# Realtime Architecture

# Media Architecture

# Security Architecture

# Testing Architecture

# Development Environment

# Deployment Strategy

# Risks And Tradeoffs

# Implementation Sequence

# Verification Criteria

# Human Decisions

# Final Recommendation

Under each heading provide useful technical content.

IMPORTANT:

There is currently no application source code.

Do not pretend an application exists.

If a requested capability cannot yet be implemented because the foundation does not exist, explicitly say so.

The architecture must prioritize the real Couple OS product and its Movie Date experience.

Do not over-engineer.

Do not select technologies merely because they are common in AI-generated applications.

Consider cost, maintainability, realtime requirements, media handling, security, mobile experience, testing, and the current development environment.

The final recommendation must clearly state whether the architecture is ready for implementation.
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

        return_code, output = run_opencode(
            prompt,
            context_file,
        )

        report_file = (
            REPORTS / f"{task_id}-opencode-plan.md"
        )

        missing_sections = validate_plan(output)

        if return_code != 0:
            status = "FAILED"
            reason = (
                f"OpenCode exited with code {return_code}."
            )
        elif missing_sections:
            status = "FAILED"
            reason = (
                "Required architecture sections are missing."
            )
        else:
            status = "PASSED"
            reason = (
                "Required architecture sections were found."
            )

        report = f"""# {task_id} — OpenCode Planning Report

Generated:
{datetime.now().isoformat(timespec="seconds")}

Stage:
ANALYSIS / ARCHITECTURE

Mode:
PLANNING ONLY

Status:
{status}

Validation:
{reason}

"""

        if missing_sections:
            report += "Missing sections:\n\n"

            for section in missing_sections:
                report += f"- {section}\n"

            report += "\n"

        report += f"""## OpenCode Final Output

{output}

## Orchestrator Decision

Planning status: {status}

Implementation authority:
DENIED

Application source code was not authorized for modification by this stage.
"""

        report_file.write_text(
            report,
            encoding="utf-8",
        )

        print()
        print(f"PLANNING STATUS: {status}")
        print(
            f"Report: "
            f"{report_file.relative_to(ROOT)}"
        )

        if missing_sections:
            print()
            print("Missing required sections:")

            for section in missing_sections:
                print(f"- {section}")

        print()
        print("Implementation authority: DENIED")

        return 0 if status == "PASSED" else 2

    except Exception as error:
        print(f"OPENCODE BRIDGE ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
