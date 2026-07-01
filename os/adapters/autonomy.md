# Adapter: autonomy roadmap

The OS is designed so growing autonomy changes the relay, never the packets, plays, or state. Three stages; the owner moves between them per direction, not all-or-nothing. Runtime details live in `os/adapters/runtime.md`.

## Action tiers (fixed across all stages)

- **Tier 0 — state writes** (`live/**` edits, log, history): never need owner approval. The writer applies them; git history is the undo.
- **Tier 1 — direction artifacts** (work/ documents, code in product repos via PR): proceed without asking; owner sees them in review/PR form. Reversible.
- **Tier 2 — external & irreversible** (publishing, sending to people, spending money, deleting non-versioned things): always an owner decision, before the act. No stage of autonomy ever auto-approves tier 2.

The tier — not the agent's judgment — decides whether the owner is interrupted.

## Stage 1: manual relay (now)

Owner carries CALL/RESULT between chat sessions and the writer. Decision inbox = `NOW.md → decisions`, surfaced by sessions and by pulse.

## Stage 2: runtime-assisted relay

A local runtime, scheduled job, or short-lived headless agent on this repo:
- applies RESULTs through the writer contract as they arrive (owner pastes once, not twice);
- runs digest/audit/pulse on schedule, producing consolidated decision batches;
- prepares the next CALL ready-to-paste;
- may trigger fresh review of executor evidence before writer apply.
Owner's manual work shrinks to: open next chat, paste one CALL, answer batched decisions.

## Stage 3: orchestrator

A loop (cron + agentic CLI, or a small service) that:
- picks `NOW.md → next` and runs the session itself via an API/CLI model call;
- chains RESULT → writer → next CALL without human hops;
- pushes only two kinds of notification to the owner: a tier-2 decision batch, and pulse digests. Four response verbs: approve / edit / reject-with-reason / answer.
- hard caps: ≤N interrupts/day (default 3 batches); any run exceeding its CALL budget stops and surfaces as blocked, never silently retries.

## Honesty instrument

At every stage, pulse tracks two numbers per week: owner-minutes spent on the system (decisions + relays) and bets closed. If the first grows while the second doesn't, the OS is failing regardless of how it feels — log it as friction.

END_OF_FILE: os/adapters/autonomy.md
