#!/usr/bin/env python3
"""Search PDF-derived source fragments with compact source/page output."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRAGMENTS = ROOT / "context" / "source_fragments"


def front_matter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def search(query: str, max_hits: int) -> int:
    pattern = re.compile(query, re.IGNORECASE)
    hits = 0
    for path in sorted(FRAGMENTS.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        source = front_matter_value(text, "source")
        start = front_matter_value(text, "page_start")
        end = front_matter_value(text, "page_end")
        rel = path.relative_to(ROOT)
        for match in matches[:3]:
            line_no = text.count("\n", 0, match.start()) + 1
            line = text.splitlines()[line_no - 1].strip()
            print(f"{rel}:{line_no}: {source} pp.{start}-{end}: {line}")
            hits += 1
            if hits >= max_hits:
                return hits
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Python regular expression, case-insensitive")
    parser.add_argument("--max", type=int, default=80, help="maximum hits to print")
    args = parser.parse_args()
    count = search(args.query, args.max)
    if count == 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
