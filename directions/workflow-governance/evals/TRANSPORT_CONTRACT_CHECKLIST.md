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
- Stage prompts remain request-only context and are not default Direction Project Files.
- `M0_DIRECTION_MAP` launch requires exact prompt availability like any other stage; unavailable prompt context returns Context Request or registry amendment need.
- Findings must be recorded in `FINDING_REGISTER.md`.

## GitHub file-read verification checks

For any workflow output that depends on a GitHub repository file read, check:

- no `truncated due to tool response token budget` marker is present;
- no `Full entry omitted because the tool response token budget was exhausted` marker is present;
- compact search result was not treated as full file content;
- expected tail anchor or end-of-file evidence is present when required;
- exact stage prompt reads are full before stage execution;
- launch/context packets include `08_DIRECTION_MAP.md` when Direction Project Files are required;
- long runtime files required in every chat are available through Project Files runtime cache or verified full GitHub read;
- if full-file availability cannot be verified, the output returns Context Request instead of continuing material work.

A partial GitHub read is a transport failure, not acceptable runtime context.

## Lifecycle State Reconciliation transport checks

For any material stage close, Codex return, or next launch where lifecycle state may have changed, check:

- `stage_result.v1` includes `lifecycle_state_reconciliation` when triggered;
- `stage_launch.v1` includes `project_files_state` and `fresh_sources_for_stage` when Project Files are stale or overridden;
- `documentation_maintenance_gate` distinguishes physical file updates from semantic runtime projection changes;
- `codex_repository_maintenance_apply.v1` requires logical runtime state classification;
- `project_files_cache_refresh_required: false` is valid only when no cached file changed and no logical runtime state made Project Files stale;
- a stale-but-nonblocking override names the exact next stage and exact fresh sources;
- stale override does not authorize general future routing.

## Structural EOF transport checks

For every changed file that defines `END_OF_FILE`, check:

- EOF marker appears exactly once;
- EOF marker is the last non-whitespace content;
- no append operation placed content below EOF;
- read-back / diff verification reports EOF validation;
- structural failure blocks next material launch until repaired.

## Direction Map transport checks

- Required Direction Project File context is `00-08` when full Direction Project Files are in scope.
- `08_DIRECTION_MAP.md` is routing context only; transport packets must not treat it as a transition authority table.
- Repository maintenance returns Project Files refresh requirements when `08_DIRECTION_MAP.md` or shared runtime cache files change.
- Checklist/eval updates do not modify canonical transport templates.

## Cross-Direction rollout verification checks

For shared workflow runtime changes, verify:

- all active Direction Projects are identified;
- central setup docs are updated if needed;
- per-Direction Project Instructions exist or are updated if needed;
- each active Direction default Project Files list includes `00-08`;
- each active Direction context index includes shared runtime cache files;
- `project_files_cache_refresh_required` is returned for every affected ChatGPT Project;
- sibling Directions are not silently skipped.

A shared workflow change that updates only Workflow Governance but leaves other active Directions stale is incomplete unless the patch explicitly proves those Directions are unaffected.

## Branch / Workstream Transport Checklist

Required transport templates:

- `workflow/transport/TOPOLOGY_LAUNCH_BUNDLE.md`
- `workflow/transport/WORKSTREAM_LAUNCH_CARD.md`
- `workflow/transport/WORKSTREAM_RESULT_CARD.md`

Required invariants:

- Topology Launch Bundle is one terminal launch artifact, not a new stage.
- Workstream Launch Card targets a registry-valid stage.
- Workstream Result Card is compact by default.
- Heavy artifact full return defaults to false.
- Branch cards include dependency policy.
- Branch cards include artifact policy.
- Branch result cards include synthesis readiness.
- Branch result cards include state-policy confirmation.
- Branch state mutation is forbidden unless explicitly approved and scoped.
