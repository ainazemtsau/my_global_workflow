# Repository Agent Instructions

This repository is the **Direction OS** — the owner's workflow system. Rules: `os/KERNEL.md`. Live direction state: `live/<direction-id>/`. Everything under `archive/**` is frozen legacy: read-only evidence, never authority, never a target of edits.

## Recognize your job from the input

| Input pasted/typed by the owner | Your role | Procedure |
|---|---|---|
| A `RESULT ...` packet (or "apply this RESULT") | **writer** | `os/adapters/coding-agent.md`, Role 1: apply the declared state-change intent against fresh current state, rebase stale blob/anchor preconditions while preserving concurrent edits, append LOG, save full RESULT to history/, maintain `END_OF_FILE:` trailers, regenerate the direction's declared owner panel if one exists (rules in the direction's `knowledge/`; adapter Role 1), commit, hand back the local `RESULT.next` continuation or fresh frontier. Bounce only an invalid/incomplete RESULT or local handoff, or an irreconcilable logical collision after rebase. |
| `MAINTENANCE REQUEST ...` (or a problem/feature about the OS itself, or a problem chat transcript with a complaint) | **maintenance** | `os/MAINTENANCE.md`. One problem per session. Never touch `live/**`. |
| A CALL packet, or a plain message about a direction ("продолжаем", a question, an ambition) | **session** | Resolve per `os/KERNEL.md` §2 OPEN; run the play from `os/plays/` (or `live/<id>/plays/` for `local/*`). In an agent CLI on this repo you become your own writer only AFTER emitting your RESULT: then apply its state_changes and commit. Chat-platform sessions are never the writer. |
| `collect next for <direction>[/<track>]` | **writer** | A sole CALL gets one paste block; a sole decision gets its brief; several return choices/recommendation, never a guess. |
| `audit <direction>` | **writer** | `os/adapters/coding-agent.md` Role 1 audit command: read-only consistency sweep of `live/<id>/`, report only — state drift → ready repair CALL, rule defect → draft MAINTENANCE REQUEST. Never edits anything. |
| `digest` (optionally `<direction>` / `since <date>`) | **writer** | `os/adapters/coding-agent.md` Role 1 digest command: read-only morning report — LOG lines from the window, current bets/tasks, pending decisions, and call frontiers across live directions. Render only: never edits, never proposes. |

## Hard rules

- One atomic leg = one job. Normally one physical chat contains one leg and ends after commit. The sole exception is an owner-approved `outcome_dispatch` controller: one physical chat may hold sequential controller legs for one day, rereading fresh Git `main` before each leg; every state-changing leg still has one play, one RESULT, one apply/commit. Its workers, reviewers, dedicated writers, and binding G5 remain separate fresh chats; day close ends the controller chat and the next day starts a new one.
- `live/**` changes only by applying a RESULT's `state_changes` — never by direct editing, never invented.
- A writer treats blob/SHA/old-text preconditions as rebase bases, not freshness locks. Stale state is expected under parallel sessions: re-read current files, apply the RESULT's explicit delta by stable path/id/key, and preserve current changes outside that delta. Staleness alone is never a bounce.
- A builder/executor handback, merge request, product RESULT, owner playtest summary, or "formally closed on dev/dev2" prose is **not** a Direction-OS close. It is evidence input. The writer may clear an `open_call` or mark done only from a valid Direction-OS RESULT/checkpoint whose evidence includes the required binding close verification; product gates + merge/push alone are never enough.
- Every state file you write ends with its `END_OF_FILE: <path>` trailer.
- Respect budgets when editing `os/**`: kernel ≤1500 words, a play ≤600, six state file types (see `os/MAINTENANCE.md`).
- Small diffs; descriptive commit messages (`<direction>[/<track>] <play> <node/task>: <log line>` for state, plain descriptive for os/).
- Do not delete files outside the scope of the job.

<!-- BEGIN: Codex multi-agent section — splice into repo-root AGENTS.md. Keep terse (32 KiB cap). -->

## Codex: how to work this OS

When running as **Codex** in this repo, you are a Direction-OS session/writer like any other coding agent. Four rules:

0. **Protocol lock comes before all Codex chatter.** For any Direction OS leg, the FIRST owner-facing line must be the `📍 ...` opening-contract header from `direction-os` — no skill-announcement, apology, summary, or "I'll read files" line may precede it. If a generic Codex skill rule asks you to announce the skill, the opening-contract header satisfies the announcement; any extra "using direction-os" note goes after the header. During an active leg, do not use the app's final answer as an ordinary progress answer: final = terminal RESULT/checkpoint only. If you cannot produce a RESULT yet, keep working in commentary or ask the required owner question. A day controller starts another leg only on a later owner turn and after a fresh Git read.

1. **Follow the direction-os skill.** The job-recognition table and hard rules above are authoritative. For the full procedure load the `direction-os` skill (`.agents/skills/direction-os/SKILL.md`) — it points at `os/KERNEL.md`, the play, and `os/adapters/coding-agent.md` (the binding authority for the writer's validate-before-apply checks). Read state from `live/<id>/`; write state ONLY via a RESULT's `state_changes`.

   **Owner-verdict guard.** A CALL is permission to start the session, not permission to decide. If the CALL/play asks for an owner-readable verdict (`accepted/revised/rejected/split`, approve/reject, choose, "можно записывать", or similar), first present a normal human brief with options/recommendation and STOP for the owner's actual words. Do not open the downstream CALL until those words exist and can be cited in `play_check`/evidence. Without the verdict, checkpoint by clearing the returning id and issuing a new continuation CALL for the same pending work.

2. **Realize a play's parallel children as subagents — but only when the play calls for it.** A play that mandates in-leg fan-out (research nominal-group generators + miner + strategic_search; converge/converge-arch miners + strategic_search) is run by spawning the matching role worker once per child, then merging/deduping their reports yourself. The role text lives in `.codex/agents/*.toml` (`explorer`, `researcher`, `validator`; `builder` is for product repos only). Native Ultra may delegate proactively, but a Direction-OS leg fans out only where its play/CALL requires it. **Known limitation:** on the desktop app / Windows, spawning a custom agent BY NAME may be unavailable (openai/codex #15250, #26828) — fall back to spawning the generic `explorer`/`worker` and injecting that role's `developer_instructions` as the prompt; see the `parallel-verify` skill. **Mechanical legs stay single-agent** (writer apply, a single `work` task, digest, audit): no subagents.

3. **Keep G5 as a fresh refutation session; model identity is never a gate.** Gate G5 ("done" needs evidence) is verified by *trying to refute* a claim in a SEPARATE physical chat from the one that did the work, including any day-controller chat. A different model or provider may add optional diversity when available, but model identity or availability never affects review eligibility and cannot block the leg. Codex subagents are still same-session helpers, so they may provide a pre-pass only; the binding G5 pass is a fresh session. State in your RESULT whether evidence came from an in-session pre-pass or from the binding fresh review. A CALL phrase like "no heavy multi-agent refutation" reduces fan-out only; it does **not** waive G5, writer validation, or the requirement to leave the `open_call` open until the close evidence exists.

Setup, replication, the by-name-spawn limitation, and version caveats: `.codex/README-CODEX-KIT.md`.

<!-- END: Codex multi-agent section -->

END_OF_FILE: AGENTS.md
