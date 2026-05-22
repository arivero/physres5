# T01 — Source audit and bibliography

## Goal

Make the bibliography and source map reliable enough for manuscript expansion.

## Instructions

1. Check every source listed in `context/source_inventory.md` against `references/pdfs/`.
2. Ensure `manuscript/references.bib` has entries for sources already cited in `main.tex` and section files.
3. Add missing BibTeX entries for all sources likely to be used in the 50-page manuscript.
4. Create `context/source_claims_matrix.md` with columns:
   - source;
   - manuscript use;
   - strongest relevant claim;
   - section where it will be cited;
   - status: verified / needs page check.
5. Do not fabricate page numbers. Mark `needs page check` when the exact page has not been inspected.

## Done when

`make test` passes and the claims matrix exists.
