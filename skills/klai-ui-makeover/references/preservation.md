# Preservation matrix

A makeover is allowed to change presentation. It is not allowed to lose a job or rename contracts. The matrix is the contract.

Inspired by remix parity (kept / moved / gap) but **this is not remix**: there is no signature feature, no mocked-only rule, no required new environment. Do not copy remix gates into this file.

## What must survive (identifiers by default)
- Pages a user can reach, under the **same route ids / layout slugs**.
- Fields and their bindings (same data, same requiredness, same field ids).
- Named actions and hooks: **same names** and same payload shapes. Do not rename an action or hook because nothing appears to call it. Call-style may change (`action('x')` → `namedAction('x')`) for the same `x`.
- Roles and who can run what.
- Nav **destinations** (route ids). Visible **labels** may change when the wording was false; that is a label change, not a route change. Record both.
- `requestHook` intent (live stays live on a connected app).
- Theme count: do not drop a theme people use; you may restyle it.

## What may change
- Layout, type, colour, density, component look — including a CSS-only token replacement that keeps schema and class ids.
- Grouping on a page (filters in a bar instead of a stack).
- Table vs cards when the job is still "find one row and act".
- Cover presentation.
- Shell colours, logo size, slot styling.
- Visible labels (not ids) when the user asked to fix wording.

## Gaps are not hypothetical
Missing in-scope behaviour is a **blocker**. A `gap` is allowed only when:

1. it is demonstrably **outside the agreed scope** of this run (named pages/flows left out on purpose), or
2. the owner **explicitly accepted that specific gap** in this run — quote the chat/message in the record.

"A reason the owner can accept" is not enough. Do not invent acceptance.

## Matrix columns
Use [assets/preservation-matrix.md](../assets/preservation-matrix.md).

| Field | Meaning |
|---|---|
| id | Stable: `page:{id}`, `action:{name}`, `hook:{name}`, `role:{name}`, `nav:{route-id}` |
| job | What the user accomplishes |
| presentation_now | Short |
| presentation_after | Short; same job |
| label_now / label_after | Visible copy only; ids stay |
| status | `pending` → `kept` (same place) / `moved` (where) / `gap` (see gap rules) |
| permissions | Unchanged? |
| data | Shape unchanged? |
| ids_unchanged | Route/hook/action ids still the same |

Done when no `pending`. `gap` without an out-of-scope proof or an explicit quoted acceptance is a fail.

## Inventory recipe (real tools)
Follow [klai-feature-map.md](klai-feature-map.md):

1. Pages overview.
2. Each in-scope page: form, fields keys, namedActions, hooks.
3. Site nav, slots, themes, CSS.
4. Roles if present.
5. Components that implement shared actions.

Partial reads: list which pages were not opened and treat them as out of scope or as `pending` you still owe.

Do not delete pages because they are ugly. Flag orphans for the owner; deleting them is a gap that needs explicit acceptance.

## Behaviour verification (not screenshots)
For each `kept`/`moved` action: the same role can still **reach** it, with the same id. Do not fire save/delete/email/pay on a connected backend unless the user actually authorized that class of consequential action in this run. Inspect effects first; prefer disposable records and isolated services; otherwise mark the fire **blocked**. If you cannot log in as a role, mark that role **unrun**.

## Recolour-only vs CSS visual-system replacement
Judge **perceptible** typography, spacing, hierarchy, component vocabulary, and states — not whether schema or class **ids** changed.

- **Legitimate makeover:** site CSS/tokens replace type scale, spacing rhythm, hierarchy, component look and states, even if field ids, class names, and named actions are unchanged. Do not churn markup or schema to look busy.
- **Not a makeover:** only the hues moved; type, spacing, hierarchy, components and states are the source's. That is polish (or an incomplete makeover). Switch or keep going until the craft actually changed.
- Gratuitous id/class/schema churn is a defect, not a completion signal.
