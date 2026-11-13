# Pattern guide

Use only the sections that apply to the user's task. Adapted from the [UI/UX Pro Max quick reference](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/references/quick-reference.md). See [LICENSE](../LICENSE).

## Forms and feedback

Keep labels visible after input. Place actionable errors beside their fields. For a long form with multiple errors, provide a summary that leads to the affected fields. Preserve entered values on a failed submission. Give pending, failure, and success states distinct feedback and confirm success after the operation completes. Test an invalid input, a failed request, and a successful retry when applicable.

## Navigation and controls

Use a link for a destination and a button for an action. Make back, cancel, and direct entry land in predictable states. When a dialog closes, return focus to its trigger or a logical successor. Give icon-only controls an accessible name and expose their state where applicable. Keep focused controls visible around sticky headers or overlays. Provide a simple click or tap action and a keyboard path for operations that also support dragging. Exercise the applicable input methods.

## Responsive layout and shared styles

Let content determine where layouts reflow. Check long labels, larger text, and narrow and intermediate widths. Keep essential actions reachable without relying on hover. On supported right-to-left layouts, inspect reading order and directional controls. Verify contrast in the actual rendered states and supported themes. Use shared semantic colors and type roles when they already express the intended meaning.

## Data displays

Choose a display around the question. A line shows change over time, bars compare categories, and a table supports exact lookup. Label units and the time range. Use labels or patterns alongside color for distinctions that matter. Make critical values available through text or a table when a chart alone would hide them from some users. Check whether zero, missing, long, or outlier values change the meaning or break the display.
