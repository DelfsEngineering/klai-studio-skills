# Klai feature map (polish)

Only real tools. If the session does not have one, skip and record the gap. Do not invent APIs.

## Discover
| Need | Tool | How |
|---|---|---|
| Apps / envs | `list_apps` | OAuth. Confirm you are on Dev, not prod. API-key connections may already be bound to one app. |
| Env metadata | `manage_environment` `get` | Preview URL, kind. Do not `update` lock/credentials/deploy for polish unless the user explicitly asked for a Dev preview URL fix; default is no env mutation. |
| Pages | `list_records_overview` `pages` | Scope list. |
| Page form | `get_entity_detail` `pages` `_path=form` | requestHook, namedActions, layout. Follow `_readRecipe`. |
| Fields / HTML | `pages[0].schema.fields` keys first, then `.html` slices | Prefer `replaceInString` later for one-line HTML. Nested `fields[n].fields[m].html` when needed. |
| Components | `list_records_overview` `components` | Shared controls. |
| Site CSS, nav, slots, theme | `get_entity_detail` `sites` | Patch via `update_site` only for tokens/shell you are polishing. Site `recModCountSite` from **sites** reads. |
| Assets | `file_assets` | Existing logos. |

Guides: fetch as MCP resources at the point of edit (`guide_html_v8`, `guide_javascript_v8`, `guide_pageSchema_v8`, `assistantGuide_slots`, `assistantGuide_SITE_SCHEMA_REFERENCE`, `assistantGuide_mcp_schema_save`, `app_ai_guidance`). Team rule in remix: `get_guide` output does not count when resources are required — follow the same when this session is configured that way.

## Write (Dev only)
- `mcp_update_schema`: `update_page`, `update_site`. Ops patches, not whole blobs.
- Read `assistantGuide_mcp_schema_save` before the first save.
- Re-read the path after save. Success reports can lie.
- Do not `duplicate_page`, `create_page`, or create environments as part of polish.
- Do not set credentials or helper database names.
- Do not deploy to production. Deploying a Dev environment only if the user needs a preview refresh **and** that is a documented Dev action — still never prod.

## Do not use
`get_images` as brand. `get_entity_detail_legacy` except as a namedActions fallback. Any FileMaker write. Email, Notion, iMac MCP.

## requestHook
Leave it. Polish is not a mocked remix. Isolated mocked previews keep whatever isolation they already have.
