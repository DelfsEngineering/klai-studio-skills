# Evidence inventory and source confidence

Direction that is not sourced becomes a mood board. Write an inventory before the five-line brief. Store it in the run folder as `EVIDENCE.md` (or a section of `RECORD.md` for a small job).

## What to collect

| Bucket | What good looks like | Typical sources |
|---|---|---|
| Audience | Role, age/eyesight/tech comfort when known, device, setting (desk, cab, shop floor, home), time pressure | Owner, CS notes, page copy, roles in the app |
| Jobs | The 3–7 tasks people actually finish; what they need on the first screen; what they never do in this app | Named actions, nav labels, forms, owner |
| Workflows as they are | Order of pages, required fields, permissions; not the redesigned order | Page list, nav, roles, hooks |
| Brand | Colour, type, logo, voice the client already owns | Authorized public site, logo files, stated tokens |
| Surfaces | Operate vs marketing/cover vs read/help | Page names, cover vs inner pages |
| Constraints | Contrast needs, printer/TV, outdoor glare, shared iPad, legal strings | Owner, setting |
| Incumbent UI | What currently works; what is dated; what users already know how to hit | Screenshots, click-through |

If there is no MCP connection, work from screenshots, a preview URL the user opened, and their words. Say that the app was not read.

## Confidence

Mark every claim:

- **Observed** — you saw it in the app, a public page, or a file. Include where.
- **Stated** — the owner or a supplied note said it. Quote short.
- **Inferred** — two or more observations point here. Say the chain.
- **Guess** — needed to write a complete brief. Must not drive irreversible choices without a label.

A token taken from a live authorized page is Observed. A palette you invented to "feel warmer" is Guess until the owner keeps it.

Do not launder a guess into Observed by writing it in confident tone.

## Source quality for brand

Highest first:

1. Files the owner handed you (logo SVG, brand PDF they said to use).
2. The client's public site or Google Business photos they asked you to match, inspected in a browser.
3. Colours and type already in the Klai theme/CSS that are clearly theirs (logo-derived, not leftover platform indigo).
4. Category conventions (field-service density, restaurant POS glanceability) as *constraints*, not as a copied look.

Never:

- A competitor's layout or component structure.
- Unsplash "industry vibe" as if it were the client's rooms or people.
- A random Dribbble shot as identity.

## Klai reads that count as evidence

When the connection allows, record:

- Page names and layout slugs from `list_records_overview` (pages).
- Roles and which pages they see, when roles exist. Do not invent roles.
- `form.namedActions` purpose in user language.
- Site nav labels (what users think the app contains).
- Theme count and names; whether a cover hides the shell.
- Data that looks live vs clearly sample.

Follow [klai-feature-map.md](klai-feature-map.md). Stop at a useful map; this is not a remix inventory. Partial is fine if you say which pages were not opened.

## Output shape

```
# Evidence
Date, app name as the user said it (no env ids in reusable docs).

## Audience
- … (Observed / Stated / Inferred / Guess)

## Jobs
- Job: …
  First-screen need: …
  Permission notes: …

## Surfaces
- Cover: marketing / none
- Inner: operate (list, detail, complete) / read

## Brand
- Token: #… / family …  Provenance: url or file. Confidence: Observed

## Gaps
- Missing: …
```
