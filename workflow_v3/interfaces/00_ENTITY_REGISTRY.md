# Workflow v3 Entity Registry

status: active_interface_layer

## Purpose

This file is the canonical registry of Workflow v3 entities for the current skeleton boundary.

Every entity below is candidate-only or interface-only unless an accepted Direction adoption/update path later creates per-Direction state.

Goal Evidence Graph, Goal Evidence Node, Active Unresolved Cut, Parent Integration Result, Graph Delta, Upstream Escalation Packet, Downstream Delta Packet, Derived Gate Check, and Memory Index are steering/control/projection/record artifacts. They are not semantic primitives, do not mutate accepted state by existence, and are not launch authority by themselves.

| Entity | Short definition | Not-this boundary | Canonical owner file/interface | State mutation rights |
| --- | --- | --- | --- | --- |
| Direction | Long-lived project/result system with its own runtime state after adoption. | Not a single file, chat, backlog, Project, or prompt. | `01_DIRECTION_STRUCTURE_INTERFACE.md` | Created/adopted only through explicit Direction adoption package. |
| Direction Runtime Root | Future per-Direction root at `directions_v3/<direction-id>/runtime/`. | Not created by this interface package. | `09_STORAGE_STATE_INTERFACE.md` | Created only through accepted per-Direction adoption. |
| Direction Spine | Stable axis for root result, success conditions, spine points, and tracks. | Not roadmap, backlog, or full Work Graph. | `01_DIRECTION_STRUCTURE_INTERFACE.md` | Mutates only through acceptance/update path. |
| Direction Map | Global structural map between Direction Spine and Active Front. | Not roadmap, backlog, unreviewed task list, or local Work Graph. | `02_DIRECTION_MAP_INTERFACE.md` | Mutates only through acceptance/update path. |
| Goal Evidence Graph | Direction Map-associated steering/control graph of claims, alternatives, obstacles, evidence requirements, and candidate focus paths. | Not semantic primitive, roadmap, backlog, accepted state, or launch authority. | `14_GOAL_EVIDENCE_GRAPH_INTERFACE.md` | Candidate/control projection; mutates accepted state only through acceptance/update path. |
| Goal Evidence Node | Graph node carrying a claim, obstacle, evidence need, relation to parent, status, and acceptance policy. | Not Work Graph node or accepted proof by existence. | `14_GOAL_EVIDENCE_GRAPH_INTERFACE.md` | Candidate/control projection until accepted. |
| Active Unresolved Cut | Selected unresolved graph frontier used to inform Active Front selection. | Not Work Graph, backlog, roadmap, or launch authority. | `14_GOAL_EVIDENCE_GRAPH_INTERFACE.md` | Candidate selection mechanism only. |
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
| FINISH_PACKET | Final lifecycle closure wrapper after explicit FINISH. | Not acceptance or launch authority. | `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md` | Candidate closure only. |
| STAGE_RESULT | Visible output for one completed material stage. | Not accepted state or closure by itself. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate stage output only. |
| CLOSURE_CHECK | Check comparing actual result to selected procedure completion. | Not acceptance, launch authority, or a global done enum. | `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md` | Candidate check result until FINISH/audit and any required acceptance/update path. |
| Parent Integration Result | Typed fan-in record comparing returned child/work results to parent criteria. | Not acceptance, evidence synthesis, mutation, or launch authority. | `15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` | Candidate record until accepted or acted on by admitted path. |
| Graph Delta | Candidate graph change record for Goal Evidence Graph structure/status/evidence links. | Not accepted graph mutation by existence. | `15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` | Candidate record until acceptance/update path. |
| Upstream Escalation Packet | Typed packet escalating a lower-layer issue to the required parent layer. | Not accepted route change or launch authority. | `15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` | Candidate packet until acted on by admitted path. |
| Downstream Delta Packet | Typed packet carrying parent-context change to affected child/work surfaces. | Not silent cancellation, launch, or accepted state. | `15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` | Candidate packet until acted on by admitted path. |
| Derived Gate Check | Internal procedure check record for strategy, discovery, delivery, verification, interface dependency, risk, or memory-learning boundaries. | Not separate runtime entity or route authority. | `15_PARENT_INTEGRATION_AND_IMPACT_INTERFACE.md` | Candidate/internal check only. |
| Transfer Packet | Complete copy-paste transfer packet for selected external/surface step. | Not a vague instruction to make a prompt. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate until launched/accepted. |
| NEXT_CHAT_CARD | Copy-paste prompt for next material chat when needed. | Not child chat prompt or accepted state. | `08_PACKET_AND_TRANSFER_INTERFACE.md` | Candidate until explicitly launched. |
| Check Job | Bounded verification task. | Not material work or acceptance. | `06_CHAT_LIFECYCLE_AND_HANDOFF_INTERFACE.md` | Returns candidate findings only. |
| Evidence | Verifiable support for a result or decision. | Not acceptance by itself. | `12_QUALITY_RECOVERY_INTERFACE.md` | Supports acceptance; does not mutate state alone. |
| Acceptance Decision | Explicit accept/reject/repair decision over candidate result/evidence. | Not adapter self-approval or chat intuition. | `12_QUALITY_RECOVERY_INTERFACE.md` | Only accepted decision/update path mutates accepted state. |
| Accepted State | Canonical state after accepted update. | Not chat memory, Project Files/Sources, packet output, check output, or document existence. | `09_STORAGE_STATE_INTERFACE.md` | Mutates only through explicit acceptance/update path. |
| Memory Candidate | Candidate context that may be useful later. | Not Memory Artifact or accepted state. | `09_STORAGE_STATE_INTERFACE.md` | Candidate until promoted. |
| Memory Artifact | Promoted memory with source and use boundary. | Not replacement for canonical state. | `09_STORAGE_STATE_INTERFACE.md` | Promoted only through explicit review/update. |
| Memory Index | Lookup surface for promoted Memory Artifacts with load/exclusion/refresh rules. | Not raw notes, accepted state, or source replacement. | `09_STORAGE_STATE_INTERFACE.md` | Index updates only through accepted memory/update path. |
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
