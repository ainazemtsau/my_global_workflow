# Knowledge — g-9c41 Wave 1 closed 3 internal legs with ZERO player-facing artifact; pre-mortem #2 is now live, the clip-terminus is orphaned

Established: 2026-06-16, review c-review-001 (commercial + audience lens harvest).

- t-1, t-2, t-3 all terminated in **internal artifacts** (ADRs, telemetry JSON, dotnet 103/103) on a **toy
  scene** (16 gas + 16 temp cells, ~75× under the real 275 KB/s clamp, loopback only). No artifact an outsider
  can see or want was produced — by design.
- The **spectacular-clip milestone** that used to force a player-facing terminus was deleted from the spine
  (s-shape-004) and reassigned to parked **g-7e15** with **no replacement**. That also **orphaned the sole
  trigger** that g-e6f2 (audience) and g-5b07 (Steam page) fire on (root TREE map_order still references it).
- Against the **fixed commercial calendar** — Steam page + Next Fest registration by **2026-08-31**, decision
  gate **2026-10-05**, money gate **2026-12-11** — **pre-mortem #2 (private engineering tunnel) has moved from
  hypothetical to LIVE**, and Wave 2 is also internal.
- **Consequence:** any next g-9c41 wave should carry a **player-facing termination clause** (an artifact a
  human reads without a debug overlay). The orphaned clip-gate trigger + a possible "first player-legible
  artifact" node are routed to map session **c-map-003**.

read_by: |
  the shape / converge play when shaping the next g-9c41 wave (the player-facing-terminus requirement); the
  commercial/traction and audience-workflow lenses at every harvest until a legible artifact exists; map
  session c-map-003 (resolve the orphaned clip trigger).

related: [[project-gascoopgame-product-repo]]

END_OF_FILE: live/indie-game-development/knowledge/g9c41-wave1-no-player-facing-premortem2-live.md
