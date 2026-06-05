# Adapter Code and Provider Interface

status: interface_summary

## Purpose

This interface summarizes code-assistant and provider boundaries for Workflow v3. It is provider-neutral: Codex, Claude Code, future code assistants, GitHub/file tools, research agents, check jobs, and human decisions are utility surfaces when used during RUN.

## Authority

Provider-neutral utility calls are governed by:

```text
workflow_v3/control_plane/UTILITY_ADAPTER_PROTOCOL.md
```

Provider returns are evidence. They are not accepted state, procedure completion, or ChatGPT FINISH by themselves.

## Utility Use

A selected main procedure may call a provider only through visible `UTILITY_CALL` when the current stage needs it. The return must come back as `UTILITY_RETURN`, match the call, resume the same selected main procedure, and be verified before reliance.

## Code-Assistant Package

A code-assistant package should include:

```text
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
```

## Verification

Returned provider evidence should be checked for branch/ref, commit or artifact identity, changed files, forbidden-path cleanliness, validation output, EOF markers when relevant, project refresh categories, push/publication status when relevant, and residual risks.

END_OF_FILE: workflow_v3/interfaces/10_ADAPTER_CODEX_PROVIDER_INTERFACE.md