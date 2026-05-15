# Static Runtime Validation Expectations

Status: baseline expectations
Owner layer: workflow validation
Scope: Workflow vNext-R shared runtime cleanup

## Purpose

This file defines the expected behavior of `runtime_static_checks.py`.

It separates hard runtime invariants from known cleanup debt.

## Active Directions

The active Direction Projects currently checked by this suite are:

- `workflow-governance`
- `solo-max-productive`
- `indie-game-development`
- `health-and-beauty`

Each active Direction is expected to have:

```text
directions/<direction-id>/project_files/00_DIRECTION_START_HERE.md
directions/<direction-id>/project_files/01_DIRECTION_STATE.md
directions/<direction-id>/project_files/02_CURRENT_PHASE.md
directions/<direction-id>/project_files/03_FOCUS_REGISTER.md
directions/<direction-id>/project_files/04_ACTIVE_GOAL.md
directions/<direction-id>/project_files/05_PORTFOLIO_QUEUE.md
directions/<direction-id>/project_files/06_CONTEXT_LIBRARY_INDEX.md
directions/<direction-id>/project_files/07_PHASE_MEMORY_INDEX.md
directions/<direction-id>/project_files/08_DIRECTION_MAP.md
directions/<direction-id>/project_setup/CHATGPT_PROJECT_INSTRUCTIONS.md
```

## Required shared runtime files

These files must exist:

```text
WORKFLOW_SOURCE_OF_TRUTH.md
workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md
workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
workflow/stage_registry/STAGE_REGISTRY.md
```

## Hard invariants

These checks are blocking in both baseline and strict mode:

1. Required shared runtime files exist.
2. Active Direction Project Files `00-08` exist.
3. Active Direction Project Instructions exist.
4. Markdown triple-backtick fences are balanced.
5. `STAGE_REGISTRY.md` declares itself the sole authority for canonical stage IDs, stage identity, prompt path/status, target runtime, activation, and normal `allowed_next`.
6. Runtime core must not maintain a second full `allowed_next` transition table.
7. Registry validation rules must preserve these invariants:
   - runtime core must not maintain a duplicate full transition table;
   - prompts must not be treated as allowed-next authority;
   - transport route fields are snapshots only;
   - terminal card types are not canonical stage IDs.
8. Active stage prompts must not use deprecated prompt delivery modes:
   - `request_from_repository`
   - `embedded_in_launch_card`
   - `pasted_in_current_chat`
   - `attached_export`
9. Present stage prompts must contain the `AD-WF-RT-001` authority boundary.
10. Required authority files with EOF markers must keep them:
    - `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`
    - `workflow/runtime/GITHUB_LONG_FILE_READ_GUARD.md`
    - `workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md`
    - `workflow/stage_registry/STAGE_REGISTRY.md`
11. Direction Project Files must not contain full stage prompt bodies.
12. Registry rows marked `prompt_status: present` must have matching prompt files under `workflow/stage_prompts/`.

## Baseline warnings

These are expected warnings during current cleanup:

1. Legacy transport card shapes:
   - `stage_launch_card: 1`
   - `stage_result_packet: 1`
   - active transport use of `card_type:`
   - active transport use of `packet_type:`
   - active transport use of `patch_type:`
2. Missing dedicated `codex_repository_maintenance_apply.v1` transport template under `workflow/transport/`.
3. Missing `END_OF_FILE:` markers in stage prompts.
4. Stale rebuild/test-active metadata:
   - `vNext-R REBUILD`
   - `test-active`
   - `rebuild root only`
   - `Installed from roadmap step`
   - `Step 7.`
5. Prompt schema duplication or old route examples in long prompts.
6. Stale `docs/CHATGPT_PROJECT_SETUP.md` setup blocks compared to the current runtime cache manifest.

## Strict-mode promotion

After corresponding cleanup patches are complete, these warning classes may be promoted to strict failures:

- legacy transport card shapes;
- missing transport schema templates;
- missing prompt EOF markers;
- stale setup docs;
- stale rebuild/test-active metadata;
- prompt schema duplication / route-list residue.

## Expected first baseline result

Until cleanup debt is resolved, the expected baseline result is:

```text
PASS_WITH_CLEANUP
```

A `BLOCKED` result means a hard runtime invariant failed and should be investigated before proceeding with further cleanup patches.

## Codex Return/Wave schema regression expectation

After S4-E Codex Return/Wave cleanup:

Canonical schema IDs:

```text
codex_return.v1
codex_wave.v1
```

Human-readable artifact names may remain:

```text
Codex Return Packet
Codex Wave Card
```

Legacy aliases are allowed only in documented compatibility sections:

```text
codex_return_packet.v1
packet_type: codex_return_packet
codex_wave_card: 1
CODEX_RETURN_PACKET_BEGIN/END
CODEX_WAVE_CARD_BEGIN/END
allowed_targets / forbidden_targets
```

Hard invariant:

- stage prompts must not contain legacy Codex schema names or wrapper tokens;
- transport templates must declare canonical `codex_return.v1` and `codex_wave.v1`;
- Codex semantic contracts must point to transport templates as packet schema authority;
- compatibility aliases must not be treated as canonical schema IDs.

`CHECK 019 — codex_return_wave_schema_regression` enforces this as a hard check in both baseline and strict mode.

## Transport authority boundary expectation

After transport schema conversion, canonical packet schema templates live in:

```text
workflow/transport/*.md
```

Runtime core remains authority for:

```text
runtime behavior
precedence
approval/formalization rules
repository maintenance rules
route process
Codex role separation
Project Files refresh/reporting rules
```

Stage registry remains authority for:

```text
canonical stage IDs
prompt path/status
activation
normal allowed_next transitions
```

Hard invariant:

- AD-WF-RT-001 and STAGE_REGISTRY must not say that packet contracts remain in runtime core until transport schemas are converted;
- runtime core may contain compatibility examples until the later packet-schema reference cleanup, but those examples are not packet-template authority;
- transport templates must retain canonical `workflow_packet: 1` and `schema: *.v1` anchors.

`CHECK 020 — transport_authority_boundary` enforces this in both baseline and strict mode.

## Runtime core packet schema reference cleanup expectation

After P2 cleanup, runtime core remains behavior authority but no longer owns full packet schema bodies.

Canonical packet templates live in:

```text
workflow/transport/*.md
```

Runtime core must reference transport templates for packet shape and keep only behavior rules, including:

```text
runtime behavior
precedence
approval/formalization rules
repository maintenance rules
route process
Codex role separation
Project Files refresh/reporting rules
```

Hard invariant:

- runtime core must not contain full packet schema bodies for common workflow packets;
- runtime core must preserve behavior anchors for formalization, repository maintenance, and Project Files refresh reporting;
- transport templates remain packet-shape authority.

`CHECK 021 — runtime_core_packet_schema_reference_cleanup` enforces this in both baseline and strict mode.

## CHECK 010 compatibility-aware legacy transport expectation

`CHECK 010 — legacy_transport_shape_scan` distinguishes active legacy transport shapes from documented compatibility aliases.

Active legacy transport shapes remain cleanup debt or blockers:

```text
stage_launch_card: 1
stage_result_packet: 1
card_type:
packet_type:
patch_type:
codex_wave_card: 1
```

Compatibility aliases are allowed only inside explicit legacy/compatibility sections of allowlisted files:

```text
workflow/transport/CODEX_RETURN_PACKET.md
workflow/transport/CODEX_WAVE_CARD.md
```

Allowed compatibility aliases must normalize to canonical schemas:

```text
codex_return.v1
codex_wave.v1
```

Hard invariant:

- strict mode must not fail merely because a legacy alias is documented in a compatibility section;
- strict mode must fail if active transport templates regress to legacy card shapes;
- compatibility aliases must not be treated as canonical schema IDs.

## CHECK 014/015 validator-noise reduction expectation

`CHECK 014 — stale_rebuild_metadata` must warn on active stale runtime metadata, but it must not warn on intentional examples/history in:

```text
workflow/validation/*
workflow/runtime/AD_WF_RT_001_SINGLE_RUNTIME_AUTHORITY_MODEL.md
directions/*/execution_logs/*
```

`CHECK 015 — prompt_schema_duplication_scan` must warn on copied prompt schema bodies and prompt-local route tables, but it must not warn on canonical schema references or compact transport-template references.

Hard invariant:

- validator-noise reductions must not hide active legacy transport shapes, copied packet schema bodies, deprecated prompt delivery modes, or route-authority drift;
- CHECK 014 should continue to surface real stale metadata in runtime-facing files;
- CHECK 015 should continue to surface true prompt schema-body duplication.

Expected effect after this refinement:

- baseline and strict validation still exit 0;
- blocking failures remain 0;
- false-positive warnings from validation docs, AD-WF-RT-001 history, execution logs, and canonical prompt references are reduced.

## Runtime core registry snapshot cleanup expectation

Runtime core must not duplicate the stage registry.

`workflow/stage_registry/STAGE_REGISTRY.md` owns:

```text
canonical stage IDs
stage identity
prompt path/status
target runtime
activation
normal allowed_next transitions
```

Runtime core may describe routing behavior, route conflict handling, lifecycle heuristics, and Phase Progress Gate rules.

Runtime core must not contain a stage identity / prompt source table copied from the registry.

Completed cleanup notes must stay current:

- P2 removed runtime-core packet schema body authority;
- P3 removed runtime-core registry snapshot duplication.

`CHECK 022 — runtime_core_registry_snapshot_cleanup` enforces this in both baseline and strict mode.

## Direction worktree repository maintenance expectation

Repository maintenance for `ainazemtsau/my_global_workflow` is worktree-aware.

Expected model:

- `C:\my_global_workflow` is the clean main integration worktree.
- Each active Direction has a matching worktree under `C:\my_global_workflow_worktrees\`.
- Direction-specific work happens on the matching `codex/direction-*` branch.
- Shared workflow/governance maintenance uses the Workflow Governance worktree by default.
- Direct-main maintenance is explicit override only.
- Direction branches must be rebased on `origin/main` before work.
- Direction branches must be pushed after work.
- The run must merge/PR into main or report explicit unmerged reason.
- Sibling Directions must not be edited from a Direction worktree unless explicitly approved.

`CHECK 023 — direction_worktree_repository_maintenance_contract` enforces this in baseline and strict mode.
