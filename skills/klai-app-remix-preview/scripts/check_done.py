#!/usr/bin/env python3
"""Machine checks for the remix definition of done.

Usage: python3 scripts/check_done.py --pages pages.json --parity parity.json

pages.json: a list of pages read from the target env (get_entity_detail), each
  {"id": "...", "name": "...", "requestHook": false} or with the full "form"
  object, in which case form.requestHook is read.
parity.json: the parity file built from assets/parity-checklist.json.

Exits 0 when every check passes, 1 otherwise, and prints each failure.
"""
import argparse, json, sys

def hook(page):
    if "requestHook" in page:
        return page["requestHook"]
    return (page.get("form") or {}).get("requestHook")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", required=True)
    ap.add_argument("--parity", required=True)
    a = ap.parse_args()
    fails = []
    pages = json.load(open(a.pages))
    if not pages:
        fails.append("pages: file is empty, nothing was checked")
    for p in pages:
        if hook(p) is not False:
            fails.append(f"requestHook not false on page {p.get('name') or p.get('id')} ({hook(p)!r})")
    items = json.load(open(a.parity)).get("items", [])
    if not items:
        fails.append("parity: no items")
    for i in items:
        st, label = i.get("status"), i.get("name") or i.get("id")
        if st not in ("kept", "moved", "gap"):
            fails.append(f"parity item {label} has status {st!r}")
        elif st == "gap" and not (i.get("reason") or "").strip():
            fails.append(f"parity gap {label} has no reason")
        elif st == "moved" and not (i.get("where") or "").strip():
            fails.append(f"parity moved item {label} has no 'where'")
    for f in fails:
        print("FAIL", f)
    print(f"{len(pages)} pages, {len(items)} parity items, {len(fails)} failures")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
