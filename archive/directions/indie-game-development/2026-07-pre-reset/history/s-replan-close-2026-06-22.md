# RESULT — s-replan-close (g-9c41, map) — 2026-06-22

```
RESULT
play: map
direction: indie-game-development
node: g-9c41
session: s-replan-close-2026-06-22

outcome: |
  The 2026-06-21/22 re-plan MARATHON is CLOSED. The дорога-A+ road is concretized into a LOCKED, reconciled architecture +
  a SLICE METHODOLOGY, owner-approved («да»). g-9c41 is re-shaped from "build the core → then promo" into a spine of small,
  visible, deterministic gas-GAMEPLAY slices; the active bet is now S0 (foundation slice). Per-mechanic depth is decided at
  EACH slice's PLAN (default room-granular). All decisions are preserved durably (5 work/ docs + 1 knowledge entry + the
  decision_inbox); a single entry point (work/dev-plan-graph-2026-06-22.md) lets a FRESH session execute with clean context.
  NO build this session (paper). The reusable-engine goal is dropped; netcode is input-lockstep; the gas model is one integer
  cell model (grid+face-flow near / room-graph-rollup far / room=LABEL everywhere); detail is a LOCAL non-authoritative
  refinement of a coarse-authoritative truth (so each peer computes ~1 bubble, not N); late-join is out; zero-legacy at
  completion is a hard requirement.

evidence:
  - 4 verification workflows over the session: wf_1a13feb0-a5f (impact analysis + adversarial re-plan: tree-vs-waves,
    survives-D1, leg sequencing — 7 agents); wf_0e379688-a88 (grid-vs-graph for the detailed tier — 6 agents, web prior-art
    incl. SS13 ZAS→LINDA, Berger-Colella AMR refluxing); wf_fff6ce9a-058 (detail authority/cost model: own-bubble-only +
    wash-out condition + event-promotion + grid/graph reconciliation — 6 agents). Each synthesized + adversarially critiqued.
  - Durable spec products: work/{gas-model-architecture-decision-2026-06-21, aplus-replan-under-locked-arch-v1,
    grid-vs-graph-resolution-2026-06-22, detail-authority-cost-model-2026-06-22, dev-plan-graph-2026-06-22}.md.
  - Owner co-creation across the session: confirmed input-lockstep cheaper-model intuition; raised + resolved grid-vs-graph
    (room=LABEL not PIPE near); raised + resolved "8 bubbles?" (no — own-bubble-only); firm decisions: NO late-join,
    ZERO-legacy; chose the slice methodology + "decide each mechanic at build time" (which also resolves the A/B depth fork:
    default A, classify per slice). Final «да» to closing the marathon into the slice methodology + S0.

state_changes:
  - TREE.md g-9c41: ADDED done_when #12 (дорога A+ architecture LOCKED + slice methodology; G9, owner «да»); ANNOTATED #2
    (networking clause SUPERSEDED by #12 / ADR-0010 — input-lockstep) + #9 (bandwidth-budget basis SUPERSEDED — binding limit =
    weakest-peer CPU).
  - NOW.md: active_bet.phase prepended with the 2026-06-22 close block; approach + done_when prepended with SUPERSEDED→slice
    redirects (historical text kept); wave_plan REPLACED with the SLICE SPINE (S0…S6+ + parallel tracks + pointer to
    dev-plan-graph); active_tasks REPLACED t-1/t-2/t-3 → S0 (foundation slice; t-2 folds into the slice gate, t-3 MOOT under
    no-late-join); decision_inbox ADDED d-arch-lock-slices-001 (answered); next REPLACED with the S0 CALL.
  - knowledge/g9c41-architecture-locked-slices.md CREATED (accepted facts + methodology; read by every g-9c41 slice PLAN).
  - work/dev-plan-graph-2026-06-22.md CREATED (single entry point: slice graph + deps + per-slice ritual + 3-bucket rule +
    decision index + hard rules).
  - LOG.md appended.

captures:
  - ADR-0010 is owed in the GAME repo (GasCoopGame): records input-lockstep superseding ADR-0004/0005 authority + the detail
    re-classification (coarse-authoritative, detail-derived-discarded-off-checksum) + the snapshot/late-join repurposing of the
    chunk codec + the §9.8 (byte)c guard fix. Authorized by this G9 close; written at S0/S2 time, never silently.
  - Per-slice mechanic classification (ведро-1/2/3) for the owner's named expressive mechanics (walk-splits-cloud, blow-to-split,
    persistent-split, directional-blow, displacement) happens at each slice's PLAN — first-pass classification in
    work/detail-authority-cost-model-2026-06-22.md §4 / dev-plan-graph §3.
  - D5 held-room return: remember cloud SHAPE (sparse fine-shadow, memory cost) vs only the room TOTAL — an owner feel decision
    deferred to the relevant slice (S4).
  - Anti-cheat residual: detail off-checksum allows gas-ESP for a modified client; acceptable for trusted-friend co-op, recorded.
  - HOME-CLEANUPS still owed (pre-existing): d-grid-sgf-001 R1 re-spec; stale ADR-0005/0007 "separate-layer=t-3" wording;
    FishNet real-UDP owner-run residual. (Carried, not this session.)
  - The owner will brief the MARKETING track (g-2f8c) with the new methodology in a separate session (devlog posts ride the
    visible slices).
  - aplus-breakdown-v1 / aplus-wave-map-v1 are now pre-lockstep history (their §4.2 RISK-register + §2 keep-open still serve as
    a PLAN check-list).

decisions_needed: []   # the open per-slice forks (mechanic-bucket, D5-shape-vs-total) are resolved at each slice's PLAN, not batched here

play_check:
  - Recite (owner): done — restated mission + g-9c41 + the locked architecture (owner present throughout).
  - Candidates & evidence (owner): done — evidence = the architecture decision doc + 4 in-session verification workflows; owner
    brought the key candidates (lockstep-cheaper, grid-not-graph-near, no-8-bubbles, slice methodology).
  - Skeleton (owner): done — the tree change is a contained node-content revision (g-9c41), not new nodes; presented + owner «да».
  - Cards / per-node verdict (owner): done — g-9c41 #12 presented; owner approved («да»). No other node changed.
  - Order (owner): done — slice spine ordered effect × foundation-dependency; owner approved the methodology.
  - Depth check / lens sweep: top-level only; tree structure intact (all 6 children keep their place); no lens uncovered (the
    methodology strengthens commercial/traction — devlog turns on per visible slice — and core-gameplay-depth via owner-eye per
    slice).
  - Close (owner): done — owner «да» to closing the marathon into the slice methodology + S0; full state applied; next ready.

log: "s-replan-close g-9c41 (map): marathon re-plan CLOSED → architecture LOCKED (input-lockstep; grid-near/graph-far; detail=local-refinement; no-late-join; zero-legacy) + SLICE methodology; TREE g-9c41 #12 (G9); bet → S0; entry = work/dev-plan-graph-2026-06-22.md"

next: |
  S0 CALL (foundation slice: voxelizer + face-flow + sandbox + FEEL grey-box) — in NOW.next. RUN IN A FRESH SESSION (context
  hygiene); the S0 PLAN ingests-and-applies work/dev-plan-graph-2026-06-22.md + the 4 decision docs. Build = an executor leg in
  GasCoopGame, opening with a PLAN (owner present).
```

END_OF_FILE: live/indie-game-development/history/s-replan-close-2026-06-22.md
