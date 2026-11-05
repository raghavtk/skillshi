---
name: teach
description: Explain a change or subsystem in plain language by combining current mechanics with evidence about its rationale. Use for 'teach me this' or 'help me understand this code'.
---

# Teach

Infer the reader's purpose and existing knowledge from the conversation. Choose the few concepts needed to answer their question. Explain the code; change it or create a persistent learning workspace only when the user requests that work.

Use [how](../how/SKILL.md) to trace present behavior and [why](../why/SKILL.md) to investigate consequential design choices. Follow those instructions directly when installed together. When either companion is unavailable, inspect entrypoints, callers, and tests for mechanics, and history or decision records for rationale. Scale the investigation to the question. Delegation is optional and requires authorization.

Keep explicit intent, corroborated inference, hypotheses, and unknowns distinct. Preserve the confidence of the rationale findings when simplifying their wording. Present-day behavior does not establish historical intent.

Start with a plain definition and the smallest complete answer. Build on it with a concrete input or user action, showing what changes, who owns the state, and what result follows. Explain concepts before naming their implementation details. Cite verified source locations where useful.

Use diagrams when they clarify an interaction. For a complicated flow, introduce parts progressively if that helps the reader follow it. Pick the available medium that fits the idea; an explanation needs no image-generation dependency.

Match the requested depth. In an interactive exchange, leave room for follow-up without quizzes or staged pauses. For a requested complete walkthrough, finish the walkthrough in one response. Use [unslop](../unslop/SKILL.md) when available to edit the explanation, preserving evidence and uncertainty. Otherwise use complete sentences, concrete mechanisms, consistent terms, and plain language.

Return the explanation itself. Finish when the reader can predict the main behavior and understand the supported reasons for its design, with evidence gaps clear.

Adapted from Lauren Tan's pstack [teach](https://github.com/cursor/plugins/blob/main/pstack/skills/teach/SKILL.md). Matt Pocock's [teach](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) was considered as a distinct learning-workspace workflow; this skill keeps the existing code-explanation scope.
