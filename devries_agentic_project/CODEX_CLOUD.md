# Codex Cloud execution guide

## Current platform check

The available OpenAI Platform command in this chat environment is API-key setup. It does not expose a tool that creates a Codex Cloud workspace or directly uploads this repository into Codex Cloud.

Codex Cloud execution therefore uses the supported repository path:

1. unpack this tarball;
2. initialize a Git repository;
3. push it to GitHub or another repository connected to Codex web;
4. open Codex web and select the repository;
5. launch task packets from `codex_tasks/`.

## Recommended cloud task order

Run these as separate Codex Cloud tasks or as a staged sequence.

1. `codex_tasks/T00_bootstrap_repo.md`
2. `codex_tasks/T01_source_audit_and_bib.md`
3. `codex_tasks/T02_casimir_operator_derivation.md`
4. `codex_tasks/T03_pole_mass_scheme.md`
5. `codex_tasks/T04_electroweak_projective_angle.md`
6. `codex_tasks/T05_string_KK_G2_bridge.md`
7. `codex_tasks/T06_flavour_so32_boundary.md`
8. `codex_tasks/T07_global_form_line_operators.md`
9. `codex_tasks/T08_referee_red_team.md`
10. `codex_tasks/T09_50_page_expand_compile.md`

## Suggested first Codex Cloud prompt

```text
Read AGENTS.md, PROJECT_BRIEF.md, OPEN_ISSUES.md, context/project_memory.md, and codex_tasks/T00_bootstrap_repo.md. Work in plan mode first. Do not edit manuscript prose until you have produced a task graph and confirmed the build/test commands. Then implement only T00. Done when make test and make manuscript pass, or when you have documented the precise failure and a minimal repair plan.
```

## Parallelization map

- Agent A: T02, algebra of the mass operator and asymptotic constraints.
- Agent B: T03, pole mass scheme and electroweak inputs.
- Agent C: T04, W/Z assignment and projective EWSB interpretation.
- Agent D: T05, string/Kaluza-Klein/G2 bridge.
- Agent E: T07, global gauge group and line-operator appendix.
- Agent F: T08, referee and red-team review.

Merge order: A+B first, then C, then D/E, then F, then T09.
