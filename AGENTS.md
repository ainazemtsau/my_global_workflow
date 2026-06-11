# Repository Agent Instructions

This repository is the **Direction OS** — the owner's workflow system. Rules: `os/KERNEL.md`. Live direction state: `live/<direction-id>/`. Everything under `archive/**` is frozen legacy: read-only evidence, never authority, never a target of edits.

## Recognize your job from the input

| Input pasted/typed by the owner | Your role | Procedure |
|---|---|---|
| A `RESULT ...` packet (or "apply this RESULT") | **writer** | `os/adapters/coding-agent.md`, Role 1: apply state_changes exactly, append LOG, save full RESULT to history/, maintain `END_OF_FILE:` trailers, commit, hand back the `next` CALL. No judgment — ambiguity goes back as a conflict. |
| `MAINTENANCE REQUEST ...` (or a problem/feature about the OS itself, or a problem chat transcript with a complaint) | **maintenance** | `os/MAINTENANCE.md`. One problem per session. Never touch `live/**`. |
| A CALL packet, or a plain message about a direction ("продолжаем", a question, an ambition) | **session** | Resolve per `os/KERNEL.md` §2 OPEN; run the play from `os/plays/` (or `live/<id>/plays/` for `local/*`). In an agent CLI on this repo you become your own writer only AFTER emitting your RESULT: then apply its state_changes and commit. Chat-platform sessions are never the writer. |
| `collect next for <direction>` | **writer** | Emit one paste block: SESSION_PAYLOAD block → play file → NOW.md → CALL (rules first, CALL last). |
| `audit <direction>` | **writer** | `os/adapters/coding-agent.md` Role 1 audit command: read-only consistency sweep of `live/<id>/`, report only — state drift → ready repair CALL, rule defect → draft MAINTENANCE REQUEST. Never edits anything. |

## Hard rules

- One session = one job. After the job is done and committed, the session ends; continuation belongs to a fresh session.
- `live/**` changes only by applying a RESULT's `state_changes` — never by direct editing, never invented.
- Every state file you write ends with its `END_OF_FILE: <path>` trailer.
- Respect budgets when editing `os/**`: kernel ≤1500 words, a play ≤600, six state file types (see `os/MAINTENANCE.md`).
- Small diffs; descriptive commit messages (`<direction> <play> <node/task>: <log line>` for state, plain descriptive for os/).
- Do not delete files outside the scope of the job.

END_OF_FILE: AGENTS.md
