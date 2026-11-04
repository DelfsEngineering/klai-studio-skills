# Scenario: older FileMaker-backed app with roles
Setup: a V1 Klai app on a FileMaker backend with three roles (admin, manager, staff), hooks calling FileMaker scripts, and a helper file set on the site.

Expected:
- Remix is V3 in a new Dev environment on the same app.
- Roles mapped from the source only; the cover has one working tile per role.
- Every FileMaker hook and script-running named action is stubbed with a matching payload shape; no credentials, no helper database.
- Helper database name and analytics IDs are not carried to the new site.
- Parity covers each role's pages and actions.
