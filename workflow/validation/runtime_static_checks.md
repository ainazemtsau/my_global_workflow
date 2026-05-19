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
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

Result:

- baseline: FAIL on missing file
- strict: FAIL on missing file

## CHECK 003 — active_direction_00_08_exist

For every active Direction, verify Project Files `00-08`.

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

## CHECK 007A — registry_present_prompt_files_exist

For every Runtime Registry row marked `prompt_status: present`, verify the referenced prompt file exists under `workflow/stage_prompts/`.

This includes `workflow/stage_prompts/M0_DIRECTION_MAP.md` when `M0_DIRECTION_MAP` is registered as present.

Result:

- baseline: FAIL on missing present prompt file
- strict: FAIL on missing present prompt file

## CHECK 008 — deprecated_prompt_delivery_modes_absent

Scan active stage prompts for deprecated prompt delivery modes:

- `request_from_repository`
- Markdown-escaped `request\_from\_repository`
- `repository-request`
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

Scan `workflow/transport/` for active legacy transport card shapes.

Active legacy shape tokens are not allowed outside documented compatibility sections:

- `stage_launch_card: 1`
- `stage_result_packet: 1`
- `card_type:`
- `packet_type:`
- `patch_type:`
- `codex_wave_card: 1`

Documented compatibility aliases are allowed only when all are true:

- the file is explicitly allowlisted for that alias;
- the occurrence is inside a markdown section whose heading contains `legacy` or `compatibility`;
- the compatibility section maps the alias to a canonical `workflow_packet: 1` / `schema: *.v1` transport template.

Current allowlisted compatibility files:

```text
workflow/transport/CODEX_RETURN_PACKET.md
workflow/transport/CODEX_WAVE_CARD.md
```

Examples of allowed compatibility aliases in those sections:

```text
packet_type: codex_return_packet
schema: codex_return_packet.v1
codex_wave_card: 1
CODEX_RETURN_PACKET_BEGIN/END
CODEX_WAVE_CARD_BEGIN/END
allowed_targets / forbidden_targets
```

Result:

- baseline: WARN on active legacy transport shapes outside documented compatibility sections.
- strict: FAIL on active legacy transport shapes outside documented compatibility sections.
- baseline and strict: PASS when legacy tokens appear only as documented compatibility aliases.

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
workflow/runtime/CONTEXT_ACQUISITION_POLICY.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

`WORKFLOW_SOURCE_OF_TRUTH.md` may warn if it lacks an EOF marker.

Result:

- baseline: FAIL for required authority EOF marker loss; WARN for short source marker absence
- strict: FAIL for required authority EOF marker loss

## CHECK 014 — stale_rebuild_metadata

Scan runtime-facing markdown files for stale rebuild/test-active metadata:

- `vNext-R REBUILD`
- `test-active`
- `rebuild root only`
- `Installed from roadmap step`
- `Step 7.`

Exclusions:

- `workflow/validation/*`, because validation files intentionally list stale tokens as expectations/check patterns.
- `workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md`, because architecture decisions may preserve historical/deferred cleanup references.
- `directions/*/execution_logs/*`, because execution logs are historical evidence and are not active runtime metadata.

Result:

- baseline: WARN on stale metadata in active runtime-facing files.
- strict: WARN until the remaining real metadata cleanup is complete; then this may be promoted to FAIL.
- excluded intentional/history surfaces must not produce warnings.

## CHECK 015 — prompt_schema_duplication_scan

Scan stage prompts for copied packet schema bodies or prompt-local route tables.

This check must not warn merely because a prompt references a canonical schema name such as:

- `stage_launch.v1`
- `stage_result.v1`
- `repository_patch.v1`
- `context_request.v1`
- `human_decision.v1`

Allowed:

- compact references to canonical transport templates;
- prose references to schema names;
- stage-specific output obligations that point to canonical templates;
- AD-WF-RT-001 route-authority boundary text.

Warn only when a prompt appears to contain:

- a copied full packet schema body beginning with `workflow_packet: 1`, `type: ...`, and `schema: ...`;
- a prompt-maintained `allowed_next` route table;
- legacy local launch-format headings such as `Next Launch Card Required Format`.

Result:

- baseline: WARN on copied schema bodies or prompt-local route-table residue.
- strict: WARN until prompt slimming cleanup is fully complete; may become FAIL after zero-noise baseline is established.
- canonical references alone must not warn.

## CHECK 016 — cross_direction_cache_setup_consistency

Check all active Directions have required Project Files, Project Instructions, and cache references through `08_DIRECTION_MAP.md`.

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

## CHECK 020 — transport_authority_boundary

Validate that the runtime authority boundary reflects completed transport schema conversion.

Hard requirements:

- `workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md` declares `workflow/transport/*.md` as canonical packet-schema / transport-template authority.
- `workflow/stage_registry/STAGE_REGISTRY.md` states that packet schema templates are owned by `workflow/transport/*.md`.
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` contains a packet template authority boundary note.
- runtime core remains behavior / precedence / formalization / repository maintenance authority.
- registry remains route authority.
- canonical transport templates exist for:
  - `stage_launch.v1`;
  - `stage_result.v1`;
  - `context_request.v1`;
  - `human_decision.v1`;
  - `repository_patch.v1`;
  - `codex_repository_maintenance_apply.v1`;
  - `codex_return.v1`;
  - `codex_wave.v1`.
- stale pre-transport-conversion wording must not remain in AD-WF-RT-001 or STAGE_REGISTRY.

Result:

- baseline: FAIL on missing boundary anchors, missing canonical transport anchors, or stale pre-conversion authority wording.
- strict: FAIL on the same conditions.

## CHECK 021 — Branch/workstream execution contract

Verifies that branch/workstream execution support is installed consistently.

Required anchors:

- `workflow/transport/TOPOLOGY_LAUNCH_BUNDLE.md`
- `workflow/transport/WORKSTREAM_LAUNCH_CARD.md`
- `workflow/transport/WORKSTREAM_RESULT_CARD.md`
- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md` includes Branch / Workstream Execution Topology behavior.
- `workflow/stage_prompts/E1_EXECUTION_BRIEF.md` includes Branch / Workstream Topology Gate.
- branch-capable prompts include Branch / workstream mode and `workstream_result_card.v1`.
- `R1_GOAL_REVIEW_DISTILL.md` rejects branch-only results as parent Goal completion.

The check prevents drift back to monolithic large-Goal execution without explicit topology handling.

## Expected baseline summary

The expected first useful run is:

```text
PASS_WITH_CLEANUP
```

This means hard runtime invariants pass and known cleanup debt remains.

## CHECK 021 — runtime_core_packet_schema_reference_cleanup

Validate that runtime core no longer owns full packet schema bodies after P2 cleanup.

Hard requirements:

- runtime core references canonical transport templates for:
  - `CONTEXT_REQUEST_CARD.md`;
  - `HUMAN_DECISION_CARD.md`;
  - `STAGE_LAUNCH_CARD.md`;
  - `STAGE_RESULT_PACKET.md`;
  - `REPOSITORY_PATCH.md`;
  - `CODEX_REPOSITORY_MAINTENANCE_APPLY.md`;
  - `EXECUTION_LOG_ENTRY.md`;
  - `DOCUMENTATION_MAINTENANCE_GATE.md`.
- runtime core must not contain full packet schema bodies for:
  - `context_request.v1`;
  - `human_decision.v1`;
  - `stage_launch.v1`;
  - `stage_result.v1`;
  - `repository_patch.v1`;
  - `codex_repository_maintenance_apply.v1`;
  - `execution_log_entry.v1`;
  - `documentation_maintenance_gate.v1`.
- runtime core must preserve behavior anchors for:
  - runtime behavior authority;
  - first-response/formalization gate;
  - repository maintenance separation;
  - Project Files refresh reporting.

Result:

- baseline: FAIL on missing transport references, full packet schema-body residue, or missing behavior anchors.
- strict: FAIL on the same conditions.

## CHECK 022 — runtime_core_registry_snapshot_cleanup

Validate that runtime core does not duplicate the stage registry.

Hard requirements:

- runtime core points to `workflow/stage_registry/STAGE_REGISTRY.md` for stage identity, prompt path/status, activation, target runtime, and normal `allowed_next` transitions.
- runtime core does not contain a duplicate stage identity / prompt source table.
- runtime core preserves Phase Progress Gate behavior.
- runtime core preserves the rule that it must not maintain a transition table.
- AD-WF-RT-001 records completed P2/P3 cleanup and does not list completed packet-schema cleanup as deferred.

Forbidden residue:

- a markdown table headed `Stage ID | Name | Runtime role | Prompt source`;
- runtime-core rows duplicating specific stage IDs and prompt sources;
- stale wording that says runtime-core packet-schema reference cleanup is still pending;
- AD-WF-RT-001 deferred cleanup item saying embedded packet schema blocks still need replacement.

Result:

- baseline: FAIL on duplicate registry snapshot residue or stale completed-cleanup wording.
- strict: FAIL on the same conditions.

## CHECK 023 — direction_worktree_repository_maintenance_contract

Validate that repository maintenance uses Direction worktrees instead of direct-main by default.

Hard requirements:

- runtime core contains `Worktree-aware repository maintenance policy`;
- runtime core defines the main integration worktree `C:\my_global_workflow`;
- runtime core defines all four active Direction worktrees and branches;
- Codex repository maintenance apply template includes `worktree_policy` and `direction_worktree_map`;
- active Direction Project Instructions contain their matching worktree and branch;
- setup docs describe the worktree maintenance setup;
- stale direct-main default wording is absent.

Result:

- baseline: FAIL on missing worktree policy anchors or stale direct-main default wording.
- strict: FAIL on the same conditions.

## CHECK 024 — context_acquisition_policy_authority

Validate that context acquisition authority is centralized.

Hard requirements:

- `workflow/runtime/CONTEXT_ACQUISITION_POLICY.md` exists;
- AD-WF-RT-001 declares it as authority for source/context acquisition order;
- runtime core references it before Context Request for exact repository context and stage prompts;
- GitHub long-file guard declares it owns verification, not acquisition order;
- runtime cache manifest includes it in required shared runtime cache.

Result:

- baseline: FAIL on missing policy file or missing authority anchors.
- strict: FAIL on the same conditions.

## CHECK 025 — github_first_acquisition_before_context_request

Validate that exact repository/path Context Request cannot skip current-run GitHub acquisition when available.

Hard requirements:

- Context Request template contains `acquisition_audit`;
- all active Direction Project Instructions contain the compact GitHub-first acquisition instruction;
- runtime core says Project File/attachment absence alone is insufficient before applying the acquisition policy.

Result:

- baseline: FAIL on missing audit fields or missing compact enforcement anchors.
- strict: FAIL on the same conditions.

## CHECK 026 — acquisition_order_not_duplicated

Validate that the complete acquisition order stays in one canonical policy file.

Hard requirements:

- the canonical policy contains exactly one complete five-item order;
- runtime core, long-file guard, manifest, transport templates, setup docs, validation docs, and Direction files do not copy that complete order.

Result:

- baseline: FAIL if the complete order is missing from the policy or copied outside it.
- strict: FAIL on the same conditions.

## CHECK 027 — stage_close_launch_boundary

Validate that stage close creates a launch card without requesting downstream execution-only prompt/files.

Hard requirements:

- runtime core contains the close-boundary rule;
- Stage Launch template contains `next_stage_context_policy` or equivalent fields.

Result:

- baseline: FAIL on missing stage-close launch-boundary anchors.
- strict: FAIL on the same conditions.

## CHECK 028 — prompt_delivery_github_connector_mode

Validate that verified GitHub connector acquisition is an approved prompt delivery path and manual fallback cannot bypass acquisition.

Hard requirements:

- AD-WF-RT-001, runtime core, and Stage Launch template allow `github_connector_verified_full_read`;
- `manual_prompt_required` means prompt remains unavailable after the acquisition policy is applied.

Result:

- baseline: FAIL on missing GitHub connector prompt mode or stale manual fallback semantics.
- strict: FAIL on the same conditions.
