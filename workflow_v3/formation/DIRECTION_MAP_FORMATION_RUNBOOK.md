# Direction Map Formation Runbook

status: active_formation_runbook

## Purpose

Use `form_direction_map` to form an initial or updated Direction Map candidate for one Direction.

A Direction Map is a foundation steering entity between Direction Spine and Active Front. It must expose structural areas, dependencies, uncertainties, risk zones, and candidate fronts without becoming a roadmap, backlog, Work Graph, Action Inbox, or product execution plan.

This procedure produces candidate output only. It does not accept the Map, persist state, update `CURRENT_STATUS.md`, update `CURRENT_NEXT_MOVE.md`, launch Codex, or continue into another steering entity.

## Trigger / When to Use

- A Direction needs an initial Direction Map candidate.
- A Direction needs an updated Direction Map candidate.
- A Direction Definition sequence explicitly selects Direction Map formation after Spine context is available or admitted as candidate context.
- A lifecycle handler, Launch Packet, accepted Next Move, or bounded human request selects `form_direction_map`.

## When Not to Use

- Do not use to create a roadmap, backlog, task list, Work Graph, Action Inbox, or product execution plan.
- Do not use to form Direction Spine, Active Front, Work Graph, Work Contract, Current Next Move, Acceptance Decision, or Memory Artifact.
- Do not use to accept or persist the Direction Map.
- Do not use when accepted Spine is required but missing and no setup-only Definition sequencing admits candidate Spine context.
- Do not use when map claims cannot be labeled as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown.
- Do not use to import legacy evidence as accepted Workflow v3 state.

## Required Inputs

- `direction_id`;
- accepted Direction Spine, or admitted candidate Spine in setup-only Definition sequencing;
- accepted records, verified excerpts, current human input, and candidate context relevant to the Map;
- known dependencies, uncertainties, risks, and possible fronts;
- source authority and required reads;
- return destination;
- forbidden surfaces and acceptance/update boundary.

## Source Requirements

Read exact source authority for the Direction Spine and any existing Direction Map when applicable.

In setup-only Definition sequencing, read exact `CURRENT_STATUS.md`, `CURRENT_NEXT_MOVE.md`, and the candidate Spine produced by Spine formation if those sources exist or are required by the launch context.

Treat Project Files/Sources, chat memory, snippets, and unverified pasted context as cache/context only. Treat old Workflow OS and old Direction files as `legacy_evidence` unless an explicit accepted import/bridge policy admits them.

If required source is missing, unreadable, stale, truncated, or lacks required EOF, stop or request the exact source rather than inventing Map structure.

## Context Classification

Classify every material Map input and claim as one of:

- accepted;
- candidate;
- unresolved;
- hypothetical;
- legacy_evidence;
- unknown.

Also classify source origin as canonical repository source, accepted record, current human input, verified excerpt, Project Files cache/context, candidate context, legacy_evidence, or unknown/unverified.

A claim without a clear label cannot be promoted into the candidate Map as if it were settled.

## Complexity Selector

Use the smallest level that can satisfy the output contract:

- `standard`: use only when source authority is sufficient, scope is narrow, and the Map update is small enough to form without user-visible intermediate confirmation.
- `checkpointed`: default for initial Maps, major Map updates, or any Map that will become a foundation for Active Front selection.
- `research_backed`: use when material external/current/domain facts affect Map structure and are allowed by the admitted scope.
- `delegated_or_tool_mediated`: use only to propose bounded child research, check job, Codex handoff, or other adapter work; do not launch it without separate admission.
- `inline`: not used for material Direction Map formation.

## Stage Cards

```text
stage_id: fit_and_boundary
purpose: Confirm the selected target is Direction Map only and the run is non-mutating candidate formation.
activation conditions: Always.
inputs: User request, selected entrypoint, run surface, target Direction, return destination.
required intermediate output: Fit Packet with target, non-goals, run-surface boundary, and complexity level.
gate: PASS if target is Direction Map only; STOP if the request asks for another entity, acceptance, persistence, product execution, or multiple independent work items.
checkpoint rule: Checkpoint if target or boundary is ambiguous.
expansion rule: Request clarification only to isolate Direction Map formation.
stop behavior: Return SPLIT_REQUIRED or BOUNDARY_CROSSING_STOP as applicable.
```

```text
stage_id: source_and_context_frame
purpose: Establish source authority and classify all Map inputs before synthesis.
activation conditions: Always after fit_and_boundary passes.
inputs: Direction Spine source, existing Direction Map source if any, accepted records, verified excerpts, current human input, candidate context, legacy material if admitted for review.
required intermediate output: Source Frame listing authoritative sources, candidate/context sources, missing sources, conflicts, labels, and read limitations.
gate: PASS if source authority is sufficient; PASS_WITH_RISK if non-blocking gaps are explicit; EXPAND if bounded source/research/check work is needed; STOP if required Spine/Map authority is missing or claims would be invented.
checkpoint rule: Required when the Map is initial, source authority is partial, or later synthesis would depend on uncertain labels.
expansion rule: Activate bounded research/check/child source inspection only for specific missing evidence questions serving this Map.
stop behavior: Return SOURCE_INTEGRITY_STOP, CONTEXT_REQUEST, or SOURCE_AUTHORITY_CONFLICT.
```

```text
stage_id: map_control_frame
purpose: Define what this Direction Map must control structurally.
activation conditions: source_and_context_frame passes or passes with risk.
inputs: Spine axis, known tracks, dependencies, uncertainties, risks, possible fronts, Direction constraints.
required intermediate output: Map Control Frame naming structural areas, dependency questions, uncertainty zones, candidate front decision needs, and non-map material to cut.
gate: PASS if the Map's control problem is specific and non-backlog; REWORK if it is too generic; STOP if it collapses into roadmap/backlog/task execution.
checkpoint rule: Required for initial Maps and major updates before alternatives are generated.
expansion rule: None except bounded clarification of structural control questions.
stop behavior: Return blocked result explaining why the target is not a Direction Map.
```

```text
stage_id: alternatives_and_criteria
purpose: Generate and compare possible Map structures before selecting a candidate.
activation conditions: map_control_frame passes and the task is not blocked.
inputs: Map Control Frame, source labels, dependencies, uncertainties, risks, possible fronts.
required intermediate output: 2-3 candidate Map structures or area groupings unless blocked, plus selection criteria.
gate: PASS if alternatives are meaningful and criteria include spine alignment, dependency clarity, uncertainty visibility, non-backlog shape, front usefulness, and source labeling; PASS_WITH_RISK if alternatives are constrained by explicit source gaps; REWORK if alternatives are superficial.
checkpoint rule: Required when alternatives materially change downstream Active Front selection.
expansion rule: Add bounded research/check proposal only when alternatives depend on a specific unresolved evidence question.
stop behavior: Return blocked or rework packet if alternatives cannot be produced without invention.
```

```text
stage_id: evidence_hypothesis_attack_and_cuts
purpose: Test candidate Map claims before final synthesis.
activation conditions: alternatives_and_criteria passes.
inputs: Candidate structures, evidence, hypotheses, labels, risks, contradictions, out-of-scope material.
required intermediate output: Evidence/Hypothesis Matrix, risk and contradiction attack, rejected/deferred structures, and focus/waste cuts.
gate: PASS if material claims have labels and weak claims remain visible; REWORK if labels, contradictions, or cuts are missing; STOP if the result is only a task list or false-certainty plan.
checkpoint rule: Required when unresolved assumptions materially affect candidate fronts or risk zones.
expansion rule: Propose bounded check/child research only for material unresolved claims; do not let child work decide the Map.
stop behavior: Return repair_required or blocked_context_request.
```

```text
stage_id: candidate_map_synthesis
purpose: Draft the candidate Direction Map in the required output shape.
activation conditions: evidence_hypothesis_attack_and_cuts passes.
inputs: Selected structure, Map fields, evidence/hypothesis matrix, cuts, rejected/deferred alternatives, source limitations.
required intermediate output: Candidate Direction Map draft with tracks, map areas, strategic dependencies, strategic uncertainties, risk zones, candidate fronts, and accepted/candidate/unresolved/hypothetical labels.
gate: PASS if the draft is coherent, source-labeled, non-backlog, and downstream-usable for Active Front selection; PASS_WITH_RISK if limitations are explicit and non-blocking; REWORK if required fields or labels are missing; STOP if it becomes roadmap/backlog/Work Graph.
checkpoint rule: Required before final output for initial Maps, major updates, or research-backed runs.
expansion rule: None after synthesis except rework of current stage.
stop behavior: Return repair_required with missing fields/labels.
```

```text
stage_id: closure_and_acceptance_question
purpose: Close the formation run without accepting or persisting the candidate Map.
activation conditions: candidate_map_synthesis passes or stops with a bounded result.
inputs: Candidate Map draft or blocked result, evidence, limitations, acceptance boundary, return destination.
required intermediate output: Candidate Map package, acceptance question, Result Packet, Event Loop Closure, and exact next move or Transition Packet.
gate: PASS if closure states candidate status, evidence, read limitations, acceptance need, and one primary next move.
checkpoint rule: None.
expansion rule: TRANSFER only to acceptance_review, check job, child chat, Codex handoff, or storage_update_adapter when separately admitted by the next step.
stop behavior: Return blocked result and exact missing source/scope decision.
```

## Gate Outcomes

- `PASS`: stage output is sufficient to continue or close.
- `PASS_WITH_RISK`: continue only with explicit source/read limitations and residual risks.
- `REWORK`: repair the current stage before continuing.
- `EXPAND`: propose or activate only an admitted bounded research/check/child/source-inspection path serving this Map.
- `STOP`: halt rather than invent, accept, mutate, import legacy state, or cross to another procedure.
- `TRANSFER`: return a complete Transition Packet for the selected next surface; do not launch it invisibly.

## Optional Expansion

Optional expansion is allowed only when a gate cannot pass from current admitted context and the expansion question is bounded.

Allowed expansion forms:

- exact repository source inspection;
- bounded child research/check chat for a specific evidence or consistency question;
- bounded check job;
- candidate Codex handoff only if repository maintenance is separately selected later;
- human decision request when source/acceptance/scope authority is ambiguous.

Expansion must not decide the Map independently, mutate state, accept output, create runtime files, or become a second material procedure inside the same RUN.

## Research Policy

Research is not mandatory by default.

Use research-backed mode only when material external/current/domain facts affect the Map structure and the admitted scope allows that research.

Research findings must remain evidence inputs. They must be separated from interpretation and labeled as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown as applicable.

Do not use external research to infer accepted Direction state, accepted Map state, Project UI state, or repository state.

## Checkpoint Policy

Checkpoints are required for:

- initial Direction Maps;
- major Direction Map updates;
- any Map that will become the foundation for Active Front selection;
- partial or conflicting source authority;
- material alternatives before final candidate selection;
- unresolved assumptions that affect candidate fronts, dependencies, or risk zones;
- any proposed expansion to child/check/research/adapter work.

Do not checkpoint every minor edit. Ordinary stage passes are not Signals by default.

## Output Contract

Return a candidate Direction Map package compatible with the active Direction Map template/interface and containing:

```text
target_entity:
source_context_classification:
frame:
candidate_alternatives:
selection_criteria:
evidence_and_hypotheses:
selected_candidate_summary:
rejected_or_deferred_alternatives:
risk_and_contradiction_attack:
focus_and_waste_cuts:
source_read_limitations:
candidate_entity:
acceptance_question:
event_loop_closure:
exact_next_move_or_transition_packet:
```

The `candidate_entity` must include:

```text
tracks:
map_areas:
strategic_dependencies:
strategic_uncertainties:
risk_zones:
candidate_fronts:
accepted_candidate_unresolved_hypothetical_labels:
```

## Eval / Quality Checks

- Uses this runbook and obeys `formation_chat` run-surface boundaries.
- Forms tracks, map areas, strategic dependencies, strategic uncertainties, risk zones, candidate fronts, and status/source labels.
- Labels material claims as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown.
- Generates 2-3 alternative Map structures unless blocked with explicit reason.
- Includes selection criteria, evidence/hypotheses, risks, contradiction attack, cuts, rejected/deferred structures, acceptance question, Event Loop Closure, and exact next move.
- Does not become roadmap, backlog, Work Graph, Action Inbox, task list, or product execution plan.
- Does not accept, persist, mutate, update status/next move, launch Codex, or continue into another steering entity.
- Performs required checkpoints for foundation or uncertain Map work.
- Stops rather than inventing source authority or unlabeled Map claims.

## Stop Conditions

Stop if:

- accepted Spine is missing and the package does not admit candidate Definition sequencing;
- required source authority is missing, unreadable, conflicting, stale, truncated, or EOF-invalid;
- Map claims cannot be labeled;
- the result is only a task list, roadmap, backlog, Work Graph, or product execution plan;
- user asks to form another steering entity in the same RUN;
- user asks to accept, persist, mutate, or update repository/runtime state;
- legacy evidence pressure appears without accepted import/bridge policy;
- child/check/research work would decide the Map independently;
- closure would require hidden next-step launch.

## Acceptance Boundary

The Direction Map remains candidate until explicit Acceptance Decision or accepted update path.

After acceptance-like human input, stop with a Transition Packet to `acceptance_review` / `storage_update_adapter`. Do not create acceptance records, mutate repository state, update `CURRENT_STATUS.md`, update `CURRENT_NEXT_MOVE.md`, persist Event Loop Closure files, launch Codex, or continue across role boundary.

## Procedure Closure

Return the candidate Direction Map or blocked result with evidence, source/read limitations, acceptance question, Event Loop Closure, and exact next move or Transition Packet.

If lifecycle FINISH is active, close through FINISH_REQUEST, Result Packet, and Event Loop Closure. The final closure must select exactly one primary next move and must not launch it invisibly.

END_OF_FILE: workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md