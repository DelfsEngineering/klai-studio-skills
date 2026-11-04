# Lessons
Read before the redesign (step 7). Add an entry only after the same failure shows up in more than one run; note the runs that triggered it.

## Anti-example
An earlier run only recoloured the copied pages; layouts stayed the same as the source. It chose a theme that ignored the actual users and how they work. The logo was tiny and the cover text was unreadable. None of it came from asking who uses the app. Lesson: start from the user profile and let every design choice follow from it.

## Tool quirks
- A component remove or a site-setting save (for example clearing an analytics ID) can report success without taking effect. Re-read after every delete or clear; if it didn't take, log it with `Klai Studio v2:report_issue` and flag it for manual clearing. Seen twice on 2026-10-29.
- Clearing helper database fields on a site may not be allowed through the tools. Avoid setting them in the first place (step 5) and flag any carried-over value.
- API-key connections cannot run `list_apps`, `create_app` or `deploy`; use the OAuth connection for writes.
- Pages opened cold may log a harmless console error; note it rather than chase it unless it breaks the page.

## Dated notes
- 2026-10-29: settled that remixes go in a new environment on the source's own app (same app, same org) so `duplicate_page` can copy pages intact.
- 2026-10-29: early runs tested only at phone width and skipped an end-to-end click-through of the main flow; step 13 now requires every width and full flows.
- 2026-10-29: the cover must be readable in every theme with a confident logo size; an earlier dark theme failed contrast.
