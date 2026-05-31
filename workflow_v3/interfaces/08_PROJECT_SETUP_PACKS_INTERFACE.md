# Project Setup and Packs Interface

status: active_interface_layer

## Purpose

This file defines Workflow v3 Project setup and pack boundaries.

## Owner/surface

Owner/surface: Project Instructions UI, Project Files/Sources, repository Project Instruction Sources, request-only sources, do-not-upload sources, payload count requirements, Project setup refresh reporting, and generated pack boundaries.

## Persistence target

Persistence target: `workflow_v3/interfaces/08_PROJECT_SETUP_PACKS_INTERFACE.md` for shared rules; future setup manifests and generated pack sources remain under their authorized `workflow_v3/**` paths.

## Project setup surfaces

Project Instructions UI is a compact behavior bootstrap.

Project Files/Sources are cache/context only.

Repository Project Instruction Sources are files used to build or copy Project Instructions UI payloads.

Request-only sources are loaded only when an admitted task needs them.

`do_not_upload_as_project_file` names sources that must not be uploaded as default Project Files/Sources.

## Payload count requirement

Future Project Instructions UI source changes require payload character counts when the source includes a Project Instructions UI payload.

Payload counts must be reported separately from repository commit evidence and Project Files/Sources refresh evidence.

## Actual Project update boundary

An actual ChatGPT Project Instructions UI update is separate from a repository commit.

A Project Files/Sources refresh is separate from a repository commit.

A request-only source refresh is separate from both.

Repository commits may change source files, but they do not prove external Project UI or Project Files/Sources were updated.

## Refresh categories

Project setup reporting must keep these categories separate:

- `project_instruction_ui_update_required`;
- `project_sources_files_refresh_required`;
- `request_only_sources_refresh_required`;
- `do_not_upload_as_project_file`.

## Pack boundary

Packs are cache/upload convenience, not authority.

Canonical `workflow_v3/**` files win over generated packs.

If a pack conflicts with exact repository source, regenerate or repair the pack through a later explicit package. Do not treat the pack as source authority.

## Future pack generation prerequisites

Future pack generation requires:

- explicit package scope;
- source files and exact ref;
- target pack names;
- cache/context warning;
- excluded do-not-upload files;
- payload or size checks when applicable;
- validation evidence;
- refresh category report;
- no implication that Project upload occurred.

## Inputs

Inputs are Project setup model files, Project Instruction Sources, manifests, request-only source lists, do-not-upload lists, pack source files, exact repository refs, and human setup decisions.

## Outputs

Outputs are setup instructions, manifests, refresh reports, payload counts, generated packs when authorized, do-not-upload lists, and project refresh requirements.

## State mutation rights

Repository setup files may be changed by authorized repository-maintenance packages.

This interface does not update actual Project Instructions UI, Project Files/Sources, request-only sources, external Projects, or accepted Direction runtime state.

## Allowed producers

Allowed producers are Project setup rollout packages, repository-maintenance packages, pack generation packages, Codex packages authorized for setup files, and human setup actions.

## Allowed consumers

Allowed consumers are ChatGPT Projects, Governance Maintenance Console setup, Direction Project setup, Codex handoffs, validation gates, and future pack generation.

## Validation/evidence requirement

Validation must report:

- Project Instructions UI update requirement;
- Project Files/Sources refresh requirement;
- request-only source refresh requirement;
- do-not-upload sources;
- payload character counts when Project Instructions UI sources changed;
- whether actual Project update was performed or not performed.

## Forbidden behaviors

- Treating Project Files/Sources as authority.
- Treating repository commit as actual Project update.
- Uploading `workflow_v3/**` files as current Project Files/Sources without a later explicit rollout/adoption package.
- Treating packs as accepted state.
- Hiding request-only sources in default Project context.
- Mixing Project Instructions UI update evidence with Project Files/Sources refresh evidence.

## Failure/recovery path

If setup refresh status is unclear, stop and report separated refresh categories.

If payload counts are required but missing, run same-package repair or return blocked result.

If actual external Project update is required, split into a separate human/tool action package with confirmation evidence.

If generated packs would be needed, split into a future pack generation package.

## Dependencies

- `workflow_v3/PROJECT_SETUP_MODEL.md`
- `workflow_v3/project_setup/CHATGPT_PROJECT_CREATION_GUIDE.md`
- `workflow_v3/project_setup/PROJECT_FILES_MANIFEST_TEMPLATE.md`
- `workflow_v3/project_setup/UNIVERSAL_DIRECTION_PROJECT_INSTRUCTIONS.md`
- `workflow_v3/project_setup/GOVERNANCE_MAINTENANCE_PROJECT_INSTRUCTIONS.md`
- `workflow_v3/project_packs/README.md`

END_OF_FILE: workflow_v3/interfaces/08_PROJECT_SETUP_PACKS_INTERFACE.md
