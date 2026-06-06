# Direction Lifecycle Output Interface

status: active_interface_layer

## Purpose

This interface defines typed Direction lifecycle facts for Workflow v3.

Lifecycle facts record missing, candidate, accepted, stale, blocked, or complete lifecycle surfaces. They do not execute material work and do not mutate state.

## Lifecycle facts

| Fact | Meaning |
| --- | --- |
| `direction_runtime_missing` | No adopted runtime root exists for the Direction. |
| `direction_adoption_needed` | Work requires explicit adoption before accepted v3 state can exist. |
| `direction_spine_missing` | Adopted Direction lacks accepted Direction Spine. |
| `direction_spine_candidate_returned` | Candidate Direction Spine has returned for review. |
| `direction_spine_accepted` | Direction Spine accepted through update path. |
| `direction_map_missing` | Adopted Direction lacks accepted Direction Map. |
| `direction_map_candidate_returned` | Candidate Direction Map has returned for review. |
| `direction_map_accepted` | Direction Map accepted through update path. |
| `active_front_missing` | Adopted Direction lacks accepted Active Front. |
| `active_front_candidate_returned` | Candidate Active Front has returned for review. |
| `active_front_accepted` | Active Front accepted through update path. |
| `work_graph_missing` | Accepted Active Front lacks local Work Graph. |
| `work_graph_created` | Local Work Graph candidate/workspace exists; it does not imply accepted or persisted Work Graph state unless an acceptance/update path records it. |
| `work_graph_node_ready` | A bounded node is ready for Work Contract creation. |
| `work_contract_created` | Work Contract created for a node or node slice. |
| `work_contract_complete` | Work Contract returned result/evidence for review. |
| `active_front_complete` | Active Front exit criteria appear satisfied and need review/closure. |
| `direction_map_update_needed` | Evidence or closure implies the Direction Map may need an update. |
| `direction_map_stale` | Direction Map may no longer reflect accepted evidence or current front state. |
| `track_imbalance_detected` | Track coverage/balance concern is visible. |
| `blocked_lifecycle_transition` | A lifecycle transition cannot safely continue. |

## Follow-up outputs

| Output | Matches | Candidate outputs |
| --- | --- | --- |
| `direction_adoption_guard` | Missing runtime, adoption-needed, or legacy boundary facts. | Blocked result, adoption decision request, or bounded adoption package candidate. |
| `direction_spine_creation` | Missing Spine or returned Spine candidate. | Candidate Spine review packet or acceptance/update request. |
| `direction_map_creation` | Missing Map or returned Map candidate. | Candidate Map review packet or acceptance/update request. |
| `active_front_selection` | Missing Active Front or candidate returned. | Candidate front selection packet with alternatives and acceptance question. |
| `work_graph_opening` | Accepted Active Front with missing Work Graph. | Candidate local Work Graph seed/opening packet. |
| `work_contract_creation` | Ready node without Work Contract. | Candidate Work Contract or Launch Packet. |
| `front_closure` | Active Front complete or front closure evidence. | Candidate front closure summary, acceptance question, and map update candidate. |
| `direction_map_update` | Map update needed, stale map, track imbalance, or closed front impact. | Candidate Direction Map update packet or Check Job. |

## Hard rules

- Follow-up output is candidate only.
- No lifecycle fact executes material work directly.
- No lifecycle fact accepts state.
- Every lifecycle transition that changes state must close with CLOSURE_CHECK, FINISH_PACKET, continuation state, and an acceptance/update path.
- A blocked lifecycle transition stops product work until the blocker is resolved or explicitly split into a future package.

END_OF_FILE: workflow_v3/interfaces/03_DIRECTION_LIFECYCLE_OUTPUT_INTERFACE.md
