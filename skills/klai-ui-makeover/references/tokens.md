# Replacement tokens and components

One system across the scoped app. If two pages could be two products, the makeover is not done.

## Token set to actually write
Document in `TOKENS.md` and implement in site CSS (or the project's real token location):

- Colour: bg, surface, hairline, text primary/secondary/muted, accent, focus, selection, danger, success (tuned).
- Type: operate family + sizes (ratio ~1.125–1.2); optional display family **cover only**.
- Space: 4px scale; density vars for compact vs comfortable if both exist.
- Radius: control / card / panel; nested inner = outer − padding (floor 4).
- Elevation: operate prefers surface steps + hairlines; soft offset shadows if used, not neon halos.
- Motion: durations 150–250ms, one ease; reduced-motion cuts.
- Browser surfaces: `::selection`, caret, scrollbar, focus ring, `text-underline-offset`, `font-variant-numeric: tabular-nums` on data.

Accent is a role, not a wallpaper. Operate pages do not wash the canvas in brand hue.

## Components
Build or restyle a small vocabulary and reuse it:

- Primary / secondary / quiet text button
- Input, select, checkbox, radio
- Table (header, row, empty, loading)
- Inline notice (error/success)
- Nav item + active
- Empty state block

Same shape in settings and in the main job page. Invented one-off controls are defects unless the job is unique (signature moment).

## Type and tables
- Operate labels are UI sans, not display.
- Tabular numbers, one numeric format.
- Identifying column stays readable at 390 (scroll inside the table if needed).

## Themes
Restyle every theme you keep. A neglected dark theme is a fail. Do not add a second theme unless the audience needs it (night warehouse, etc.).

## What not to import
Upstream kits, default indigo, "AI" sparkle, stock orbs. Authorized brand tokens yes; their landing-page grid no.
