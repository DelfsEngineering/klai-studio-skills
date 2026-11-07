# States, overflow, consistency

Every interactive component in scope needs a real default, hover, focus, active, disabled, loading, error path. Add empty and success where the job can go there. Inspired by Impeccable operate notes; own wording. [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md).

## Per control
| State | What to check |
|---|---|
| Default | Matches the system; not leftover platform indigo unless that *is* the brand. |
| Hover | Surface or colour step, not a jump in layout. Pointer vs touch: no hover-only essential info. |
| Focus | Visible ring, not outline:none without a replacement. Logical tab order. |
| Active / pressed | Brief pressed step (tiny scale-down or inset), then settle. |
| Disabled | Not the only difference in colour if colour-blind; also `disabled`/aria. |
| Loading | Skeleton in place for content regions; do not centre a spinner that shoves the layout. Button loading keeps width. |
| Error | Message names the field, the problem, and the recovery. Beside the field, not only a toast. |
| Empty | Teaches the next action with the real verb. Not "nothing here". |
| Success | Quiet confirmation; celebration only on a real completion the user would notice. |
| Permission | Hidden vs disabled: match the product. Do not expose an action the role cannot run. Do not silently drop it from the DOM if the source showed it as disabled. |

## Content lengths
Check the same component with short, typical, and long strings (names, SKUs, error text). Truncate with a title or expand; do not clip mid-glyph without a cue.

## Overflow and clipping
- Dropdowns, date pickers, typeaheads must escape `overflow: hidden` / `auto` ancestors (fixed/portal/popover — use whatever Klai HTML already allows; do not invent a React portal API).
- Sticky headers must not cover focused inputs.
- Modals only when the job needs interruption or protected focus. Prefer inline.
- Horizontal page scroll at 390 is a defect unless it is a labelled table region.

## Component vocabulary
Same button shape, input height, and icon style on every scoped page. If Save looks different in two places, one is wrong. Promoting a one-off to a shared component is in scope for polish; inventing a new visual language is not.

## Themes
If the app has more than one theme, every state is checked in each. A dark theme that fails contrast is not "optional mood".
