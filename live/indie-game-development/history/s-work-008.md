# RESULT — s-work-008 (c-work-003) — Wave-2 t-2 framing (PLAN with owner + executor CALL)

Session: `work` play, bet **g-9c41 Wave 2**, task **t-2** (direction `indie-game-development`). Job: resolve the
1–2 owner GAMEPLAY decisions t-2 needs, plan the BS4 narrowing + openspec lifecycle, and FRAME the executor CALL
for t-2 — NOT build. Owner PRESENT (the 2 decisions were a live sparring conversation). Closes c-work-003; t-2
stays active with c-exec-006 framed.

## outcome

Both owner gameplay decisions are resolved, the two planner spec actions are planned, and the executor CALL
**c-exec-006** is framed and adversarially hardened (a 3-agent verify pass caught a real spec-contamination trap).

- **Р1 — what a room does when FULL → DECIDED (d-roomfull-001): closed level + per-room CAPACITY + BACK-PRESSURE.**
  One rule: a cell never exceeds its capacity (every flow/inject clamps to `[0,capacity]`). A source cannot push
  into a full room (it idles); a saturated CLOSED region SATURATES AND HOLDS — no terminal throw, no int overflow,
  no negative, mass-exact (capacity ≪ the int domain; internal math already in `long`). This is the t-2 LIVENESS
  done_when and it refutes the t-1 A10-3 terminal-overflow. **NO sink this wave** — the owner found a real risk (an
  always-on sink leaks all the gas → the threat self-resolves → anti-climax). Owner: «противодавление … самое
  логичное, самое хорошее решение»; «со стоком согласен» (defer). NAMED future seams: gas-vents-to-space
  (double-edged: relieves gas but decompression kills), doors-break-under-pressure (destructibility R9; back-pressure
  already stores the pressure number it reads), >2 bands / sector-subdivision (a configurable knob, Wave 3+).
- **Р2 — per-species TEMPERATURE → DEFERRED + BS4 narrowed (d-crossband-inv-001 ratified) + FORWARD-CONSTRAINT.**
  Build t-2 on the ratified per-band model (integration, not new physics — mixing physics into a build leg is what
  broke t-1). Per-species temperature = a named future seam (g-d3a8 / gas-type design). FORWARD-CONSTRAINT:
  temperature stays an INDEPENDENT layer, readable at any resolution on a committed revision; never fuse it into the
  gas store so as to foreclose a future per-species temperature. A room-temperature map ALREADY exists today, so
  deferring ≠ "one temperature everywhere" (the owner's worry — resolved).
- **Amount-on-return clarification (owner-accepted).** Correct AMOUNT on return is handled THIS wave by the always-on
  whole-level coarse tier (GG4 coarse half: source rate × elapsed). The FINE intra-room cloud SHAPE (a corner puff /
  creeping front) is Wave 3 (the fine tier + the owner-signed band-handoff). Owner: «понял, что это будет в волне 3,
  окей». No broken promise — two halves, two waves; the amount-half is in t-2's done_when.
- **Planner spec actions PLANNED (carried into c-exec-006).** (i) narrow ADR-0005 BS4; (ii) openspec L22 — apply the
  c-exec-005 change delta WITH its cross-band restatement narrowed in the same pass, then archive.

## evidence

- The 2 decisions were resolved in a live owner conversation (this session) and recorded in NOW.md decision_inbox
  (d-roomfull-001 answered; d-crossband-inv-001 note (5) RATIFIED). The amount-vs-shape split is recorded against
  the existing d-return-reconstruction-001 / GG4 coarse half.
- The framed CALL c-exec-006 (full text in `next` below) binds the VERIFIED §CONTRACTS (work/converge-g-9c41.md
  §CONTRACTS, converge-verify PASSED CLEAN): IN1/IN2/GG1/GG2/GG3/GG4-OR4 (coarse half)/CR1/CR2/CR3/OR1/OR2/OR3.
- **Adversarial hardening (wf_1b929b4e, 3 parallel reviewers reading the real source files):** 3 should-fix + 2 nits,
  all folded. The standout (flagged by TWO independent reviewers, then owner-eyes-confirmed): the c-exec-005 openspec
  change-folder delta `openspec/changes/c-exec-005-t1-coarse-band-solver/specs/sim-core/spec.md:82` (criterion b of
  "Requirement: Buoyancy by capacity-fill + overflow") STILL restates the dead cross-band claim — "the heaviest
  species (0), when made HOT … is displaced to the UPPER band (ceiling) **past a colder species**" — while the LIVE
  canonical `openspec/specs/sim-core/spec.md` is grep-clean. Applying the delta VERBATIM (the planner action's
  literal instruction) would RE-INJECT the exact claim the BS4 narrowing removes. Fix folded: c-exec-006 narrows
  criterion (b) in the SAME pass and binds a falsifiable done_when ("canonical spec ends with NO 'past a colder
  species' prose; BS10(e) preserved"; tests L7/BS10(e) untouched). Also folded: GG1 (topology-change feed) named +
  bound as its OWN observable on the breach (same-tick agreement / revision-monotonic / replay-identity — GG3
  inherits GG1), refutable independent of the CR2 hash; and the BS4 `eff=1@temp≥252` example reframed as a
  single-species fact, not a cross-band comparative.

## state_changes

- NOW.md `active_tasks` t-2: status `next → active`; done_when REFINED (added LIVENESS d-roomfull-001 + GG1 same-tick
  + CR3 negative test + the planner spec actions incl. the openspec-narrow-in-same-pass guard; per-gas temperature +
  fine intra-room shape marked OUT); status note records the 2 decisions + c-exec-006 framed + the verify pass.
- NOW.md `decision_inbox`: ADDED d-roomfull-001 (answered); APPENDED note (5) to d-crossband-inv-001 (ratified +
  forward-constraint + the openspec spec.md:82 contamination GUARD).
- NOW.md `open_calls`: c-work-003 → done; ADDED c-exec-006 (queued, framed).
- NOW.md `next`: rewritten — c-exec-006 is framed; the 4 t-1 SHAPE inputs RESOLVED + carried; the openspec guard +
  GG1 binding noted.
- LOG.md: one line appended. history/: this file.

## captures

- (already named as future seams in d-roomfull-001 — not new work this session) gas-vents-to-space (double-edged
  w/ decompression), doors-break-under-pressure (destructibility R9), >2 bands / sector-subdivision (configurable
  knob). Per-species temperature + per-species buoyancy RATE remain on the per-species-buoyancy seam line.

## decisions_needed

- none open. Р1 + Р2 resolved with the owner this session; the amount-vs-shape split owner-accepted.

## play_check (work play)

1. Recite — DONE (restated t-2 goal/done_when + the bet in the opening contract).
2. Owner inputs (owner) — DONE. The artifact IS owner-content (gas feel he will live by). Two decisions resolved in a
   live sparring conversation; owner words cited: «противодавление … самое логичное, самое хорошее решение»; «со
   стоком согласен»; «понял, что это будет в волне 3, окей». Р2 confirmed by his consistent «не вижу смысла сейчас»
   + the resolved extensibility worry; owner closed the discussion («всё обсудили, можно закрывать»).
3. Do the work — DONE. Framed the executor CALL c-exec-006 (the session frames the outcome + evidence pointers,
   never designs the solution — architecture is the executor leg's PLAN, owner present); planned the BS4 narrowing +
   openspec L22; hardened the CALL with a 3-agent adversarial verify (call:research-style child pass, wf_1b929b4e).
4. Self-check — DONE. c-work-003 done_when: (a) decisions recorded ✓ (d-roomfull-001 + d-crossband-inv-001 (5));
   (b) BS4 narrowing + openspec lifecycle planned ✓ (carried in c-exec-006 actions (i)/(ii), contamination-guarded);
   (c) full executor CALL framed ✓ (goal/context/boundaries/done_when/return/budget binding the §CONTRACTS); (d)
   RESULT carries the CALL + decisions + state_changes, closes c-work-003, t-2 stays active ✓.
5. Close — this RESULT; next = open c-exec-006 in GasCoopGame (PLAN-first, owner present).

## log

work (g-9c41/t-2 FRAMING, owner present): Р1 closed-level+capacity+back-pressure (d-roomfull-001) + Р2 per-species
temp deferred + BS4 narrow (d-crossband-inv-001 ratified) + forward-constraint; executor CALL c-exec-006 framed +
adversarially hardened (wf_1b929b4e caught the openspec spec.md:82 cross-band contamination + GG1 same-tick).
c-work-003 → done; t-2 → active.

## next — CALL c-exec-006 (executor leg, GasCoopGame)

```
CALL c-exec-006 — Wave-2 t-2: real DA-composed level + breach + coarse replication (liveness)
to: executor (coding agent, GasCoopGame, branch dev → main when green)
direction: indie-game-development   bet: g-9c41 Wave 2   task: t-2   parent: s-work-008 (c-work-003)
opens_with: a PLAN with the owner PRESENT (the architecture below is decided at that PLAN, NOT pre-decided here).

goal: |
  Put the kill-gate-proven coarse band solver onto a REAL DA-composed generated level, networked-consistent, with
  ONE real controlled breach driving a real topology change → gas flows room-to-room and HOLDS (LIVENESS: a full
  room exerts back-pressure and the world saturates-and-holds, never crashes), host + 2 clients consistent at coarse
  scale, and the single field-sampling oracle agreeing across consumers AND peers. Engine-free core + composition
  modes; NO graphics (that is t-4).

context: |
  - Foundation UNTOUCHED, do not re-open: ADR-0004 §LOCK + ADR-0003 v2 C1–C22 + frozen ADR-0005 BS1–BS15 (t-1
    kill-gate PASS_WITH_NITS, merged main @a868270). t-1 = synthetic seeded graph, headless, capacity-fill+overflow
    + per-band temperature; in-memory loopback host==client oracle.
  - VERIFIED §CONTRACTS to BIND (live/indie-game-development/work/converge-g-9c41.md §CONTRACTS, converge-verify
    PASSED CLEAN): IN1/IN2 (ingestion/TopologyDocument + adapter-replaceability), GG1 (topology-change feed), GG2
    (geometry/band sovereignty), GG3 (real controlled breach → vertical portals), GG4/OR4 (band-handoff — COARSE
    half only this wave), CR1/CR2/CR3 (coarse-tier replication + dual-guarantee consistency + integer-exact
    authoritative state, PER LAYER), OR1/OR2/OR3 (single field-sampling oracle / thinnest-open-level / ExposureQuery).
  - Owner decisions s-work-008 (owner present — HONOR, do not re-litigate):
    * ROOM-FULL = closed level + capacity-from-real-geometry + back-pressure (d-roomfull-001). A cell never exceeds
      its capacity (clamp to [0,capacity]); a source cannot inject beyond capacity (it idles); a full closed region
      SATURATES AND HOLDS — no terminal throw, no int overflow, no negative, mass-exact. NO sink this wave (gas does
      not leave the level). This is the A10-3 liveness fix: t-1 guarded CONSISTENCY; t-2 guards LIVENESS.
    * per-species TEMPERATURE = DEFERRED (d-crossband-inv-001 ratified). Build on the ratified per-band model.
      FORWARD-CONSTRAINT: temperature stays an INDEPENDENT layer, readable at any resolution on a committed revision;
      NEVER fuse temperature into the gas store in a way that forecloses a future per-species temperature.
    * AMOUNT-on-return = the COARSE always-on whole-level tier (correct quantity = source rate × elapsed; GG4 coarse
      half). The FINE intra-room cloud shape (corner puff / creeping front) is Wave 3 (owner-accepted) — OUT here.
  - Planner-directed SPEC actions (owner-ratified this session — the builder APPLIES the dictated wording, does NOT
    author them; everything else in BS stays frozen):
    (i) NARROW ADR-0005 BS4: remove the over-specified cross-band prose "a hot heavy species inverts past a cold
        light one — e.g. species 0 at temp ≥ 252 has eff = 1" and replace with the per-band-throttle TRUTH the model
        delivers: "each band's eff uses THAT band's own temperature; a hotter band holds proportionally less dense
        gas, so a HOT FLOOR drives gas upward. A hot species' OWN eff collapses toward the floor value (e.g. species 0
        at temp ≥ 252 has eff = 1, from the frozen law) so it is no longer the densest and rises — a SINGLE-species
        fact, NOT a cross-band comparison." Keep the frozen MW/eff law + BuoyancyTempShift=2. Add a NAMED FUTURE SEAM
        line: true cross-band per-SPECIES inversion (a hot heavy species overtaking a specific colder lighter one
        across bands) requires PER-SPECIES TEMPERATURE — DISTINCT from the per-species RATE seam — OUT of this wave.
        Fold the G5 N4 note (per-band-eff realized as a lower-band-temperature-throttled capacity + monotone-by-
        species-id overflow). MUST NOT weaken any BS10 criterion (BS10(e) "hot heavy species stratifies to the
        ceiling" stays — it tests per-band rise, not a cross-band per-species sort).
    (ii) openspec lifecycle (L22): apply the openspec/changes/c-exec-005-t1-coarse-band-solver/ spec delta to
        openspec/specs/sim-core/spec.md, then archive the change folder to openspec/changes/archive/. ⚠ CONFIRMED (not
        conditional): that change-folder delta — specs/sim-core/spec.md:82, criterion (b) of "Requirement: Buoyancy by
        capacity-fill + overflow" — ITSELF restates the dead cross-band claim ("the heaviest species (0), when made
        HOT … is displaced to the UPPER band (ceiling) PAST A COLDER SPECIES"); the LIVE canonical sim-core/spec.md is
        grep-clean. Apply the delta WITH criterion (b) NARROWED in the SAME pass (drop "past a colder species" →
        "the hot heaviest species rises to the upper band/ceiling because its own hot lower band holds proportionally
        less dense gas — its eff collapses so it is no longer the densest"), mirroring the BS4 narrowing. Keep the
        acceptance TEST wording (L7 / BS10(e)) UNCHANGED (already tests per-band rise, not a cross-band sort) — no
        gate touched. A verbatim apply that re-injects "past a colder species" is a FAIL.
  - Build-quality discipline (mandatory, builder-stage quality fix + I22): an INDEPENDENT test-author writes the
    acceptance/red tests from the CONTRACTS + the spec (incl. the NEW liveness/saturation + topology-seam + breach-
    flow + replication/oracle tests) BEFORE the build; the builder makes them pass and may NOT edit them. "A FIX IS
    A CHANGE": any fix routes through the gated contour (invariant-audit + red-test-first), never an in-session
    symptom hotfix. Engine-free core (R13); networking is an edge wrapper (R14); composition-root DI mode selection
    (R14). Env: Unity Personal → no headless Unity activation; the BINDING headless gate = the engine-free core + the
    in-memory loopback host+2-client reconstruction oracle; any REAL FishNet PlayMode / real-DA-scene axis is
    OWNER-RUN — PLAN the headless-vs-PlayMode split.

boundaries: |
  - OPEN WITH A PLAN, owner present — the ARCHITECTURE (the topology-adapter interface; the back-pressure / capacity
    representation; the breach mechanism; interest-management/relevance; the headless-vs-PlayMode split; the
    coarse↔fine seam left for Wave 3) is decided at that PLAN, NOT pre-designed here. This CALL frames OUTCOME +
    evidence, not the solution.
  - Do NOT re-open the LOCK / ADR-0003 v2 C1–C22 / frozen BS1–BS15 (the BS4 narrowing is the ONE planner-dictated
    edit; the builder applies the exact ratified wording, never authors a frozen-spec change). t-2 only ADDS.
  - OUT of scope (named, not dropped): graphics / render (t-4); per-species temperature (deferred); sink / venting /
    gas-leaves-the-level (deferred future seam); destructibility / doors-break-under-pressure (deferred future seam);
    the FINE tier / intra-room cloud shape / coarse↔fine no-jerk handoff (Wave 3); sector subdivision + more-than-2
    bands (deferred configurable knob); room-interior population (d-generator-001 OUT); temperature→gas feedback
    (post-g-d3a8).
  - t-2 = INTEGRATION (real level + breach + network + liveness), NOT new physics.

done_when: |
  (binds the VERIFIED §CONTRACTS + the existing NOW.md t-2 done_when + the owner decisions; binding by G5)
  1. IN1/IN2 — a generator-agnostic topology seam reads (scene-geometry + semantic tags/markers) → TopologyDocument;
     adapter-replaceability demonstrated on the DA room-composer alone (hand-made tagged room prefabs; meaningful
     size, hundreds of rooms; logically-identical deterministic ids across peers); GG2 sovereignty (geometric
     change-sets keyed by sector id, zero gas inputs).
  2. The coarse band solver runs on the REAL level, whole-level always-on; per-room CAPACITY bound to the real DA
     room geometry (the t-1 "named seam: t-2 binds free volume to real geometry").
  3. LIVENESS (d-roomfull-001): a full room exerts back-pressure (a source cannot inject beyond capacity; cells
     clamped [0,capacity]); a saturated CLOSED region holds — NO terminal throw, NO int overflow, NO negative,
     mass-exact; clearing a source after saturation leaves a LIVE field (refutes the A10-3 terminal-overflow).
  4. GG1/GG3 — ONE real controlled breach → topology change on a SINGLE agreed tick every peer observes identically;
     the topology-revision is strictly MONOTONIC (no unreconstructable gap); the change-set is REPLAY-IDENTICAL (a
     peer at revision r given the change-set to r+1 reaches r+1 with no host-private state) — stated as its own
     observable, refutable independent of the hash; gas flows (no outflow before, an outflow path the first tick
     after applied); CR2 LOSSLESS bit-exact ACROSS the coarse topology change.
  5. CR1 — coarse replication reaches host + 2 clients PER LAYER (coverage-floor vacuous = whole-level interest,
     anchored to gameplay-reach V2-2; an entitled-but-omitted region FAILS).
  6. CR2/CR3 — dual-guarantee per layer (lossless bit-exact every tick + lossy ≤Q with bit-exact-at-settle, one
     shared recon path); coarse authoritative state EXACT integer (no float in the hashed/wired state); the negative
     test (a non-deterministically-reduced float path FAILS the lossless oracle) stays non-vacuous.
  7. OR1/OR3 — the single-oracle cross-consumer probe: a client visual read-model (OR1) and a client-resident far-AI
     ExposureQuery (OR3) on DIFFERENT peers return the SAME concentration for the same (point, species, committed
     revision); a region entitled per OR3 but omitted from a client's stream FAILS.
  8. GG4 coarse half — exact source-pin: a source's identity survives a non-destructive topology change and the gas
     accumulates at a believable GRADUAL rate (amount = source strength × elapsed; the correct-amount-on-return).
  9. Clean 1-player parity (crit-7) on the same level + the same determinism/hash discipline.
  10. Planner spec actions applied: BS4 narrowed (exact ratified wording, no BS10 weakening); the c-exec-005 openspec
      delta applied + the change folder archived; AND the canonical sim-core/spec.md after delta+archive contains NO
      cross-band per-species-inversion prose (no "past a colder species" / "inverts past a cold light one") while
      BS10(e) hot-heavy-to-ceiling stratification is preserved; the temperature forward-constraint recorded in the
      PLAN/ADR.
  Scored against a default-FAIL G0 ledger frozen pre-build; the BINDING verification = an INDEPENDENT fresh-session
  G5 refutation (a Codex/GPT-5.5 read-only pre-pass is allowed; binding = the fresh session) + owner manual
  acceptance (the OWNER-RUN real-DA-scene / FishNet PlayMode axis + a real-level legibility eyeball).

return: |
  RESULT (executor) home to direction indie-game-development: outcome + evidence = commits/PR in GasCoopGame +
  check.ps1 output (gate green: the independent-author battery incl. the NEW liveness/saturation + topology-seam +
  breach-flow + replication/oracle tests; mutation ≥ floor; scale arithmetic; CR3 negative control) + the fresh-
  session G5 verdict + the owner manual-acceptance record. next = home to direction (close c-exec-006; advance t-2 →
  done on G5 PASS, then frame t-3 ∥ t-4).

budget: |
  A substantial multi-session engineering leg — PLAN-first (owner present), then independent-test-author RED tests
  from the contracts/spec, then build, then independent fresh-session G5. Land with cushion before the 2026-07-24
  node wall (leaves room for t-3 ∥ t-4). Degrade ladder unchanged (kill_by next_if_false): if the leg slips, the
  terminus is solver-agnostic. Close with a checkpoint RESULT on any platform switch / long leg.
```

END_OF_FILE: live/indie-game-development/history/s-work-008.md
