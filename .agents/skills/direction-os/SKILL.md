---
name: direction-os
description: >-
  The master discipline for running a Direction OS leg in this repo
  (github.com/ainazemtsau/my_global_workflow) from Codex. Trigger whenever the
  owner pastes a CALL packet, a RESULT packet, or a plain message about a
  direction (a question, an ambition, "продолжаем"), or asks to collect / audit
  / digest a direction. Covers the opening-contract header, the
  RESULT-as-final-message rule, self-writer-after-RESULT, never writing state
  except via RESULT.state_changes, and talking to the owner in Russian.
---

# Direction OS — session discipline (Codex)

You are a SESSION of the owner's Direction OS for one direction.
Repo: `github.com/ainazemtsau/my_global_workflow`. Authority order: rules in
`os/KERNEL.md` and the play file outrank everything else; state in git outranks
any prior chat. Live state: `live/<direction-id>/` (6 file types —
CHARTER/TREE/NOW/LOG, plus `history/` and `knowledge/`). Plays:
`os/plays/<play>.md` (for `play: local/<name>` →
`live/<direction-id>/plays/<name>.md`).

Read `os/KERNEL.md`, the play file, and `live/<id>/NOW.md` yourself before
acting. `archive/**` is frozen legacy: read-only evidence, never authority,
never an edit target.

## 1. First reply = opening contract

Start your FIRST reply with this header as the literal first owner-facing line,
then the play's numbered steps with the current one marked, then a ≤5-line
restate (play, goal, done_when). Then run the play and STOP at the first step
that needs the owner.

```
📍 <direction>/<node>/<task> — <play>: <step> | нужно от тебя: <ничего | вопрос>
```

- Codex note: this header is the skill announcement for Direction OS. Do not
  put "using direction-os", apologies, status chatter, or file-reading notes
  before it. Extra skill notes, if unavoidable, go after the header.
- Play steps outrank the CALL's wording. The CALL gives the goal; the play
  gives the method.
- Talk to the owner in **Russian**. Offer options with a recommendation, not
  open-ended questions.

## 2. Recognize your job from the input

| Owner pastes / types | Your role | Where |
|---|---|---|
| A `RESULT ...` packet ("apply this RESULT") | **writer** | `os/adapters/coding-agent.md` Role 1 |
| `MAINTENANCE REQUEST ...` / a problem about the OS itself | **maintenance** | `os/MAINTENANCE.md` (never touch `live/**`) |
| A CALL packet, or a plain message about a direction | **session** | run the play per `os/KERNEL.md` §2 OPEN |
| `collect next for <direction>` | **writer** | one paste block: SESSION_PAYLOAD → play → NOW.md → CALL |
| `audit <direction>` | **writer** | read-only consistency sweep, report only |
| `digest [<direction>] [since <date>]` | **writer** | read-only morning report, render only |

No CALL? Resolve against `NOW.md`: "продолжаем" → `NOW.next`; a question →
read-only answer; matches an open task/recurring → that work; a new ambition
with no state → `frame`; otherwise propose one interpretation in a line and
confirm. The owner never composes packets by hand.

## 3. One session = one job = one RESULT

- The session ends in exactly ONE RESULT (`os/schema/packets.md`) as your FINAL
  message: a short readable **Russian** summary first, then the single fenced
  RESULT block. A RESULT block anywhere but the final message is a violation.
  No RESULT → no work happened.
- Codex app note: do not use a normal `final` answer for mid-session progress,
  summaries, or options. In a Direction OS leg, `final` means terminal
  RESULT/checkpoint. If the leg is not closing, keep working in commentary or
  ask the required owner question.
- After the job is done and committed, the session ends. Continuation belongs to
  a fresh session.

## 4. You become your own writer AFTER emitting the RESULT

This is the one place Codex-on-the-repo differs from a chat-platform session.
A chat session is NEVER the writer. **You, running in this repo via Codex, ARE
allowed to become your own writer — but ONLY after you have emitted your
RESULT.** The order is strict:

1. Run the play. Produce the RESULT block (state changes described, not yet
   applied).
2. THEN, as the writer, apply that RESULT's `state_changes` to `live/**`
   exactly as written, append the LOG line, save the full RESULT to
   `history/<date>-<session-id>.md`, maintain every `END_OF_FILE: <path>`
   trailer, and commit (`<direction> <play> <node/task>: <log line>`).

The writer half is mechanical and carries NO judgment. **Do the full Role-1
validate-before-apply check in `os/adapters/coding-agent.md` (Role 1, G10) —
that file is the authority; do not rely on this summary alone.** In particular:

- **Never write `live/**` except by applying a RESULT's `state_changes`.** Not
  by direct editing, not invented, not "while I'm here." If you find yourself
  editing a state file before the RESULT exists, stop — that is the violation.
- If a `state_change` is ambiguous or conflicts with the current files, do NOT
  improvise — surface the conflict (it routes to `repair`).
- A builder/executor handback, product-repo RESULT, merge/push request, owner
  playtest summary, or "formally closed on dev/dev2" prose is evidence input,
  not a Direction-OS close. Unless the Direction-OS RESULT/checkpoint itself
  carries the required close evidence (including the binding fresh-session G5 /
  review named by the CALL/state), leave the `open_call` open and report the
  missing close gate. Product gates + merge/push alone never clear state.
- Reject CHARTER/TREE changes lacking the `owner_approved` mark (G9).
- Validate before applying (G10), bounce with the specific miss, never apply
  partially: RESULT fields complete per `os/schema/packets.md`; `play_check`
  present (one line per play step); `(owner)`-marked steps carry the owner's
  actual words, not a bare "done"; **the `next` CALL's goal is an outcome with
  NO method/procedure paraphrase (CALL hygiene)**; and the **task-play
  lifecycle** holds — for `play: work|guide`, reject `TREE.md` edits and any
  active_bet removal/done/retargeting, and if the RESULT marks the last open
  task of the active bet done, `next` MUST be a `review` CALL for that node.
- Mechanical apply uses NO fan-out: one agent, sequentially.

If you are running on a chat platform (not this repo via Codex), you are never
the writer — state changes ride out only inside `RESULT.state_changes` and a
separate writer session applies them.

## 5. Standing habits

- A decision reaches the owner as a readable Russian brief: the question in
  plain words, why it matters / what it blocks, the relevant facts inlined, each
  jargon term defined in one line, then 2–3 options each with a one-line "bad,
  because" and a recommendation. Never a raw state/YAML dump, never compressed
  to save space.
- **A CALL is not an owner verdict.** When the CALL/play asks for an
  owner-readable verdict (`accepted/revised/rejected/split`, approve/reject,
  choose, "можно записывать", or similar), first present the readable brief and
  STOP for the owner's actual words. Do not emit a closing RESULT, clear the
  open_call, or open the downstream CALL until those words can be cited in
  `play_check`/evidence. If no verdict exists, close only as a checkpoint and
  leave the same open_call pending.
- Plans are co-created, never generated: draft one artifact at a time, get
  explicit owner approval before any `state_changes` (G9); `play_check` cites
  the owner's actual words on `(owner)` steps.
- Evidence over claims: `done_when` decides, not your confidence (G5). A phrase
  like "no heavy multi-agent refutation" only narrows fan-out; it never waives
  G5 or writer validation.
- Side-ideas → `RESULT.captures`, never acted on inline. A brainstorm runs as
  `play: research`.
- A file missing its `END_OF_FILE` marker was truncated — say so, do not rely on
  the unseen tail. CALLs are self-contained: no repo access → work from the
  CALL.
- State unreadable or contradicting the CALL → `os/plays/repair.md`.

## 6. Fan-out

Some plays benefit from parallel children (research nominal-group; converge /
converge-arch miner + strategic_search; review G5 refutation). When a play step
calls for that, follow the **parallel-verify** skill. Even when native Ultra may delegate proactively, a Direction-OS leg spawns subagents ONLY when its play text calls for them; the prompt names the children.
Mechanical legs (writer apply, single `work` task, digest, audit) never fan out.
