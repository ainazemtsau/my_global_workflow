# EXTENDING — how the OS is customized and extended

The OS cannot cover every future stage up front — and must not try (KERNEL §7). Instead, extension is cheap, layered, and additive. This file defines where customization lives at each level and the rules that keep the core small.

## Levels

| Level | What can be customized | How |
|---|---|---|
| Direction | its lenses | `CHARTER.md → lenses` (already core) |
| Direction | its own procedures (playtest protocol, release checklist, training routine) | `live/<id>/plays/<name>.md`; invoked as `play: local/<name>` in a CALL; same format and ≤600-word budget as `os/plays/` |
| Direction | its policies and parameters | `knowledge/` entries with `read_by:`; appetites/thresholds in CHARTER constraints |
| Product repo | validation thresholds, review rubric, agent config | `validation.config`, `REVIEW.md`, AGENTS.md — via the repo's `docs/FRICTION.md` discipline |
| System | new modules (engineering is the first; future candidates: marketing, content, finance) | `os/<module>/` as a self-contained folder; wired in through lenses and CALLs — the kernel is never edited to add a module |

## Rules

1. **Additivity.** No level may override gates G1–G8, the CALL/RESULT schemas, or the six state file types. Local plays are procedure files, not state — the six-type budget is untouched.
2. **Same discipline locally.** A local play follows the `os/plays/` format (Purpose / Reads / Writes / Steps / Done when / Notes) and budget. A direction may have at most 5 local plays; wanting a sixth means two should merge — or one should be promoted.
3. **Promotion path.** A local play that proves itself in ≥2 directions is a friction-candidate for promotion into `os/plays/` (via a maintenance session). The reverse also holds: an os/ play used by only one direction is a candidate for demotion to local.
4. **No speculative extension.** A local play or module is created when real work needs it in the current bet — never "for the future" (G8 spirit applies to structure, not just goals).

## How a session resolves a play

`play: <name>` → `os/plays/<name>.md`. `play: local/<name>` → `live/<direction-id>/plays/<name>.md`. A session that can read neither file is in repair.

END_OF_FILE: os/EXTENDING.md
