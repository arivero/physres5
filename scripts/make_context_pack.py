#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "AGENTS.md",
    "PROJECT_BRIEF.md",
    "OPEN_ISSUES.md",
    "context/project_memory.md",
    "context/source_inventory.md",
    "context/done_definition.md",
    "codex_tasks/T00_bootstrap_repo.md",
]
OUT = ROOT / "context" / "context_pack.md"


def main() -> None:
    parts = []
    for rel in FILES:
        p = ROOT / rel
        parts.append(f"# FILE: {rel}\n\n" + p.read_text(encoding="utf-8"))
    OUT.write_text("\n\n---\n\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
