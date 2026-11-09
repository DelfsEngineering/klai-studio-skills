# Evals (klai-ui-makeover)

## This skill should run
1. **New look, same product.** "Replace the visual system; keep every permission and named action." → makeover. Matrix has no pending. Reachability verified; live fires only with actual authorization.
2. **Presentation rearrange.** "Put filters in one bar; don't add features." → makeover (allowed presentation change). Remix would be wrong.
3. **Authorized brand.** "Use our public green; don't copy their homepage grid." → tokens with provenance; layout original.
4. **CSS-only system.** "New look in site CSS; keep every id." → makeover if type/spacing/hierarchy/components/states actually change. Unchanged schema/class names are not a fail.

## This skill should not run
4. "Written brief only." → direction.
5. "Keep this identity, fix spacing." → polish.
6. "Redesign the workflows and add a wizard on a mocked Dev preview." → remix. Makeover must not add the wizard or create a remix env.

## Quality
- Direction exists before token replacement (written in-run is OK; no extra approval wait on Dev visuals).
- Production untouched.
- Route/hook/action ids preserved; labels distinguished.
- In-scope missing behaviour is a blocker unless outside agreed scope or explicitly accepted (quoted). No hypothetical "owner can accept".
- Connected Dev: inspect effects; disposable/isolated; actual authorization or block the fire.
- Zero-backend-request only if the env is an isolated mock.
- Name-swap on cover + one operate page.
