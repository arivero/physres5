---
name: latex-revtex-builder
description: Build, repair, and page-count the REVTeX manuscript.
---

# REVTeX builder

Use this skill for LaTeX compilation, bibliography, and page-count checks.

## Workflow

1. Run `make manuscript`.
2. If compilation fails, inspect the `.log` and repair the minimal cause.
3. Ensure citations are present in `references.bib`.
4. Record the page count using `pdfinfo manuscript/main.pdf` when available.
5. Avoid physics rewrites unless needed for compilation.

## Output

Create `reviews/build_report.md`.
