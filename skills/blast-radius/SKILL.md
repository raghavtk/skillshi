---
name: blast-radius
description: Assess what a specific change could break beyond its diff, trace downstream contracts, and test the assumptions its safety depends on. Use for 'blast radius', 'what could this break', or focused change-impact analysis.
---

# Blast radius

Establish the change and comparison point. For branch work, resolve the base and merge base; for working-tree work, include staged, unstaged, and relevant untracked files. For a proposed change, state the assumed behavior and distinguish predictions from an executable implementation. Read the affected code, callers, tests, and applicable contracts before claiming coverage.

Explain what changes semantically, including consequences the diff does not spell out. Trace beyond direct callers into persisted data, serialization, cross-language consumers, configuration, feature flags, and downstream operations when relevant. For library behavior, inspect the version actually shipped and any local patches. Check ordering, asynchronous work, teardown, and resource ownership where they affect the outcome. A search with no matches limits the known consumers; it does not prove none exist.

Identify the few consequential facts that safety depends on, such as whether cache eviction can remove live entries or trigger callbacks. Focus investigation on those assumptions. Do not force a wide change into a single safety claim or treat proving one fact as proving the entire change safe.

For each important assumption, trace a concrete failure case and run the smallest useful check against the real code or shipped dependency when feasible. Prefer an existing test or a temporary reproducer with assertions that fail if the assumption is wrong. Exercise the relevant operation, timing, and configuration; a mock restating the assumption does not verify it. If the implementation does not exist yet, test relevant current behavior and mark the proposed behavior unproven.

Keep probes isolated from production state, shared services, and real external effects. Use temporary fixtures and owned resources. Assessment permits investigation and appropriately scoped checks; persistent fixes, commits, publication, or live mutations need authorization for those actions. If execution is unavailable or would exceed that scope, explain the limit and provide the smallest next verification step rather than claiming proof.

Report evidence at its actual level: source inspection, a traced failure path, an executed check, or reproduction in the running application. Include verified file locations and, for execution, the command, meaningful result, and tested conditions. An existing test is not a fresh passing run. State what each check establishes and what remains unproven.

Separate confirmed breakage, plausible unresolved risks, and checked cases that were cleared. Each material risk needs a trigger, an affected consumer or contract, a consequence, and supporting evidence. Describe likelihood and impact qualitatively from the known conditions; avoid invented probabilities or speculative inventories. Preserve uncertainty when history or external consumers are inaccessible.

Return a concise account of the semantic change, its safety assumptions and evidence, material downstream risks, cleared cases, and the cheapest remaining checks before adoption or merge. Use available how, why, or unslop guidance when useful; this workflow does not require those skills, an arena, or delegation. Finish when consequential assumptions have been tested or explicitly marked unproven, and the coverage limits are clear.

Adapted from Lauren Tan's pstack [blast-radius](https://github.com/cursor/plugins/blob/main/pstack/skills/blast-radius/SKILL.md), retaining downstream investigation and executable verification with explicit scope and evidence handling.
