# Verification (makeover)

Screenshots prove look. They do not prove the product still works. Run both.

Capabilities described here are generic browser checks (viewports, themes, console, network, emulation). This skill is not Playwright CLI and does not claim reel identity. Do not install tools. Use sanctioned available browsers. Never bypass auth. [LICENSE-THIRD-PARTY.md](../LICENSE-THIRD-PARTY.md).

## Tool choice
1. Agent browser tools.
2. Already-installed browser CLI.
3. If neither: cannot call makeover done; mark verification blocked.

## Viewport matrix
Required: **390** and **1280**, realistic heights. Add **768** and/or **1024** when columns, tables, or collapsing nav exist. Profiled device first.

All in-scope **themes**. All in-scope **roles** for permission checks.

## Behaviour
From the preservation matrix, walk **without unauthorized writes**:

- Primary job is still reachable (control present, labelled, in role)
- Empty, loading, error
- Long content
- Permission: a lesser role does not run an admin action
- Named actions still **exist** with the same names and contracts

Compare with baseline: no dropped control, no new permission, no renamed route/hook/action ids.

## Consequential live actions
A Dev UI is **not** necessarily isolated data, email, payments, or deletion. Before any behavioural test that would click Save, Submit, Delete, Send, Pay, Print-to-backend, or fire a named action/hook:

1. **Inspect effects.** Read the named action, hook, `requestHook`, and likely network.
2. **Prefer isolation.** Disposable records and isolated or mocked services.
3. **Actual authorization.** Fire the action only if the user, in this run, actually authorized that class of consequential action. Quote them in the record. A request to make over visuals is **not** that authorization, and "Dev edits don't need extra approval" is **not** a blanket OK to run live saves.
4. **Otherwise block.** Mark the behaviour check **blocked**, not passed. Do not click.

Visual/reachability checks can pass while the live fire stays blocked.

## Console / network
When available, after each flow. New errors you caused are fails.

**Zero backend-request** only for an **explicit isolated mocked preview**. A connected Dev makeover talking to its backend is normal. Do not apply remix Gate B's zero-request rule here.

## Accessibility
Contrast 4.5:1 / 3:1. Keyboard. Visible focus. Reduced motion: essential UI still visible. Mark emulation unrun if you cannot set it.

## Clipping
Dropdowns, sticky headers, 390 overflow. After shots vs before for accidental regression in jobs.

## Mocks vs live
Label every session. Do not present mock data as a production sign-off.

## Finish
Matrix has no pending. Unrun cells listed. Production not touched. Closing summary names remaining platform limits (save no-ops, unread pages).
