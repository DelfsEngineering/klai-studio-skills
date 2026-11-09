# Changelog
Newest first. Each entry: date, what changed, why, which run or request prompted it.

## 2026-11-08: data-model guides
- What: added `guide_dataModelsApp_v8` and `guide_dataModelsPage_v8` to the guides fetched before a save. Read them before saving a value that has to be there on a later page.
- Why: those guides already cover the app model and page data model. The skill was not sending the run to them.
- Prompted by: SCORRA remix review; Charles, 2026-11-08.

## 2026-11-04: principles and gates
- What: replaced the 18-step checklist with three hard gates (A: profile, inventory and parity file, guides read as MCP resources, user-chosen server before the first save; B: browser check at 390px and 1280px in every theme with screenshots, zero backend requests, FAILED if no browser; C: never worse than the source) plus principles. LESSONS.md, the changelog and the email template are now shoulds. Added a start-of-run rule to compare any local copy with GitHub main and follow GitHub if they differ.
- Why: a run followed a stale local copy and skipped steps one by one.
- Prompted by: post-mortem of the Purr & Pour remix run; Charles, 2026-11-04 call.

## 2026-10-29: restructure
- What: split into SKILL.md (Inputs, three tiers, numbered workflow, verification-loop DoD) plus references/, assets/, LESSONS.md, CHANGELOG.md and evals/. Moved targeting and open questions to the campaign page; moved people, template apps, backend name into Inputs and a team config note.
- Why: skill-writing research (18 proposed changes) for a lean, client-agnostic, verifiable skill.
- Prompted by: owner request on the 2026-10-29 call.

## 2026-10-29: client-agnostic pass
- What: removed client names, domains and IDs; anti-example made generic; source connection described generically.
- Why: the skill must be reusable across clients.

## 2026-10-29: user-profile-first rewrite
- What: step 1 became the user profile; preset theme directions and styling examples removed; real redesign made the default with preservation as the end check; anti-slop design principles added.
- Why: a run recoloured pages and picked a theme that ignored the real users.

## 2026-10-29: earlier revisions
- Target placement set to a new environment on the source app; naming check added after the browser check; all data calls mocked with an upgrade path note.
- 2026-10-29: Cover headline is "We remixed {App name}" (Charles).
