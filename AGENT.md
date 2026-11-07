# klai-studio-skills

Agent skills for Klai Studio work. Each skill lives in `skills/<name>/` in Agent Skills layout: `SKILL.md` plus optional `scripts/`, `references/` and `assets/`. To use one, point your agent's skills directory at this repo's `skills/` folder, or copy the skill folder into it. Each skill's instructions are in its own `SKILL.md`. A copied folder must include every relative file that `SKILL.md` names (`references/`, `assets/`, `evals/`); skills do not load files from sibling skill folders.

Validate layout, in-skill links, required source credits, and direction/polish/makeover/remix selection with `python3 scripts/validate_skills.py`.

These skills are public. Never commit secrets or credentials.

## Choosing a design skill

Pick one. If the request spans two jobs, finish the first skill's exit criteria, then hand off. Do not merge them into one pass.

| Job | Skill | Owns | Does not own |
|---|---|---|---|
| Evidence-based visual brief | `klai-design-direction` | Audience, jobs, character, materials, 1–2 signature moments, brand extraction with provenance | Editing UI, changing flows |
| Better execution of the current look | `klai-ui-polish` | Spacing, type, tokens, states, contrast, overflow, component consistency | New visual system, new IA, new jobs |
| New look, same product | `klai-ui-makeover` | Replacement visual system; may rearrange presentation | New workflows, permission or data-contract changes |
| Workflow redesign / win-back preview | `klai-app-remix-preview` | Mocked Dev remix with profile-driven structure and a signature feature | Craft-only polish of the live look |

Working-app screens (task UI) and marketing/cover screens are different modes. Direction, polish and makeover each say how. The remix skill keeps its own written rules; do not reinterpret them from these three.

**Pending merge:** `klai-design-direction`, `klai-ui-polish` and `klai-ui-makeover` land on a review branch. They are not on `main` until Charles merges. Do not treat `main` raw URLs for those three as authoritative until that merge. Remix stays the published skill on `main`.

## Skills

### klai-design-direction
- What it does: writes a visual brief from who uses the app, what they do, and authorized brand evidence. No UI edits.
- When to use it: someone asks for design direction, a visual brief, brand extraction, or how the app should look before any restyle.
- Load on demand: this folder's `SKILL.md`, then only the files it names under the same folder.

### klai-ui-polish
- What it does: raises craft on the current visual system without changing workflows or information architecture.
- When to use it: someone asks to polish, tighten, unslop, or fix spacing, type, states, contrast or overflow, and the look is already the right direction.
- Load on demand: this folder's `SKILL.md`, then only the files it names under the same folder.

### klai-ui-makeover
- What it does: replaces the visual system and may rearrange presentation, while preserving functionality, permissions and data contracts.
- When to use it: someone asks for a UI makeover, a new look and feel, or a visual redesign that keeps the same jobs and flows.
- Load on demand: this folder's `SKILL.md`, then only the files it names under the same folder.

### klai-app-remix-preview
- What it does: builds a redesigned, fully mocked preview ("remix") of an existing client's Klai Studio app in a new Dev environment. The design follows a written profile of the app's real users. The skill then verifies the preview.
- When to use it: someone asks for a remix, a win-back preview, or a redesigned demo of an existing client's Klai app.
- Load on demand: fetch https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/SKILL.md, then fetch only the files under https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/ that it points to.
