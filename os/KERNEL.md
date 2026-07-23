# KERNEL — Direction OS

Authority order: live owner instruction > this kernel > the active play > direction state files > everything else (history, prior chats, model memory). On conflict the higher source wins; log the conflict as friction (§7).

## 1. What this is

In this file, legacy word `session` means atomic leg unless `physical chat` is explicit.

The OS runs the owner's life directions — long-term ambitions — through many short AI sessions over durable state in a git repository.

- A **direction** lives in `live/<id>/` as the fixed state files (§3).
- A **leg** is one job under one play. Normally one chat = one leg. Only an owner-approved `outcome_dispatch` controller may keep one physical chat for one day and run sequential legs; before each it rereads fresh Git `main`, and the next day starts a new chat. Context is RAM: unwritten memory is not state.
- A **play** is a named procedure in `os/plays/`; only plays change state.
- The **owner** decides. Agents do everything else. Packets are self-contained; no play makes the owner copy state by hand.

## 2. Session contract

1. **OPEN** — input is a CALL **or a plain owner message**. Read `NOW.md` and the play's files. Resolve plain input against NOW: new TREE-backed track → map; retirement/primary handoff → review; other lifecycle or launch/loss → work; track/task/CALL → its call/decision; "продолжаем" → sole actionable call/decision; several → grouped choice/recommendation without mutation; none → running/waits/blocks/pauses; "что можно делать" → ready calls by track; question → read-only; no-state ambition → frame; otherwise interpret and confirm. For an authorized controller, `начинаем день`, launch receipt, refill/`что ещё`, material event, and `закрываем день` are successive work-leg intents against its ordinary root. The first reply of every leg is the **opening contract**: orientation header, numbered play steps with the current one marked, and a ≤5-line restate (play, goal, done_when); then run the play and stop at the first owner step. Play outranks CALL. Contradictory state → repair. The owner never composes packets.
2. **WORK** — follow the play. Cross-cutting moves available in any session:
   - `call:research` — spawn a bounded child question (CALL packet, §4); children may spawn their own.
   - `call:executor` — delegate execution to a working agent (CALL packet, §4).
   - `capture` — record emergent work or an idea as one line in RESULT.captures. Never act on a capture in the same session; it is triaged at shape or pulse.
   - `decision` — put a question to the owner in RESULT.decisions_needed, always with 2–3 options and a recommendation.
3. **CLOSE** — emit RESULT (§4) as the leg's final message only: readable summary, then one fenced RESULT. It ends the leg, checkpoints included; the writer applies/commits state_changes. Normal continuation uses RESULT.next in a fresh chat. A day controller may accept the next owner turn in the same physical chat only after that transaction, starting again at OPEN; day close ends it. A checkpoint keeps partial work active through a continuation CALL.

**Orientation header.** Every owner-facing reply starts with one line:
`📍 <direction> / <track-or-legacy> / <node> / <task> — <play>: <current step> | нужно от тебя: <ничего | вопрос>`

**Language.** Talk to the owner in the owner's language (Russian). State files keep keys in English; values may be any language.

**Owner-facing vs machine.** The RESULT block — and any packet or state file, a charter draft included — is a machine artifact for the writer. What the owner reads is its substance as a readable summary in his language, never a YAML/state dump as the reply body; the machine block rides once, fenced, at the end of the final message, for the relay to carry.

**Legs do not write.** Repo access is not write permission. Changes travel only inside RESULT.state_changes, applied by the writer; an agent-CLI leg here becomes its own writer only after emitting its RESULT.

**Two-strikes rule.** After two failed correction rounds on the same point: stop, close with a handoff note in RESULT, continue in a fresh session.

**Read-only exception.** A state question needs no play or RESULT and changes nothing. Exploration producing keepable ideas runs as research so captures return via RESULT.

## 3. Direction state — six file types, never more

| File | Holds | Written by |
|---|---|---|
| `CHARTER.md` | mission, measurable success criteria, constraints, lenses, product repos | frame |
| `TREE.md` | recursive goal tree — outcomes only, no tasks; every non-root node carries its one-line `why` | frame (root), map, shape (splits), review |
| `NOW.md` | active bet/tasks, optional track index, open-call dispatch frontier, recurring work, decisions | every leg |
| `LOG.md` | append-only: one line per leg + link | every leg |
| `history/` | full RESULT of every leg, one file each | append-only |
| `knowledge/` | accepted facts and decisions; each entry names who reads it and when | review, pulse |

`work/` holds products (documents, assets, scans) — outputs, not state.

**Goal tree node:** `id` (stable short id, e.g. `g-3f7a`), `goal` (an outcome, not an activity), `done_when` (verifiable), `status: parked | shaped | active | parallel | done | dropped`, optional `children`. `active` is the one bet; `parallel` is a routing-only track with no tasks. A shaped node also carries `appetite` and `kill_by`.

A **bet** is one shaped node in `NOW.md`. Its tasks (`t-1`…): `goal`, `done_when`, `status`, each ≤ half a focused day.

## 4. Packets

**CALL** — the only way work moves between sessions and agents:
`goal` (outcome, not method) · `context` (file pointers, links — enough to work without asking) · `boundaries` (out of scope, do not touch) · `done_when` (verifiable) · `return` (expected format) · `budget` (time or effort cap).

**RESULT** — the only way a session ends:
`outcome` (what changed in the world, not a narrative of effort) · `evidence` (proof matching done_when) · `state_changes` (exact NOW/TREE edits) · `captures` · `decisions_needed` · `play_check` (one line per play step: done or skipped+why; steps the play marks `(owner)` cite the owner's words) · `log` (one line) · `next` (local issued CALL, `awaiting_decision`, or `return-to-parent/requester/owner`). It never writes NOW or selects foreign work.

In track-mode a continuation may be `running|waiting|blocked|paused`; `open_calls.status` decides whether it is dispatchable.

An engineering CALL goes to the product repo. Its `return` comes HOME; only Direction issues successor CALLs. Evidence = commits/PR + checks; the OS pins no branch/path/SHA.

## 5. Hard gates — all mechanically checkable

- **G1 (WIP).** One active bet per direction; ≤3 active tasks. Track-mode: owner-set WIP limit caps non-paused roots/decisions; ≤1 root/track; children share its budget.
- **G2 (rolling wave).** Tasks exist only inside the active bet. Every other tree node stays outcome-level.
- **G3 (appetite).** Appetite is set before tasks are written and never extends. There is no extend operation: an over-appetite bet dies; continuing means re-shaping a new bet.
- **G4 (bet validity).** A bet without done_when and kill_by is invalid.
- **G5 (evidence).** `done` requires evidence matching done_when. Verification tries to refute the claim in a separate physical chat from the work and from any day controller; an in-controller leg is never binding G5.
- **G6 (shape validity).** A shape output without a cut list (≥1 real cut), a lens sweep verdict per lens, and a task testing the riskiest assumption is invalid.
- **G7 (decisions).** Every owner decision request carries options and a recommendation; decisions are batched, never scattered through a leg.
- **G8 (intake).** New directions and new top-level goals enter only through frame. New ideas default to `parked` — the parking lot is the system's normal answer to enthusiasm.
- **G9 (co-creation).** CHARTER.md and TREE.md change only with the owner's explicit in-leg approval: planning legs present drafts one artifact at a time (a tree node is an artifact, carrying its one-line `why`), and the RESULT marks each approval (`owner_approved`). The writer rejects charter/tree changes without it.
- **G10 (protocol).** Every leg's first reply carries the play steps; RESULT appears only in its final message; legs never write state directly. The writer rejects missing `play_check` steps or owner steps without actual words.

A session that cannot pass a gate stops and reports — it never improvises around a gate.

## 6. Plays

`frame · map · shape · converge · converge-arch · converge-verify · work · guide · review · research · pulse · repair` — defined in `os/plays/`. Directions may add local plays in `live/<id>/plays/` (procedure files, not state; same format and budget; invoked as `play: local/<name>` — see `os/EXTENDING.md`). A session that does not know its play is in repair.

## 7. Changing the OS

The OS is infrastructure, not a direction. It changes only in maintenance sessions on this repo following `os/MAINTENANCE.md`: an explicit owner request is a sufficient trigger; self-initiated changes need ≥2 entries on the same point in `os/FRICTION.md`. Budgets are absolute: kernel ≤1500 words, a play ≤600 words, six state file types. Wanting more structure is usually the wrong problem.

END_OF_FILE: os/KERNEL.md
