RESULT s-health-nutrition-t1-framing-repair-001 (call: owner-correction-2026-06-17)
direction: health   play: repair   node/task: g-health-nutrition-system/t-1

outcome: |
  NOW.md corrected the t-1 framing for the active nutrition bet. The next step is no longer a
  standalone ChatGPT Deep Research guide before Health AI nutrition exists. It is now an executor
  CALL for ainazemtsau/health-ai to implement Health AI nutrition's research-to-program
  setup/refresh procedure and use the first owner setup as bootstrap or explicit pending Deep
  Research packet.

evidence: |
  Owner correction supplied 2026-06-17:
  "the issue is separating a one-off Deep Research run from building Health AI nutrition's own
  research capability. The revised next CALL should implement the research loop in-system and use
  the first research pass only as proof, not as external prep."

  Current state before repair:
  - NOW.md t-1 was kind: guide, surface: ChatGPT Deep Research.
  - NOW.next was CALL c-health-nutrition-t1-deep-research-program-001 to session/play guide.

  Corrected state:
  - NOW.md t-1 is kind: executor, repo: ainazemtsau/health-ai.
  - NOW.next is CALL c-health-nutrition-t1-research-program-procedure-001 to executor/kind engineering.
  - open_calls registry replaced the old one-off research guide call with the executor capability/bootstrap call.

state_changes: |
  Applied the following Direction OS state changes.

  1) live/health/NOW.md

  Replaced active_bet.riskiest_assumption with:

    Health AI nutrition can own a repeatable research-to-program procedure: request broad Deep Research,
    normalize it into an actionable active program, persist it in GitHub-state, and refresh it later
    without turning research into an external one-off.

  Replaced task t-1 with an executor task:

    - id: t-1
      kind: executor
      repo: ainazemtsau/health-ai
      status: active
      goal: >
        Implement Health AI nutrition's research-to-program procedure and use it to bootstrap the first
        personalized nutrition program flow.
      done_when: >
        Health AI nutrition has a research-backed setup/refresh procedure; the procedure can generate a broad
        Deep Research request/prompt with expected output schema; it defines how Deep Research output is normalized
        into evidence base, method landscape, active nutrition program, first-cycle assumptions, safety boundaries,
        tracking/review framework, refresh triggers, and writer-compatible Health AI nutrition file changes; it
        supports first owner setup and later targeted refreshes; if an actual Deep Research report is unavailable,
        the output is an owner/operator-ready Deep Research packet plus explicit pending state, not invented research
        conclusions.
      evidence_expected: >
        Commit/PR, file list, research-to-program procedure, broad Deep Research prompt and output schema,
        normalizer contract, first-setup/pending-state evidence, writer-compatible change examples, and checks.

  Replaced open_calls entry c-health-nutrition-t1-deep-research-program-001 with:

    - id: c-health-nutrition-t1-research-program-procedure-001
      to: executor
      for: t-1
      issued: 2026-06-17
      note: >
        Implement Health AI nutrition research-to-program procedure/bootstrap in the product repo.

  Replaced NOW.next with:

    CALL c-health-nutrition-t1-research-program-procedure-001
    to: executor
    direction: health
    node: g-health-nutrition-system  task: t-1
    repo: ainazemtsau/health-ai
    kind: engineering
    goal: |
      Health AI nutrition has a first-class research-to-program setup/refresh procedure, and the first owner
      nutrition setup is bootstrapped through that procedure or left as an explicit pending Deep Research packet.
    context: |
      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/work/converge-g-health-nutrition-system.md
      - live/health/work/converge-g-health-nutrition-system-arch.md
      - live/health/knowledge/health-core-corrected-g5-review.md
      - health-ai acceptance/core/evidence-summary.md
      - health-ai core/extensions/attach-contract.md
      - health-ai core/procedures/template-contract.md
      - health-ai core/provenance/day-type.md

      Correction:
      Deep Research must not be treated as external one-off prep before Health AI nutrition exists.
      Health AI nutrition must own the research-to-program process: decide when research is needed,
      generate a broad Deep Research request, define the expected output schema, normalize the report into
      evidence/reference/program artifacts, persist those artifacts in GitHub-state, and support later targeted
      refreshes when training, plateau, hunger, medical constraints, travel, bad weeks, or maintenance transition
      make existing evidence insufficient.

      Owner profile known from charter:
      male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
      strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
      cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

      Shape requirements:
      - No nutrition feature cuts.
      - Health AI nutrition has research capability as a first-class procedure, not a one-time external report.
      - Use broad Deep Research through that procedure, not a hardcoded narrow diet prompt.
      - Do not assume a preselected diet.
      - Produce the procedure, prompt/schema, normalizer contract, and first setup/bootstrap path for:
        research brief + method landscape/reference + personalized active nutrition program.
      - Program must support no structured training initially and adaptation when training starts later.
      - Expert variables are system-decided; ask only irreducible owner facts.
      - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
    boundaries: |
      Do not fake Deep Research if an actual Deep Research report is not available.
      Do not make research an external one-off outside Health AI nutrition.
      Do not create a generic menu-only answer or hardcode a preselected diet.
      Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
      tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
      Do not prescribe medically or diagnose.
      Do not rewrite g-health-core.
      Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
      Do not store raw daily nutrition logs in Direction OS.
    done_when: |
      - Nutrition has a research-backed setup/refresh procedure in the Health AI nutrition namespace.
      - The procedure can generate a broad Deep Research prompt and expected output schema without assuming a
        preselected diet.
      - The procedure defines how Deep Research output becomes method landscape, evidence reference, active
        nutrition program, first cycle assumptions, safety boundaries, tracking/review framework, refresh triggers,
        and writer-compatible file changes.
      - It supports first owner setup and later targeted refreshes.
      - If the actual report is missing, the repo contains an owner/operator-ready Deep Research packet and explicit
        pending state, not invented research conclusions.
    return: |
      RESULT with commit/PR, file list, checks, research-to-program procedure, prompt/schema, normalizer contract,
      first setup/bootstrap or pending Deep Research packet evidence, state_changes, and next CALL.
    budget: one focused executor movement
    surface: coding agent in health-ai product repo

  2) live/health/LOG.md

  Appended:

    2026-06-17 — repair g-health-nutrition-system/t-1: corrected next from one-off Deep Research guide to Health AI research-to-program executor capability/bootstrap; old open call replaced. → history/2026-06-17-s-health-nutrition-t1-framing-repair-001.md

  3) live/health/history/2026-06-17-s-health-nutrition-shape-001.md

  Appended missing trailer:

    END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-shape-001.md

captures:
  - Watch for future CALL wording where an external tool run can be mistaken for a system capability; keep the capability as the durable owner of the process.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done; NOW.next one-off Deep Research guide contradicted owner correction that Health AI nutrition must own the research capability
  - 2 Reconstruct: done; newest evidence is commit 49f12cf plus owner correction supplied 2026-06-17
  - 3 Propose corrected state: done; corrected t-1/open_calls/next to executor capability/bootstrap
  - 4 Confirm: done; owner correction supplied the intended replacement framing: "The revised next CALL should implement the research loop in-system and use the first research pass only as proof, not as external prep."
  - 5 Friction: done; no os/FRICTION.md entry, treated as one-off CALL-framing ambiguity rather than an OS rule defect

log: |
  repair g-health-nutrition-system/t-1: corrected next from one-off Deep Research guide to Health AI research-to-program executor capability/bootstrap; old open call replaced.

next: |
  CALL c-health-nutrition-t1-research-program-procedure-001
  to: executor
  direction: health
  node: g-health-nutrition-system  task: t-1
  repo: ainazemtsau/health-ai
  kind: engineering
  goal: |
    Health AI nutrition has a first-class research-to-program setup/refresh procedure, and the first owner
    nutrition setup is bootstrapped through that procedure or left as an explicit pending Deep Research packet.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai core/extensions/attach-contract.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md

    Correction:
    Deep Research must not be treated as external one-off prep before Health AI nutrition exists.
    Health AI nutrition must own the research-to-program process: decide when research is needed,
    generate a broad Deep Research request, define the expected output schema, normalize the report into
    evidence/reference/program artifacts, persist those artifacts in GitHub-state, and support later targeted
    refreshes when training, plateau, hunger, medical constraints, travel, bad weeks, or maintenance transition
    make existing evidence insufficient.

    Owner profile known from charter:
    male, 35, 182 cm, 125 kg, BMI about 37.7; goal is sustainable weight loss toward 90-95 kg,
    strength/muscle/energy protection, long-term adherence and maintenance. Owner has sport/diet experience,
    cooking infrastructure, scale, willingness to use AI tracking; no stated restrictions yet.

    Shape requirements:
    - No nutrition feature cuts.
    - Health AI nutrition has research capability as a first-class procedure, not a one-time external report.
    - Use broad Deep Research through that procedure, not a hardcoded narrow diet prompt.
    - Do not assume a preselected diet.
    - Produce the procedure, prompt/schema, normalizer contract, and first setup/bootstrap path for:
      research brief + method landscape/reference + personalized active nutrition program.
    - Program must support no structured training initially and adaptation when training starts later.
    - Expert variables are system-decided; ask only irreducible owner facts.
    - Output must be suitable for t-2 implementation as Health AI nutrition module on g-health-core.
  boundaries: |
    Do not fake Deep Research if an actual Deep Research report is not available.
    Do not make research an external one-off outside Health AI nutrition.
    Do not create a generic menu-only answer or hardcode a preselected diet.
    Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
    tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
    Do not prescribe medically or diagnose.
    Do not rewrite g-health-core.
    Do not add UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker requirements.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    - Nutrition has a research-backed setup/refresh procedure in the Health AI nutrition namespace.
    - The procedure can generate a broad Deep Research prompt and expected output schema without assuming a
      preselected diet.
    - The procedure defines how Deep Research output becomes method landscape, evidence reference, active
      nutrition program, first cycle assumptions, safety boundaries, tracking/review framework, refresh triggers,
      and writer-compatible file changes.
    - It supports first owner setup and later targeted refreshes.
    - If the actual report is missing, the repo contains an owner/operator-ready Deep Research packet and explicit
      pending state, not invented research conclusions.
  return: |
    RESULT with commit/PR, file list, checks, research-to-program procedure, prompt/schema, normalizer contract,
    first setup/bootstrap or pending Deep Research packet evidence, state_changes, and next CALL.
  budget: one focused executor movement
  surface: coding agent in health-ai product repo

END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-t1-framing-repair-001.md
