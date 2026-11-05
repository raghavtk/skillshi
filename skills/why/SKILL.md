---
name: why
description: Investigate design rationale, tradeoffs, regressions, and historical thresholds through code history and supporting records. Distinguish documented intent, inference, and unresolved causes.
---

# Why

Anchor the question in a concrete decision, symbol, behavior, or change. Establish what needs explaining and the competing explanations worth distinguishing.

Trace introduction and subsequent changes through blame, logs, patches, and renames. Read substantive commits and available linked discussions. Search relevant requirements, design records, incidents, and measurements rather than assuming every source is accessible. A vague commit message proves a change occurred, not why it was chosen.

Classify evidence while reasoning:

- Explicit intent: cite the statement and its scope.
- Corroborated inference: connect independent clues and explain remaining uncertainty.
- Hypothesis: name what observation would distinguish it from alternatives.
- Unknown: state the searched sources and the missing evidence.

Current code establishes mechanics. A measured correlation does not alone establish cause. Preserve conflicting accounts and check the user's hypothesis against counterevidence. Do not substitute a reasonable modern rationale for undocumented history or write personal motives on someone's behalf.

Answer the question first, with citations near claims. For planned changes, identify constraints still worth preserving and assumptions that may have expired. Stop once the consequential explanations are supported or the remaining gaps are explicit. Read-only investigation authorizes no messages, publication, or unrelated changes.

Adapted from pstack's [why](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) and [confidence guide](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md).
