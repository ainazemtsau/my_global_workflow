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
| `digest` (optionally `<direction>` / `since <date>`) | **writer** | `os/adapters/coding-agent.md` Role 1 digest command: read-only morning report — LOG lines from the window, current bets/tasks, pending decisions, next CALLs across live directions. Render only: never edits, never proposes. |

## Hard rules

- One session = one job. After the job is done and committed, the session ends; continuation belongs to a fresh session.
- `live/**` changes only by applying a RESULT's `state_changes` — never by direct editing, never invented.
- A builder/executor handback, merge request, product RESULT, owner playtest summary, or "formally closed on dev/dev2" prose is **not** a Direction-OS close. It is evidence input. The writer may clear an `open_call` or mark done only from a valid Direction-OS RESULT/checkpoint whose evidence includes the required binding close verification; product gates + merge/push alone are never enough.
- Every state file you write ends with its `END_OF_FILE: <path>` trailer.
- Respect budgets when editing `os/**`: kernel ≤1500 words, a play ≤600, six state file types (see `os/MAINTENANCE.md`).
- Small diffs; descriptive commit messages (`<direction> <play> <node/task>: <log line>` for state, plain descriptive for os/).
- Do not delete files outside the scope of the job.

<!-- BEGIN: Codex multi-agent section — splice into repo-root AGENTS.md. Keep terse (32 KiB cap). -->

## Codex: how to work this OS

When running as **Codex** in this repo, you are a Direction-OS session/writer like any other coding agent. Four rules:

0. **Protocol lock comes before all Codex chatter.** For any Direction OS session input, the FIRST owner-facing line must be the `📍 ...` opening-contract header from `direction-os` — no skill-announcement, apology, summary, or "I'll read files" line may precede it. If a generic Codex skill rule asks you to announce the skill, the opening-contract header satisfies the announcement; any extra "using direction-os" note goes after the header. During an active leg, do not use the app's final answer as an ordinary progress answer: final = terminal RESULT/checkpoint only. If you cannot produce a RESULT yet, keep working in commentary or ask the required owner question.

1. **Follow the direction-os skill.** The job-recognition table and hard rules above are authoritative. For the full procedure load the `direction-os` skill (`.agents/skills/direction-os/SKILL.md`) — it points at `os/KERNEL.md`, the play, and `os/adapters/coding-agent.md` (the binding authority for the writer's validate-before-apply checks). Read state from `live/<id>/`; write state ONLY via a RESULT's `state_changes`.

   **Owner-verdict guard.** A CALL is permission to start the session, not permission to decide. If the CALL/play asks for an owner-readable verdict (`accepted/revised/rejected/split`, approve/reject, choose, "можно записывать", or similar), first present a normal human brief with options/recommendation and STOP for the owner's actual words. Do not emit a closing RESULT, clear the open_call, or open the downstream CALL until those words exist in the session and can be cited in `play_check`/evidence. Without the verdict, close only as a checkpoint that leaves the same open_call pending.

2. **Realize a play's parallel children as subagents — but only when the play calls for it.** A play that mandates in-leg fan-out (research nominal-group generators + miner + strategic_search; converge/converge-arch miners + strategic_search) is run by spawning the matching role worker once per child, then merging/deduping their reports yourself. The role text lives in `.codex/agents/*.toml` (`explorer`, `researcher`, `validator`; `builder` is for product repos only). **Codex spawns a subagent only when explicitly told to** — so fan out only where the play/CALL says to. **Known limitation:** on the desktop app / Windows, spawning a custom agent BY NAME may be unavailable (openai/codex #15250, #26828) — fall back to spawning the generic `explorer`/`worker` and injecting that role's `developer_instructions` as the prompt; see the `parallel-verify` skill. **Mechanical legs stay single-agent** (writer apply, a single `work` task, digest, audit): no subagents.

3. **Keep G5 as a fresh refutation session; cross-family is optional unless explicitly requested.** Gate G5 ("done" needs evidence) is verified by *trying to refute* a claim in a SEPARATE session from the one that did the work. A different model family can be requested for extra rigor on a specific CALL, but it is not the default hard gate. Codex subagents are still same-session helpers, so they may provide a pre-pass only; the binding G5 pass is a fresh session. State in your RESULT whether evidence came from an in-session pre-pass or from the binding fresh review. A CALL phrase like "no heavy multi-agent refutation" reduces fan-out only; it does **not** waive G5, writer validation, or the requirement to leave the `open_call` open until the close evidence exists.

Setup, replication, the by-name-spawn limitation, and version caveats: `.codex/README-CODEX-KIT.md`.

<!-- END: Codex multi-agent section -->

END_OF_FILE: AGENTS.md
