#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md",
    "PROJECT_BRIEF.md",
    "OPEN_ISSUES.md",
    "manuscript/main.tex",
    "manuscript/references.bib",
    "calculations/devries_spectrum.py",
    "context/source_inventory.md",
    "codex_tasks/T00_bootstrap_repo.md",
]


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        print("Missing required files:")
        for p in missing:
            print(f" - {p}")
        return 1

    main_tex = (ROOT / "manuscript/main.tex").read_text(encoding="utf-8")
    bib = (ROOT / "manuscript/references.bib").read_text(encoding="utf-8")
    keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bib))
    cited = set()
    for block in re.findall(r"\\cite\{([^}]+)\}", main_tex):
        cited.update(k.strip() for k in block.split(","))
    missing_keys = sorted(cited - keys)
    if missing_keys:
        print("Cited keys missing from references.bib:")
        for k in missing_keys:
            print(f" - {k}")
        return 1
    print("Project sanity check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
