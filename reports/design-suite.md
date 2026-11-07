# DESIGN-SUITE report (review branch)

Date: 2026-11-07 (updated after content review)
Task: DESIGN-SUITE
Branch: `cursor/design-suite-skills-de3d` (pending Charles merge; do not treat as published)
Repo: `DelfsEngineering/klai-studio-skills`
PR: https://github.com/DelfsEngineering/klai-studio-skills/pull/1

This work stays on the review PR. It did **not** merge, deploy, email, sync Notion, edit production apps, write a skill registry, or touch bots/Mac copies.

## Deliverables

| Skill | Folder | Job |
|---|---|---|
| Design direction | `skills/klai-design-direction/` | Evidence-based visual brief; no UI edits |
| UI polish | `skills/klai-ui-polish/` | Execution only; workflows/IA/system stay |
| UI makeover | `skills/klai-ui-makeover/` | Replace visual system; preserve jobs, permissions, data contracts |
| Remix (unchanged) | `skills/klai-app-remix-preview/` | Workflow redesign / mocked win-back preview |

Each new skill is **self-contained**: `SKILL.md`, `references/`, `assets/`, `evals/`, `LICENSE-THIRD-PARTY.md`, `NOTICE`, `licenses/Apache-2.0.txt`. Packaged copies must not rely on sibling folders.

Bundle: `python3 scripts/validate_skills.py --pack /tmp/klai-design-suite-skills.tgz`

## Content-review corrections (this update)

Verified against the bundle and fixed in-place:

1. **HIGH — live-action guard.** Polish `references/verify.md` Interaction and makeover Behaviour/preservation no longer tell the agent to click save/actions on a connected backend. Inspect effects first; disposable records and isolated services; user's **actual** authorization for that class of action; otherwise mark the fire **blocked**. Visual Dev edits still need no extra approval — that is not a blanket live-action OK.
2. **MEDIUM — contracts.** Route ids, slugs, hooks, named actions, payload shapes preserved by default. Visible **labels** may change. Missing in-scope behaviour is a blocker unless outside agreed scope or **explicitly** accepted (quoted). Hypothetical "owner can accept" removed from the completion rule.
3. **MEDIUM — CSS-only makeover.** Done is judged by perceptible type, spacing, hierarchy, components, states. Preserved schema/class ids do not fail a real CSS visual-system replacement. Hue-only is not a makeover. Gratuitous markup/schema churn is a defect.
4. **LOW — direction entry.** Read-only is a scope boundary, not a confirmation question. Polish table example and pass order now start with action/accessibility, not spacing.

Eval fixtures added for those four contracts.

## Source license handling (re-verified 2026-11-07)

Read as text only; nothing installed or executed. Re-checked in this update:

| Source | License re-check | Notices now in each skill |
|---|---|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache 2.0, Copyright 2025 Paul Bakaus. **No** repo-root NOTICE (HTTP 404). | `licenses/Apache-2.0.txt` (official Apache text), copyright in `NOTICE`, change notes in `LICENSE-THIRD-PARTY.md`. Adapted methods, not a copy of Impeccable files. |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Apache 2.0, Copyright Microsoft. **No** repo-root NOTICE (HTTP 404). | Same Apache file + NOTICE line. No command table copied. Reel identity **uncertain**. |
| [heydamir/unslop](https://github.com/heydamir/unslop) | CC BY 4.0 (LICENSE at repo root). Creator Damir Sokolovsky. | Credit, license URI, change notes, **as-is / Section 5 disclaimer**. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | MIT, Copyright (c) 2026 Leonxlnx (LICENSE). | Copyright + MIT permission/disclaimer text in `LICENSE-THIRD-PARTY.md`. |
| [designlang@12.16.0](https://cdn.jsdelivr.net/npm/designlang@12.16.0/package.json) | MIT per package.json, author masyv. No separate copyright year in that package.json. | Author + MIT named; skill text not copied; must not install. |

These skills are original instruction text. Apache §4 notices are included because methods were adapted from Apache-licensed documentation. If a lawyer later treats them as fully independent, the bundled Apache file is still accurate attribution, not a claim that Klai assigned copyright to those authors.

## Actual checks run

- `python3 scripts/validate_skills.py` — frontmatter, in-skill links, NOTICE + Apache-2.0.txt presence, CC BY change notes + as-is disclaimer, MIT copyright/permission notice, selection + contract fixtures, remix untouched.
- Manual grep for the four loopholes after the edit.

## Limitations / unrun (truthful)

- **No live Klai app** was polished or made over. Browser verification procedures were not executed against a client app.
- **No Playwright / designlang install.**
- **Skill registry / bots / Mac copies:** not written. Merge awaits Charles.
- **main raw URLs** for the three new skills are not valid until merge.
- License review here is based on the upstream LICENSE/package.json files fetched on 2026-11-07, not a legal opinion.

## Pending (explicit)

1. Charles reviews this branch/PR.
2. Merge to `main` — **not done**.
3. Bot/skill-registry install — **not done**.
