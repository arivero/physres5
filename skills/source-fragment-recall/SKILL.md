---
name: source-fragment-recall
description: Search and recall the local PDF-derived markdown knowledge base for conceptual manuscript work, especially string theory, Kaluza-Klein, GUT weak-angle lineage, electroweak scheme distinctions, and DeVries/Rivero source claims.
---

# Source Fragment Recall

Use this skill when manuscript work needs conceptual source recall from `references/pdfs/`.

## Workflow

1. Search `context/source_fragment_index.md` to identify relevant source slugs.
2. Search `context/source_fragments/` with `rg`, keeping page-range filenames in the result.
3. Read only the needed fragments.
4. Record source-backed claims in `context/concept_claims_matrix.md` or a focused note.
5. For open derivations, add Lean-style obligations in `notes/lean/`; these notes are scaffolds for expert review and are not compiled.

## Useful Searches

```bash
rg -n "sin2|3/8|weak mixing|Weinberg angle|SU\\(5\\)|Spin\\(10\\)" context/source_fragments
rg -n "Kaluza|compactification|circle|winding|momentum|boundary" context/source_fragments
rg -n "Regge|dual model|open string|endpoint|brane|D-brane" context/source_fragments
rg -n "pole|Breit|MS|running|effective potential" context/source_fragments
rg -n "Higgs mechanism|W boson|Z boson|vacuum expectation|mass matrix" context/source_fragments
```

## Output Discipline

- Cite source fragments by path and page range in notes.
- Use affirmative exposition in manuscript prose.
- Treat extracted text as a recall aid; exact citations still require page-level reading.
