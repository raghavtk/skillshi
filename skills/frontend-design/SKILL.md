---
name: frontend-design
description: Design and implement distinctive frontend interfaces for websites and apps, including new pages, components with visual design decisions, and redesigns. Choose between a focused design pass and deeper art direction based on the requested tier and token budget.
license: Apache-2.0 AND MIT
---

# Frontend Design

Adapted from [Anthropic's frontend-design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md). Interaction guidance draws on [Emil Kowalski's design engineering skill](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md). This version adapts both workflows for any compatible agent and adds two budget tiers. See [LICENSE](LICENSE).

For a marketing page or portfolio, use landing-page-design if available to plan the page's story and evidence. Use this skill when the work also needs deeper visual or interaction guidance. On its own, this skill works for those pages too.

## Choose the tier

- **Quickdraw** is the lower-budget default. Use it for routine UI work, targeted edits, tight budgets, or when the budget is unknown. Pick one direction, build it, and check the result.
- **Art Director** is the higher-budget tier. Use it when the user asks for it or gives you room for exploration and refinement on a flagship page, distinctive redesign, or other design-led brief. Read [Art Director](references/art-director.md) for the extra passes. A request for a small change still has a small scope in this tier.

Honor the user's tier choice and spending limits. When an Art Director request has a tight budget, keep the comparison and review focused on the most consequential decision. Preserve enough budget to finish and verify the requested work. These tiers describe relative effort and work with or without a token counter.

## Design and build

1. Identify the audience, what they came to do, and what is distinctive about the subject. Read the brief and inspect any existing UI, components, and assets. Respect the requested look and established product conventions. If a detail is open, use a reasonable assumption and continue when it is easy to reverse.
2. Pick a direction the subject can support. Decide what people should see or do first and use composition, type, color, and spacing to make that clear. Where the brief gives you freedom, choose one distinctive visual move tied to the subject. A dense work queue may need a clear row hierarchy and sharp state labels. A ceramics studio might lead with a full-bleed close-up that shows the glaze. Question repeated cards, decorative labels, and gradients when they lack a job.
3. Build the requested interface in the existing stack. Reuse its components and styles where they fit. Use meaningful content and action labels, and make relevant empty, loading, error, and success states useful. Keep the interface responsive, readable, and operable with a keyboard. Make feedback immediate for frequent actions. Use brief, interruptible motion where it clarifies feedback, state, or spatial relationships. Preserve the feedback with reduced motion. Read [Interaction design](references/interaction-design.md) when motion or gesture behavior is central to the task, or when diagnosing an interaction that feels slow, awkward, or unreliable.
4. Check the changed interface in a preview when available. Inspect a representative wide and narrow view, exercise the main interaction and relevant states, and fix material issues. When a changed control can be triggered repeatedly, check that its final state and focus follow the latest input. For Quickdraw, keep this to one focused review. If a preview is unavailable, use source inspection and existing checks, then state which visual or interactive checks remain unverified.
