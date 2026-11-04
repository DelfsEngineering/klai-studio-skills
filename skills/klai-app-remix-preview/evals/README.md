# Evals
Re-run all three scenarios after every edit to this skill (and when the model changes). Read the run's record and check each expected behaviour; a skill edit ships only when all pass.

Common expectations for every scenario:
- A user profile is written before any design work, and the record ties major choices to it.
- No page is recolour-only; before and after screenshots exist for every page.
- Parity file has no pending items; every gap has a reason.
- requestHook is false on every page and zero requests reach the backend or helper.
- No preset or copied styling.

Scenarios: `filemaker-app-with-roles.md`, `phone-first-field-app.md`, `desk-admin-app.md`.
