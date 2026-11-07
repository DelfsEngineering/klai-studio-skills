# Klai feature map (makeover)

Real tools only. Missing tool → gap in the record, not a made-up call.

## Discover
Same reads as polish: `list_apps`, `manage_environment get`, `list_records_overview` (pages, components, file_assets), `get_entity_detail` on pages (`form`, fields, html slices, namedActions) and sites (nav, slots, layouts, css, theme). Follow `_readRecipe`. Roles from existing data only.

`list_apps` / env writes need OAuth. API-key connections are often read-or-bound to one app.

Guides as MCP resources at the point of edit: `guide_pageSchema_v8`, `guide_html_v8`, `guide_javascript_v8`, `assistantGuide_slots`, `assistantGuide_SITE_SCHEMA_REFERENCE`, `assistantGuide_mcp_schema_save`, `assistantGuide_fileMaker` (only if you must understand a hook you are preserving), `app_ai_guidance`. If this team's rule is that `get_guide` never counts, do not treat it as the fetch.

## Write (Dev)
- `mcp_update_schema` `update_page` / `update_site` (and component ops when that is how shared widgets are stored).
- Ops patches. Unique `replaceInString` for large HTML.
- Site modification counts from **sites** reads, not echoed page saves.
- Re-read after every save.
- Do not create a remix environment. Do not `duplicate_page` unless you are copying inside the same Dev app for a reason in the plan (rare; usually you restyle in place).
- Do not set credentials, helper DB, analytics IDs.
- Do not production deploy. Do not production lock/unlock as a side effect.

## Isolation
Makeover of a connected app keeps its data connections. Isolated mocked previews keep theirs. Do not globally force `requestHook: false`; that is a remix preview rule.

## report_issue
When a documented platform quirk blocks a reversible visual change, log it rather than looping silent failures.
