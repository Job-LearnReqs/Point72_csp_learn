# Codex configuration

This directory contains the project-shared Codex configuration copied from
`~/.codex`.

Codex loads repo-local `.codex/config.toml` and `.codex/rules/` only after the
checkout is trusted from the user-level config. On a new machine, run:

```bash
sh .codex/setup.sh
```

That script adds a trust entry for the current checkout to
`~/.codex/config.toml`. The smooth learning-session behavior remains in this
repo:

- `approval_policy = "never"`
- `sandbox_mode = "danger-full-access"`
- `.codex/rules/default.rules`

Only non-secret configuration should be committed here. Keep authentication,
history, logs, shell snapshots, SQLite state, temporary files, and installed
system skills in your user-level Codex home directory.
