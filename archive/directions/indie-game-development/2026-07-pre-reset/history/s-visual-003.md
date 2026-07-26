RESULT s-visual-003 (resolves d-visual-buildstep0-001 from s-visual-002)
direction: indie-game-development   play: research (s-visual-002 owner-review amendment)   node/task: g-7e15 (VISUAL parallel track)

outcome: |
  Decision d-visual-buildstep0-001 RESOLVED = ADJUST. The owner rejected "build-step 0 = a min-spec perf spike
  FIRST": he has NO min-spec machine to measure on, does not want to chase problems that aren't here yet, and wants
  a WORKING visual on his HOME machine first, with optimization + min-spec derivation as a LATER pass once the game
  exists. On his direct question ("does measuring perf change what you build?") the honest answer is NO — a perf
  number changes only tuning knobs or, worst case, forces a later swap of the BODY-rendering technique, which the
  read-only seam makes cheap. So min-spec perf is DE-GATED: the build sequence now starts with the working-visual-on-
  home legs (steps 1→4 on FAKE data) and treats perf as a later optimization pass. Cheap safeguards kept from day one
  (2 body knobs + a free non-gating home frame-cost reading + body-behind-the-seam). The architecture itself is
  UNCHANGED (the owner accepted it; only the sequencing/perf-gating changed).

evidence: |
  work/gas-visual-architecture-2026-06-26.md updated (§6 perf-unknowns reframed as deferred; §7 intro = a PERF POLICY
  + step-0 row recharacterized from a front gate to a deferred policy; §9 confidence reworded). NOW.md g-7e15.next
  ADJUSTED (build sequence steps 1→6, working-visual-on-home first; recommended next = author the build-step-1 CALL).
  Owner's in-session words: «у меня нет слабой машины, я не могу её померить … не хочу размываться … для начала хочу
  получить рабочую версию на хоме … потом оптимизируем и поймём минимальные требования … визуализацию не думаю, что
  тебе много вариантов сделать».

state_changes: |
  work/gas-visual-architecture-2026-06-26.md: perf de-gated — §6 perf-unknowns header → "DEFERRED to a later
    optimization pass (NOT a front gate)"; §7 intro → a PERF POLICY block (working-visual-on-home first; 2 body knobs;
    free non-gating home reading; body behind the seam; NAMED DEFERRED RISK = later body-technique swap, bounded by
    decoupling); §7 step-0 row → "PERF — DEFERRED (a policy, not a leg)"; §9 confidence reworded to the deferral.
  NOW.md parallel_tracks g-7e15 `next`: the "STEP 0 = MIN-SPEC PERF SPIKE FIRST … d-visual-buildstep0-001 (open)"
    passage REPLACED → d-visual-buildstep0-001 ANSWERED = ADJUST + the adjusted build sequence (steps 1→6, working-
    visual-on-home first) + the cheap safeguards + the named deferred risk + recommended next = author the
    build-step-1 executor CALL + a reconciliation note (engine S0 now delivered, RN1 read-seam exists for step 6).
  LOG.md: + the s-visual-003 line.

captures:
  - The owner's "defer perf, build first" steer mirrors the engine bet's own d-sparse-solver-defer-001 (defer the
    weak-CPU re-measure to a later gate) — a consistent direction-wide pattern: build + measure-on-home now, derive
    min-spec + optimize at a later dedicated gate.
  - Concurrent-session drift reconciled: while this visual thread ran, engine sessions s-work-019 (S0 DELIVERED,
    GasCoopGame main @824948d) + s-work-020 (S1 reframed FORCED-FLOW) committed on top of s-visual-002 (b002dca),
    preserving the g-7e15 block. The visual track is unaffected; S0's RN1 read-seam now EXISTS for the step-6 swap.

decisions_needed: []

play_check:
  - 1 recite: done — restated the open decision (d-visual-buildstep0-001: proceed to a min-spec perf spike first vs
    adjust) and the owner's reframing.
  - 2 investigate: skipped — no new investigation; this is the owner-review amendment of the s-visual-002 deliverable
    (a judgment + plan edit, not research).
  - 3 confidence: done — confirmed FIRST-HAND against committed state that a perf number does not change the
    architecture (only tuning / a seam-cheap body swap), and reconciled the concurrent engine drift (git HEAD d1a8bda;
    b002dca preserved) before writing.
  - 4 close (owner): done — owner steered ADJUST in his own words («нет слабой машины … для начала рабочая версия на
    хоме … потом оптимизируем»); I sparred (agreed on substance, kept the cheap safeguards + named the deferred risk),
    applied the de-gating, and set next.

log: visual-track adjust (g-7e15, s-visual-003): d-visual-buildstep0-001 = ADJUST — min-spec perf de-gated (owner has no min-spec HW; a perf number doesn't change the architecture), build sequence now working-visual-on-home first + perf a later pass + cheap safeguards + named deferred risk; concurrent engine drift (S0 done / S1 forced-flow) reconciled; next = author the build-step-1 executor CALL.

next: |
  Author the build-step-1 executor CALL for a fresh GasCoopGame_dev session: the working-visual-on-home leg = the
  read-only SEAM + the two GPU buffers (GasParams + the clipmap GridView) + a FakeGasViewSource + the body indexing
  GasParams[dominantTypeId] + the stride-conformance gate, on FAKE data, per work/gas-visual-architecture-2026-06-26.md
  §7 step 1. Build the 2 body knobs (resolution scale + step count) in from the start; take a free non-gating
  frame-cost reading on the home machine. Opens with a PLAN (owner present). Owner starts it when he chooses (parallel
  to the engine bet, ~40–60 min/day).

END_OF_FILE: live/indie-game-development/history/s-visual-003.md
