# Clean-Start Direction Adoption Package Template

status: template

## Boundary

This template is for a future explicit package. It does not adopt a Direction now and does not create runtime state now.

Clean-start adoption begins semantic Workflow v3 Direction definition/adoption from current explicit decisions. It is not the setup-only root creation package.

Use `workflow_v3/adoption/SETUP_ONLY_DIRECTION_RUNTIME_ROOT_PACKAGE_TEMPLATE.md` when the task is only to create technical root placeholders and binding before semantic Definition.

Old `directions/**` files are `legacy_evidence` only and must not be imported, migrated, or accepted by implication.

## Required package fields

`direction_id`:

`adoption_mode`: clean_start | bridge_only | selective_import | full_migration | no_adoption

`clean_start_reason`:

`legacy_evidence_allowed`: true | false

`legacy_evidence_paths`:

`accepted_initial_direction_spine`:

`accepted_initial_direction_map`:

`accepted_initial_active_front`:

`formation_procedure_paths`:

`project_setup_required`: true | false

`project_refresh_required`: true | false

`rollback/coexistence notes`:

`acceptance_decision_ref`:

## Source authority

Use exact repository path/ref reads for canonical Workflow v3 files and any legacy evidence paths.

Classify all old Direction files as `legacy_evidence` unless a later explicit bridge/import package authorizes a different status.

Project Files/Sources and prior chat are cache/context only.

## Future runtime root

If and only if this future package is accepted and authorized to create runtime state, the runtime root target is:

```text
directions_v3/<direction-id>/runtime/**
```

Do not create that path from this template alone.

## Required outputs

- adoption decision summary;
- accepted initial Direction Spine or explicit blocked reason, after Direction Spine formation and acceptance;
- accepted initial Direction Map or explicit blocked reason, after Direction Map formation and acceptance;
- accepted initial Active Front or explicit blocked reason, after Active Front formation and acceptance;
- runtime root creation plan or explicit no-creation decision;
- project_binding_artifacts_required;
- per_direction_project_setup_sources_required;
- manual_project_instruction_ui_update_required;
- continuation_protocol_ready;
- Project setup impact classification;
- separated refresh requirements;
- rollback/coexistence notes;
- adoption result packet.

## Stop conditions

Stop and return a Context Request if:

- Direction identity is unclear;
- adoption mode is unclear;
- setup-only root creation is being attempted through this semantic adoption template;
- required entity formation has not happened for semantic Spine/Map/Front;
- the package attempts implicit migration;
- acceptance decision is missing;
- old state would be imported without explicit bridge/import authority;
- Project setup action is required but not authorized;
- required source cannot be read fully;
- clean-start state would need to be invented from legacy evidence.

END_OF_FILE: workflow_v3/adoption/CLEAN_START_DIRECTION_ADOPTION_PACKAGE_TEMPLATE.md
