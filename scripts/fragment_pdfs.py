#!/usr/bin/env python3
"""Convert local PDF sources into page-range markdown fragments.

The manuscript workflow uses these fragments as a searchable source corpus.
Each fragment keeps the original PDF path and page range in front matter so
conceptual claims can be traced back to local source material.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "references" / "pdfs"
OUT_DIR = ROOT / "context" / "source_fragments"
INDEX = ROOT / "context" / "source_fragment_index.md"
CHUNK_SIZE = 10


@dataclass(frozen=True)
class PdfMeta:
    filename: str
    pages: int
    tags: tuple[str, ...]


TOPIC_TAGS = {
    "01_": ("devries-rivero", "casimir-secular", "weak-angle-clue"),
    "02_": ("string", "regge", "duality"),
    "03_": ("cft", "affine-algebra", "modular"),
    "04_": ("string", "duality", "vacua"),
    "05_": ("qft", "poincare", "fields"),
    "06_": ("gauge-theory", "global-form", "line-operators"),
    "07_": ("standard-model", "higgs-mechanism", "electroweak"),
    "08_": ("standard-model", "electroweak", "symmetry"),
    "09_": ("extra-dimensions", "boundary-conditions", "electroweak"),
    "10_": ("kaluza-klein", "supergravity", "compactification"),
    "11_": ("g2", "m-theory", "singularities"),
    "12_": ("g2", "m-theory", "topology-change"),
    "13_": ("g2", "compactification", "kk-spectrum"),
    "14_": ("g2", "m-theory", "review"),
    "15_": ("supergravity", "supersymmetry"),
    "16_": ("gut", "su5", "spin10", "representation-theory"),
    "17_": ("gut", "e6", "representation-theory"),
    "18_": ("electroweak", "higgs", "eft"),
    "19_": ("higgs", "custodial", "electroweak"),
    "24_": ("g2", "chiral-fermions", "gut-representations"),
    "25_": ("g2", "anomaly", "gauge-fields"),
    "26_": ("spectral-geometry", "lens-spaces"),
    "27_": ("spectral-geometry", "laplacian"),
    "28_": ("spectral-geometry", "hodge-laplacian"),
    "29_": ("standard-model", "global-form", "line-operators"),
    "30_": ("standard-model", "global-form", "topological-tests"),
    "31_": ("g2", "higgs-bundles", "matter-localization"),
    "32_": ("constants", "pdg"),
    "34_": ("msbar", "standard-model-parameters", "scheme"),
    "35_": ("cdf-ii", "w-boson-mass", "electroweak-input"),
    "40_": ("radion", "moduli-stabilization", "extra-dimensions", "electroweak"),
    "41_": ("radion", "higgs-stabilizer", "warped"),
    "42_": ("diphoton-excess", "95gev", "collider"),
    "43_": ("running-alpha", "vacuum-polarization", "fine-structure"),
    "44_": ("kaluza-klein", "salam-strathdee", "historical"),
    "45_": ("gauge-higgs-unification", "hosotani", "extra-dimensions"),
    "46_": ("breitenlohner-freedman", "ads-stability", "supergravity"),
    "47_": ("supersymmetric-quantum-mechanics", "morse-theory", "hodge"),
    "48_": ("supersymmetry", "higgs", "z-boson"),
    "49_": ("worldline-supersymmetry", "spinning-particles"),
    "50_": ("superconnection", "su2-1", "electroweak"),
    "witten1981": ("kaluza-klein", "fermion-quantum-numbers", "historical"),
}


def slugify(filename: str) -> str:
    stem = filename.removesuffix(".pdf")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").lower()
    return slug


def tags_for(filename: str) -> tuple[str, ...]:
    for prefix, tags in TOPIC_TAGS.items():
        if filename.startswith(prefix):
            return tags
    return ("source",)


def run_text(command: list[str]) -> str:
    result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout


def page_count(pdf: Path) -> int:
    info = run_text(["pdfinfo", str(pdf)])
    for line in info.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not determine page count for {pdf}")


def extract(pdf: Path, start: int, end: int) -> str:
    text = run_text(["pdftotext", "-layout", "-f", str(start), "-l", str(end), str(pdf), "-"])
    return text.rstrip()


def write_fragment(pdf: Path, slug: str, tags: tuple[str, ...], start: int, end: int) -> Path:
    out_path = OUT_DIR / slug / f"pages_{start:03d}-{end:03d}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tag_lines = "\n".join(f"  - {tag}" for tag in tags)
    body = extract(pdf, start, end)
    content = (
        "---\n"
        f"source: {pdf.name}\n"
        f"pdf: references/pdfs/{pdf.name}\n"
        f"page_start: {start}\n"
        f"page_end: {end}\n"
        "topic_tags:\n"
        f"{tag_lines}\n"
        "status: extracted\n"
        "---\n\n"
        f"{body}\n"
    )
    out_path.write_text(content, encoding="utf-8")
    return out_path


def convert_pdf(pdf: Path) -> PdfMeta:
    pages = page_count(pdf)
    tags = tags_for(pdf.name)
    slug = slugify(pdf.name)
    for start in range(1, pages + 1, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE - 1, pages)
        write_fragment(pdf, slug, tags, start, end)
    return PdfMeta(filename=pdf.name, pages=pages, tags=tags)


def write_index(metas: list[PdfMeta]) -> None:
    lines = [
        "# Source fragment index",
        "",
        "Generated from `references/pdfs/` by `scripts/fragment_pdfs.py`.",
        f"Fragments use {CHUNK_SIZE}-page ranges where possible and preserve PDF page numbers.",
        "",
        "| Source | Pages | Tags | Status |",
        "|---|---:|---|---|",
    ]
    for meta in metas:
        tags = ", ".join(meta.tags)
        lines.append(f"| `{meta.filename}` | {meta.pages} | {tags} | extracted |")
    lines.append("")
    lines.append("Extraction status records successful text extraction only. Exact claims still require page-level reading before citation.")
    INDEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for required in ("pdfinfo", "pdftotext"):
        if not shutil.which(required):
            raise SystemExit(f"Missing required command: {required}")

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    metas = [convert_pdf(pdf) for pdf in sorted(PDF_DIR.glob("*.pdf"))]
    write_index(metas)
    print(f"Converted {len(metas)} PDFs into {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
