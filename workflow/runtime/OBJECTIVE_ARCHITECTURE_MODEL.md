# Objective Architecture Model

```yaml
artifact_control:
  artifact_name: "Objective Architecture Model"
  schema: objective_architecture_model.v1
  owner_layer: runtime
  status: canonical
  repo_path: "workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md"
  default_load: yes
  freshness: refresh_when_basis_validity_horizon_frontier_or_solution_shape_rules_change
  last_updated: "2026-05-18"
```

## Purpose

Define the workflow runtime rules for proving what work should happen next inside a Direction.

This file owns basis-validity rules for:

- per-Direction objective architecture;
- Horizon Acceptance Proof;
- Active Frontier derivation;
- Next Action Proof;
- Minimum Sufficient Solution Proof;
- anti-anchor handling for user-provided implementation examples;
- solution-shape minimality, human-burden, component-necessity, and overcut guards;
- audit/research/execution readiness gates;
- route-valid versus basis-valid distinction.

It does not own canonical stage IDs, prompt paths, prompt status, target runtime, activation, or normal stage-to-stage `allowed_next` transitions. Those remain owned by `workflow/stage_registry/STAGE_REGISTRY.md`.

It does not own packet templates. Packet templates remain owned by `workflow/transport/*.md`.

It does not replace Direction Project Files, Phase state, Goal state, Portfolio Queue, Context Loading Index, or Phase Memory.

## Core invariant

```text
route_valid is not basis_valid.
basis_valid is not solution_minimal.
solution_minimal is not solution_trivial.
```

A selected stage may be registry-valid and still be logically invalid when the proposed work is not grounded in the Direction objective, accepted horizon, active frontier, prerequisites, concrete target, or evidence path.

A proposed action may be basis-valid and still be invalid when the selected solution shape is overbuilt, anchored to nonbinding user examples, violates a stated dominant constraint, preserves unnecessary components, or cuts below the minimum complete outcome.

Runtime launch rule:

```text
No accepted horizon -> no active frontier.
No active frontier -> no material Goal selection.
No Next Action Proof -> no material stage launch.
No concrete target -> no audit/research/execution.
No evidence -> no closure.
```

Runtime launch rule extension:

```text
No Minimum Complete Outcome -> no material scope cut.
No Minimum Sufficient Solution Proof -> no material HOW, process, architecture, template, artifact, workstream, or chat-splitting choice when solution shape is material.
No Component Necessity Test -> no durable artifact/template/workstream/chat split.
No Human Burden Budget -> no higher-burden solution when low burden is a stated primary constraint.
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
  solution_shape_check:
    required: true | false
    required_because:
      - reason:
    proof_status: not_required | inherited | proven | missing | failed
    solution_minimal: true | false | null
    complete_enough: true | false | null
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

## Minimum Sufficient Solution Proof

Minimum Sufficient Solution Proof validates the selected form of the solution.

It answers:

```text
Why this solution shape, rather than a simpler, heavier, user-example-anchored, or overcut alternative?
```

Core distinction:

```text
basis_valid is not solution_minimal.
solution_minimal is not solution_trivial.
scope_cutting is not goal fragmentation.
user examples are hypotheses unless explicitly marked as requirements.
```

Required when any of these are true:

- G1 is shaping a material Goal from a user seed with implementation examples;
- E1 is planning HOW, architecture, process, artifact structure, templates, workstreams, chat splits, or Codex execution envelope;
- multiple implementation paths exist;
- low burden, low friction, speed, simplicity, or "not геморно" is a stated user constraint;
- the proposed solution adds recurring user actions, persistent logs, reports, templates, roles, reviews, or multi-chat coordination;
- the task risks overbuilding, future-proofing, or cutting below a complete usable loop.

Produce or inherit a compact `minimum_sufficient_solution_proof`:

```yaml
minimum_sufficient_solution_proof:
  user_input_classification:
    real_job:
    desired_outcome_state:
    hard_constraints:
      - constraint:
        evidence:
    user_examples:
      - example:
        classification: nonbinding_idea | explicit_requirement | constraint | anti_example
        why:
    assumptions_not_allowed:
      - assumption:
  minimum_complete_outcome:
    one_complete_user_visible_loop:
    must_be_usable_without_extra_system: true | false
    success_predicates:
      - predicate:
    failure_if_removed:
      - element:
        what_fails:
    not_enough_if:
      - condition:
  dominant_constraint:
    type: human_burden | cognitive_load | context_persistence | safety | accuracy | cost | time | tooling | uncertainty | other
    evidence:
    implication_for_solution_shape:
  solution_shape_alternatives:
    - id:
      shape:
      derived_from_user_example: true | false
      burden:
      completeness:
      main_risk:
      why_rejected_or_kept:
  component_necessity:
    - component:
      acceptance_predicate_it_supports:
      if_removed_what_fails:
      simpler_substitute:
      keep_cut_or_park: keep | cut | park
  human_burden_budget:
    recurring_user_actions:
      - action:
        frequency:
        expected_minutes:
    context_switches:
    required_manual_formatting:
    review_frequency:
    failure_mode_when_user_skips:
    burden_verdict: acceptable | too_high | unknown
  overcut_guard:
    still_solves_real_job: true | false
    one_complete_loop_exists: true | false
    not_just_micro_task: true | false
    deferred_items_do_not_block_current_use: true | false
  verdict:
    selected_shape:
    why_this_is_enough:
    why_not_simpler:
    why_not_more_complex:
    required_components:
      - component:
    parked_components:
      - component:
        activation_trigger:
    validation_loop:
    solution_minimal: true | false
    complete_enough: true | false
    launch_allowed: true | false
```

Hard gates:

```text
Reject or route to repair when:
- user examples are treated as requirements without explicit evidence;
- no alternative independent from user examples is considered;
- the selected solution shape violates a stated dominant constraint;
- low burden is primary but Human Burden Budget is missing or too_high;
- a component remains even though removal does not break a current acceptance predicate;
- a future-proofing component is kept without current acceptance, safety, evidence, or persistence necessity;
- scope cutting removes the minimum complete outcome;
- the result is a micro-task rather than one complete usable loop;
- scoring is used to compensate for a violated hard constraint.
```

Required comparison rule:

```text
At least one considered solution shape must not be structurally derived from the user's examples.
```

Low-burden rule:

```text
If low burden is a stated primary constraint, a higher-burden solution is invalid unless it prevents a concrete safety, evidence, persistence, or correctness failure that the lower-burden option cannot handle.
```

Component rule:

```text
If removing a component does not break a current acceptance predicate, cut or park it.
```

Overcut rule:

```text
Cut scope until slightly uncomfortable, but not below the minimum complete outcome.
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
  solution_shape_proven_or_not_required: true
```

For product/project execution through Executor/Codex, execution readiness also requires:

```yaml
executor_handoff_readiness:
  target_project_ref_explicit: true
  executor_project_setup_status_known: true
  executor_project_setup_status_acceptable: true
  execution_work_package_or_equivalent_explicit: true
  validation_and_return_contract_explicit: true
```

Acceptable setup status is `complete` or `complete_with_approved_fallback`. Core-only setup is acceptable.

Stack-specific tuning is optional unless it is required to make validation or evidence possible.

Executor Project Setup itself is a distinct setup action/capability and does not require prior completed project setup.

This extension does not duplicate transport schemas and does not change stage registry authority.

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

When a user-stated hard constraint exists, candidate scoring must not compensate for violating it. In particular, `objective_impact` or `unlock_value` must not override a failed low-burden, component-necessity, safety, source-of-truth, or minimum-complete-outcome gate.

## Stage integration rules

Router:
- must not choose a material route from registry validity alone;
- must require basis-validity when selecting strategic Phase/Goal/research/audit/execution work;
- must require Minimum Sufficient Solution Proof when material solution shape, architecture/process choice, recurring user burden, or user-example anchoring risk exists;
- must route to B1_PROBLEM, S3_DECIDE, Context Request, Human Decision, or Stop when solution minimality is missing or false for material work;
- if basis is unclear, route to M0_DIRECTION_MAP, B1_PROBLEM, Context Request, Human Decision, or Stop.

M0_DIRECTION_MAP:
- owns horizon acceptance proof and active frontier derivation when the map is missing, stale, uninitialized, or materially affects strategic selection;
- when deriving horizon/frontier, must keep dominant constraint and human-burden implications visible when they materially affect strategic selection;
- must not build a broad roadmap or backlog.

G0_GOAL_SELECT:
- should select from active frontier ready nodes;
- must not select candidates merely because they match nonbinding user examples;
- must reject or route away from parked, premature, or unsupported candidates.

G1_GOAL_SHAPE:
- must challenge the selected seed before shaping it;
- must classify user examples as nonbinding ideas, explicit requirements, constraints, or anti-examples before shaping the Goal;
- must define Minimum Complete Outcome before scope cutting;
- must reject Goal shapes that are overbuilt, undercut, or anchored to nonbinding examples;
- must not turn an ungrounded seed into a polished Goal Contract;
- must include the Goal's graph/frontier binding when relevant.

A1_AUDIT:
- must start with audit readiness when the audit target is strategic, old-code, source-of-truth, or high-risk;
- may challenge whether a plan is overbuilt, undercut, user-example-anchored, or violating the dominant constraint when that is the audit target;
- must not audit broadly without criteria and downstream decision target.

D1_DEEP_RESEARCH:
- must start with research readiness;
- when research is used for solution-shape choice, must return implications for minimum sufficient solution rather than broad best-practice expansion;
- must not research broadly without a decision it unlocks.

E1_EXECUTION_BRIEF:
- must inherit or produce Next Action Proof before execution planning;
- must not plan HOW until the selected solution shape passes Minimum Sufficient Solution Proof or is explicitly not required;
- every durable artifact, template, recurring report, workstream, chat split, or repository-backed process must pass Component Necessity Test;
- must not plan HOW for unproven WHAT.

R1_GOAL_REVIEW_DISTILL:
- after reviewing a Goal, must report graph/frontier implications when the Goal touched map-bound strategic work;
- must report whether the delivered outcome created unnecessary operational burden;
- must not convert parked optional components into required continuation work without new basis-valid and solution-minimal proof;
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
Do not treat user examples as requirements unless explicitly classified as requirements.
Do not let scoring compensate for violating a hard human-burden or dominant-constraint gate.
Do not cut below the Minimum Complete Outcome.
Do not keep artifacts, templates, recurring reports, workstreams, or chat splits that fail Component Necessity Test.
Do not equate solution minimality with triviality or micro-task fragmentation.
```

## End-of-file marker

`END_OF_FILE: workflow/runtime/OBJECTIVE_ARCHITECTURE_MODEL.md`
