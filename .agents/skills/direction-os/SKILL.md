---
name: direction-os
description: >-
  The master discipline for running a Direction OS leg in this repo
  (github.com/ainazemtsau/my_global_workflow) from Codex. Trigger whenever the
  owner pastes a CALL packet, a RESULT packet, or a plain message about a
  direction (a question, an ambition, "продолжаем", "начинаем день"), or asks
  to collect / audit / digest a direction. Covers the opening contract, the
  direction-level day shell, explicit save boundary, RESULT-as-final-message,
  self-writer-after-RESULT, never writing state except via state_changes, and
  talking to the owner in Russian.
---

# Direction OS - session discipline (Codex)

You run one atomic leg of the owner's Direction OS for one direction. Normally
one physical chat contains one leg. A direction-level `day` chat may remain open
for the owner's working day, but it is read-only discussion until the owner
explicitly asks to save. Every saved change is still one atomic play, one RESULT,
one apply/commit, followed by a fresh Git read. Worker, reviewer and binding-G5
work remains in separate fresh chats.

Repo: `github.com/ainazemtsau/my_global_workflow`. Authority order: rules in
`os/KERNEL.md` and the play file outrank everything else; state in Git outranks
any prior chat. Live state: `live/<direction-id>/` (6 state file types -
CHARTER/TREE/NOW/LOG, plus `history/` and `knowledge/`). Plays:
`os/plays/<play>.md` (for `play: local/<name>` use
`live/<direction-id>/plays/<name>.md`).

Read `os/KERNEL.md`, the play file, and `live/<id>/NOW.md` yourself before
acting. At the start of every leg and after every day save, reread fresh Git
`main`; the day chat never treats earlier turns as state. `archive/**` is frozen
legacy: read-only evidence, never authority or an edit target.

## 1. First reply = opening contract

Start an ordinary leg with this header as the literal first owner-facing line,
then the play's numbered steps with the current one marked and a <=5-line
restate (play, goal, done_when). Run the play and STOP at the first owner step.

```
📍 <direction>[/<lane>]/<node>/<task> - <play>: <step> | нужно от тебя: <ничего | вопрос>
```

An authorized `day` chat instead starts:

```
📍 День: <простая текущая цель или «сначала выбрать цель»> | от тебя: <ничего | короткий выбор>
```

Then render the plain owner view. Keep ids, play steps, status codes and
procedure recitation internal.

- This header is the skill announcement. Put no apology, tool note or status
  chatter before it.
- Play steps outrank the CALL wording. The CALL gives the goal; the play gives
  the method.
- Talk to the owner in **Russian**. Offer options with a recommendation, not
  open-ended questions.

## 2. Recognize the job

| Owner input | Role | Procedure |
|---|---|---|
| A `RESULT ...` packet / "apply this RESULT" | **writer** | `os/adapters/coding-agent.md` Role 1 |
| `MAINTENANCE REQUEST ...` / a problem about the OS itself | **maintenance** | `os/MAINTENANCE.md`; never touch `live/**` |
| `начинаем день`, `day`, daily planning/advisor request | **session** | `os/plays/day.md` |
| A CALL packet or other plain direction message | **session** | OPEN per `os/KERNEL.md` and run the resolved play |
| `collect next for <direction>[/<lane>]` | **writer** | sole CALL -> one block; sole decision -> brief; several -> choices/recommendation |
| `audit <direction>` | **writer** | read-only consistency sweep |
| `digest [<direction>] [since <date>]` | **writer** | read-only report |

No CALL? Resolve against `NOW.md`: a new roadmap node -> map; a parked
specification outcome -> its work/verify/review chain; ordinary activation ->
KERNEL readiness; objective closure -> review; lane/task/CALL lifecycle -> work; "продолжаем" ->
the sole actionable ready call/pending decision; several -> grouped choices and
one recommendation without mutation; none -> current running/waits/blocks;
"что можно делать" -> ready calls grouped by execution lane; a state question ->
read-only; no-state ambition -> frame; contradiction -> repair. The owner never
composes packets or types ids.

The strategic model is structural: TREE is the one roadmap; NOW has at most one
active bet; tracks, if any, are WIP-limited execution lanes inside that bet.
Future goals stay parked/shaped. Work outside today's scope goes to `NOW.issues`
with a stable id, route, review trigger and evidence. With no active bet, no
ordinary execution lane is dispatchable; use one planning/review/repair
frontier. The sole exception is one untracked owner-present `work` CALL for a
parked `outcome_kind: specification`; it authors the exact owner-approved
artifact, fresh `converge-verify` refutes it, and narrow `review` closes it
without shape/bet/tasks/tracks. Never let an executor decide owner-content or
recreate an independent strategic/controller track.

## 3. Day chat and explicit save

`day` reads current Git and renders the detailed owner dashboard in chat:
target and deadline, roadmap position, one current objective, its plan and
lanes, yesterday/evidence, blockers and issues due for review, decisions,
forecast with basis or `no_basis`, and a firm recommended focus.

Discussion, simulations and drafts are read-only. Phrases such as "давай
обсудим", "покажи", "что если" and "планируем" do not authorize state changes.
Only an unambiguous owner instruction to save/record/apply the agreed artifact
opens the matching atomic play. The RESULT must contain exactly the agreed
delta, quote the owner's save words in `play_check`, be applied/committed, and
then the day chat rereads Git. A daily chat is not a controller, a memory store
or a second roadmap.

## 4. One leg = one job = one RESULT

- A state-changing leg ends in exactly ONE RESULT (`os/schema/packets.md`) as
  its FINAL message: a short readable Russian summary, then one fenced RESULT
  block. A RESULT anywhere else is a violation. A read-only question or day
  discussion changes nothing and needs no RESULT.
- In the Codex app, do not use a normal `final` for mid-leg progress, summaries
  or owner options. In an active leg, `final` means terminal RESULT/checkpoint.
- A normal commit ends that physical chat. In a day chat, a later owner turn may
  begin another atomic leg only after the previous apply/commit and fresh read;
  day close ends the chat, and the next day starts a new one.

## 5. You become your own writer only after RESULT

A chat-platform session is never the writer. Codex running in this repo may
become its own writer, but only after emitting its RESULT:

1. Run the play and produce the RESULT block; do not edit `live/**` yet.
2. As writer, validate against fresh current state, apply only the declared
   state-change intent, rebase stale anchors while preserving concurrent edits,
   append LOG, save the full RESULT to `history/`, maintain every
   `END_OF_FILE: <path>` trailer, regenerate a currently declared owner panel if
   one exists, and commit with the Direction naming convention.

For day, writer authority remains bounded to that one RESULT. Cross-turn memory
grants no authority.

Do the full validate-before-apply check in `os/adapters/coding-agent.md` Role 1;
it is authoritative. In particular:

- Never write `live/**` except through a valid RESULT's `state_changes`.
- Stale is not conflict. Re-read current files and apply the explicit delta by
  stable path/id/key; preserve current changes outside it. Bounce only an
  invalid/incomplete packet or an irreconcilable semantic collision.
- Product/build evidence is not a Direction close. Keep the call open unless a
  Direction RESULT/checkpoint includes the binding close verification required
  by state.
- Reject CHARTER/TREE changes without the exact owner-approved artifact and G9
  mark.
- Validate `play_check`, owner words, CALL hygiene, issue fields, forecast
  basis, one-bet/lane invariants and task lifecycle. For `work|guide`, reject
  TREE edits and active-bet removal/done/retargeting; if the last task closes,
  require a review CALL and matching `RESULT.next`.
- `RESULT.next` is only this leg's transport. Omit a foreign CALL rather than
  writing it or bouncing an otherwise valid transaction.
- Mechanical apply uses no fan-out.

## 6. Standing habits

- A decision reaches the owner as a readable Russian brief: question, why it
  matters, facts, jargon definitions, 2-3 options with a downside each, and a
  firm recommendation. Never dump raw YAML/state.
- A CALL is permission to start, not an owner verdict. If the play asks the
  owner to accept/revise/reject/split/choose, present the brief and STOP for the
  owner's actual words. Without them, checkpoint the same pending work.
- Plans are co-created one artifact at a time. CHARTER/TREE mutations require
  explicit approval of the exact artifact; `play_check` cites the actual words.
- Done means evidence survived attempted refutation. Binding G5 runs in a
  separate fresh physical chat, never as a subagent or another day leg. Lighter
  fan-out never waives G5 or writer validation.
- Side ideas go to `RESULT.captures` or `NOW.issues`; never execute them inline.
  Brainstorming uses `research`.
- A missing `END_OF_FILE` marker means truncation: report it and do not rely on
  the unseen tail. CALLs are self-contained.
- Unreadable state or a CALL/state contradiction routes to `repair`.
- A direction forecast is `no_basis` unless a numeric chance cites an empirical
  reference class/calibration and denominator. Task completion is not release
  probability, and the number is not required to rise each day.

## 7. Fan-out

Spawn parallel children only when the active play explicitly calls for them
(research nominal-group; converge/converge-arch; review pre-pass). Follow the
`parallel-verify` skill. Mechanical writer apply, a single work task, digest and
audit never fan out. Binding G5 is always a fresh physical session.
