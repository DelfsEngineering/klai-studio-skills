# klai-studio-skills

Agent skills for Klai Studio work. Each skill lives in `skills/<name>/` in Agent Skills layout: `SKILL.md` plus optional `scripts/`, `references/` and `assets/`. To use one, point your agent's skills directory at this repo's `skills/` folder, or copy the skill folder into it. Each skill's instructions are in its own `SKILL.md`.

## Skills

### klai-app-remix-preview
- What it does: builds a redesigned, fully mocked preview ("remix") of an existing client's Klai Studio app in a new Dev environment. The design follows a written profile of the app's real users. The skill then verifies the preview.
- When to use it: someone asks for a remix, a win-back preview, or a redesigned demo of an existing client's Klai app.
- Load on demand: fetch https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/SKILL.md, then fetch only the files under https://raw.githubusercontent.com/DelfsEngineering/klai-studio-skills/main/skills/klai-app-remix-preview/ that it points to.

These skills are public. Never commit secrets or credentials.
