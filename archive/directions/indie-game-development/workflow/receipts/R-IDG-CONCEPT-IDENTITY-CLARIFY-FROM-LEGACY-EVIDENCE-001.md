---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: concept_identity_clarification_receipt
  status: accepted_after_verify_commit
  owner: proof_carrying_workflow_os
---

# R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-001

## Receipt State

```yaml
receipt_id: R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-001
direction_id: indie-game-development
operator: ClarifyObjective / LegacyEvidenceReview / HumanDecision
target_obligation: O-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE
status: accepted_after_verify_commit
result_kind: bounded_concept_identity_frame
creates_accepted_state: true
accepted_state_kind: bounded_concept_identity_from_legacy_evidence
legacy_documents_authority: evidence_only
legacy_documents_accepted_wholesale: false
child_handoff_needed: false
```

## Purpose

Record the bounded concept identity clarification result admitted by `R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-ADMIT-001` and corrected by current human input.

This closes the admitted obligation without creating strategy, roadmap, Horizon, Active Frontier, product execution, CodexExecution, Steam launch strategy, engine/networking commitment, old-code transfer, or full legacy import.

## Accepted Concept Identity Frame

```yaml
accepted_concept_identity_frame:
  identity_frame: >
    Co-op reactive gas-ecology expedition game / systemic atmospheric
    survival-puzzle-action frame. Players enter hazardous
    technical/lab/underground spaces where atmosphere behaves as a systemic
    ecology: different gases move, settle, rise, mix, transform, react, help,
    harm, obscure, slow, explode, mutate, or behave anomalously.

  player_fantasy_wording: >
    A co-op expedition team enters a dangerous facility where the atmosphere
    behaves like a living/reactive system. The team survives and progresses by
    understanding different gases, carrying samples or loot, managing
    containment, manipulating topology and ventilation, and using or preventing
    reactions between gases.

  short_player_facing_phrase: >
    Enter a place where the air lives by its own rules, and survive, exploit,
    or break that chemistry as a team.

  co_op_framing: >
    Co-op is based on distributed control over a reactive environment:
    scanning, carrying, venting, isolating, opening/closing topology, rescuing,
    triggering, and recovering from gas reaction events. Team mistakes can
    become systemic events: wrong door, wrong vent, broken container,
    incompatible gases, chain reaction, explosion, transformation, or
    anomalous gas behavior.

  genre_frame_candidate: >
    Co-op reactive gas-ecology expedition game / systemic atmospheric
    survival-puzzle-action.

  gameplay_promise: >
    Meaningful gameplay emerges from combinations: gas type + topology +
    ventilation + verticality + containment + loot/container state + player
    action + gas-to-gas reactions. Players can read, transport, isolate,
    release, mix, neutralize, trigger, avoid, or exploit gases. Mistakes and
    improvisations can produce explosions, transformations, new gas clouds,
    temporary benefits, area denial, environmental changes, or anomalous
    events.

  gas_grid_topology_gameplay_role: >
    Gas is not merely an ambient hazard. It is a reactive multi-gas ecology:
    different gas types can have different density, spread, hazard, visibility,
    source/sink, reaction, transformation, containment, and special/anomalous
    behavior. Grid/topology is the shared spatial substrate that lets gas,
    ventilation, verticality, doors/openings, source/sink anchors, future
    pressure/temperature hooks, containment, loot rupture, and reaction events
    become readable gameplay.
```

## Supported By Legacy Evidence

```yaml
supported_by_legacy_evidence:
  - typed gases with density, hazard, visibility, spread, source/sink, and reaction profile
  - heavy/light/neutral gas behavior
  - multiple gases in the same container and independent concentration tracking
  - reaction/transformation hooks deferred from implementation but valid as concept evidence
  - gas propagation, accumulation, clearing, vertical behavior, source/sink behavior, topology sensitivity, observable hazard state
  - grid/topology as stable spatial identity, connectivity, passability, vertical relation, vent availability, effective topology, and future mutation substrate
  - co-op/systemic/simulation-driven frame as legacy evidence candidate
  - real game, not only technical demo
```

## Current Human Input Integrated

```yaml
current_human_input_integrated:
  - multi-gas ecology is concept-critical, not a minor technical detail
  - different gases may be heavy, light, move differently, and interact
  - gases may react, explode, transform into new gases, or create special effects
  - rare/special/anomalous gases are candidate identity material
  - procedural gas visual identity is candidate context
  - possible lore candidate: research/pharmaceutical station finds valuable/healing gas, digs deeper into underground lab/city, encounters anomalous or intelligent gas
  - carried loot/container rupture can release gases and create co-op reaction events
  - grid is candidate shared substrate for future systems such as temperature, pressure, ventilation, and environmental modifiers
  - event-driven/system-boundary thinking is candidate technical context only, not implementation commitment
```

## Remaining Gaps

```yaml
remaining_gaps:
  - exact core loop
  - exact mission/objective structure
  - exact genre label
  - baseline player count
  - co-op roles or symmetry/asymmetry
  - gas taxonomy boundary
  - reaction taxonomy boundary
  - beneficial vs hostile gas boundary
  - rare/anomalous gas role
  - procedural gas visual identity rules
  - gas loot/container gameplay role
  - lore premise selection
  - readability of gas composition and reactions without debug overlays
  - how much chemistry is core loop versus later expansion
  - how grid hosts pressure/temperature/ventilation/reaction hooks without becoming over-engineered
  - commercial hook proof
  - technical feasibility proof
  - engine choice
  - networking stack
  - old code reuse/rewrite/discard verdict
  - monetization/pricing/revenue target
  - Steam launch strategy
```

## Candidate Next Obligations

```yaml
candidate_next_obligations:
  - obligation_id: O-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY
    status: candidate_proposed_only
    purpose: >
      Define which parts of multi-gas ecology are core identity versus future
      expansion: gas types, reactions, transformations, special gases,
      beneficial gases, hostile gases, anomalous gases.

  - obligation_id: O-IDG-REACTIVE-GAS-CORE-LOOP-CLARIFY
    status: candidate_proposed_only
    purpose: >
      Clarify how carrying loot, breaking containers, mixing gases, isolating
      zones, venting, and triggering reactions create minute-to-minute co-op
      gameplay.

  - obligation_id: O-IDG-GAS-READABILITY-AND-VISUAL-IDENTITY-GAP-AUDIT
    status: candidate_proposed_only
    purpose: >
      Identify what must be readable to players: gas type, density, movement,
      danger, reaction risk, beneficial effects, anomaly state, and procedural
      visual differentiation.

  - obligation_id: O-IDG-LORE-PREMISE-CANDIDATE-CLARIFY
    status: candidate_proposed_only
    purpose: >
      Preserve and compare lore candidates such as pharmaceutical/research
      station, healing gas, deep excavation, underground lab/city, and
      intelligent/anomalous gas without selecting a narrative roadmap.

  - obligation_id: O-IDG-STRATEGY-ADMISSION-DECISION
    status: candidate_proposed_only
    purpose: >
      Decide later whether strategy admission is safe after concept identity is
      accepted. This candidate does not admit or execute strategy.
```

## Forbidden Claims Preserved

```yaml
forbidden_claims_preserved:
  no_strategy: true
  no_roadmap: true
  no_horizon_selection: true
  no_active_frontier_selection: true
  no_product_execution: true
  no_codex_execution: true
  no_steam_launch_strategy: true
  no_engine_commitment: true
  no_networking_stack_commitment: true
  no_old_code_transfer: true
  no_full_legacy_import: true
  no_algorithm_selection: true
  no_final_gas_taxonomy: true
  no_final_reaction_system: true
  no_final_lore_selection: true
```

## Scope Audit

```yaml
scope_audit:
  target_obligation: O-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE
  in_scope_used:
    - live GitHub main proof state
    - admitted obligation boundary
    - accepted bounded legacy concept evidence inventory
    - current human correction about multi-gas ecology and reactions
  necessary_dependencies:
    - Ledger authority boundary
    - Obligations allowed/forbidden outputs
    - legacy evidence only boundary
  parked_residual_context:
    - procedural gas visual system
    - exact gas taxonomy
    - exact reaction implementation
    - event-driven technical architecture
    - temperature/pressure systems
    - lore details
    - player count finalization
    - engine/networking choices
    - old code transfer/reuse
  proposed_residual_obligations:
    - O-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY
    - O-IDG-REACTIVE-GAS-CORE-LOOP-CLARIFY
    - O-IDG-GAS-READABILITY-AND-VISUAL-IDENTITY-GAP-AUDIT
    - O-IDG-LORE-PREMISE-CANDIDATE-CLARIFY
    - O-IDG-STRATEGY-ADMISSION-DECISION
  blocked_or_forbidden:
    - strategy
    - roadmap
    - Horizon selection
    - Active Frontier selection
    - product execution
    - CodexExecution
    - Steam launch strategy
    - engine commitment
    - networking stack commitment
    - old-code transfer
    - final algorithm/data model selection
    - final lore roadmap
  child_handoff_needed: false
  hidden_acceptance_check: pass
  one_obligation_scope: pass
```

## Verification Result

```yaml
verification:
  receipt_created: true
  ledger_update_required: true
  obligations_update_required: true
  receipts_index_update_required: true
  dashboard_projection_update_required: true
  commit_required_for_accepted_state: true
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-001.md
