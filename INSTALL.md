# Installation

```bash
tar -xzf devries_agentic_project.tar.gz
cd devries_agentic_project
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest pyyaml
make test
make manuscript
```

## Codex local

```bash
codex --cd . --ask-for-approval on-request "Read AGENTS.md and codex_tasks/T00_bootstrap_repo.md. Plan first, then execute T00."
```

## Codex Cloud

Push this directory as a Git repository, connect it in Codex web, and launch tasks from `codex_tasks/`. Start with `T00_bootstrap_repo.md`.

## GPT-5.5 Pro review

After Codex completes T02--T08, paste `prompts/06_gpt55pro_concept_review.md` with the compiled manuscript and review files.
