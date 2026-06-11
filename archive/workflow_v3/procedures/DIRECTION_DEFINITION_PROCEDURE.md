# Procedure: Direction Definition

title: Direction Definition
status: active_procedure
canonical_location: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
entrypoint: launch_direction_definition
kind: core
procedure_boundary: formation_chat
child_call_policy: child_call_allowed_when_needed_for_bounded_source_check_or_research_only

## Purpose

Coordinate semantic Direction Definition after a setup-only root exists.

This procedure does not form semantic Direction entities itself. It verifies that semantic definition is admitted, classifies available context, selects exactly one next semantic definition step, and returns a bounded next-step packet / Transfer Packet for that selected procedure.

The ordinary first next procedure is `form_direction_spine`.

This procedure must not form, accept, persist, or execute Direction Spine, Direction Map, Active Front, Work Graph, Work Contract, roadmap, backlog, or product work.

## Trigger / When to Use

Use this procedure when all are true:

- START selected `launch_direction_definition`;
- the selected procedure path is `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md`;
- a setup-only root exists or exact accepted setup-root evidence is available;
- semantic Direction Definition is pending or explicitly admitted;
- the current next move is `launch_direction_definition`, or an admitted repair/adoption boundary explains why the current next move must be normalized to `launch_direction_definition`;
- the requested work is to route semantic Direction Definition to one next definition procedure, not to create downstream semantic artifacts directly.

Typical post-bootstrap use:

- `CURRENT_STATUS` confirms `setup_only_root_created`;
- `CURRENT_STATUS` says semantic definition is pending/candidate-only;
- `CURRENT_NEXT_MOVE` confirms `launch_direction_definition`;
- candidate semantic context from bootstrap or user input may exist, but it remains candidate-only;
- no accepted Direction Spine exists yet, so the selected next step is normally `form_direction_spine`.

## When Not to Use

Do not use this procedure to:

- create candidate Direction Spine content;
- create candidate Direction Map content;
- select candidate Active Front;
- accept Spine, Map, Front, Work Graph, Work Contract, or semantic Direction state;
- persist repository/runtime state;
- write `CURRENT_STATUS`, `CURRENT_NEXT_MOVE`, `DIRECTION_SPINE`, `DIRECTION_MAP`, or `ACTIVE_FRONT`;
- create roadmap, backlog, product strategy, or product execution content;
- launch Work Graph or Work Contract formation;
- run another core procedure inside this RUN;
- treat a NEXT_CHAT_CARD or Transfer Packet as proof that downstream work has happened;
- rely on Project Files/Sources cache, chat memory, Project title, uploaded files, or old eval files as accepted Direction state.

If the operator asks to form the Spine directly and setup/definition routing is already satisfied, route to `form_direction_spine` in a separate lifecycle instead of using this procedure.

## Required Inputs

Required START/lifecycle inputs:

```text
selected_entrypoint: launch_direction_definition
selected_procedure_path: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
kind: core
procedure_boundary: formation_chat
return_destination:
```

Required Direction/context inputs:

```yaml
direction_definition_request:
  direction_id: string | unknown
  runtime_root: directions_v3/<direction-id>/runtime/ | unknown
  setup_only_root_status: setup_only_root_created | pending | missing | conflicting | unknown
  semantic_definition_status: pending_definition | candidate_only | accepted | conflicting | unknown
  current_status_ref:
    path: string | unknown
    ref: branch | tag | commit | accepted_excerpt | unknown
    status: exact_read | verified_excerpt | missing | conflicting | unknown
  current_next_move_ref:
    path: string | unknown
    ref: branch | tag | commit | accepted_excerpt | unknown
    status: exact_read | verified_excerpt | missing | conflicting | unknown
  candidate_context_for_direction_definition: optional
  accepted_or_admitted_launch_boundary: present | missing | conflicting | unknown
  return_destination: same_chat | specified_parent | unknown
```

Required next-step inputs:

```yaml
next_step_selection_inputs:
  registry_ref:
  default_next_entrypoint: form_direction_spine
  default_next_procedure_path: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
  selected_next_entrypoint: unknown_until_stage_3
  selected_next_step_count_required: exactly_one
```

If any required input is missing and cannot be safely inferred from exact source or current user input, return a typed STOP or bounded context request. Do not invent missing Direction state.

## Source Requirements

Always read or verify exact accepted excerpts for:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`;
- `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md`;
- exact `CURRENT_STATUS.md` through resolved binding, or a verified accepted status excerpt;
- exact `CURRENT_NEXT_MOVE.md` through resolved binding, or a verified accepted next-move excerpt;
- `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` when the default next step is considered.

Read when relevant:

- runtime binding file resolving `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md`;
- `workflow_v3/procedures/DIRECTION_MAP_FORMATION_PROCEDURE.md` only when a verified prior Spine context could justify an exceptional Map next step;
- `workflow_v3/procedures/ACTIVE_FRONT_FORMATION_PROCEDURE.md` only when verified Map / Goal Evidence Graph context could justify an exceptional Active Front next step;
- source integrity, legacy, adoption, or recovery sources only when the current inputs claim prior semantic state, legacy state, or conflicting binding/status evidence.

EOF / integrity requirements:

- verify EOF markers where present;
- report unreadable, missing, truncated, or conflicting sources;
- distinguish exact repository source from verified excerpt;
- do not use broad repository search as binding authority.

Forbidden authority sources:

- `workflow_v3/evals/**`;
- deleted eval files;
- Project Files/Sources cache as accepted state;
- chat memory as accepted state;
- Project title as binding or semantic authority;
- uploaded files as accepted state unless separately admitted and verified;
- candidate docs or generated packs as accepted state;
- legacy Direction files unless separately admitted as legacy_evidence.

## Context Classification

Classify every material input before relying on it:

```yaml
context_classification:
  canonical_source:
    - registry source
    - selected procedure source
    - selected downstream procedure source
    - control-plane protocol source when read
  accepted_record:
    - accepted setup-only root package/status
    - exact accepted binding/status/next-move files
    - verified accepted excerpts
  candidate_context:
    - user-provided goals, outcomes, constraints, tracks, product ideas
    - semantic notes carried from bootstrap
    - provisional naming or framing
  adapter_evidence:
    - child/check/file/GitHub return evidence, only after verification
  cache_or_context_only:
    - Project Files/Sources
    - chat memory
    - Project title
    - uploaded files not separately admitted
  unknown_or_unverified:
    - any source claim without exact path/ref or verified excerpt
```

Candidate context may be passed to the selected next procedure, but it must remain candidate-only. This procedure must not convert candidate context into accepted Direction state.

## Complexity Selector

Use the smallest launch path that satisfies the output contract:

- `standard_spine_launch`: setup-only root and current next move are valid, no accepted Spine exists, and `form_direction_spine` is the selected next step.
- `source_repair_or_context_request`: exact setup/status/next-move evidence is missing, conflicting, or unavailable.
- `exceptional_next_step_selection`: verified prior semantic context exists and may justify selecting `form_direction_map` or `form_active_front` instead of `form_direction_spine`.
- `blocked_downstream_unavailable`: the selected downstream procedure is missing, conflicting, or not authored enough to execute.
- `recovery_required`: accepted state, candidate context, binding, current status, or next move conflict and cannot be safely normalized inside this procedure.

Complexity selection must not become runtime stage compression. RUN executes the declared stages below one material stage at a time.

## Completion Contract

```text
completion:
  result: Direction Definition next-step packet for exactly one selected semantic definition procedure, or explicit blocked result with exact missing setup, source, admission, selected-step, downstream-procedure, or packet boundary
  proof: setup-only root/status and CURRENT_NEXT_MOVE were checked from exact/admitted sources; context was classified; exactly one next step was selected; default form_direction_spine selection or exceptional selection was justified; downstream procedure availability was checked; transfer packet / NEXT_CHAT_CARD boundary is bounded; no downstream entity was formed or accepted; no required child call remains open
  blocked_if: setup-only root is missing, CURRENT_STATUS or CURRENT_NEXT_MOVE cannot be read or verified, launch_direction_definition is not admitted, source authority conflicts, selected next step is missing or multiple, downstream procedure mapping is unavailable, downstream procedure is not executable and blocked status is not explicit, candidate context is treated as accepted, packet boundary is incomplete, required child return is missing or unverified, or this procedure attempts to form or accept Spine, Map, Active Front, Work Graph, Work Contract, roadmap, backlog, or product work
```

## Stage Cards

### Stage 1 - Source Lock and Launch Admission

```text
stage_id: source_lock_and_launch_admission
stage_type: material stage
purpose: Confirm exact source authority, setup-only root evidence, and launch_direction_definition admission before semantic routing.
inputs: Registry, selected procedure source, binding/status/next-move evidence, setup root evidence, return destination.
required_stage_result: source_lock, setup_only_root_status, current_status_check, current_next_move_check, launch_admission_status, return_destination_status, source_limitations.
gate: PASS if exact/admitted sources are present and CURRENT_STATUS/CURRENT_NEXT_MOVE admit launch_direction_definition; EXPAND if bounded exact source access is required; STOP if setup root is missing, source conflicts, current next move is not launch_direction_definition, or return destination is missing.
utility_allowed_if: Exact source access, GitHub/file retrieval, or bounded source verification is required and the child-call gate passes.
blocked_if: missing_setup_root, current_status_not_read, current_next_move_not_read, current_next_move_not_launch_direction_definition, source_authority_conflict, return_destination_missing.
```

Internal checks:

```text
check_id: current_status_semantic_pending_check
stage_type: internal_check
purpose: Confirm status supports semantic definition launch.
pass_if: CURRENT_STATUS or verified accepted excerpt shows setup_only_root_created and semantic definition pending/candidate-only.
blocked_if: semantic definition is already accepted without admitted next boundary, status is conflicting, or status cannot be verified.
```

```text
check_id: current_next_move_launch_check
stage_type: internal_check
purpose: Confirm the next move is launch_direction_definition.
pass_if: CURRENT_NEXT_MOVE or verified accepted excerpt names launch_direction_definition as current/primary next move.
blocked_if: next move is missing, conflicting, or points to another procedure without admitted repair/adoption boundary.
```

### Stage 2 - Candidate Context Classification

```text
stage_id: candidate_context_classification
stage_type: material stage
purpose: Separate accepted setup/runtime facts from candidate semantic context.
inputs: Stage 1 source lock, setup/status/next-move facts, user input, bootstrap candidate context, accepted/admitted launch boundary.
required_stage_result: accepted_context, candidate_context_for_direction_definition, rejected_authority_sources, semantic_state_boundaries, unresolved_questions.
gate: PASS if candidate context is labeled candidate-only and no semantic state is accepted by implication; REWORK if accepted and candidate claims can be separated; STOP if semantic claims are presented as accepted without authority or candidate context required for launch is absent.
utility_allowed_if: Bounded source/check work is needed to classify conflicting source authority.
blocked_if: candidate_context_treated_as_accepted_state, Project cache or chat memory used as accepted state, hidden acceptance, hidden update path, legacy/adoption claim without admitted boundary.
```

Stage 2 must not improve, rewrite, or decide the Direction Spine. It may only prepare candidate context and unresolved questions for the selected next procedure.

### Stage 3 - Next Definition Step Selection

```text
stage_id: next_definition_step_selection
stage_type: material stage
purpose: Select exactly one next semantic definition step.
inputs: Stage 1 launch admission, Stage 2 context classification, registry mapping, downstream procedure source, prerequisite context.
required_stage_result: selected_next_definition_step, selected_next_procedure_path, selected_next_step_status, why_this_step_now, rejected_or_deferred_next_steps, downstream_procedure_availability, source_limitations.
gate: PASS if exactly one registered next step is selected and justified; PASS_WITH_RISK if the selected step is correct but downstream procedure body is still a stub and the limitation is explicit; STOP if no registered next step is available, more than one step is selected, or prerequisite context is missing for an exceptional step.
utility_allowed_if: Bounded exact source verification is required to resolve downstream procedure availability.
blocked_if: no_registered_next_step, multiple_next_steps_selected, hidden_run_switch, selected_downstream_source_missing, selected_downstream_source_conflicting.
```

Default selection rule:

```yaml
default_next_step:
  entrypoint: form_direction_spine
  procedure_path: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
  selected_when:
    - setup-only root exists
    - semantic definition is pending
    - no accepted Direction Spine exists
    - form_direction_spine is registered
    - no admitted exceptional boundary selects a later step
```

Exceptional selection rules:

```yaml
exceptional_next_steps:
  form_direction_map:
    allowed_only_if:
      - candidate or accepted Spine context exists
      - explicit admitted boundary selects Map formation
      - Map procedure source is registered and available
    otherwise: defer
  form_active_front:
    allowed_only_if:
      - Direction Map / Goal Evidence Graph context exists
      - explicit admitted boundary selects Active Front formation
      - Active Front procedure source is registered and available
    otherwise: defer
```

Stage 3 must not execute the selected next procedure.

### Stage 4 - Direction Spine Readiness Preview

```text
stage_id: direction_spine_readiness_preview
stage_type: material stage
purpose: When the selected next step is form_direction_spine, preview whether the next procedure has enough candidate context to work from explicit signals rather than intuition.
activation condition: selected_next_definition_step == form_direction_spine.
inputs: Candidate context, source limitations, Direction Spine Formation procedure source.
required_stage_result: readiness_status, readiness_signals, gaps_to_pass_forward, anti_intuition_notes, source_limitations.
gate: PASS if readiness signals are explicit and no candidate Spine content is created; PASS_WITH_RISK if sufficient launch context exists but gaps must be carried forward; STOP if minimum context is absent or the preview starts forming Spine content.
utility_allowed_if: Bounded source/check/research is required to classify a material uncertainty and the child-call gate passes.
blocked_if: preview_generates_candidate_spine, user_first_phrasing_accepted_as_final, roadmap_or_backlog_generated, readiness_score_replaces_spine_formation, downstream_procedure_executed_inside_definition.
```

Readiness preview fields:

```yaml
direction_spine_readiness_preview:
  status: ready_for_form_direction_spine | ready_with_unresolved_questions | blocked_missing_minimum_context | blocked_downstream_procedure_body_not_authored
  signals:
    root_outcome_signal: present | missing | needs_elicitation
    success_dimensions_signal: present | missing | needs_elicitation
    constraints_signal: present | missing | needs_elicitation
    non_goals_signal: present | missing | needs_elicitation
    proof_indicators_signal: present | missing | needs_elicitation
    failure_modes_signal: present | missing | needs_elicitation
    open_uncertainties_signal: present | missing | needs_elicitation
  gaps_to_pass_forward:
  forbidden_interpretation: readiness preview is not candidate Direction Spine content
```

Allowed preview examples:

- “Candidate context appears to contain a possible root-outcome signal, but Spine Formation must derive and test the candidate.”
- “Proof indicators are missing and should be elicited by Spine Formation.”
- “Open uncertainties must be carried forward; do not invent answers here.”

Forbidden preview examples:

- “The Direction root outcome is X.”
- “The accepted success dimensions are A/B/C.”
- “The Active Front should be Y.”
- “The roadmap/backlog should include these tasks.”

If the selected next step is not `form_direction_spine`, mark this stage `not_applicable` with evidence and continue to Stage 5.

### Stage 5 - Next-Step Packet and Closure

```text
stage_id: next_step_packet_and_closure
stage_type: material stage
purpose: Return the bounded Direction Definition result and closure evidence.
inputs: Stage 1-4 outputs, selected next procedure source, readiness preview when applicable, return destination.
required_stage_result: direction_definition_next_step_packet_or_blocked_result, selected_next_procedure, transfer_packet_or_NEXT_CHAT_CARD_content, source_limitations, residual_risks, CLOSURE_CHECK.
gate: PASS if output satisfies the completion contract and no child calls are open; PASS_WITH_RISK if the selected next step is correct but downstream procedure is not authored and the blocked continuation is explicit; STOP if required packet fields, source evidence, selected-step boundary, or closure proof is missing.
utility_allowed_if: Required child/adaptor work is needed for current-goal verification and can be bounded.
blocked_if: selected_next_step_missing, selected_next_step_count_not_one, packet_boundary_incomplete, open_child_calls, missing_required_validation_or_evidence, hidden_procedure_switch, package_or_card_used_as_only_completion.
```

## Direction Definition Next-Step Packet

The primary output is:

```yaml
direction_definition_next_step_packet:
  packet_version: direction_definition_next_step_packet.v1
  produced_by:
    entrypoint: launch_direction_definition
    procedure_path: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
    procedure_boundary: formation_chat
  source_basis:
    registry_ref:
    setup_root_status_ref:
    current_status_ref:
    current_next_move_ref:
    selected_downstream_procedure_ref:
  setup_check:
    setup_only_root_status:
    semantic_definition_status:
    current_next_move:
    launch_admission_status:
  context_classification:
    accepted_context:
    candidate_context:
    rejected_authority_sources:
    unresolved_or_unknown:
  selected_next_step:
    entrypoint:
    procedure_path:
    selection_reason:
    prerequisite_status:
    downstream_procedure_status:
    selected_step_count: 1
  direction_spine_readiness_preview:
    included_when: selected_next_step.entrypoint == form_direction_spine
    readiness_status:
    readiness_signals:
    gaps_to_pass_forward:
    forbidden_interpretation: not_candidate_spine_content
  continuation:
    transfer_packet:
      target_entrypoint:
      target_procedure_path:
      allowed_context_to_pass:
      required_inputs_for_next_chat:
      acceptance_boundary:
      return_destination:
    next_chat_card:
      title:
      why:
      main_procedure_to_start:
      context_to_paste:
      expected_result:
      evidence_or_return_needed:
      start_instruction:
  limitations:
  residual_risks:
```

If the selected downstream procedure is still `stub_procedure_pending_authoring`, the result must be explicit:

```yaml
blocked_downstream_procedure_body_not_authored:
  selected_next_step:
  selected_next_procedure_path:
  reason: PROCEDURE_BODY_NOT_AUTHORED
  semantic_definition_result_status: blocked_after_selection
  next_required_maintenance:
    main_procedure_to_start: author_workflow_procedure
    target_file:
    expected_result: authored downstream procedure body
```

## Child / Adapter Policy

```text
child_call_policy:
  allowed_when:
    - exact source access or verification cannot be completed in the current chat;
    - bounded source conflict check is required;
    - bounded research/check is required for a material non-obvious method or evidence gap;
    - repository/runtime mutation is separately admitted and exact write boundaries, validation, and return verification are present.
  common_targets:
    - GitHub/file access for exact source;
    - check job for source conflict;
    - child research only when genuinely required;
    - Codex/storage only for separately admitted bounded mutation.
  forbidden_when:
    - to run form_direction_spine as a hidden child;
    - to generate Spine, Map, Active Front, Work Graph, Work Contract, roadmap, backlog, or product content;
    - to accept semantic state;
    - to persist runtime state without storage/update authority;
    - to avoid producing a required Transfer Packet or NEXT_CHAT_CARD;
    - to switch the selected main procedure during RUN.
  return_verification:
    - returned evidence must match the child call;
    - returned evidence is evidence only, not accepted state by itself;
    - branch, commit, changed files, validation, EOF, and source evidence must be verified when applicable.
  same_main_procedure_resume: true
```

`open_child_calls != empty`, missing child return, unverified child return, or missing required validation/evidence blocks CHECK, FINISH, and CLOSED.

## Optional Expansion

Allowed expansion is limited to:

- exact source inspection;
- bounded binding/status/next-move verification;
- bounded source conflict checks;
- bounded research/check only when genuinely required to resolve a material non-obvious evidence issue;
- preparing a Transfer Packet or NEXT_CHAT_CARD for the selected single next step.

Expansion must remain subordinate to `launch_direction_definition`.

Expansion must not:

- run a downstream core procedure;
- create downstream candidate semantic artifacts;
- create a second route authority;
- create accepted state;
- create a new mandatory check-file layer;
- broaden into roadmap, backlog, Work Graph, Work Contract, or product execution.

## Research Policy

Research is not required by default.

Use this posture:

- `forbidden`: ordinary source/status/next-step routing where internal Workflow v3 sources are sufficient.
- `optional`: method sanity check for non-obvious readiness criteria, only if it does not delay or complicate the launch boundary.
- `required`: only when a material external/current evidence gap directly blocks next-step selection and cannot be resolved by exact internal source inspection.

When research is required, open a visible `CHILD_PROCEDURE_CALL` with bounded research questions, expected return, and verification. Do not perform hidden research and do not use research to form the Spine inside this procedure.

## Checkpoint Policy

No checkpoint is required for the ordinary `form_direction_spine` selection when setup-only root, current status, current next move, and registry mapping are consistent.

Checkpoint or stop when:

- setup/status/next-move evidence conflicts;
- a non-default next step is proposed;
- candidate context is too sparse or ambiguous to launch Spine Formation;
- downstream procedure source is missing or still not authored;
- source authority depends on legacy/adoption evidence;
- child/adaptor work is required;
- the operator asks to persist or accept semantic state.

## Quality Checks

- Procedure uses no `workflow_v3/evals/**` source and does not recreate a separate eval layer.
- Setup-only root status is read or exact limitation is reported.
- `CURRENT_STATUS` and `CURRENT_NEXT_MOVE` are read from exact/admitted sources or verified accepted excerpts before semantic routing.
- `CURRENT_STATUS` confirms `setup_only_root_created` and semantic definition pending/candidate-only, or blocked status is explicit.
- `CURRENT_NEXT_MOVE` confirms `launch_direction_definition`, or admitted repair/adoption boundary is explicit.
- Candidate context remains candidate-only.
- Exactly one next semantic step is selected.
- Default next step is `form_direction_spine` unless a verified exceptional boundary exists.
- Direction Spine readiness preview does not create candidate Spine content.
- Direction Map and Active Front are deferred unless prerequisite context and separate admitted boundary exist.
- No roadmap, backlog, Work Graph, Work Contract, product execution, acceptance, or persistence is created.
- Transfer Packet / NEXT_CHAT_CARD is continuation only and not proof that downstream work happened.
- Required child/adaptor calls are visible, bounded, returned, and verified before reliance.
- `CLOSURE_CHECK` compares actual result to this procedure's completion contract.

## Stop Conditions

Stop with an explicit blocked result when any of these occur:

- setup-only root is missing;
- setup-only root status conflicts with semantic definition launch;
- `CURRENT_STATUS` cannot be read or verified;
- `CURRENT_NEXT_MOVE` cannot be read or verified;
- `CURRENT_NEXT_MOVE` is not `launch_direction_definition` and no admitted repair/adoption boundary exists;
- return destination is missing;
- source authority conflicts;
- candidate context is treated as accepted state;
- a legacy/adoption claim is needed but not admitted;
- no registered next semantic step is available;
- more than one next semantic step is selected;
- `form_direction_map` or `form_active_front` is selected without prerequisite context and admitted boundary;
- downstream procedure source is missing or conflicting;
- downstream procedure body is not authored and blocked continuation is not explicit;
- Direction Definition starts forming or accepting Spine, Map, Active Front, Work Graph, Work Contract, roadmap, backlog, or product work;
- required child/adaptor return is missing or unverified;
- repository/runtime mutation is requested without admitted storage/update or child/adaptor write boundary;
- the output is only a handoff, package, card, child-call packet, or NEXT_CHAT_CARD without satisfying or explicitly blocking this procedure's completion contract.

## Procedure Closure

Close with one of:

- `direction_definition_next_step_packet` for exactly one selected next semantic definition procedure;
- `blocked_downstream_procedure_body_not_authored` when the correct next procedure is selected but cannot execute yet;
- explicit blocked result naming exact missing setup, source, admission, selected-step, downstream-procedure, child-return, or packet boundary.

Closure must include:

```yaml
CLOSURE_CHECK:
  selected_entrypoint: launch_direction_definition
  selected_procedure_path: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
  completion_contract:
  actual_result:
  setup_only_root_check:
  current_status_read_check:
  current_next_move_read_check:
  context_classification_check:
  selected_next_step_check:
  selected_next_step_count_check:
  downstream_boundary_check:
  candidate_only_check:
  child_return_status:
  source_limitations:
  residual_risks:
  gaps:
  decision: pass | pass_with_risk | blocked
```

FINISH may close only after CHECK passes or the blocked completion condition is explicit, with no open, missing, or unverified required child returns.

NEXT_CHAT_CARD is post-closed continuation only. It must not represent unfinished child work from the current START goal.

Ordinary successful continuation:

```yaml
NEXT_CHAT_CARD:
  title: Form Direction Spine
  why: Direction Definition selected form_direction_spine as the next semantic definition step.
  main_procedure_to_start: form_direction_spine
  context_to_paste: Direction Definition next-step packet and candidate context.
  expected_result: candidate Direction Spine package or explicit blocked result.
  evidence_or_return_needed: setup/status/next-move evidence, candidate context, acceptance boundary, and source limitations.
  start_instruction: START with form_direction_spine.
```

Downstream procedure not authored continuation:

```yaml
NEXT_CHAT_CARD:
  title: Author Direction Spine Formation procedure body
  why: Direction Definition selected form_direction_spine, but the downstream procedure body is not authored.
  main_procedure_to_start: author_workflow_procedure
  context_to_paste: DIRECTION_SPINE_FORMATION_PROCEDURE.md target role, future body scope, must-not constraints, and Direction Definition next-step packet.
  expected_result: active DIRECTION_SPINE_FORMATION_PROCEDURE.md body.
  evidence_or_return_needed: updated downstream procedure source with completion block and quality checks.
  start_instruction: START with author_workflow_procedure for DIRECTION_SPINE_FORMATION_PROCEDURE.md.
```

If no continuation is needed, return:

```yaml
no_next_chat_needed:
  reason:
```

END_OF_FILE: workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md
