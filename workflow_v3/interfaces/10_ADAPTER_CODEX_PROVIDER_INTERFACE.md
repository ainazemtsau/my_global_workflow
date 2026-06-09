# Code Assistant and Provider Interface

status: interface_summary

## Purpose

This interface summarizes the code-assistant/provider boundary for Workflow v3. Code/repository mutation is a `code_repository_dependency` and runs only through Codex/code assistant. Non-mutating support adapters are separate dependency surfaces.

## Authority

Routing and dependency type selection is governed by:

```text
workflow_v3/control_plane/ROUTING_AND_DEPENDENCY_PROTOCOL.md
```

Support adapter packet compatibility is governed by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

Provider returns are evidence. They are not accepted state, procedure completion, or ChatGPT FINISH by themselves.

## Code Repository Dependency

A selected main procedure may call Codex/code assistant only through visible `DEPENDENCY_CALL` with `dependency_type: code_repository_dependency` when the current stage needs repository/code mutation, patching, branch creation, commits, pushes, file writes, implementation, write probes, or repository-side validation requiring writes.

The parent enters `RUN_WAITING_FOR_DEPENDENCY_RETURN`; the return must come back as `DEPENDENCY_RETURN` / `CODEX_RETURN_PACKET`, match the call, resume the same selected main procedure, and pass `DEPENDENCY_RETURN_VERIFICATION` before reliance. `CHILD_PROCEDURE_CALL` / `CHILD_PROCEDURE_RETURN` and legacy `UTILITY_CALL` / `UTILITY_RETURN` labels are compatibility aliases only.

ChatGPT parent may draft packets and verify return evidence. It must not execute repository writes, write probes, branch creation, commits, pushes, or patch application.

## Support Adapter Dependencies

Non-mutating check, research, analysis, evidence, and real human decision support use `support_adapter_dependency`. GitHub or file access from ChatGPT parent is read or verification only unless a separate admitted write executor returns verifiable write evidence.

## Code-Assistant Dependency Packet

A code-assistant dependency packet should include:

```text
dependency_id:
dependency_type: code_repository_dependency
repository:
base_ref:
target_branch_or_branch_policy:
purpose:
goal:
source_files_to_read:
allowed_paths:
forbidden_paths:
required_changes:
validation:
stop_conditions:
commit_push_instructions:
requested_return_fields:
project_refresh_requirements:
parent_verification_contract:
unresolved_until_returned:
```

## Verification

Returned provider evidence should be checked for branch/ref, commit or artifact identity, changed files, forbidden-path cleanliness, validation output, EOF markers when relevant, project refresh categories, push/publication status when relevant, and residual risks.

END_OF_FILE: workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md
