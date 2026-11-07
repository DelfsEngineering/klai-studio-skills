# Preservation matrix

A makeover is allowed to change presentation. It is not allowed to lose a job. The matrix is the contract.

Inspired by remix parity (kept / moved / gap) but **this is not remix**: there is no signature feature, no mocked-only rule, no required new environment. Do not copy remix gates into this file.

## What must survive
- Pages a user can reach (or an explicit gap the owner accepts, e.g. an unused orphan you did not delete).
- Fields and their bindings (same data, same requiredness).
- Named actions and hooks: same names unless nothing calls them; same payload shape.
- Roles and who can run what.
- Nav destinations (labels may change if they were false; destinations stay).
- `requestHook` intent (live stays live on a connected app).
- Theme count: do not drop a theme people use; you may restyle it.

## What may change
- Layout, type, colour, density, component look.
- Grouping on a page (filters in a bar instead of a stack).
- Table vs cards when the job is still "find one row and act".
- Cover presentation.
- Shell colours, logo size, slot styling.

## Matrix columns
Use [assets/preservation-matrix.md](../assets/preservation-matrix.md).

| Field | Meaning |
|---|---|
| id | Stable: `page:{id}`, `action:{name}`, `hook:{name}`, `role:{name}`, `nav:{label}` |
| job | What the user accomplishes |
| presentation_now | Short |
| presentation_after | Short; same job |
| status | `pending` → `kept` (same place) / `moved` (where) / `gap` (reason) |
| permissions | Unchanged? |
| data | Shape unchanged? |

Done when no `pending`. `gap` without a reason is a fail.

## Inventory recipe (real tools)
Follow [klai-feature-map.md](klai-feature-map.md):

1. Pages overview.
2. Each in-scope page: form, fields keys, namedActions, hooks.
3. Site nav, slots, themes, CSS.
4. Roles if present.
5. Components that implement shared actions.

Partial reads: list which pages were not opened and treat them as out of scope or as `pending` you still owe.

Do not delete pages because they are ugly. Flag orphans for the owner.

## Behaviour verification (not screenshots)
For each `kept`/`moved` action: the same role can still reach it and the same kind of result happens (save, print, open, mock return). If you cannot log in as a role, mark that role **unrun**.

## Recolour-only
If after the plan the schema and class names are the source's and only colours changed, you did not do a makeover. Either complete the system replacement or switch to polish.
