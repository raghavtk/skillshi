# Interaction design

Adapted from [Emil Kowalski's design engineering skill](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md). See the MIT notice in [LICENSE](../LICENSE).

## Choose motion by purpose

Name what motion communicates. It can acknowledge a press, connect a popover to its trigger, show a state change, or explain a sequence. Frequent keyboard and navigation actions should feel immediate. Keep any feedback for repeated actions brief and let users act while it plays.

## Tune the interaction

- For a small overlay, start with a short ease-out so the response is visible as soon as it opens. If it scales, use a subtle change anchored to the trigger. A centered dialog can use its own center. Treat a duration around 150–250 ms as a starting point for small overlays and adjust against the rendered result.
- For controls that can be toggled rapidly, use a transition that can change course from its current position. For direct manipulation, track the active pointer, handle cancellation, and consider release velocity as well as distance. Use a spring if the interaction benefits from carrying momentum through a release or reversal.
- Keep hit targets and focus behavior stable while the visuals change. Check mouse, touch, and keyboard paths when supported. Make hover enhancements work only for hover-capable input. Preserve feedback with reduced motion through immediate changes or a restrained fade.
- Prefer animating specific properties. On the web, try transform and opacity first for motion that can leave layout intact. If the interaction stutters, profile it under representative load and inspect layout and paint work before adding more effects.

Replay the interaction at normal speed and interrupt it by closing, reopening, or reversing it. Use slowed playback to diagnose awkward starts, stops, or origins when needed. Confirm the final state and focus match the last user action.
