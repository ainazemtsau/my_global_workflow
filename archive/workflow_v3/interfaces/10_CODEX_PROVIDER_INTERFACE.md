# Code Assistant Development Runtime Interface

status: interface_summary

## Purpose

This interface summarizes the Workflow v3 boundary for repository mutation through a Code Assistant Development Runtime. Codex is the current execution surface instance. The canonical dependency type is `code_repository_dependency`.

Dependency returns are evidence only. They are not accepted state, procedure completion, ChatGPT CHECK, ChatGPT FINISH, or CLOSED by themselves.

## Authority

Routing and dependency type selection is governed by:

```text
workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md
```

Support dependency packet is governed by:

```text
workflow_v3/control_plane/SUPPORT_DEPENDENCY_PROTOCOL.md
```

The code repository dependency schema is governed by:

```text
workflow_v3/procedures/CODE_REPOSITORY_DEPENDENCY_PROCEDURE.md
```

Return verification is governed by:

```text
workflow_v3/procedures/CODE_REPOSITORY_DEPENDENCY_RETURN_VERIFICATION_PROCEDURE.md
```

## Code Repository Dependency

A selected main procedure may call the Code Assistant Development Runtime only through visible `DEPENDENCY_CALL` with `dependency_type: code_repository_dependency` when the current stage needs repository/code mutation, patching, file writes, implementation, write probes, or repository-side validation requiring writes.

The ChatGPT parent sends intent, source authority, path boundaries, validation requirements, target integration evidence requirements, and acceptance boundary. The Code Assistant Development Runtime owns internal workspace/ref/branch/commit/rebase/merge/push mechanics.

The parent enters `RUN_WAITING_FOR_DEPENDENCY_RETURN`; the return must come back as `DEPENDENCY_RETURN`, match the call, resume the same selected main procedure, and pass dependency return verification before reliance. Prior packet labels are unsupported.

ChatGPT parent may draft dependency calls and verify returned evidence. It must not execute repository writes, write probes, ref changes, commits, pushes, integration, or patch application.

## DEPENDENCY_CALL

A `code_repository_dependency` call includes:

```text
dependency_id:
dependency_type: code_repository_dependency
execution_surface: Code Assistant Development Runtime
repository:
repository_role:
target_integration_ref:
expected_base_commit_sha:
workspace_policy_id:
integration_policy_id:
purpose:
goal:
source_files_to_read:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_conditions:
project_refresh_requirements:
expected_return_contract:
parent_verification_contract:
unresolved_until_returned:
```

## DEPENDENCY_RETURN

The return contract requires evidence for:

```text
target_integration_ref:
expected_base_commit_sha:
observed_base_commit_sha:
base_matches_expected:
workspace_binding_used:
internal_work_ref:
internal_branch_if_any:
  return_only: true
changed_files:
forbidden_paths_touched:
unlisted_paths_touched:
validation_output:
result_commit_sha:
integration_required:
integration_status:
final_target_commit_sha:
target_contains_result_commit:
target_remote_verification:
push_status:
pending_integration_reason:
exact_next_action_if_not_integrated:
project_refresh_requirements:
residual_risks:
```

## Verification

Returned dependency evidence must be checked for target integration ref, expected and observed base commit SHA, workspace binding, internal work evidence, changed files, forbidden-path cleanliness, unlisted paths, validation output, EOF markers when relevant, project refresh categories, result commit, integration status, final target commit, target containment proof, remote verification, push status, pending integration reason, exact next action when not integrated, and residual risks.

The code assistant must not claim acceptance, CHECK, FINISH, or CLOSED.

END_OF_FILE: workflow_v3/interfaces/10_CODEX_PROVIDER_INTERFACE.md
