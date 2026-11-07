# Verification (polish)

Judge the rendered app, not only the CSS you wrote. Batch looks: fix what one pass shows, then look again.

Capabilities below are adapted from common browser-automation features (snapshots, viewports, console, network, reduced motion, contrast, colour scheme). This skill is **not** Playwright CLI and does not claim to match a reel identity. Do not install Playwright or any CLI to satisfy this file. Use a sanctioned tool that is already available. Never bypass login walls, CAPTCHAs, or permission prompts. [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md).

## Tool choice
Pick the first that exists and is allowed:

1. The agent's existing browser tools (open the preview, resize, click, screenshot, console/network if exposed).
2. An already-installed browser CLI in PATH (use it; do not upgrade-install).
3. Owner-supplied screenshots plus honest gaps — only if 1 and 2 are impossible.

If you cannot open the app, mark Gate-equivalent verification **FAILED / blocked**, not skipped, and do not call polish done.

## Viewport matrix
Always:

- **390** wide (phone)
- **1280** wide (desk)

Also, when the layout has columns, data tables, or a collapsing nav — the widths where it actually misbehaves. Common risk points: **768**, **1024**. Do not invent a 12-width grid; add a width when you have a reason (column collapse, table, wrapping actions).

Profiled device first when the direction or user named one (field phone vs desk).

Height: use a realistic phone height (~844) and a desk height (~800–900) so sticky headers and first-screen composition are visible.

## Themes and roles
Every in-scope theme. Every in-scope role if actions differ. Label the shot: `page-theme-width-role`.

## Content states
For each representative page: typical data, **long** strings, **empty**, **loading**, **error**. Permission-denied if roles exist. Do not only photograph the happy path.

## Mocks vs live
Write in the record whether data is live, recorded, or mocked. Never call a mock "production verified".

## Console and network
If the tool can show them, after each main flow:

- Console: new errors you introduced vs pre-existing. Note harmless cold-load errors; do not chase platform noise.
- Network: unexpected failures (4xx/5xx on actions the user just ran).

**Zero backend requests** — check this **only** when the user (or the environment) is an explicitly isolated mocked preview. Ordinary polish of a connected Dev app **will** talk to its backend; that is expected. Do not fail polish for live requests.

## Interaction, not only screenshots
- Click primary jobs.
- Keyboard: tab to the primary action, operate it, escape menus.
- Focus visible.
- `prefers-reduced-motion` if the tool can emulate it; otherwise check CSS and mark emulation unrun.
- Forced-colors / extra contrast if available; else unrun.

Overlap, clipping, unexpected horizontal scroll: fail.

## Coverage vs ambition
A small scoped polish does not need every page in the app. It does need every page you changed, plus the shared shell, at the matrix above.

## Honest blockers
Examples: no browser tool; preview behind owner SSO; MCP cannot list the page; save reported ok but re-read shows old HTML. Write what would unblock. Do not imply a check ran.
