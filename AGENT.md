# klai-studio-skills

Agent skills for Klai Studio work. Each skill lives in `skills/<name>/` in Agent Skills layout: `SKILL.md` plus optional `scripts/`, `references/` and `assets/`. To use one, point your agent's skills directory at this repo's `skills/` folder, or copy the skill folder into it. Each skill's instructions are in its own `SKILL.md`.

## Skills

### klai-app-remix-preview
- What it does: builds a redesigned, fully mocked preview ("remix") of an existing client's Klai Studio app in a new Dev environment. The design follows a written profile of the app's real users. The skill then verifies the preview and drafts a "we remixed your app" email for the owner to send.
- When to use it: someone asks for a remix, a win-back preview, or a redesigned demo of an existing client's Klai app.
- Source-of-truth doc: the Notion page "Skill: Klai App Remix Preview".

This repo is private. Never commit secrets or credentials.
