# RESULT — s-work-010 (g-9c41 Wave 2): open t-3 ∥ t-4 in parallel (owner chose C; framed + hardened both executor legs)

direction indie-game-development / bet g-9c41 / Wave 2 / play work (executor-leg framing, owner present).

## outcome

- Owner DECISION d-wave2-seq-001 resolved in-session (owner present): run **t-3 ∥ t-4 in PARALLEL** (option C) — «давай рассмотрим возможность запуска параллельно … я бы сейчас сфокусировался бы на 2х задачах». G1 holds (2 active tasks ≤ 3).
- Owner added three binding requirements for t-4 (echo-numbered): **R1** wire the REAL Dungeon Architect so it actually generates the level; **R2** when an action can't go via MCP, give step-by-step Unity instructions + answer the owner's questions; **R3** a step sent to the owner is NOT done until he actually does it and confirms (no self-marking owner-run steps; leg can't close on an unconfirmed step). R2/R3 saved to auto-memory as a standing habit (feedback-owner-run-unity-steps-real-gate).
- Two executor legs FRAMED (outcome + acceptance only; HOW → each leg's PLAN) and **adversarially hardened** (workflow wd3a59z47 / wf_d2088dd9-590: 4 critique lenses → adversarial verify; 20 findings, 17 confirmed; 14 substantive must-fixes folded, 3 "inputs-not-delivered" flags handled as a tooling note — see captures) and **OPENED**: c-exec-007 (t-3) + c-exec-008 (t-4). Full CALL text below.
- Parallel-safety designed in: t-4 reads the FROZEN gas read-model IGasReadModel/RN1 and never reaches below it; t-3 EXTENDS the read seam additively and never changes ConcentrationAt; file-ownership split (t-3 = Core/** + tests, edits no scene/MonoBehaviour; t-4 owns *.unity + a NEW render scene, never co-edits GasDebugCoarseScene/GasDebugDirector). C is reversible — pausing t-3 leaves t-4 unaffected (t-4 depends on t-2, not t-3).
- Key hardening correction (finding #1, code-verified): coarse temperature is ALREADY shipped by t-2 as wire/hash plane 6 — a coupled plane of CoarseBandLayer, NOT a registered layer — and its CR1/CR2/CR3 replication already exists + is owner-accepted. So t-3 is purely ADDITIVE: it proves XL2 by registering a genuinely NEW independent demonstrative layer (not by re-homing temperature), and MUST NOT touch plane 6's representation/layerKey/fold-order/read-model ctor (that would couple into t-4).

## evidence

- d-wave2-seq-001 → answered (owner words quoted in NOW.md decision_inbox + here).
- t-3 status queued → active (c-exec-007); t-4 status queued → active (c-exec-008); both in NOW.md open_calls (full notes) + full CALLs below.
- Hardening: workflow wd3a59z47 (run wf_d2088dd9-590), 24 agents, 17/20 confirmed; the 14 folded must-fixes are itemized against the CALL clauses below.
- No code/spec touched in GasCoopGame this session (framing only). Builders execute the legs.

## state_changes

- NOW.md active_bet.phase: appended the 2026-06-19 s-work-010 line (owner chose C; both legs framed+hardened+opened; parallel-safety + file-ownership split).
- NOW.md active_tasks: t-3 → active (note: ADDITIVE on t-2; opened as c-exec-007); t-4 → active (note: owner R1/R2/R3; opened as c-exec-008).
- NOW.md decision_inbox d-wave2-seq-001 → answered (owner C, present; quote; R1/R2/R3 recorded).
- NOW.md open_calls: added c-exec-007 (open) + c-exec-008 (open) with full notes.
- NOW.md next: replaced — two legs in flight (parallel-safety restated) → review the Wave-2 node when both return; carry-forward + owner-side non-gating unchanged.
- LOG.md: appended the s-work-010 line.
- Auto-memory: created feedback-owner-run-unity-steps-real-gate.md + MEMORY.md index pointer (R2/R3 standing habit).

## captures

- cap-1: R2 (instructions-not-only-MCP) + R3 (owner-run = a real, blocking gate; not-done-until-owner-confirms) are candidate STANDING habits beyond t-4 — consider promoting to os/engineering (a Unity / owner-run-axis rule) at a maintenance session. Saved to auto-memory now; OS-rule promotion is maintenance-gated (do NOT touch os/** from a direction session). Relates to deliverable-exists-invariant-v7.
- cap-2: the hardening workflow's draft-injection likely glitched — 3 critique/verify agents saw the c-exec-007/c-exec-008 drafts as the literal token `undefined` (findings #5/#10/#14). They compensated by reading live state directly and still produced 14 grounded must-fixes; the verifier confirmed them. Lesson for future CALL-hardening workflows: verify `args` actually reach the agents, or pass the drafts via a committed work/ file rather than inline `args`.

## decisions_needed

(none — d-wave2-seq-001 was the only open decision and the owner resolved it in-session.)

## play_check (play: work)

1. Recite — DONE: restated t-3/t-4, the bet, and that t-1/t-2 are closed.
2. Owner inputs (owner) — engineering legs, not owner-content; but the SEQUENCING + R1/R2/R3 are owner inputs and the owner was present. (owner) Owner chose C: «давай рассмотрим возможность запуска параллельно … я бы сейчас сфокусировался бы на 2х задачах»; and «ВАЖНО что в t4 мы настроили DA … можно работать не через MCP … предоставлять мне инструкцию что нажимать и делать в unity … нельзя считать её выполненной пока я её фактически не сделаю».
3. Do the work — DONE: framed both executor CALLs (call:executor ×2) and adversarially hardened them (wf wd3a59z47); the session framed outcome+evidence, did NOT design the solution (each leg opens with a PLAN, owner present).
4. Self-check — DONE: each CALL's done_when checked against the VERIFIED §CONTRACTS + the hardening checklists; R1/R2/R3 encoded with teeth (existence-proof / guide-loop / close-gate); parallel-collision guard stated in both.
5. Close — DONE: RESULT opens both legs; next = two legs in flight → review the Wave-2 node when both return.

## log

work (g-9c41 Wave 2 / t-3 ∥ t-4 OPEN, owner present): owner chose C (parallel); framed + adversarially hardened (wf wd3a59z47, 14 must-fixes) + opened c-exec-007 (t-3 engine) + c-exec-008 (t-4 render + REAL DA, owner R1/R2/R3); parallel-safe by read-model freeze + file-ownership split.

## next

Two executor legs in flight (c-exec-007, c-exec-008), each opening with a PLAN (owner present) in GasCoopGame (dev→main when green). When BOTH return → a review session for the Wave-2 node g-9c41. t-4 may return DONE-pending-owner-LOOK. Owner-side non-gating: push GasCoopGame (dev @7987506 / main @ce79e10) + this OS commit; validate the literal FishNet UDP wire when the host network is healthy.

---

# §c-exec-007 — Wave-2 t-3 executor CALL (FULL, framed + hardened)

to: a fresh executor (builder) session in the GasCoopGame product repo (branch dev → main when green).
play: work (executor leg) — indie-game-development / bet g-9c41 / Wave 2 / task t-3.
parent: s-work-010.
opens_with: an interactive PLAN (owner present) — this CALL states the OUTCOME + acceptance only; HOW is decided at the PLAN and recorded in an ADR, never invented here.

goal: A 3rd independent system-layer is networked-consistent at coarse scale alongside gas, having plugged in WITHOUT core edits — the extensibility seam is EXERCISED, not argued.

context:
- Binds the now-APPLIED canonical spec openspec/specs/sim-core/spec.md (t-2 requirements live) + the VERIFIED §CONTRACTS in work/converge-g-9c41.md §CONTRACTS (XL1, XL2, §RESOLVED-4, CR1/CR2/CR3, OR1/OR3).
- FROZEN by t-2 (c-exec-006), READ by t-4 — t-3 MUST NOT change: the coarse temperature wire/hash plane (CoarseLayerKeys.TemperatureKey=6) and its cell representation; the fact that temperature is a PLANE produced by the single coupled writer CoarseBandLayer (it is NOT, and need NOT become, a separately-registered layer — CoarseLayerKeys §LOCK-EXT); the CellHash.FoldLayer plane order (species 2..5, then temperature 6); CoarseBandStore._temperature storage; the CoarseGasReadModel ctor shape. The CR1/CR2/CR3 per-layer replication of plane 6 ALREADY EXISTS + is owner-accepted (t-2 done_when 5,6) — t-3 does NOT re-deliver it.
- Runs PARALLEL with t-4 (c-exec-008). Parallel-safety: t-4 consumes the FROZEN gas read-model IGasReadModel.ConcentrationAt(point, species, committedRevision); t-3 may EXTEND the read seam additively (a temperature/other-layer grid-addressed read at a committed revision) but MUST NOT change ConcentrationAt, widen the gas species enum, alter gas revision-gating, or add an overload shadowing the gas read path.
- Decisions carried: d-tempfeedback-001 (temperature = SINK; feedback DEFERRED post-g-d3a8; the §RESOLVED-4 read seam is grid-ADDRESSED, never data-routing), d-crossband-inv-001 Р2 (temperature stays INDEPENDENT/readable at any resolution on a committed revision; never fuse into the gas store; per-species temperature deferred but not foreclosed).

done_when (purely ADDITIVE on t-2; verifiable acceptance):
1. XL2 EXISTENCE (file-level isolation IS the proof, not a test name): a NEW 3rd INDEPENDENT non-feedback demonstrative layer EXISTS as new source file(s) under Assets/GasCoopGame/Core/Field/Layers/ keyed by a FRESH unused LayerKey (not Gas, not Temperature=6, not any coarse key already in use), registered on the LayerRegistry with a git-diff-EMPTY proof on the registry seam AND on every pre-existing sibling layer file — it ADDS files, edits none. A deliverable-coverage row resolves the NEW layer's file PATH (a Test-Path / file-existence deliver assertion — headless-class core files are NOT covered by the engine-class exists-path that caught leg-8).
2. Gas-only run reproduces the t-2 goldens BYTE-IDENTICAL; the gas+new-layer run keeps the gas Hash() byte-identical AND an RNG-conservation guard proves the new layer consumed ZERO gas RNG. The byte-identical / RNG guards are written against the genuinely-NEW 3rd layer, not re-run against the existing gas+temperature pair.
3. The layer-count the RevisionBarrier/store is constructed with is ASSERTED to accommodate the new LayerKey — the LOCK's SHALL-re-size SURFACED, never a silent capacity bump.
4. XL1 (gas→temperature SINK observable) by a non-vacuous suppressed-event NEGATIVE oracle (independent test-author): a reaction/heat GridEvent drives the EXISTING coupled temperature's sink response, measurable at the firing tick; SUPPRESS the event → the response must NOT fire (RED if a phantom/always-on response sneaks through).
5. §RESOLVED-4 read-ready seam exercised on a COMMITTED revision: a cross-layer consumer query "value at grid-cell c as of committed revision r" (incl. reading temperature plane 6) returns the layer-internal representation translated to grid coords deterministically; a NEGATIVE test rejects a live mid-tick / wrong-uncommitted-revision read (not silently served). PUSH replication and PULL read seam are distinct obligations — neither assumed-covered by the other.
6. Regression (don't break t-2): the gas-side IGasReadModel (ConcentrationAt signature + gas outputs + purity/integer-only/reflection-guarded-float-free + revision-mismatch rejection) stays byte-identical to the recorded t-2 oracle goldens (CoarseOracleTests OR1/OR3 vectors) across a representative point/species/revision set after the new read seam lands; the existing coarse temperature plane-6 replication stays GREEN under the new layer's registration.
7. Discipline: an INDEPENDENT test-author writes the RED acceptance oracles from the contract rows BEFORE build (builder can't edit them); check.ps1 -Deliver GREEN (headless + in-memory loopback binding gate); mutation ≥ 70; binding verdict = a fresh-session G5 refutation.

boundaries:
- Do NOT re-open ADR-0004 §LOCK / ADR-0003 v2 C1–C22 / frozen ADR-0005 BS1–BS15. This leg only ADDS; all Wave-1 + t-1 + t-2 goldens stay byte-green (a touched LOCKed artifact or a regressed golden = FAIL).
- If any t-3 change would alter plane-6 representation, layerKey, fold order, or the read-model ctor → OUT OF SCOPE, STOP-and-report (it would couple t-3 into t-4 under the shared read-model).
- Temperature stays a PURE SINK: gas→temperature exercised; temperature→gas FEEDBACK DEFERRED (d-tempfeedback-001). Building any read-back coupling — even dressed as "exercising §RESOLVED-4" — escalates to the owner, not a builder call. Forward constraint: the read seam lets a layer read another's field at any resolution on a committed revision, but MUST NOT fuse temperature into the gas store.
- No per-species temperature / cross-band per-species inversion (Wave 3, d-crossband-inv-001). Temperature stays a per-BAND-cell property.
- Scope of the extensibility proof = EXACTLY one new demonstrative independent layer (no 2nd/feedback layer, no new gas TYPES).
- CORE + TEST leg ONLY: register via the in-core LayerRegistry seam (CoarseField.cs) + prove in Core.Tests. t-3 edits NO *.unity scene asset and NO Adapters/GasDebug MonoBehaviour. (May extend CoarseBandStore/CoarseField/CoarseLayerKeys in core — textually mergeable C#; any such shared-core edit is t-3-OWNED, t-4 rebases at merge.)
- Out: >1 controlled breach; room-interior population (d-generator-001); mid-run late-join as a t-3 gate.
- →PLAN (owner present, decided in the product repo + ADR, NOT invented or restated here): layer-registry schema, subscribe-vs-read-model wiring, the XL2 byte-identical guard mechanism, the barrier-table re-size surfacing, the gas→temperature sink coupling. The goal/done_when state the OUTCOME + consistency PROPERTY only; HOW is the PLAN's.

return: builder RESULT routed home (commits/PR dev→main when green; check.ps1 -Deliver output; mutation artifact; fresh-session G5 verdict; the new layer file path as the XL2 existence artifact). The direction owns the next CALL.

budget: to the 2026-07-24 hard wall; pure C# core + loopback (no owner-run Unity axis on this leg).

---

# §c-exec-008 — Wave-2 t-4 executor CALL (FULL, framed + hardened)

to: a fresh executor (builder) session in the GasCoopGame product repo (branch dev → main when green).
play: work (executor leg) — indie-game-development / bet g-9c41 / Wave 2 / task t-4.
parent: s-work-010.
opens_with: an interactive PLAN (owner present) — OUTCOME + acceptance only; HOW at the PLAN + an ADR.

goal: A player can SEE the real coarse sim — a room visibly fills bottom-up from the breach, heavier gas low, the source identifiable, readable WITHOUT a debug overlay and as deliberate stylization not a stub — on a level generated by the REAL Dungeon Architect.

context:
- Reads the FROZEN gas read-model IGasReadModel/RN1 (SOLVER-AGNOSTIC; works on band OR degraded scalar) and reaches no lower (this insulates t-4 from t-3's internal barrier-table re-size). Depends on t-2's level+breach+read-model, NOT on t-3.
- From t-2: GasDebugCoarseScene.unity + the crude-cube debug renderer (to be REPLACED by the real stylized render in a NEW scene), SceneTopologyComposer + DaTopologyProducer + IDaRoomReader (FixedLevelRoomReader stands in now), GasRoomTag/GasLinkTag, the proven OR1/OR3 oracle (CoarseOracleTests). DA is installed + compiles ([DA-PATCH], owner-run).
- Decisions: d-generator-001 (DA room-composer mode; population OUT), d-bandhandoff-001 §SIGNOFF-BH (no-shimmer-EVER; on-return fill gradual, not strictly monotone).
- Runs PARALLEL with t-3 (c-exec-007).

done_when:
1. crit-6 render slice: a room visibly fills bottom-up from the breach side over time, heavier gas settles low, the source/breach identifiable — NO debug overlay, deliberate low-poly stylization not a stub; ms-budget on a min-spec class machine.
2. Acceptance has TWO separate gates, both required:
   (a) MACHINE-CHECKABLE (RN2): the PLAN FREEZES, BEFORE build, a machine-readable blind-check spec as a red-test-authored ledger row — the ground-truth schema (read-model-derived facts the agent is scored on, AT LEAST: gas-present, which-room-is-filling, filling-from-the-breach-side, heavier-gas-settles-low) + a numeric pass floor (correct ≥ a frozen N-of-M across the scripted breach run). The blind vision-agent is scored against ground truth DERIVED FROM the RN1 read-model (not free-form), reproducible (same revision sequence → same verdict), result written to a committed artifact docs/measurements/<call>-rn2-blind.json. The field set + N/M are PLAN/owner-set, but the floor MUST be frozen pre-build (an unstated/post-hoc bar = coverage FAIL).
   (b) The render-slice deliverable (committed Unity scene + recorded capture artifact) is an ENGINE-class v7 deliverable-coverage row: closes ONLY on a recorded existence proof — a committed path under Assets/** (scene) + a capture under docs/measurements/** the deliver check Test-Paths — NEVER a headless/sibling test name, stub, directory, or pre-existing file (the c-exec-006 leg-8 trap). BUILD (scene + capture exist + clear the machine floor) precedes LOOK.
3. NO-SHIMMER (owner-signed, testable): a committed test asserts the rendered RN1-sourced value sequence is CONTINUOUS across the off-screen-computed → on-screen surfacing transition on entry — no single-frame visible jump/pop above epsilon (the owner-signed GG4/OR4 coarse-half «это 100%», d-bandhandoff-001). Continuity only — NOT monotonicity (on-return fill is gradual/no-jump, explicitly not required strictly non-decreasing; curve-shape stays PLAN).
4. SOLVER-AGNOSTIC: renders from the RN1 published read-model ONLY (no direct band-solver coupling); a smoke run passes against BOTH the band publisher AND the scalar-per-volume degrade publisher (terminus survives the 06-30 degrade, kill_by next_if_false(i)). RN1 references the same OR1/OR3 oracle already proven + closed in t-2 — t-4 reads it, does NOT re-prove/re-bind OR1/OR3.
5. R1 — REAL Dungeon Architect wired, existence-proven (SCOPE-SPLIT from the render terminus): a real DungeonArchitectRoomReader : IDaRoomReader backed by the installed DA package (Assets/CodeRespawn/DungeonArchitect) produces the room volumes + door/wall links at level-generation time, funnelled through the EXISTING DaTopologyProducer → TopologyConformance seam. FixedLevelRoomReader is REMOVED from the runtime path (grep: zero non-test references; may remain only inside Assets/Tests/** as a fixture). The room prefabs the level is built from carry the GasRoomTag/GasLinkTag components the SceneTopologyComposer reads (the composed TopologyDocument is derived from real DA output, not InCodeRoomLevelProducer). EVIDENCE = a committed run-artifact under docs/measurements/ whose TopologyDocument (room count, StableIds, portals) is produced from DA output, with a fresh DA seed yielding a DIFFERENT but still TopologyConformance-passing level (two seeds → two distinct conforming ProfileHashes). The in-code==DA ProfileHash-equality test is RETAINED as the IN2 adapter-replaceability invariant but is EXPLICITLY NON-SUFFICIENT for R1 and MUST NOT be cited as R1 evidence — R1 closes only on the DA-output run-artifact + the zero-runtime-reference grep on FixedLevelRoomReader.
   GEOMETRY-MOVE RULE: real-DA wiring MUST NOT change TopologyDocument's shape or the FoldLayer/chunk addressing, and MUST keep IN2 ProfileHash-equality GREEN + re-run t-2's CR1/CR2 lossless oracle + ProfileHash goldens on the real-DA level. If real DA reads the SAME logical level t-2's FixedLevelRoomReader encodes → ProfileHash/sector-count/chunkCount/barrier-table byte-identical, and the t-2 run-artifact (docs/measurements/leg8-visible-slice-c-exec-006.json) stays asserted unchanged. If real DA deliberately composes a DIFFERENT/larger level (e.g. toward the R1 ~3,300-sector scale) → that changes sector→chunk→barrier-table count and is a t-3-COORDINATED barrier-table re-size event (t-3 owns the [2,4]→[N,4] re-size), with the run-artifact RE-RECORDED on the new level — NEVER a unilateral t-4 edit. A silent geometry move from t-4 is a cross-leg golden break, out of bounds.
6. R2 — instructions-not-only-MCP (guide loop): for every action this leg needs that is NOT performable via Unity MCP (Editor scene/prefab/material wiring, render-pipeline config, a compile-blocker patch, the DA asset hookup, an env/network condition), the builder DRIVES it as a guide loop (os/plays/guide.md): numbered ONE-action-at-a-time Editor instructions, the OWNER performs each, the owner confirms with a screenshot or a short answer, the builder verifies against the expected state before the next step, and ANSWERS the owner's questions before advancing. The owner's per-step confirmation IS the evidence; a sent-but-unconfirmed step is NOT done_when-satisfied; batching multiple actions into one instruction, or self-marking a sent step complete, is forbidden; each blocked action + its resolution is logged to docs/FRICTION.md.
7. R3 — owner-confirmation close-gate: the RESULT carries an owner-run checklist (one row per owner-run step: status pending|confirmed + the owner's literal token / a screenshot-or-recording ref + date). BUILD vs LOOK stay separate: the render-slice existence + the RN1-read artifact + the RN2 machine floor close HEADLESSLY (NOT owner-run, may NOT be deferred to the owner); the DA-wiring existence closes on the recorded existence proof. Only the LOOK is owner-run (the owner gamer-eye legibility verdict + the owner-signed no-shimmer). The builder MUST NOT mark an owner-run LOOK step done, infer it from a headless/loopback/vision-agent proxy, or reclassify it as 'env-deferred' (the FishNet-UDP env-deferral pattern applies ONLY to a transport/host-environment blocker whose binding gate is already headless+loopback — it is NOT a template for the owner-eye axis, whose binding evidence IS the owner). Close condition: with every BUILD/existence row green and the headless+vision gate green BUT an owner-LOOK row pending → the leg returns DONE-pending-owner-LOOK (built, gated, eyeball outstanding) and hands back to the direction; it does NOT return PASS/closed. t-4 → done ONLY when every owner-run row is confirmed; a BUILD/existence blocker is a normal gate FAIL (not owner-deferrable); a genuinely-blocked owner-LOOK step returns BLOCKED-on-owner with the pending checklist.

boundaries:
- Reads RN1/IGasReadModel only — do NOT modify the core sim or change ConcentrationAt (t-3 parallel-safe). t-4 OWNS all *.unity scene assets + the render director/terminus; build the player-legible terminus as a NEW scene + NEW director (do NOT co-edit GasDebugCoarseScene.unity or GasDebugDirector.cs — fork-by-copy if needed, leaving the t-2 debug scene untouched).
- Do NOT re-open ADR-0004 §LOCK / ADR-0003 C1–C22 / ADR-0005 BS1–BS15; all Wave-1 + t-1 + t-2 goldens stay byte-green.
- EXCLUDE g-7e15's menace/silhouette/material bars (player-LEGIBLE, not spectacular). COARSE-only render: the FINE 25cm per-cell window + the coarse↔fine no-jerk-on-ENTRY handoff + OR1 cross-TIER composition = Wave 3 (un-exercisable now); t-4 holds no-jerk/no-shimmer-EVER on the COARSE half only. The d-returnfidelity-001 mid-transient (far+UNSETTLED) return bar is a FINAL-impl / Wave-3 design requirement — NOT a t-4 acceptance bar; do NOT bind it into done_when. No temperature visualization (t-3's field is not rendered this wave).
- Out: >1 controlled breach; room-interior population (d-generator-001); mid-run late-join as a t-4 gate.
- →PLAN (owner present, decided in the product repo + ADR, NOT invented or restated here): the RN1 read-model sampling/interpolation scheme, push-vs-poll surfacing, the render pipeline (URP/HDRP), and the quantized-volumetric stylization technique. The goal/done_when state the player-legible OUTCOME + the RN2 blind-vision-agent + owner-eye acceptance only; HOW is the PLAN's.

return: builder RESULT routed home (commits/PR; check.ps1 -Deliver; the RN2 blind-check artifact; the DA-output run-artifact; real footage/screenshots of the DA level filling — feeds g-2f8c's 2026-08-31 page date; the owner-run checklist with confirmed/unconfirmed rows).

budget: rides the 07-11→07-24 cushion to ~07-21; auto-shrinks to a ≤1wk minimal-legibility floor (t-1 already met, so no shrink triggered).

END_OF_FILE: live/indie-game-development/history/s-work-010.md
