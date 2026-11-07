#!/usr/bin/env python3
"""Validate Agent Skills layout, links, credits, and design-suite selection.

Usage:
  python3 scripts/validate_skills.py
  python3 scripts/validate_skills.py --pack /tmp/klai-design-suite-skills.tgz

Exits 0 on success, 1 on failure. Prints each FAIL and a summary.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NEW_SKILLS = [
    "klai-design-direction",
    "klai-ui-polish",
    "klai-ui-makeover",
]
ALL_SKILLS = NEW_SKILLS + ["klai-app-remix-preview"]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SIBLING_RE = re.compile(r"(?:\.\./)+klai-")

REQUIRED_CREDITS = {
    "klai-design-direction": [
        "Damir Sokolovsky",
        "CC BY 4.0",
        "creativecommons.org/licenses/by/4.0",
        "Paul Bakaus",
        "Apache License 2.0",
        "Leonxlnx",
        "designlang",
        "uncertain",
    ],
    "klai-ui-polish": [
        "Damir Sokolovsky",
        "CC BY 4.0",
        "creativecommons.org/licenses/by/4.0",
        "Paul Bakaus",
        "Apache License 2.0",
        "Leonxlnx",
        "Playwright",
        "uncertain",
        "must not assume Playwright is installed",
    ],
    "klai-ui-makeover": [
        "Damir Sokolovsky",
        "CC BY 4.0",
        "creativecommons.org/licenses/by/4.0",
        "Paul Bakaus",
        "Apache License 2.0",
        "Leonxlnx",
        "Playwright",
        "uncertain",
        "do not install Playwright",
    ],
}

# Generic fixtures only — fail if these customer/env markers appear in new skills.
FORBIDDEN_IN_NEW = [
    r"Purr\s*&\s*Pour",
    r"Floristware",
    r"idSite\s*[:=]\s*\d+",
    r"filemaker\.example",
]


def parse_frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        raise ValueError("missing YAML frontmatter delimited by ---")
    data = {}
    key = None
    folded = False
    acc = []
    for raw in m.group(1).splitlines():
        if key and (raw.startswith("  ") or raw.startswith("\t")):
            acc.append(raw.strip())
            continue
        if key is not None:
            data[key] = " ".join(acc).strip() if folded else (acc[0] if acc else "")
            key, folded, acc = None, False, []
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"unparseable frontmatter line: {raw}")
        k, v = raw.split(":", 1)
        k, v = k.strip(), v.strip()
        if v in (">-", ">", "|"):
            key, folded, acc = k, True, []
        else:
            if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                v = v[1:-1]
            data[k] = v
    if key is not None:
        data[key] = " ".join(acc).strip() if folded else (acc[0] if acc else "")
    return data


def skill_text(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text()


def check_frontmatter(name: str, fails: list[str]) -> dict | None:
    path = SKILLS / name / "SKILL.md"
    if not path.is_file():
        fails.append(f"{name}: missing SKILL.md")
        return None
    text = path.read_text()
    try:
        fm = parse_frontmatter(text)
    except ValueError as e:
        fails.append(f"{name}: {e}")
        return None
    n = fm.get("name", "")
    d = fm.get("description", "")
    if n != name:
        fails.append(f"{name}: frontmatter name {n!r} does not match directory")
    if not NAME_RE.match(n) or n.startswith("-") or n.endswith("-") or "--" in n:
        fails.append(f"{name}: invalid name {n!r}")
    if len(n) < 1 or len(n) > 64:
        fails.append(f"{name}: name length {len(n)} not in 1–64")
    if not d or len(d) > 1024:
        fails.append(f"{name}: description missing or length {len(d)} > 1024")
    if "Use when" not in d and "use when" not in d.lower():
        # remix uses "Use when" in folded description
        if "Use when" not in text.split("---", 2)[1]:
            fails.append(f"{name}: description should say when to use the skill")
    return fm


def iter_md_files(skill_dir: Path):
    for p in skill_dir.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md", ".json", ".py"}:
            yield p


def check_links(name: str, fails: list[str]) -> None:
    skill_dir = SKILLS / name
    for p in iter_md_files(skill_dir):
        text = p.read_text()
        if SIBLING_RE.search(text) and p.suffix == ".md":
            fails.append(f"{name}: {p.relative_to(ROOT)} looks like a sibling-skill link")
        if p.suffix != ".md":
            continue
        for href in MD_LINK_RE.findall(text):
            href = href.strip()
            if href.startswith("#") or href.startswith("mailto:"):
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
                continue
            path_part = href.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            target = (p.parent / path_part).resolve()
            try:
                target.relative_to(skill_dir.resolve())
            except ValueError:
                fails.append(
                    f"{name}: {p.relative_to(ROOT)} links outside the skill folder: {href}"
                )
                continue
            if not target.exists():
                fails.append(
                    f"{name}: {p.relative_to(ROOT)} broken relative link {href}"
                )


def check_credits(name: str, fails: list[str]) -> None:
    credit_path = SKILLS / name / "LICENSE-THIRD-PARTY.md"
    if not credit_path.is_file():
        fails.append(f"{name}: missing LICENSE-THIRD-PARTY.md")
        return
    blob = credit_path.read_text() + "\n" + (SKILLS / name / "SKILL.md").read_text()
    for needle in REQUIRED_CREDITS[name]:
        if needle.lower() not in blob.lower() and needle not in blob:
            fails.append(f"{name}: missing required credit/phrase {needle!r}")
    if "CC BY 4.0" in blob and "Changes:" not in blob and "Changes :" not in blob:
        fails.append(f"{name}: CC BY adaptation must include a change note")


def check_forbidden(name: str, fails: list[str]) -> None:
    for p in iter_md_files(SKILLS / name):
        text = p.read_text()
        for pat in FORBIDDEN_IN_NEW:
            if re.search(pat, text, re.I):
                fails.append(
                    f"{name}: {p.relative_to(ROOT)} matches forbidden customer/env pattern {pat}"
                )


def check_when_sections(name: str, fails: list[str]) -> None:
    text = skill_text(name)
    for heading in ("When to use", "When not to use", "Entry criteria", "Exit criteria"):
        if heading.lower() not in text.lower():
            fails.append(f"{name}: SKILL.md missing {heading!r}")
    others = [s for s in ALL_SKILLS if s != name]
    # New skills must name the other three jobs so packaged copies still hand off.
    if name in NEW_SKILLS:
        for other in others:
            if other not in text:
                fails.append(f"{name}: SKILL.md never mentions {other} (handoff/selection)")


def check_selection(fails: list[str]) -> None:
    fixtures = json.loads((ROOT / "evals/design-suite-selection.json").read_text())
    bodies = {n: skill_text(n) for n in ALL_SKILLS if (SKILLS / n / "SKILL.md").is_file()}
    for fx in fixtures:
        exp = fx["expected"]
        if exp not in bodies:
            fails.append(f"selection {fx['id']}: expected skill {exp} missing")
            continue
        body = bodies[exp]
        desc = parse_frontmatter(body).get("description", "")
        hay = (desc + "\n" + body).lower()
        for needle in fx.get("must_match_expected", []):
            if needle.lower() not in hay:
                fails.append(
                    f"selection {fx['id']}: expected {exp} to contain {needle!r}"
                )
        for other in fx.get("handoff_in_expected", []):
            if other not in body:
                fails.append(
                    f"selection {fx['id']}: {exp} should mention handoff {other}"
                )
        # Expected skill should be a better keyword fit than a random other new skill
        # for distinctive tokens from the request (remix/polish/makeover/direction).
        req = fx["request"].lower()
        if exp == "klai-design-direction" and "do not edit" in req:
            if "no UI edits" not in body and "does not edit" not in body.lower() and "not edit UI" not in body:
                fails.append(f"selection {fx['id']}: direction skill should say it does not edit UI")


def check_remix_untouched(fails: list[str]) -> None:
    """Best-effort: remix files should exist; git check is done by the caller too."""
    remix = SKILLS / "klai-app-remix-preview" / "SKILL.md"
    if not remix.is_file():
        fails.append("remix: SKILL.md missing")
        return
    text = remix.read_text()
    if "klai-ui-polish" in text or "klai-design-direction" in text:
        fails.append("remix: SKILL.md was edited to mention new skills (not requested)")


def pack(dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dest, "w:gz") as tf:
        for name in NEW_SKILLS:
            tf.add(SKILLS / name, arcname=f"skills/{name}")
        tf.add(ROOT / "AGENT.md", arcname="AGENT.md")
        tf.add(ROOT / "CHANGELOG.md", arcname="CHANGELOG.md")
        tf.add(ROOT / "evals", arcname="evals")
        tf.add(ROOT / "scripts/validate_skills.py", arcname="scripts/validate_skills.py")
        report = ROOT / "reports/design-suite.md"
        if report.is_file():
            tf.add(report, arcname="reports/design-suite.md")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", help="write a .tgz bundle of the three new skills plus index")
    args = ap.parse_args()
    fails: list[str] = []
    for name in ALL_SKILLS:
        check_frontmatter(name, fails)
    for name in NEW_SKILLS:
        check_links(name, fails)
        check_credits(name, fails)
        check_forbidden(name, fails)
        check_when_sections(name, fails)
        if not (SKILLS / name / "evals" / "README.md").is_file():
            fails.append(f"{name}: missing evals/README.md")
    check_selection(fails)
    check_remix_untouched(fails)
    if not (ROOT / "AGENT.md").read_text().count("klai-design-direction"):
        fails.append("AGENT.md does not index klai-design-direction")
    for f in fails:
        print("FAIL", f)
    print(f"{len(ALL_SKILLS)} skills scanned, {len(NEW_SKILLS)} new, {len(fails)} failures")
    if args.pack and not fails:
        pack(Path(args.pack))
        print("packed", args.pack)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
