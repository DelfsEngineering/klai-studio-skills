# Design-suite selection scenarios

Machine-readable copy: [design-suite-selection.json](design-suite-selection.json).

Used by `scripts/validate_skills.py` to check that each skill's description and WHEN sections still distinguish the four jobs. Remix `SKILL.md` is **read-only** here; if remix's own WHEN is too generic to match, the fixture still expects remix for workflow-redesign prompts via keywords in *new* skills' handoff tables plus remix's existing "remix / win-back / redesigned demo" description.

| ID | Request (generic) | Expected skill |
|---|---|---|
| dir-brief-only | Write a visual design direction for this field-service app from the users and brand. Do not edit screens. | klai-design-direction |
| dir-brand-extract | Extract a visual brief from our authorized public website; no UI changes. | klai-design-direction |
| polish-keep-look | The dashboard looks sloppy. Keep the brand and layout; tighten spacing and states. | klai-ui-polish |
| polish-unslop-nav | Remove the glow on the nav; do not change workflows. | klai-ui-polish |
| makeover-new-look | Give this app a new look and feel but keep every workflow and permission the same. | klai-ui-makeover |
| makeover-filters-bar | Rearrange the filters into one bar; same jobs; new visual system. | klai-ui-makeover |
| remix-winback | Remix this at-risk client's app with a new structure and a signature feature on a mocked Dev preview. | klai-app-remix-preview |
| remix-workflows | Redesign the workflows and information architecture of this Klai app as a win-back demo. | klai-app-remix-preview |
| dir-readonly-not-a-question | Direction-first handoff must not ask the user to confirm no UI edits. | klai-design-direction |
| polish-live-side-effect-guard | Connected Dev polish must not fire save/email/pay/delete without actual authorization. | klai-ui-polish |
| makeover-live-side-effect-guard | Connected Dev makeover: inspect effects; block unauthorized live fires. | klai-ui-makeover |
| polish-route-vs-label | Labels may change; route/hook/action ids stay. | klai-ui-polish |
| makeover-route-vs-label | Same id/contract default; labels distinguished. | klai-ui-makeover |
| makeover-no-hypothetical-acceptance | Missing in-scope behaviour is a blocker unless out of scope or explicitly accepted. | klai-ui-makeover |
| makeover-css-only-legitimate | CSS visual-system replacement may keep schema/class ids. | klai-ui-makeover |
