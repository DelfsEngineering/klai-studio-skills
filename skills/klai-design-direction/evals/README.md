# Evals (klai-design-direction)

Re-read this skill's `SKILL.md` and check each scenario. A skill edit is not "done" if a scenario would pick the wrong skill or skip a required brief block.

Shared selection fixtures for the whole suite: `evals/design-suite-selection.json` at the **repo root** (packaged with the repo, not inside this folder). When this skill folder is copied alone, still apply the cases below from this file.

## This skill should run
1. **Brief only.** "Write a visual direction for this field checklist app from the users and our website." → direction. No UI edits. `DIRECTION.md` has audience, character without banned words, moments, quiet chrome, provenance, name-swap.
2. **Brand extract.** "Match our public site; don't change the app yet." → direction. Tokens have URL + date + confidence. No layout clone. No `npx designlang`.
3. **Prerequisite.** "Make it over, but we have no brief." → write direction first, then **hand off** to makeover. Direction skill does not restyle.

## This skill should not run
4. "Tighten spacing, keep the green." → polish.
5. "New look, same permissions and hooks." → makeover (it may write a brief internally).
6. "Remix this client with a new feature on Dev mocks." → remix.

## Quality
- Operate vs cover called out when both exist.
- Guesses labelled.
- No customer account/env ids in the skill files themselves (run records may contain them).
