RESULT s-health-nutrition-workflow-converge-001 (call: c-health-nutrition-workflow-converge-001)
direction: health   play: converge   node/task: g-health-nutrition-system/c-health-nutrition-workflow-converge-001

outcome: |
  Closed WHAT for the Health AI nutrition workflow graph now exists as a proposed work artifact:
  live/health/work/converge-g-health-nutrition-workflow-graph.md.

  The closed WHAT states that nutrition startup and continuation must operate as an explicit graph:
  STARTUP/ROUTER -> PROGRAM -> CYCLE -> WEEK_PLAN -> DAY_LOOP -> REVIEW -> MUTATION -> next bounded state.

  The contract explicitly prevents the rejected UX failure: Health AI must not answer nutrition startup by
  dumping menu/recipe/grocery/log/review content. One chat resolves one bounded workflow state transition
  or one bounded owner-facing question/task.

  No nutrition execution was started. No menus, recipes, grocery lists, shopping instructions, daily plans,
  training/activity work, or product repo edits were produced.

evidence: |
  Direction OS state currently blocks nutrition execution until the workflow contract is converged:
  live/health/NOW.md says g-health-nutrition-system has evidence but lacks a strict owner-approved
  operating graph for program/cycle/week/day/review/mutation, and says not to start the first real
  nutrition execution cycle until the contract is converged. Source: 

  Owner requirement imported from NOW:
  - "у нас должен быть чёткий, понятный рабочий процесс, условно, как наш воркоп"
  - "каждый шаг должен быть определен чётко, куда он идёт, что после него"
  - "никакого вот этого ... AI как-то порешает"
  - "в чате должно быть, что условно один чат, он решает только один вопрос"
  Source: 

  Required workflow concepts were explicit in the active CALL/NOW: program, cycle, week plan,
  day loop, reviews, mutation rules, and a state graph where each state names purpose, inputs,
  owner-provided facts, AI-decided facts, output artifact, next state, stop/block conditions,
  and review trigger. Source: 

  Existing Health AI nutrition evidence remains useful but insufficient as owner-facing execution UX:
  the accepted G5 knowledge says nutrition had zero blocker gaps across W1-W13/NCA0-NCA9 and names
  active operational files, while NOW says those artifacts are seeds and not accepted execution flow.
  Sources:  

  Health AI already has the needed low-level owner-input boundary: owner updates may be messy
  free-form text/voice/photos; templates are internal parser/write targets only; clarifiers are limited
  to material safety, irreducible medical/allergy facts, or the next food decision.
  Sources:  

state_changes: |
  1) Add file: live/health/work/converge-g-health-nutrition-workflow-graph.md

  -----BEGIN FILE live/health/work/converge-g-health-nutrition-workflow-graph.md-----
  ---
  # Converge — g-health-nutrition-workflow-graph

  > Produced by converge session s-health-nutrition-workflow-converge-001 on 2026-06-17.
  > Assembly surface only; not a Direction OS state file.
  > Scope: workflow WHAT overlay for g-health-nutrition-system after rejected startup UX.
  > Status: CLOSED WHAT, route to converge-arch.
  > Authority: owner live instruction in c-health-nutrition-workflow-converge-001 + repair-trigger
  > words imported in live/health/NOW.md + existing nutrition WHAT/ARCH/G5 files as seeds only.

  ## §TRIAGE

  triage: **heavy** — converge **ON** — because:
  - product-defining: this is the owner-facing operating graph for nutrition startup and continuation;
  - model-bearing: a wrong default reintroduces the rejected "AI somehow decides / wall of content" UX;
  - cross-cutting: the graph spans Direction OS boundaries, Health AI state, owner interaction, and
    Health AI nutrition artifacts;
  - decomposes into a state machine: startup/router, program, cycle, week plan, day loop, review,
    mutation, block conditions, and one-chat-one-task routing.

  ## §IMPORTS

  Imported as born-closed where owner-approved or file-backed:

  - I1 — Direction OS is not a raw nutrition diary. Raw daily food logs, photos, and check-ins live
    only in Health AI nutrition; Direction OS receives summary/decision/problem/CALL only.
  - I2 — Owner-facing input is ordinary text/voice/photo. Fixed LOG templates, JSON, colon fields,
    and checklists are internal parser/write targets, never owner requirements.
  - I3 — Existing Health AI nutrition artifacts are implementation/research seeds only for this
    workflow issue. They are not accepted startup UX and must not be dumped as one owner-facing wall.
  - I4 — Existing nutrition W1-W13, NCA0-NCA9, and G5 review remain valid as lower-level nutrition
    artifact evidence; this overlay closes the missing operating graph before execution.
  - I5 — Core/shared concepts remain core-owned: phase, week, day, weight_trend, adherence,
    biofeedback, PLAN-vs-LOG, materiality, parse, and schema/versioning. Nutrition consumes them
    and writes only nutrition-namespaced fields/files.

  ## §DIRTY INPUT DISPOSITION

  - D1 — The rejected startup behavior is treated as failure evidence, not as a partial workflow.
  - D2 — Current active program/cycle/menu/grocery/fallback/log/review files may be referenced by
    later architecture/implementation as seeds, but cannot define owner-facing flow by themselves.
  - D3 — A tomorrow-start packet is not a startup router. It can be an output of a specific workflow
    state only after that state has been selected.
  - D4 — No nutrition execution output is produced by this converge session.

  ## §GLOSSARY

  | Term | meaning-here | load-bearing properties | rejected readings |
  |---|---|---|---|
  | workflow graph | Explicit Health AI nutrition state machine. Each state names purpose, inputs, owner-provided facts, AI-decided facts, output artifact, next state, stop/block conditions, and review trigger. | Removes "AI somehow decides"; every transition is named before execution. | Loose list of files; wall of content; hidden agent judgment. |
  | startup/router | First nutrition-facing operator state. It identifies current graph state, one bounded next task, whether owner input is needed, and the next CALL/action. | Prevents menu/recipe/grocery/log dump at startup. | "Here is the whole nutrition system" as first response. |
  | one-chat-one-task | Every owner-facing chat has exactly one current workflow state and one bounded output or question. | Keeps nutrition interaction compact and steerable. | One chat emits program + cycle + week menu + grocery + recipes + LOG + review instructions. |
  | program state | Larger nutrition outcome arc: success criteria, safety constraints, phase assumptions, review cadence, and mutation policy. | Program is the parent plan; it is not a menu. | Static diet sheet or generic nutrition advice. |
  | cycle state | Bounded execution loop inside a program, e.g. first cycle / next week / travel week / post-review rebuild. | Makes execution finite and reviewable. | Permanent diet forever; ad hoc daily improvisation. |
  | week plan state | Pre-execution planning state for the next week/cycle segment. It prepares the needed plan artifacts but does not itself mean execution has started. | Separates planning from daily logging and review. | Dumping all food content whenever nutrition starts. |
  | day loop state | Daily operating state where owner sends messy updates or near-term food questions; Health AI parses internally and makes/logs a bounded next-day or same-day decision. | Owner never fills templates; raw logs remain in Health AI. | Direction OS food diary; fixed daily form. |
  | review state | Decision state consuming Health AI LOG summaries, owner feedback, and core metrics to emit hold/mutate/rebuild/update/refresh/brake/medical-check language. | Review changes artifacts or explicitly holds. | Passive summary that changes nothing. |
  | mutation state | One bounded artifact/rule/state change produced by review or a material trigger. | Changes the system in a named scope. | Free-form regeneration of everything. |
  | block condition | A condition that stops normal transition and routes to conservative mode, owner material clarifier, review, or a new CALL. | Makes safe stopping explicit. | Silent continuation through ambiguity/red flags. |

  ## §SIGNOFF — DEFINE

  §SIGNOFF: owner approved workflow terms @ 2026-06-17 —
  "nutrition must work as a defined operating workflow/graph; program -> cycle -> week -> day -> review -> mutation; one chat solves one bounded question/task; existing health-ai nutrition artifacts are seeds, not accepted execution UX."

  Imported supporting owner words from NOW:
  - "у нас должен быть чёткий, понятный рабочий процесс, условно, как наш воркоп"
  - "каждый шаг должен быть определен чётко, куда он идёт, что после него"
  - "никакого вот этого ... AI как-то порешает"
  - "в чате должно быть, что условно один чат, он решает только один вопрос"

  ## §WHAT

  Status legend: all rows are `answered`.

  WG1. Startup/router contract
  status: answered
  requirement: |
    Nutrition startup must first resolve the current workflow state and present only:
    current state, one bounded next task/question, whether owner input is needed, and the next action/CALL.
    It must not emit program + cycle + week plan + menu + recipes + grocery + LOG + review content as one wall.
  source: owner repair words; CALL boundaries; GLOSSARY startup/router and one-chat-one-task.
  acceptance: |
    A nutrition startup response can be checked mechanically: it has exactly one current state and one bounded
    next action, and it contains no menu, recipe, grocery list, shopping instruction, daily plan, or raw LOG dump
    unless the selected state specifically authorizes that exact artifact.

  WG2. State graph completeness
  status: answered
  requirement: |
    Every nutrition workflow state must define these fields before execution: purpose, inputs,
    owner-provided facts, AI-decided facts, output artifact, next state, stop/block conditions, and review trigger.
  source: CALL required workflow concepts; GLOSSARY workflow graph.
  acceptance: |
    A future architect/executor can inspect each state and find all required fields. If any field is missing,
    workflow execution is blocked.

  WG3. Canonical transition path
  status: answered
  requirement: |
    Default path is STARTUP/ROUTER -> PROGRAM -> CYCLE -> WEEK_PLAN -> DAY_LOOP -> REVIEW -> MUTATION.
    MUTATION routes back to DAY_LOOP, WEEK_PLAN, CYCLE, or PROGRAM depending on mutation scope.
  source: owner requirement "program -> cycle -> week -> day -> review -> mutation"; GLOSSARY state terms.
  acceptance: |
    Health AI can name the current nutrition state and the only allowed next state(s). It does not jump from
    startup directly into multi-artifact execution content.

  WG4. Program state
  status: answered
  requirement: |
    Program state owns the larger nutrition outcome arc: objective, success criteria, safety constraints,
    current assumptions, review cadence, and mutation policy. It consumes core profile/phase/metrics and stores
    output as a Health AI nutrition program artifact or writer packet.
  source: CALL Program concept; existing active-program seed; GLOSSARY program state.
  acceptance: |
    Program setup/update produces or updates only the program-level artifact/packet. It does not produce menus,
    grocery lists, recipes, or daily plans in the same chat.

  WG5. Cycle state
  status: answered
  requirement: |
    Cycle state owns a bounded execution loop inside the program: cycle objective, duration/checkpoints,
    cycle assumptions, tracking precision, review schedule, and conditions for continuation/rebuild/brake.
  source: CALL Cycle concept; existing first-cycle seed; GLOSSARY cycle state.
  acceptance: |
    Cycle setup/update produces or updates only a cycle-level artifact/packet and names the next state
    (normally WEEK_PLAN). It does not start daily execution by itself.

  WG6. Week plan state
  status: answered
  requirement: |
    Week plan state prepares the next week/cycle segment before execution. It may produce or update the
    plan artifact categories needed for execution, but only when this state is explicitly selected.
  source: CALL Week plan concept; existing menu/grocery/recipe/fallback seeds; GLOSSARY week plan state.
  acceptance: |
    Week planning is a bounded workflow task. If menu/recipe/grocery/prep artifacts are needed, they are produced
    inside this state or as writer packets, not dumped by the startup/router or by unrelated states.

  WG7. Day loop state
  status: answered
  requirement: |
    Day loop state accepts free-form owner updates or near-term food questions, parses them internally into
    Health AI nutrition LOG state/writer packet, and returns only the bounded next daily decision or logging result.
  source: Health AI owner interaction contract; CALL Day loop concept; GLOSSARY day loop state.
  acceptance: |
    Owner is never asked to fill a LOG template or fixed checklist. Raw daily food/photo/check-in data stays
    inside Health AI nutrition, not Direction OS.

  WG8. Review state
  status: answered
  requirement: |
    Review state consumes Health AI nutrition LOG summaries, owner feedback, and core metrics/phase/biofeedback/
    adherence to emit one explicit decision: hold, mutate, rebuild, update, refresh, brake, or non-diagnostic
    medical-check language.
  source: CALL Reviews concept; existing first-cycle-review seed; GLOSSARY review state.
  acceptance: |
    A review cannot be only a passive summary. It must either hold explicitly or name the mutation/rebuild/brake
    target and the next graph state.

  WG9. Mutation state
  status: answered
  requirement: |
    Mutation state applies or packets one bounded change to Health AI nutrition artifacts/rules/state after review
    or a material trigger. It must name target artifact(s), mutation reason, expected effect, and next review trigger.
  source: CALL mutation rules concept; GLOSSARY mutation state.
  acceptance: |
    Mutation does not regenerate the whole nutrition system. If multiple unrelated changes are needed, they split
    into separate bounded tasks/CALLs.

  WG10. One-chat-one-task interaction rule
  status: answered
  requirement: |
    Every nutrition chat has one current workflow state and one bounded output/question. When multiple outputs are
    needed, the operator routes them as a sequence of states/CALLs instead of printing a wall.
  source: owner repair words; GLOSSARY one-chat-one-task.
  acceptance: |
    The owner-facing surface is compact: state, why it matters, what is blocked, one output or one question,
    and one recommended next action. No scattershot multi-artifact answer.

  WG11. Owner-facts vs AI-decided facts in every state
  status: answered
  requirement: |
    Each state must distinguish owner-provided irreducible facts from AI-decided expert variables. Health AI asks
    only material irreducible facts; expert nutrition variables are decided by the system from evidence/profile/
    phase/feedback and are not offered to owner as setup choices.
  source: imported nutrition WHAT; Health AI interaction contract; CALL boundary "Do not ask owner to choose expert nutrition variables."
  acceptance: |
    No state asks "how many meals per day?", macro targets, deficit, timing, tracking precision, or review cadence
    as owner preferences. Missing owner facts create pending/reduced/default states where safe.

  WG12. Direction OS / Health AI data boundary
  status: answered
  requirement: |
    Raw daily nutrition data, food logs, photos, and check-ins live in Health AI nutrition only. Direction OS may
    receive only summaries, decisions, problems, and next CALLs.
  source: CALL boundaries; imported G5 review; GLOSSARY day loop state.
  acceptance: |
    No workflow transition writes raw daily nutrition diary content into live/health/NOW.md, LOG.md, TREE.md,
    knowledge/, or history except as summarized RESULT evidence.

  WG13. Seed artifact authority
  status: answered
  requirement: |
    Existing Health AI nutrition artifacts are seeds and evidence, not accepted owner-facing workflow UX. They can
    satisfy state outputs only after the graph selects the relevant state and the output is bounded to that state.
  source: CALL context; GLOSSARY startup/router.
  acceptance: |
    A future session cannot justify the rejected startup wall by pointing to active program/menu/grocery/fallback/
    LOG/review files. It must route through the workflow graph first.

  WG14. Safety and block routing
  status: answered
  requirement: |
    Safety red flags, medical uncertainty, unsafe deterioration, materially missing allergy/medical facts, or
    workflow ambiguity block normal progression and route to conservative mode, one material clarifier, review,
    or a new CALL.
  source: Health AI safety boundary; existing active-program safety seed; GLOSSARY block condition.
  acceptance: |
    The graph has explicit stop/block conditions. It does not silently continue nutrition execution through
    red flags or material uncertainty, and it does not make diagnoses or prescriptions.

  ## §SIGNOFF — RESOLVE / WHAT

  §SIGNOFF: owner approved nutrition workflow graph WHAT @ 2026-06-17 —
  "nutrition must work as a defined operating workflow/graph; program -> cycle -> week -> day -> review -> mutation; one chat solves one bounded question/task; existing health-ai nutrition artifacts are seeds, not accepted execution UX."

  ## §COVERAGE

  Done_when coverage:
  - program state -> WG3, WG4.
  - cycle state -> WG3, WG5.
  - week state / week plan -> WG3, WG6.
  - day state / day loop -> WG3, WG7.
  - review state -> WG3, WG8.
  - mutation state -> WG3, WG9.
  - one-chat-one-task rule -> WG1, WG10.
  - state graph fields -> WG2.
  - existing artifacts as seeds, not accepted UX -> WG13.
  - no raw Direction OS nutrition data -> WG12.
  - no expert nutrition variables asked from owner -> WG11.
  - stop/block/review triggers -> WG2, WG8, WG9, WG14.

  Cross-node / boundary coverage:
  - Direction OS strategic boundary -> WG12.
  - Health AI owner-free-form interface -> WG7, WG10.
  - g-health-core shared concepts consumed, not duplicated -> WG4, WG5, WG8.
  - existing nutrition G5 artifacts remain seeds/evidence -> WG13.
  - no training/activity route in this issue -> WG14 blocks scope expansion.

  Mechanism decomposition coverage:
  - startup/router -> WG1.
  - state fields -> WG2.
  - transition path -> WG3.
  - bounded output rule -> WG10.
  - owner-fact vs AI-decided fact split -> WG11.
  - raw-data boundary -> WG12.
  - seed artifact authority -> WG13.
  - safety/block routing -> WG14.

  ## §OPEN / DEFERRED CHECK

  open rows: 0
  deferred rows: 0
  owner decisions needed: 0

  ## §ROUTE

  Next: converge-arch.

  Reason:
  - triage is heavy because this is a product-defining workflow/state-machine contract;
  - architecture must map WG1-WG14 to Health AI file/procedure/operator contracts before any executor CALL;
  - shape/execution remains blocked until the workflow graph passes architecture and verification.

  END_OF_FILE: live/health/work/converge-g-health-nutrition-workflow-graph.md
  -----END FILE live/health/work/converge-g-health-nutrition-workflow-graph.md-----

  2) Update live/health/NOW.md:

  Keep:
  - active_bet.status: none
  - tasks: []
  - open_calls: []
  - recurring: []
  - decisions: []

  Replace the entire `next: |` block with:

  next: |
    CALL c-health-nutrition-workflow-converge-arch-001
    to: session
    direction: health
    play: converge-arch
    node: g-health-nutrition-system
    goal: |
      Health AI nutrition has an architecture/contract surface for the newly closed workflow graph
      WHAT so startup, program, cycle, week plan, day loop, review, and mutation can be implemented
      without recreating the rejected wall-of-content UX.
    context: |
      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/work/converge-g-health-nutrition-workflow-graph.md
      - live/health/work/converge-g-health-nutrition-system.md
      - live/health/work/converge-g-health-nutrition-system-arch.md
      - live/health/knowledge/health-nutrition-system-g5-review.md
      - health-ai AGENTS.md
      - health-ai SYSTEM.md
      - health-ai x_nutrition/index.md
      - health-ai x_nutrition/procedures/operator-seams.md
      - health-ai x_nutrition/programs/active-program.md
      - health-ai x_nutrition/cycles/first-cycle.md
      - health-ai x_nutrition/logs/YYYY-MM-DD.md
      - health-ai x_nutrition/reviews/first-cycle-review.md

      Current contradiction:
      - Nutrition artifacts exist and previously passed G5, but owner rejected the startup UX because
        it produced a wall of menu/recipe/shopping/log content instead of a strict workflow.
      - The converge session closed WG1-WG14 as the WHAT overlay for the missing workflow graph.
      - Existing Health AI nutrition artifacts are seeds/evidence only, not accepted owner-facing
        workflow UX.

      Required architecture outcome:
      - Map WG1-WG14 to Health AI file/procedure/operator contracts.
      - Define how the operator resolves current workflow state and routes one-chat-one-task.
      - Define architecture boundaries for startup/router, program, cycle, week plan, day loop,
        review, mutation, block conditions, and writer handoff.
      - Preserve Direction OS raw-data boundary and Health AI free-form owner input boundary.
    boundaries: |
      Do not start nutrition execution.
      Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
      Do not move to training/activity.
      Do not edit product repo code in this session.
      Do not ask owner to choose expert nutrition variables.
      Do not add UI/app/runtime/server/database/cron/scheduler/background-worker requirements.
      Do not rewrite g-health-core or duplicate core-owned concepts.
      Keep owner-facing output compact; if too large, close with a checkpoint and next CALL.
    done_when: |
      A closed architecture/contract surface exists for the nutrition workflow graph WHAT:
      every WG1-WG14 row is mapped to concrete Health AI state/procedure/file/operator contract
      obligations or explicitly rejected as HOW, with open/deferred/blocker rows equal to zero,
      and the set is ready for converge-verify.
    return: |
      RESULT with architecture artifact changes, coverage WG1-WG14, state_changes, and next CALL.
    budget: one focused converge-arch session; workflow graph only

  3) Append to live/health/LOG.md:

  - 2026-06-17 — s-health-nutrition-workflow-converge-001: closed nutrition workflow graph WHAT overlay for g-health-nutrition-system; route to converge-arch; no nutrition execution.

  4) Add history file:

  - live/health/history/2026-06-17-s-health-nutrition-workflow-converge-001.md
    Content: this RESULT packet exactly as emitted.

captures: []

decisions_needed: []

play_check:
  - 1 Triage & import: done — imported current G5 as valid evidence but not accepted startup UX; imported owner repair words and current boundaries; triage heavy — converge ON; imported: [I1, I2, I3, I4, I5].
  - 2 Define: done — defined workflow graph, startup/router, one-chat-one-task, program, cycle, week plan, day loop, review, mutation, block condition; §SIGNOFF cites owner words: "nutrition must work as a defined operating workflow/graph; program -> cycle -> week -> day -> review -> mutation; one chat solves one bounded question/task; existing health-ai nutrition artifacts are seeds, not accepted execution UX."
  - 3 Resolve: done — closed WG1-WG14; open rows 0; deferred rows 0; owner decisions needed 0; acceptance rows cover startup/router, all required states, one-chat-one-task, owner-fact/AI-decision split, Direction OS boundary, seed artifact authority, and safety/block routing.
  - 4 Close & route: done — converge_coverage complete; canon_proposed: [workflow graph, startup/router, one-chat-one-task, program state, cycle state, week plan state, day loop state, review state, mutation state, block condition]; next routes to converge-arch because triage is heavy/product-defining.

log: 2026-06-17 — s-health-nutrition-workflow-converge-001: closed nutrition workflow graph WHAT overlay; no nutrition execution; next converge-arch.

next: |
  CALL c-health-nutrition-workflow-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    Health AI nutrition has an architecture/contract surface for the newly closed workflow graph
    WHAT so startup, program, cycle, week plan, day loop, review, and mutation can be implemented
    without recreating the rejected wall-of-content UX.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-workflow-graph.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-nutrition-system-g5-review.md
    - health-ai AGENTS.md
    - health-ai SYSTEM.md
    - health-ai x_nutrition/index.md
    - health-ai x_nutrition/procedures/operator-seams.md
    - health-ai x_nutrition/programs/active-program.md
    - health-ai x_nutrition/cycles/first-cycle.md
    - health-ai x_nutrition/logs/YYYY-MM-DD.md
    - health-ai x_nutrition/reviews/first-cycle-review.md

    Current contradiction:
    - Nutrition artifacts exist and previously passed G5, but owner rejected the startup UX because
      it produced a wall of menu/recipe/shopping/log content instead of a strict workflow.
    - The converge session closed WG1-WG14 as the WHAT overlay for the missing workflow graph.
    - Existing Health AI nutrition artifacts are seeds/evidence only, not accepted owner-facing
      workflow UX.

    Required architecture outcome:
    - Map WG1-WG14 to Health AI file/procedure/operator contracts.
    - Define how the operator resolves current workflow state and routes one-chat-one-task.
    - Define architecture boundaries for startup/router, program, cycle, week plan, day loop,
      review, mutation, block conditions, and writer handoff.
    - Preserve Direction OS raw-data boundary and Health AI free-form owner input boundary.
  boundaries: |
    Do not start nutrition execution.
    Do not produce menus, recipes, grocery lists, shopping instructions, daily plans, or food logs.
    Do not move to training/activity.
    Do not edit product repo code in this session.
    Do not ask owner to choose expert nutrition variables.
    Do not add UI/app/runtime/server/database/cron/scheduler/background-worker requirements.
    Do not rewrite g-health-core or duplicate core-owned concepts.
    Keep owner-facing output compact; if too large, close with a checkpoint and next CALL.
  done_when: |
    A closed architecture/contract surface exists for the nutrition workflow graph WHAT:
    every WG1-WG14 row is mapped to concrete Health AI state/procedure/file/operator contract
    obligations or explicitly rejected as HOW, with open/deferred/blocker rows equal to zero,
    and the set is ready for converge-verify.
  return: |
    RESULT with architecture artifact changes, coverage WG1-WG14, state_changes, and next CALL.
  budget: one focused converge-arch session; workflow graph only