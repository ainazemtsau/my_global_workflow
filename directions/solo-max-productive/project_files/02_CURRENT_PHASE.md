# 02_CURRENT_PHASE.md

```yaml
artifact_control:
  artifact_name: "02 Current Phase"
  schema: current_phase.v1
  owner_layer: persistence
  status: projection
  source_file: "directions/solo-max-productive/project_files/02_CURRENT_PHASE.md"
  default_load: yes
  freshness: fresh
  last_refresh_at: "2026-05-13"
  refresh_source: "G1-2026-05-13-exocortex-phase-repair"

current_phase:
  state: repair_required_pending_p0
  phase_name: Personal Workflow App Kernel Exploration
  phase_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration"
  repair_target_phase_name: EXOCORTEX App Foundation
  critical_constraint: "The Phase must be repaired before Goal shaping continues. The target is the future EXOCORTEX application / personal external brain; the current ChatGPT + GitHub + Codex workflow remains the construction workflow and should not be replaced until the new system is radically better and ready."
  minimum_outcome: "P0 repairs or restarts the Phase as EXOCORTEX App Foundation, with clear phase objective, closure criteria, constraints, and first Goal candidate for EXOCORTEX Product Foundation Definition."
  validation_signal: "A repaired Phase exists whose objective is to build the foundation for the future EXOCORTEX application, not to make a temporary convenience replacement for the current workflow."

phase_intent:
  summary: "Build the foundation for EXOCORTEX: a future personal AI application / external brain with memory, tools, working environment, learning loops, Reality Alignment, and progressive autonomy."
  nuance:
    - "The current ChatGPT + GitHub + Codex workflow remains the working construction system."
    - "The user will not switch to EXOCORTEX until it is radically better and sufficiently complete."
    - "The EXOCORTEX document is required concept input for Phase repair."
    - "The first repaired Goal should define product/application foundation, not execute implementation."
    - "Future LLMs should amplify the EXOCORTEX substrate rather than replace it."
    - "Max Vision remains large; P0/G1 must cut scope into a buildable foundation without pretending the final app is small."

guard_state:
  active_goal_unresolved: true
  active_goal: "Personal Workflow App Kernel Min Proof"
  active_goal_status: invalidated_by_phase_repair_pending_p0
  active_goal_path: "directions/solo-max-productive/phases/personal-workflow-app-kernel-exploration/goals/personal-workflow-app-kernel-min-proof"
  proposed_phase_repair: "EXOCORTEX App Foundation"
  proposed_first_goal_after_repair: "EXOCORTEX Product Foundation Definition"
  next_route: P0_PHASE_START
  route_note: "Launch via Router/new P0 run; G1 stopped and does not directly execute P0."
  blocker: phase_misframed_for_exocortex_target
```

## Phase repair brief

The current Phase frame is too weak for the clarified target. The target is not current-workflow convenience replacement. The target is a future EXOCORTEX application / personal external brain.

P0 should decide whether to repair this phase in place or start a new phase container. The repaired Phase should keep the scope bounded: foundation definition first, no implementation, no stack choice, no full architecture, no Task Master/Codex product execution graph.

## Anti-duplicate requirement for P0

P0 must include a visible line:

```text
Почему это не повтор прошлой фазы:
<concrete delta>
```

Expected delta: the prior frame asked whether the current workflow should evolve toward a custom app/kernel; the repaired frame treats EXOCORTEX as the accepted future target and uses the current workflow only as the construction system.
