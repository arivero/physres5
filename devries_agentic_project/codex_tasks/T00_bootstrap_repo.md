# T00 — Bootstrap repository

## Goal

Verify repository structure, build commands, and source inventory before manuscript edits.

## Context files

- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `OPEN_ISSUES.md`
- `context/project_memory.md`
- `context/source_inventory.md`
- `manuscript/main.tex`

## Instructions

1. Read the context files.
2. Run `make numbers`, `make test`, and `make manuscript`.
3. Repair only build/test breakage.
4. Do not expand physics prose in this task.
5. Create `reviews/T00_bootstrap_report.md` summarizing:
   - commands run;
   - results;
   - any repair made;
   - current manuscript page count;
   - recommended next task.

## Done when

`make test` and `make manuscript` pass, or the exact failure and minimal repair are documented.
