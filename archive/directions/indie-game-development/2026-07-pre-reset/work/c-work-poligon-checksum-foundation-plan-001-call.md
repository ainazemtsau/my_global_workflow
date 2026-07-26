# CALL c-work-poligon-checksum-foundation-plan-001 — checksum foundation PLAN route

to: session
direction: indie-game-development
play: work
node: g-9c41
task: M1-A0
goal: |
  Для checksum foundation существует один authoritative self-contained PLAN-only executor CALL,
  готовый к owner-present product planning и к будущему fresh BUILD после Phase 0.
context: |
  Read live/indie-game-development/NOW.md and
  history/2026-07-10-s-repair-poligon-a0-checksum-route-001.md.
  Returned frozen A0 evidence: work/c-exec-poligon-a0-001-build-call.md;
  C:\projects\Unity\GasCoopGame_core\docs\results\c-exec-poligon-a0-001.md;
  C:\projects\Unity\GasCoopGame_core\docs\measurements\overlap-c-exec-poligon-a0-001.md;
  checkpoint 0d2a8ae7084434f46a795efbd913d4c784ed17f3. Old A0 is STOP/NOT DELIVERED.

  Owner sequencing verdict: «Я согласен с твоими рекомендациями. Сейчас давай, я так понимаю,
  что мы сначала должны реализовать вот этот новый сервис по чек-сумме и потом продолжить работу
  над нашей задачей текущей.» This approves ordering, not a frozen product spec.

  Accepted planning contour:
  1. Legacy MeaningChecksum remains the exact slow audit/golden/debug oracle.
  2. Separate StateRevision serves render/snapshot dirty detection and is not called a checksum.
  3. Legacy full checksum leaves automatic per-frame/per-sense polling.
  4. Before live gas networking/S4, plan a versioned incremental synchronization digest:
     session-static digest + transactionally maintained dynamic root; ordinary root read O(1);
     no full-domain scan on a sparse ordinary step.
  5. Fast A0 activity snapshot does not call the legacy global checksum; exact legacy hash, if exposed,
     is a separate explicitly slow API.
  6. Do not turn sequential FNV into a supposedly identical incremental hash; the new digest lives beside
     it and old golden hashes remain unchanged.

  Performance evidence: docs/measurements/c-exec-023-kernel-scaling-matrix.json in GasCoopGame_core
  records 196,608 cells, Step 0.4045 ms and MeaningChecksum 28.2085 ms on strong CoreCLR; historical and
  optimistic, not a current guarantee. RealGasViewSource polls the legacy checksum each enabled Unity frame;
  PlayerSense folds it into each observation; current Net/FishNet has no checksum transport/compare path.
boundaries: |
  This Direction session authors only the PLAN-only executor CALL. It does not design/freeze the product PLAN,
  author RED tests, create a BUILD CALL, edit product code, or claim delivery. The product Planner owns detailed
  architecture and must return an owner-readable plan for actual owner approval.
  Do not edit or reopen the old frozen PLAN/base/CALL; any future A0 continuation uses a fresh successor change id.
  PLAN-only may be routed before Phase 0 merge, but checksum BUILD may start only after Phase 0 is confirmed MERGED,
  followed by fresh origin/main rebase, full gates, review and binding fresh G5.
  Preserve the fixed 11-leg appetite: owner chose option «А», coalescing future M1-9 + M1-10 without cutting evidence.
done_when: |
  1. work/c-exec-poligon-checksum-foundation-plan-001-call.md exists as one self-contained `to: executor`,
     `kind: engineering`, PLAN-only product CALL with a business-level goal and no play-procedure paraphrase.
  2. It carries the accepted contour above as owner direction, explicitly not as a pre-frozen implementation spec,
     and requires a detailed simple owner-readable PLAN plus actual owner approval.
  3. It permits no BUILD/RED/product implementation in the PLAN session and encodes the Phase-0 MERGED prerequisite,
     fresh origin/main rebase, full gates, review and binding fresh G5 for later BUILD.
  4. It leaves old c-exec-poligon-a0-001 immutable/closed as STOP, leaves M1-A0 blocked, and opens neither a BUILD CALL
     nor the successor A0 PLAN.
return: |
  RESULT with the new PLAN-only executor CALL path, a short contract summary, exact evidence pointers, and explicit
  confirmation that no product file, RED test, BUILD CALL, successor A0 plan, TREE or CHARTER changed.
budget: one session

END_OF_FILE: live/indie-game-development/work/c-work-poligon-checksum-foundation-plan-001-call.md
