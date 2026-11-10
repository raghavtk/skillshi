---
name: improve-codebase-architecture
description: Scan an existing codebase for evidence-backed architectural improvements, especially shallow modules, scattered caller coordination, and unclear state ownership. Rank refactoring candidates and develop a selected design; implement only when requested.
---

# Improve codebase architecture

Establish whether the user wants opportunities, a detailed design, implementation, or a combination. Prefer a named subsystem or pain point. Otherwise use recent history to identify areas with repeated changes, then inspect their callers and tests. A small, coherent codebase may have no worthwhile candidate.

Read applicable repository guidance, domain terminology, and architectural decisions when present. Missing glossaries or decision records are evidence gaps, not reasons to create new files automatically.

## Find and compare opportunities

Look for concrete friction: one change scattered across many modules, callers coordinating internal stages, duplicated ownership of an invariant, abstractions that expose most of their implementation, or important behavior that is hard to exercise through a public entrypoint. Trace at least one real operation through the suspected area before recommending a refactor.

A deep module hides useful complexity behind a simpler interface. Judge depth by what callers need to know, not file size. Apply a deletion check: if a wrapper disappeared, would callers need to take over meaningful work or merely call the next function? A layer that owns compatibility, authorization, transactions, or resource lifetime can justify its existence even when short. Similar code alone does not establish a shared concept.

For each supported candidate, explain:

- The affected files and a concrete operation that exposes the friction, with source locations supporting the claim.
- What responsibility would move, its authoritative owner, and how callers would become simpler.
- Which public behavior and invariants must survive, including failure and cleanup paths.
- Expected benefits, migration costs, risks, and any conflict with an existing decision.
- Why changing the structure is preferable to a smaller local fix or leaving it alone.
- Recommendation strength: strong, worth exploring, or speculative, with the evidence behind it.

Prioritize by observed pain and likely change needs. Separate expected gains from measured results. Do not invent candidates to fill a quota. Show the current and proposed relationships when a diagram helps. Use the requested report format or the environment's available artifact tools; for an HTML report, prefer a self-contained file without network dependencies. Label proposed diagrams as proposals.

Recommend the next useful slice. If the request is only exploratory, deliver the candidates and let the user choose before developing an extensive design. If a target and implementation are already authorized, continue within that scope without another approval checkpoint.

## Develop the selected change

For the selected candidate, use architect and principle-foundational-thinking guidance when available. Otherwise perform the following design work directly; neither companion is required.

Start with the operations callers need, their dominant access paths, and realistic caller usage. Identify the authoritative data, valid state transitions, and invariants before choosing a representation or interface. For consequential choices, compare structurally different viable designs, including their accepted costs; avoid alternatives that only rename or rearrange the same structure.

Give each mutable fact a clear owner. Where actors overlap, trace reads, writes, publication, and destruction; show how the whole operation preserves its invariants, rather than assuming a synchronized container is enough. Resolve lifetime, error handling, and cleanup at the proposed interface. Address these concerns to the extent the candidate actually involves them.

Sequence migration by dependencies and uncertainty. Choose a narrow slice that exercises the new ownership and caller contract, specify compatibility boundaries and rollback needs, and identify when superseded paths can be removed. Do not leave two permanent owners of the same responsibility. Repeated caller workarounds are a reason to reconsider the proposed model.

Tie each promised improvement to a verification criterion. Test through consumer-visible contracts, preserving coverage of external effects and important failures. Internal rearrangement should not require changing behavioral expectations. If implementation is authorized, carry the selected slice through migration and appropriate checks; otherwise leave implementation steps in the design.

Keep investigation read-only unless changes were requested. Update glossaries or decision records only when included in the authorized work. Completion means evidence-backed candidates for a scan, a reviewable design for design work, or an implemented and appropriately verified change for implementation work. State remaining uncertainty and verification limits.

Adapted from Matt Pocock's [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md). Replaces its required companion skills, model workflows, and CDN report with self-contained, platform-neutral guidance.

Design and ownership guidance also draws on pstack's [architect](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md) and [foundational thinking principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-foundational-thinking/SKILL.md).
