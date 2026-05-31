# Workflow v3 Entity Registry

status: active_interface_layer

## Purpose

This file is the canonical registry of Workflow v3 entities for the current skeleton boundary.

Every entity below is candidate-only or interface-only unless an accepted Direction adoption/update path later creates per-Direction state.

| Entity | Short definition | Not-this boundary | Canonical owner file/interface | State mutation rights |
| --- | --- | --- | --- | --- |
| Direction | Long-lived project/result system with its own runtime state after adoption. | Not a single file, chat, backlog, Project, or prompt. | `01_DIRECTION_STRUCTURE_INTERFACE.md` | Created/adopted only through explicit Direction adoption package. |
| Direction Runtime Root | Future per-Direction root at `directions_v3/<direction-id>/runtime/`. | Not created by this interface package. | `09_STORAGE_STATE_INTERFACE.md` | Created only through accepted per-Direction adoption. |
| Direction Spine | Stable axis for root result, success conditions, spine points, and tracks. | Not roadmap, backlog, or full Work Graph. | `01_DIRECTION_STRUCTURE_INTERFACE.md` | Mutates only through acceptance/update path. |
| Direction Map | Global structural map between Direction Spine and Active Front. | Not roadmap, backlog, Action Inbox, or local Work Graph. | `02_DIRECTION_MAP_INTERFACE.md` | Mutates only through acceptance/update path. |
| Track | Stable strategic lane within the Direction Spine/Map. | Not a task list or workstream branch by itself. | `02_DIRECTION_MAP_INTERFACE.md` | Changes only through accepted Spine/Map update. |
| Map Area | Named part of Direction Map that can host risks, dependencies, candidate fronts, or closed fronts. | Not a Work Graph node or backlog item. | `02_DIRECTION_MAP_INTERFACE.md` | Changes only through accepted Map update. |
| Strategic Dependency | Dependency that affects sequencing or viability across map areas/tracks. | Not ordinary task dependency inside a local Work Graph. | `02_DIRECTION_MAP_INTERFACE.md` | Accepted only through Map/decision update. |
| Strategic Uncertainty | Material unknown that affects Direction route, front choice, or risk. | Not vague concern or untracked idea. | `02_DIRECTION_MAP_INTERFACE.md` | Accepted/closed only through evidence and acceptance/update path. |
| Candidate Active Front | Proposed focus selected from Direction Map areas. | Not accepted current focus until reviewed. | `04_ACTIVE_FRONT_SELECTION_INTERFACE.md` | Candidate only until accepted. |
| Active Front | Accepted current focus selected from the Direction Map. | Not global Direction state, roadmap, or all active work. | `04_ACTIVE_FRONT_SELECTION_INTERFACE.md` | Mutates only through acceptance/update path. |
| Front Exit Criteria | Conditions that define when an Active Front can close. | Not optional notes or hidden acceptance. | `04_ACTIVE_FRONT_SELECTION_INTERFACE.md` | Accepted with Active Front or later accepted update. |
| Work Graph | Local execution graph under one Active Front. | Not Direction Map, roadmap, or global backlog. | `05_WORK_GRAPH_AND_NODE_INTERFACE.md` | Created/updated through accepted Active Front work path. |
| Work Graph Node | Bounded unit in a local Work Graph. | Not an unbounded project task or future route claim. | `05_WORK_GRAPH_AND_NODE_INTERFACE.md` | Opens/closes through Work Graph and closure records. |
| Node Closure | Summary and evidence trail when a Work Graph Node closes. | Not implicit "done" claim. | `05_WORK_GRAPH_AND_NODE_INTERFACE.md` | Recorded after evidence/acceptance review. |
| Work Contract | Bounded agreement for one run or node slice. | Not permanent roadmap or scope-expanding prompt. | `05_WORK_GRAPH_AND_NODE_INTERFACE.md` | Created through Launch Packet or accepted work path. |
| Run | Execution of a Work Contract by an adapter or human. | Not acceptance, route choice, or state mutation. | `10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | Produces candidate result/evidence only. |
| Result Packet | Returned candidate result, evidence, limits, and next surface. | Not accepted state. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate until accepted. |
| Evidence | Verifiable support for a result or decision. | Not acceptance by itself. | `12_QUALITY_RECOVERY_INTERFACE.md` | Supports acceptance; does not mutate state alone. |
| Acceptance Decision | Explicit accept/reject/repair decision over candidate result/evidence. | Not adapter self-approval or chat intuition. | `12_QUALITY_RECOVERY_INTERFACE.md` | Only accepted decision/update path mutates accepted state. |
| Accepted State | Canonical state after accepted update. | Not chat memory, Project Files/Sources, Signal, Handler result, or document existence. | `09_STORAGE_STATE_INTERFACE.md` | Mutates only through explicit acceptance/update path. |
| Memory Candidate | Candidate context that may be useful later. | Not Memory Artifact or accepted state. | `09_STORAGE_STATE_INTERFACE.md` | Candidate until promoted. |
| Memory Artifact | Promoted memory with source and use boundary. | Not replacement for canonical state. | `09_STORAGE_STATE_INTERFACE.md` | Promoted only through explicit review/update. |
| Signal | Emitted event/fact record. | Not task, command, acceptance, mutation, or Action Inbox item. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | Does not mutate state. |
| Lifecycle Signal | Signal category for Direction lifecycle transitions. | Not automatic lifecycle transition. | `03_DIRECTION_LIFECYCLE_SIGNAL_INTERFACE.md` | Fact only; transition requires acceptance/update when state changes. |
| Handler | Registry rule/process that reacts to Signals. | Not executor, acceptor, or hidden controller. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | Produces candidate outputs only. |
| Action Inbox Item | Candidate action retained for review or conversion. | Not raw Signal, backlog, roadmap, or auto-run queue. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | Candidate until converted/dropped/closed through review. |
| Check Job | Bounded verification task. | Not material work or acceptance. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | Returns candidate findings only. |
| Event Loop Closure | Visible closure after material work/review. | Not hidden automation or acceptance. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | May propose persistence; state changes only through acceptance/update. |
| Progression Router Result | Candidate routing output selecting one primary next move. | Not execution, acceptance, or hidden roadmap. | `07_EVENT_LOOP_AND_ROUTING_INTERFACE.md` | Candidate until accepted or explicitly launched. |
| Next Move | Exact next instruction after closure/review. | Not accepted state. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate/transport until acted on or accepted. |
| Transition Packet | Complete copy-paste transfer packet for selected external/surface step. | Not a vague instruction to make a prompt. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate until launched/accepted. |
| Next Chat Prompt | Copy-paste prompt for next material chat when needed. | Not child chat prompt or accepted state. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate until explicitly launched. |
| Child Chat | Chat serving current parent target and returning to parent. | Not next material chat or independent track. | `06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` | Produces candidate result for parent synthesis. |
| Parent Chat | Current synthesis authority for a target with child returns. | Not automatic acceptor of missing child evidence. | `06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` | Synthesizes candidates; acceptance still explicit. |
| Runtime Console | Read-only status/navigation surface. | Not execution controller or state mutator. | `10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | Read-only; may draft candidate packets. |
| Adapter | Provider or human execution surface for bounded work. | Not runtime authority or acceptor. | `10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | Returns candidate result/evidence only. |
| Codex Handoff | Bounded repository work package sent to Codex. | Not permission for Codex to route product meaning or accept state. | `10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | Codex writes only allowed paths under package; result returns for verification. |
| Codex Result Verification | Review of Codex changed files, validation, and boundaries. | Not automatic acceptance. | `10_ADAPTER_CODEX_PROVIDER_INTERFACE.md` | Produces verification evidence and candidate closure. |
| Project Instructions UI | Compact behavior bootstrap for a ChatGPT Project. | Not long docs, accepted state, or auto-updated by commit. | `11_PROJECT_SETUP_CONTEXT_INTERFACE.md` | Updates only through explicit Project setup rollout. |
| Project Files/Sources | Uploaded/cache context for Projects. | Not canonical authority or acceptance proof. | `11_PROJECT_SETUP_CONTEXT_INTERFACE.md` | Refresh only through explicit setup/adoption package. |
| Request-only Sources | Sources loaded only when an admitted task needs them. | Not default Project Files/Sources. | `11_PROJECT_SETUP_CONTEXT_INTERFACE.md` | Refresh/report separately. |
| legacy_evidence | Old Workflow OS/Direction files used as evidence only. | Not accepted v3 state or import by implication. | `12_QUALITY_RECOVERY_INTERFACE.md` | Import/use only through explicit legacy/adoption process. |

END_OF_FILE: workflow_v3/interfaces/00_ENTITY_REGISTRY.md
