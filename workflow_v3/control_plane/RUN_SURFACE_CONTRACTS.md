# Run Surface Contracts

status: active_control_plane

## Purpose

Every admitted material action has a `run_surface_type`. The run surface contract defines allowed operations, forbidden operations, required inputs, required outputs, and stop conditions.

## Lifecycle integration

Every run_surface_type is executed only inside RUN.

RUN can execute only the procedure selected in START.

Procedures using the Procedure Definition Framework execute as bounded stage/gate loops inside RUN.

A run surface contract cannot authorize procedure switching.

A run surface contract cannot authorize state mutation unless run_surface_type is storage_update_adapter.

A run surface contract cannot authorize acceptance by the same chat that produced the candidate output.

Every material run surface must return FINISH_REQUEST before FINISH.

## `generic_answer`

allowed_operations:
- answer lightweight non-state-sensitive questions;
- cite limitations when current repository or runtime state is not read.

forbidden_operations:
- mutate state;
- infer current Direction status;
- perform acceptance, recovery, Codex, or Next Move work.

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
- accept evidence or launch next work.

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
- prepare per-Direction Project Instructions source plan if required by setup procedure;
- prepare Project Files manifest plan if required by setup procedure;
- prepare Storage Update Package or Codex handoff if persistence is needed;
- produce Result Packet and Event Loop Closure.

forbidden_operations:
- mutate repository directly;
- create runtime files directly in the setup chat;
- define or accept Direction Spine;
- define or accept Direction Map;
- define or accept Active Front;
- create Work Graph;
- create Work Contract;
- define root outcome as accepted state;
- define product strategy, roadmap, backlog, or implementation plan;
- import `workflow/**` or `directions/**` as accepted Workflow v3 state;
- read legacy evidence unless the setup procedure explicitly requires it;
- create acceptance records;
- update CURRENT_STATUS or CURRENT_NEXT_MOVE directly;
- update actual ChatGPT Project Instructions UI;
- refresh Project Files/Sources externally;
- launch Codex without a bounded Codex handoff.

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
- Storage Update Package or Codex handoff if persistence is needed;
- Result Packet;
- Event Loop Closure;
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
- produce Event Loop Closure in chat.

forbidden_operations:
- mutate repository;
- create acceptance record;
- update `CURRENT_STATUS.md`;
- update `CURRENT_NEXT_MOVE.md`;
- accept own output;
- launch Codex unless separately admitted;
- create Work Graph before accepted Active Front;
- treat user context as acceptance;
- treat acceptance signal as storage authorization;
- execute more than one steering entity unless the selected procedure itself is explicitly admitted as a single bounded procedure and START_PACKET names that single procedure;
- continue from one steering entity to another by conversation momentum;
- enter FINISH without FINISH_REQUEST and explicit FINISH or ФИНИШ token.

required_inputs:
- target entity or selected Direction Definition procedure;
- exact procedure source;
- source authority and required reads;
- return destination.

required_outputs:
- candidate entity or blocked result;
- evidence, read limitations, acceptance question, Event Loop Closure, exact next move or Transition Packet;
- FINISH_REQUEST before FINISH;
- selected procedure result only;
- no hidden next procedure launch.

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

required_inputs:
- candidate result ref;
- evidence refs;
- reviewer authority;
- affected state paths and boundaries.

required_outputs:
- Acceptance Decision candidate or explicit human decision request;
- storage update need if applicable;
- Event Loop Closure and next move.

stop_conditions:
- evidence missing, reviewer authority unclear, self-acceptance risk, unclear affected paths, or write request.

## `storage_update_adapter`

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

required_inputs:
- complete Storage Update Package.

required_outputs:
- changed files, validation output, commit/push status when requested, limitations, return fields.

stop_conditions:
- missing package, missing allowed files, forbidden paths, expected diff absent, validation absent, or source integrity failure.

## `procedure_authoring`

allowed_operations:
- read exact Workflow v3 procedure framework, registry, control-plane, eval, and existing procedure sources;
- design candidate procedure definitions;
- design registry entry proposals;
- design run surface compatibility statements;
- design eval proposals;
- design migration plans for simple procedures;
- produce Codex/storage handoff candidates only when separately requested and bounded;
- produce Result Packet and Event Loop Closure.

forbidden_operations:
- mutate repository/runtime state directly;
- update actual ChatGPT Project Instructions UI;
- accept its own output;
- execute the procedure being authored;
- migrate complex formation/entity procedures unless separately scoped;
- launch Codex without a separately admitted `codex_handoff`;
- touch Direction runtime state;
- import legacy evidence as current state.

required_inputs:
- target procedure name or intent;
- expected trigger and output;
- target run surface or candidate run surface;
- source files to inspect;
- requested integration scope;
- repository/base ref when repository work is requested.

required_outputs:
- candidate procedure definition or integration plan;
- registry entry proposal;
- run surface compatibility statement;
- eval proposal;
- allowed/forbidden paths if handoff is needed;
- Result Packet;
- Event Loop Closure;
- exact next move.

stop_conditions:
- target procedure is unbounded;
- requested work crosses into execution, acceptance, storage, or complex formation migration;
- required sources are missing or unreadable;
- procedure would authorize hidden mutation or self-acceptance.

## `codex_handoff`

allowed_operations:
- package bounded implementation or repository maintenance work for Codex;
- define source reads, allowed/forbidden paths, validation, commit/push policy, and return fields.

forbidden_operations:
- execute product work by implication;
- omit validation or return fields;
- authorize writes outside allowed paths.

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

required_inputs:
- Codex return fields and exact branch/commit context.

required_outputs:
- verification result, failures, residual risks, next move.

stop_conditions:
- missing branch/commit/diff/validation or forbidden path touch.

## `check_job`

allowed_operations:
- answer a bounded source, evidence, consistency, or validation question;
- return candidate findings.

forbidden_operations:
- execute material work;
- mutate state;
- accept results.

required_inputs:
- scoped question, exact sources, return destination.

required_outputs:
- findings, evidence, limitations, return packet.

stop_conditions:
- question expands into material work or required source is missing.

## `child_research_chat`

allowed_operations:
- perform bounded supporting research/checks for a parent target;
- return result to parent.

forbidden_operations:
- decide parent target;
- mutate state;
- accept output;
- become independent execution track.

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

required_inputs:
- suspect state refs, evidence refs, source locks, recovery question.

required_outputs:
- recovery outcome candidate and next move.

stop_conditions:
- source missing, recovery would require write, or acceptance authority unclear.

## `runtime_console_readonly`

allowed_operations:
- summarize exact status from bound sources;
- draft candidate packets and next moves.

forbidden_operations:
- execute material work;
- mutate state;
- accept evidence;
- launch Codex directly.

required_inputs:
- exact binding/status/next move sources.

required_outputs:
- read-only console summary, source limits, candidate actions.

stop_conditions:
- binding missing, state unreadable, or console attempts hidden control.

END_OF_FILE: workflow_v3/control_plane/RUN_SURFACE_CONTRACTS.md
