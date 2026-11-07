---
name: klai-ui-makeover
description: >-
  Replaces the visual system of a Klai Studio app and may rearrange presentation
  while preserving functionality, permissions and data contracts. Use when
  someone asks for a UI makeover, a new look and feel, or a visual redesign
  that keeps the same jobs and flows. Do not use for craft-only polish, a
  direction-only brief, or a workflow/IA remix (klai-ui-polish,
  klai-design-direction, klai-app-remix-preview).
license: LICENSE-THIRD-PARTY.md
compatibility: >-
  Klai Studio MCP for reads and Dev writes. Browser verification uses whichever
  sanctioned browser tool is available. Playwright CLI is optional and must not
  be installed just to run this skill.
---

# Klai UI makeover

A makeover replaces how the app looks and how screens are presented. It does not replace what the app does. Jobs, routes, permissions, named actions, hooks and payload shapes stay. Type, colour, density, chrome, component vocabulary and visual hierarchy may all change. Presentation can be regrouped (a toolbar instead of scattered buttons, a table instead of identical cards) when the same job is easier that way.

The old look is evidence and anti-reference, not a base to tint. Do not split the difference into polish on a discarded identity.

Load files from **this skill folder only**. Paths are relative to this `SKILL.md`.

Until Charles merges this skill to `main`, it exists only on the review branch. Never merge, deploy or publish from this run.

## When to use
- The user asks for a makeover, a new look and feel, a visual redesign, or "it should not look like this anymore", and they want the same product underneath.
- The incumbent visual system is the problem (dated chrome, incoherent tokens, marketing slop on a working app), not a few spacing bugs.
- Workflows are keepers. If they also want different jobs or a win-back remix with new features, that is remix, not this skill.

## When not to use

| User actually wants | Use instead |
|---|---|
| Written brief only | `klai-design-direction` |
| Keep this identity, fix execution | `klai-ui-polish` |
| New workflows, IA, signature feature, mocked win-back preview | `klai-app-remix-preview` |
| Hue-only swap with unchanged type, spacing, hierarchy, components and states | Not a makeover. Either polish the real system or actually replace how it looks. Preserved schema/class ids alone do not make a CSS restyle "recolour-only". |

## Entry criteria
1. Target is a **Dev** environment or an isolated preview of the same app. Production is out of scope. Prefer the existing Dev env; do not create a remix environment unless handing off to remix.
2. A direction will exist before visual replacement. Write it in this run (same shape as `klai-design-direction`) if one was not supplied. For reversible Dev work, do not wait for a second approval after you have written it, unless the user asked to review first. Production publish still belongs to the owner.
3. A preservation matrix will be started before the first visual save. See [references/preservation.md](references/preservation.md).

## Exit criteria
New visual system is consistent across the scoped app (judge perceptible type, spacing, hierarchy, components and states — not whether ids churned); preservation matrix has no `pending`; in-scope missing behaviour is a blocker unless it is outside agreed scope or the owner explicitly accepted that gap in this run; production untouched.

## Inputs
- **App / Dev env**
- **Direction** or audience + authorized brand reference
- **Scope**: whole app vs named shells and pages
- **Must-keep**: logo, legal strings, role names, hook names

## Hard constraints
- Preserve functionality, permissions and data contracts. Preserve **route ids**, layout slugs, hook names, named action names, and payload shapes **by default**. Visible **labels** (nav text, button captions, page titles) may change; identifiers may not. HTML may call `namedAction('name')` rather than a literal `action('name')` for the **same** name if you touch that markup — that is call-style, not a rename.
- Do not add signature features, new jobs, or IA redesign (new mental model of the work). That is remix.
- You may rearrange presentation: grouping, hierarchy, density, table vs cards, shell styling, cover-as-marketing vs app chrome. You may not hide a permission, skip a required field, or change who can run an action.
- Missing in-scope behaviour is a **blocker**, not a reasoned gap you assume the owner would accept. A gap is allowed only when it is demonstrably outside the agreed scope of this run, or the owner **explicitly accepted that specific gap** in this run (quote them in the record).
- Dev only. No prod deploy, no credentials, no helper-database writes, no email/Notion, no secrets.
- Do not install upstream CLIs. Use sanctioned available tools. Never bypass auth or site blocks.
- Zero backend-request is **not** a makeover gate unless this environment is an explicitly isolated mocked preview.
- Visual/CSS edits on Dev do not need extra approval. That is **not** authorization to click save, delete, email, pay, or other consequential actions on a connected backend. Inspect effects first; use disposable records and isolated services; follow the user's actual authorization for that class of action; otherwise mark the check blocked. See [references/verify.md](references/verify.md).
- Working-app surfaces: quiet chrome, richness in one or two moments. Marketing/cover: more expression is allowed. Do not rewrite remix's "premium" rule; this skill just does not use "premium" as a character word.
- Accessibility floors remain: contrast, focus, keyboard, reduced-motion respect.

## Workflow
Create `makeover-runs/<app-slug>/RECORD.md` first.

1. **Confirm makeover.** New jobs → remix. Craft only → polish. Brief only → direction.
2. **Preservation matrix.** Inventory pages, fields, named actions, hooks, roles, nav destinations. [references/klai-feature-map.md](references/klai-feature-map.md), [references/preservation.md](references/preservation.md), [assets/preservation-matrix.md](assets/preservation-matrix.md). Status starts `pending`.
3. **Direction.** If missing, write `DIRECTION.md` using [assets/direction-template.md](assets/direction-template.md) and [references/direction-shape.md](references/direction-shape.md). Copy/voice before layout. Brand extraction with provenance only from authorized public reference.
4. **Baseline captures.** [references/verify.md](references/verify.md). Before shots at 390 and 1280, risk breakpoints, each theme. Distinguish live data from mocks.
5. **Scoped reversible plan.** [references/plan.md](references/plan.md). Site tokens and shell first, then shared components, then pages. Plan what rolls back (CSS, slots, components) without data migration.
6. **Replace the system.** [references/tokens.md](references/tokens.md). One vocabulary across the app: type scale, colour roles, radius, density, buttons, inputs, tables, empty/error. Fetch the matching Klai guide as an MCP resource immediately before the edit it covers. Re-read after saves.
7. **Presentation rearrangements** stay inside the matrix: same jobs, clearer presentation. Log each rearrangement and why the job is unchanged.
8. **Verify behaviour.** Walk jobs without unauthorized live writes. Roles see what they should. Follow the consequential-action guard in [references/verify.md](references/verify.md). Console/network if available.
9. **Originality.** Name-swap the cover and a representative operate page. If they could be another product, push direction into type, moments and copy. [references/originality.md](references/originality.md).
10. **Report.** Matrix, plan, before/after, verification, blockers.

Examples: [references/examples.md](references/examples.md). Record template: [assets/record-template.md](assets/record-template.md).

## Files in this skill
- `references/preservation.md` — feature/behaviour matrix.
- `references/direction-shape.md` — brief shape used inside a makeover.
- `references/plan.md` — scoped reversible plan.
- `references/tokens.md` — replacement system, consistency.
- `references/originality.md` — name-swap check.
- `references/verify.md` — browser and behaviour verification.
- `references/klai-feature-map.md` — real Klai tools.
- `references/examples.md` — generic worked examples; do not copy.
- `assets/direction-template.md`, `assets/preservation-matrix.md`, `assets/record-template.md`
- `LICENSE-THIRD-PARTY.md`, `NOTICE`, `licenses/Apache-2.0.txt`, `evals/`, `CHANGELOG.md`

## Definition of done
1. Direction written and followed.
2. Preservation matrix: no `pending`; every `moved` has `where`; every `gap` is either outside agreed scope or explicitly accepted in this run (quoted). Identifiers (routes, hooks, actions) unchanged by default.
3. Tokens and components are consistent across scoped pages and the shell. Done is judged by perceptible type, spacing, hierarchy, components and states. Preserved schema/class ids do not fail a real CSS visual-system replacement; hue-only with unchanged craft is not a makeover.
4. Behaviour, permissions and data contracts checked in a real browser path, not screenshots only, under the live-action guard. Unauthorized consequential clicks are blockers, not passes.
5. Viewport matrix: 390, 1280, intermediate risk widths, all in-scope themes, long/empty/loading/error.
6. Unrun checks listed. Zero-backend-request only if this is an isolated mocked preview.
7. Production, credentials and publishing untouched.
8. Closing summary of shipped vs skipped.

## Sources
[LICENSE-THIRD-PARTY.md](LICENSE-THIRD-PARTY.md). Playwright identity in the original reel is uncertain; this skill does not claim to be Playwright CLI.
