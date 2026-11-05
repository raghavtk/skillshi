---
name: principle-test-behavior-not-implementation
description: Assess or write tests against observable contracts and independent expectations. Use when adding regressions, changing assertions, or checking whether tests survive refactoring.
---

# Test behavior, not implementation

Name the consumer, interface, promised behavior, and independent source for the expectation. Drive the executable/public boundary with a concrete input and assert the relevant return, error, state, external effect, or invariant.

Evaluate two edits: a broken contract should fail the test, while an internal refactor preserving that contract should pass. These counterfactuals expose weak assertions and internal coupling; use an actual before-fix reproduction when practical.

Expectations derived by the function under test, assertions on self-created fixtures, and source-text searches cannot establish unrelated runtime behavior. For configuration, invoke the actual consumer or assert semantic meaning. Exact bytes and snapshots are valid when the bytes themselves are a published contract.

Mock external boundaries when appropriate. An internal helper call is ordinarily not observable; an external payment or message can be. A no-effect assertion needs a positive case demonstrating that the observer detects the effect.

Pin wording, order, timing, and counts only when the contract requires them. Preserve useful coverage when replacing coupled tests. Choose necessary checks proportional to the change; do not generate tests merely to restate implementation details.

Adapted from pstack's [test behavior principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-test-behavior-not-implementation/SKILL.md).
