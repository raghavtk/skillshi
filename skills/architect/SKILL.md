---
name: architect
description: Design substantial changes from requirements and existing runtime constraints. Compare module and data-model alternatives, sketch caller-facing APIs, and plan migration and validation before implementation.
---

# Architect

Establish the requested deliverable: design, implementation, or both. For planning-only work, finish with a reviewable design and implementation gates.

Ground the design in authoritative requirements, current call/data flow, and integration constraints. Investigate history when ownership or layering changes; keep inferred rationale separate from documented intent. Mark conflicting or missing sources.

Write realistic caller usage before proposing types. For consequential choices, compare structurally different viable designs. Explain public contracts, state ownership, lifetime, concurrency, failure behavior, and migration. Prefer an interface that hides useful complexity without requiring callers to coordinate internal stages.

Check for duplicate state owners, exposed internals, manually synchronized lists, shallow forwarding layers, and unnecessary frameworks. Adapt heuristics to the actual constraints. Record the selected shape, rejected alternatives, accepted costs, evidence gaps, and the next executable slice.

Keep sketches in design artifacts until implementation is requested. During implementation, reconcile departures with requirements and revise the sketch when repeated workarounds expose a mistaken assumption. Preserve existing behavior through explicit migration checks.

Use available tools and authorized delegation; another product's model roster or arena is not required. Completion means each affected requirement has an owner, planned mechanism, and verification criterion, with proposals distinguished from user decisions.

Adapted from pstack's [architect](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md), [design checks](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md), and [rationale guide](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/rationale-template.md).
