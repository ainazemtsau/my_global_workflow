# Workflow v3 Direction Adoption

status: active_repository_completion_framework

## Purpose

This directory defines the source model for future Direction adoption packages.

It does not adopt any Direction, create `directions_v3/<direction-id>/runtime/**`, import legacy state, migrate old Direction proof, update Project Instructions UI, refresh Project Files/Sources, or execute product work.

## Migration boundary

Adoption is per Direction. Migration/adoption mode is explicit per Direction.

Old `directions/**` files are `legacy_evidence` only. They may support future adoption review, but they do not become accepted Workflow v3 state automatically.

There is no automatic import and no automatic discard. A future accepted package must choose the mode for the named Direction, review the evidence, and authorize any accepted update.

Runtime root creation under `directions_v3/<direction-id>/runtime/**` remains separate and accepted.

## Files

- `CLEAN_START_DIRECTION_ADOPTION_PACKAGE_TEMPLATE.md` - package template for a future clean-start adoption mode.
- `DIRECTION_RUNTIME_ROOT_MANIFEST_TEMPLATE.md` - future runtime root manifest template.
- `DIRECTION_BOOTSTRAP_DECISION_TEMPLATE.md` - explicit adoption decision template.
- `DIRECTION_RUNTIME_CREATION_CHECKLIST.md` - checklist for creating a runtime root in a later authorized package.
- `LEGACY_EVIDENCE_REVIEW_TEMPLATE.md` - review template for old files as evidence only.
- `ADOPTION_RESULT_PACKET_TEMPLATE.md` - result packet template for returning adoption package evidence.

## Stop conditions

Stop with a Context Request if any future adoption package has:

- unclear Direction identity;
- unclear adoption mode;
- attempted implicit migration;
- missing acceptance decision;
- forbidden old-state import;
- Project setup action required but not authorized.

END_OF_FILE: workflow_v3/adoption/README.md
