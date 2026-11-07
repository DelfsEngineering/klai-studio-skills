# Ordered passes

Finish a pass across the scoped path before starting the next. When almost everything must change inside the *same* system, you may implement in one save per page as long as every pass is applied. Do not skip spacing because colour is more fun.

Own wording, inspired by Unslop's pass order and Impeccable operate/craft-floor mechanics. Credits: [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md). Change from Unslop: **blocked actions and accessibility floors run before spacing**, because an untappable primary control outranks rhythm.

## 0. System inventory
List existing tokens, shared CSS, components, header/sidebar slots. Polish binds to these. If there is no system, infer one from the majority of screens and write it down; do not invent a second one.

## 1. Blocked actions and accessibility floors
Fix what stops the job before you tune gaps.

- Unclip and un-cover primary actions (especially at 390). A control that cannot be used is impact 1.
- Contrast floors: text 4.5:1, large text and icons 3:1, in every in-scope theme.
- Visible focus and a keyboard path to every control you touch.
- Touch targets on phone-first profiles: the primary must be hittable without a hover-only path.
- Do not fire the primary on a connected backend to "test" it unless authorized; seeing it, focusing it, and proving it is not clipped is the polish check.

## 2. Spacing and density
- 4px rhythm for margin, padding, gap, control heights (2px only as a nudge inside a control).
- Same-role rows share height and gap.
- Tight within a group, generous between groups.
- Operate density follows the job: dispatch tables stay dense; a once-a-week settings page can breathe.
- Nav rows are the densest chrome (about 32–36px), labels aligned, section labels closer to their items than to the previous section.
- Thumb reach on phone-first profiles: primary actions not only in a top-right desk pattern.

## 3. Colour execution (not a new brand)
- One accent role: primary action, selection, the one number that matters.
- Neutrals tinted toward the existing world, not a new world.
- Three text roles, not a ladder of leftover greys.
- Semantic colour only for meaning (error, success), tuned into the palette.
- Contrast: 4.5:1 text, 3:1 large text and icons, including placeholder and disabled-that-must-still-be-read cases. If disabled text is meant to be unreadable as text, it is not the only indicator of state.
- Operate surfaces: do not flood backgrounds with brand hue. Marketing/cover may.

## 4. Icons
- One set, one optical size, one stroke.
- Colour follows text role.
- Align in a fixed box so labels share a column.
- Remove icons that do not add meaning.

## 5. Copy (wording, not IA)
- Buttons use the app's verbs.
- Titles name the context, not a greeting.
- Visible labels only. Do not rename route ids, slugs, hooks, or named actions to fix copy.
- No new claims. Ask before changing factual or legal strings.
- Numbers: one format, tabular figures.
- Empty and error sentences teach the next step.

## 6. Typography
- Operate: one UI family is usually enough; scale ratio about 1.125–1.2; fixed rem steps, not a fluid display face shrinking in a sidebar.
- Measure: prose 65–75ch; tables may run wide.
- Weights: a small set. Hierarchy from size + colour + weight together.
- No negative tracking on small text.
- Tabular numerals for times, money, counts.
- Run real strings at 390 and 1280; fix wrap and overflow.

## 7. Layout execution (not new IA)
- Alignment to the existing grid.
- Optical alignment (icons, currency) as well as pixel.
- Working pages stay in their established alignment (usually left). Do not centre an operate form because a cover is centred.
- Header and nav remain the same structure unless they are visually broken (then repair, do not reinvent).

## 8. Details
- Radius by size, nested inner = outer − padding (floor 4px) unless the incumbent system already defines otherwise.
- Tables: header sticky if rows are long; row hover; aligned decimals; no wrapping that hides the identifying column at 390 (allow horizontal scroll *inside* the table with a visible cue, rather than crushing columns to unreadable).
- Charts: one highlight; muted grid; no rainbow-for-one-series.
- Browser surfaces: selection, caret, scrollbar, focus ring, underline offset, tabular nums — from the palette.

## 9. Motion
- 150–250ms, ease-out, feedback only (hover, press, open/close, saved).
- Respect `prefers-reduced-motion`: no required information only in motion.
- No operate page-load sequence.

## After the passes
Re-walk the audit list. Missing in-scope primary actions or contrast failures are blockers, not waivers. Other items fail unless they are outside agreed scope, a named platform limit, or the owner explicitly accepted that item in this run. Re-read Klai records after save.
