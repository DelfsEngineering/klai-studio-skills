---
name: klai-ui-polish
description: >-
  Improves visual execution of an existing Klai Studio app without changing
  workflows, information architecture, or the visual system. Use when someone
  asks to polish, tighten, unslop, or fix spacing, type, states, contrast,
  overflow or component drift, and the current look is the right direction.
  Do not use to write a direction-only brief, replace the visual system, or
  redesign workflows (klai-design-direction, klai-ui-makeover,
  klai-app-remix-preview).
license: LICENSE-THIRD-PARTY.md
compatibility: >-
  Klai Studio MCP for reads and Dev writes. Browser verification uses whichever
  sanctioned browser tool is available. Playwright CLI is optional and must not
  be installed just to run this skill.
---

# Klai UI polish

Polish raises craft on the look the app already has. Workflows, navigation structure, permissions, data contracts and the visual system stay. Spacing, type, density, states, contrast, overflow, browser chrome and component consistency move.

Load files from **this skill folder only**. Paths below are relative to this `SKILL.md`. Do not follow sibling-skill links.

Until Charles merges this skill to `main`, it exists only on the review branch. Do not deploy or publish as part of this run.

## When to use
- The user asks to polish, tighten, clean up, unslop, or fix spacing, typography, hover/focus, tables, clipping or inconsistency.
- The current brand, layout skeleton and IA are keepers. Defects are execution, not concept.
- A direction already exists, or the incumbent look is coherent enough to treat as the system.

## When not to use

| User actually wants | Use instead |
|---|---|
| Only a written brief, no UI edits | `klai-design-direction` |
| New visual world, new type/colour/shape language, same jobs | `klai-ui-makeover` |
| New flows, IA, cover-as-win-back, signature feature, mocked remix | `klai-app-remix-preview` |
| Recolour as a substitute for a discarded look | `klai-ui-makeover` (do not "polish" a look you are throwing away) |

If the concept is wrong, say so and hand off to makeover or remix. Do not smuggle a new identity through polish.

## Entry criteria
1. A target app on a **non-production** environment, or an explicit isolated preview. Production writes are out of scope.
2. Either a `DIRECTION.md` or a short incumbent-system note (palette, type, density, what must not change). If neither exists and the look is incoherent, write a one-page direction using `klai-design-direction` methods, save it in the polish record, and continue. Do not pause reversible Dev polish for a ceremonial approval.
3. Scope: which pages or flows. Default: the path the user named, plus shared shell (header, nav, theme CSS) that those pages use.

## Exit criteria
Audit items in scope are fixed or waived with a reason; verification matrix is run or marked blocked; workflows and IA are unchanged; production was not touched.

## Inputs
- **App / env**: Dev or isolated preview. Never prod.
- **Direction or incumbent system**: what to preserve.
- **Scope**: pages, roles, themes.
- **Known bugs**: overlap, unreadable tables, missing focus, and so on.

## Hard constraints
- No workflow, IA, permission or data-contract changes. No new jobs, no removed jobs.
- Preserve **route ids**, layout slugs, hook names, named action names, and payload shapes. Visible **labels** (nav text, button captions, page titles) may change when the user asked to fix wording. A label is not a route id; do not rename identifiers to fix copy.
- No replacement palette, type family or shape language. Tune tokens that already belong to the system; do not swap the system.
- Dev writes only. No production deploy, no credentials, no helper-database changes, no email/Notion.
- Do not install Playwright, designlang or other remote kits. Use sanctioned tools that are already available. Never bypass auth, approvals or site blocks.
- `requestHook` and live backend calls stay as the app already intends. A **zero backend-request** rule applies only when this run is an explicitly isolated mocked preview. It is never a universal polish gate.
- Visual/CSS edits on Dev do not need extra approval. That is **not** authorization to click save, delete, email, pay, or other consequential actions on a connected backend. Inspect effects first; use disposable records and isolated services; follow the user's actual authorization for that class of action; otherwise mark the check blocked. See [references/verify.md](references/verify.md).
- Accessibility floors are not optional: text contrast 4.5:1, large text and icons 3:1, visible focus, keyboard path for every control you touch.
- Aesthetic "never" lists are defaults, not bans. A brief or real brand can keep a violet accent, an eyebrow that carries status, or denser chrome. See [references/audit.md](references/audit.md). Do not apply marketing richness to operate chrome, and do not flatten a cover into a form toolbar. This skill does not change remix's written rules.

## Workflow
Create `polish-runs/<app-slug>/RECORD.md` first.

1. **Confirm polish.** If they want a new look or new flows, hand off.
2. **Baseline.** Follow [references/verify.md](references/verify.md) for captures: representative pages, 390 and 1280, plus any intermediate width where the layout actually breaks (often 768 and 1024), every in-scope theme. Label mocks vs live. Save before shots.
3. **Discover the system.** [references/klai-feature-map.md](references/klai-feature-map.md). Read site CSS, theme, components, shared nav/slots, and the pages in scope. Fetch the Klai guide for the thing you are about to edit as an MCP resource when that guide exists (`guide_html_v8`, `assistantGuide_slots`, `assistantGuide_mcp_schema_save`, and so on). `get_guide` tool output is not a substitute when resources are how this team loads guides.
4. **Audit by user impact.** [references/audit.md](references/audit.md). Priority: blocked tasks and contrast failures, then missing states, then density/type/spacing, then cosmetic drift.
5. **Ordered passes.** [references/passes.md](references/passes.md). Action and accessibility floors first (unclip primary actions, contrast, focus), then spacing and the rest. Finish a pass across the scoped path before the next. Do not perfect one card while a primary control is untappable.
6. **States and overflow.** [references/states.md](references/states.md). Default, hover, focus, active, disabled, loading, error, empty, success. Dropdowns must escape clipping parents. Long content, empty, loading and error are real checks, not screenshots of the happy path.
7. **Verify.** [references/verify.md](references/verify.md) again. Console and network if the browser tool can show them. Keyboard, contrast, reduced motion. Do not fire consequential live actions without actual authorization. Mark anything unrun or blocked.
8. **Diff hygiene.** No unrelated churn. Re-read after each save; Klai saves can report success without taking effect.
9. **Report.** What changed, what was waived, verification evidence, blockers.

Templates: [assets/audit-template.md](assets/audit-template.md), [assets/record-template.md](assets/record-template.md). Examples: [references/examples.md](references/examples.md).

## Files in this skill
- `references/audit.md` — impact triage and context-sensitive tells.
- `references/passes.md` — ordered craft passes.
- `references/states.md` — interaction and content states; clipping.
- `references/verify.md` — browser matrix, tools, honest blockers.
- `references/klai-feature-map.md` — real Klai tools, no invented APIs.
- `references/examples.md` — generic worked examples; do not copy.
- `assets/audit-template.md`, `assets/record-template.md`
- `LICENSE-THIRD-PARTY.md`, `NOTICE`, `licenses/Apache-2.0.txt`, `evals/`, `CHANGELOG.md`

## Definition of done
1. Record shows baseline, audit, passes, verification.
2. In-scope pages still complete the same jobs, with the same permissions, route ids, hooks, named actions and data shapes. Visible labels may have been corrected; identifiers were not renamed.
3. Visual system (brand colour role, type families, shell structure) is the incumbent system, executed better.
4. Verification matrix: 390 and 1280 required; intermediate widths where risk exists; every in-scope theme; long/empty/loading/error; keyboard and contrast. Unrun cells named.
5. Console/network inspected when the tool can; otherwise marked unavailable, not passed.
6. Zero-backend-request checked only for an isolated mocked preview.
7. Closing summary of shipped vs skipped.

## Sources
[LICENSE-THIRD-PARTY.md](LICENSE-THIRD-PARTY.md). Playwright identity in the original reel is uncertain; this skill does not claim to be Playwright CLI.
