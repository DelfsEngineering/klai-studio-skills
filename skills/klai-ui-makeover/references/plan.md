# Scoped reversible plan

Write `PLAN.md` in the run folder before the first visual save. The point is to change the look in an order you can unwind without data migration.

## Scope
- In: pages, shell, shared CSS, shared components you will restyle.
- Out: production, credentials, helper DB, new features, other apps.

Default target: the existing **Dev** environment of this app. Do not create a new remix env. Do not deploy prod.

## Order of work (reversible layers)
1. **Site tokens and CSS** — colour roles, type, radius, density, focus, selection, scrollbars. One place. Easy rollback: restore previous CSS from the pre-save read.
2. **Shell / slots / nav styling** — header, sidebar, cover frame. Keep **route ids**; visible labels may change.
3. **Shared components** — buttons, inputs, tables, dialogs.
4. **Pages** — presentation rearrangements, still bound to the matrix.
5. **Cover** last or in parallel if it is marketing-only; do not leave inner pages in the old world and a new cover (or the reverse) as the finished state.

Save CSS before you rewrite every page so a failed page does not leave a half-tokenized app with no system. A token/CSS replacement that keeps schema and class ids is a valid makeover if type, spacing, hierarchy, components and states actually change. Do not churn markup ids to look busy.

## Rollback
Keep in the record:

- Pre-change site CSS and nav snippet (path + hash or excerpt).
- Pre-change component ids you will patch.
- What you will **not** attempt to roll back (do not cache live business data).

If a save succeeds in the tool but re-read shows no change, log it, do not pile more ops. Same class of quirk remix already documented: some clears report ok and do nothing.

## Presentation rearrangements (allowed)
Examples that keep the job:

- Filters in one bar instead of three stacked cards.
- A dense table instead of equal image cards when there are no real images.
- Detail fields in two columns on 1280, one column on 390.
- Destructive action moved from the header into a labelled footer, still present.

Examples that are **remix** (stop):

- Adding a calendar when there was only a list, as a new way of working.
- Merging two roles.
- A new "signature" module.

## Guides
Immediately before each kind of edit, fetch the matching MCP resource. Do not work from memory of another app.

## Batching
Do not screenshot after every token tweak. Finish a layer, then look at 390 and 1280 once, then continue.
