# RESULT — s-research-011 (gas-model A+ architecture, co-creation)

direction: indie-game-development
play: research
node: g-9c41
date: 2026-06-21
session: s-research-011

## summary

Deepened the already-ratified дорога A+ (d-gasmodel-redesign-001) into a concrete, owner-approved,
deterministic gas-model ARCHITECTURE via co-creation + 4 workflow runs (wf_a105d2b4 / wf_12c909a7 /
wf_7d44a7dd / wf_a04144c9). Full durable spec authored + committed:
work/gas-model-architecture-decision-2026-06-21.md (commit 3aa0f57, local/unpushed).

Core architecture (owner-confirmed D1–D13): NETCODE = input-lockstep (only inputs on the wire; gas
complexity never touches the net; per-machine CPU is the only limit; free host-migration). MODEL =
ONE integer cellular gas + an integer CHEMISTRY collision table, at LOD-BY-CELL-SIZE (near = full 3D
fine; mid = 2.5D/coarse spatial; far = 1-cell-per-room "bucket"). Big/important rooms stay
authoritative+spatial (HOLD state on return, no "jump"); only small/distant rooms collapse to a
bucket. SPARSE dominant-gas-per-cell (+transient mix on reaction) — NOT dense per-species planes.
ALL mechanics work at every tier with precision degrading by distance (mechanic×tier proof in the
doc). Loot dose = "gas actually reached it" (near/mid), %+delay only very far. Reactions everywhere
(telegraph+window near; room-level far; precise far-location deferred to graph-fronts). Real height =
via 3D near (not 2-band-everywhere). Cut: corridor-carve-by-hand (D13), reusable-engine-as-goal (D12),
pure-A1-uniform-voxels, A3-analytic, dense-pages-per-gas, smooth-blob-as-authority, host-broadcast netcode.

## play_check

- read state + code + prior docs (gas-model-design-full, aplus-wave-map/breakdown); verified ground truth in code (orifice no-area, BandCount=2 const, CellHash value-only + ChunkEncoder byte bug, SimCore lockstep exists, breach pre-declared).
- ran 4 adversarial/research workflows (3-approach study; hybrid depth-attack; deep web research+composite; cloud-math+optimizations); extracted + verified load-bearing claims first-hand.
- co-creation with owner: presented options, sparred, owner ratified D1–D13.
- authored durable spec work/gas-model-architecture-decision-2026-06-21.md (committed 3aa0f57); NO build (paper design per session framing).

## state_changes (applied by writer 2026-06-21)

- work/gas-model-architecture-decision-2026-06-21.md — AUTHORED + COMMITTED (3aa0f57, local/unpushed). Comprehensive architecture spec — owner decisions D1–D13, requirements ontology R1–R20, mechanic×tier proof, rejected/cut, deferred optimizations+triggers, seams-to-reserve-now, signed depth-properties P1–P10, risk-first de-risk plan. (Already on disk — not re-created.)
- NOW.md — APPENDED to decision_inbox d-gasmodel-redesign-001 the "ARCHITECTURE DEEPENED (2026-06-21, s-research-011)" dated block (D1–D13 summary + planner-reconcile note + LOCK-touching flag).
- LOG.md — APPENDED the s-research-011 line.
- history/s-research-011.md — THIS file.

## next

CALL — PLANNER: reconcile the A+ wave plan with the LOCKED architecture, then shape the first gas-model leg.

- goal: a wave/leg plan that integrates the locked architecture — net = input-lockstep (a change from the
  host-broadcast LOCK assumption, reconcile the replication/LOCK framing), model = cell-size LOD with
  near-3D + chemistry table + sparse-dominant + the §9 seams reserved from day one. Decide how the current
  active bet (Wave A t-1 generator-blind reader/sandbox — still needed to read levels into the sim) fits,
  what is superseded, and the sequencing. (Owner expects possibly re-planning all waves / the tree.)
- context: read work/gas-model-architecture-decision-2026-06-21.md (§8 deferred-with-triggers, §9 seams-now,
  §11 de-risk, §12 recommended rough sequencing, §13 open items). Recommended FIRST executor leg =
  a grey-box FEEL prototype near-in-3D (make-or-break "is it fun" owner-eye; can't be unit-tested) +
  spikes-before-faith (per-half-day 2-machine bit-identical proofs of active-front / segment-merge /
  wake before committing them). Owner: planner decides timing.
- boundaries: this was a PAPER design session — no build done. Do NOT silently re-open the LOCK without an ADR;
  the netcode shift (D1) + cell-size LOD (D2) are real LOCK-touching changes needing their own ADR.
- return: a shaped wave/leg plan (or the next CALL) for the gas-model architecture build.

END_OF_FILE: live/indie-game-development/history/s-research-011.md
