# Transport Contract Checklist

Use this checklist to validate runtime transport contracts.

## Checklist

- `stage_launch.v1`
- `stage_result.v1`
- `context_request.v1`
- `human_decision.v1`
- `stop.v1`
- `repository_patch.v1`
- `execution_log_entry.v1`
- `documentation_maintenance_gate`
- `changed_files_context_refresh`
- `codex_repository_maintenance_apply.v1`

## Rules

- Packet contracts come from `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`.
- Do not invent local packet schemas.
- Findings must be recorded in `FINDING_REGISTER.md`.

## GitHub file-read verification checks

For any workflow output that depends on a GitHub repository file read, check:

- no `truncated due to tool response token budget` marker is present;
- no `Full entry omitted because the tool response token budget was exhausted` marker is present;
- compact search result was not treated as full file content;
- expected tail anchor or end-of-file evidence is present when required;
- exact stage prompt reads are full before stage execution;
- long runtime files required in every chat are available through Project Files runtime cache or verified full GitHub read;
- if full-file availability cannot be verified, the output returns Context Request instead of continuing material work.

A partial GitHub read is a transport failure, not acceptable runtime context.

## Cross-Direction rollout verification checks

For shared workflow runtime changes, verify:

- all active Direction Projects are identified;
- central setup docs are updated if needed;
- per-Direction Project Instructions exist or are updated if needed;
- each active Direction default Project Files list includes `00-07`;
- each active Direction context index includes shared runtime cache files;
- `project_files_cache_refresh_required` is returned for every affected ChatGPT Project;
- sibling Directions are not silently skipped.

A shared workflow change that updates only Workflow Governance but leaves other active Directions stale is incomplete unless the patch explicitly proves those Directions are unaffected.
