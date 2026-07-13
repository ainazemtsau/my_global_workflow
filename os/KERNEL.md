# KERNEL — Direction OS

Authority order: live owner instruction > this kernel > the active play > direction state files > everything else (history, prior chats, model memory). On conflict the higher source wins; log the conflict as friction (§7).

## 1. What this is

The OS runs the owner's life directions — long-term ambitions — through many short AI sessions over durable state in a git repository.

- A **direction** lives in `live/<id>/` as a fixed set of state files (§3).
- A **session** is one chat doing exactly one job under exactly one play. Context is RAM: **assume interruption at any moment** — anything not written back to state does not exist.
- A **play** is a named procedure in `os/plays/`. Plays are the only way state changes.
- The **owner** decides. Agents do everything else. No play may require the owner to copy state by hand; packets are self-contained so any relay (human today, orchestrator later) can carry them.

## 2. Session contract

1. **OPEN** — input is a CALL **or a plain owner message** (typed or dictated). Read the direction's `NOW.md` plus the files the active play lists. With a plain message, resolve it against NOW.md: "продолжаем" → run `NOW.next`; a question → read-only; it matches an open task or recurring → that work; a new ambition where no state exists → frame; otherwise propose an interpretation in one line and confirm. The first reply is the **opening contract**: the orientation header, the play's numbered steps with the current one marked, and a ≤5-line restate (play, goal, done_when) — then run the play, stopping at the first step that needs the owner; play steps outrank the CALL's wording. If state is unreadable or contradicts the input — repair. Structured CALLs are for machines and copy-paste; the owner never has to compose one.
2. **WORK** — follow the play. Cross-cutting moves available in any session:
   - `call:research` — spawn a bounded child question (CALL packet, §4); children may spawn their own.
   - `call:executor` — delegate execution to a working agent (CALL packet, §4).
   - `capture` — record emergent work or an idea as one line in RESULT.captures. Never act on a capture in the same session; it is triaged at shape or pulse.
   - `decision` — put a question to the owner in RESULT.decisions_needed, always with 2–3 options and a recommendation.
3. **CLOSE** — emit RESULT (§4) as the session's final message only: a readable owner summary first, then the single fenced RESULT block. A RESULT block appears nowhere else; emitting one ends the session, checkpoint included. A writer agent applies state_changes and commits. The session is dead after RESULT; continuation happens in a fresh session via RESULT.next. A session may close early with a **checkpoint** RESULT (partial outcome, task stays active, continuation CALL) — switching platforms or splitting long work is normal.

**Orientation header.** Every owner-facing reply starts with one line:
`📍 <direction> / <node> / <task> — <play>: <current step> | нужно от тебя: <ничего | вопрос>`

**Language.** Talk to the owner in the owner's language (Russian). State files keep keys in English; values may be any language.

**Owner-facing vs machine.** The RESULT block — and any packet or state file, a charter draft included — is a machine artifact for the writer. What the owner reads is its substance as a readable summary in his language, never a YAML/state dump as the reply body; the machine block rides once, fenced, at the end of the final message, for the relay to carry.

**Sessions do not write.** No session edits repo state directly — a repo tool or connector is read access, not write permission. State changes travel only inside RESULT.state_changes, applied by the writer (os/adapters/coding-agent.md); an agent-CLI session on this repo becomes its own writer only after emitting its RESULT.

**Two-strikes rule.** After two failed correction rounds on the same point: stop, close with a handoff note in RESULT, continue in a fresh session.

**Read-only exception.** Answering owner questions from state needs no play and no RESULT — and must change nothing. Owner-initiated exploration or brainstorming that starts producing ideas worth keeping runs as a research session instead (`play: research, goal: explore X`), so captures return via RESULT.

## 3. Direction state — six file types, never more

| File | Holds | Written by |
|---|---|---|
| `CHARTER.md` | mission, measurable success criteria, constraints, lenses, product repos | frame |
| `TREE.md` | recursive goal tree — outcomes only, no tasks; every non-root node carries its one-line `why` | frame (root), map, shape (splits), review |
| `NOW.md` | the active bet, its tasks, recurring obligations, open calls (in-flight registry), decision inbox, ready next CALL | every session |
| `LOG.md` | append-only: one line per session + link | every session |
| `history/` | full RESULT of every session, one file each | append-only |
| `knowledge/` | accepted facts and decisions; each entry names who reads it and when | review, pulse |

`work/` holds products (documents, assets, scans) — outputs, not state.

**Goal tree node:** `id` (stable short id, e.g. `g-3f7a`), `goal` (an outcome in the world, not an activity), `done_when` (verifiable), `status: parked | shaped | active | done | dropped`, optional `children`. A shaped node also carries `appetite` (time budget) and `kill_by` (metric + threshold + date).

A **bet** is one shaped node committed into `NOW.md` with tasks. Tasks (`t-1`…) exist only there: `goal`, `done_when`, `status`, sized at half a focused day or less.

## 4. Packets

**CALL** — the only way work moves between sessions and agents:
`goal` (outcome, not method) · `context` (file pointers, links — enough to work without asking) · `boundaries` (out of scope, do not touch) · `done_when` (verifiable) · `return` (expected format) · `budget` (time or effort cap).

**RESULT** — the only way a session ends:
`outcome` (what changed in the world, not a narrative of effort) · `evidence` (proof matching done_when) · `state_changes` (exact NOW/TREE edits) · `captures` · `decisions_needed` · `play_check` (one line per play step: done or skipped+why; steps the play marks `(owner)` cite the owner's words) · `log` (one line) · `next` (ready CALL, or `awaiting_decision`).

An executor CALL for engineering goes to a coding agent in the direction's product repo. The agent owns solution architecture and implementation mechanics inside the writer-finalized transaction identity; evidence is commits/PR plus check output. For engineering work the OS pins the target worktree, branch, base authority and acceptance identity so a later session cannot silently switch transactions.

## 5. Hard gates — all mechanically checkable

- **G1 (WIP).** One active bet per direction; ≤3 active tasks. Nothing new starts until something finishes or dies.
- **G2 (rolling wave).** Tasks exist only inside the active bet. Every other tree node stays outcome-level.
- **G3 (appetite).** Appetite is set before tasks are written and never extends. There is no extend operation: an over-appetite bet dies; continuing means re-shaping a new bet.
- **G4 (bet validity).** A bet without done_when and kill_by is invalid.
- **G5 (evidence).** `done` requires evidence matching done_when. A bet is verified in a session other than the one that did the work, by trying to refute the claim, not confirm it.
- **G6 (shape validity).** A shape output without a cut list (≥1 real cut), a lens sweep verdict per lens, and a task testing the riskiest assumption is invalid.
- **G7 (decisions).** Every owner decision request carries options and a recommendation; decisions are batched, never scattered through a session.
- **G8 (intake).** New directions and new top-level goals enter only through frame. New ideas default to `parked` — the parking lot is the system's normal answer to enthusiasm.
- **G9 (co-creation).** CHARTER.md and TREE.md change only with the owner's explicit in-session approval: planning sessions present drafts one artifact at a time (a tree node is an artifact, carrying its one-line `why`), and the RESULT marks each approval (`owner_approved`). The writer rejects charter/tree changes without it.
- **G10 (protocol).** The first reply carries the play's step plan; a RESULT block appears only as the final message; sessions never write state directly. The writer rejects a RESULT whose `play_check` misses a step or whose `(owner)` steps lack the owner's actual words.

A session that cannot pass a gate stops and reports — it never improvises around a gate.

## 6. Plays

`frame · map · shape · converge · converge-arch · converge-verify · work · guide · review · research · pulse · repair` — defined in `os/plays/`. Directions may add local plays in `live/<id>/plays/` (procedure files, not state; same format and budget; invoked as `play: local/<name>` — see `os/EXTENDING.md`). A session that does not know its play is in repair.

## 7. Changing the OS

The OS is infrastructure, not a direction. It changes only in maintenance sessions on this repo following `os/MAINTENANCE.md`: an explicit owner request is a sufficient trigger; self-initiated changes need ≥2 entries on the same point in `os/FRICTION.md`. Budgets are absolute: kernel ≤1500 words, a play ≤600 words, six state file types. Wanting more structure is usually the wrong problem.

END_OF_FILE: os/KERNEL.md
