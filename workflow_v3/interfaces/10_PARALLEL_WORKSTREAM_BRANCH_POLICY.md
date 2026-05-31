# Parallel Workstream and Branch Policy

status: active_interface_layer

## Purpose

This file defines future parallel workstream ownership and branch policy for Workflow v3 development.

## Owner/surface

Owner/surface: parent/child workstream coordination, integration-owned files, workstream-owned files, forbidden surfaces, branch isolation, Codex implementation sequencing, and merge order.

## Persistence target

Persistence target: `workflow_v3/interfaces/10_PARALLEL_WORKSTREAM_BRANCH_POLICY.md`.

## Workstream ownership map

Integration-owned files and surfaces:

- `workflow_v3/interfaces/**`;
- cross-surface term definitions;
- packet and transfer boundaries;
- storage/adoption/legacy seams;
- Project setup refresh category rules;
- adapter/Codex/provider boundaries;
- quality gate definitions that affect multiple workstreams.

Workstream-owned files are the narrow files explicitly named by a reviewed workstream package.

Forbidden files/surfaces unless explicitly named by a separate authorized package:

- `workflow/**`;
- `directions/**`;
- `directions_v3/<direction-id>/runtime/**`;
- product repository files;
- generated project pack files;
- actual ChatGPT Project setup outside `workflow_v3/**`;
- candidate docs under `workflow/candidates/**` as accepted authority;
- old Workflow OS decommission, rename, delete, or move.

## Parent and child chat rules

A parent may launch child chats only when the child has a bounded Launch Packet, exact source context or Context Request boundaries, explicit in-scope and out-of-scope surfaces, evidence requirements, return destination, and stop conditions.

Child output returns to the parent as candidate evidence.

No child chat is an independent execution track.

No child may redefine locked terms, accept state, route future work, launch Codex silently, or decide adoption/import.

## Branch and Codex policy

Use review branches for material repository work unless the package explicitly authorizes another branch policy.

No parallel Codex commits may target overlapping paths.

Cross-cutting changes require an integration branch.

No Codex implementation should follow a child design result until the parent or integration review has reviewed and selected that design result.

Codex packages must state base SHA, branch, allowed paths, forbidden paths, validation, stop conditions, commit/push instructions, and requested return fields.

## Merge order

Future Workflow v3 merge order should be:

1. interface layer;
2. lifecycle/event-loop reconciliation;
3. quality/eval reconciliation;
4. source/project setup reconciliation;
5. adapter/Codex reconciliation;
6. packs/rollout;
7. sandbox/adoption only after explicit package.

Later work may adjust this order only through integration review.

## Inputs

Inputs are parent workstream plans, child Launch Packets, design results, Codex packages, branch state, source authority, path ownership, and integration decisions.

## Outputs

Outputs are ownership decisions, branch policies, launch permissions, return rules, merge-order guidance, blocked results, and integration review requests.

## State mutation rights

This policy does not mutate accepted state.

Branches and repository files may be changed only by explicit packages within allowed paths and after required review.

## Allowed producers

Allowed producers are parent chats, integration review, repository-maintenance packages, and Codex packages operating under explicit branch and path constraints.

## Allowed consumers

Allowed consumers are parent workstreams, child chats, Codex packages, Check Jobs, merge/review processes, and Project setup rollout planning.

## Validation/evidence requirement

Validation must show branch name, base SHA, changed files, allowed paths, no forbidden surfaces changed, no overlapping parallel Codex changes, and evidence that child outputs returned to the parent before implementation.

## Forbidden behaviors

- Parallel Codex commits on overlapping paths.
- Child chats as independent execution tracks.
- Codex implementation from unreviewed design output.
- Hidden launch of child chats or Codex.
- Cross-cutting changes on a workstream branch without integration ownership.
- Touching forbidden surfaces by convenience.
- Using candidate docs as accepted Workflow v3 authority.

## Failure/recovery path

If path ownership overlaps, stop and route to integration review.

If a child result is missing or incomplete, return a blocked result or rerun/narrow the child Launch Packet.

If branch state is unsafe, stop before editing and request repair or a new branch.

If a proposed change requires forbidden surfaces, split into a future explicit package.

## Dependencies

- `workflow_v3/interfaces/00_INTERFACE_CANON.md`
- `workflow_v3/QUALITY_AND_RECOVERY.md`
- `workflow_v3/project_setup/GENERIC_AI_PROVIDER_SETUP.md`
- `workflow_v3/SIGNALS_HANDLERS_ACTION_INBOX.md`

END_OF_FILE: workflow_v3/interfaces/10_PARALLEL_WORKSTREAM_BRANCH_POLICY.md
