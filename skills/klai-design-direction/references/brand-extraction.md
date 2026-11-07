# Brand extraction with provenance

Take tokens from an authorized public reference so the app can belong to the same organisation. Do not clone the reference's layout, section order, or distinctive component structures.

This method is an original write-up inspired by the *kind of outputs* a design-language extractor produces (palette, type, spacing base, components, contrast). It does **not** run `designlang`, `npx`, or any other installer. Upstream skill text was not copied. See [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md).

## Authorization
Proceed only when at least one is true:

- The user named the URL or file and asked you to match it.
- The page is the client's own public site or a brand PDF they supplied.
- The owner said "use our website" and gave the address.

Do not use a competitor, a template gallery, or a site whose design license is unknown as a layout source. If you are unsure whether you may use it, extract nothing expressive; ask, or stick to facts the owner stated.

## Do not install or execute remote extractors
No `npm install`, no `npx designlang`, no cloned upstream scripts, no `postinstall` browser downloads. If a tool is already present in the environment, still prefer manual inspection so this skill stays portable. Never execute code fetched from the reference site. Do not submit forms, check out, or click purchase/contact on the reference site; computed-style reads and screenshots are enough.

## Manual extract (sanctioned browser or given files)

Work in this order. Record as you go in `BRAND.md` next to the direction.

1. **Identity assets.** Logo SVG/PNG from the owner or from the site's own files, not a screenshot redraw. Note light and dark versions if both exist.
2. **Colour.** From computed styles on large surfaces and on the primary button/link, not from a hero photograph. Capture:
   - background / raised surface / hairline
   - primary text / secondary text
   - accent used for action or selection
   - semantic success/danger only if they are clearly systematic
   Hex or `oklch` as observed. If the site uses a gradient as decoration, do not import the gradient; note "accent appears in marketing as a wash; we keep the endpoint colour only" when that is the honest reading.
3. **Type.** Family names from computed `font-family` (or from a webfont stylesheet). Note weights actually used. Do not download font files unless the owner has a license path; if the Klai app cannot host that face, record the intended family and a licensed substitute, labelled as substitute.
4. **Spacing and radius.** A repeating base (often 4 or 8px) and a small set of radii for controls vs cards. Measure two or three components, not one.
5. **Components as vocabulary, not as markup.** "Text button + filled primary", "underline tabs", "row height ~40px". Do not copy class names or DOM.
6. **Voice.** Three short phrases from their site that sound like them. No new claims.

Photograph-heavy marketing pages: take colour from chrome and type, not from the photo.

## Provenance line (required on every token)

```
accent: #1F4B3A
source: https://example.com (owner-authorized public site)
observed: header CTA computed background, 2026-11-07
confidence: Observed
used-as: primary action and selection only
```

If two pages disagree, say so and pick with a reason (more frequent, more recent, closer to the logo).

## What not to copy
- Grid, hero split, card counts, illustration style, distinctive motion.
- Stock photos from the reference page.
- Their product UI chrome if they are a different product (you want *brand*, not *their app*).

## Confidence and gaps
If the browser cannot open the URL (auth wall, network policy, CAPTCHA), mark extraction **blocked**. Do not invent a palette and call it theirs. Continue the rest of the brief from audience and jobs; leave brand as "stated by owner" or "gap".

## After extraction
Feed tokens into the direction: accent role, type for operate vs cover, what stays quiet. The makeover or polish skill applies them. This skill stops at the brief.
