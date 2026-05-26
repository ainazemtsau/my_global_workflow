# 05_PORTFOLIO_QUEUE.md

```yaml
artifact_control:
  artifact_name: "05 Portfolio Queue"
  schema: portfolio_queue.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/05_PORTFOLIO_QUEUE.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-19"
  refresh_source: "OA-MIGRATION-SMP-EXOCORTEX-CORE-FOUNDATION-2026-05-19"
```

## Current queue state

Current Phase: `EXOCORTEX App Foundation`

Current Phase path: `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration`

Current Phase status: active / repaired in place by `P0_PHASE_START`

Active Goal: `EXOCORTEX Core Foundation Definition` / `goal_shaped_pending_E1`

Superseded Goal: `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof`

Superseded Goal status: preserved as superseded provenance; not executable.

Required candidate for Phase closure: `EXOCORTEX Product Foundation Definition` — shaped as active Goal `EXOCORTEX Core Foundation Definition`, pending `E1_EXECUTION_BRIEF`.

Next route: `E1_EXECUTION_BRIEF` after G1 repository patch apply/read-back and Project Files refresh.

## Required for Phase closure

```yaml
required_for_closure:
  - id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
    title: EXOCORTEX Product Foundation Definition
    status: shaped_as_active_goal_pending_E1
    smallest_useful_result: "Define EXOCORTEX Core Foundation with expandable core, memory/context persistence, model interoperability, tools/actions extensibility, interaction/process loops, workspace surfaces, Reality Alignment, first buildable foundation boundary, non-goals, and validation criteria."
    validation_link: "May satisfy Phase Minimum Outcome after R1 review/distill."
```

## Optional expansion candidates — not required for closure

```yaml
optional_expansion:
  - EXOCORTEX technical architecture map
  - tech stack shortlist
  - implementation spike
  - UI/workspace mockup
  - Event Ledger prototype
  - memory model prototype
  - external research on current AI app infrastructure
  - Codex/Task Master/product execution graph
```

Queue note:

- The accepted Direction Objective is EXOCORTEX as a persistent personal AI brain / external-brain application.
- The active queue target has moved from G1 shaping to E1 execution-brief preparation for the Core Foundation Definition artifact.
- The prior candidate `Personal Workflow System Core and MVP Definition` is too weak and is superseded by EXOCORTEX phase repair.
- Do not create `03_KERNEL_MIN_PROOF_BRIEF.md`.
- Do not build the app during this P0/G1 shaping boundary.
- Do not choose technical stack.
- Do not design full architecture.
- Do not create a product execution graph.
- Treat vNext One-Goal Smoke Test and Create Lightweight Codex Small-Fix Lane as superseded test-state unless explicitly reactivated.
- Broad product/architecture/research work remains deferred unless a later stage explicitly routes it.
