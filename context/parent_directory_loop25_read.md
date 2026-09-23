# Parent Directory Loop 25 Read

This note records the Loop 25 read of `..` from `/home/codexssh/physres5`.
The pass used a shallow parent inventory plus two read-only sidecar reads:
one over `../physres5lineage/seeds/prTalks`, and one over adjacent physics folders including
`../physres5lineage/weak`, `../phys4`, `../phys6gpd`, `../recap`, and `../phys3`.

## Protocol

- Treat adjacent folders as project-source memory, critique records, and source queues.
- Keep PDFs as source objects.  Text extraction is an access aid for triage.
- Promote manuscript claims through primary literature in `references/pdfs/`,
  newly downloaded primary papers, or explicit project-source labels.
- Exclude runtime state, dotfile configuration, caches, editor state, package
  folders, generated logs, credentials, and unrelated administrative files from
  manuscript claims.

## Active Parent Clusters

| Parent path | Status | Useful content |
|---|---|---|
| `../physres5lineage/seeds/prTalks/` | project PDF source notes | Electroweak ray, two-branch block, positive pole-spectrum clue, negative branch as order-parameter candidate, KK \(7/6/5\) and \(3/2/1\) interpolation, orbit quadratic, Regge alternatives, and representation-channel reading \(T_H=1/2\), \(T_{\rm adj}=1\). |
| `../physres5lineage/weak/` | critique and obstruction notes | Conservative electroweak scaffold, W/Z assignment obligations, scheme and photon checks, Wigner--Eckart obstruction, Higgs-sector spurion ideas, and referee-style checklists. |
| `../phys4/notes/` | source queue | SU(2|1) and superconnection source candidates, brane/endpoint dictionaries, Hanany--Witten and M-theory route candidates, Higgs-confinement continuity analogs, and branch-structure analogs. |
| `../phys3/` | provenance queue | Witten-KK and dimensional-interpolation provenance, SO(32)/Chan--Paton source trails, and older Rivero/DeVries equation context. |
| `../phys6gpd/` | conjectural mechanism queue | Optional \(G_2\), octonion, and Casimir mechanism context requiring source upgrade before manuscript use. |
| `../recap/` | future flavor queue | Koide and fermion-mass summaries.  Use after a focused flavor/source issue opens. |
| root-level TeX and Markdown files | historical drafts | Rivero/DeVries, Seiberg, and bootstrap drafts may supply provenance or source leads after focused review. |

## Manuscript-Relevant Findings

1. The electroweak ray remains the central admissibility filter: a valid route
   preserves the photon null direction, the common Higgs radial parameter, and
   the W/Z projective ratio along the broken-to-unbroken ray.
2. The parent files agree with the current main theorem target: derive the
   ordered sampling rule from one gauge-Higgs or source operator.
3. The superconnection queue should be upgraded through primary SU(2|1) and
   graded-connection sources before it carries additional journal-facing claims.
4. The Wigner--Eckart route is useful as an obstruction record.  A revival
   requires new parent data, operator tensor type, projection, and
   normalization.
5. The KK/string route queue should prioritize one source-controlled matrix
   entry, especially \(\Sigma_{aa,J}=J\) from CHM-style boundary data.
6. The Higgs-branch interpolation queue should connect \(x_-(J)\), the
   order-parameter scale, and the top-sector source map through a
   gauge-invariant scalar functional.
7. The SO(32) material remains a flavor-boundary source queue until a derived
   endpoint/orientifold embedding couples it to the electroweak kernel.

## Promotion Targets

- `notes/lean/ParentDirectoryLoop25.lean` records the obligation structure.
- `notes/lean/SuperconnectionAssignment.lean` now includes trace separation,
  Wigner--Eckart exclusion, SO(32) coupling discipline, and CHM compatibility.
- `CLOSED_ISSUES.md` records O13--O15 closure; O16 stays open.
