# Codex setup notes

- `AGENTS.md` is the primary durable instruction file. Keep it concise and make task-specific files explicit.
- Codex Cloud works from a connected repository. This package is arranged as a repository to push and connect.
- `skills/` packages task-specific workflows for optional Codex skill/plugin use.
- `.codex/config.toml.example` is an example only. Copy it into `.codex/config.toml` after the repository is trusted and after checking the current model names exposed by your Codex client.
- This repository does not require an OpenAI API key. It is intended for Codex CLI, IDE, app, or cloud surfaces authenticated through your ChatGPT/Codex access.
