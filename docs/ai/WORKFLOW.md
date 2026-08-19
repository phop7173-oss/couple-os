# Couple OS — AI Development Workflow

## 1. Purpose

This document defines how the Couple OS AI development team executes software-development tasks.

The workflow exists to make AI-assisted development:

- repeatable
- auditable
- testable
- efficient
- safe
- production-oriented

The system must reduce repetitive human work without removing human product judgment.

The Product Owner remains the final authority over product decisions and release acceptance.

---

## 2. Core Development Loop

Every significant development task follows this lifecycle:

INTAKE
↓
ANALYZE
↓
PLAN
↓
IMPLEMENT
↓
TEST
↓
REVIEW
↓
FIX
↓
VERIFY
↓
REPORT
↓
HUMAN ACCEPTANCE

A task may repeat the TEST → REVIEW → FIX → VERIFY cycle as many times as necessary.

A task must not be marked complete merely because implementation finished.

---

## 3. Task Intake

A task enters the system from one of these sources:

### Product Owner

The Product Owner directly requests a feature, improvement, bug fix, investigation, or technical change.

### Development Team

An agent may identify:

- a bug
- a security problem
- a regression
- missing tests
- technical debt
- an architectural risk

The agent must report the issue instead of silently expanding the task.

### Automated Detection

Automation may detect:

- failed tests
- failed builds
- dependency problems
- CI failures
- runtime failures
- monitoring problems

Automated findings become tasks only when enough information exists to reproduce or investigate them.

---

## 4. Task Classification

Every task must be classified before implementation.

Possible categories:

- FEATURE
- BUG
- REFACTOR
- SECURITY
- PERFORMANCE
- TEST
- DOCUMENTATION
- INVESTIGATION
- INFRASTRUCTURE

The category determines which agents are required.

---

## 5. Task Priority

Tasks use:

- P0 — critical production failure
- P1 — major user-impacting problem
- P2 — important product or engineering work
- P3 — useful improvement
- P4 — optional improvement

P0 and P1 work may interrupt normal feature development when justified.

---

## 6. Orchestrator Responsibilities

The Orchestrator controls task progression.

It must:

1. receive the task
2. identify the task category
3. inspect repository state
4. load relevant product requirements
5. identify dependencies
6. identify required agents
7. create or update the task record
8. start the appropriate workflow
9. collect agent reports
10. detect failures
11. trigger appropriate follow-up work
12. prevent unauthorized scope expansion
13. require evidence before verification
14. stop when human judgment is required
15. produce the final task report

The Orchestrator coordinates the team.

It does not replace the Product Owner.

---

## 7. Repository Inspection

Before implementation, the responsible agent must inspect the current repository.

At minimum, inspect:

- repository structure
- relevant source files
- package configuration
- existing tests
- existing documentation
- current Git status
- relevant recent commits
- existing architecture

Agents must not assume that the repository is empty or that previous work does not exist.

---

## 8. Requirement Loading

Before planning, the team should load the relevant project specifications.

Important sources include:

- AGENTS.md
- docs/PRODUCT.md
- docs/MVP.md when present
- docs/ai/TEAM.md
- docs/ai/WORKFLOW.md
- relevant architecture documents
- relevant task records

More specific requirements take precedence over general assumptions.

If requirements conflict or are ambiguous, the task must stop for clarification when the ambiguity could materially change the implementation.

---

## 9. Analysis Stage

The Product Analyst determines:

- what problem is being solved
- who is affected
- expected behavior
- acceptance criteria
- dependencies
- edge cases
- risks
- affected areas of the repository

The output must be an implementation-ready task brief.

The analyst must not invent product requirements.

---

## 10. Planning Stage

The Architect converts the approved requirement into a technical plan.

The plan should identify:

- affected components
- data flow
- API changes
- database changes
- UI changes
- realtime changes
- security implications
- testing strategy
- migration requirements
- rollback considerations when relevant

The plan should minimize unnecessary complexity.

The team should prefer existing project capabilities before introducing new infrastructure or dependencies.

---

## 11. Implementation Stage

The Implementation Engineer:

- follows the approved plan
- follows repository conventions
- makes focused changes
- writes maintainable code
- adds appropriate tests
- preserves existing functionality
- avoids unrelated rewrites
- avoids unnecessary dependencies

The implementation engineer must not silently change product scope.

If implementation reveals a major requirement problem, stop and report it.

---

## 12. Testing Stage

Testing must be proportional to the change.

Possible verification levels:

### Level 1 — Static Verification

Examples:

- formatting
- linting
- type checking
- static analysis

### Level 2 — Unit Testing

Test isolated logic and components.

### Level 3 — Integration Testing

Test interactions between components and services.

### Level 4 — End-to-End Testing

Test realistic user flows.

### Level 5 — Real Device Testing

Required when behavior depends on:

- mobile UI
- device hardware
- networking
- playback
- permissions
- platform-specific behavior

### Level 6 — Human Testing

Required for final product acceptance.

---

## 13. Verification Evidence

Agents must distinguish between:

VERIFIED
NOT VERIFIED
BLOCKED

VERIFIED means relevant evidence was actually obtained.

NOT VERIFIED means the agent did not perform the required verification.

BLOCKED means verification could not be performed because of an external or unresolved condition.

Agents must never claim a test passed without evidence.

---

## 14. Review Stage

The Code Reviewer evaluates:

- correctness
- maintainability
- architecture
- error handling
- test coverage
- regression risk
- unnecessary complexity
- consistency with repository conventions

The Security Reviewer is required when a task affects:

- authentication
- authorization
- personal information
- couple data
- external input
- secrets
- payments
- file handling
- networking
- access control

---

## 15. Failure Loop

If tests or reviews fail:

TEST FAILURE
↓
IDENTIFY FAILURE
↓
CLASSIFY CAUSE
↓
CREATE FIX TASK
↓
IMPLEMENT FIX
↓
RETEST
↓
REVIEW
↓
VERIFY

Possible failure causes:

- implementation defect
- incorrect assumption
- requirement ambiguity
- environment problem
- infrastructure problem
- dependency problem
- test defect

The team must identify the cause before claiming resolution.

---

## 16. Scope Expansion Rule

During implementation, an agent may discover additional work.

Additional work must be classified as:

### Required

Necessary to complete the approved task safely.

This may be included in the current task.

### Recommended

Useful but not required.

Create a follow-up task.

### Unrelated

Outside the current objective.

Do not implement it.

This rule prevents autonomous agents from continuously expanding the project.

---

## 17. Human Decision Gate

The workflow must stop and request the Product Owner when:

- product requirements conflict
- a major product decision is required
- architecture choices have significant long-term consequences
- implementation would materially change the user experience
- privacy implications are unclear
- security risk is significant
- the task requires a business decision
- the agent cannot safely infer the intended behavior

The system must not guess when the decision materially affects the product.

---

## 18. Human Feedback Loop

After AI verification, the Product Owner may test the product.

The Product Owner can respond with:

### ACCEPT

The task is accepted.

### CHANGE

The Product Owner wants a modification.

The feedback becomes the next task or iteration.

### REJECT

The implementation does not meet the intended product goal.

The task returns to analysis.

### BLOCK

The Product Owner cannot currently evaluate or proceed.

The task remains blocked.

---

## 19. Completion Definition

A development task is considered AI-complete only when:

- implementation is complete
- required tests have been executed
- required reviews are complete
- known failures are resolved or explicitly accepted
- relevant documentation is updated
- Git state is understood
- the final report is produced

AI-complete does not automatically mean product-accepted.

Final product completion requires:

AI VERIFIED
↓
HUMAN REVIEW
↓
HUMAN ACCEPTED

---

## 20. Git Discipline

Agents must understand the repository state before and after their work.

Before implementation:

- inspect git status
- inspect relevant history

After implementation:

- inspect changed files
- inspect diff
- run appropriate verification
- ensure unrelated files were not modified

Agents must not overwrite unrelated human work.

Commit strategy must follow the repository's established engineering contract.

The Orchestrator must never assume that a change was pushed successfully without evidence.

---

## 21. Overnight / Autonomous Work

Autonomous work may continue without the Product Owner when the task is already approved and bounded.

Autonomous agents may:

- inspect
- implement
- test
- review
- fix
- repeat the verification cycle

They must stop when:

- requirements become ambiguous
- a major product decision is required
- a security-sensitive decision cannot be safely inferred
- destructive action is proposed
- the task exceeds approved scope
- required credentials or external services are unavailable
- verification cannot establish correctness

The agent must leave a clear report describing the stopping condition.

---

## 22. Autonomous Safety Boundary

The AI team must not independently:

- publish a product
- spend money
- purchase services
- expose private user data
- delete important production data
- change core product direction
- create deceptive user experiences
- bypass security controls
- weaken authentication
- remove required safety mechanisms

These actions require explicit authorization.

---

## 23. Task Handoff Contract

Every handoff must contain:

### Task

What is being worked on.

### Objective

What outcome is required.

### Context

Relevant product and technical information.

### Work Performed

What the current agent actually did.

### Files Changed

Exact files modified.

### Tests

Commands or procedures executed.

### Results

Actual results.

### Decisions

Technical or product decisions made.

### Limitations

Known limitations or unverified behavior.

### Next Step

The recommended next action.

---

## 24. Final Report

The final Orchestrator report must contain:

- task identifier
- task objective
- final status
- files changed
- implementation summary
- tests executed
- verification evidence
- review findings
- unresolved issues
- known limitations
- recommended human test procedure
- recommended next task

The report must clearly distinguish:

AI VERIFIED

from:

HUMAN ACCEPTED

---

## 25. State Machine

The standard task state machine is:

BACKLOG
↓
APPROVED
↓
ANALYZING
↓
PLANNED
↓
IMPLEMENTING
↓
TESTING
↓
REVIEWING
↓
FIXING
↓
VERIFYING
↓
HUMAN_REVIEW
↓
ACCEPTED

Alternative exits:

ANALYZING → BLOCKED

PLANNED → BLOCKED

IMPLEMENTING → BLOCKED

TESTING → FIXING

REVIEWING → FIXING

VERIFYING → FIXING

HUMAN_REVIEW → CHANGE

HUMAN_REVIEW → REJECTED

---

## 26. Core Operating Principle

The Orchestrator should maximize useful autonomous development while minimizing unnecessary human intervention.

The desired operating model is:

Human defines the goal.
AI analyzes the work.
AI plans the solution.
AI builds.
AI tests.
AI reviews.
AI fixes.
AI verifies.
AI reports.
Human tests the product.
Human decides.
AI continues.

The objective is not maximum autonomy.

The objective is maximum useful output with reliable quality and human control.
