# Couple OS — AI Engineering Contract

## Mission

Couple OS is a real commercial product for couples.

The initial product wedge is **Movie Date**.

This repository must be developed as production software, not as an AI-generated demo.

The goal is to build software that real users genuinely want to use and are willing to pay for when the value justifies it.

---

# 1. Development hierarchy

When making decisions, follow this order:

1. Explicit product requirements
2. Acceptance criteria
3. Architecture decisions in `docs/DECISIONS.md`
4. Existing repository behavior and tests
5. Established engineering conventions
6. Agent judgment

Never silently override a higher-level requirement with personal preference.

---

# 2. Core agent rules

Before changing code:

- Inspect the repository.
- Read relevant documentation.
- Understand existing architecture.
- Identify affected components.
- Plan non-trivial changes before implementation.

During implementation:

- Make the smallest coherent change that satisfies the requirement.
- Do not rewrite unrelated code.
- Do not introduce unnecessary dependencies.
- Do not invent APIs, credentials, services, or requirements.
- Do not fabricate test results.
- Do not claim success without evidence.
- Preserve existing behavior unless the requirement explicitly changes it.

After implementation:

- Run relevant tests.
- Run relevant builds.
- Review the resulting diff.
- Check for regressions.
- Update documentation when behavior or architecture changes materially.
- Report exactly what was changed and what was verified.

---

# 3. Product discipline

Do not add features merely because they are technically interesting.

Every feature must have a reason to exist.

Before implementing a significant feature, identify:

- user problem
- target user
- expected value
- acceptance criteria
- dependencies
- risks
- testing requirements

Do not expand the MVP without explicit product approval.

Do not assume that "more features" means "better product."

---

# 4. Engineering principles

Prefer:

- simple architecture
- clear boundaries
- maintainable code
- strong typing
- testability
- observable behavior
- reliable error handling
- secure defaults
- official platform APIs
- mature and well-maintained libraries

Avoid:

- premature microservices
- unnecessary abstraction
- dependency proliferation
- duplicated business logic
- hidden state
- magic behavior
- speculative infrastructure
- temporary hacks presented as permanent solutions

---

# 5. Android principles

When Android development begins:

- Prefer official Android and Jetpack APIs.
- Follow modern Android architecture.
- Keep UI, state, domain logic, and data responsibilities clear.
- Support configuration changes appropriately.
- Handle lifecycle correctly.
- Consider offline and reconnection behavior where relevant.
- Test important user flows on a physical device.
- Do not assume emulator behavior represents all real devices.

---

# 6. Backend principles

Backend code must:

- validate external input
- authenticate users
- authorize access to resources
- handle errors explicitly
- avoid leaking sensitive information
- use safe database access patterns
- maintain clear API contracts
- be testable independently of the UI

Never bypass authorization merely to make development easier.

---

# 7. Security

Never commit:

- passwords
- API keys
- access tokens
- private keys
- production credentials
- personal secrets

Never weaken security controls to make a test pass.

Authentication and authorization must be treated as separate concerns.

Users must only be able to access resources they are authorized to access.

---

# 8. Testing

Testing is part of implementation, not an optional final step.

Use the appropriate level of testing:

- unit tests
- integration tests
- API tests
- database tests
- synchronization tests
- Android UI tests
- authentication tests
- failure/reconnection tests
- regression tests

Not every change requires every type of test.

The agent must choose appropriate coverage and explain significant omissions.

---

# 9. Definition of Done

A task is not complete merely because code was written.

A task is complete when applicable criteria are satisfied:

- [ ] Requirements implemented
- [ ] Acceptance criteria satisfied
- [ ] Existing relevant behavior preserved
- [ ] Appropriate tests added or updated
- [ ] Relevant tests pass
- [ ] Build succeeds
- [ ] Lint/static analysis passes where configured
- [ ] Security implications considered
- [ ] No known critical regression remains
- [ ] Documentation updated where necessary
- [ ] Git diff reviewed
- [ ] Final report contains evidence

---

# 10. Verification evidence

Agents must distinguish between:

**Verified**

and

**Not verified**

Never say:

> "Everything works."

unless appropriate verification was actually performed.

Reports should include commands executed and meaningful results.

Example:

```text
Verification:

./gradlew test
PASS

./gradlew lint
PASS

./gradlew assembleDebug
PASS
