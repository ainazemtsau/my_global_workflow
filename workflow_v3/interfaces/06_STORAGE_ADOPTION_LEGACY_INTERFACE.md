# Storage, Adoption, and Legacy Interface

status: active_interface_layer

## Purpose

This file defines storage, adoption, and legacy seams for Workflow v3.

## Owner/surface

Owner/surface: shared Workflow v3 namespace, future per-Direction runtime storage, old Workflow OS coexistence, old Direction legacy evidence, and adoption modes.

## Persistence target

Persistence target: `workflow_v3/interfaces/06_STORAGE_ADOPTION_LEGACY_INTERFACE.md` for shared rules; future per-Direction runtime state belongs under `directions_v3/<direction-id>/runtime/**` only after explicit adoption.

## Namespace roles

`workflow_v3/**` is the shared rules/setup namespace for Workflow v3.

`directions_v3/<direction-id>/runtime/**` is future per-Direction state only after an explicit adoption package.

`workflow/**` remains the current Workflow OS and rollback context unless a later explicit package changes that boundary.

`directions/**` remains old Direction `legacy_evidence` for Workflow v3 unless an explicit bridge/import/adoption package says otherwise.

## Future layout under directions_v3

Future adopted Directions may use:

```text
directions_v3/<direction-id>/runtime/
  state/
  fronts/
  records/
  memory/
  operations/
  archive/
  indexes/
  config/
  console/
```

Creating that root requires a separate per-Direction adoption package with explicit acceptance, scope, validation, and rollback/coexistence evidence.

## Adoption modes

`clean_start` begins v3 from an explicit current decision without importing old state.

`bridge_only` references old state through an explicit bridge without claiming import.

`selective_import` imports specific artifacts with evidence and Acceptance Decision.

`full_migration` is allowed only after a separate migration policy, validation evidence, and rollback design.

`no_adoption` keeps the Direction under the old Workflow OS.

The default for existing Directions is `clean_start` from an explicit current decision unless a later accepted package says otherwise.

## Adoption preconditions

Adoption requires:

- Direction id and target runtime root;
- adoption mode;
- source authority and legacy evidence classification;
- accepted current Direction Spine, Active Front, Current Status, and Next Move or a declared clean-start equivalent;
- allowed and forbidden paths;
- rollback/coexistence evidence;
- Project setup refresh report;
- acceptance/update path;
- validation evidence;
- explicit human or governance acceptance.

## Forbidden implicit adoption/import

No document, chat, Project File, pack, old receipt, old ledger, old obligation, old project file, candidate doc, Signal, Handler result, Codex output, or interface file creates adoption or import by existing.

No `directions_v3/<direction-id>/runtime/**` root may be created by an interface-only package.

## Rollback/coexistence requirements

Workflow v3 must preserve the current Workflow OS and rollback context until a later explicit package changes that boundary.

Old files must not be deleted, renamed, moved, replaced, or decommissioned by implication.

Non-adopted Directions remain under the current Workflow OS.

## Inputs

Inputs are source authority, adoption decisions, legacy evidence, storage layout rules, accepted records, rollback/coexistence checks, and Project setup refresh requirements.

## Outputs

Outputs are storage targets, adoption mode decisions, bridge/import boundaries, rollback/coexistence evidence, and blocked results when adoption/import is unsafe.

## State mutation rights

This interface does not mutate Direction runtime state.

Future adoption packages may create or mutate `directions_v3/<direction-id>/runtime/**` only after explicit adoption acceptance.

Shared repository documentation under `workflow_v3/**` may be edited by authorized repository-maintenance packages.

## Allowed producers

Allowed producers are adoption packages, storage layout packages, bridge/import packages, rollback/coexistence verification packages, and bounded Codex packages authorized for those surfaces.

## Allowed consumers

Allowed consumers are parent chats, adoption reviews, Project setup packages, Runtime Console design, quality gates, Codex handoffs, and future Direction Projects.

## Validation/evidence requirement

Validation must show no forbidden path changes, no implicit Direction runtime root creation, old Workflow OS coexistence preserved, old Direction files classified as `legacy_evidence`, adoption mode explicit, and Project refresh categories separated.

## Forbidden behaviors

- Treating old `directions/**` as `accepted_v3_state`.
- Importing old ledgers, obligations, receipts, project files, or runtime files by implication.
- Creating per-Direction runtime roots without adoption.
- Weakening rollback/coexistence.
- Decommissioning old Workflow OS files.
- Treating generated packs as authority.

## Failure/recovery path

If adoption/import would be required, stop and split into a future adoption, bridge, selective import, full migration, or no-adoption decision package.

If legacy source is touched unexpectedly, run the legacy guard path and return a human decision request or blocked result.

If rollback/coexistence evidence is missing, stop with a Check Job or Context Request.

## Dependencies

- `directions_v3/README.md`
- `workflow_v3/STORAGE_LAYOUT.md`
- `workflow_v3/LEGACY_EVIDENCE_POLICY.md`
- `workflow_v3/ACTIVATION_STATUS.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`

END_OF_FILE: workflow_v3/interfaces/06_STORAGE_ADOPTION_LEGACY_INTERFACE.md
