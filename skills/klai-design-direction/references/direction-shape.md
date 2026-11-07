# Shape of the brief

Fill [assets/direction-template.md](../assets/direction-template.md). This file explains what each block must do. Vague praise is failure: if a line would fit a banking app and a bakery, rewrite it.

Methods here are adapted (own wording) from Unslop's five-line direction, Impeccable's surface modes, and Taste's "copy before layout" and "kind of work decides the plan". Credits: [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md).

## Required lines

### 1. Audience and jobs
Who, where, on what device, what they must finish. Not "users". Example of the right grain: "Dispatchers at a desk, 24-inch monitor, answering the phone with the board already open; they scan 40 open jobs and assign one without opening a detail."

### 2. Character
Two or three concrete words plus a sentence of behaviour. Allowed grain: `calm, exact, a little warm`; `fast, technical, slightly dry`; `plain, physical, high-contrast in sun`.

Do not use as character: clean, modern, sleek, minimal, premium, elegant, stunning, world-class, AI-native. Those describe templates.

Character must follow audience. A night warehouse handheld is not "editorial." A donor gala microsite is not "dense admin."

### 3. Material world and context
Where this work sits in the real world: paper dockets, truck cabs, florist coolers, fluorescent back offices, rain on a phone. This tints neutrals and chooses density. It is not an excuse to watermark textures on every panel.

Operate surfaces: the world shows in accent, data, and one or two moments — not in orange backgrounds behind a 12-hour table.

Marketing/cover surfaces: the world may tint larger areas and carry a scene.

### 4. One or two signature moments
Name the actual thing: "the job board's overdue column", "the cover photograph of the shop floor", "the completion stamp on a field checklist". Richness goes here: colour, material, a chart that means something, a product view.

Everything else is quiet chrome. If you cannot name the moments, you do not have a direction yet.

### 5. What stays quiet
Navigation, buttons, labels, filters, settings. No glow, no extra accent, no animated shell. Write this explicitly so a later polish or makeover does not "add delight" to the toolbar.

## Mode map (per surface, not per product)

| Mode | Visitor success | Klai typical surface | Ambition |
|---|---|---|---|
| Operate | Finish a task | Lists, boards, forms, settings, role home | Precision, restraint, known patterns earn their place |
| Marketing / cover | Decide and enter | Remix-style splash, public brochure page | More expression; still specific to this product |
| Read | Understand | Help, policy, changelog | Structure first, then a reading experience worth staying in |

A scheduling tool's landing page is marketing. Its calendar is operate. Do not dress the calendar like the landing page.

This map does **not** edit `klai-app-remix-preview`. Remix has its own cover and "premium, not minimal" language. When you hand off to remix, hand them `DIRECTION.md` as input; they follow remix rules for the preview.

## Copy before layout

Write, in the brief:

- Page title pattern (what the window is called).
- Primary action verbs that already exist in the app; do not invent features.
- Empty-state sentence that teaches the next click.
- Error sentence that names the problem and the recovery.
- Cover headline only if there is a cover; it must fail a name-swap.

Then note layout consequences: a 12-word empty state needs a different block than a 3-word one; a numeric board needs tabular figures and right-aligned columns.

## Working-app vs marketing richness

**Operate:** one family often carries the UI. Tight type scale (about 1.125–1.2 between steps). Density when the job is a table. Familiar affordances. Delight is a moment, not a page-load sequence.

**Marketing:** asymmetric hero or a real scene, one primary action, product-specific nouns. Still no filler orbs, still no unverified "10,000 teams" claims.

If an inner Klai page is a working tool, it is operate even when the company is fashionable.

## What the brief must not do
- Pick a palette because it is fashionable.
- Ban a device or pattern the audience actually uses (example: do not ban dense tables for a dispatcher).
- Require an approval gate after a reversible Dev implementation skill starts, unless the user asked to review first.
- Instruct remix to drop its gates or its mocked-preview rules.
