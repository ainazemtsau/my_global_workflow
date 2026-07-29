RESULT s-health-nutrition-t1-research-program-procedure-001 (call: c-health-nutrition-t1-research-program-procedure-001)
direction: health   play: work   node/task: g-health-nutrition-system/t-1
outcome: |
  In health-ai, Health AI nutrition now owns a first-class research-to-program setup/refresh
  procedure in the pending `x_nutrition` namespace. The repo contains a broad Deep Research
  packet, expected output schema, normalizer contract, runnable acceptance harness, and explicit
  first setup pending state.

  No actual Deep Research report was available, so no method landscape conclusions, calorie or
  macro targets, menu, first cycle, or active personalized nutrition program were invented.
evidence: |
  Product repo: C:\projects\health-ai
  Commit: ce930bc nutrition t-1: add research-to-program setup
  Push: origin/main updated from 8bc980a to ce930bc.

  Files:
  - AGENTS.md
  - CLAUDE.md
  - README.md
  - SYSTEM.md
  - x_nutrition/index.md
  - x_nutrition/procedures/research-to-program.md
  - x_nutrition/research/deep-research-packet.md
  - x_nutrition/contracts/deep-research-output.schema.json
  - x_nutrition/contracts/normalizer-contract.md
  - x_nutrition/state/first-setup-pending.md
  - acceptance/x_nutrition/research-setup-matrix.json
  - acceptance/x_nutrition/research-setup-evidence-summary.md
  - tools/check_nutrition_research_setup.py

  Research-to-program procedure:
  - `x_nutrition/procedures/research-to-program.md` defines first setup, targeted refresh,
    artifact-mutation-only paths, operator-invoked trigger, stop conditions, file boundaries,
    report validation, report normalization, artifact writes, and refresh triggers.

  Broad Deep Research prompt/schema:
  - `x_nutrition/research/deep-research-packet.md` is owner/operator-ready and explicitly says
    not to assume a preselected diet.
  - `x_nutrition/contracts/deep-research-output.schema.json` requires report metadata, evidence
    method, owner profile, owner-fact gaps, method landscape, evidence reference, personalization
    decisions, active-program blueprint, first cycle, tracking/review, safety, refresh triggers,
    and artifact write plan.

  Normalizer contract:
  - `x_nutrition/contracts/normalizer-contract.md` maps an actual report into method landscape,
    evidence reference, active program, first cycle, menu/recipe/grocery/fallback/log/review
    artifacts, pending-state update, and writer-compatible change packet.

  First setup/bootstrap evidence:
  - `x_nutrition/state/first-setup-pending.md` records known owner profile and pending irreducible
    facts; `actual_deep_research_report` is `missing`; active program, method landscape, evidence
    reference, and first cycle are `not_generated`.

  Check output:
  - `python tools/check_nutrition_research_setup.py` => PASS; required artifacts 8; acceptance
    rows 7 pass, 0 fail; blocker gaps 0; actual Deep Research report missing, setup left pending.
  - `python tools/check_acceptance_matrix.py` => PASS; acceptance rows 17; contract rows 9;
    plan agenda rows 27; architecture inputs 9; blocker gaps 0.
  - `python tools/check_core_slice.py` => PASS; 32 core files checked; schema/frontmatter OK;
    matrix target files OK; formula check OK; PLAN/LOG separation OK; forbidden module/runtime
    directories absent.
  - `python tools/check_core_evidence.py` => PASS; dry-run scenarios 11; acceptance/contract
    rows 26 pass, 0 fail; blocker gaps 0.
state_changes: |
  live/health/NOW.md:
  - tasks.t-1.status: active -> done.
  - open_calls: remove c-health-nutrition-t1-research-program-procedure-001.
  - open_calls: add c-health-nutrition-first-setup-deep-research-001 for g-health-nutrition-system first setup.
  - next: replace c-health-nutrition-t1-research-program-procedure-001 with c-health-nutrition-first-setup-deep-research-001.

  live/health/LOG.md:
  - Append: 2026-06-17 — health/g-health-nutrition-system/t-1 work: health-ai x_nutrition research-to-program setup committed and pushed (ce930bc); actual Deep Research report missing, first setup left pending with packet/schema/normalizer; next Deep Research report. → history/2026-06-17-s-health-nutrition-t1-research-program-procedure-001.md

  live/health/history/2026-06-17-s-health-nutrition-t1-research-program-procedure-001.md:
  - Save this full RESULT.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done; t-1 serves active bet b-health-nutrition-system-full-001 and requires a Health AI nutrition research-to-program setup/refresh procedure or explicit pending Deep Research packet.
  - 2 Owner inputs (owner): skipped with reason; this was an engineering procedure/harness task, not owner-content for immediate personal use. Known owner facts from CHARTER were reused; no new owner words were required, and no expert variables were asked.
  - 3 Do the work: done; implemented pending `x_nutrition` namespace in health-ai and pushed commit ce930bc.
  - 4 Self-check: done; nutrition harness and all three core checks passed; no actual report was available, so first setup remained pending rather than invented.
  - 5 Close: done; t-1 marked done and next research CALL prepared for the actual Deep Research report before t-2.
log: health/g-health-nutrition-system/t-1 work: health-ai x_nutrition research-to-program setup committed and pushed (ce930bc); actual Deep Research report missing, first setup left pending with packet/schema/normalizer; next Deep Research report.
next: |
  CALL c-health-nutrition-first-setup-deep-research-001
  to: research
  direction: health
  play: research
  node: g-health-nutrition-system
  goal: |
    A source-cited owner nutrition evidence report exists in Health AI-compatible structured form
    for the first setup.
  context: |
    Direction state:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md

    Product evidence:
    - health-ai commit ce930bc nutrition t-1: add research-to-program setup
    - pushed to origin/main
    - x_nutrition/research/deep-research-packet.md
    - x_nutrition/contracts/deep-research-output.schema.json
    - x_nutrition/contracts/normalizer-contract.md
    - x_nutrition/state/first-setup-pending.md
    - acceptance/x_nutrition/research-setup-evidence-summary.md

    Current state:
    - Health AI owns the nutrition research-to-program procedure.
    - Actual Deep Research report is missing.
    - First owner setup is explicitly pending; no active nutrition program, method conclusions,
      calorie/macro targets, or menus were invented.
    - Known owner profile: male, 35, 182 cm, 125 kg, BMI about 37.7; sustainable weight loss
      toward 90-95 kg; preserve strength/muscle/energy/adherence; sport and diet experience;
      cooking infrastructure; scale; willing to use AI tracking; no stated restrictions yet.
  boundaries: |
    Do not assume a preselected diet.
    Do not produce a generic menu-only answer.
    Do not ask owner to choose expert variables such as meals/day, deficit, protein, timing,
    tracking precision, intermittent fasting, calorie cycling, diet breaks, or refeeds.
    Do not diagnose or prescribe medically.
    Do not require UI/app/vitrine/Mealie/Notion/runtime/DB/server/cron/scheduler/background-worker.
    Do not store raw daily nutrition logs in Direction OS.
  done_when: |
    - A source-cited report is returned or saved in schema-compatible form for
      x_nutrition/contracts/deep-research-output.schema.json.
    - The report compares a broad method landscape without preselecting a diet.
    - It covers evidence reference, owner-fact gaps, system-decided variables, active-program
      blueprint, first-cycle assumptions, safety boundaries, tracking/review framework,
      and refresh triggers.
    - It supports no structured training initially and adaptation when training starts later.
    - If the report is not good enough to normalize, blocker gaps are explicit.
  return: |
    RESULT with report artifact/path or paste-ready report, schema coverage, source list,
    blocker gaps if any, and next CALL for t-2 executor if usable.
  budget: one Deep Research pass
  surface: Deep Research capable model
  parent: s-health-nutrition-t1-research-program-procedure-001

END_OF_FILE: live/health/history/2026-06-17-s-health-nutrition-t1-research-program-procedure-001.md
