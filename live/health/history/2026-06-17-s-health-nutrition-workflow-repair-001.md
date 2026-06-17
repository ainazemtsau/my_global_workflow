RESULT s-health-nutrition-workflow-repair-001 (call: owner-repair-request-2026-06-17)
direction: health   play: repair   node/task: g-health-nutrition-system

outcome: |
  NOW.md no longer routes health to shape/start the first real nutrition execution cycle.
  It now routes to a converge session for a strict Health AI nutrition workflow graph:
  program -> cycle -> week -> day -> review -> mutation, with one bounded chat/task per
  movement and no owner-facing walls.

evidence: |
  Owner explicitly rejected the current startup behavior and requested state update:
  "Давай тогда обнови стейт, дай мне next whole card по нужному формату."
  He also clarified the required operating model:
  - "у нас должен быть чёткий, понятный рабочий процесс, условно, как наш воркоп"
  - "каждый шаг должен быть определен чётко, куда он идёт, что после него"
  - "никакого ... AI как-то порешает"
  - "в чате должно быть, что условно один чат, он решает только один вопрос"

  Contradicting prior state:
  - live/health/NOW.md previously routed to c-health-first-nutrition-cycle-shape-001.
  - The owner-facing test showed the Health AI nutrition execution surface is not ready
    for shaping/starting: it dumped menu/recipe/shopping/log content instead of operating
    through a strict workflow.

state_changes: |
  Apply these exact Direction OS state changes.

  1) live/health/NOW.md

  Replace the active_bet.note with:

    No active bet. g-health-nutrition-system remains closed by prior binding G5 file/functionality
    evidence, but the first owner-facing nutrition startup attempt exposed a workflow defect:
    Health AI nutrition has artifacts, yet no strict owner-approved operating graph for program,
    cycle, week, day, review, and mutation flow. Do not shape/start the first real nutrition
    execution cycle or move to training until the nutrition workflow contract is converged.

  Keep tasks: [], open_calls: [], recurring: [], decisions: [].

  Replace NOW.next with CALL c-health-nutrition-workflow-converge-001 exactly as written in
  the updated NOW.md.

  2) live/health/LOG.md

  Append:
  - 2026-06-17 — health nutrition workflow repair: owner rejected first nutrition startup surface as structurally wrong; NOW rerouted from first-cycle shape to converge a strict nutrition workflow graph before execution/training. → history/2026-06-17-s-health-nutrition-workflow-repair-001.md

  3) live/health/history/

  Save this RESULT as:
  live/health/history/2026-06-17-s-health-nutrition-workflow-repair-001.md

captures:
  - Product repo follow-up: after workflow converge/verify, health-ai x_nutrition artifacts likely need retrofit; do not patch them ad hoc before the workflow contract is closed.
  - UX rule: one nutrition chat should solve one bounded workflow question/task and close with next state, not print a broad menu/log wall.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — NOW.next said first-cycle shape/start; owner-visible evidence says nutrition execution workflow is structurally unready.
  - 2 Reconstruct: done — prior G5 covered file/functionality evidence, but owner test exposed missing workflow graph; health-ai commit 2a3988f fixed only free-form logging leakage, not workflow.
  - 3 Propose corrected state: done — keep no active bet, reroute NOW.next to c-health-nutrition-workflow-converge-001.
  - 4 Confirm: done — owner approved repair/update with "Давай тогда обнови стейт, дай мне next whole card по нужному формату."
  - 5 Friction: skipped — this is a Health AI product/workflow defect, not a Direction OS rule defect; no os/FRICTION.md edit.

log: >
  2026-06-17 — health nutrition workflow repair: owner rejected first nutrition startup
  surface as structurally wrong; NOW rerouted from first-cycle shape to converge a strict
  nutrition workflow graph before execution/training.

next: |
  CALL c-health-nutrition-workflow-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition has an owner-approved workflow contract that makes program, cycle,
    week, day, review, and mutation states unambiguous before any nutrition execution starts.
  context: |
    Current visible contradiction:
    - Direction OS NOW previously routed to shape/start the first real nutrition execution cycle.
    - Owner tested the Health AI nutrition startup surface and rejected it as structurally wrong:
      it produced a wall of menu/recipe/shopping/log content instead of a strict workflow.
    - Owner requirement: nutrition must work like a defined operating workflow/graph, not
      "AI decides somehow"; one chat should solve one bounded question/task and avoid walls.

    Owner words from the repair trigger:
    - "у нас должен быть чёткий, понятный рабочий процесс, условно, как наш воркоп"
    - "каждый шаг должен быть определен чётко, куда он идёт, что после него"
    - "никакого вот этого ... AI как-то порешает"
    - "в чате должно быть, что условно один чат, он решает только один вопрос"

    Treat existing health-ai nutrition artifacts as implementation/research seeds, not as an
    accepted owner-facing execution workflow:
    - health-ai commit 2a3988f fixed only free-form logging leakage; it did not solve the
      missing workflow graph.
    - Existing active program/menu/grocery/fallback/log/review files may be used as evidence
      and raw material, but the next session must not assume they are accepted UX or execution flow.

    Required workflow concepts to resolve:
    - Program: a larger outcome arc, e.g. 12 weeks or several months, with success criteria.
    - Cycle: a bounded execution loop inside a program, potentially weekly.
    - Week plan: menu/food plan built with owner participation before execution.
    - Day loop: free-form owner updates parsed internally; no owner-facing templates.
    - Reviews: day/week/cycle/program reviews with explicit mutation rules.
    - State graph: each state names purpose, inputs, owner-provided facts, AI-decided facts,
      output artifact, next state, stop/block conditions, and review trigger.

    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md
    - health-ai AGENTS.md, SYSTEM.md, x_nutrition/index.md, and current x_nutrition artifacts.
  boundaries: |
    Do not store raw daily food logs, photos, or check-ins in Direction OS.
    Do not start the first nutrition execution cycle.
    Do not produce menus, recipes, grocery lists, shopping instructions, or daily food plans.
    Do not move to training/activity yet.
    Do not build or edit product repo code in this session.
    Do not ask owner to choose expert nutrition variables.
    Do not make medical diagnoses or prescriptions.
    Keep owner-facing output compact: one bounded workflow question/task per chat; if the
    work is too large, close with a checkpoint and the next CALL rather than printing a wall.
  done_when: |
    A closed owner-approved WHAT for the Health AI nutrition workflow graph exists, covering
    program/cycle/week/day/review/mutation states and the one-chat-one-task interaction rule,
    with acceptance rows ready for converge-verify or converge-arch as the play requires.
  return: |
    RESULT with workflow WHAT artifact changes, owner decisions if any, state_changes, and next CALL.
  budget: one focused converge session; one workflow issue only

END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-workflow-repair-001.md
