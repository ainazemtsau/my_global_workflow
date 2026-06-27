# RESULT — s-work-018 (work, g-9c41 / S0)

date: 2026-06-23
play: work
node: g-9c41
task: S0
input: CALL — S0 (FOUNDATION SLICE: voxelizer + face-flow + sandbox + FEEL grey-box)

## outcome

The S0 foundation-slice executor CALL is FRAMED and adversarially HARDENED into c-exec-013
(build-ready) and registered as an open_call. The build itself runs as a SEPARATE GasCoopGame leg —
this OS `work` session frames + hardens the executor CALL and hands off (it does not design the
solution; the voxelizer/face-flow HOW stays the GasCoopGame PLAN's job). 12 must-fix + 5 should-fix
CALL-text tightenings were folded, every one a verified CAPTURE that re-opens NO locked decision (so
no ADR-0010/G9 was needed to frame the CALL). The delete/keep ledger was corrected against the real
GasCoopGame tree at HEAD a89b36b — catching a compile-break the original CALL would have created
(orphaned SnapGridFlowTopologySource) and a phantom "VScale file" hunt (it is a const inside the
reader). S0 stays active, awaiting the executor return.

CALL-vs-committed reconciliation: the CALL pasted into the session was a slightly older copy (it
listed the ARCHIVED aplus-replan-under-locked-arch-v1.md as an ingest target, which dev-plan-graph
§4 says NOT to read at PLAN, and omitted the s-research-012..017 cellsize synthesis + the two
knowledge READ-FIRST docs). The committed NOW.next was used as the source of truth (richer + current).

## evidence

- work/c-exec-013-call.md — the full hardened, build-ready S0 executor CALL (created this session):
  §0 pre-flight (v7→v8 re-sync + READ-FIRST + ingest list), goal (outcome), context (locked arch),
  boundaries (corrected delete/keep + OUT-of-S0 + LOCK boundary), done_when with per-clause
  [HEADLESS-RED]/[BUILD-SCAN]/[OWNER-RUN] verification surfaces, STOP-discipline v8 named anti-crutch
  list, evidence, budget, residual-risk flags.
- Hardening workflow wwr2am1l9 (64 agents; ground 3 + attack 6 lenses + per-finding adversarial
  verify + synth): 49/54 findings kept after the "is-it-real + does-it-reopen-the-lock" filter → 12
  must-fix + 5 should-fix amendments, all folded. Synth overall verdict: build-ready once the must-fix
  set is applied (it is). Output: tasks/wwr2am1l9.output.
- Ledger verified vs GasCoopGame HEAD a89b36b: DELETE set corrected (VScale = const@SnapGridFlowRoomReader.cs:76,
  not a file; SnapGridFlowTopologySource.cs added — sole caller + DA-model read; GasViewCoarseScene.unity
  scene-ref must be re-pointed/cleared to avoid a missing-script GUID). KEEP set verified present +
  load-bearing in Core (TopologyDocument/Conformance, TopologyStableIds, IGasReadModel=RN1,
  CoarseSectorGraph=ROOM-partition, RectDecomposition); far-tier TopologyPortalSpec explicitly preserved for S4.
- Determinism framing (clause 5) survived attack as CONFIRMED-CLEAN — integer-only + one-machine
  zero-float scan = the cross-CPU guarantee; no 2-machine gate; matches drift-guard #2/#5 + d-reflux-gate-001.
- Process note: the workflow's args.call interpolation rendered as `undefined`; agents recovered by
  validating against the committed NOW.md active_tasks S0 text (lines 278-305) — the correct
  authoritative text — so findings are sound.

## the 12 must-fix amendments folded into c-exec-013

1. Voxelizer + doorway→open-faces MUST be built in headless Core/** (closes the c-exec-012 Adapters/**
   self-cert escape; the binding DA-vs-hand identical-voxelization RED test is authorable only there).
2. ZERO-LEGACY delete set corrected: SnapGridFlowRoomReader.cs (contains VScale const + DA-model read)
   AND SnapGridFlowTopologySource.cs (sole caller + DA-model read) + scene-ref reconcile; grep-clean +
   compiles + no missing-script GUID acceptance; a compile break from this deletion is a CALL-scoped
   task, not a STOP-blocker.
3. Zero-float scan wired as a real check.ps1 gate step over the authoritative Core path + a planted-float
   RED control (named-but-unwired prose does not satisfy the clause).
4. Owner-eye split: «точно» discharged by the green headless/build suite; «весело» the ONLY owner-run
   non-unit-testable axis; all [HEADLESS-RED]/[BUILD-SCAN] green BEFORE the owner-eye gate.
5. 4 GAP sockets enumerated as day-one stubbed DATA with schema-presence RED tests (GAP-1 cap, GAP-4
   tick_divisor, GAP-2 void/exterior region_id sink, GAP-3 resolution_tag pair).
6. resolution_tag = the integer PAIR (geometry_res, gas_res) + build-enforced geometry=integer-multiple
   invariant (REJECT 75 vs 50); TopologyConformance pins the 2:1 mapping; start 50cm 1:1 → green → 100cm by config.
7. gas cell = 50cm GLOBAL authoritative pinned (so the voxelization-determinism RED test has a grid
   dimension); 25cm is NOT authoritative in S0; other knobs stay PLAN-decided.
8. Face-flow law CONSUMES open-face count as data (R6 HARD): RED tests MONOTONIC + SLIT-SEEPS + WALL-ZERO
   + MASS-CONSERVATION + EMERGENT-HEIGHT, with an equilibrium guard.
9. Equality oracle for "identical" voxelization (the canonical per-cell tuple + canonical order) +
   the openFaces() function signature; TopologyConformance extended additively for the near grid;
   keep TopologyPortalSpec for far S4.
10. Per-face primitive reserves §9.9 edge attributes (integer conductivity, direction-mask, breach
    threshold) as day-one inert-default integer fields (so S1/S5 are a data write, not a primitive rewrite).
11. checksum-covers-MEANING negative controls per meaning-dimension + canonical-order digest of the
    active-set (species-id reserved comparator slot).
12. OUT-of-S0 anti-blocker/anti-probe/anti-2-machine clause (the 3 binding probes are S4/S5/S6, never
    S0 blockers or RED tests; no RED test may require a 2nd physical machine).

## should-fix (also folded)

- STOP-discipline v8 named anti-crutch/anti-descope list (VScale-stretch, scene-tags, area-scalar,
  DA-model read, float fast-path, reduced-fidelity descope) + the fidelity floor (area always affects
  flow; a single open face seeps).
- ADR-0010 + owner-G9 lock-boundary on the ведро-classification step.
- structured snapshot stable/versioned/named schema reading the same canonical record as the gizmos.
- collapse/expand interface shape invariants (per-region/per-layer, mass-exact, never-average-a-column,
  reserves {energy_sum, capacity_sum}; identity body only in S0).
- flux-register integer carry + sparse checksum fold (only non-zero/active faces folded).

## state_changes (applied by this session as its own writer)

- NOW.md active_bet.phase: prepended the s-work-018 line.
- NOW.md active_tasks id:S0: status stays `active`; note extended (framed + hardened as c-exec-013;
  closes done only on c-exec-013 GREEN + owner «весело»).
- NOW.md open_calls: added c-exec-013 (status: queued; full CALL → work/c-exec-013-call.md).
- NOW.md next: replaced — open c-exec-013 in GasCoopGame; on GREEN apply RESULT + S1; on STOP triage.
- CREATE work/c-exec-013-call.md (the full hardened CALL).
- LOG.md: appended the s-work-018 line.
- CREATE history/s-work-018.md (this RESULT).

## captures

- Workflow args plumbing: a dynamic-workflow `args.call` rendered as `undefined` to the agents (they
  recovered by reading the live CALL). For future CALL-framing hardenings, inline critical text in the
  script body or verify args plumbing first. Single occurrence → log-and-watch (os/changes-don't-break-what-works),
  not yet a maintenance trigger.
- ChunkEncoder.cs:125 `(byte)c` silent chunk-count overflow (>255 chunks, hash stays green; §9.8/§14)
  is a REAL known silent-corruption bug, S2 net-replication scope — already on the c-exec-009
  named-deferral list. Carried, not acted on; resolved the ZERO-LEGACY ambiguity by scoping the S0
  delete to the dead DA→grid path only.

## decisions_needed

None. The ChunkEncoder ZERO-LEGACY ambiguity was resolved as a delegated tech call (out of S0 scope,
kept-as-is, known bug stays a named deferral) per "decide delegated tech Qs yourself".

## play_check (work)

1. Recite — done: restated S0 goal (sandbox: level→integer per-face grid + gas fills a room by
   face-flow, owner-eye «весело») and the bet g-9c41.
2. Owner inputs (owner) — N/A: S0 is engineering infrastructure, NOT owner-content (no food/voice/
   schedule/money the owner personally lives by); owner participation is the PLAN co-creation inside
   the GasCoopGame executor leg. No owner authoring is required to frame this CALL (G9 governs
   CHARTER/TREE, not CALLs).
3. Do the work — done: framed the executor CALL, hardened it via wf wwr2am1l9, folded 12 must-fix +
   5 should-fix, corrected the ledger, registered c-exec-013.
4. Self-check — done: compared c-exec-013 against the S0 done_when point-by-point via the hardening
   synth; verdict build-ready once must-fix folded (folded); residual risks named.
5. Close — done: this RESULT; next = open c-exec-013. S0 stays active (not the last-task-done case →
   next is NOT a review CALL).

## next

CALL — open c-exec-013 (S0 FOUNDATION SLICE) in GasCoopGame (C:\projects\Unity\GasCoopGame), a FRESH
Claude Code session, owner present. Build-ready CALL = work/c-exec-013-call.md. §Re-sync v7→v8 FIRST →
PLAN → RED-first independent test-author → build → -Deliver gate → fresh-session G5 → owner-eye «весело».
On GREEN return → a fresh OS session applies the RESULT (writer), marks S0 done, opens S1
(выброс-при-спауне + выдавливание). On STOP → a fresh OS session triages the escalation options
(re-shape, never substitute).

END_OF_FILE: live/indie-game-development/history/s-work-018.md
