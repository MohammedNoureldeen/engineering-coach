"""Check the portable package and local documentation links (Python 3.10+)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "engineering-coach"
MODES = {"changes", "decisions", "terms", "flow", "quiz", "practice"}
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def check() -> list[str]:
    errors = []
    required = [
        ROOT / "README.md",
        ROOT / "README.ar.md",
        ROOT / "LICENSE",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        *(SKILL / "references" / f"{mode}.md" for mode in sorted(MODES)),
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(ROOT)}")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Not UTF-8: {path.relative_to(ROOT)}")
            continue
        if "[TODO:" in content:
            errors.append(f"Unfinished scaffold: {path.relative_to(ROOT)}")
        for raw in LINK.findall(content):
            target = raw.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(ROOT):
                errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
            elif not linked.exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
            if path.is_relative_to(SKILL) and not linked.is_relative_to(SKILL):
                errors.append(f"Installed skill needs external file: {target}")

    for readme in (ROOT / "README.md", ROOT / "README.ar.md"):
        if readme.is_file():
            content = readme.read_text(encoding="utf-8")
            for mode in MODES:
                if f"`{mode}`" not in content:
                    errors.append(f"Mode {mode} missing from {readme.name}")

    try:
        cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        ids = [case["id"] for case in cases]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate evaluation case IDs")
        for case in cases:
            if not case["prompt"].startswith("$engineering-coach") or not case["criteria"]:
                errors.append(f"Incomplete evaluation case: {case['id']}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Cannot read evaluation cases: {exc}")
    return errors


if __name__ == "__main__":
    failures = check()
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: required files, six modes, UTF-8 Markdown, local links, installable references, evaluation cases")
