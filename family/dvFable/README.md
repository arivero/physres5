# dvFable — de Vries electroweak relation, Fable 5 run

Successor workspace to [`../dv2`](../dv2). Created 2026-06-11. Prior material
is **symlinked, read-only by convention** — never edit through a symlink.

## Mission

Decide — solve-or-no-go, never "open/conditional" — whether the de Vries
electroweak relation has a genuine physical origin or is a coincidence, and
document the result honestly either way. Inherits the full discipline of
`PRIOR-AGENT.md` (read it first; do not re-derive its findings).

**First task (gates everything):** resolve the orbit-loophole question for the
cleanest formulation `X+ = β²` before building any structure on top of it.
The prior run's failure mode was building edifices (M^{pqr} gates, a 48-page
paper) on an untested conjecture. Not again.

## Inherited rules (from dv2)

1. Lead with the cleanest formulation (orbit / `X+ = β²`), not the 2×2 block.
2. Geometry forced, never fitted: D=10, K6 minimal cosets, internal SU(2),
   gauge-Higgs. No integer scans.
3. Typeset = derived. Write the paper only as results close; "not yet derived"
   lives in `%` comments.
4. Established no-go's stand: the de Vries 2×2 block **cannot** be a unitary
   gauge-invariant KK mass structure. Do not relitigate.

## Layout

| Path | What | Status |
|------|------|--------|
| `PRIOR-AGENT.md` | dv2's distilled state of knowledge + restart plan | link, read first |
| `references/` | source papers (PDFs + manifests) | link |
| `corpus/` | cleaned source conversations + formula/priority indexes | link |
| `prior-work/` | full first attempt (claudeFinal.tex, M^{pqr} apparatus) | link, archive |
| `loop-history/` | dv2's 2026-05-25 loop run: milestone tests + LOOP-LOG | link, archive |
| `GOALS.md` | **new** fixed goals, terminal standards, loop protocol (2026-06-11) | normative |
| `notes/` | **new** derivations, audits, no-go's — this run's work (`notes/LOG.md` = loop log) | working dir |
| `calc/` | **new** verification scripts (SymPy checks etc.) | working dir |
| `loop/` | **new** dispatch prompts + raw two-arm outputs | working dir |
