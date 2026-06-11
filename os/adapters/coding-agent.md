# Adapter: coding / working agents (Claude Code, Codex, Gemini CLI, ...)

Two distinct roles run on agentic tools. Any vendor works; switching vendors changes nothing outside this file.

## Role 1: writer (kind: mechanical)

Applies a RESULT's `state_changes` to `live/**` and commits.

Contract:
- Input: a RESULT packet (or its state_changes section).
- Apply edits exactly as written; append the log line to LOG.md; save the full RESULT to `history/<date>-<session-id>.md`; commit with a descriptive message (`<direction> <play> <node/task>: <log line>`).
- Maintain the `END_OF_FILE: <path>` trailer on every state file it writes (truncation guard, schema/direction-files.md).
- No judgment: if a state_change is ambiguous or conflicts with current files, do NOT improvise — reply with the conflict (this routes to repair).
- Also emits the `next` CALL back to the owner/orchestrator if one is present.
- Record CALLs issued in state_changes into `NOW.md → open_calls`; clear an entry when its RESULT arrives.
- `collect` command: on "collect next for <direction>" (or a CALL id), emit ONE paste-ready block for chat platforms: the play file, then NOW.md, then the CALL last (context first, CALL last). This replaces the owner assembling three sources by hand on platforms without a reliable connector.

**The writer is ephemeral — never a standing chat.** Every RESULT is self-contained, so the writer needs no memory; a long-lived writer session is accumulated noise and cost (one chat = one job applies to the writer too). Manual loop: open a fresh agent session → paste the RESULT → it applies, commits, hands back the next CALL → close it. Headless one-shot invocations (`claude -p` / `codex exec`) do the same without a chat at all; an orchestrator replaces the hop entirely at autonomy stage 2+.

**Concurrency.** Parallel directions: one git worktree per direction, writers of different directions run in parallel; within one direction RESULTs apply one at a time. Sync/push protocol and rules: `os/adapters/worktrees.md`.

## Role 2: executor (kind: engineering)

Receives a business task CALL targeting a product repo (`repo:` field). The full engineering process — plan gate, autonomous build, validation gates, retry/escalation, final report — is defined in `os/engineering/CONTOUR.md`; repo bootstrap in `os/engineering/PROJECT_SETUP.md`. The contract summary:

Contract:
- The CALL gives goal / context / boundaries / done_when / return / budget. The agent owns everything else: design, implementation, refactoring, branch/PR mechanics.
- Repo-internal conventions (build, test, style, architecture rules) live in that repo's AGENTS.md / CLAUDE.md — command-first, written once per repo. The OS never duplicates them.
- Exit report (= the RESULT's evidence): descriptive commits or PR link, diff summary, output of the checks run (tests/build), explicit list of assumptions made, anything cut for budget.
- "Done" is the CALL's done_when verified by a runnable check, not the agent's assertion. A task that can't carry a runnable check should say how it is to be verified instead — at CALL time, not after.
- Blockers surface early: if the task looks infeasible or 2x over budget, stop and report — a fast "blocked, because" is a good result; days of silent struggle are not.

## Sizing rule

One executor CALL ≤ a focused half-day of human-equivalent work. Bigger means the task needed splitting at shape time — send it back as such.

## Running thinking sessions here too

Any OS play can run in an agentic CLI session instead of a chat app: the agent reads `os/KERNEL.md`, the play file, and `live/<dir>/NOW.md` itself, and can act as its own writer for state changes (one relay hop instead of two, or zero with an orchestrator). Recommended default for shape / review / pulse / repair, which are state-heavy; chat apps stay attractive for frame and long work dialogs.

END_OF_FILE: os/adapters/coding-agent.md
