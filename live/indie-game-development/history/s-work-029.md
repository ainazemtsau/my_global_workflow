# s-work-029 — research/audit (g-9c41): full-plan gap audit

Date: 2026-06-29
Play: research (owner-initiated full-plan analysis) → captures + decisions
Direction / node: indie-game-development / g-9c41 (whole gas-engine plan)
Trigger: owner «раз у нас оказались такие проблемы, давай сделаем анализ всего плана … нет ли проблем … в простом
детальном и понятном виде» (after the buoyancy gap surfaced).

## outcome

Audited the WHOLE g-9c41 gas-engine plan (canon + slice spine) for gaps of the buoyancy CLASS and others, grounding every
finding in the COMMITTED canon AND the real built code. Verdict: the FOUNDATION (50cm near-grid, forced-flow jets,
multiplayer-determinism proof) is solid + honestly scoped; the big hole is the BRIDGE to the "jewel" — every
character-giving mechanic (gas TYPES, weight/buoyancy, reactions, dose/damage, temperature) is in the design model but
scheduled NOWHERE (one open "S6+" line), the same shape as buoyancy, ×5-6. Plus a direction risk (next step S3 = far-tier
plumbing while near-character work is unscheduled), 2 co-op safety holes, canon spec staleness, and tidy-ups. Nothing
broken/dangerously hidden — gaps of SEQUENCING + HONEST SIZING, mostly fixable now with planning decisions, not code.

## evidence
- Audit workflow wf_59afe6f0-426: 70 agents, 8 lenses (model→slice, built-vs-planned, deps/sequencing, open-questions,
  lock/burial/ADR, player-feel, scope-honesty, cross-track) → per-gap refute-verify → synthesis. 53 raised → 37 verified.
- Each gap grounded in a canon §/line, NOW.md, history, OR a first-hand code fact (e.g. species=1 hardcoded; no buoyancy/
  damage/reaction code in the new near grid; networking has zero mention of the gas field; determinism scans skip Coarse/).
- Full report → work/gas-engine-plan-audit-2026-06-29.md (5 themes, 37 gaps, top-5).

## captures (durable; the audit's findings — see the report for all 37)
- THE CHARACTER ROAD (root): every character mechanic unscheduled → d-character-road-001 (OPEN).
- Co-op interdependence node (c-map-004) dropped + forced-coop now frozen design → d-coop-interdependence-repin-001 (OPEN).
- Scan-root parity gap (Coarse/ outside the determinism scans) → already on the S3 task; confirmed important (close before S3).
- Multi-gas TYPES + dose/damage unscheduled → part of d-character-road-001.
- Canon spec STALE: forced-flow missing from the model §3; S1/S2 spine lines stale; Fact-4 "chemistry day-one" contradiction
  → a cheap canon-refresh (owner-gated, like the ADR-0002 fix) — recommended next.
- Tidy-ups: duplicate ADR-0012 (engine+visual); orphaned v1 Layers dead code (Fact-6); stale ADR-0010 mentions in finished
  text; detail-bubble + hangar-fallback both deferred-and-leaning-on-each-other → pin.
- Old far-tier has proven 4-species + weight + heat integer math → PORT before S4 deletes it (don't re-R&D).

## decisions_needed (owner)
- d-character-road-001 (OPEN): define the ordered character sub-spine (TYPES → weight/buoyancy → reactions →
  type-damage/temperature) + answer buoyancy-vs-S3 priority. Recommend: character-road before S3.
- d-coop-interdependence-repin-001 (OPEN): re-pin the dropped co-op-interdependence engine affordance.
- (offer) cheap canon-spec refresh (forced-flow into the model; S1/S2 spine lines; Fact-4; ADR-0012 rename) — owner go.

## play_check
- This was an owner-initiated analysis (research). No state was changed beyond recording the audit + the 2 decisions + the
  captures. No slice re-planned (that awaits the owner's d-character-road answer). G1 intact (no new active bet/task).

## log
2026-06-29 — research/audit (g-9c41): full-plan gap audit (37 verified gaps); headline = the character "jewel" has no build road; 2 decisions + captures recorded.

## next
Owner picks the next direction: (A) the character-road (TYPES/weight/reactions — the visible jewel) vs (B) S3 far-tier
plumbing. Recommend A. Then I shape the chosen route (define the character sub-spine as named slices) + optionally do the
cheap canon-spec refresh. The 37-gap report is the working agenda.

END_OF_FILE: live/indie-game-development/history/s-work-029.md
