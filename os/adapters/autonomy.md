# Adapter: autonomy roadmap

The OS is designed so growing autonomy changes the relay, never the packets, plays, or state. Three stages; the owner moves between them per direction, not all-or-nothing. Runtime details live in `os/adapters/runtime.md`.

## Action tiers (fixed across all stages)

- **Tier 0 — state writes** (`live/**` edits, log, history): never need owner approval. The writer applies them; git history is the undo.
- **Tier 1 — direction artifacts** (work/ documents, code in product repos via PR): proceed without asking; owner sees them in review/PR form. Reversible.
- **Tier 2 — external & irreversible** (publishing, sending to people, spending money, deleting non-versioned things): always an owner decision, before the act. No stage of autonomy ever auto-approves tier 2.

The tier — not the agent's judgment — decides whether the owner is interrupted.

## Stage 1: manual relay

For v29/legacy work, the owner carries a Direction CALL to the executor, then carries each current-stage HOME to a fresh Direction session/writer; that session emits the successor CALL. For a v30/v31 engineering root the owner carries the root once: its repo runner launches the separate fresh stages and returns only REPORT or ESCALATE HOME. If that runner cannot launch truly separate sessions, the root stops before work instead of collapsing roles or reviving owner stage relays. Decision inbox = `NOW.md → decisions`, surfaced by sessions and by pulse.

## Stage 2: runtime-assisted relay

A local runtime, scheduled job, or short-lived headless agent on this repo:
- applies RESULTs through the writer contract as they arrive (owner pastes once, not twice);
- runs digest/audit/pulse on schedule, producing consolidated decision batches;
- prepares every ready CALL grouped by track; the owner can open one or several without assembling packets;
- may trigger fresh review of executor evidence before writer apply.
Owner's manual work shrinks to: choose a ready CALL card grouped by track, open its chat, answer batched decisions.

## Stage 3: orchestrator

A loop (cron + agentic CLI, or a small service) that:
- claims owner- or policy-selected ready calls and runs separate API/CLI sessions without overlapping product writes; several calls with no explicit policy require a choice;
- chains v29/legacy RESULT → writer → issued CALL, and v30/v31 product-stage receipts inside one root, without human hops;
- pushes only two kinds of notification to the owner: a tier-2 decision batch, and pulse digests. Four response verbs: approve / edit / reject-with-reason / answer.
- hard caps: ≤N interrupts/day (default 3 batches); any run exceeding its CALL budget stops and surfaces as blocked, never silently retries.

## Honesty instrument

At every stage, pulse tracks two numbers per week: owner-minutes spent on the system (decisions + relays) and bets closed. If the first grows while the second doesn't, the OS is failing regardless of how it feels — log it as friction.

END_OF_FILE: os/adapters/autonomy.md
