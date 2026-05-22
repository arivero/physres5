# Loop 54 Referee Review: O2b Closure

Scope:
- Current W/Z input audit in Sec. III.
- O2b movement from open to closed issues.

Findings:
- No blocking findings.
- Section III states the Breit--Wigner-to-pole convention and limitations.
- The audit uses PDG W/Z Breit--Wigner inputs, converts to pole values, states uncorrelated uncertainty treatment, and blocks W-only replacements without covariance/convention rules.
- O2b is removed from `OPEN_ISSUES.md` and recorded in `CLOSED_ISSUES.md` with future covariance-aware refinement deferred.

Arithmetic check:
- Recomputed `M_W,pole = 80.340724 GeV`.
- Recomputed `M_Z,pole = 91.153773 GeV`.
- Recomputed `sPole = 0.2231767970`.
- Recomputed uncorrelated propagated uncertainty `0.000260813`.

Verdict:
- Pass.
