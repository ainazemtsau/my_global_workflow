# CALL c-exec-025 — W1b: per-cell dominant-type read-API (ENGINE mini-CALL, byte-identical, GasCoopGame_dev)

> Opens after: c-exec-024 DONE — Sc-kernel ledger FULLY CLOSED, binding fresh-session G5 SOUND (s-work-041,
> 2026-07-03). The Sc-kernel→Sc-reactions GAP's remaining engine item before c-exec-021 (Sc-reactions) fires.
> Base = GasCoopGame main @38ab715 (Sc-kernel + c-exec-024 cleanup + the contract fact-check ADR-P-0003 all
> merged/pushed). Fires in a FRESH GasCoopGame_dev session/worktree — NEVER dev_2 (dev_2 is the visual render
> worktree; this is a Core/Field engine edit). Windowed here per d-w1b-window-001 (owner-answered 2026-07-02): the
> visual track's per-cell dominant-type read is a Core/Field edit that cannot ride a render-only leg, so it fires
> as its own tiny engine mini-CALL in the gap. dev→main merge + push OWNER-GATED.

Direction: indie-game-development / g-9c41 (engine) serving g-7e15 (visual Stage 2 consumer).

## goal (outcome, not method)

The near gas field exposes a read-only, encapsulation-safe accessor for the per-cell DOMINANT type — the per-cell
dominant-type STAMP that Sc-rep already lays — so a downstream consumer (the visual track's Stage 2 «Паспорт типа»,
and later reactions/typing reads) can query «what type dominates this cell» WITHOUT reaching into mutable field
internals and WITHOUT any change to tick behavior.

## context

- Sc-rep (c-exec-022, merged) laid a per-cell dominant-type STAMP on the sparse-dominant near field
  (SparseDominantNearGasField) — «the socket env-derived typing/waves/reactions key off». W1b is the READ seam over
  that EXISTING stamp; it does NOT invent new stamp semantics.
- d-w1b-window-001 (NOW.decisions): W1b fires as its own engine mini-CALL in the Sc-kernel→Sc-reactions gap,
  GasCoopGame_dev worktree, before c-exec-021; c-exec-021 rebases over it via its own §Re-sync.
- Repo conventions/gates: GasCoopGame AGENTS.md (contract v11 + ADR-P-0003; run contour + tools/check.ps1 -Deliver).

## boundaries / STOP

- ENGINE-ONLY, GasCoopGame_dev worktree — NEVER dev_2, NEVER Assets/GasCoopGame/Adapters or /Net (no render/particle
  code — Stage 2 consumes this seam in dev_2 later; this leg exposes only the engine-side read).
- READ-ONLY accessor: NO tick/behavior change → byte-identity MUST hold (single-type + determinism goldens
  byte-identical to the post-c-exec-024 baseline; ADR-0002 determinism preserved). If exposing the read forces any
  mutable-internals leak or a behavior change — STOP and surface.
- Consume the EXISTING Sc-rep dominant stamp; do NOT add typing/reactions/waves/damage semantics (those are
  c-exec-021 / Sc-typing / Sc-damage). No golden rebaseline.
- §Re-sync to the current os/engineering contract at fire time before building (the repo is at v11 + ADR-P-0003;
  confirm nothing newer is owed).

## done_when

1. A read-only accessor on the near field returns the per-cell DOMINANT TypeId (the Sc-rep stamp) for a queried
   cell, with a well-defined sentinel for an empty / no-dominant cell; encapsulation-safe (no mutable-internals
   handle escapes to the caller).
2. Independent-author RED test FIRST (separate earlier commit), then build-to-green: the accessor returns the
   correct dominant type for representative cells — single-type cell, multi-type cell (dominant = max-mass, tie =
   lowest TypeId per the Sc-rep stamp rule), and empty cell (sentinel) — matching the stamp the tick already lays.
3. Byte-identity: single-type no-regression + determinism goldens byte-identical to the post-c-exec-024 baseline;
   the tick-kernel files unchanged (a read accessor adds no write path).
4. tools/check.ps1 -Deliver GREEN (full battery: deliverable-coverage by done_when; review-evidence if a
   frozen/openspec change is opened; negative-control; mutation ≥70). Fresh-session G5 + owner-eye per the contour
   for a frozen change.
5. §Re-sync stamped (synced_contract_version = current) if the repo was behind at fire.

## return

RESULT routed HOME: commits, -Deliver transcript, the accessor + its RED-first tests, byte-identity evidence
(goldens unchanged / tick files untouched), §Re-sync note. dev→main merge + push OWNER-GATED. On GREEN → the
Sc-kernel→Sc-reactions gap is CLEAR; next = re-harden c-exec-021 (§Re-sync + full fire-time re-hardening, fill
§PENDING from the Sc-kernel RESULT) and fire Sc-reactions in a fresh GasCoopGame_dev session (owner-present PLAN).

## budget

One small slice (a read accessor + RED-first tests + byte-identity proof). If exposing the stamp read turns out to
need a real field-layout change (not a pure accessor), STOP — that is a bigger leg needing its own shape.

END_OF_FILE: live/indie-game-development/work/c-exec-025-w1b-call.md
