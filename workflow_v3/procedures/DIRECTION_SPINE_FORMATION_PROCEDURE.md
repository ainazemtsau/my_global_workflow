# Procedure: Direction Spine Formation

title: Direction Spine Formation
status: active_procedure
canonical_location: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
entrypoint: form_direction_spine
run_surface_type: formation_chat
procedure_class: core_material
embedded_use_policy: may_use_global_utility_layer

## Purpose

Direction Spine Formation forms a candidate Direction Spine that defines what success means for one Direction.

It produces the candidate semantic axis for later Direction Map and Goal Evidence Graph formation: root outcome, success dimensions, constraints, non-goals, failure modes, proof indicators, and open uncertainties.

It is not a roadmap, backlog, implementation plan, product execution plan, Direction Map, Goal Evidence Graph, Active Front, Work Graph, or Work Contract.

The output is candidate only until explicit acceptance/update authority accepts and persists it through a separate admitted path.

## Trigger / When to Use

Use this procedure when all apply:

- START selected `form_direction_spine`;
- Direction Definition or an admitted Next Move selected Direction Spine formation;
- no accepted Direction Spine exists, or accepted authority explicitly requests candidate Spine revision;
- candidate Direction context is available or the procedure can ask for minimal missing context;
- a candidate root success axis is needed before Direction Map or Goal Evidence Graph formation.

## When Not to Use

Do not use this procedure to:

- create Direction Map;
- create Goal Evidence Graph;
- select Active Front;
- create Work Graph;
- create Work Contract;
- execute product work;
- produce an implementation plan;
- produce a roadmap or backlog;
- accept or persist candidate Spine output;
- import legacy evidence as accepted state;
- treat the first user phrasing as final or accepted.

## Required Inputs

- `direction_id`;
- source authority and repository ref;
- setup-only root context or Direction Definition result/context;
- `candidate_context_for_direction_definition` if available;
- current human input;
- known constraints or user goals if supplied;
- relevant accepted records if any;
- return destination;
- acceptance boundary.

## Source Requirements

Before material output, read exact sources needed for formation:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`;
- `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md`;
- matching `formation_chat` run surface contract in `workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md`;
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md` when utility, check, child, research, handoff, or return boundaries are involved;
- Direction Definition result or launch packet when supplied;
- setup-only `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md` when formation depends on a runtime root;
- accepted Direction Spine only when this is a revision or update case;
- relevant candidate context;
- `workflow_v3/templates/DIRECTION_SPINE_TEMPLATE.md` only when field shape is needed.

Missing, truncated, stale, unreadable, or authority-conflicting sources must produce a blocked result or context request. If a source has an `END_OF_FILE` marker, verify it before relying on the read.

## Context Classification

Classify context before deriving the candidate Spine:

- exact repository sources at resolved ref are `canonical_repository_source`;
- accepted Direction records are `accepted_record` only when explicit accepted evidence exists;
- user goals, outcomes, constraints, and product ideas are `current_human_input` and `candidate_context`;
- old `directions/**` files are `legacy_evidence` only;
- Project Files/Sources, project title, uploads, pasted excerpts, previous chat memory, and summaries are cache/context unless verified against exact repository state;
- prior Direction Definition outputs are `candidate_context` unless accepted;
- research/check/child results are `adapter_evidence` or `candidate_context` until integrated and accepted by a later path.

Never promote current human input, candidate context, adapter evidence, or legacy evidence into accepted Direction state inside this procedure.

## Complexity Selector

- `simple`: user supplied enough candidate context for a compact candidate Spine and no source conflicts exist.
- `standard`: multiple inputs need synthesis, alternatives, criteria, risks, and evidence gaps.
- `checkpointed`: root outcome, success dimensions, constraints, or non-goals are ambiguous or high-impact.
- `delegated_or_tool_mediated`: a bounded check job or child research/check is required for source/evidence consistency or domain framing.
- `research_backed`: external/current research is required only when the user asks for it or when forming a high-impact Spine depends on non-obvious external market, domain, legal, or technical facts.

Use the smallest complexity that can produce a bounded candidate Spine and explicit acceptance question.

## Stage Cards

```text
stage_id: source_lock_and_fit
purpose: Confirm the request belongs to form_direction_spine and lock source authority.
activation conditions: Always active at RUN start.
inputs: START packet, Procedure Registry entry, this procedure source, formation_chat run surface contract, source authority/ref, Direction Definition context or launch packet, user request.
required intermediate output: source lock, entrypoint fit, run_surface_type fit, read limitations, accepted/candidate context boundary.
gate: PASS if entrypoint/source/run surface match and exact sources are readable. STOP on missing source, wrong entrypoint, product execution, state mutation request, or source authority conflict.
checkpoint rule: Checkpoint only when source authority or entrypoint fit is ambiguous.
expansion rule: EXPAND only to exact source inspection or a bounded source/evidence consistency check.
stop behavior: Return SOURCE_INTEGRITY_STOP, UNREGISTERED_ACTION_EXCEPTION, BOUNDARY_CROSSING_STOP, or WRITE_NOT_ADMITTED with exact reason.
```

```text
stage_id: context_intake_and_classification
purpose: Gather and classify candidate Direction context.
activation conditions: source_lock_and_fit passed.
inputs: current human input, candidate_context_for_direction_definition, Direction Definition result/context, accepted records if any, setup-only context, source limitations.
required intermediate output: context_classification, candidate_context_summary, accepted_record_refs, evidence_gaps, minimum missing context if blocked.
gate: PASS if enough candidate context exists to generate alternatives. PASS_WITH_RISK if context is sparse but a bounded candidate can be drafted with limitations. STOP if context is insufficient and no useful candidate can be formed.
checkpoint rule: Checkpoint when sparse or conflicting context would materially affect the root outcome.
expansion rule: EXPAND only to bounded source/evidence checks or minimal context request.
stop behavior: Return CONTEXT_REQUEST, SOURCE_AUTHORITY_CONFLICT, or LEGACY_BOUNDARY_STOP.
```

```text
stage_id: success_axis_discovery
purpose: Identify possible root outcome candidates, success dimensions, constraints, non-goals, failure modes, proof indicators, and open uncertainties.
activation conditions: context_intake_and_classification passed or passed with risk.
inputs: candidate context summary, accepted records, evidence gaps, constraints, user goals, known non-goals.
required intermediate output: candidate success axes, alternatives considered, assumptions, evidence gaps, contradiction list, risk list.
gate: PASS if at least one candidate success axis plus alternatives or limitations exists. REWORK if the output becomes roadmap, backlog, product plan, or task list.
checkpoint rule: Checkpoint when alternatives expose materially different Direction meanings.
expansion rule: EXPAND to bounded child research/check only when evidence or domain framing is required before a candidate can be responsibly formed.
stop behavior: Return VALIDATION_REQUIRED_STOP or CONTEXT_REQUEST when no bounded candidate axis can be produced.
```

Discovery requirements:

- do not lock the first user phrasing;
- generate alternatives unless the case is trivial or blocked;
- name assumptions and evidence gaps;
- separate success meaning from implementation sequence.

```text
stage_id: criteria_and_tradeoff_frame
purpose: Define criteria before selecting the candidate Spine.
activation conditions: success_axis_discovery produced at least one candidate axis.
inputs: alternatives, constraints, evidence gaps, failure modes, proof indicators, user supplied priorities.
required intermediate output: criteria list, tradeoff frame, selection risks, reject/defer policy.
gate: PASS if selection criteria are explicit. STOP if selection would be intuition-only.
checkpoint rule: Checkpoint when criteria conflict or user confirmation is required before selection.
expansion rule: EXPAND only to bounded check/research for criteria that depend on current external facts.
stop behavior: Return VALIDATION_REQUIRED_STOP or ACCEPTANCE_AMBIGUITY.
```

Criteria examples:

- user value;
- build feasibility;
- business or strategic viability;
- maintainability;
- risk exposure;
- evidenceability;
- reversibility;
- fit to stated constraints.

```text
stage_id: candidate_spine_selection
purpose: Select or synthesize one candidate Direction Spine from alternatives.
activation conditions: criteria_and_tradeoff_frame passed.
inputs: criteria, alternatives, candidate context, source basis, risk list, evidence gaps.
required intermediate output: candidate Direction Spine package draft with root_outcome, success_dimensions, constraints, non_goals, failure_modes, proof_indicators, open_uncertainties, alternatives considered, and rejected/deferred alternatives.
gate: PASS if candidate Spine is bounded and traceable. PASS_WITH_RISK if evidence gaps are explicit. REWORK if it includes roadmap, backlog, Work Graph, Work Contract, product execution, or hidden acceptance.
checkpoint rule: Checkpoint when rejected alternatives are plausible and materially change the Direction.
expansion rule: No expansion into Map, Front, Work Graph, Work Contract, or execution.
stop behavior: Return REWORK or STOP with exact boundary failure.
```

```text
stage_id: anti_flattening_and_risk_review
purpose: Prevent technical-only collapse, convenience-track selection, hidden roadmap, and overfit to user impulse.
activation conditions: candidate_spine_selection produced a draft.
inputs: candidate Spine draft, success dimensions, alternatives, deferred items, constraints, evidence gaps, failure modes.
required intermediate output: anti_flattening_review, contradiction review, deferred dimension triggers, risk gates, overfit review.
gate: PASS if anti-flattening checks pass. REWORK if candidate is too narrow, too broad, single-track collapsed, hollow, or hiding commitments.
checkpoint rule: Checkpoint when a deferred dimension could invalidate the root outcome.
expansion rule: EXPAND only to bounded red-team or evidence check.
stop behavior: Return REWORK with repair target or STOP if a non-hollow candidate cannot be formed.
```

Required checks:

- success dimensions are not collapsed into one convenient track;
- deferred dimensions have reason and review trigger;
- contradictions are named;
- risk gates and evidence gaps are visible;
- the candidate does not merely restate the user's impulse.

```text
stage_id: candidate_package_and_acceptance_question
purpose: Produce candidate Direction Spine package and explicit acceptance/revision question.
activation conditions: anti_flattening_and_risk_review passed or passed after rework.
inputs: candidate Spine, source basis, context classification, evidence gaps, anti-flattening review, return destination, acceptance boundary.
required intermediate output: candidate_direction_spine_package, acceptance_question, Result Packet, Next Move Packet.
gate: PASS if output contract is complete. STOP if acceptance or persistence is implied.
checkpoint rule: None by default after package completion.
expansion rule: No expansion after candidate package except repair of missing fields.
stop behavior: Return blocked Result Packet and exact next move.
```

```text
stage_id: closure
purpose: Close selected procedure with FINISH_REQUEST readiness.
activation conditions: candidate_package_and_acceptance_question passed or stopped with blocked result.
inputs: stage outputs, unresolved questions, result packet, next move packet, external handoff status.
required intermediate output: FINISH_REQUEST readiness and exact next move.
gate: PASS if no pending external return and exact next move exists.
checkpoint rule: None.
expansion rule: No expansion after closure.
stop behavior: Return blocked closure with source/read limitations and exact blocking reason.
```

## Gate Outcomes

Allowed gate outcomes:

- `PASS`;
- `PASS_WITH_RISK`;
- `REWORK`;
- `EXPAND`;
- `STOP`;
- `TRANSFER`;
- `RUN_EXTERNAL_HANDOFF`;
- `RUN_EXTERNAL_RETURN`.

`RUN_EXTERNAL_HANDOFF` is allowed only for bounded supporting check or research evidence needed before closure, and must resume the same selected `form_direction_spine` owner RUN.

## Optional Expansion

Allowed expansion:

- exact source inspection;
- bounded `check_job_packet` for source/evidence consistency;
- bounded `child_research_packet` only when supporting research is needed to form or stress-test the Spine;
- bounded `child_chat_packet` for alternative generation or red-team review when scoped.

Not allowed expansion:

- product execution;
- roadmap or backlog generation;
- Work Graph or Work Contract creation;
- Direction Map, Goal Evidence Graph, or Active Front formation;
- persistence or acceptance;
- unbounded market/product research.

## Research Policy

Research is not mandatory by default.

Research status:

- `forbidden`: candidate context and internal sources are enough for a safe candidate Spine.
- `optional`: research could improve domain realism but is not required for a candidate.
- `required`: the user explicitly asks for research, or the Spine would depend on current external facts, market facts, legal constraints, or technical constraints that cannot be safely assumed.

If research is required, do not silently research or continue. Return bounded research questions/evidence plan or a `child_research_packet` under the Utility Use Gate.

## Utility / Adapter Policy

common_utility_choices:
- `check_job_packet` for source/evidence consistency;
- `child_research_packet` for bounded external/domain support;
- `child_chat_packet` for bounded alternative generation or red-team review;
- `project_refresh_instruction_packet` for reporting only.

forbidden_utility_categories:
- `codex_handoff_packet` for product implementation;
- `storage_update_package` unless acceptance/update authority is explicit and separately admitted;
- any utility that creates Direction Map, Goal Evidence Graph, Active Front, Work Graph, Work Contract, product roadmap, or execution work inside this RUN.

external_handoff_policy:
- use `RUN_EXTERNAL_HANDOFF` only when an allowed utility result is required before the candidate Spine can close;
- handoff must include complete `copy_paste_packet`, expected return packet, validation required on return, and same-owner resume rule.

external_return_policy:
- `RUN_EXTERNAL_RETURN` must match the emitted handoff and resume `form_direction_spine`, not a new owner procedure.

embedded_verification_policy:
- returned check/research/child output is adapter evidence or candidate context only and must be integrated before reliance.

storage_boundary:
- this procedure must not mutate repository/runtime state directly;
- persistence requires a separate accepted update path.

## Checkpoint Policy

No checkpoint is required for a clean simple run where candidate context is sufficient and risk is low.

Checkpoint when:

- root outcome is ambiguous or high-impact;
- success dimensions conflict or are under-specified;
- constraints or non-goals materially change the candidate Spine;
- one candidate would collapse the Direction into a single convenient track;
- a bounded utility result changes source/evidence context;
- the candidate package cannot be completed without repair.

Checkpoints are internal RUN gates and must not switch owner procedure or start another material lifecycle.

## Output Contract

Return this shape:

```text
candidate_direction_spine_package:
  status:
  direction_id:
  source_basis:
  context_classification:
  root_outcome:
  success_dimensions:
  constraints:
  non_goals:
  failure_modes:
  proof_indicators:
  open_uncertainties:
  alternatives_considered:
  rejected_or_deferred_alternatives:
  evidence_gaps:
  anti_flattening_review:
  acceptance_question:
  source_read_limitations:
  result_packet:
  next_move_packet:
```

Next Move default:

```text
next_move_type: human_decision
primary_next_move: accept/revise/reject candidate Direction Spine
acceptance_boundary: candidate Spine is not accepted until explicit Acceptance Decision / update path.
```

If the user explicitly asks for the next procedure after candidate Spine and acceptance is not yet resolved, the next move should still be human_decision or an admitted acceptance review, not `form_direction_map` by implication.

## Eval / Quality Checks

- START selected exactly one owner procedure: `form_direction_spine`.
- Procedure Registry, this procedure source, matching run surface contract, required context, and relevant template shape were read or limitations were stated.
- First user phrasing was not treated as final/accepted.
- Alternatives were generated or a no-alternatives reason was stated.
- Criteria were defined before candidate selection.
- Candidate package includes root_outcome, success_dimensions, constraints, non_goals, failure_modes, proof_indicators, and open_uncertainties.
- Evidence gaps and source limitations are explicit.
- Anti-flattening / no single-track collapse review was performed.
- Roadmap, backlog, Work Graph, Work Contract, Direction Map, Goal Evidence Graph, Active Front, and product execution content were cut.
- Acceptance question is present.
- No persistence or acceptance occurred.
- Map/Front are not launched by implication.
- FINISH_REQUEST is emitted before FINISH when lifecycle closure applies.
- FINISH emits FINISH_PACKET, Result Packet, and Next Move Packet with exactly one primary next move.

## Stop Conditions

Stop when any applies:

- required sources are missing, unreadable, truncated, stale, or authority-conflicting;
- wrong entrypoint;
- user demands product work;
- user demands roadmap or backlog;
- user demands Direction Map, Goal Evidence Graph, Active Front, Work Graph, or Work Contract formation;
- candidate context is insufficient to produce a useful candidate;
- legacy evidence is treated as accepted state;
- Project Files/Sources are treated as source authority;
- acceptance or persistence is requested without admitted path;
- multiple independent Directions or goals are mixed without split;
- the procedure would produce a hollow or single-track-collapsed Spine.

## Procedure Closure

Output is candidate only.

This procedure does not mutate, persist, accept, or launch accepted Direction state.

It does not silently launch Direction Map, Goal Evidence Graph, Active Front, Work Graph, Work Contract, or product execution work.

RUN closes with FINISH_REQUEST before FINISH when complete or blocked.

After explicit FINISH, emit FINISH_PACKET, Result Packet, and Next Move Packet. The exact next move is normally human decision or admitted acceptance review for the candidate Spine.

After FINISH, the same chat must not begin a new material START.

END_OF_FILE: workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md
