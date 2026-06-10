# Parallel Workstream Branch Policy

status: active_interface_layer

## Purpose

This interface defines future workstream and branch policy for Workflow v3 repository maintenance.

## File ownership

Integration-owned files:

- interface registry and coverage matrix;
- runtime model summaries;
- shared lifecycle/routing docs;
- storage state interface;
- quality/recovery interface;
- Project setup/context boundaries.

Workstream-owned files:

- files explicitly named in a bounded reviewed work package;
- branch-local candidate docs under allowed paths;
- scoped templates or implementation files assigned to one workstream.

Forbidden files/surfaces:

- `workflow/**` unless a task explicitly authorizes current Workflow OS maintenance;
- `directions/**`;
- `directions_v3/<direction-id>/runtime/**` without adoption package;
- product repository files;
- generated project packs unless package authorizes generation;
- actual ChatGPT Project setup outside repository files.

## Branch rules

- No parallel Codex commits on overlapping paths.
- Cross-cutting changes require an integration branch.
- No Codex implementation until design result is reviewed when the task is design-first or interface-wide.
- Review branch is required for repository maintenance that changes shared workflow rules.
- Do not push directly to main.

## Support Dependency Boundary

Support dependencies are bounded support/decomposition/review surfaces for the current parent target.

They may perform only the specific bounded dependency work requested by the parent prompt. They are not independent execution tracks.

Dependency outputs return to parent/integration synthesis. They must not commit independently, accept state, route product meaning, launch unrelated work, or become a substitute for the next material chat boundary.

END_OF_FILE: workflow_v3/interfaces/13_PARALLEL_WORKSTREAM_BRANCH_POLICY.md
