# Codex Wave Transport Template

```yaml
artifact_control:
  artifact_name: "Codex Wave Transport Template"
  schema: transport_template.v1
  owner_layer: transport
  status: canonical
  repo_path: "workflow/transport/CODEX_WAVE_CARD.md"
  runtime_schema: codex_wave.v1
  last_updated: "2026-05-13"
```

## Purpose

Defines a generic canonical transport template for dispatching a bounded Codex work wave.

For approved Workflow repository maintenance apply/read-back, prefer the dedicated `CODEX_REPOSITORY_MAINTENANCE_APPLY.md` template.

## Transport authority boundary — AD-WF-RT-001

This template is not routing authority. It does not authorize product/project execution unless the appropriate execution route has already approved that work.

## Transport invariants

- HTML is forbidden as transport.
- Use plain Markdown with YAML-style fields.
- Unknown extension fields must be tolerated by consumers.
- Codex scope must be bounded by exact repository paths or named artifacts.
- Codex must be told whether the wave is read-only, preview, apply, repair, or validation.
- Codex must return evidence.

## Canonical packet template

```yaml
workflow_packet: 1
type: codex_wave
schema: codex_wave.v1
codex_role: product_project_execution | repository_maintenance | read_only_audit_validation | launch_bundle_preparation
not_product_project_execution: true | false

wave:
  id:
  title:
  mode: read_only | preview | apply | repair | validate | launch_bundle
  priority: low | normal | high

repository:
  name:
  branch:
  allowed_paths:
    - path:
      reason:
  forbidden_paths:
    - path:
      reason:

task:
  objective:
  acceptance_criteria:
    - criterion:
  non_objectives:
    - item:

constraints:
  - constraint:

allowed_actions:
  - action:

forbidden_actions:
  - action:
    reason:

evidence_required:
  readback_required: true | false
  diff_verification_required: true | false
  commit_verification_required: true | false
  validation_commands:
    - command:
      expected:

return_requirement:
  final_state_required: true
  files_changed_required: true
  evidence_required: true
  blockers_required_if_any: true
  cannot_claim_done_without_evidence: true

technical_context_boundary:
  chatgpt_default_load_full_product_technical_context: false
  product_technical_context_owner: codex_project_workspace
  project_local_context_sources:
    - AGENTS.md
    - Project Execution Profile
    - Validation Profile
    - Module Map
    - ADRs
    - public interface docs
    - internal module knowledge for editable modules
    - .codex memory
  return_to_chatgpt: compact_summary_and_pointers_only

technical_discovery_preflight:
  required: true | false
  trigger_reasons:
    - new_module_or_public_interface_possible
    - multi_file_or_modular_work
    - reuse_vs_new_ambiguous
    - refactor_may_be_safer
    - module_boundary_or_generated_path_risk
    - validation_scope_may_change
  bounded_discovery_scope:
    - path_or_module:
      reason:
  decision_values:
    - reuse_existing
    - extend_existing
    - refactor_existing
    - create_new_module
    - cross_module_request
    - blocked_missing_context
    - human_decision_required
  stop_if:
    - material_architecture_decision_outside_envelope
    - dependency_direction_change_required
    - public_interface_change_outside_scope
    - forbidden_or_protected_path_required
    - validation_scope_expands_materially

extensions: {}
```

## Validation anchors

- `workflow_packet: 1`
- `schema: codex_wave.v1`
- `codex_role`
- `allowed_paths`
- `evidence_required`

## Legacy compatibility aliases

Canonical schema identity:

```yaml
workflow_packet: 1
type: codex_wave
schema: codex_wave.v1
```

Human-readable artifact names such as `Codex Wave Card` may remain in prose.

Legacy packet shapes may be tolerated only as compatibility input, not as schema authority:

```text
codex_wave_card: 1
CODEX_WAVE_CARD_BEGIN / CODEX_WAVE_CARD_END wrappers
allowed_targets
forbidden_targets
```

Compatibility normalization:

```text
codex_wave_card: 1 -> workflow_packet: 1 / type: codex_wave / schema: codex_wave.v1
CODEX_WAVE_CARD_BEGIN/END -> extensions.legacy_wrapper
allowed_targets -> repository.allowed_paths or allowed_actions, depending on value type
forbidden_targets -> repository.forbidden_paths or forbidden_actions, depending on value type
legacy packet fields -> canonical fields when names match, otherwise extensions.legacy_*
```

Producers should emit `codex_wave.v1`.

Consumers may tolerant-read legacy wave card shapes during migration, but must not treat legacy names as canonical schema IDs.

## End-of-file marker

`END_OF_FILE: workflow/transport/CODEX_WAVE_CARD.md`
