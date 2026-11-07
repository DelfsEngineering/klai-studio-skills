# Prioritized audit

Polish starts with a written audit, then fixes in impact order. Do not wander the CSS.

Adapted in own words from Unslop's audit-then-triage and Impeccable polish's defect ranking. Credits: [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md). Changes: Klai tools; context can keep a pattern; operate vs marketing; no detector CLI.

## Impact order (fix in this sequence)

1. **Blocked or misleading work** — controls that cannot be used, clipped primary actions, contrast that fails on the actual text, wrong enabled/disabled, information that looks clickable and is not (or the reverse).
2. **Missing states** — no loading, empty, error, success, disabled, or permission-denied path for a control you ship.
3. **Hierarchy, density, responsive, system drift** — the job is not the loudest thing; tables wrap into mush; one page's button is not the shared button.
4. **Type, spacing, colour execution** — still the same system, badly applied.
5. **Cosmetic leftover** — unused shadow, inconsistent icon optical alignment, debug outlines.

Do not perfect a marketing cover while an operate table fails at 390.

## Baseline before opinions
Open the scoped path as a user would. Note device, theme, role. Screenshot before changing. If the app needs auth you do not have, stop and record the blocker; do not bypass. Do not click save, delete, email, or pay to "use the feature" unless the user actually authorized that consequential action; Dev is not automatically isolated.

## Tells (defaults, not bans)

Use these as a hunt list. If the direction or a real brand *uses* a listed pattern on purpose, keep it and write why. Blanket bans are how operate UIs lose necessary density and how branded violet becomes accidental grey.

**Surfaces.** Hue-on-hue gradients behind working UI; glow as depth; every element accented so nothing leads; glass on a 12-hour dispatch board.

**Type.** Too many sizes on one operate screen; mixed number formats; tracked uppercase as section chrome; tiny type in sun/field use; display faces on table labels.

**Icons.** Emoji as the only nav affordance; three icon sets; sparkle-as-AI. Keep emoji if the audience is children and the owner asked — then make them consistent, not random.

**Spacing.** Arbitrary 13px gaps; siblings with different padding; groups tighter to neighbours than to their own items; 4px scale is the default rhythm, 2px only inside small controls.

**Copy.** Greeting-plus-wave as a page title; hype (supercharge, seamless, unlock); unverified social proof; trailing periods on buttons. Do not rewrite factual legal copy.

**Components.** Every container a pill; rainbow charts; identical stat cards in a row with sparklines; leftover platform indigo when the brand is not indigo.

**Overflow.** Dropdowns clipped by `overflow: hidden`; sticky headers covering the focused field; horizontal scroll at 390 that is not a deliberately scrollable table; text clipped without title/tooltip.

**Browser surfaces.** Unstyled text selection, caret, scrollbars, focus rings, underline offset, and lining numerals on tabular data — they still show, and they still look like "nobody designed this" if they clash.

**Motion.** Looping pulse on static content; page-load choreography on operate; `transition-all`; layout-property animation (width/height/top/left).

**Template look after cleanup.** Grey page + Inter + one old accent, on a product whose world is not that. That is not "done polish"; it is missing direction. Hand back a short direction note or hand off to makeover if the system itself is wrong.

## Light vs heavy
- **Light:** a handful of tells, identity is right → this skill, scoped fixes.
- **Heavy but identity is right:** still polish, but plan passes and expect shared CSS work.
- **Identity is wrong:** stop. Recommend makeover. Do not "polish" a look you intend to throw away.
- **Jobs are wrong:** remix.

## Output
Fill [assets/audit-template.md](../assets/audit-template.md). Each item: where, impact (1–5), pass that will fix it, keep/fix/waive.
