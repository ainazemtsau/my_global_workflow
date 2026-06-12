# EVIDENCE INDEX — indie-game-development archive

Status: evidence-only (see live/indie-game-development/CHARTER.md, "Archive status"). Nothing here is accepted state. Import into live/ is selective, with an explicit reason and pointer, normally during map/audit sessions.

Origin: compressed 2026-06-12 from the full 153-file legacy archive (two old workflow generations: the "vNext-R" phases/goals payload and the later "Proof Workflow" ledger/receipts layer). All process scaffolding was deleted; everything remains recoverable from git history (commit "archive indie-game-development: compress legacy archive to evidence/").

Chronology hint: product/, technical/, proof/ come from the vNext-R generation (2026-04/05); distilled/ is the later Proof-Workflow layer and holds the most recent owner-corrected identity statements.

## product/ — what game this is (design truth of the old system)

- game-foundation.md — concept spine: 2–4 player co-op around managing a dangerous gas environment through level space; first product hypothesis; non-goals.
- primary-product-bet-expedition.md — selected bet Expedition vs rejected Containment with full rationale; stable product identity; locked run structure, minimum action contour, procgen function, harm/co-op status; non-goals; anti-audience.
- expedition-experience-model.md — locked experience model: core loop, tension sources, 8-step run structure, roles of gas / gas types / topology / procgen, co-op pattern, harm pattern, player promise.
- expedition-skeleton-document.md — minimum provable skeleton ("нарастающая экспедиционная ставка"): causal chain, lift, dangerous gas-vessel value, tools as risky capital, between-run consequence ledger, hard no-recovery-run boundary, decision queue, deferred hypotheses.
- expedition-proof-handoff.md — the single proof question for the first proof goal (judgment loop, not gas demo).
- technical-foundation-gas-and-grid-contract.md — Gas ↔ Grid peer-foundation contract: gas-owned vs grid-owned responsibilities, shared contract surfaces, fail-fast rule.
- clean-start-transfer-boundary.md — what transfers from the old code: starting set (Gas.Config/Foundation/Topology/T1/T2 + legacy Grid substrate), transfer-later (Gas.Interest, Gas.T3.Data), reference-only, do-not-carry; GridV2 is not a default replacement.

## technical/ — old-code evidence and frozen technical decisions

- 01_OLD_PROJECT_GRID_TOPOLOGY_TECHNICAL_DOC.md — only documentation of the old repo's (TheLastExit) Grid/Topology: Grid Core vs GridV2, rooms/doors/portals, events, tests.
- 02_OLD_PROJECT_GAS_SIMULATION_TECHNICAL_DOC.md — only documentation of GasV2R: module structure, T1/T2/T3.Data tiers, Interest/LOD, fail-fast validation, fixed-tick host control.
- 03_OLD_PROJECT_GRID_GAS_INTERACTION_DOC.md — only documentation of the old Grid–Gas integration (IGasGridEventHandler, GasGridIntegrationService, event ordering).
- 04_CORE_TECHNICAL_FOUNDATION_DECISION_BRIEF.md — frozen decisions: FishNet + Steamworks default for player-hosted co-op, domain-first model with Unity as render shell, Grid/Gas reuse is audit-required (not granted), smallest durable nucleus.
- 01_FIRST_TECHNICAL_NUCLEUS_FUNCTIONAL_SPEC.md — what the first gas nucleus must prove (propagation, accumulation, vertical density behavior, source/sink, topology sensitivity, debug visibility) and what it defers (CFD, explosions, final netcode).
- 01_GAS_COOP_GAME_PROJECT_EXECUTION_PROFILE.md — execution profile of the new game project: domain-first, testable core, adapter boundaries.
- 02_A1_AUDIT_RESULT.md — audit of legacy Grid sufficiency: reusable invariants, rejected assumptions (no monolith carry-over, no direct code transfer, old room ids insufficient), selected architecture (stable spatial identity graph, versioned change sets, narrow consumers).
- 03_FOUNDATION_MULTIPLAYER_READINESS_GUARDRAIL.md — Grid core is not "done" if single-player-only: must expose stable identity, command/commit, version/change-set, snapshot/delta seams.
- H1_G4A_PHASE_CLOSE_SUMMARY.md — pointer to the actually existing foundation in the GasCoopGame repo (commit 236bc30e..., MODULE_MAP.md, evidence files); parked candidate phases G4B–G4E. Input for the deferred "which repo to canonize" decision (CHARTER, Canonical repos).

## proof/ — how the first proof was framed

- 03_MINIMUM_EXPEDITION_PROOF_CORE.md — proof question, six observable signals, explicit gas-only-proof rejection, go/revise/kill rules, stop rules.
- 02_FIRST_PLAYABLE_PROOF_SLICE_BRIEF.md — candidate slice "Unstable Vessel at the Return-Path Split" mapped to the minimum Expedition loop.
- 01_EXPEDITION_SLICE_DEPRESSOR_METHOD_V0.md — reusable slice pressure-test method: paper-run protocol, MDA mapping, red-team questions, removal/swap/connection/spectacle tests, pass/weak/fail matrix.

## distilled/ — latest-generation identity statements (Proof-Workflow layer)

- IDG_LEGACY_CORE_COMPRESSION_IMPORT_PACKET_001.md — compressed adoption (with amendments) of the legacy core: Expedition bet, Gas/Grid peer foundation and contract, clean-start boundary.
- R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-001.md — identity frame "co-op reactive gas-ecology expedition / systemic atmospheric survival-puzzle-action", player fantasy, gameplay promise, evidence confidence levels, list of open gaps.
- R-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY-001.md — which parts of the gas ecology are core identity vs deferred expansion; candidate follow-up questions.

## Caveat — superseded numbers

Files in distilled/ (and some older docs) carry constraints from the previous system: 9-month revenue gate, 50–80 h/week, $1000 envelope. These are superseded by live/indie-game-development/CHARTER.md (six-month money gate 2026-12-11, 80–90 h/week, ~$3000 cap). Read them as identity/design evidence, never as current constraints.

END_OF_FILE: archive/directions/indie-game-development/evidence/EVIDENCE_INDEX.md
