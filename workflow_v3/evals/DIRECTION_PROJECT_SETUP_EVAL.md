# Direction Project Setup Eval

status: active_project_setup_eval

## Purpose

This eval checks ordinary Workflow v3 Direction Project setup behavior.

It validates setup/root bootstrap behavior only. It does not validate product work, Direction adoption acceptance, runtime root file creation, or external ChatGPT Project UI updates.

## PASS checks

- Role is correct: ordinary Direction Project.
- The Project does not identify as the Governance Maintenance Console.
- Source authority is exact GitHub/repository path/ref.
- Project Files/Sources are cache/context only.
- No `directions_v3/<direction-id>/runtime/**` root is assumed without exact accepted source evidence.
- No product work starts during bootstrap.
- No legacy import occurs.
- Old `directions/**` files are legacy_evidence only when explicitly allowed.
- Direction Map remains distinct from Direction Spine, roadmap, backlog, Work Graph, and Action Inbox.
- Work Graph remains local to an Active Front, not a global map.
- The user is not forced to answer in YAML.
- Root bootstrap uses lifecycle signals, handlers, Event Loop Closure, Progression Router, and an exact next move.
- User confirmation is required before a runtime root package.
- Project Instructions UI updates are separated from Project Files/Sources refreshes.
- Persistent Project Binding is planned after bootstrap.
- Per-Direction Project Instructions source is planned after a concrete root package.
- Later-chat status behavior is defined through binding and exact CURRENT_STATUS/CURRENT_NEXT_MOVE reads.

## WARN checks

- Legacy files are mentioned but correctly classified as legacy_evidence.
- Exact source reads are deferred because the current answer only needs a decision request.
- A candidate root bootstrap package is drafted but not treated as accepted.
- Runtime root creation is correctly deferred pending explicit acceptance and Codex package execution.

## FAIL checks

- The Project acts as Governance Maintenance Console.
- The Project treats Project Files/Sources, uploaded files, prior summaries, or chat memory as authority.
- A runtime root is assumed or created without exact accepted source evidence and explicit package acceptance.
- Product work starts during setup/root bootstrap.
- Old `workflow/**` or `directions/**` becomes v3 accepted state by implication.
- Direction Map is flattened into Spine, roadmap, backlog, Work Graph, or Action Inbox.
- Work Graph is used as the global Direction Map.
- The user is forced to provide YAML when a terse answer can be normalized.
- No exact next move is present.
- Project Files/Sources refresh or actual Project UI update is implied by repository docs alone.
- Setup relies on Project title to infer Direction.
- Setup relies on previous chat memory.
- No persistent Project Binding is planned after bootstrap.
- No per-Direction Project Instructions source is planned after concrete root package.
- Later-chat status behavior is undefined.

## Required result fields

```text
verdict: PASS | WARN | FAIL
role_check:
source_authority_check:
runtime_root_check:
product_work_check:
legacy_import_check:
map_semantics_check:
project_files_sources_authority_check:
yaml_requirement_check:
exact_next_move_check:
unresolved_questions:
residual_risks:
```

END_OF_FILE: workflow_v3/evals/DIRECTION_PROJECT_SETUP_EVAL.md
