# PRD reduction loop 58 editor report

Date: 2026-05-23

Scope:
- Follow the recent editor feedback after the O1, O2b, and O3 closure commits.
- Remove visible scaffold language from the compiled paper text.
- Clear the two-column layout warnings left by loop 57.

Editor feedback used:
- The loop 56 editor report flagged `evidence`, `complete`, `ledger`, `bookkeeping`, old target labels, and process-language headings.
- The loop 58 lightweight editor pass flagged notebook phrasing in the route sections, strong labels such as `entire target`, `fully specified`, and `clean value`, and overfull displays in Secs. VI and IX.

Resolution:
- Recast main-text references to theorem-target numbering as open calculations, source conditions, or Appendix D source conditions.
- Replaced table headings such as `Required derivation`, `Derivation target`, and `Target` with source-facing headings.
- Replaced adjectival claims such as `clean weak-angle value` with explicit physics labels such as `group-theoretic weak-angle value`.
- Converted the wide \(G_2\) dictionary from a `widetext` table into a two-column enumeration.
- Split or shortened the remaining wide displays in the electroweak, interval, and \(G_2\) sections.

Verification:
```bash
make manuscript
pdfinfo manuscript/main.pdf | rg '^Pages|File size'
```
Result: build passed; `manuscript/main.pdf` is 34 pages.

```bash
awk 'match($0,/\\(\\.\\/sections\\/[^ ]+/){f=substr($0,RSTART+2,RLENGTH-2)} /Overfull \\\\hbox|Overfull \\\\vbox/{print f ":" NR ":" $0}' manuscript/main.log
```
Result: no overfull hbox or vbox entries.

```bash
rg -n 'manuscript|draft|notebook|scaffold|Journal-facing|source-status|source status|manuscript-facing|this manuscript|T1|T2|T3|\b[Ee]vidence\b|\bcomplete\b|\bComplete\b|\bcompleted\b|\bCompleted\b|\bledger\b|\bbookkeeping\b|\baudit\b|\bAudit\b' <compiled section list>
```
Result: no matches.

```bash
rg -n '\bnot\s+[^.]{0,80}\bbut\b|\brather than\b|\bnot merely\b|\bnot only\b|\bnot\s+[^,.;:]{1,80},\s*but\b|,\s*not\s+' manuscript/sections manuscript/main.tex
```
Result: no matches.

```bash
git diff --check
```
Result: no whitespace errors.

Residual note:
- `manuscript/sections/E_dimensional_interpolation.tex` is currently uncompiled and still contains older target-number scaffolding. It was excluded from the compiled-section scan because `manuscript/main.tex` no longer inputs it.
