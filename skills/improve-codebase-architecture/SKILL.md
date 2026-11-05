---
name: improve-codebase-architecture
description: Identify evidence-backed refactoring opportunities in an existing codebase, especially shallow modules and scattered caller coordination. Compare candidates and develop a selected design; implement only when requested.
---

# Improve codebase architecture

Establish whether the user wants opportunities, a detailed design, implementation, or a combination. Prefer a named subsystem or pain point. Otherwise use recent history to identify areas with repeated changes, then inspect their callers and tests. A small, coherent codebase may have no worthwhile candidate.

Read applicable repository guidance, domain terminology, and architectural decisions when present. Missing glossaries or decision records are evidence gaps, not reasons to create new files automatically.

Look for concrete friction: one change scattered across many modules, callers coordinating internal stages, duplicated ownership of an invariant, abstractions that expose most of their implementation, or important behavior that is hard to exercise through a public entrypoint. Trace at least one real operation through the suspected area before recommending a refactor.

A deep module hides useful complexity behind a simpler interface. Judge depth by what callers need to know, not file size. Apply a deletion check: if a wrapper disappeared, would callers need to take over meaningful work or merely call the next function? A layer that owns compatibility, authorization, transactions, or resource lifetime can justify its existence even when short. Similar code alone does not establish a shared concept.

For each supported candidate, explain:

- The affected files and a concrete operation that exposes the friction.
- What responsibility would move, its authoritative owner, and how callers would become simpler.
- Which public behavior and invariants must survive, including failure and cleanup paths.
- Expected benefits, migration costs, risks, and any conflict with an existing decision.
- Recommendation strength: strong, worth exploring, or speculative, with the evidence behind it.

Prioritize by observed pain and likely change needs. Separate expected gains from measured results. Do not invent candidates to fill a quota. Show the current and proposed relationships when a diagram helps. Use the requested report format or the environment's available artifact tools; for an HTML report, prefer a self-contained file without network dependencies. Label proposed diagrams as proposals.

Recommend the next useful slice. If the request is only exploratory, deliver the candidates and let the user choose before developing an extensive design. If a target and implementation are already authorized, continue within that scope without another approval checkpoint.

For the selected candidate, write realistic caller usage and compare viable designs before changing code. Resolve ownership, lifetime, concurrency, error behavior, compatibility, and migration. Use architect guidance when available, or perform that design work directly. Test through consumer-visible contracts, preserving coverage of external effects and important failures. Internal rearrangement should not require changing behavioral expectations.

Keep investigation read-only unless changes were requested. Update glossaries or decision records only when included in the authorized work. Completion means evidence-backed candidates for a scan, a reviewable design for design work, or an implemented and appropriately verified change for implementation work. State remaining uncertainty and verification limits.

Adapted from Matt Pocock's [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md). Replaces its required companion skills, model workflows, and CDN report with self-contained, platform-neutral guidance.
