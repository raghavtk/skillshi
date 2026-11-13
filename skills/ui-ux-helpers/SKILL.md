---
name: ui-ux-helpers
description: Choose or review UI patterns for web, mobile, and desktop product interfaces. Use for concrete decisions about forms, navigation, accessibility, responsive behavior, data displays, or shared UI defaults.
license: MIT
---

# UI/UX Helpers

Start with the user's task, the target surface, and the interaction that needs to work. Inspect existing components, platform conventions, supported input methods, and realistic content. Use the project stack for implementation details.

- **Choose a pattern.** State the outcome in observable terms, such as “a user can find and correct an invalid field without losing the rest of the form.” Compare alternatives only when they change the user's path. Use [Pattern guide](references/patterns.md) for forms, navigation, controls, responsive layouts, and data displays.
- **Set shared defaults.** When the request spans screens or components, define the few roles that need to stay consistent: type and spacing scales, semantic color, component states, and responsive behavior. Start with the existing system. Choose density from the frequency and volume of work. Record a screen-specific exception only when its content or task needs it. Document defaults when the user asks for a reusable specification or the repository already maintains one.
- **Review an interface.** Walk the primary path at a representative size and input method. Prioritize inaccessible or blocked paths, misleading states, and failed recovery before layout, performance, and cosmetic issues. Read the relevant sections of the pattern guide to exercise failure and edge cases. Cite the condition, what the user experiences, and the proposed correction. For a review-only request, return findings.

When implementing a fix, recheck the exact path and relevant failure state. If preview or device testing is unavailable, inspect source and existing tests and identify the checks that still need a live run. Use landing-page-design for marketing and portfolio narratives, and frontend-design for art direction or detailed motion when available. This skill can resolve its own pattern decisions independently.

Adapted from [Next Level Builder's UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md). This version turns prioritized design guidance into a portable workflow and a local pattern reference. See [LICENSE](LICENSE).
