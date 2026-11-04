---
name: klai-app-remix-preview
description: >-
  Builds a redesigned, fully mocked preview ("remix") of an at-risk client's
  Klai Studio app in a new Dev environment, driven by a written profile of the
  app's real users, then verifies it for the owner to review.
  Use when someone asks for a remix, win-back preview, or
  redesigned demo of an existing client's Klai app.
---
# Klai app remix preview

A remix shows a client their own app, redesigned for the people who actually use it and extended with one or two new features. It is a preview on Dev with mocked data, never a change to their live app.

Load on demand: this file is https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/SKILL.md. Fetch the references, scripts and assets it names from https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/<path>, one at a time as each part of the work needs them. Do not clone the repo.

## Use the current skill (required, first)
The first tool call of every run is a fetch of https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/SKILL.md, and the commit hash of main (from https://api.github.com/repos/DelfsEngineering/klai-studio-skills/commits/main) is written into `remix-runs/<source-app-id>/RECORD.md` before any other tool call, including any Klai call. Follow that fetched file. A local copy (for example `.cursor/skills/klai-app-remix-preview/SKILL.md`) or a file already open in the editor does not count as the fetch and never governs the run. If the commit hash is not in the record, the run has not started.

Second step, right after the hash and before the profile, inventory or any building: settle the FileMaker server. List the servers available (for example with `list_apps`). If there is exactly one, say you will use it and note that in the record. If there are several, list them all by name and id and ask the user which to use now, so they can answer early and walk away; do not recommend one, never pick one yourself, and do not treat the source app's server as the default. Only a chat reply naming the server counts. Keep reading the source while you wait, but nothing in Gate A's blocked list happens until the answer is in the record. If a tool later says a server is required (for example MCP_SERVER_REQUIRED), use the recorded choice.

Third step, as soon as the server is in the record: create the empty remix app or environment on that server, so there is something to see while the rest builds, and write its ids and preview URL into the record. Then continue with the profile, inventory, guides and the rest. Creating the empty target needs only the commit hash and the server choice; copying pages, deploying and saving still wait for the full Gate A.

## Before you build (required)
- Run record: a live checklist at a fixed path. As the first step, create `remix-runs/<source-app-id>/RECORD.md` at the root of the working project, with a checklist of every required step (Before you build items, Gates A, B and C, each Definition of done check, closing summary), each marked done or not done. Update it as each piece of work completes, not at the end, and write decisions there as you make them (profile, inventory and parity files, guides read, server picked, gate results). Before moving to the next step, re-read the record, confirm nothing earlier is still open or skipped, and finish anything that is. Keep the inventory and parity files in the same folder. Use this path every run; if a record for that source app already exists, read it first and add a new dated run section.
- Re-read the Klai Studio MCP system prompt at the start of every remix. Do not work from memory of an earlier turn.
- Guides are MCP resources on the Klai Studio v2 server. Fetch each guide as a resource at the point the work needs it, not all up front. If that fetch fails, stop and report the exact error. Do not fall back to the get_guide tool; a get_guide result never counts, even when it returns the guide text.
- Fetch the matching guide right before the work it covers (page schema, HTML, JavaScript, site layouts and navigation, slots, FileMaker behavior, UI and brand), and log each one you read. If one applies and you have not read it, stop and read it before saving:
  - guide_pageSchema_v8
  - guide_html_v8
  - guide_javascript_v8
  - assistantGuide_SITE_SCHEMA_REFERENCE
  - assistantGuide_slots
  - assistantGuide_fileMaker
  - app_ai_guidance

## Inputs
The caller supplies these; the rest of this skill refers to them by name. Defaults come from the team config note at the end.
- **App name**: the client's app as they know it.
- **Source connection**: the read-only MCP connection to the client's source app (an app API-key connector).
- **Org**: the Klai organization that owns the source app.
- **Target app/env**: where the remix goes. Default: a new Development environment named "Remix Preview" on the source app.
- **Frozen copy**: a frozen bookmark copy of the source, if one exists.
- **CS account**: the client's CS account notes (goals, pain points, history).
- **Backend type**: the client's data backend (for example a database server and helper file).
- **Template apps**: finished remixes to look at for quality bar, not for styling.

Missing CS notes, contact or helper details do not stop a run; record what was missing.

## Tier 1: hard constraints
Each is stated only here; the rest of the skill relies on it.
- Build on Dev only, because a preview must never put the client's live app or data at risk.
- Treat the source connection as read-only, because it reaches the client's real app.
- Leave the frozen copy, if one exists, untouched, because it is the fixed baseline for testing this skill.
- Mock every data call, set no backend credentials and no helper database, because the preview must never touch the client's backend.
- Set `requestHook` to false on every page, because any live hook would leak a request to the backend.
- Put the remix in a new environment on the source app (same app, same org), because `duplicate_page` only copies within one org. If that is impossible, use another Dev app and log why.
- Build the remix on V3, because older versions are being retired.

## Gates (hard stops)
Gates block progress. They are not checklist items to tick off one by one: if a gate is not met, stop and meet it before going on. Write each gate's evidence into the run record.

**Gate A: before the first copy, deploy or save into the remix.** Creating the empty remix app or environment is allowed once the commit hash and server are in the record (third step above). No deploy, copy or save call (for example `deploy_environment`, `duplicate_page`, `mcp_update_schema`) until all four are in the record. Reading the source is allowed:
1. A written user profile (see principles).
2. An inventory written to a file per `references/inventory.md`, plus a parity file from `assets/parity-checklist.json` with every item `pending`.
3. The guides from "Before you build" that the first save needs, read as MCP resources, each one logged. `get_guide` output does not count.
4. The server: the only one available, or the one the user chose in chat when there are several. Do not recommend one.
If any is missing, stop. No saves, no duplicated pages, no environment changes until it is met.

**Gate B: deploying is not done.** A remix is not done until a browser check has passed:
- Lint first, before the browser check: scan every page's generated HTML for old-style action calls, that is a call to a function literally named `action` with a string (for example `action('name')`; a regex like `(?<![A-Za-z_.])action\s*\(\s*['"]` finds them). Log each hit in the record, convert it to `namedAction('name')`, save, and re-scan. The browser check does not start until the scan has zero hits.
- At 390px and 1280px wide, in every theme, with a screenshot of each page at each width and theme. Check the profiled device first. Click every page, button, tile, role and theme; look for overlap, clipping, horizontal scroll, and empty, loading and error states.
- Zero requests to the backend or helper in the browser's network log.
- If no browser is available, mark the check FAILED in the record (not skipped) and do not call the remix done.

**Gate C: never worse than the source.** In the browser, compare the remix side by side with the source app at desktop and phone widths, in both themes. If any page has layout gaps, broken spacing, or a theme that looks worse than the source, fix it and re-run Gate B. A remix that looks worse than what it started from is not done.

## Principles (use judgment)
- **The user profile drives everything.** Write down who opens the app: role, device, setting, what they need fast, and age, eyesight and tech comfort when known. Use the CS account, the source's content and what the owner said; mark guesses as guesses. There are no preset themes or styles; pick the direction from the profile and justify major choices against it in the record. One theme by default; add a second only if the profile gives a reason.
- **Know the source before touching it.** The inventory covers every page, layout, data call (with payload shape) and named action; note partial reads and why. From it, list what is dated or hard for the profiled user and 3 to 5 logical extensions. Map roles only when the app has roles; don't invent them.
- **Environment.** Create the target app/env with `Klai Studio v2:manage_environment`, preview then confirm. Don't carry over analytics IDs, test components or helper database names.
- **Duplicating is a baseline, not a redesign.** Copy every source page with `duplicate_page` and register its layout slugs; if that isn't possible, rebuild from the inventory and log each fallback. Then redesign: rework layout, structure, type, spacing and components on every page for its job and the profiled user. Set shared tokens and CSS on the site and confirm they deployed. A layer that only recolours the source's classes is not a remix. Take before and after screenshots of each page; if a page still looks like the source, it isn't done.
  - The site frame is part of the redesign, and it must match the cover. Read `assistantGuide_slots` as a resource, then use the site layout settings and slots to restyle the top bar, header and sidebar to the cover's theme, colours, type and branding: app name and logo, header and sidebar colours, item styling, active state, and every header slot. Re-pointing links or changing one slot is configuration, not restyling. Never leave the platform's default header colour, sidebar colour, Dev Tools or a default title such as "Getting Started". If the cover hides the shell (`hideHeader`), the inner pages' frame must still be restyled; check it on an inner page after navigating in from the cover, in every theme. A remix that redesigns only page content inside a stock frame is not done.
- **Design direction: premium, not minimal (core requirement).** The remix must feel high-end, not minimalist: rich, layered and purposeful, with considered type, depth, imagery, colour and detailed components. Go to town on visual quality. Use subtle animation (transitions, hover and load states) only where it helps the experience, never as decoration. A clean but plain remix is not done.
- **Build pages in sections, not one block.** Where a page has distinct parts, create its HTML as separate grouped section objects (for example header, left side, right side, footer), each its own element in the page schema, rather than one giant HTML block. One block is easier to write but hard for the user to edit later; sections keep each part independently editable.
- **Preservation is the end check, not the target.** Every field, binding, named action and hook call must still do the same job for the user, while the markup around it can change completely. In HTML call `namedAction('name')`, not `action('name')`.
- **Signature feature.** One extension the client would want at once, working on mock data, with a visible New tag. Other extensions: working UI over mock data only.
- **Feels real outside the cover.** Same flows as production, realistic mock data in the client's domain, the client's real catalog, no demo banners.
- **Cover purpose.** The cover is a splash page that announces the makeover, like a launch brochure, not a title card. Before anyone clicks in, it gives a real sense of the remix: show the redesigned app itself (a mobile or desktop snippet, or screenshots of the new look) and frame it as an announcement of what changed and why it is better for the people who use it.
- **Cover.** "We remixed {App name}" plus a small "Klai Remix · Preview" label, the client's logo at a confident size, readable in every theme. Show what changed and the signature feature, then "Explore your remix"; one tile per role if there are roles. The only page that says it's a preview: it runs on sample data, and copying the source hooks makes it live.
- **Stubs.** Replace every data call from the inventory with a local mock of the same shape (model or named action), and keep a stub list.
- **Naming.** Compare each page name with what the page now shows and does; rename misleading ones to a plain name the client would recognize. Leave hook names and route slugs unless nothing calls them. Log old, new and why; flag empty or orphaned pages for the owner instead of deleting them.
- **Parity.** Mark each parity item `kept`, `moved` (with where) or `gap` (with reason). Fix gaps you can.
- **Design principles.** Follow `references/design-principles.md`. Any principle can be broken when the profile calls for it; note it in the record.
- **Examples policy.** The core holds no styling examples. If examples are ever added, give three or more deliberately diverse ones in `examples.md`, labelled "illustrative, do not copy".

## Shoulds
- Read `LESSONS.md` before redesigning.
- If the run changed this skill, add a `CHANGELOG.md` entry. Add a new rule only after the same failure is seen in more than one run, and log the triggering runs in `LESSONS.md`.

## Files in this skill
- `references/inventory.md`: the MCP read recipe for the inventory.
- `references/design-principles.md`: anti-slop principles and their sources.
- `assets/parity-checklist.json`: schema for the parity file.
- `LESSONS.md`: anti-example, tool quirks and dated notes.
- `scripts/check_done.py`: machine checks for done items 1 and 3.
- `CHANGELOG.md`: dated history of this skill.
- `evals/`: three test scenarios; see `evals/README.md`.

## Connections
- Source connection: reads only (`list_records_overview`, `get_entity_detail`).
- `Klai Studio v2` (OAuth): all writes on the target app/env: `Klai Studio v2:list_apps`, `Klai Studio v2:manage_environment`, `Klai Studio v2:mcp_update_schema` (including its `duplicate_page` op), `Klai Studio v2:get_entity_detail`, `Klai Studio v2:list_records_overview`, `Klai Studio v2:report_issue`. API-key connections cannot list apps, create apps or deploy.

## Definition of done
Done means Gates A, B and C passed and all of these hold. Run the checks, fix what fails, re-run until all pass. Checks 1 and 3 are scripted: save each page's form from the target env to `pages.json`, then run `python3 scripts/check_done.py --pages pages.json --parity <parity file>` and keep its output in the record. It must exit 0.
1. `requestHook` is false on every page (read each page's form).
2. Gate B passed, including zero backend or helper requests.
3. The parity file has no `pending`; every `gap` has a reason.
4. Contrast: text 4.5:1, large text and icons 3:1, in every theme including the cover.
5. Screenshot review: each after-shot checked against the redesign principle and `references/design-principles.md`, the cover against the cover principle, and every page against the premium design direction.
6. Gate C passed.
7. Record written: which skill file governed the run, profile and how choices follow from it, app and environment ids, preview URL, source connection, inventory and parity files, guides read, signature feature, stub list, renames, screenshots, gate results, principle exceptions, what would make each stub real.
8. Closing summary at the end of the run: a short list of what shipped and what was skipped or not done. No per-layout tracking.

## Team config note
Defaults for this team: backend type FileMaker (server plus helper file); owner Charles Delfs; design questions about the New tag go to Pearson.
