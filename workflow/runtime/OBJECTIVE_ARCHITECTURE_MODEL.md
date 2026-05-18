# Objective Architecture Model

```yaml
artifact_control:
  artifact_name: "Objective Architecture Model"
  schema: objective_architecture_model.v1
  owner_layer: runtime
  status: canonical
  repo_path: "workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md"
  default_load: yes
  freshness: refresh_when_basis_validity_horizon_or_frontier_rules_change
  last_updated: "2026-05-18"
```

## Purpose

Define the workflow runtime rules for proving what work should happen next inside a Direction.

This file owns basis-validity rules for:

- per-Direction objective architecture;
- Horizon Acceptance Proof;
- Active Frontier derivation;
- Next Action Proof;
- audit/research/execution readiness gates;
- route-valid versus basis-valid distinction.

It does not own canonical stage IDs, prompt paths, prompt status, target runtime, activation, or normal stage-to-stage `allowed_next` transitions. Those remain owned by `workflow/stage_registry/STAGE_REGISTRY.md`.

It does not own packet templates. Packet templates remain owned by `workflow/transport/*.md`.

It does not replace Direction Project Files, Phase state, Goal state, Portfolio Queue, Context Loading Index, or Phase Memory.

## Core invariant

```text
route_valid is not basis_valid.
```

A selected stage may be registry-valid and still be logically invalid when the proposed work is not grounded in the Direction objective, accepted horizon, active frontier, prerequisites, concrete target, or evidence path.

Runtime launch rule:

```text
No accepted horizon -> no active frontier.
No active frontier -> no material Goal selection.
No Next Action Proof -> no material stage launch.
No concrete target -> no audit/research/execution.
No evidence -> no closure.
```

## Direction independence

Each Direction has its own root objective, active initiative, active horizon, objective graph, active frontier, and next-action proofs.

The shared workflow engine provides the procedure. It must not impose one global objective across all Directions.

Human input may set values, priorities, constraints, and final consent. Human input is not automatically proof.

ChatGPT/Codex output may propose conclusions. Assistant output is not automatically proof.

Evidence owns facts. Logic owns validity. Workflow owns process.

## Objective stack

Use this compact stack when selecting strategic work:

```text
Direction Objective
-> Initiative
-> Horizon
-> Capability / Constraint node
-> Milestone / Proof node
-> Goal
-> Stage
-> Task / Execution Slice
-> Evidence
```

A higher layer defines why a lower layer exists. A lower layer must be derivable from the layer above it.

## Node model

Objective graph nodes may use these types:

```text
objective
initiative
horizon
capability
constraint
decision
evidence_gap
audit_target
research_question
execution_readiness
implementation_slice
validation_surface
artifact
documentation_promotion
```

Node statuses:

```text
candidate
ready
active
blocked
locked
premature
parked
done
superseded
rejected
unknown
```

Edge types:

```text
requires
unlocks
refines
evidences
blocks
alternative_to
conflicts_with
activates_when
```

## Horizon Acceptance Proof

A horizon is an intended state, not a task.

Before a material active horizon is accepted or changed, produce a compact `horizon_acceptance_proof`:

```yaml
horizon_acceptance_proof:
  candidate_horizon:
  direction_objective:
  objective_link:
    claim:
    evidence:
  current_state_basis:
    known_done:
    known_blockers:
    unknowns:
  unlock_claim:
    what_this_horizon_unlocks:
    why_unlock_matters:
  exit_predicates:
    - predicate:
  prerequisite_check:
    satisfied:
    missing:
    assumed:
  lock_check:
    horizon_is_locked: true | false
    locked_by:
    if_locked_select_prerequisite_horizon:
  alternatives_considered:
    - horizon:
      why_rejected:
  verdict:
    accepted: true | false
    reason:
    confidence: low | medium | high
```

Hard gates:

```text
Reject or route to repair when:
- horizon is not linked to the Direction objective;
- horizon describes an activity instead of a state;
- exit predicates are missing;
- unlock claim is vague or unsupported;
- prerequisites are unknown and material;
- the horizon is locked without a prerequisite horizon;
- the horizon is duplicate, premature, or optional expansion;
- source basis is missing or contradictory.
```

Locked horizon handling:

```text
If a strategically correct horizon is locked, keep it as parent context and select the nearest prerequisite horizon or frontier node instead of pretending the parent horizon is directly executable.
```

## Active Frontier

The active frontier is the set of nodes that are currently legitimate candidates for next material work.

```yaml
active_frontier:
  ready_nodes:
    - node_id:
      reason_ready:
      expected_unlock:
  blocked_nodes:
    - node_id:
      blocker:
      unblock_route:
  premature_nodes:
    - node_id:
      premature_because:
  parked_nodes:
    - node_id:
      activation_trigger:
  selected_next_node:
  selection_reason:
```

A node is ready only when:

- its parent objective/horizon is active;
- hard prerequisites are done, accepted as not required, or explicitly routed;
- success predicate is clear;
- required context/evidence is available or can be requested exactly;
- doing it now unlocks a meaningful next state;
- it is not merely interesting, optional, or premature.

## Next Action Proof

Before launching material G1, A1, D1, E1, F0, C1, C2, or a material Router-selected stage, produce or inherit a compact `next_action_proof`.

```yaml
next_action_proof:
  direction_objective:
  current_horizon:
  selected_frontier_node:
  proposed_work:
  proposed_stage:
  desired_delta:
  why_this_now:
  prerequisite_check:
    satisfied:
    missing:
    assumed:
  active_frontier_check:
    is_on_frontier: true | false
    why_not_premature:
  expected_unlock:
  alternatives_considered:
    - action:
      why_rejected:
  evidence_basis:
    - artifact_or_state:
      supports:
  readiness:
    concrete_target_exists: true | false
    acceptance_criteria_exist: true | false
    context_available: true | false
    stage_semantics_match: true | false
  verdict:
    basis_valid: true | false
    route_valid: true | false
    launch_allowed: true | false
```

If `basis_valid: false`, do not launch the material stage. Route to the smallest safe correction:

```text
M0_DIRECTION_MAP
B1_PROBLEM
S3_DECIDE
Context Request
Human Decision
Stop
```

## Audit readiness gate

A1 audit work is allowed only when:

```yaml
audit_readiness:
  audit_object_explicit: true
  audit_criteria_explicit: true
  downstream_decision_explicit: true
  source_evidence_available_or_requestable: true
  what_changes_after_audit_defined: true
```

If these are false or unknown, A1 must not perform a broad audit. It should return B1_PROBLEM, S3_DECIDE, Context Request, Human Decision, or Stop.

## Research readiness gate

D1 research work is allowed only when:

```yaml
research_readiness:
  research_question_explicit: true
  decision_unblocked_by_answer: true
  source_scope_defined: true
  stop_condition_defined: true
```

If these are false or unknown, D1 must not perform broad research. It should return B1_PROBLEM, S3_DECIDE, Context Request, Human Decision, or Stop.

## Execution readiness gate

E1/F0/C1/C2 execution planning or execution is allowed only when:

```yaml
execution_readiness:
  implementation_target_explicit: true
  allowed_surfaces_explicit: true
  validation_surface_explicit: true
  acceptance_or_review_path_explicit: true
  basis_validity_inherited_or_proven: true
```

If these are false or unknown, execution must not proceed.

## Candidate comparison

Candidate scoring is allowed only after hard gates pass.

Use qualitative scoring, not false mathematical certainty:

```yaml
candidate_score:
  objective_impact: 0-5
  unlock_value: 0-5
  constraint_removal: 0-5
  evidence_value: 0-5
  scope_smallness: 0-5
  reversibility: 0-5
  risk: 0-5 negative
  uncertainty: 0-5 negative
  human_burden: 0-5 negative
  context_cost: 0-5 negative
```

Scores are decision aids, not proof. The final route must include explicit rationale and rejected alternatives.

## Stage integration rules

Router:
- must not choose a material route from registry validity alone;
- must require basis-validity when selecting strategic Phase/Goal/research/audit/execution work;
- if basis is unclear, route to M0_DIRECTION_MAP, B1_PROBLEM, Context Request, Human Decision, or Stop.

M0_DIRECTION_MAP:
- owns horizon acceptance proof and active frontier derivation when the map is missing, stale, uninitialized, or materially affects strategic selection;
- must not build a broad roadmap or backlog.

G0_GOAL_SELECT:
- should select from active frontier ready nodes;
- must reject or route away from parked, premature, or unsupported candidates.

G1_GOAL_SHAPE:
- must challenge the selected seed before shaping it;
- must not turn an ungrounded seed into a polished Goal Contract;
- must include the Goal's graph/frontier binding when relevant.

A1_AUDIT:
- must start with audit readiness when the audit target is strategic, old-code, source-of-truth, or high-risk;
- must not audit broadly without criteria and downstream decision target.

D1_DEEP_RESEARCH:
- must start with research readiness;
- must not research broadly without a decision it unlocks.

E1_EXECUTION_BRIEF:
- must inherit or produce Next Action Proof before execution planning;
- must not plan HOW for unproven WHAT.

R1_GOAL_REVIEW_DISTILL:
- after reviewing a Goal, must report graph/frontier implications when the Goal touched map-bound strategic work;
- must not select a next required Goal merely because a surface is unresolved;
- must check whether the proposed continuation is basis-valid and on the active frontier.

P9_PHASE_CLOSE:
- may update compact map/frontier state when closing a Phase;
- must preserve Phase Memory and avoid duplicate or premature next Phase selection.

## Proof depth

Use adaptive proof depth.

Compact proof is sufficient for low-risk local continuation.

Full proof is required for:
- horizon selection/change;
- active frontier change;
- Goal selection from multiple candidates;
- audit/research launch;
- execution planning;
- Codex product/project execution envelope;
- shared workflow runtime changes.

## Forbidden behavior

```text
Do not infer basis-validity from route-validity.
Do not treat unresolved surfaces as automatic next Goals.
Do not run audit/research without a concrete target.
Do not accept a horizon because it sounds plausible.
Do not use scoring before hard gates.
Do not let user preference or assistant confidence replace proof.
Do not turn Direction Map into a calendar roadmap or backlog.
```

## End-of-file marker

`END_OF_FILE: workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
