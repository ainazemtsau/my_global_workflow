---
artifact_control:
  namespace: workflow_v3
  artifact_type: pilot
  status: candidate
  owner: workflow_governance
  authority: candidate_parallel_runtime_not_active
---

# Indie Game Development Pilot

This file is candidate v3 design material. It is not active Workflow OS authority and does not supersede `workflow/**`.

## Status

- Candidate pilot only.
- No current Indie Game Development state mutation.
- No product execution.
- No accepted Direction runtime state.
- This pilot does not change `directions/indie-game-development/**`.

## Example Direction Control Skeleton

```yaml
direction_control:
  direction_id: indie_game_development_v3_pilot
  root_result: Ship a small game that the owner is proud to show publicly.
  success_conditions:
    - A playable core loop exists and is validated by the owner.
    - A production system can sustain small iterative releases.
    - Quality bar and pride criteria are explicit.
    - Public visibility route is chosen after readiness review.
  global_spine:
    - Core feasibility proof.
    - Production system setup.
    - Quality and pride review.
    - Public visibility route review.
    - Release candidate path.
  tracks:
    core_feasibility:
    production_system:
    quality_pride:
    public_visibility_watch:
  active_front:
    primary: core_feasibility_proof
    support:
      - production_system_minimum_viable_loop
      - quality_pride_criteria_draft
    watch:
      - public_visibility_route_options
    parked:
      - release_campaign_detail
    blocked: []
  event_journal_ref:
  review_queue_ref:
  shared_memory_index_ref:
  latest_continuation_packet_ref:
```

## Example Active Front

Primary: core feasibility proof.

Candidate node contract:

```yaml
node_contract:
  node_id: core_feasibility_proof
  parent_node: root_direction
  node_type: composite
  purpose: Prove that the game has a small playable core worth continuing.
  inputs:
    - owner taste and constraints
    - available engine or toolchain options
    - minimum viable loop idea
  allowed_memory_refs:
    - imported only after explicit import/review
  forbidden_actions:
    - mutate current IDG state
    - claim v3 active authority
    - start implementation without execution readiness
  expected_outputs:
    - feasibility questions
    - slice path
    - validation plan
    - result report
  validation_or_review_required: owner review
  integration_owner: parent_direction
```

## Example Support Tracks

- Production system: define the minimum loop for planning, building, validating, and closing game slices.
- Quality/pride: define the owner's bar for feel, coherence, polish, and public confidence.
- Public visibility watch: monitor when a route review is needed; do not push visibility work before readiness.

## Example Post-Readiness Route-Review Problem

```yaml
review_job:
  id: public_visibility_route_after_readiness
  target: public_visibility_watch
  trigger: core_feasibility_and_quality_readiness_pass
  question: Which public visibility route is appropriate after the game has a validated core and owner pride criteria?
  input_state_refs:
    - core_feasibility_result_report
    - quality_pride_decision_record
    - production_system_result_report
  allowed_memory_refs:
    - shared_direction_memory_after_import_review
  allowed_external_research: true
  forbidden_actions:
    - mutate current IDG state
    - launch public campaign
    - apply route change directly
  output_required: patch_proposal
  max_scope: route comparison and recommendation only
```

## Preservation Boundary

Current IDG data remains untouched and can be imported later only by explicit import. Existing IDG files are evidence candidates, not v3 authority.

END_OF_FILE: workflow-v3/pilots/indie-game-development/README.md
