# Direction Map Formation Eval

status: active_eval

## Purpose

Validate Direction Map formation quality after `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md` was migrated into the Procedure Definition Framework.

This eval checks both the Direction Map artifact and the procedure execution discipline used to produce it.

## Source files to inspect

- `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md`
- `workflow_v3/interfaces/02_DIRECTION_MAP_INTERFACE.md`
- `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`
- `workflow_v3/formation/ENTITY_FORMATION_CANON.md`
- `workflow_v3/evals/PROCEDURE_DEFINITION_EVAL.md`
- `workflow_v3/evals/PROCEDURE_EXECUTION_EVAL.md`
- exact source/evidence files named by the admitted Direction Map run

## Evidence required

- selected entrypoint and run surface;
- source/context frame;
- complexity level and checkpoint policy;
- stage outputs or skipped-stage reasons;
- gate outcomes;
- expansion/research/child/check outputs when used;
- candidate Direction Map package;
- acceptance question;
- Result Packet and Event Loop Closure;
- exact next move or Transition Packet.

## PASS checks

- START selected `form_direction_map` as exactly one entrypoint.
- RUN used `workflow_v3/formation/DIRECTION_MAP_FORMATION_RUNBOOK.md` and obeyed `formation_chat` run-surface boundaries.
- Complexity level was justified, with `checkpointed` used for initial Maps, major updates, or Maps that become foundation for Active Front selection.
- Source/context frame classified material inputs and claims as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown.
- Required source authority for Direction Spine and any existing Direction Map was read, or missing/unreadable sources were named as blockers.
- Stage Cards were executed or skipped with reasons: `fit_and_boundary`, `source_and_context_frame`, `map_control_frame`, `alternatives_and_criteria`, `evidence_hypothesis_attack_and_cuts`, `candidate_map_synthesis`, and `closure_and_acceptance_question`.
- Gates were applied visibly enough for review and used real outcomes: `PASS`, `PASS_WITH_RISK`, `REWORK`, `EXPAND`, `STOP`, or `TRANSFER`.
- Required checkpoints occurred for foundation or uncertain Map work.
- Generates 2-3 alternative Map structures or area groupings unless blocked with explicit reason.
- Defines selection criteria including spine alignment, dependency clarity, uncertainty visibility, non-backlog shape, front usefulness, and source labeling.
- Includes evidence/hypotheses, risks, contradiction attack, focus/waste cuts, and rejected/deferred structures.
- Candidate entity is compatible with `workflow_v3/templates/DIRECTION_MAP_TEMPLATE.md`.
- Forms tracks, map areas, strategic dependencies, strategic uncertainties, risk zones, candidate active fronts, accepted/closed fronts where applicable, blocked areas, evidence links, and label blocks.
- Labels material claims as accepted, candidate, unresolved, hypothetical, legacy_evidence, or unknown.
- Includes acceptance question, Result Packet, Event Loop Closure, and exact next move or Transition Packet.
- Direction Map remains candidate until explicit Acceptance Decision or accepted update path.
- No repository/runtime state is mutated.
- No acceptance record is created by the formation chat.
- No Codex, child chat, check job, storage update, or next material procedure is launched invisibly.

## WARN checks

- Some Map claims are unresolved but clearly labeled and carried as residual risk.
- Alternatives are constrained by explicit source gaps but still materially different.
- Source limitations are non-blocking and clearly stated.
- A checkpoint was collapsed into a single response only because the admitted scope was narrow and not foundation-forming.
- Candidate fronts are provisional pending acceptance.

## FAIL checks

- Procedure selection or execution switches from Direction Map into another steering entity.
- Formation chat creates or implies accepted Direction Map state.
- Map is a roadmap, backlog, task list, Work Graph, Action Inbox, or product execution plan.
- Labels and source discipline are missing.
- Map claims are presented as settled without accepted source/evidence or explicit candidate/unresolved/hypothetical labeling.
- Required source authority is missing but the Map is synthesized anyway.
- 2-3 alternatives are omitted without a blocked reason.
- Required checkpoints are skipped for an initial, major, or foundation Map.
- Gate failures are ignored and final output is produced anyway.
- Research, child chat, check job, or external/tool work decides the Map independently.
- Work Graph nodes are mixed into Direction Map.
- Acceptance-like input is treated as storage authorization.
- Repository/runtime files are mutated inside formation chat.
- Closure launches acceptance review, storage update, Codex, child/check job, or next material work invisibly.

## Output contract checks

The result must include the formation wrapper from `ENTITY_FORMATION_CANON.md`:

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

The `candidate_entity` must include fields compatible with `DIRECTION_MAP_TEMPLATE.md`:

```text
direction_id:
map_status:
formation_runbook_ref:
formation_eval_ref:
source_spine_ref:
map_claim_discipline:
tracks:
map_areas:
strategic_dependencies:
strategic_uncertainties:
candidate_active_fronts:
accepted_or_closed_fronts:
blocked_areas:
risk_zones:
evidence_links:
accepted_labels:
candidate_labels:
unresolved_labels:
hypothetical_labels:
update_candidates:
acceptance_decision_ref:
limitations:
```

## Required recovery/repair action

- If a required source is missing, stop with source/context request instead of accepting weak synthesis.
- If the Map collapses into roadmap/backlog/Work Graph/task list, return same-procedure repair before acceptance review.
- If acceptance, storage, Codex, child/check work, or next material work is needed, return a Transition Packet and do not launch it invisibly.
- If state was mutated or acceptance was implied inside formation chat, block acceptance and route to `recovery_review`.

END_OF_FILE: workflow_v3/evals/DIRECTION_MAP_FORMATION_EVAL.md