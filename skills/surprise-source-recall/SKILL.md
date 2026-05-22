---
name: surprise-source-recall
description: Trigger lateral source recall during conceptual manuscript revision when direct advisor/referee loops stop producing new ideas; searches adjacent source-fragment themes, historical cues, and mechanism analogies.
---

# Surprise Source Recall

Use after one or two referee/advisor cycles when the manuscript has become locally coherent and needs new conceptual connections.

## Trigger

Run this skill when a section feels correct but conceptually exhausted.

## Method

1. Name the current local object: equation, branch, boundary condition, scale, representation, or compactification datum.
2. Search the source corpus for adjacent mechanisms, not the same keyword.
3. If the local corpus stalls, use web search for primary sources, reviews, or historically relevant papers. Download useful PDFs into `references/pdfs/`, update `context/source_inventory.md`, rerun `scripts/fragment_pdfs.py`, and add source-matrix entries.
4. Read two fragments outside the section's current source family.
5. Write one Lean-style note in `notes/lean/` recording any new obligation or analogy.
6. Add only ideas that generate an equation, test, or explicit open calculation.

## Lateral Search Patterns

- For `negative branch`: search `tachyon`, `Goldstone`, `modulus`, `radion`, `instability`, `spectral cover`.
- For `pole placement`: search `threshold`, `matching`, `duality`, `background`, `boundary value`.
- For `J assignment`: search `current algebra`, `Casimir`, `adjoint`, `doublet`, `endpoint`, `Chan-Paton`.
- For `KK`: search `charge`, `winding`, `Wilson line`, `monodromy`, `orbifold`, `interval`.
- For `look-elsewhere`: search `coincidence`, `selection`, `structural`, `unification`, `consistency`.

## Rule

The output is a short note or source-matrix entry. Manuscript prose changes come later, after the idea survives one review loop. Use local fragments for final manuscript claims whenever possible; use web search to discover missing sources and verify modern or unstable claims.
