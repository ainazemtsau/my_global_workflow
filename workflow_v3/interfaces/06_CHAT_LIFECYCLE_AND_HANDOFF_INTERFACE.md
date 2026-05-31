# Chat Lifecycle and Handoff Interface

status: active_interface_layer

## Purpose

This interface defines parent, child, next chat, Codex, Check Job, human decision, and Runtime Console boundaries.

## Chat and run surfaces

| Surface | Lifecycle role | Target | Scope | Source authority | Expected result | Return destination | Closure signal | Event Loop Closure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| parent material chat | Synthesis authority for current material target. | Current Work Contract, review, or lifecycle target. | Bounded current target. | Exact repo/path/ref plus accepted records. | Result Packet, synthesis, decision request, or packets. | Same parent chat or accepted update path. | `material_run_closed` or relevant lifecycle signal. | Required after material work/review. |
| child chat | Focused support for current parent target. | Required subquestion or subresult. | Narrow child prompt. | Sources named by parent. | Compact child result for parent. | Parent chat. | `child_result_returned` or `child_missing_result`. | Required in parent synthesis; child should return closure fields. |
| next material chat | New material target after current target closes. | Next accepted Work Contract/front/node target. | New bounded target. | Transition Packet/Next Chat Prompt. | New Result Packet and closure. | Its own closure/return path. | `material_run_closed`. | Required. |
| check job chat | Bounded verification. | Source/evidence/consistency question. | Check only, not material work. | Exact sources in Check Job. | Candidate finding with limits. | Requesting chat. | `check_job_closed`. | Required when result is reviewed. |
| Codex run | Bounded repository implementation. | Codex handoff target. | Allowed paths only. | Repo/ref/branch and package. | Commit/diff/evidence/validation or blocked result. | Current chat for verification. | `codex_result_returned`. | Required after verification. |
| Codex result verification in current chat | Verify Codex output. | Changed files, validations, boundaries. | Verification only. | Repo branch/commit/diff. | Verification result and closure. | Current chat/acceptance path. | `codex_result_verified` or validation failure signal. | Required. |
| human decision surface | Judgment, permission, or acceptance. | Explicit decision question. | Human-only decision. | Packet evidence and options. | Decision or blocked response. | Requesting chat/path. | `human_decision_returned` or acceptance signal. | Required when decision affects route/state. |
| runtime console/status chat | Read-only orientation. | Status, uncertainty, candidate packets. | No material execution. | Verified state/indexes. | Status and candidate Next Move/packet. | User or parent chat. | `console_status_closed`. | Required only if material review/routing occurred. |

## Hard boundaries

- Child chat is a bounded support/decomposition/review surface for the current parent target and returns to parent.
- Child chat may perform only the specific bounded child work requested by the parent prompt.
- Child chat is not next material chat.
- Next material chat starts only after the current material target is accepted, persisted, verified, or explicitly stopped.
- Parent remains synthesis authority.
- Child missing result blocks synthesis when the child result is required.
- When multiple children are launched, Parent Recovery Block is required.
- Child chat must not commit independently, accept state, route product meaning, launch unrelated work, or become a substitute for the next material chat boundary.
- No chat may accept state by intuition or route product meaning without visible closure and acceptance/update path.

END_OF_FILE: workflow_v3/interfaces/06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md
