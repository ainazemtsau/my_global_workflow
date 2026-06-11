# 00_DIRECTION_START_HERE.md

```yaml
artifact_control:
  artifact_name: "00 START HERE - Direction"
  schema: direction_start_here.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/00_DIRECTION_START_HERE.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-19"
  refresh_source: "OA-MIGRATION-SMP-EXOCORTEX-CORE-FOUNDATION-2026-05-19"
```

## Current pointers

Current Phase: EXOCORTEX App Foundation -> `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration`

Current Phase status: active / repaired in place by `P0_PHASE_START`

Phase path note: the folder slug remains `personal-workflow-app-kernel-exploration` temporarily. This is intentional to avoid duplicate active Phase state and migration overhead before the EXOCORTEX foundation definition exists.

Active Goal: EXOCORTEX Core Foundation Definition -> `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/exocortex-core-foundation-definition`

Active Goal status: `goal_shaped_pending_E1`

Superseded Goal: Personal Workflow App Kernel Min Proof -> `directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof`

Superseded Goal status: preserved as superseded/replaced provenance. It must not proceed to `E1_EXECUTION_BRIEF`.

Required first Goal candidate for Phase closure: EXOCORTEX Product Foundation Definition -> `goal_shaped_pending_E1`. This existing candidate now means EXOCORTEX Core Foundation Definition.

Current focus: Prepare E1 execution brief for producing the EXOCORTEX Core Foundation Definition.

Next route: `E1_EXECUTION_BRIEF`; launch is blocked until this G1 repository patch is applied/read back and Project Files cache is manually refreshed.

Direction Map: initialized / M0-reviewed / migrated from uninitialized stub. Use `08_DIRECTION_MAP.md` as current strategic routing authority.

State note:

- vNext One-Goal Smoke Test is obsolete test/pilot state from Workflow vNext-R validation.
- Do not continue Create Lightweight Codex Small-Fix Lane unless the user explicitly reactivates it.
- The old active Goal, Personal Workflow App Kernel Min Proof, is superseded as an execution target.
- The prior replacement candidate, Personal Workflow System Core and MVP Definition, is superseded by the EXOCORTEX App Foundation phase repair.
- The EXOCORTEX concept document is required context for E1 Core Foundation execution brief preparation.
- G1 formalized `exocortex-core-foundation-definition` on 2026-05-19. E1 must produce the minimum HOW for the definition artifact, not implementation.
- Do not create `03_KERNEL_MIN_PROOF_BRIEF.md`.
- Do not delete the old Goal folder; preserve it as superseded/replaced provenance.
- Do not start app implementation, choose a stack, design full architecture, or create a Codex product execution graph before the Core Foundation Definition is reviewed.

## Phase Closure Contract

Closure criteria:

1. A reviewed EXOCORTEX Core Foundation Definition exists.
   - Evidence required: accepted Goal output or Goal review showing core substrate, memory/context persistence, model interoperability, tools/actions extensibility, interaction/process loops, workspace surfaces, learning from outcomes, Reality Alignment, non-goals, validation criteria, and first buildable foundation boundary.
2. The foundation explicitly separates Max Vision from Min Proof / buildable foundation.
   - Evidence required: clear not-now boundaries for implementation, stack, full architecture, omnichannel expansion, automation buildout, and UI surface proliferation.
3. The old proof/replacement framing is durably superseded.
   - Evidence required: Project Files show old Goal preserved as provenance, not executable current work.
4. Phase continuation after foundation definition requires an explicit phase-progress decision.
   - Evidence required: `phase_progress_gate` after R1 determines whether `P9_PHASE_CLOSE`, continuation, or Human Decision is appropriate.

Required goal map:

```yaml
required_for_closure:
  - goal_id: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
    name: EXOCORTEX Product Foundation Definition
    status: goal_shaped_pending_E1
    meaning: EXOCORTEX Core Foundation Definition
    evidence_required: accepted Core Foundation definition and R1 review/distill result
optional_expansion:
  - EXOCORTEX technical architecture map
  - tech stack shortlist
  - implementation spike
  - UI/workspace mockup
  - Event Ledger prototype
  - memory model prototype
  - external research on current AI app infrastructure
  - Codex/Task Master/product execution graph
first_phase_closing_candidate_if_known: G1-CAND-2026-05-13-EXOCORTEX-PRODUCT-FOUNDATION
after_goal_gate_policy:
  phase_progress_gate_after_R1: required
  optional_expansion_not_required_for_closure: true
  P9_required_when_completed_goal_may_satisfy_minimum_outcome: true
```

## Default Project Files to load

Load these Direction Project Files by default:

1. `00_DIRECTION_START_HERE.md`
2. `01_DIRECTION_STATE.md`
3. `02_CURRENT_PHASE.md`
4. `03_FOCUS_REGISTER.md`
5. `04_ACTIVE_GOAL.md`
6. `05_PORTFOLIO_QUEUE.md`
7. `06_CONTEXT_LIBRARY_INDEX.md`
8. `07_PHASE_MEMORY_INDEX.md`
9. `08_DIRECTION_MAP.md`

Also load shared runtime cache files defined in:

```text
workflow/runtime/WORKFLOW_RUNTIME_CACHE_MANIFEST.md
```

If `08_DIRECTION_MAP.md` is uninitialized or marked `needs_m0_review`, run `M0_DIRECTION_MAP` to migrate/build the map from current `00-07` progress and user-provided initiative context before relying on it for strategic Phase/Goal selection.

## Shared runtime file

- `workflow/runtime/WF_VNEXT_R_RUNTIME_CORE.md`

Do not create or require a local runtime-core copy under this Direction `project_files/` folder.
