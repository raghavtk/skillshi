---
name: how
description: Explain current code behavior, runtime flow, state ownership, and change locations from source and tests. Use for walkthroughs and subsystem understanding; investigate historical intent with why.
---

# How

Resolve the user's concrete operation and scope. Start at its executable or public entrypoint, then follow the calls and data that determine the result. Read callers and tests as well as the defining function.

Build a compact model covering inputs, state owners, transformations, outputs, and relevant external boundaries. Include timing, thread/process ownership, cleanup, and failure paths when they change behavior. Separate logical/world state from presentation or transport representations where that distinction matters.

Explain the main path before exceptional branches. Cite verified files, symbols, and locations. Describe an actual usage example or trace when it helps the reader predict behavior. A dependency diagram is useful only when it resolves an interaction that prose obscures.

Check competing accounts against the implementation. State whether a claim comes from source inspection, a test's assertions, or an executed check; an existing test file is not a fresh passing run. For dynamic configuration or dispatch, identify what selects the path and what remains unverified.

Finish when the reader can explain the operation's outcome and identify the owner of a relevant change. Use history to answer motivation through why; present-day mechanics alone do not establish the author's reasons. Scale depth to the question and delegate only when authorized.

Adapted from pstack's [how](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md) and [explainer guide](https://github.com/cursor/plugins/blob/main/pstack/skills/how/references/explainer-prompt.md).
