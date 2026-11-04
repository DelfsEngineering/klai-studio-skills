# Inventory recipe
All reads go through the source connection. Write results to a file as you go; it becomes the parity list.

1. Pages: `list_records_overview` (collection pages) for the source site. Record id, name and layout slug for each.
2. For each page, with `get_entity_detail`:
   - read `form`, then `pages[0].schema.fields` with keysOnly first, then each field, including nested `fields[n].fields[m]`;
   - read `form.namedActions` in full, using `_itemStart` batches until `hasMore` is false;
   - page through large HTML with the slice parameters; never stop at the first chunk.
   Always read the response's `_readRecipe`, `_suggestions` and errors before the next call.
3. Components: `list_records_overview` (components), then each component's props and actions.
4. Site: navigation (`content.navigation`), layouts, slots and header insertions.
5. App data and model: `model`, `modelDev`, data sources, and the hooks each page calls.
6. Roles, theme, CSS and file assets.

Output: a numbered list of pages, fields, actions (with what each is for), components, nav items and hooks. Copy each item into the parity file (`assets/parity-checklist.json`) with status `pending`. Note anything read only partially and why.
