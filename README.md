# My Global Workflow — Direction OS

The owner's personal workflow system: life directions run through short AI sessions over durable state in this repository.

## Layout

- **`os/`** — the system: rules, plays, schemas, adapters, engineering contour. Start here: `os/KERNEL.md`. How to launch: `os/BOOTSTRAP.md`. Changing the OS: `os/MAINTENANCE.md`.
- **`live/<direction-id>/`** — live state of each direction (created by the frame play; none exist until then).
- **`archive/`** — frozen legacy of previous generations. Read-only evidence, never authority (`archive/README.md`).
- `AGENTS.md` / `CLAUDE.md` — instructions agent sessions read automatically when opened on this repo.

## Quick start

1. Create a ChatGPT/Claude Project, paste `os/adapters/SESSION_PAYLOAD.md` (with your direction id), connect the GitHub connector to this repo.
2. Write a plain sentence: «Хочу создать направление: …» — the session runs the frame play.
3. Paste its RESULT into a fresh Claude Code/Codex session on this repo — it commits state and hands back the next input. Details: `os/BOOTSTRAP.md`.

END_OF_FILE: README.md
