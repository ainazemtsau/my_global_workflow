# s-work-030 — shape (g-9c41): the CHARACTER ROAD + frame the first slice (Sc-types / c-exec-019)

Date: 2026-06-29
Play: shape (owner «можем оформлять» d-character-road-001) + frame the first slice's executor CALL
Direction / node: indie-game-development / g-9c41
Owner clarifications this session: TEST types not lore (span behaviour range); ENGINE-ONLY this slice (visual forgotten —
connects later, dev2 independent); shared-PARENT param layer (R15); post-release/mod extensibility = reserve the seam now.

## outcome

Shaped the CHARACTER ROAD as the near-term ordered spine (the bet rolls here, NOT the far-tier), and framed its first
slice as a build-ready (hardening-pending) executor CALL.

- ROAD (active_tasks, ordered): **Sc-types → Sc-weight → Sc-reactions → Sc-damage**, AHEAD of the far-tier **S3/S4/S5**
  (PARKED → when levels get big). Rolling-wave: only Sc-types detailed; the rest named + dependency-tagged.
- FIRST slice **Sc-types** = the multi-gas META-TYPE/TYPE param structure (R15 3-layer: shared PARENT params [density/
  packing, ratio-to-air=weight, spread speed] → per-meta-type → type/instance config + env tuning). Engine carries ≥2 TEST
  meta-types behaving differently via EXISTING params (spread/density); + the day-one per-cell dominant-TypeId checksum
  socket; + the MODDABILITY seam (ordered content-hashed session-fixed type registry → lockstep handshake hook; external
  mod-loader DEFERRED). ENGINE-ONLY (no visual hookup). Lock = ADR-0002.
- CALL c-exec-019 FRAMED → work/c-exec-019-call.md; adversarial hardening RUNNING (wf_672e0128-009) — fold then ready.

## evidence / decisions
- Shape doc → work/character-road-shape-2026-06-29.md (ordered road + Sc-types spec).
- d-character-road-001 → ANSWERED (road adopted). d-buoyancy-near-weight-priority-001 → SUBSUMED into Sc-weight.
  d-coop-interdependence-repin-001 → folds into Sc-reactions/Sc-damage PLANs.
- The earlier-recorded seams (R15 3-layer, day-one TypeId socket, moddability registry+handshake, dense-vs-sparse-at-PLAN,
  port-old-far-tier-weight-math) carried into the slice specs + the CALL.

## state_changes
- NOW.md active_tasks: S3 → parked (far-tier deferred); + Sc-types (active) + Sc-weight/Sc-reactions/Sc-damage (parked).
- NOW.md open_calls: + c-exec-019 (framed; hardening running).
- NOW.md decision_inbox: d-character-road-001 → answered; d-buoyancy-... → answered/subsumed.
- NOW.md next: IMMEDIATE NEXT → open c-exec-019 once hardened; direction = character road; far-tier parked.
- work/: character-road-shape-2026-06-29.md + c-exec-019-call.md. LOG + one line. history/s-work-030.md.

## play_check (shape)
- Cut list (G6): this slice CUTS visual hookup, weight/reactions/damage/temperature, lore types, the real mod-loader,
  far-tier. Riskiest assumption tested first: ≥2 types behave differently AND stay deterministic in loopback.
- Owner co-creation (G9): the road + slice-1 scope follow the owner's explicit «можем оформлять» + his TEST-types/
  engine-only/shared-parent/mod-seam clarifications. The far-tier deferral is a real reprioritization, owner-chosen.
- Did NOT detail downstream slices (rolling-wave; named only). Did NOT touch the canon §5 spine text yet (the spine
  reprioritization lives in NOW.md + the shape doc; the cheap canon-spec refresh is a separate owner-go item).

## decisions_needed (owner)
- (offer) cheap canon-spec refresh (forced-flow into model §3; S1/S2 spine lines; Fact-4; dup ADR-0012) — owner go.

## log
2026-06-29 — shape (g-9c41): shaped the CHARACTER ROAD (Sc-types→weight→reactions→damage; far-tier parked) + framed the first slice CALL c-exec-019 (Sc-types); hardening running.

## next
Fold the c-exec-019 hardening (wf_672e0128-009) → owner opens c-exec-019 in a fresh GasCoopGame_dev session (PLAN, owner
present) on the post-S2 base (main @adb9255). Then the road rolls to Sc-weight. Optional: the cheap canon-spec refresh.

END_OF_FILE: live/indie-game-development/history/s-work-030.md
