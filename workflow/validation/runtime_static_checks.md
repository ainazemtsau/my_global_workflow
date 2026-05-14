# Runtime Static Checks Specification

Status: baseline specification
Owner layer: workflow validation
Scope: Workflow vNext-R static runtime consistency

## CHECK 001 — markdown_fence_balance

Scan markdown files for balanced triple-backtick fences.

Result:

- baseline: FAIL on imbalance
- strict: FAIL on imbalance

## CHECK 002 — required_shared_runtime_files_exist

Required files:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

Result:

- baseline: FAIL on missing file
- strict: FAIL on missing file

## CHECK 003 — active_direction_00_07_exist

For every active Direction, verify Project Files `00-07`.

Active Directions:

- `workflow-governance`
- `solo-max-productive`
- `indie-game-development`
- `health-and-beauty`

Result:

- baseline: FAIL on missing file
- strict: FAIL on missing file

## CHECK 004 — active_direction_project_instructions_exist

For every active Direction, verify:

```text
directions/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

Result:

- baseline: FAIL on missing file
- strict: FAIL on missing file

## CHECK 005 — registry_authority_markers

Verify `STAGE_REGISTRY.md` declares itself the sole authority for:

- canonical stage IDs;
- stage identity;
- stage prompt path;
- prompt status;
- target runtime;
- stage activation availability;
- normal stage-to-stage `allowed_next` transitions.

Result:

- baseline: FAIL if missing
- strict: FAIL if missing

## CHECK 006 — runtime_core_no_duplicate_full_transition_table

Runtime core may describe route-selection behavior, but it must not maintain a second full `allowed_next` transition table.

Result:

- baseline: FAIL if full duplicate transition table is detected
- strict: FAIL if full duplicate transition table is detected

## CHECK 007 — registry_validation_rules_present

Verify registry validation rules include these invariants:

- runtime core must not maintain a second full `allowed_next` transition table;
- prompts must not be treated as authority for `allowed_next`;
- stage registry interface files are derived/reference surfaces only;
- transport route fields are snapshots only;
- terminal card types are not canonical stage IDs.

Result:

- baseline: FAIL if missing
- strict: FAIL if missing

## CHECK 008 — deprecated_prompt_delivery_modes_absent

Scan active stage prompts for deprecated prompt delivery modes:

- `request_from_repository`
- `embedded_in_launch_card`
- `pasted_in_current_chat`
- `attached_export`

Result:

- baseline: FAIL if found in active stage prompt body
- strict: FAIL if found in active stage prompt body

## CHECK 009 — ad_wf_rt_001_boundary_present

Every present stage prompt must contain the `AD-WF-RT-001` authority boundary.

Result:

- baseline: FAIL if missing
- strict: FAIL if missing

## CHECK 010 — legacy_transport_shape_scan

Scan `workflow/transport/` for legacy active card shapes:

- `stage_launch_card: 1`
- `stage_result_packet: 1`
- `card_type:`
- `packet_type:`
- `patch_type:`

Result:

- baseline: WARN
- strict: FAIL

## CHECK 011 — transport_apply_template_presence

Verify a dedicated `codex_repository_maintenance_apply.v1` transport template exists under `workflow/transport/`.

Result:

- baseline: WARN if missing
- strict: FAIL if missing

## CHECK 012 — prompt_eof_markers

Verify stage prompts include `END_OF_FILE:` markers.

Result:

- baseline: WARN if missing
- strict: FAIL if missing

## CHECK 013 — authority_eof_markers

Verify EOF markers exist in authority files that already define them:

```text
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

`WORKFLOW_SOURCE_OF_TRUTH.md` may warn if it lacks an EOF marker.

Result:

- baseline: FAIL for required authority EOF marker loss; WARN for short source marker absence
- strict: FAIL for required authority EOF marker loss

## CHECK 014 — stale_rebuild_metadata

Scan runtime-facing files for stale metadata:

- `vNext-R REBUILD`
- `test-active`
- `rebuild root only`
- `Installed from roadmap step`
- `Step 7.`

Result:

- baseline: WARN
- strict: WARN until metadata cleanup is complete; then may become FAIL

## CHECK 015 — prompt_schema_duplication_scan

Scan long prompts for duplicated packet schema blocks and old route examples.

Result:

- baseline: WARN
- strict: WARN until prompt slimming is complete; then may become FAIL

## CHECK 016 — cross_direction_cache_setup_consistency

Check all active Directions have required Project Files, Project Instructions, and cache references.

Check `docs/CHATGPT_PROJECT_SETUP.md` for likely stale setup coverage.

Result:

- baseline: FAIL for missing required Direction files; WARN for stale docs setup blocks
- strict: FAIL for missing required files and, after setup cleanup, stale docs setup blocks

## CHECK 017 — project_files_do_not_contain_stage_prompt_bodies

Direction Project Files must not contain full stage prompt bodies.

Result:

- baseline: FAIL if detected
- strict: FAIL if detected

## CHECK 018 — interface_path_detection

`workflow/interfaces/` may be absent. Interface files may live under:

```text
workflow/stage_registry/interfaces/
```

Result:

- baseline: INFO/WARN only
- strict: INFO/WARN only

## CHECK 019 — codex_return_wave_schema_regression

Validate Codex Return/Wave schema canonicalization after S4-E cleanup.

Hard requirements:

- `workflow/transport/CODEX_RETURN_PACKET.md` declares canonical `workflow_packet: 1`, `type: codex_return`, `schema: codex_return.v1`.
- `workflow/transport/CODEX_WAVE_CARD.md` declares canonical `workflow_packet: 1`, `type: codex_wave`, `schema: codex_wave.v1`.
- transport files document legacy compatibility aliases for:
  - `codex_return_packet.v1`;
  - `packet_type: codex_return_packet`;
  - `codex_wave_card: 1`;
  - `CODEX_RETURN_PACKET_BEGIN/END`;
  - `CODEX_WAVE_CARD_BEGIN/END`;
  - `allowed_targets` / `forbidden_targets`.
- `workflow/codex/CODEX_RETURN_PACKET_CONTRACT.md` references transport as schema authority and preserves DONE evidence discipline.
- `workflow/codex/CODEX_WAVE_CARD_CONTRACT.md` references transport as schema authority and preserves Task Master boundary.
- `workflow/codex/WAVE_RECORD_TEMPLATE.md` documents canonical schema IDs and legacy aliases for historical records.
- stage prompts must not contain legacy Codex schema tokens:
  - `codex_return_packet.v1`;
  - `packet_type: codex_return_packet`;
  - `CODEX_RETURN_PACKET_BEGIN`;
  - `CODEX_RETURN_PACKET_END`;
  - `codex_wave_card: 1`;
  - `CODEX_WAVE_CARD_BEGIN`;
  - `CODEX_WAVE_CARD_END`;
  - `allowed_targets:`;
  - `forbidden_targets:`.

Result:

- baseline: FAIL on missing canonical anchors or unauthorized legacy schema-token residue.
- strict: FAIL on missing canonical anchors or unauthorized legacy schema-token residue.

## Expected baseline summary

The expected first useful run is:

```text
PASS_WITH_CLEANUP
```

This means hard runtime invariants pass and known cleanup debt remains.
