#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "references" / "pdfs"
INDEX = ROOT / "context" / "source_inventory.md"


def main() -> None:
    pdfs = sorted(p.name for p in PDF_DIR.glob("*.pdf"))
    index = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    print(f"PDF count: {len(pdfs)}")
    missing = [name for name in pdfs if name not in index]
    if missing:
        print("PDFs missing from context/source_inventory.md:")
        for name in missing:
            print(f" - {name}")
        raise SystemExit(1)
    print("All local PDFs are represented in source_inventory.md")


if __name__ == "__main__":
    main()
