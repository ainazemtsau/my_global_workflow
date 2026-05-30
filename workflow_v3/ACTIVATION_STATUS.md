# Workflow v3 Activation Status

status: active_skeleton_namespace_corrected

## Status matrix

| Surface | Status |
| --- | --- |
| workflow_v3_production_namespace_skeleton | active |
| direction_adoption | none |
| legacy_state_import | none |
| chatgpt_project_ui_update | none |
| project_files_sources_refresh | none |
| old_workflow_os_decommission | none |

## What is activated at this slice

Activated means only this:

- the repository now has the initial `workflow_v3/**` documentation/setup skeleton;
- the skeleton defines Workflow v3 production namespace boundaries for later packages;
- the skeleton may be cited as the starting source for future Workflow v3 setup work.

Activation at this slice does not mean a live runtime exists. It does not create accepted Direction state, accepted v3 state, migration authority, Project setup authority, or decommission authority.

## What remains not activated

Not activated in this slice:

- any Direction adoption;
- any `directions_v3/<direction-id>/runtime/**` state root;
- any old Direction state import;
- any bridge from old Direction files into accepted v3 state;
- any actual ChatGPT Project Instructions UI update;
- any current Project Files/Sources refresh;
- any request-only source refresh;
- any old Workflow OS archive, deletion, rename, move, replacement, or decommission.

## Allowed future packages

Allowed future packages must be separate, explicit, bounded, and validated. Examples:

- production runtime rule refinement under `workflow_v3/**`;
- future Project setup rollout package with measured payload character counts;
- future project pack generation package;
- one per-Direction adoption package after an explicit adoption decision;
- clean-start Direction runtime state package under `directions_v3/<direction-id>/runtime/**`;
- bridge or selective import package only after explicit policy and evidence;
- rollback/coexistence verification package.

## Forbidden next actions

Forbidden as an implicit follow-up to this slice:

- adopting a Direction automatically;
- importing old Direction state automatically;
- treating old Ledger, Obligations, Receipts, or project files as accepted_v3_state;
- updating actual ChatGPT Projects from these files;
- refreshing current Project Files/Sources from these files;
- uploading these files as current Project Files/Sources without a later explicit rollout/adoption package;
- deleting, renaming, moving, replacing, or decommissioning old Workflow OS files;
- using candidate docs as accepted Direction state.

END_OF_FILE: workflow_v3/ACTIVATION_STATUS.md
