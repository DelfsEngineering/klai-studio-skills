---
name: klai-design-direction
description: >-
  Writes an evidence-based visual design brief for a Klai Studio app from
  audience, jobs, workflows and authorized brand references. Use when someone
  asks for design direction, a visual brief, brand extraction, or how an app
  should look before any UI edits. Do not use to polish execution, replace a
  visual system, or redesign workflows (those are klai-ui-polish,
  klai-ui-makeover, and klai-app-remix-preview).
license: LICENSE-THIRD-PARTY.md
compatibility: >-
  Klai Studio MCP for read-only app evidence. Browser tools optional for
  authorized public brand references. Does not require Playwright or designlang.
---

# Klai design direction

A direction is a written visual brief. It says who the app is for, what work it supports, what character the surfaces should have, and which one or two moments carry richness. It is evidence, not slogans. This skill does not edit pages, CSS, navigation or environments.

Load files from **this skill folder only**. Paths below are relative to this `SKILL.md`. Do not read sibling skills for shared text; each skill ships its own copies. After merge to `main`, the same relative paths exist under `skills/klai-design-direction/` in this repo. Until then this skill lives on the review branch only.

## When to use
- The user asks for design direction, a visual brief, a look-and-feel writeup, or brand extraction.
- A polish, makeover or remix is requested but there is no written direction yet, and the missing brief would control visual choices. Write the brief first, then hand off. Do not wait for a separate approval of reversible Dev work.
- Someone needs operate-vs-marketing guidance for a Klai app without changing screens yet.

## When not to use
Hand off; do not stretch this skill into implementation.

| User actually wants | Use instead |
|---|---|
| Keep this look, fix craft (spacing, type, states, contrast, overflow) | `klai-ui-polish` |
| New visual system, same jobs, permissions and data | `klai-ui-makeover` |
| New workflows, IA, signature feature, win-back mocked preview | `klai-app-remix-preview` |
| Production deploy, live data, emails, Notion, secrets | Refuse that part; this skill is a brief only |

If the user names two jobs ("write the brief and then make it over"), finish this skill's exit criteria, then say the handoff and load the next skill.

## Entry criteria
All of these, or stop and say what is missing:
1. A target app or a concrete audience + jobs description. An app id or MCP connection is enough; a prose brief is enough if there is no app yet.
2. This skill is **read-only**. That is a scope boundary, not a question to ask the user. Do not ask them to confirm that you will not edit UI. If they already asked to restyle, still write the brief as the first artifact, then hand off without an extra approval gate for Dev work.
3. Any brand reference the user wants followed is an **authorized** public page, file or stated token. Do not scrape a competitor to copy a layout. Do not invent a brand the client did not offer.

## Exit criteria
The run is done when `DIRECTION.md` exists, the record lists evidence with confidence, the name-swap check is written, and no page was edited. Stop there unless the user already named a follow-on skill.

## Inputs
Caller supplies what they have. Missing CS notes do not block a brief; mark gaps.
- **App**: the Klai app as the client knows it, plus the connection if reads are allowed.
- **Audience and jobs**: who opens it, on which device, in what setting, what they must finish fast.
- **Brand references**: logo files, public marketing site, stated colours/type. Unauthorized or unknown-license layouts are not sources.
- **Mode hint**: working app, marketing/cover, or both. If omitted, infer from surfaces and say so.
- **Constraints**: accessibility, existing tokens to keep, things the owner already rejected.

Do not put customer account ids, env ids, emails or helper-file names into the reusable skill files. They may appear in a run record for that job only.

## Hard constraints
- Read-only toward the app. No `mcp_update_schema`, no deploy, no environment create/update, no credential writes.
- No production changes. No emails, Notion sync, secrets or iMac access.
- Direction language is concrete. Ban as character words: clean, modern, sleek, minimal, premium. Say materials, light, density, tempo and who it is for instead.
- Do not install upstream CLIs, run remote extractors, or vendor their collections. Brand extraction is manual inspection of authorized pages with whatever sanctioned browser is already available. See [references/brand-extraction.md](references/brand-extraction.md).
- Do not claim a ranking ("top-rated", "award-winning") unless the user supplied a verifiable source.
- Working-app chrome stays quiet; richness lives in one or two content moments. Marketing/cover surfaces may carry more expression. Write both when the app has both. This does not change `klai-app-remix-preview`.

## Workflow
Create `design-runs/<app-or-brief-slug>/RECORD.md` first, with a live checklist of these steps. Update it as you go.

1. **Settle the job.** If this is really polish, makeover or remix, stop and say so. If direction is a prerequisite, continue.
2. **Inventory evidence.** Follow [references/evidence.md](references/evidence.md). Separate observed fact, owner statement, and guess. Guess stays labelled.
3. **Map Klai surfaces (when an app is readable).** Follow [references/klai-feature-map.md](references/klai-feature-map.md). Use only tools that exist on the connection. Record pages, nav, roles, themes, and which surfaces are operate vs cover/marketing. Partial reads are allowed; note why.
4. **Extract brand only from authorized public reference.** Follow [references/brand-extraction.md](references/brand-extraction.md). Provenance on every token. Tokens and character, never layout plagiarism.
5. **Choose a mode per surface.** Follow [references/direction-shape.md](references/direction-shape.md). Operate vs marketing is a surface property, not a product property.
6. **Write voice and labels before layout notes.** Headings, primary actions, empty-state promises, error recovery. Layout notes come after, because line length and hierarchy depend on the words.
7. **Fill the brief.** Use [assets/direction-template.md](assets/direction-template.md). Required blocks: audience and jobs, character (concrete words), material world and context, one or two signature moments, what stays quiet, tokens with provenance, mode map, name-swap result, open guesses.
8. **Originality check.** Follow [references/originality.md](references/originality.md). If swapping the product name still fits, the brief is generic; push it until it would not.
9. **Stop or hand off.** Do not start CSS. If the user already asked for polish or makeover, load that skill and pass `DIRECTION.md` as input. No extra approval wait for reversible Dev work. Production publish still needs the owner.

Worked generic examples: [references/examples.md](references/examples.md). Selection fixtures: [evals/README.md](evals/README.md).

## Files in this skill
- `references/evidence.md` — inventory and source confidence.
- `references/direction-shape.md` — shape of the brief, operate vs marketing.
- `references/brand-extraction.md` — provenance rules and manual extract method.
- `references/originality.md` — name-swap / template-look check.
- `references/klai-feature-map.md` — read-only Klai discovery with real tools.
- `references/examples.md` — illustrative generic worked examples; do not copy styling.
- `assets/direction-template.md` — the artifact to fill.
- `LICENSE-THIRD-PARTY.md` — credits, licenses, change notes.
- `NOTICE` — required third-party notices.
- `licenses/Apache-2.0.txt` — Apache 2.0 terms for adapted Apache-licensed methods.
- `evals/` — selection and brief-quality scenarios.
- `CHANGELOG.md` — dated history of this skill.

## Definition of done
1. `RECORD.md` exists and every workflow step is done or explicitly blocked.
2. `DIRECTION.md` follows the template; no banned character words; each major choice cites evidence.
3. Brand tokens that were taken from a reference list URL, date, what was taken, and confidence.
4. Name-swap check is written and would fail for a different product (or the brief was revised until it does).
5. No app writes, deploys or production touches.
6. Unrun browser checks (if a public reference could not be opened) are listed as blockers, not implied as done.
7. Closing summary: what the brief decided, what was guessed, which skill should run next if any.

## Sources
Methods adapted with own wording. Required credits: [LICENSE-THIRD-PARTY.md](LICENSE-THIRD-PARTY.md). Do not treat upstream files as ranked or as a drop-in kit.
