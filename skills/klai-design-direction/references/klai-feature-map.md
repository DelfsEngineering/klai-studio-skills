# Klai feature map (read-only, direction)

Use only tools that exist on the current connection. Do not invent endpoints, resource names, or parameters. If a tool is missing, skip that row and write the gap.

This map is for **evidence**. Direction does not write. For writes, polish and makeover ship their own copies of a write-capable map.

## What you can usually discover

| Question | Tool (when present) | Notes |
|---|---|---|
| Which orgs, servers, apps, environments | `list_apps` (OAuth / Klai Studio v2) | App API keys often cannot list apps. Do not pick a server for the user when several exist if a later skill would need that choice; direction only needs to know which app you were asked to look at. |
| Pages | `list_records_overview` collection `pages` | id, name, layout slug. |
| One page's jobs | `get_entity_detail` collection `pages` | Start `_path=form`. Then `pages[0].schema.fields` with `_keysOnly` / `_maxDepth`. HTML via field `.html` slices. Follow `_readRecipe` and `_suggestions`; do not guess alternate roots. |
| Named actions | `form.namedActions` (may need batched reads; may fail as a subpath) | Record name and what it does for the user. |
| Components | `list_records_overview` collection `components` | Shared widgets. |
| Files | `file_assets` | Logos, images already in the app. |
| Shell, nav, theme, CSS | `get_entity_detail` collection `sites` | `content.navigation`, layouts, slots, header, theme, css. Site counts for later writes come from sites reads, not from page saves. |
| Data bindings | `model`, `modelDev`, page hooks, `form.requestHook` | Direction notes live vs mock; it does not change them. |
| Environment URL / kind | `manage_environment` action `get` | Dev vs prod. Direction never deploys. |
| Roles | page/site fields when present | Map existing roles only. |

Guides (`guide_html_v8`, `assistantGuide_slots`, `assistantGuide_fileMaker`, `app_ai_guidance`, `assistantGuide_SITE_SCHEMA_REFERENCE`, `assistantGuide_mcp_schema_save`, …) are MCP **resources** on Klai Studio v2 when that is how the session is configured. Fetch a guide when you need it. A `get_guide` tool result is not automatically the same thing; if the team rule is resources-only, follow that.

`get_entity_detail_legacy` is a fallback for truncated namedActions, not a default.

Images from `get_images` are stock placeholders. They are not brand evidence.

## Operate vs cover
If a page is a splash, brochure, or "enter the app" cover, tag it marketing. If it lists work, edits records, or completes a job, tag it operate. Settings and logs are operate. Help articles are read.

## Stop condition
You have enough when you can fill audience/jobs (or mark them Guess), list the main surfaces, and say whether a real brand file or public site exists. You do not need every HTML chunk.
