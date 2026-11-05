---
name: code-review
description: Review a specified change or working tree for requirement fidelity, correctness, and documented standards. Report actionable, evidence-backed findings without requiring a PR or publishing comments.
---

# Code review

Pin scope first. Resolve any supplied base/reference. For branch work, record the merge base and commits; for working-tree work, include staged, unstaged, and relevant untracked files. If scope cannot be inferred safely, clarify it before claiming coverage.

Find the specification in the user's request, assignment, issue, or local design. Find repository standards and relevant callers/tests. Record missing sources; they limit conclusions rather than preventing every useful review.

Inspect two distinct axes:

- Spec and correctness: missing requirements, changed contracts, incorrect behavior, failure paths, ownership, lifetime, concurrency, and regressions.
- Standards and design: documented conventions and justified maintainability concerns. Treat design smells as hypotheses, not automatic violations; repository choices override generic preferences.

Trace suspicious code to a concrete trigger and consequence. Reproduce when useful and authorized. For each actionable finding, give severity, location, evidence, affected behavior, and the smallest reasonable correction. Distinguish confirmed defects, conditional risks, and questions. Avoid speculative findings, tool-enforced formatting noise, and mandatory abstraction for similar lines.

Keep the axes visible in the report. If no actionable findings remain, say so with coverage and verification gaps. Reviews may run sequentially or through authorized independent agents. Do not edit, commit, post comments, or start PR workflows unless requested.

Adapted from Matt Pocock's [two-axis code review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md), with local working-tree support and evidence-based defect review.
