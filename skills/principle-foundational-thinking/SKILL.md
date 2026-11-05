---
name: principle-foundational-thinking
description: Resolve data shape, ownership, invariants, and dependencies before substantial logic changes. Use for foundational design or refactoring that affects multiple callers or concurrent actors.
---

# Foundational thinking

Write the required operations and dominant access paths before choosing structures. Identify authoritative state, valid transitions, lifetimes, and the invariants callers rely on. Compare plausible representations against those needs, including migration and failure handling.

Give mutable state one clear owner. Before sharing it, trace concurrent reads, writes, destruction, and publication. Choose isolated ownership, immutable snapshots, or explicit synchronization according to the actual interactions. A thread-safe container does not make a multi-step operation atomic.

Consolidate concepts and invariants where they genuinely coincide. Similar syntax alone does not justify a shared abstraction. Keep public interfaces small enough that callers do not need internal coordination rules.

Sequence work by dependency and uncertainty. Establish shared types or a narrow executable slice when later tasks need them. Preserve compatibility through explicit migration boundaries; subtract demonstrably obsolete code within scope rather than accumulating two permanent ways to do the same task.

Complete an increment when its behavior and ownership are coherent and verifiable. Repeated caller workarounds are evidence to reconsider the model. Document accepted costs and alternatives, and keep the foundation proportional to the user's current task.

Adapted from pstack's [foundational thinking principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-foundational-thinking/SKILL.md).
