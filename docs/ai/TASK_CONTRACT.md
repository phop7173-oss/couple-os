# Couple OS — AI Task Contract

## 1. Purpose

This document defines the standard machine-readable and human-readable structure used by the Couple OS AI development workflow.

Every significant engineering task should have a task record.

The task record allows the Orchestrator and development agents to share a consistent understanding of:

- what must be built
- why it must be built
- what is in scope
- what is out of scope
- what evidence is required
- what has already been completed
- what remains unresolved

---

## 2. Task Identity

Every task must have:

- unique task ID
- title
- category
- priority
- current state
- creation date
- originating request

Example:

Task ID:

COUPLE-001

Title:

Movie Date shared readiness

Category:

FEATURE

Priority:

P1

State:

APPROVED

---

## 3. Task Structure

A task record should contain these sections:

### Identity

- task_id
- title
- category
- priority
- state

### Objective

A concise description of the desired outcome.

### User Problem

The user problem being solved.

### Product Context

Relevant product requirements.

### Scope

What the task includes.

### Non-Scope

What the task explicitly does not include.

### Acceptance Criteria

Specific conditions that must be satisfied.

### Technical Context

Relevant repository and architecture information.

### Dependencies

Other systems, tasks, libraries, services, or decisions required.

### Risks

Known technical, product, security, privacy, or operational risks.

### Verification Plan

How the task will be tested.

### Handoff History

Record of work performed by each agent.

### Final Result

Final implementation and verification status.

---

## 4. Objective

The objective must describe the outcome, not merely the implementation.

Weak:

"Create a WebSocket handler."

Better:

"Allow both partners in a Movie Date to see the same readiness state in real time."

The task should be understandable from a user and product perspective.

---

## 5. User Problem

Every product-facing task should explain the user problem.

Example:

"Partners need to know whether both people have finished preparing before the Movie Date can start."

This prevents implementation from becoming disconnected from user value.

---

## 6. Scope

Scope defines exactly what the task may change.

Example:

IN SCOPE:

- readiness state
- readiness API
- realtime readiness events
- readiness UI
- readiness tests

OUT OF SCOPE:

- movie playback synchronization
- chat
- reactions
- character animations
- recommendation systems

Agents must not silently expand the task beyond its defined scope.

---

## 7. Acceptance Criteria

Acceptance criteria must be observable.

Good acceptance criteria:

- Partner A can mark themselves ready.
- Partner B can mark themselves ready.
- Both clients receive updated readiness state.
- Movie start remains unavailable until both partners are ready.
- Refreshing the page does not incorrectly reset persisted readiness state.
- Disconnect/reconnect does not create inconsistent readiness state.

Bad acceptance criteria:

- "Make readiness work well."
- "Make it fast."
- "Make the UI nice."

When possible, acceptance criteria should be testable.

---

## 8. Technical Context

Technical context should include only information relevant to the task.

Possible information:

- existing architecture
- relevant source files
- database models
- API endpoints
- realtime events
- frontend components
- existing tests
- dependencies

Agents must inspect the repository instead of trusting stale assumptions.

---

## 9. Dependencies

Dependencies may include:

- another task
- database migration
- authentication
- realtime infrastructure
- external service
- library
- product decision

If a dependency is unresolved, the task may become BLOCKED.

---

## 10. Risk Classification

Each task should identify relevant risks.

Possible categories:

### LOW

Limited local change with low regression risk.

### MEDIUM

Multiple components or shared behavior affected.

### HIGH

Security, privacy, data integrity, authentication, realtime consistency, payments, or major architecture affected.

### CRITICAL

Potential production-wide failure, severe security issue, destructive operation, or major data loss.

High and Critical tasks require stronger verification.

---

## 11. Agent Handoff

Each agent must append a handoff record.

Format:

Agent:

ROLE

Started:

TIMESTAMP

Completed:

TIMESTAMP

State:

STATE

Work performed:

DESCRIPTION

Files changed:

LIST

Tests executed:

LIST

Results:

RESULT

Problems:

LIST

Decisions:

LIST

Next recommendation:

DESCRIPTION

---

## 12. Agent Output Contract

Every agent must return a structured result containing:

STATUS

One of:

- COMPLETE
- PARTIAL
- BLOCKED
- FAILED

SUMMARY

Short explanation of what happened.

CHANGES

Files or systems changed.

TESTS

Tests or verification performed.

EVIDENCE

Actual evidence supporting the result.

ISSUES

Known problems.

NEXT_STEP

Recommended next action.

---

## 13. Evidence Requirements

Evidence should be concrete whenever possible.

Examples:

- command executed
- test output
- build output
- screenshot
- log
- API response
- reproducible behavior
- code inspection result

The agent must not replace evidence with confidence.

For example:

"Should work"

is not verification.

"npm test completed with 42 passing tests"

is evidence.

---

## 14. Status Rules

### COMPLETE

The agent completed its assigned responsibility and required verification for that stage.

### PARTIAL

Some work was completed but the stage is not fully finished.

### BLOCKED

The agent cannot continue without an external decision, dependency, credential, environment fix, or clarification.

### FAILED

The agent attempted the task but could not complete it due to an implementation or process failure.

---

## 15. State Transition Rules

Only valid transitions should be allowed.

APPROVED
→ ANALYZING

ANALYZING
→ PLANNED

ANALYZING
→ BLOCKED

PLANNED
→ IMPLEMENTING

PLANNED
→ BLOCKED

IMPLEMENTING
→ TESTING

IMPLEMENTING
→ BLOCKED

TESTING
→ REVIEWING

TESTING
→ FIXING

REVIEWING
→ VERIFYING

REVIEWING
→ FIXING

FIXING
→ TESTING

VERIFYING
→ HUMAN_REVIEW

VERIFYING
→ FIXING

HUMAN_REVIEW
→ ACCEPTED

HUMAN_REVIEW
→ CHANGE

HUMAN_REVIEW
→ REJECTED

CHANGE
→ ANALYZING

---

## 16. Human Feedback Contract

When the Product Owner tests the result, the feedback should contain:

### Result

- ACCEPT
- CHANGE
- REJECT
- BLOCK

### What Was Tested

Describe the real-world scenario.

### Expected Behavior

What should have happened.

### Actual Behavior

What actually happened.

### Severity

- LOW
- MEDIUM
- HIGH
- CRITICAL

### Additional Notes

Any useful observations.

This feedback becomes the next source of truth for iteration.

---

## 17. Orchestrator Decision Rules

The Orchestrator should automatically continue when:

- the next stage is unambiguous
- required inputs exist
- the current stage passed
- no human decision is required

The Orchestrator must stop when:

- requirements conflict
- product direction is unclear
- security risk requires human approval
- destructive action is proposed
- scope materially changes
- required external access is unavailable
- verification cannot establish correctness

---

## 18. Task Completion

A task is not complete simply because code exists.

The minimum completion sequence is:

IMPLEMENTED
→ TESTED
→ REVIEWED
→ VERIFIED
→ REPORTED
→ HUMAN ACCEPTED

For internal technical tasks that do not require human product testing, the Orchestrator may mark the task VERIFIED after appropriate engineering verification.

For user-facing product changes, HUMAN ACCEPTED remains the final state.

---

## 19. Example Task

Task ID:

COUPLE-001

Title:

Movie Date shared readiness

Category:

FEATURE

Priority:

P1

Objective:

Allow two connected partners to prepare for a Movie Date and prevent the movie from starting until both partners are ready.

User Problem:

Partners need a reliable way to know whether both people are ready before starting their shared Movie Date.

Scope:

- readiness state
- readiness persistence
- realtime readiness synchronization
- readiness UI
- readiness tests
- start-button gating

Non-Scope:

- movie playback synchronization
- chat
- reactions
- character animation

Acceptance Criteria:

1. Partner A can become ready.
2. Partner B can become ready.
3. Both clients receive the updated readiness state.
4. The Movie Date cannot start until both partners are ready.
5. The UI clearly communicates the current readiness state.
6. Refresh and reconnect behavior does not create inconsistent shared state.
7. Automated tests cover the core readiness behavior.
8. End-to-end verification confirms the complete flow.

Verification:

- unit tests where appropriate
- integration tests
- realtime tests
- end-to-end test
- manual real-device verification

Final State:

HUMAN_REVIEW

---

## 20. Principle

The task contract exists to prevent ambiguity.

Every agent should know:

WHAT am I doing?

WHY am I doing it?

WHAT am I allowed to change?

WHAT must be true when I finish?

HOW will I prove it?

WHAT should happen next?

The Orchestrator uses this contract to move work between agents reliably.
