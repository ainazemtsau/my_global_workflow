---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: obligations_storage
  status: first_foundation_nucleus_execution_readiness_packaged
  owner: proof_carrying_workflow_os
---

# Indie Game Development Obligations

## Admission Boundary

These Obligations govern the Indie Game Development pilot under the workflow.

No old Direction files are imported as accepted truth.

No product execution Obligations are currently admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

## Open Obligations

No open_next obligations.

### O-IDG-LEGACY-INVENTORY-OPTIONAL

```yaml
obligation_id: O-IDG-LEGACY-INVENTORY-OPTIONAL
type: legacy_import
statement: Optionally inspect old Indie Game Development files as legacy evidence only.
status: open_optional
optional: true
full_legacy_state_import_performed: false
bounded_legacy_evidence_inventory_committed: true
bounded_inventory_receipt: R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
legacy_state_authority: false
required_operator_before_evidence_use:
  - LegacyImport
acceptance_conditions:
  - Legacy Import Receipt created
  - no old state imported without verification and commit
  - old Direction Map / Active Goal / Current Phase demoted if encountered
rule: Old files must not become evidence or accepted state without explicit LegacyImport Operator invocation.
```

## Candidate-Only Next Obligations

Candidate/proposed only. None are admitted as open_next obligations.

- O-IDG-TECHNICAL-EVIDENCE-AUDIT-FOR-FOUNDATION-BLOCKERS
- O-IDG-FIRST-EXPEDITION-PROOF-EXECUTION-READINESS-PACKAGE

## Satisfied Obligations

### O-IDG-FIRST-FOUNDATION-NUCLEUS-EXECUTION-READINESS-PACKAGE

```yaml
obligation_id: O-IDG-FIRST-FOUNDATION-NUCLEUS-EXECUTION-READINESS-PACKAGE
type: clarify_objective / readiness_package / human_decision
statement: >
  Accept the first no-player foundation nucleus execution-readiness package as
  bounded proof-state persistence only, including Grid as authoritative
  extensible spatial substrate, bounded topology mutation/breach readiness,
  event/change-set/snapshot contract surfaces, and gas profile/effect-hook
  extensibility, without admitting product execution, CodexExecution,
  implementation, strategy, roadmap, Horizon, Active Frontier, Steam launch
  strategy, engine commitment, networking stack commitment, old-code transfer,
  final gas taxonomy, or final reaction graph.
status: satisfied
priority: next
admitted_by: current_human_decision_2026-05-28
satisfied_by: R-IDG-FIRST-FOUNDATION-NUCLEUS-EXECUTION-READINESS-PACKAGE-001
accepted_result:
  accepted_state_kind: first_foundation_nucleus_execution_readiness_package
  proof_state_after_commit: first_foundation_nucleus_execution_readiness_packaged
  admits_only: bounded_no_player_foundation_nucleus_readiness_package
  executes_only: readiness_packaging
  grid_spatial_substrate_extensibility: accepted_for_package
  bounded_topology_mutation_breach_readiness: accepted_for_package
  event_change_set_snapshot_contract: accepted_for_package
  gas_profile_effect_hook_extensibility: accepted_for_package
  technical_evidence_audit_before_this_package: conditional_not_mandatory
  open_next_obligations: []
  no_strategy: true
  no_roadmap: true
  no_horizon_selection: true
  no_active_frontier_selection: true
  no_product_execution: true
  no_codex_execution: true
  no_implementation: true
  no_steam_launch_strategy: true
  no_engine_commitment: true
  no_networking_stack_commitment: true
  no_old_code_transfer: true
  no_final_gas_taxonomy: true
  no_final_reaction_graph: true
required_operator:
  - ClarifyObjective
  - ReadinessPackage
  - HumanDecision
```

### O-IDG-FOUNDATION-CORE-ACCEPTANCE-AND-EXECUTION-READINESS

```yaml
obligation_id: O-IDG-FOUNDATION-CORE-ACCEPTANCE-AND-EXECUTION-READINESS
type: clarify_objective / readiness_frame / human_decision
statement: >
  Accept the foundation-core execution-readiness decision frame as bounded
  readiness framing only, without admitting product execution, CodexExecution,
  implementation, strategy, roadmap, Horizon, Active Frontier, Steam launch
  strategy, engine commitment, networking stack commitment, or old-code
  transfer.
status: satisfied
priority: next
admitted_by: current_human_handoff_2026-05-28
satisfied_by: R-IDG-FOUNDATION-CORE-ACCEPTANCE-AND-EXECUTION-READINESS-001
accepted_result:
  accepted_state_kind: foundation_core_execution_readiness_decision_frame
  proof_state_after_commit: foundation_core_execution_readiness_framed
  admits_only: bounded_readiness_framing
  executes_only: bounded_readiness_framing
  foundation_core_execution_readiness_state: committed
  separate_technical_evidence_audit_before_readiness: conditional_not_mandatory
  preferred_candidate_next_obligation: O-IDG-FIRST-FOUNDATION-NUCLEUS-EXECUTION-READINESS-PACKAGE
  candidate_follow_up_obligations_only: true
  open_next_obligations: []
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
  no_implementation: true
candidate_next_obligations_only:
  - O-IDG-FIRST-FOUNDATION-NUCLEUS-EXECUTION-READINESS-PACKAGE
  - O-IDG-TECHNICAL-EVIDENCE-AUDIT-FOR-FOUNDATION-BLOCKERS
  - O-IDG-FIRST-EXPEDITION-PROOF-EXECUTION-READINESS-PACKAGE
required_operator:
  - ClarifyObjective
  - HumanDecision
```

### O-IDG-LEGACY-CORE-COMPRESSION-IMPORT

```yaml
obligation_id: O-IDG-LEGACY-CORE-COMPRESSION-IMPORT
type: legacy_import_compression / clarify_objective / human_decision
statement: >
  Rapidly compress and import useful restored Legacy progress about game
  concept, foundation core, technical foundation, first nucleus/MVP/proof core,
  and related documentation, without importing old workflow state wholesale and
  without admitting product execution, CodexExecution, implementation, engine or
  networking commitments, strategy, roadmap, Horizon, Active Frontier,
  Steam launch strategy, old-code transfer, final gas taxonomy, or final
  reaction graph.
status: satisfied
priority: critical
admitted_by: current_human_handoff_2026-05-28
satisfied_by: R-IDG-LEGACY-CORE-COMPRESSION-IMPORT-001
accepted_result:
  accepted_state_kind: bounded_legacy_core_compression_import
  proof_state_after_commit: legacy_core_compression_imported
  import_packet: directions/indie-game-development/workflow/import_packets/IDG_LEGACY_CORE_COMPRESSION_IMPORT_PACKET_001.md
  legacy_documents_authority: evidence_only
  legacy_documents_accepted_wholesale: false
  domain_game_documentation_claims: adopted_with_amendments
  legacy_game_concept: adopted_with_amendments
  foundation_core: adopted_with_amendments
  technical_invariants: adopted_with_amendments
  first_nucleus_or_mvp_route: split_candidate_only
  candidate_follow_up_obligations_only: true
  open_next_obligations: []
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
  no_implementation: true
  no_old_workflow_state_import: true
  no_final_gas_taxonomy: true
  no_final_reaction_system: true
required_operator:
  - LegacyEvidenceReview
  - ClarifyObjective
  - HumanDecision
```

### O-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY

```yaml
obligation_id: O-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY
type: clarify_objective / identity_boundary / human_decision
statement: >
  Clarify which parts of the accepted reactive multi-gas ecology are core
  identity versus future expansion, including gas types, reactions,
  transformations, special gases, beneficial gases, hostile gases, and
  anomalous gases, without producing a final gas taxonomy, final reaction
  system, implementation, strategy, roadmap, Horizon, Active Frontier, product
  execution, CodexExecution, Steam launch strategy, engine commitment,
  networking commitment, or old-code transfer.
status: satisfied
priority: next
admitted_by: R-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY-ADMIT-001
satisfied_by: R-IDG-GAS-ECOLOGY-IDENTITY-BOUNDARY-CLARIFY-001
accepted_result:
  accepted_state_kind: bounded_gas_ecology_identity_boundary
  result_kind: bounded_gas_ecology_identity_boundary
  gas_ecology_identity_preserved: true
  identity_frame_preserved: co-op reactive gas-ecology expedition game / systemic atmospheric survival-puzzle-action
  gas_ecology_boundary_preserved: reactive multi-gas ecology, not gas-as-hazard only
  grid_topology_role_preserved: shared spatial gameplay substrate for gas movement, containment, ventilation, verticality, source/sink anchors, topology changes, reaction locations, and future pressure/temperature/environment hooks
  bounded_core_identity:
    - gas ecology is identity-bearing, not decorative hazard dressing
    - multi-gas qualitative distinction is core, final gas taxonomy is not
    - reaction/transform potential is core, final reaction graph is not
    - topology-mediated gas play is core, implementation model is not
    - player-readable atmospheric manipulation is core, UI/VFX rules are not
    - hostile/beneficial/special/anomalous role spectrum is core, exact roles are not
    - co-op systemic event potential is core, final mission/team design is not
  candidate_follow_up_obligations_only: true
  no_new_next_obligation_admitted: true
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
  no_implementation: true
  no_final_gas_taxonomy: true
  no_final_reaction_system: true
  no_final_lore_selection: true
required_operator:
  - ClarifyObjective
  - HumanDecision
```

### O-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE

```yaml
obligation_id: O-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE
type: clarify_objective / legacy_evidence_review / human_decision
statement: >
  Clarify concept identity from Legacy concept evidence only. Legacy documents
  may be reviewed as evidence-only input and must not be accepted wholesale.
  The obligation may extract and verify concept identity candidates, gaps, and
  candidate next obligations without creating strategy, roadmap, Horizon, Active
  Frontier, product execution, CodexExecution, Steam launch strategy, engine
  commitment, networking stack commitment, old-code transfer, or full legacy
  import.
status: satisfied
priority: next
admitted_by: R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-ADMIT-001
satisfied_by: R-IDG-CONCEPT-IDENTITY-CLARIFY-FROM-LEGACY-EVIDENCE-001
legacy_documents_authority: evidence_only
legacy_documents_accepted_wholesale: false
accepted_result:
  accepted_state_kind: bounded_concept_identity_from_legacy_evidence
  result_kind: bounded_concept_identity_frame
  concept_identity_content_accepted: true
  identity_frame: co-op reactive gas-ecology expedition game / systemic atmospheric survival-puzzle-action
  gas_ecology_boundary: reactive multi-gas ecology, not gas-as-hazard only
  grid_topology_role: shared spatial gameplay substrate for gas movement, containment, ventilation, verticality, source/sink anchors, topology changes, reaction locations, and future pressure/temperature/environment hooks
  candidate_next_obligations_only: true
  no_next_obligation_admitted: true
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
required_operator:
  - ClarifyObjective
  - LegacyEvidenceReview
  - HumanDecision
```

### O-IDG-POST-INVENTORY-ORIENTATION-FRAME

```yaml
obligation_id: O-IDG-POST-INVENTORY-ORIENTATION-FRAME
type: orientation / projection_boundary
statement: >
  Create a bounded post-inventory orientation frame from accepted receipts and the
  accepted bounded legacy concept evidence inventory only. Classify accepted facts,
  legacy-evidence-only facts, candidate context, unresolved decisions, evidence gaps,
  and safe next route classes without selecting strategy, Horizon, Active Frontier,
  roadmap, engine, networking stack, Steam launch strategy, product execution, or
  CodexExecution.
status: satisfied
priority: next
satisfied_by: R-IDG-POST-INVENTORY-ORIENTATION-FRAME-001
accepted_result:
  accepted_state_kind: bounded_post_inventory_orientation_frame
  no_strategy: true
  no_roadmap: true
  no_horizon: true
  no_active_frontier: true
  no_product_execution: true
  no_codex_execution: true
  no_steam_launch_strategy: true
  no_engine_commitment: true
  no_networking_stack_commitment: true
  no_old_code_transfer: true
  no_next_obligation_admitted: true
required_operator:
  - Projection
  - ClarifyObjective
```

### O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY

```yaml
obligation_id: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
type: legacy_import
statement: >
  Inspect old Indie Game Development concept/archive material as legacy evidence only,
  extracting bounded concept facts needed for future strategy: concept premise,
  gameplay core, gas simulation role, player fantasy, genre/frame, commercial hooks,
  technical gameplay pillars, and explicit unknowns.
status: satisfied
priority: critical
satisfied_by: R-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY-001
accepted_result:
  accepted_state_kind: bounded_legacy_evidence_inventory_only
  legacy_state_authority: false
  inventoried_fields:
    - concept premise
    - gameplay core
    - gas simulation role
    - player fantasy candidate
    - genre/frame candidate
    - commercial hooks candidate
    - technical gameplay pillars
    - explicit unknowns
  no_strategy: true
  no_roadmap: true
  no_horizon: true
  no_active_frontier: true
  no_product_execution: true
  no_codex_execution: true
  no_steam_launch_strategy: true
  no_engine_commitment: true
  no_networking_stack_commitment: true
  no_old_code_transfer: true
  no_next_obligation_created: true
required_operator:
  - LegacyImport
```

### O-IDG-STRATEGIC-ROUTE-DECIDE

```yaml
obligation_id: O-IDG-STRATEGIC-ROUTE-DECIDE
type: human_decision
statement: Decide which strategic route to admit next from the projection map, without selecting Horizon, Active Frontier, roadmap, or execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-STRATEGIC-ROUTE-DECIDE-001
accepted_result:
  selected_route: A_LEGACY_CONCEPT_EVIDENCE_FIRST
  next_obligation: O-IDG-LEGACY-CONCEPT-EVIDENCE-INVENTORY
  no_legacy_facts_imported: true
  no_strategy: true
  no_horizon: true
  no_active_frontier: true
  no_roadmap: true
  no_execution: true
required_operator:
  - HumanDecision
```

### O-IDG-STRATEGIC-MAP-PROJECTION-CREATE

```yaml
obligation_id: O-IDG-STRATEGIC-MAP-PROJECTION-CREATE
type: projection
statement: Run the projection-only strategic path map step from accepted proof state; do not create Horizon, Active Frontier, roadmap, or product execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-STRATEGIC-MAP-PROJECTION-CREATE-001
accepted_result:
  projection_id: IDG-STRATEGIC-PATH-MAP-PROJECTION-001
  projection_only: true
  no_horizon: true
  no_active_frontier: true
  no_roadmap: true
  no_execution: true
  no_legacy_import: true
required_operator:
  - Projection
```

### O-IDG-CONSTRAINTS-DEFINE

```yaml
obligation_id: O-IDG-CONSTRAINTS-DEFINE
type: clarify
statement: Define hard constraints for the direction such as solo capacity, time, budget, acceptable risk, preferred product domain, and execution boundaries.
status: satisfied
priority: critical
satisfied_by: R-IDG-CONSTRAINTS-DEFINE-001
accepted_result:
  constraints:
    - solo developer by default, with AI/Codex/workflow assistance allowed and no human team assumed by default
    - 50-80 hours/week available for the game direction
    - low-spend default with about $200 current liquidity, about $100/month ChatGPT spend, $1000 normal budget envelope, and up to $3000 justified ceiling
    - income/revenue flow should exist within 9 months of accepting the constraints receipt, while exact amount, pricing, launch date, and monetization model remain unresolved
    - high risk tolerance accepted, bounded by no technology for technology's sake
    - gameplay depth is more important than technical complexity or physical accuracy for its own sake
    - Steam-only / PC-via-Steam accepted as platform/distribution boundary
    - marketing/business execution is allowed, but requires a workflow-provided playbook for actions, publishing, timing, and evaluation
required_operator:
  - ClarifyObjective
```

### O-IDG-SUCCESS-SEMANTICS-DEFINE

```yaml
obligation_id: O-IDG-SUCCESS-SEMANTICS-DEFINE
type: clarify
statement: Define what success means for this direction before strategy or execution.
status: satisfied
priority: critical
satisfied_by: R-IDG-SUCCESS-SEMANTICS-DEFINE-001
accepted_result:
  success_requires_all:
    - technical_pride_success
    - game_completion_success
    - commercial_success
    - personal_pride_success
required_operator:
  - ClarifyObjective
```

### O-IDG-ROOT-OBJECTIVE-CONFIRM

```yaml
obligation_id: O-IDG-ROOT-OBJECTIVE-CONFIRM
type: human_decision / clarify_objective
statement: Confirm or redefine the root objective for Indie Game Development under the workflow.
status: satisfied
satisfied_by: R-IDG-ROOT-OBJECTIVE-DECISION-001
accepted_result:
  root_objective: Create and finish an indie game within the already selected concept, with two equal top-level outcomes: a technically strong game the user can be proud of, and a commercially successful product that can generate meaningful revenue.
  root_level_constraints:
    - Work within the already selected concept; do not restart concept discovery by default.
    - Technical strength / technical ambition is a root-level value pillar.
    - Commercial success / meaningful revenue is a root-level value pillar.
    - Old concept/archive material remains legacy evidence only until admitted through valid workflow.
required_operator:
  - ClarifyObjective
```

## Blocked Obligations

None.

## Execution Boundary

No CodexExecution/product execution Obligations are admitted.

No CodexExecution operator may run.

No roadmap item exists without admitted Obligation.

Execution remains unavailable until required constraints, strategy, and execution-ready precondition Receipts are accepted and committed.

The first foundation nucleus execution-readiness package satisfies one bounded obligation only. It creates no product execution, CodexExecution, implementation, roadmap, Horizon, Active Frontier, Steam launch strategy, engine commitment, networking stack commitment, old-code transfer, final gas taxonomy, or final reaction graph.

The legacy core compression import creates candidate follow-up obligations only. It does not admit a next run.

END_OF_FILE: directions/indie-game-development/workflow/OBLIGATIONS.md
