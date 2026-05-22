# PRD reduction loop 57 editor report

Date: 2026-05-23

Scope:
- Convert the compiled manuscript toward a Physical Review D article under the requested 50-page maximum.
- Preserve the pole-spectrum construction and source-theory caveats.

Edits made:
- Switched `manuscript/main.tex` from REVTeX `preprint` to `reprint`.
- Removed Appendix E from the compiled article.
- Replaced the 1973-line theorem-target appendix with a compact acceptance-test appendix.
- Converted the introduction target array to prose.
- Split several two-column display equations and added one `widetext` block for the neutral-projector definitions.
- Rebuilt `manuscript/main.pdf`.

Verification:
```bash
make manuscript
pdfinfo manuscript/main.pdf
```
Result: build passed; compiled PDF is 32 pages.

```bash
rg -n '\bnot\s+[^.]{0,80}\bbut\b|\brather than\b|\bnot merely\b|\bnot only\b|\bnot\s+[^,.;:]{1,80},\s*but\b|,\s*not\s+' <compiled section list>
```
Result: no matches.

```bash
rg -n '\b[Ee]vidence\b|\bcomplete\b|\bComplete\b|\bcompleted\b|\bCompleted\b|\bledger\b|\bbookkeeping\b|\baudit\b|\bAudit\b|this manuscript|source-status|manuscript-facing' <compiled section list>
```
Result: no substantive matches. The only broad `T1` hit was `\usepackage[T1]{fontenc}`.

```bash
git diff --check
```
Result: no whitespace errors.

Residual issue:
- `manuscript/main.log` still reports 49 overfull hbox warnings after the two-column conversion. Several are small, but the route sections still contain wide technical displays that need a dedicated layout pass before the manuscript can be called PRD-clean.

Conclusion:
- The page-count requirement has been met in the compiled artifact.
- The PRD suitability requirement remains active because equation/table layout needs further cleanup.
