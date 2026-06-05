# Run Surface Contracts

status: active_control_plane

## Purpose

Every admitted material action has a `run_surface_type`. The run surface contract defines semantic operations, forbidden operations, required inputs, required outputs, utility boundary notes, and stop conditions.

## Run surface taxonomy

- `selected_owner_run_surface`: a `run_surface_type` selected through Procedure Registry for one owner procedure.
- `utility_child_surface`: a bounded utility/check/child/research surface used through Utility Adapter Protocol; not a new selected owner procedure unless independently registered and selected.
- `readonly_surface`: a surface that reads or summarizes only and cannot execute material work or mutate state.
- `storage_update_adapter`: direct write surface only when selected from an admitted storage package.

## Lifecycle integration

Every run_surface_type is executed only inside RUN.

RUN can execute only the owner procedure selected in START.

Procedures using the Procedure Definition Framework execute as bounded stage/gate loops inside RUN.

A run surface contract cannot authorize procedure switching.

A run surface contract cannot authorize direct in-chat state mutation unless run_surface_type is `storage_update_adapter`.

External utility writes through Codex/storage utility require Utility Use Gate, write gate, exact path boundaries, validation, and RUN_EXTERNAL_RETURN verification. They remain subordinate to the same owner RUN and do not select a new owner procedure.

A run surface contract cannot authorize acceptance by the same chat that produced the candidate output.

Every material run surface must return FINISH_REQUEST before FINISH.

Embedded utility/adapter use is governed by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

Run surfaces do not whitelist every utility. Utility notes name common affordances or explicit restrictions only. They are compatibility and boundary notes, not routing authority.

The global utility layer is available to `core_material` owner procedures through the Utility Use Gate unless source, policy, safety, forbidden-operation, or write boundaries explicitly forbid the utility.

## Utility adapter compatibility

Default for `core_material` owners is global utility availability through the Utility Use Gate.

Utility use cannot authorize procedure switching, hidden mutation, hidden acceptance, or hidden next work.

RUN_EXTERNAL_HANDOFF and RUN_EXTERNAL_RETURN are governed by `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`.

Run surface `allowed_operations` and `forbidden_operations` still control semantic work. A utility note is packet/schema compatibility or an explicit boundary, not a broadening of the surface.

## `generic_answer`

allowed_operations:
- answer lightweight non-state-sensitive questions;
- cite limitations when current repository or runtime state is not read.

forbidden_operations:
- mutate state;
- infer current Direction status;
- perform acceptance, recovery, Codex, or Next Move work.

utility_notes:
- no material utility by default.

required_inputs:
- bounded question that does not depend on current canonical state.

required_outputs:
- answer or escalation to registered procedure.

stop_conditions:
- answer depends on current repo state, Direction runtime state, acceptance, Codex, recovery, or current Next Move.

## `status_review`

allowed_operations:
- resolve binding where relevant;
- read exact `CURRENT_STATUS.md` and `CURRENT_NEXT_MOVE.md`;
- summarize current accepted status and limitations.

forbidden_operations:
- execute material work;
- mutate state;
- accept evidence or start next work.

utility_notes:
- no material utility by default.

required_inputs:
- direction binding or exact runtime state path when status is Direction-specific.

required_outputs:
- status summary, source locks, limitations, exact next review/admission need.

stop_conditions:
- missing binding, unreadable state, conflicting state, or stale cache pressure.

## `setup_only_root_bootstrap`

allowed_operations:
- read exact control-plane, setup, bootstrap, storage layout, and project setup sources;
- resolve or normalize `direction_id`;
- classify setup mode and legacy policy;
- check whether the requested runtime root already exists;
- treat user purpose/goals only as `candidate_context_for_direction_definition`;
- prepare candidate setup-only root/bootstrap package;
- prepare Project Binding plan;
- prepare Project Instructions source plan if required;
- prepare Project Files manifest plan if required;
- prepare storage package or Codex handoff packet if persistence work is needed;
- produce Result Packet and Next Move Packet.

forbidden_operations:
- mutate repository directly;
- create runtime files directly in the setup chat;
- define or accept semantic Direction entities;
- define root outcome as accepted state;
- define product strategy, roadmap, backlog, or implementation plan;
- import legacy files as accepted Workflow v3 state;
- read legacy evidence unless the setup procedure explicitly requires it;
- create acceptance records;
- update CURRENT_STATUS or CURRENT_NEXT_MOVE directly;
- update actual ChatGPT Project Instructions UI;
- refresh Project Files/Sources externally;
- start Codex without a bounded handoff packet.

utility_notes:
- `codex_handoff_packet`;
- `codex_return_verification` only for a result returned from a handoff emitted by the same selected setup run;
- `check_job_packet`;
- `storage_update_package`;
- `project_refresh_instruction_packet`.

utility_policy:
- Candidate Codex handoff packets and storage update packages are allowed only where existing allowed operations permit persistence planning.
- No direct mutation, hidden acceptance, or Direction runtime mutation is authorized.

required_inputs:
- repository;
- base ref / source ref;
- direction_id or direction_id normalization input;
- setup mode;
- legacy policy;
- exact setup/control-plane procedure sources;
- mutation policy.

required_outputs:
- blocked result or candidate setup-only root/bootstrap package;
- source locks;
- candidate Project Binding plan;
- storage package or Codex handoff packet if persistence work is needed;
- Result Packet;
- Next Move Packet;
- exact next move.

stop_conditions:
- required source is missing, truncated, unreadable, stale, or lacks required EOF;
- runtime root already exists or conflicts with clean-start setup;
- semantic Direction content would be defined during setup;
- legacy import pressure appears;
- write is requested without storage_update_adapter package;
- actual Project UI / Project Files refresh is attempted directly;
- source lock lacks resolved main commit SHA or required file identity;
- action crosses from setup_only_root_bootstrap to formation_chat, acceptance_review, or storage_update_adapter without new admission.

## `formation_chat`

allowed_operations:
- read exact sources;
- classify context;
- generate alternatives;
- form candidate entity;
- ask acceptance question;
- produce Result Packet;
- produce Next Move Packet in chat.

forbidden_operations:
- mutate repository;
- create acceptance record;
- update `CURRENT_STATUS.md`;
- update `CURRENT_NEXT_MOVE.md`;
- accept own output;
- start Codex without a bounded packet and Utility Use Gate pass;
- create downstream entities before accepted prerequisites;
- treat user context as acceptance;
- treat acceptance wording as storage authorization;
- execute more than one steering entity unless the selected procedure itself is explicitly admitted as a single bounded procedure and START_PACKET names that single procedure;
- continue from one steering entity to another by conversation momentum;
- enter FINISH without FINISH_REQUEST and explicit FINISH or ФИНИШ token.

utility_notes:
- `check_job_packet`;
- `child_chat_packet`;
- `child_research_packet`;
- `storage_update_package` only as candidate next-surface output after the selected formation result is ready for acceptance/update routing.

utility_policy:
- Utility packets must match the selected formation procedure and must not broaden into unrelated entity formation.
- Do not block `codex_handoff_packet` solely because Codex is absent from these notes; apply the global Utility Use Gate and source/safety/write boundaries.
- Persistence may use same-owner external utility handoff only when approval/update authority, path boundaries, validation, and return verification are explicit; otherwise emit a blocked result or candidate package.

required_inputs:
- target entity or selected Direction Definition procedure;
- exact procedure source;
- source authority and required reads;
- return destination.

required_outputs:
- candidate entity or blocked result;
- evidence, read limitations, acceptance question, Result Packet, Next Move Packet, and Transfer Packet when transfer is needed;
- FINISH_REQUEST before FINISH;
- selected procedure result only;
- no hidden next procedure start.

stop_conditions:
- missing source, target drift, role boundary crossing, acceptance ambiguity, write request, or forbidden sequencing.

## `acceptance_review`

allowed_operations:
- review candidate result and evidence;
- form accept/reject/repair/block/park decision candidate;
- identify storage update need and return path.

forbidden_operations:
- mutate repository;
- allow producing adapter to accept its own output;
- treat validation/file existence as acceptance;
- broaden accepted changes beyond candidate/evidence;
- continue to semantic next step.

utility_notes:
- `check_job_packet`;
- `storage_update_package` only after acceptance/update need is explicitly formed as candidate output.

required_inputs:
- candidate result ref;
- evidence refs;
- reviewer authority;
- affected state paths and boundaries.

required_outputs:
- Acceptance Decision candidate or explicit human decision request;
- storage update need if applicable;
- Result Packet and Next Move Packet.

stop_conditions:
- evidence missing, reviewer authority unclear, self-acceptance risk, unclear affected paths, or write request.

## `storage_update_adapter`

surface_taxonomy: `storage_update_adapter`

allowed_operations:
- write only when a Storage Update Package exists and lists exact allowed files;
- apply exact required changes;
- run listed validation;
- return branch/commit/diff/validation evidence.

forbidden_operations:
- decide acceptance;
- broaden state changes;
- touch unlisted paths;
- continue to next semantic step;
- use chat memory/cache as accepted state.

utility_notes:
- storage execution uses the storage write gate; no additional material utility by default.

utility_policy:
- Direct in-chat storage execution is allowed only under selected `storage_update_adapter`.
- Same-owner external Codex/storage utility writes are adapter work, not selected storage owners, and require write gate plus verified RUN_EXTERNAL_RETURN.

required_inputs:
- complete Storage Update Package.

required_outputs:
- changed files, validation output, commit/push status when requested, limitations, return fields.

stop_conditions:
- missing package, missing allowed files, forbidden paths, expected diff absent, validation absent, or source integrity failure.

## `work_contract_execution`

allowed_operations:
- execute same-chat bounded work if the admitted Work Contract allows it;
- produce Transfer Packet for external execution;
- collect result and evidence from the allowed execution surface;
- return Result Packet.

forbidden_operations:
- accept result;
- mutate state;
- change parent route;
- broaden contract scope.

utility_notes:
- `codex_handoff_packet` when the admitted Work Contract allows Codex execution;
- `codex_return_verification` for a returned result of a Codex handoff emitted by the same selected work-contract run;
- `check_job_packet`;
- `child_chat_packet`.

utility_policy:
- Utility packets are allowed only when the admitted Work Contract names the external execution or verification surface.
- Returned Codex evidence must match the emitted handoff before reliance.

required_inputs:
- admitted Work Contract;
- allowed execution surface;
- expected result and evidence requirements;
- return destination.

required_outputs:
- blocked result, Transfer Packet, or candidate Result Packet with evidence and limitations;
- Next Move Packet to parent integration, acceptance review, or stop.

stop_conditions:
- Work Contract is missing, unaccepted, unbounded, or grants no allowed execution surface;
- requested execution would mutate state, accept output, change parent route, or broaden scope.

## `parent_integration`

allowed_operations:
- review child/result packets;
- compare evidence to parent criteria;
- produce Parent Integration Result;
- produce graph, escalation, delta, or derived-check candidates when needed.

forbidden_operations:
- invent missing child evidence;
- accept state;
- start next work invisibly.

utility_notes:
- `check_job_packet`;
- `child_chat_packet`;
- `child_research_packet`.

utility_policy:
- Check, child, or research packets must remain bounded to the parent integration target and cannot accept state.

required_inputs:
- parent Work Graph node, Active Front, or Goal Evidence Graph target;
- returned child/work Result Packets;
- parent acceptance criteria and evidence requirements;
- return destination.

required_outputs:
- Parent Integration Result;
- missing/conflicting evidence list when applicable;
- candidate graph/escalation/delta packet when applicable;
- Next Move Packet.

stop_conditions:
- required parent target is missing;
- required child/work result is missing or conflicting;
- integration would accept state, synthesize evidence, or open new work invisibly.

## `procedure_authoring`

allowed_operations:
- read exact Workflow v3 procedure framework, registry, control-plane, eval, and existing procedure sources;
- design candidate procedure definitions;
- design canonical procedure location and naming decisions;
- design self-contained stub target specs and detailed procedure bodies;
- design registry entry proposals;
- design run surface compatibility statements;
- design eval proposals;
- design authoring plans for simple procedures;
- produce bounded Codex/check/research/storage handoff packets when requested by the selected authoring scope and allowed by the procedure;
- verify returned Codex evidence for a handoff emitted by the same selected authoring run before relying on it;
- produce Result Packet and Next Move Packet.

forbidden_operations:
- mutate repository/runtime state directly;
- update actual ChatGPT Project Instructions UI;
- accept its own output;
- execute the procedure being authored;
- author complex procedure bodies unless separately scoped;
- preserve obsolete runbook/playbook path or naming for a procedure;
- leave a registry entry pointing outside canonical procedure files;
- start Codex without a bounded handoff packet;
- touch Direction runtime state;
- import legacy evidence as current state.

utility_notes:
- `codex_handoff_packet`;
- `codex_return_verification` for a returned result of a Codex handoff emitted by the same selected authoring run;
- `check_job_packet`;
- `child_research_packet`;
- `storage_update_package` only as candidate next-surface output;
- `project_refresh_instruction_packet`.

utility_policy:
- Codex handoff packets are limited to bounded repository maintenance patches of the selected authoring result.
- Codex return verification is limited to evidence from the same emitted handoff.
- Check job and child research packets require bounded questions.
- Hidden storage execution, hidden acceptance, Direction runtime mutation, and unrelated procedure authoring by utility expansion are forbidden.

required_inputs:
- target procedure name or intent;
- expected trigger and output;
- target run surface or candidate run surface;
- source files to inspect;
- requested integration scope;
- repository/base ref when repository work is requested;
- current registry entrypoint, proposed procedure path, and current stub target spec when authoring a stub body.

required_outputs:
- candidate procedure definition, stub target spec, or integration plan;
- canonical location and naming decision;
- registry entry proposal or registry delta;
- run surface compatibility statement;
- eval proposal;
- allowed/forbidden paths if handoff is needed;
- Result Packet;
- Next Move Packet;
- exact next move.

stop_conditions:
- target procedure is unbounded;
- requested work crosses into execution, acceptance, storage, or complex procedure body authoring;
- required sources are missing or unreadable;
- procedure would authorize hidden mutation or self-acceptance;
- procedure would keep obsolete runbook/playbook path or naming;
- registry delta would leave a procedure pointed outside canonical procedure files.

## `codex_handoff`

allowed_operations:
- package bounded implementation or repository maintenance work for Codex;
- define source reads, allowed/forbidden paths, validation, commit/push policy, and return fields.

forbidden_operations:
- execute product work by implication;
- omit validation or return fields;
- authorize writes outside allowed paths.

utility_notes:
- produces `codex_handoff_packet`; no embedded child utility categories.

utility_policy:
- This is a `utility_adapter` surface.
- When selected by START it prepares a standalone package.
- Embedded use supplies packet schema and quality checks only; it is not the selected owner procedure.

required_inputs:
- repository, base_ref, branch policy, goal, source files, path boundaries, validation, stop conditions.

required_outputs:
- self-contained Codex handoff package.

stop_conditions:
- missing repository/base/source/path boundaries or conflict with workflow authority.

## `codex_result_verification`

allowed_operations:
- verify branch, commit, changed files, allowed paths, validation output, EOF markers, payload counts, refresh categories, push status, and residual risks.

forbidden_operations:
- claim done without validation;
- accept result by verification alone;
- repair runtime state unless separately admitted.

utility_notes:
- produces `codex_return_verification`; no embedded child utility categories.

utility_policy:
- This is a `verification_adapter` surface.
- When selected by START it performs standalone verification.
- Embedded use verifies returned evidence matching an emitted handoff; it is not the selected owner procedure.

required_inputs:
- Codex return fields and exact branch/commit context.

required_outputs:
- verification result, failures, residual risks, next move.

stop_conditions:
- missing branch/commit/diff/validation or forbidden path touch.

## `check_job`

surface_taxonomy: `utility_child_surface`

allowed_operations:
- answer a bounded source, evidence, consistency, or validation question;
- return candidate findings.

forbidden_operations:
- execute material work;
- mutate state;
- accept results.

utility_notes:
- produces `check_job_packet`; no embedded child utility categories.

required_inputs:
- scoped question, exact sources, return destination.

required_outputs:
- findings, evidence, limitations, return packet.

stop_conditions:
- question expands into material work or required source is missing.

## `child_research_chat`

surface_taxonomy: `utility_child_surface`

allowed_operations:
- perform bounded supporting research/checks for a parent target;
- return result to parent.

forbidden_operations:
- decide parent target;
- mutate state;
- accept output;
- become independent execution track.

utility_notes:
- produces `child_research_packet`; no embedded child utility categories.

required_inputs:
- parent target, child question, source boundary, required return fields.

required_outputs:
- child result, evidence, limitations, parent return destination.

stop_conditions:
- parent context missing, question unbounded, or child tries to decide.

## `recovery_review`

allowed_operations:
- inspect suspect runtime/process state;
- classify contamination, missing evidence, and recovery options.

forbidden_operations:
- repair runtime files without separate admitted package;
- retroactively accept state without explicit record;
- invent proof state.

utility_notes:
- `check_job_packet`;
- `codex_return_verification` only when reviewing returned Codex evidence as suspect evidence.

utility_policy:
- Utility use is limited to evidence checks for the selected recovery review and cannot repair, mutate, or accept state.

required_inputs:
- suspect state refs, evidence refs, source locks, recovery question.

required_outputs:
- recovery outcome candidate and next move.

stop_conditions:
- source missing, recovery would require write, or acceptance authority unclear.

## `runtime_console_readonly`

surface_taxonomy: `readonly_surface`

allowed_operations:
- summarize exact status from bound sources;
- draft candidate packets and next moves.

forbidden_operations:
- execute material work;
- mutate state;
- accept evidence;
- start Codex directly;
- act as an execution controller.

utility_notes:
- no material utility by default.

required_inputs:
- exact binding/status/next move sources.

required_outputs:
- read-only console summary, source limits, candidate actions.

stop_conditions:
- binding missing, state unreadable, or console attempts hidden control.

END_OF_FILE: workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md
