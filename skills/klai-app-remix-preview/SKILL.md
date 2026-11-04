---
name: klai-app-remix-preview
description: >-
  Builds a redesigned, fully mocked preview ("remix") of an at-risk client's
  Klai Studio app in a new Dev environment, driven by a written profile of the
  app's real users, then verifies it and drafts the "we remixed your app" email
  for the owner. Use when someone asks for a remix, win-back preview, or
  redesigned demo of an existing client's Klai app.
---
# Klai app remix preview

A remix shows a client their own app, redesigned for the people who actually use it and extended with one or two new features. It is a preview on Dev with mocked data, never a change to their live app.

## Inputs
The caller supplies these; every step refers to them by name. Defaults come from the team config note at the end.
- **App name**: the client's app as they know it.
- **Source connection**: the read-only MCP connection to the client's source app (an app API-key connector).
- **Org**: the Klai organization that owns the source app.
- **Target app/env**: where the remix goes. Default: a new Development environment named "Remix Preview" on the source app.
- **Frozen copy**: a frozen bookmark copy of the source, if one exists.
- **CS account**: the client's CS account notes (goals, pain points, history).
- **Owner**: who reviews the result and sends the email.
- **Contact**: the client person the email is addressed to.
- **Backend type**: the client's data backend (for example a database server and helper file).
- **Source-of-truth doc**: the page this skill is synced with.
- **Template apps**: finished remixes to look at for quality bar, not for styling.

Missing CS notes, contact or helper details do not stop a run; record what was missing.

## Tier 1: hard constraints
Each is stated only here; later steps rely on it.
- Build on Dev only, because a preview must never put the client's live app or data at risk.
- Treat the source connection as read-only, because it reaches the client's real app.
- Leave the frozen copy, if one exists, untouched, because it is the fixed baseline for testing this skill.
- Mock every data call, set no backend credentials and no helper database, because the preview must never touch the client's backend.
- Set `requestHook` to false on every page, because any live hook would leak a request to the backend.
- Never send email as the owner; draft it, because outreach is the owner's call.
- Put the remix in a new environment on the source app (same app, same org), because `duplicate_page` only copies within one org. If that is impossible, use another Dev app and log why.
- Build the remix on V3, because older versions are being retired.

## Tier 2: principles (use judgment)
- The user profile from step 1 drives every design choice. There are no preset themes or styles; pick the direction from the profile and justify major choices against it in the record. One theme by default; add a second only if the profile gives a reason.
- Redesign is the goal: rework layout, structure, type, spacing and components on every page. Rewriting page HTML is expected; a layer that only recolours the source's classes is not a remix.
- Preservation is the end check, not the target: every field, binding, named action and hook call must still do the same job for the user, while the markup around it can change completely (step 15).
- Outside the cover page the app should feel real: same flows as production, realistic mock data in the client's domain, the client's real catalog, no demo banners.
- Follow `references/design-principles.md`. Any principle can be broken when the profile calls for it; note it in the record.
- Examples policy: the core holds no styling examples. If examples are ever added, give three or more deliberately diverse ones in `examples.md`, labelled "illustrative, do not copy".

## Files in this skill
- `references/inventory.md`: the MCP read recipe for step 2.
- `references/design-principles.md`: anti-slop principles and their sources.
- `assets/email.md`: the email draft for step 16.
- `assets/parity-checklist.json`: schema for the parity file (steps 2 and 15).
- `LESSONS.md`: anti-example, tool quirks and dated notes. Read before step 7.
- `CHANGELOG.md`: dated history of this skill.
- `evals/`: three test scenarios; see `evals/README.md`.

## Connections
- Source connection: reads only (`list_records_overview`, `get_entity_detail`).
- `Klai Studio v2` (OAuth): all writes on the target app/env: `Klai Studio v2:list_apps`, `Klai Studio v2:manage_environment`, `Klai Studio v2:mcp_update_schema` (including its `duplicate_page` op), `Klai Studio v2:get_entity_detail`, `Klai Studio v2:list_records_overview`, `Klai Studio v2:report_issue`. API-key connections cannot list apps, create apps or deploy.

## Tier 3: workflow
Copy this checklist into the run's record and tick it off:
```
[ ] 1 user profile        [ ] 2 inventory         [ ] 3 assess
[ ] 4 roles               [ ] 5 environment       [ ] 6 duplicate_page base
[ ] 7 read LESSONS.md     [ ] 8 page redesign     [ ] 9 signature feature
[ ] 10 extensions         [ ] 11 cover            [ ] 12 stub data calls
[ ] 13 quality + browser  [ ] 14 naming check     [ ] 15 parity
[ ] 16 cover image+email  [ ] 17 record           [ ] 18 changelog
```
1. User profile. Write down who opens the app: role, device, setting, what they need fast, and age, eyesight and tech comfort when known. Use the CS account, the source's content and what the owner said; mark guesses as guesses.
2. Inventory (source connection). Follow `references/inventory.md` and write the result to a file, plus a parity file from `assets/parity-checklist.json` with every item `pending`. Note partial reads and why.
3. Assess. List every data call and its payload shape (each becomes a stub), what is dated or hard for the profiled user, and 3 to 5 logical extensions.
4. Roles. Map them only when the app has roles; don't invent them.
5. Environment (`Klai Studio v2:manage_environment`). Create the target app/env, preview then confirm. Don't carry over analytics IDs, test components or helper database names.
6. Base (`Klai Studio v2:mcp_update_schema` duplicate_page). Copy every source page and register its layout slugs. If duplication isn't possible, rebuild from the inventory and log each fallback.
7. Read `LESSONS.md`.
8. Redesign page by page. Set shared tokens and CSS on the site and confirm they deployed. Rework each page for its job and the profiled user, checking it against `references/design-principles.md`; in HTML call `namedAction('name')`, not `action('name')`. Take before and after screenshots of each page; if a page still looks like the source, it isn't done.
9. Signature feature. One extension the client would want at once, working on mock data, with a visible New tag.
10. Extensions. Working UI over mock data only.
11. Cover. "We remixed {App name}" plus a small "Klai Remix · Preview" label, the client's logo at a confident size, readable in every theme. Show what changed and the signature feature, then "Explore your remix"; one tile per role if there are roles. The only page that says it's a preview: it runs on sample data, and copying the source hooks makes it live.
12. Stub data calls. Replace each call from step 3 with a local mock of the same shape (model or named action), and keep a stub list.
13. Quality and browser check. On the profiled device first, then desktop, tablet and phone in each theme: click every page, button, tile, role and theme; look for overlap, clipping, horizontal scroll, and empty, loading and error states. Watch the request log.
14. Naming check. Compare each page name with what the page now shows and does; rename misleading ones to a plain name the client would recognize. Leave hook names and route slugs unless nothing calls them. Log old, new and why; flag empty or orphaned pages for the owner instead of deleting them.
15. Parity. Mark each item in the parity file `kept`, `moved` (with where) or `gap` (with reason). Fix gaps you can.
16. Cover image, then draft the email from `assets/email.md` for the owner.
17. Record: profile and how choices follow from it, app and environment ids, preview URL, source connection, inventory and parity files, signature feature, stub list, renames, screenshots, principle exceptions, what would make each stub real.
18. Changelog. If the run changed this skill, add a `CHANGELOG.md` entry. Add a new rule only after the same failure is seen in more than one run, and log the triggering runs in `LESSONS.md`.

## Definition of done: verification loop
Run the machine checks, fix what fails, re-run until all pass, then review screenshots.
1. `requestHook` is false on every page (read each page's form).
2. Zero requests to the backend or helper in the request log during step 13.
3. The parity file has no `pending`; every `gap` has a reason.
4. Contrast: text 4.5:1, large text and icons 3:1, in every theme including the cover.
5. Screenshot review: each after-shot checked against step 8 and `references/design-principles.md`, the cover against step 11, every width from step 13.
6. Checklist complete, email drafted not sent, record written (step 17).

## Team config note
Defaults for this team: backend type FileMaker (server plus helper file); owner Charles Delfs; design questions about the New tag go to Pearson; template apps "EOS Traction Board" redesign and "Grant Review Demo".
