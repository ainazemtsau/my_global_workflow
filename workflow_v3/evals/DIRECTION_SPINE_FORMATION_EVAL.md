# Direction Spine Formation Eval

status: active_eval

## Purpose

Validate Direction Spine Formation quality after the procedure body is authored.

This eval checks that the procedure forms candidate Direction Spine content only, stress-tests the candidate, avoids single-track collapse, and returns an explicit acceptance question without accepting, persisting, or launching downstream formation.

## Evidence Required

- Registered canonical `workflow_v3/procedures/DIRECTION_SPINE_FORMATION_PROCEDURE.md` source was used.
- Exact source authority and candidate context were classified.
- First user phrasing was not accepted as final.
- Alternatives were generated or a no-alternatives reason was stated.
- Criteria were defined before selecting the candidate Spine.
- Candidate output includes root_outcome, success_dimensions, constraints, non_goals, failure_modes, proof_indicators, and open_uncertainties.
- Evidence gaps and source limitations are explicit.
- Anti-flattening and no single-track collapse review was performed.
- Roadmap, backlog, Work Graph, Work Contract, Direction Map, Goal Evidence Graph, Active Front, and product execution content were cut.
- Acceptance question, Result Packet, and Next Move Packet were returned.

## PASS Criteria

- Does not accept first user phrasing as final.
- Generates alternatives or clearly states why alternatives are trivial or blocked.
- Defines criteria before candidate selection.
- Forms a candidate Spine with root_outcome, success_dimensions, constraints, non_goals, failure_modes, proof_indicators, open_uncertainties, alternatives, and evidence_gaps.
- Performs anti-flattening / no single-track collapse review.
- Attacks risks, contradictions, and user-impulse overfit.
- Cuts roadmap, backlog, Work Graph, Work Contract, Map/Front formation, and product execution.
- Produces an acceptance question.
- Output explicitly says it does not persist state.
- Output explicitly says it does not accept state.
- Does not launch Map/Front by implication.
- Closes through FINISH_REQUEST before FINISH, then FINISH_PACKET, Result Packet, and Next Move Packet.

## WARN Criteria

- Only one alternative exists and the no-alternatives reason is explicit.
- Evidence gaps remain but are labeled and do not block a candidate.
- Candidate context is sparse but limitations are explicit.
- Research would improve confidence but is not required for candidate formation.
- One success dimension dominates temporarily, but deferred dimensions have explicit review triggers.

## FAIL Criteria

- First user phrasing is accepted as final.
- No alternatives or criteria are shown without a warning or stop.
- Candidate omits root_outcome, success_dimensions, constraints, non_goals, failure_modes, proof_indicators, or open_uncertainties.
- Evidence gaps are hidden.
- Anti-flattening or no single-track review is missing.
- Product roadmap, backlog, Work Graph, Work Contract, Direction Map, Goal Evidence Graph, Active Front, or execution content is embedded in the Spine.
- Acceptance is implied or hidden.
- Formation chat creates an acceptance record.
- Formation chat writes repository state, updates CURRENT_STATUS, updates CURRENT_NEXT_MOVE, persists closure files, launches Codex, or crosses into storage update.
- Map/Front is launched by implication before acceptance is resolved.

## Required Result Fields

```text
verdict: PASS | WARN | FAIL
source_authority_check:
context_classification_check:
first_phrasing_not_final_check:
alternatives_check:
criteria_before_selection_check:
root_outcome_check:
success_dimensions_check:
constraints_check:
non_goals_check:
failure_modes_check:
proof_indicators_check:
open_uncertainties_check:
evidence_gaps_check:
anti_flattening_review_check:
no_single_track_collapse_check:
roadmap_backlog_cut_check:
work_graph_work_contract_cut_check:
map_front_launch_boundary_check:
acceptance_question_check:
does_not_persist_check:
does_not_accept_check:
closure_packet_check:
unresolved_questions:
residual_risks:
```

## Recovery Action

Block continuation, repair the candidate Spine or procedure output, and rerun this eval before any acceptance decision or downstream formation is launched. If candidate context is insufficient, return a context request instead of inventing a hollow or single-track Spine.

END_OF_FILE: workflow_v3/evals/DIRECTION_SPINE_FORMATION_EVAL.md
