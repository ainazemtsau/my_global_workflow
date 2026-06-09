# Procedure: Direction Project Root Bootstrap

title: Direction Project Root Bootstrap
status: active_procedure
canonical_location: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
entrypoint: direction_project_root_bootstrap
procedure_boundary: setup_only_root_bootstrap
kind: core
routing_dependency_policy: dependency_allowed_when_needed_for_bounded_setup_evidence_or_mutation_only

## Purpose

Create a setup-only technical runtime root bootstrap result for one future Workflow v3 Direction Project.

This procedure prepares or verifies the technical root, binding, setup-source, placeholder state, storage/update boundary, validation requirements, and post-bootstrap continuation for a Direction.

It must not define semantic Direction content, accept Direction outcomes, create semantic Direction Spine / Direction Map / Active Front content, create a Work Graph, create a Work Contract, import legacy state, or perform product work.

Root bootstrap is infrastructure setup only.

## Trigger / When to Use

Use this procedure when all are true:

- START selected `direction_project_root_bootstrap`;
- the selected procedure path is `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`;
- the requested work is setup-only root bootstrap for one ordinary Workflow v3 Direction Project;
- the operator needs to normalize or confirm `direction_id`;
- the operator needs a setup-only runtime root package, binding plan, Project setup source plan, or explicit blocked bootstrap result;
- semantic Direction Definition has not yet been accepted for this Direction.

Typical first-chat use:

- a newly created ordinary Direction Project has no accepted runtime root yet;
- root/bootstrap needs to produce setup-only placeholder state and `CURRENT_NEXT_MOVE = launch_direction_definition`;
- any user-provided outcome, tracks, goals, product ideas, or constraints must be classified as `candidate_context_for_direction_definition` only.

## When Not to Use

Do not use this procedure to:

- define semantic Direction content;
- accept a root outcome;
- create accepted Direction Spine content;
- create accepted Direction Map content;
- select or accept Active Front;
- create Work Graph;
- create Work Contract;
- execute product work;
- import old Direction files or legacy state;
- migrate/adopt an existing Direction without a separately admitted adoption/migration package;
- persist repository/runtime files directly inside this core procedure without an admitted storage or dependency write path;
- update actual ChatGPT Project Instructions UI;
- refresh actual ChatGPT Project Files/Sources;
- treat Project title, chat memory, Project Files/Sources, uploaded files, or generated packs as binding authority;
- continue to Direction Definition in the same material lifecycle before bootstrap closure.

## Required Inputs

Required START/lifecycle inputs:

```text
selected_entrypoint: direction_project_root_bootstrap
selected_procedure_path: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
procedure_boundary: setup_only_root_bootstrap
kind: core
routing_dependency_policy: dependency_allowed_when_needed_for_bounded_setup_evidence_or_mutation_only
```

Required task inputs:

```yaml
direction_bootstrap_request:
  project_type: ordinary_direction_project
  direction_id: string | missing
  direction_display_name: string | optional
  setup_mode: setup_only_root_bootstrap
  repository: owner/name | unknown
  source_ref: branch | tag | commit | unknown
  project_name_or_title_hint: string | optional_non_authority
  legacy_policy: not_used | legacy_evidence_read_only | migration_or_adoption_requires_separate_package | unknown
  runtime_root_evidence:
    exact_runtime_root_path: directions_v3/<direction-id>/runtime/ | unknown
    exact_binding_path: directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md | unknown
    accepted_root_package_ref: string | not_applicable | unknown
  mutation_policy: candidate_only | storage_update_package_candidate | dependency_mutation_requested | unknown
  return_destination: same_chat | specified_parent | unknown
  candidate_context_for_direction_definition: optional
```

Required if a setup-only runtime root package will be prepared:

```yaml
setup_package_inputs:
  explicit_setup_confirmation: present | missing
  target_repository: owner/name
  base_ref_or_current_state_ref: branch | tag | commit
  direction_id: normalized_path_safe_direction_id
  package_status: candidate
  project_instruction_payload_source_ref: repository_ref
  storage_or_dependency_write_authority: not_admitted | admitted_with_exact_boundary
```

If any required input is missing and cannot be safely inferred from exact source or current user input, return a typed STOP or bounded Context Request.

## Direction ID Policy

`direction_id` is a technical path/binding identifier, not a semantic Direction definition.

A valid `direction_id` must be:

- explicit or safely normalized from current user input;
- path-safe;
- stable across chats;
- one Direction only;
- not derived from Project title as authority;
- not inferred by broad repository search.

Recommended normalized form:

```text
lowercase ASCII slug using letters, numbers, hyphen, or underscore
```

Required safety rules:

- no `/`;
- no `\`;
- no `..`;
- no leading or trailing slash;
- no empty string;
- no broad placeholder such as `<direction-id>`, `todo`, `unknown`, `same as project`, or `use previous`;
- no multi-Direction list.

If the user provides semantic naming, goals, product ideas, or outcomes while providing `direction_id`, classify those semantic parts as `candidate_context_for_direction_definition`.

## Setup-Only Placeholder Policy

The procedure may prepare only technical placeholder state for future Direction Definition.

Allowed placeholder status values:

```text
pending_definition
none_selected
setup_only_root_created
launch_direction_definition
```

Required setup-only placeholder plan:

```yaml
runtime_root: directions_v3/<direction-id>/runtime/

runtime_config:
  - directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md

runtime_state:
  - path: directions_v3/<direction-id>/runtime/state/DIRECTION_SPINE.md
    semantic_status: pending_definition
    allowed_content: placeholder only
  - path: directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md
    semantic_status: pending_definition
    allowed_content: placeholder only
  - path: directions_v3/<direction-id>/runtime/state/ACTIVE_FRONT.md
    semantic_status: none_selected | pending_definition
    allowed_content: placeholder only
  - path: directions_v3/<direction-id>/runtime/state/CURRENT_STATUS.md
    runtime_status: setup_only_root_created
    semantic_definition_status: pending_definition
  - path: directions_v3/<direction-id>/runtime/state/CURRENT_NEXT_MOVE.md
    primary_next_move: launch_direction_definition
```

Forbidden placeholder content:

- accepted Direction purpose;
- accepted root outcome;
- accepted Direction Spine claims;
- accepted Direction Map structure;
- accepted Active Front;
- accepted Work Graph;
- accepted Work Contract;
- product strategy;
- task backlog;
- legacy import;
- any semantic state described as accepted.

## Project Binding Policy

A root bootstrap package must include a canonical Project Binding plan.

Target binding path:

```text
directions_v3/<direction-id>/runtime/config/DIRECTION_PROJECT_BINDING.md
```

Binding role:

- locator and continuation configuration only;
- not accepted product state;
- not Direction Map;
- not Work Graph;
- not previous chat memory;
- not Project title authority.

Binding must include or derive:

```yaml
direction_id:
binding_status: candidate | accepted | superseded
project_type: ordinary_direction_project
semantic_definition_status: pending_definition
runtime_root: directions_v3/<direction-id>/runtime/
current_status_path: directions_v3/<direction-id>/runtime/state/CURRENT_STATUS.md
current_next_move_path: directions_v3/<direction-id>/runtime/state/CURRENT_NEXT_MOVE.md
direction_spine_path: directions_v3/<direction-id>/runtime/state/DIRECTION_SPINE.md
direction_map_path: directions_v3/<direction-id>/runtime/state/DIRECTION_MAP.md
active_front_path: directions_v3/<direction-id>/runtime/state/ACTIVE_FRONT.md
project_setup_source_path: directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
project_files_manifest_path: directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md
project_instruction_payload_source_ref:
accepted_root_package_ref:
acceptance_decision_ref:
source_authority:
project_title_hint:
project_title_is_not_authority: true
```

If a binding already exists and conflicts with user input, Project title, uploaded files, optional Project Files cache, or chat memory, stop and request binding repair from exact repo/path/ref evidence.

Do not infer binding from:

- Project title;
- previous chat memory;
- uploaded files;
- Project Files/Sources;
- broad repository search;
- old Direction directory names.

## Project Setup Source Policy

A setup-only root package may generate per-Direction Project setup source files, but it must not apply them to the actual ChatGPT Project UI.

Concrete target files:

```text
directions_v3/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
directions_v3/<direction-id>/project_setup/PROJECT_FILES_MANIFEST.md
```

The concrete `CHATGPT_PROJECT_INSTRUCTIONS.md` must be generated from:

- accepted runtime binding;
- accepted runtime root package ref;
- acceptance decision ref;
- exact repository ref used for setup.

The binding capsule inside the Project Instructions payload must be generated from the canonical binding source, not invented manually.

The concrete `PROJECT_FILES_MANIFEST.md` must state:

- Project Files/Sources are cache/context only;
- exact repository files at named repo/path/ref remain source authority;
- default Project Files/Sources decision is none;
- optional binding file cache, if used later, is cache only;
- runtime state files are not uploaded by default;
- `workflow_v3/**` source docs are not uploaded by default.

Refresh reporting must be separate:

```yaml
project_instruction_ui_update_required: true when concrete per-Direction source is generated or changed; manual UI update only
project_sources_files_refresh_required: false by default unless optional binding cache is explicitly used
request_only_sources_refresh_required: false by default
do_not_upload_as_project_file: true for Project Instructions source
```

## Storage Package Boundary

This core procedure must not directly mutate repository/runtime state.

Allowed outputs without direct write:

- setup-only root bootstrap result;
- candidate setup-only root package;
- candidate Storage Update Package;
- complete `DEPENDENCY_CALL` packet for a bounded code repository, storage persistence, or support adapter dependency if mutation/check/readback is explicitly admitted;
- blocked result.

A candidate Storage Update Package must include:

```yaml
storage_update_package:
  package_version: storage_update_package.v1
  package_id:
  produced_by:
    source_entrypoint: direction_project_root_bootstrap
    source_procedure_path: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
    source_procedure_boundary: setup_only_root_bootstrap
    source_result_ref:
    source_finish_ref:
  update_authority:
    authority_type:
    authority_ref:
    authority_statement:
    authority_scope:
    not_accepted_by_storage: true
    not_executed_by_acceptance: true
  repository_target:
    repository:
    base_ref:
    target_ref:
    expected_head_sha_before_write:
    write_surface:
    commit_policy:
    push_policy:
  source_authority:
    canonical_sources:
    forbidden_authority_sources:
      - Project Files/Sources cache
      - chat memory
      - candidate docs unless explicitly accepted and referenced
      - legacy Direction files unless separately admitted as legacy_evidence
    source_conflict_policy: stop_on_conflict
  path_boundaries:
    allowed_files:
    forbidden_paths:
    path_rule: exact_allowed_files_only_no_globs_no_wildcards
    unlisted_path_policy: stop
  change_set:
    - change_id:
      path:
      operation: create | update | delete
      change_authority_ref:
      current_state_requirement:
      allowed_change:
      no_other_changes_allowed: true
  validation:
    validation_required: true
    commands_or_checks:
    eof_checks:
    diff_checks:
    validation_absent_policy: stop
  project_refresh_requirements:
    project_instruction_ui_update_required:
    project_sources_files_refresh_required:
    request_only_sources_refresh_required:
    do_not_upload_as_project_file:
    refresh_notes:
  return_contract:
    required_return_fields:
      - status
      - changed_files
      - unchanged_files
      - created_files
      - deleted_files
      - forbidden_paths_touched
      - pre_write_refs
      - post_write_refs
      - diff_summary
      - eof_check_results
      - validation_output
      - commit_sha
      - push_status
      - project_refresh_requirements
      - source_limitations
      - residual_risks
      - exact_next_move
```

A storage packet, dependency packet, handoff, card, or copy-paste packet is never parent lifecycle completion by itself when mutation is required for the current START goal.

## Source Requirements

Read exact sources needed for the current bootstrap scope.

Always required:

- `workflow_v3/control_plane/PROCEDURE_REGISTRY.md`
- `workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md`
- `workflow_v3/control_plane/CHAT_LIFECYCLE_PROTOCOL.md`
- `workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md`
- `workflow_v3/control_plane/CHAT_FINISH_PROTOCOL.md`

Required when generating or validating setup package content:

- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTALLER.md`
- `workflow_v3/project_setup/DIRECTION_PROJECT_SETUP_VALIDATION_CHECKLIST.md`
- `workflow_v3/project_setup/DIRECTION_ROOT_BOOTSTRAP_LAUNCH_PACKET_TEMPLATE.md`
- `workflow_v3/templates/DIRECTION_PROJECT_BINDING_TEMPLATE.md`
- `workflow_v3/project_setup/PER_DIRECTION_PROJECT_INSTRUCTIONS_SOURCE_TEMPLATE.md`
- `workflow_v3/project_setup/PER_DIRECTION_PROJECT_FILES_MANIFEST_TEMPLATE.md`

Required when producing a post-bootstrap Direction Definition continuation:

- `workflow_v3/project_setup/DIRECTION_DEFINITION_LAUNCH_PACKET_TEMPLATE.md`
- `workflow_v3/procedures/DIRECTION_DEFINITION_PROCEDURE.md` if the next procedure source must be validated in the same result

Required when preparing persistence boundaries:

- `workflow_v3/control_plane/STORAGE_UPDATE_PROTOCOL.md`
- `workflow_v3/templates/STORAGE_UPDATE_PACKAGE_TEMPLATE.md`
- `workflow_v3/procedures/STORAGE_UPDATE_PROCEDURE.md` when validating a storage_update continuation/package shape

Source authority rules:

- exact repository files at named repo/path/ref win;
- Project Files/Sources are cache/context only;
- chat memory is not accepted state;
- Project title is not binding authority;
- old `directions/**` or legacy Direction files are legacy_evidence only unless separately admitted;
- candidate docs remain candidate context unless accepted through admitted procedure;
- if exact source is missing, truncated, stale, or conflicting, stop or state explicit source limitations.

## Context Classification

Classify relevant inputs before material conclusions:

```yaml
canonical_repository_source:
  - exact files read from repository/runtime refs
accepted_record:
  - accepted runtime binding, accepted root package, or accepted update authority when exact ref exists
current_human_input:
  - direction_id, setup request, explicit setup confirmation, corrections, project name/title hint
verified_excerpt:
  - exact excerpt with source path/ref and enough integrity evidence
Project_Files_cache_context:
  - non-authoritative cache only
candidate_context_for_direction_definition:
  - user-provided outcome, goals, tracks, product ideas, constraints, or strategy during bootstrap
candidate_context:
  - unaccepted setup package, proposed binding, proposed project setup source
legacy_evidence:
  - old Direction files or migration/adoption evidence
adapter_evidence:
  - GitHub/file readback, code-assistant return, storage return, validation/check result
unknown_unverified:
  - any source not read or not matched to exact authority
```

## Complexity Selector

Use the smallest sufficient bootstrap path:

- `inline_blocked`: required source/input is missing, setup mode is wrong, or semantic work is requested.
- `identity_only`: normalize/report direction_id and setup status without preparing a runtime package.
- `candidate_package`: prepare setup-only root package and validation plan without mutation.
- `storage_package_candidate`: prepare complete candidate Storage Update Package, but do not execute it.
- `delegated_or_tool_mediated`: open visible `DEPENDENCY_CALL` only when exact mutation/check/repository work is admitted and bounded.
- `already_bootstrapped`: exact accepted runtime root/binding already exists and no setup package should be created.

Research posture: external research is not required. Use exact internal Workflow v3 source authority.

## Stage Cards

Runtime stage normalization: each material stage emits `STAGE_RESULT` and waits for `CONTINUE` / `ДАЛЬШЕ` before the next material stage unless the next step is an internal check. Runtime must not compress declared stages into a simple, compact, shortcut, or single-stage path.

### Stage 0 - Bootstrap Surface Admission

```text
stage_id: bootstrap_surface_admission
stage_type: material stage
purpose: Confirm this RUN is the selected setup-only root bootstrap procedure and not semantic Direction Definition, product work, Governance maintenance, or storage execution.
inputs: START_CONTRACT, Procedure Registry metadata, current user request, project type, setup mode.
required_stage_result: selected_entrypoint, selected_procedure_path, project_type, setup_mode, source authority statement, boundary classification.
gate: PASS if selected_entrypoint is direction_project_root_bootstrap, kind is core, project type is ordinary_direction_project, and setup mode is setup_only_root_bootstrap. STOP if this is Governance maintenance, product work, semantic definition, storage_update, or unregistered action.
utility_allowed_if: Exact source read is needed to verify registry/procedure/lifecycle source.
blocked_if: selected source is missing, project type is wrong, setup mode is not setup-only, or request requires semantic Direction content.
```

### Stage 1 - Direction ID and Legacy Policy Gate

```text
stage_id: direction_id_and_legacy_policy_gate
stage_type: material stage
purpose: Normalize one path-safe direction_id and classify legacy/input policy without importing legacy state.
inputs: user-provided direction id/name, project title hint, legacy policy, candidate semantic text.
required_stage_result: normalized direction_id, rejected/accepted normalization notes, legacy_policy, candidate_context_for_direction_definition, unresolved input questions.
gate: PASS if one concrete path-safe direction_id is present and legacy policy is not_used, legacy_evidence_read_only, or migration_or_adoption_requires_separate_package. STOP if direction_id is unsafe, missing, multi-Direction, or depends on Project title/memory as authority.
utility_allowed_if: None by default; exact source read may be used only to verify a named existing binding/path.
blocked_if: direction_id contains unsafe path characters, is a placeholder, conflicts with exact binding evidence, or user asks to import legacy state in this procedure.
```

### Stage 2 - Root State and Binding Evidence Gate

```text
stage_id: root_state_and_binding_evidence_gate
stage_type: material stage
purpose: Determine whether an accepted runtime root or binding already exists using exact repo/path/ref evidence only.
inputs: normalized direction_id, repository/ref, exact runtime root path, exact binding path, accepted_root_package_ref if any.
required_stage_result: root_state_classification, binding_evidence, source_read_limitations, conflict status.
gate: PASS if exact evidence shows runtime root missing, setup/adoption need, already_bootstrapped, or a bounded conflict/blocker. STOP if binding evidence is conflicting, stale, unreadable, or cannot be resolved without inference.
utility_allowed_if: Exact GitHub/file read is needed for named runtime root/binding/current status paths.
blocked_if: source read is required but unavailable, binding conflicts with direction_id, existing accepted root should be used instead of bootstrapped, or broad search would be needed to infer state.
```

### Stage 3 - Setup-Only Package Design

```text
stage_id: setup_only_package_design
stage_type: material stage
purpose: Build the setup-only root package design with placeholder state, binding, project setup sources, and next move.
inputs: direction_id, root_state_classification, setup source templates, binding template, project setup templates, explicit setup confirmation when needed.
required_stage_result: candidate setup-only package, target paths, placeholder statuses, binding plan, per-Direction project setup source plan, candidate_context handling.
gate: PASS if the package is setup-only and uses only placeholder semantic statuses. REWORK if package content is too vague but repairable. STOP if it includes accepted semantic content, legacy import, product work, or unbounded paths.
utility_allowed_if: Exact source reads for setup templates or current target files are needed.
blocked_if: explicit setup confirmation is required but missing, package would define Direction semantics, or package would create/update unlisted paths.
```

### Stage 4 - Storage and Dependency Boundary Gate

```text
stage_id: storage_and_dependency_boundary_gate
stage_type: material stage
purpose: Decide whether the result remains candidate-only, becomes a candidate Storage Update Package, or opens a visible dependency call.
inputs: candidate setup package, mutation_policy, storage protocol, storage package template, routing/dependency protocol, exact path boundaries.
required_stage_result: storage_boundary_decision, storage_update_package_candidate if applicable, dependency_call_need, allowed files, forbidden paths, validation and return contract.
gate: PASS if no direct mutation occurs and every possible write path is exact, visible, bounded, validated, and return-verifiable. DEPENDENCY_CALL only if external mutation/check work is admitted and complete. STOP if mutation is requested without exact authority, paths, validation, or return contract.
utility_allowed_if: Dependency call is needed for exact mutation/check/readback and the complete DEPENDENCY_CALL packet is emitted.
blocked_if: hidden write, unbounded Codex/storage request, missing storage authority, broad globs, missing validation, or actual Project UI/File refresh is requested.
```

### Stage 5 - Validation and Refresh Classification

```text
stage_id: validation_and_refresh_classification
stage_type: material stage
purpose: Validate setup-only boundaries, placeholder values, source integrity needs, Project setup payload requirements, and refresh categories.
inputs: setup package, binding plan, project setup source plan, storage/dependency boundary decision, validation checklist.
required_stage_result: validation_result, placeholder_status_check, no_semantic_content_check, path_boundary_check, payload_measurement_need, refresh_classification, residual risks.
gate: PASS if validation checks are explicit and no setup-only boundary violation remains. PASS_WITH_RISK only when limitations are explicit and do not affect safety. STOP if validation is absent or boundary checks fail.
utility_allowed_if: Exact payload measurement/check may be used when concrete Project Instructions source is generated.
blocked_if: Project UI update is implied, Project Files/Sources refresh is implied, payload count is missing when required, semantic content appears, or storage/dependency returns are open/unverified.
```

### Stage 6 - Closure

```text
stage_id: closure
stage_type: material stage
purpose: Return the setup-only bootstrap result, CLOSURE_CHECK, FINISH readiness, and exact continuation.
inputs: all previous stage outputs, dependency return evidence if any, validation result, completion contract.
required_stage_result: root_bootstrap_result, CLOSURE_CHECK, source limitations, residual risks, continuation decision.
gate: PASS if the completion contract is satisfied or blocked explicitly. STOP if required dependency return is open, missing, or unverified; required validation is absent; or actual result is only a package/card/handoff.
utility_allowed_if: None.
blocked_if: open_dependencies is non-empty, dependency return is missing/unverified, validation/evidence is missing, or continuation would carry unfinished dependency work.
```

## Gate Outcomes

Use:

- `PASS` when a stage can safely continue or close;
- `PASS_WITH_RISK` only when limitations are explicit and do not change setup/write safety;
- `REWORK` when a bounded input/package issue can be repaired before mutation;
- `EXPAND` only for exact source reads, exact validation checks, or exact package/binding inspection;
- `STOP` for missing source, unsafe direction_id, semantic boundary crossing, source conflict, missing validation, or missing authority;
- `DEPENDENCY_CALL` only for visible bounded dependency work;
- `DEPENDENCY_RETURN` only when verifying returned evidence from a matching dependency call.

## Optional Expansion

Allowed expansion:

- exact repository/file read for named sources;
- exact current runtime root/binding/status readback;
- exact setup template source inspection;
- exact storage package shape validation;
- exact payload character count measurement when a concrete Project Instructions source is generated;
- bounded dependency call for exact mutation/check/readback when admitted.

Forbidden expansion:

- semantic Direction authoring;
- legacy migration/adoption by implication;
- broad repository discovery to infer Direction identity;
- product planning or product execution;
- Direction Definition launch inside the same RUN;
- Project UI update;
- Project Files/Sources refresh;
- hidden Codex/storage/check launch;
- accepting this procedure's own candidate output.

## Research Policy

External/current research is not required.

This procedure relies on exact internal Workflow v3 repository sources, setup templates, control-plane protocols, storage protocol, and runtime state evidence.

If an external tool/provider behavior is uncertain and affects write safety, STOP with a bounded blocker or emit a complete visible `DEPENDENCY_CALL` only when the call boundary, expected return, and verification are exact.

## Routing / Dependency Policy

```yaml
routing_dependency_policy:
  allowed_when:
    - exact source read is needed and cannot be completed inline
    - exact current runtime root/binding readback is needed
    - exact validation/check evidence is needed
    - repository/runtime mutation is explicitly admitted and exact write boundaries are available
  allowed_dependency_types:
    - support_adapter_dependency for non-mutating source readback, validation checks, and reporting support
    - storage_persistence_dependency for candidate storage_update package boundaries
    - code_repository_dependency for exact repository mutation through Codex/code assistant only
  forbidden_when:
    - dependency call would define semantic Direction content
    - dependency call would import legacy state
    - dependency call would create Spine/Map/Front semantic content
    - dependency call would create Work Graph or Work Contract
    - dependency call would perform hidden mutation
    - dependency call would update actual ChatGPT Project UI
    - dependency call would refresh Project Files/Sources directly
    - dependency call would launch Direction Definition before root bootstrap closure
    - dependency call boundary uses placeholders, broad globs, or "same as above"
  return_verification:
    - match dependency_id
    - confirm same selected main procedure resumes
    - classify return as evidence, not accepted state
    - verify branch/commit/ref when repository mutation occurred
    - verify only allowed paths changed
    - verify forbidden paths untouched
    - verify EOF markers where required
    - verify validation output
    - verify payload character count where Project Instructions source changed
    - verify project refresh categories
  same_main_procedure_resume: true
```

`CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN` and `UTILITY_CALL` / `UTILITY_RETURN` may appear only as compatibility aliases for `DEPENDENCY_CALL` and `DEPENDENCY_RETURN`.

CHECK, FINISH, and CLOSED are blocked while any required dependency return is open, missing, unverified, or required validation/evidence is absent.

## Checkpoint Policy

Checkpoint when:

- direction_id normalization is ambiguous;
- legacy policy is unclear;
- root/binding evidence conflicts;
- user asks to include semantic content in setup;
- runtime root package would be prepared and explicit setup confirmation is missing;
- mutation is requested but storage/dependency authority is not exact;
- per-Direction Project Instructions source would be generated and payload measurement or refresh classification is not available;
- dependency call is needed.

No checkpoint is required for a blocked result that names exact missing input/source.

## Completion Contract

```text
completion:
  result: setup-only root bootstrap result with status candidate_package_ready, storage_package_candidate_ready, applied_after_verified_dependency_return, already_bootstrapped, or blocked; including direction_id, setup-only package/binding/setup-source boundary, validation, refresh classifications, source limitations, residual risks, and exact continuation
  proof: direction_id validation, setup-only boundary checks, exact source/binding evidence, placeholder status plan, storage/dependency boundary decision, validation evidence, dependency-return verification when applicable, CLOSURE_CHECK, and continuation boundary are recorded
  blocked_if: direction_id is missing or unsafe, setup mode is not setup-only, exact sources are missing or conflicting, accepted runtime root/binding already exists and should not be recreated, semantic Direction content is required, legacy import/adoption is requested, storage/write authority is absent, path boundaries or validation are incomplete, actual Project UI/File refresh is requested, or required dependency return is open/missing/unverified
```

## Output Contract

```yaml
root_bootstrap_result:
  status: candidate_package_ready | storage_package_candidate_ready | applied_after_verified_dependency_return | already_bootstrapped | blocked
  direction_id:
  project_type: ordinary_direction_project
  setup_mode: setup_only_root_bootstrap
  root_state_classification: direction_runtime_missing | direction_adoption_needed | already_bootstrapped | binding_conflict | source_unverified | blocked

  candidate_context_for_direction_definition:
    present: true | false
    summary:
    authority_classification: candidate_context_only

  setup_only_root_package:
    package_status: candidate | applied_verified | not_created | blocked
    runtime_root:
    runtime_config_files:
      - path:
        purpose:
    runtime_state_placeholders:
      - path:
        placeholder_status:
        semantic_content_allowed: false
    current_status_plan:
    current_next_move_plan:
    no_semantic_content_check:
    no_legacy_import_check:

  project_binding_plan:
    binding_source_path:
    binding_status: candidate | accepted | superseded | not_created
    source_authority:
    project_title_is_not_authority: true
    conflict_policy:

  project_setup_source_plan:
    chatgpt_project_instructions_source_path:
    project_files_manifest_path:
    payload_measurement:
      required: true | false
      measured_chars:
      target_max_chars:
      hard_max_chars:
      verdict:
    manual_project_instruction_ui_update_required:
    project_files_sources_default:
    request_only_sources:
    do_not_upload_as_project_file:

  storage_boundary:
    direct_mutation_performed: false
    storage_update_package_candidate:
      present: true | false
      package_id:
      allowed_files:
      forbidden_paths:
      validation_checks:
      return_contract:
    dependency_call:
      opened: true | false
      dependency_id:
      dependency_type:
      execution_surface:
      expected_return:
      verification_required_on_return:
      compatibility_aliases:
        child_call_id_if_legacy:
    dependency_return_verification:
      required: true | false
      status: not_applicable | verified | missing | unverified | blocked

  validation:
    source_integrity:
    direction_id_check:
    placeholder_status_check:
    no_semantic_content_check:
    no_project_ui_update_check:
    no_project_files_refresh_execution_check:
    path_boundary_check:
    storage_package_check:
    dependency_return_check:
    refresh_classification_check:

  project_refresh_requirements:
    project_instruction_ui_update_required:
    project_sources_files_refresh_required:
    request_only_sources_refresh_required:
    do_not_upload_as_project_file:
    refresh_notes:

  source_read_limitations:
  residual_risks:
  CLOSURE_CHECK:
  FINISH_PACKET_after_explicit_FINISH:
  NEXT_CHAT_CARD_or_no_next_chat_needed_after_explicit_FINISH:
```

## Continuation Policy

Continuation depends on the bootstrap result status.

If `status: applied_after_verified_dependency_return` or exact accepted root/binding evidence proves setup-only root exists:

```yaml
NEXT_CHAT_CARD:
  title: Launch Direction Definition
  why: setup-only root exists and CURRENT_NEXT_MOVE is launch_direction_definition
  main_procedure_to_start: launch_direction_definition
  context_to_paste: include direction_id, runtime_root, current_status_path, current_next_move_path, project_binding_source_path, source refs, and candidate_context_for_direction_definition if any
  expected_result: bounded Direction Definition next-step packet or blocked result
  evidence_or_return_needed: exact CURRENT_STATUS and CURRENT_NEXT_MOVE readback
  start_instruction: START with Direction Definition procedure after reading exact binding/current status/current next move
```

If `status: storage_package_candidate_ready` and persistence has not been applied:

```yaml
NEXT_CHAT_CARD:
  title: Persist Setup-Only Root Package
  why: setup-only root package is candidate-only and requires admitted persistence before Direction Definition
  main_procedure_to_start: persist_accepted_state
  context_to_paste: complete Storage Update Package with exact authority, paths, changes, validation, and return fields
  expected_result: storage update result with changed/no-op/blocked evidence
  evidence_or_return_needed: verified changed files, refs, EOF checks, validation, refresh categories, commit/push status
  start_instruction: START with storage_update only if the Storage Update Package is complete and admitted
```

If `status: candidate_package_ready` without storage authority:

```yaml
NEXT_CHAT_CARD:
  title: Accept or Persist Bootstrap Candidate
  why: setup-only root package exists only as candidate output
  main_procedure_to_start: accept_candidate_entity | persist_accepted_state
  context_to_paste: candidate setup-only root package and exact acceptance/storage question
  expected_result: acceptance/update decision or blocked result
  evidence_or_return_needed: explicit accepted update authority before persistence
  start_instruction: START with the appropriate registered owner procedure
```

If `status: already_bootstrapped`:

```yaml
NEXT_CHAT_CARD:
  title: Continue From Binding
  why: accepted runtime root already exists
  main_procedure_to_start: status_review | launch_direction_definition
  context_to_paste: exact binding/current status/current next move refs
  expected_result: status/continuation from exact binding
  evidence_or_return_needed: exact CURRENT_STATUS and CURRENT_NEXT_MOVE
  start_instruction: START with the selected registered owner procedure
```

If `status: blocked`:

```yaml
no_next_chat_needed:
  reason: blocked until exact missing source/input/authority is supplied
```

A `NEXT_CHAT_CARD` is post-closed continuation only. It must not carry unfinished dependency work from the current START goal and must not replace a required `DEPENDENCY_CALL`.

## Eval / Quality Checks

Procedure definition checks:

- Purpose is specific and bounded.
- Trigger and non-trigger are distinguishable.
- Required inputs are explicit.
- Source requirements are explicit.
- Context classification exists.
- Complexity selector exists.
- Stage Cards produce intermediate outputs and real gates.
- Dependency-call decision gate is explicit.
- Output contract is downstream-usable.
- Stop conditions prevent invention, hidden mutation, hidden acceptance, hidden procedure switching, legacy import, and semantic boundary crossing.
- Completion result is not only a package, handoff, card, dependency packet, copy-paste packet, storage packet, or NEXT_CHAT_CARD.
- Procedure closure uses CLOSURE_CHECK, FINISH_PACKET, and NEXT_CHAT_CARD or no_next_chat_needed correctly.
- Canonical `workflow_v3/procedures/**` location and `*_PROCEDURE.md` naming are preserved.
- Registry kind remains `core`.

Setup-only checks:

- `direction_id` is valid and path-safe.
- setup mode is `setup_only_root_bootstrap`.
- Project type is `ordinary_direction_project`.
- root package uses only setup-only placeholder statuses.
- `DIRECTION_SPINE` is `pending_definition`.
- `DIRECTION_MAP` is `pending_definition`.
- `ACTIVE_FRONT` is `none_selected` or `pending_definition`.
- `CURRENT_STATUS` is `setup_only_root_created` with `semantic_definition_status: pending_definition`.
- `CURRENT_NEXT_MOVE` is `launch_direction_definition`.
- candidate semantic text is classified as `candidate_context_for_direction_definition`.
- no semantic Direction content is accepted.
- no legacy state is imported.
- no Project UI update or Project Files/Sources refresh is performed.

Storage/dependency checks:

- direct mutation is not performed by this core procedure.
- storage package has exact paths, changes, validation, authority, and return fields when produced.
- dependency calls are visible, bounded, and same-main-procedure.
- required dependency returns are verified before reliance.
- CHECK/FINISH block on open, missing, or unverified dependency returns.

## Stop Conditions

Stop with a typed blocker when:

- selected entrypoint/path/kind does not match this procedure;
- request is not setup-only root bootstrap;
- user asks for semantic Direction Definition inside bootstrap;
- `direction_id` is missing, unsafe, ambiguous, or multi-Direction;
- setup mode is missing or not `setup_only_root_bootstrap`;
- Project type is not ordinary Direction Project;
- exact required source is missing, truncated, stale, or conflicting;
- root/binding evidence conflicts and cannot be resolved from exact source;
- accepted runtime root already exists and the user asks to recreate it without admitted repair/migration authority;
- legacy import/adoption is requested;
- storage/write authority is absent or ambiguous;
- path boundaries use globs, broad directories, placeholders, or "same as previous";
- validation is missing;
- actual ChatGPT Project UI update is requested;
- actual Project Files/Sources refresh is requested;
- dependency call would be hidden, unbounded, or semantic;
- required dependency return is open, missing, or unverified;
- completion proof cannot be produced.

Common blocked reason labels:

```text
SOURCE_INTEGRITY_STOP
BOUNDARY_CROSSING_STOP
DIRECTION_ID_REQUIRED
DIRECTION_ID_UNSAFE
SETUP_MODE_NOT_SETUP_ONLY
BINDING_CONFLICT
RUNTIME_ROOT_ALREADY_EXISTS
LEGACY_IMPORT_NOT_ADMITTED
SEMANTIC_CONTENT_NOT_ADMITTED
WRITE_NOT_ADMITTED
STORAGE_PACKAGE_INCOMPLETE
VALIDATION_REQUIRED_STOP
DEPENDENCY_RETURN_REQUIRED_STOP
COMPLETION_CONTRACT_NOT_SATISFIED
```

## Procedure Closure

RUN closes only through `CLOSURE_CHECK`.

`CLOSURE_CHECK` must compare actual result to this procedure's completion contract:

```yaml
CLOSURE_CHECK:
  selected_entrypoint: direction_project_root_bootstrap
  selected_procedure_path: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
  completion_contract:
  actual_result:
  proof:
  open_dependencies:
  missing_dependency_returns:
  unverified_dependency_returns:
  required_validation_evidence:
  gaps:
  decision: pass | return_to_run_repair | blocked
  next_action:
```

CHECK may request FINISH only when:

- setup-only bootstrap result satisfies the completion contract; or
- blocked completion is explicit with exact missing source/input/authority; and
- no required dependency return is open, missing, or unverified; and
- required validation/evidence is present.

FINISH starts only after standalone `FINISH` or `ФИНИШ`.

FINISH must return `FINISH_PACKET` with:

- selected entrypoint/path;
- completion contract;
- CLOSURE_CHECK;
- finish audit;
- result;
- evidence;
- validation;
- project refresh requirements;
- residual risks;
- continuation.

After FINISH passes, the chat is CLOSED for material work.

`NEXT_CHAT_CARD` is post-closed continuation only. It must not represent unfinished dependency work, must not replace `DEPENDENCY_CALL`, and must not be used as evidence that root bootstrap completed.

END_OF_FILE: workflow_v3/procedures/DIRECTION_PROJECT_ROOT_BOOTSTRAP_PROCEDURE.md
