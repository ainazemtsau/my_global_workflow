# CALL c-exec-017 — S2a: ZERO-LEGACY RETIREMENT of the host-authoritative reconstruction spine

Direction: indie-game-development / g-9c41 / S2a. The FIRST half of the S2 split (owner «Split S2a+S2b» at the c-exec-016
PLAN, 2026-06-28). Runs FIRST — it produces the clean ZERO-LEGACY base S2b's load-bearing loopback proof builds on.
Executor: a FRESH GasCoopGame_dev session (branch `dev` → `main` when green, owner-gated). Opens with a PLAN (owner present).
State source = NOW.md (active_tasks S2a). Canon = knowledge/g9c41-gas-engine-SPEC.md (Факт-1 / Факт-5 / Факт-6 / §7 / §8).
Authored from the owner-signed c-exec-016 PLAN inventory (imported RESULT → history/c-exec-016-plan-split-2026-06-28.md;
the port-vs-delete sets below were produced + verified first-hand by the PLAN's 7-agent workflow `wf_89e9d3c2`).

## Why this leg (the split)

The c-exec-016 PLAN concluded SPLIT-NEEDED (per the CALL's own budget clause): S2 = a ZERO-LEGACY half (this leg) + a
load-bearing loopback half (S2b / c-exec-018). Reason: the migration-spine RETIREMENT (delete the pre-lockstep
host-authoritative reconstruction machinery, Факт-6) is a large, NO-new-behavior surgery that is cleanest run on its own
and BEFORE the load-bearing determinism proof — you do not want to elevate a loopback gate while legacy reconstruction code
still litters the tree. This leg adds ZERO new behavior; it only removes legacy + keeps the tree green.

## goal (outcome, not method)

The working tree is ZERO-LEGACY under input-lockstep (ADR-0010, Факт-6): the two pre-lockstep host-authoritative
reconstruction families are DELETED (incl. the Факт-5-buried late-join/snapshot path), the surviving store/reducer/far-tier/
input-bus infra is KEPT (with the lock-inverted «followers must not re-run» framing pruned), and every affected test is
REWRITTEN — not dragged. NO new behavior, NO new authoritative subtree. `-Deliver` stays GREEN throughout.

## context (read first — applied, not just cited)

1. **§Re-sync the GasCoopGame repo contract to its CURRENT version FIRST** (do not assume an earlier version — re-read).
2. **Base correction (verified at the PLAN, re-verify first-hand):** the build base = `main` @eed321b, NOT stale `dev`
   (`dev` was ~22 behind; `dev ⊆ main`). The visual track (c-visual-001 S1–S3) touched ZERO `Core/**`, so engine Core on
   `main` == `dev`. **Housekeeping FIRST (owner-approved, done_when 0):** fast-forward `dev` up to `main` @eed321b
   (`dev ⊆ main` → clean `--ff-only`) BEFORE any new `dev` commit, then archive the `c-exec-014` / `c-exec-015` openspec
   change folders (this removes the `-Deliver` re-scan coupling so the gate does not re-scan retired frozen folders).
3. **Canon (mandatory, applied):** Факт-6 (ZERO-LEGACY on finish — no unused/legacy code; rollback via git history only;
   tests rewritten, not dragged) + Факт-5 (NO late-join → no full-snapshot obligation; base↔raid = clean session boundary)
   + §7 «ПОХОРОНЕНО» (host-broadcast / single-writer / «клиенты реконструируют» / chunked-delta → replaced by input-lockstep)
   + §8 (keep-as-far-tier 2-band note; the `CoarseChunkFollower`/follower-parity warning relevant to S2b, not this leg).

## the retirement inventory (owner-signed at the c-exec-016 PLAN; RE-VERIFY first-hand at the tip before deleting)

**DELETE — chunked-delta family (test-only consumers, §7-buried):** `CoarseChunkFollower`, `ICoarseChunkLink`,
`LoopbackCoarseChunkHub`, `FishNetChunkChannel` (+ `ChunkBatchBroadcast`), `ChunkEncoder`, `ChunkDecoder`,
`Chunk` / `ChunkBatch` / `ChunkCodecParams` / `ResolutionKey`, `RevisionBarrier`.

**DELETE — field-state-channel family (asymmetric host-PUBLISHES / followers-CONSUME):** `IFieldStateChannel`,
`InMemoryFieldStateChannel`, `FishNetFieldStateChannel` (+ `FieldStateBroadcasts`), `FieldSnapshot` (the Факт-5 late-join
path), `FieldDelta`, `FieldStreamDriver` (+ `DesyncException`), `FieldHost`, `FieldHostFactory`.

**KEEP — survives lockstep / live infra (do NOT delete):**
- `FieldState` / `ZoneRecord` / `FieldStep` — the store + reducer, reused by Layers. **DROP** the «followers must not
  re-run» framing + the `Follower_OnlyMutatesViaApply` guard (ADR-0010 INVERTS it — under input-lockstep every peer
  re-runs); **prune** the snapshot/delta-only mutators left orphaned by the deletes.
- `CellHash` — shared by the surviving `CoarseBandStore.Hash()`.
- the **2-band far-tier** (keep-as-far-tier, §8) — it retires at **S4** room-rollup, NOT here.
- `RevisionFeed` / `IGridEventBus` — the LIVE layer event bus (this is NOT `RevisionBarrier`; do not delete it).
- `FishNetTickInputBus` / `TickInputBroadcasts` — the surviving input-lockstep wire.

**OUT-OF-SCOPE — leave untouched:** `Core/Sim/*` (the ADR-0002 8×8 int-grid risk-spike toy; 4 live consumers + an accepted
ADR; retiring it is a SEPARATE owner/ADR decision, not this leg).

**§7-burial re-check (must hold after the delete):** nothing anchors `BandCount=2` as an authoritative collapse target —
the only such coupling was `CoarseChunkFollower.SectorMass`, itself in the delete set.

## tests — REWRITTEN, not dragged (Факт-6)

~25 reconstruction / chunk / field-stream suites are rewritten or deleted (not dragged). Specific moves verified at the PLAN:
- `EncapsulationGuardTests` — WireDtos whitelist updated to drop the deleted DTOs.
- `LayerRegistryTests` — its oracle re-anchored on `FieldStep` (was on a deleted type).
- The **DW9 input-bus coexistence assertion** — EXTRACTED into a surviving test BEFORE its host file is deleted (do not lose it).
- Surviving-invariant RED criteria that MUST stay green (the change could falsify them → they are the regression guard):
  F11 `c-014` determinism harness; Layers survive the channel delete; `CoarseBandStore.Hash()` determinism (CellHash kept);
  input-bus coexistence preserved.

## boundaries (out of scope / STOP-escalate if tempted)

- **NO new behavior, NO new feature, NO new authoritative subtree** — this is a deletion + keep-prune + test-rewrite leg
  only. (So no change to the zero-float / int-overflow scan roots is needed — if you find one is needed, STOP: that means
  you added authoritative code, which is out of S2a scope.)
- **NO loopback load-bearing work** — the 2-endpoint hash over the full forced-flow scenario + RED controls + Adapters
  3-mode owner-eye is **S2b (c-exec-018)**, on this leg's clean base. Do not pull it forward.
- **Do NOT delete a KEEP-set member**; do NOT retire the 2-band far-tier (S4) or `Core/Sim` (separate ADR). If a KEEP-set
  member turns out to have a surviving consumer that breaks, or a delete needs a behavior change to stay green = **STOP +
  escalate** (do not silently substitute or expand scope).
- Laws stay in headless `Core/**`; `Adapters/**` unchanged except where a deleted family had an adapter (delete it too).
  ADR-0010 input-lockstep, gas-50, R5, R12/R13/R14 unchanged.

## done_when (verifiable)

0. **HOUSEKEEPING FIRST:** `dev` fast-forwarded up to `main` @eed321b (`dev ⊆ main`, clean `--ff-only`, before any new dev
   commit) + `c-exec-014` / `c-exec-015` openspec folders archived.
1. **DELETE both families** (chunked-delta + field-state-channel, incl. the Факт-5 `FieldSnapshot` late-join path) — the
   exact sets above, RE-VERIFIED first-hand at the tip (no surviving non-test consumer for any deleted symbol; a grep proves
   it).
2. **KEEP set intact + pruned**: `FieldState`/`ZoneRecord`/`FieldStep` survive with the «must-not-re-run» framing +
   `Follower_OnlyMutatesViaApply` guard removed and orphaned snapshot/delta mutators pruned; `CellHash`, 2-band far-tier,
   `RevisionFeed`/`IGridEventBus`, `FishNetTickInputBus`/`TickInputBroadcasts` untouched-and-green.
3. **TESTS rewritten not dragged**: the ~25 suites rewritten/deleted; the EncapsulationGuard whitelist, LayerRegistry
   oracle, and the extracted DW9 coexistence assertion handled as above; the 4 surviving-invariant RED criteria green.
4. **§7-burial re-check passes** (no `BandCount=2`-as-authoritative-collapse-target coupling remains).
5. **check.ps1 -Deliver GREEN** (build + headless + zero-float scan + int-overflow scan + mutation ≥70 on any touched Core +
   spec-silence + coverage). No scan-root change (no new authoritative subtree).
6. **ZERO-LEGACY 3-lens re-audit CLEAN** (grep for the deleted symbols = 0 non-test/non-history hits; no orphaned files; no
   dead references). Rollback only via git history.
7. **OWNER-EYE (confidence, NOT a gate):** owner sees the suite green on the retired tree (no behavior changed). dev→main
   merge + push owner-gated.

## discipline / gates (carried from S0/S1)

RED-first by an INDEPENDENT test-author for any surviving-invariant guard (builder cannot edit the red tests) · Core/**
placement · -Deliver GREEN · mutation ≥ floor (70%) · a FRESH-SESSION G5 (different model family) that tries to REFUTE the
delete/keep boundary + tests-rewritten-not-dragged + the §7-burial re-check — COULD-NOT-REFUTE is the bar · STOP-discipline
(a KEEP-member that breaks, a delete needing a behavior change, a temptation to expand into S2b's loopback work, or any
need to reopen ADR-0010 = mandatory STOP + escalate).

## return

A RESULT routed HOME (the OS owns the next CALL): outcome + evidence (commits, the FF + archive, the delete/keep grep
proofs, -Deliver transcript, mutation json, G5 verdict, the ZERO-LEGACY 3-lens re-audit) + any findings for the planner.
dev→main merge + push is OWNER-GATED. On GREEN → the direction authors + hardens S2b (c-exec-018, the load-bearing loopback)
on this clean base.

## budget

One leg (deletion + keep-prune + test-rewrite). It should NOT split further — if the inventory turns out materially wrong
at the tip (a "delete" has a live consumer, or a "keep" is actually dead), STOP and return the correction rather than
improvising. Do not pull S2b loopback work forward to "save a trip".

END_OF_FILE: live/indie-game-development/work/c-exec-017-call.md
