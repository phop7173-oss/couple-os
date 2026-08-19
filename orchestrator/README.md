# Couple OS Orchestrator

The Couple OS Orchestrator coordinates AI-assisted software development.

## Responsibilities

The Orchestrator:

1. receives an approved task
2. creates a task record
3. loads project instructions
4. determines the required development stages
5. invokes the appropriate AI development process
6. records results
7. runs verification
8. detects failures
9. requests another iteration when appropriate
10. produces a final report
11. stops for human decisions when required

## Authority Boundary

The Orchestrator does not have unrestricted authority.

It must not independently:

- change product direction
- deploy production
- spend money
- delete important data
- bypass security
- expose private information
- approve major product decisions

## Human Role

The Product Owner remains responsible for:

- product decisions
- real-world testing
- acceptance
- rejection
- prioritization

## Development Philosophy

The goal is not maximum autonomy.

The goal is maximum useful autonomous engineering while maintaining reliable verification and human control.
