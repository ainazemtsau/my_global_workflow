RESULT s-health-hq-orchestrator-converge-001 (call: c-health-hq-orchestrator-converge-001)
direction: health   play: converge   node/task: g-health-hq-goal-coordinator/t-2

outcome: |
  Converge checkpoint produced; WHAT is not owner-signed yet.

  Imported decisions:
  - Health HQ was owner-approved as a goal-management/orchestration layer, not a reviewer-only layer.
  - Owner constraints imported: reviews/checks are owner-triggered; HQ may diagnose/route but must not silently mutate domain artifacts; current/future domains need report/integration structures.
  - Repair imported: health-ai @6ca3f18 / 9ad9330 is retained only as narrow technical proof, not product acceptance.
  - Direction OS tracking boundary imported: no routine project/process tracking or raw body/nutrition/training diary in Direction OS unless owner explicitly asks.

  Triage:
  - triage: heavy — converge ON — because the node is model-bearing, cross-domain, and defines the product's goal-achievement semantics, domain demand contracts, and safety/governance boundaries.

  Draft corrected route:
  - The active bet should not continue into implementation from the summary-only proof.
  - The bet can be repaired only by narrowing the remaining route to owner-signed WHAT + research + converge-arch/verify before any corrected executor task.
  - If owner does not approve that narrowing, the current Health HQ bet should be killed/parked and health work should return to nutrition/training execution.

  Current close state:
  - Not forward-clean: Define/Resolve signoff is missing.
  - Not backward-clean enough for verify: research and owner signoff are missing.
  - Next is owner decision d-health-hq-converge-route-001.

evidence: |
  State read:
  - os/KERNEL.md: sessions do not write directly; RESULT is final; active bet/task gates and G7/G9/G10 apply.
  - os/plays/converge.md: heavy/model-bearing nodes run converge ON; Define and Resolve require signed terms/WHAT; heavy/sibling nodes route to converge-arch before converge-verify.
  - os/schema/packets.md: RESULT must contain outcome, evidence, state_changes, captures, decisions_needed, play_check, log, and next.
  - live/health/CHARTER.md: mission is sustained weight/strength/energy/maintenance with Health AI as operating support, not Direction OS raw diary.
  - live/health/TREE.md: g-health-hq-goal-coordinator already names top-level goal structure, owner requests, domain integration contracts, dry-run review, routed requests, no silent domain edits, and no raw Direction OS data.
  - live/health/NOW.md: active bet repair note says the old summary-only proof is not accepted as full Health HQ and t-2 is active for owner-signed WHAT or kill/narrow route.
  - live/health/knowledge/health-direction-os-tracking-boundary.md: Direction OS does not track projects/processes/raw health diary by default.
  - live/health/history/2026-06-29-c-health-map-evidence-001.md: research recommended a thin referee/reconciler only if bounded, not cockpit/tracker/second kernel.
  - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md: owner clarified goal management, owner-triggered checks, and domain report/integration needs.
  - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md: shaped Health HQ bet was initially scoped as thin coordinator/front door.
  - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md: owner approved the shaped bet with "approve recommended bet".
  - live/health/history/2026-07-01-s-health-hq-scope-repair-001.md: owner accepted repair route with "ок"; product proof is retained only as technical slice.
  - health-ai @6ca3f18:
    - x_health_hq/evidence-summary.md says the proof is summary-only, fixture-backed, and limited by pending current metrics.
    - x_health_hq/reviews/2026-07-01-dry-run-progress-review.md returns blocked_missing_metrics, coordination_bottleneck, non-mutating routed requests, and boundary flags.
    - tools/check_health_hq_thin_slice.py validates only a REVIEW-only summary coordinator proof.

  External calibration used:
  - NIDDK Choosing a Safe and Successful Weight-loss Program:
    https://www.niddk.nih.gov/health-information/weight-management/choosing-a-safe-successful-weight-loss-program
    Relevant calibration: safe weight-loss programs include realistic goals, eating plan, physical activity, habit support, monitoring/feedback/support, and maintenance; first 5-10% loss in about 6 months is a realistic initial target.
  - CDC Adult Physical Activity Guidelines:
    https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
    Relevant calibration: adults need at least 150 minutes moderate-intensity activity weekly and 2 days muscle-strengthening weekly.
  - WHO Physical Activity fact sheet:
    https://www.who.int/news-room/fact-sheets/detail/physical-activity
    Relevant calibration: activity affects cardiovascular/metabolic health, body adiposity, mental health, cognitive health, and sleep; all activity counts.

state_changes: |
  Apply from the current state where:
  - live/health/NOW.md still has task t-2 active.
  - live/health/NOW.md still has open_calls containing c-health-hq-orchestrator-converge-001.
  - live/health/work/converge-g-health-hq-goal-coordinator.md does not exist.
  - live/health/history/2026-07-02-s-health-hq-orchestrator-converge-001.md does not exist.

  live/health/NOW.md:
  - Keep active_bet:
      id: b-health-hq-goal-coordinator-v0-001
      node: g-health-hq-goal-coordinator
      status: active
      appetite: 5 calendar days
      started: 2026-07-01
      kill_by: >
        2026-07-06 end-of-day Europe/Amsterdam. Kill/review if by this date Health HQ cannot
        show a corrected, owner-signed route toward goal-achievement orchestration, or if the
        work remains only a status/review dispatcher without milestone/metric/strategy/domain-demand
        structure for reaching the root health goal.
  - Keep active_bet.repair_note/proof_kept/cut_list/lens_sweep/assumptions/forecast/against/next_if_true/next_if_false unchanged.
  - Update task t-2 as:
      - id: t-2
        node: g-health-hq-goal-coordinator
        status: active
        kind: session
        goal: >
          Health HQ has an owner-signed WHAT for goal-achievement orchestration, or the current bet is
          explicitly killed/narrowed with a clear next route.
        done_when: >
          Corrected requirements explicitly cover root-goal achievement, milestones/phases, metrics,
          strategy/review loop, domain demand contracts, and the difference between safety boundaries
          and the product's positive purpose.
        checkpoint: >
          Converge triage/import completed. Draft Health HQ goal-achievement WHAT/route exists in
          live/health/work/converge-g-health-hq-goal-coordinator.md. The WHAT is not owner-signed.
          Owner decision d-health-hq-converge-route-001 is required before research/arch/verify or kill/park routing.
  - Replace open_calls with: []
  - Replace decisions with:
      - id: d-health-hq-converge-route-001
        q: >
          How should Health HQ proceed after converge found that the current proof is too narrow?
        options:
          - A: approve recommended narrow route — keep Health HQ alive only as WHAT/research/architecture now; no new Health AI implementation until research + converge-arch + converge-verify pass.
          - B: kill/park Health HQ now and return to nutrition/training execution.
          - C: deliberately cut HQ to status/review-only and accept the existing summary-only technical slice as v0.
        bad_because:
          A: >
            Delays product build.
          B: >
            Leaves cross-domain goal management unmanaged.
          C: >
            Contradicts the owner repair and collapses Health HQ back into status dispatcher.
        recommendation: >
          A, because it preserves the owner-corrected product essence — goal-achievement orchestration through
          milestones, metrics, strategy loop, and domain demand contracts — while preventing more implementation on
          the rejected status-dispatcher route. B is safer than C if owner no longer wants HQ now. C is not recommended.
  - Replace next with:
      awaiting_decision d-health-hq-converge-route-001
  - Keep recurring r-health-ai-minor-fix-lane unchanged.
  - Maintain END_OF_FILE trailer.

  live/health/work/converge-g-health-hq-goal-coordinator.md:
  - Add the following new file exactly:

    # converge — g-health-hq-goal-coordinator

    imported:
      - live/health/history/2026-06-29-c-health-map-evidence-001.md
      - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
      - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
      - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md
      - live/health/history/2026-07-01-s-health-hq-scope-repair-001.md
      - live/health/knowledge/health-direction-os-tracking-boundary.md
      - health-ai @6ca3f18 / 9ad9330 technical proof

    triage:
      type: heavy
      converge: ON
      because: >
        The node defines a cross-domain, model-bearing product layer: root-goal achievement orchestration,
        phase/milestone/metric governance, strategy loop, domain demand contracts, and authority boundaries.
        Wrong stub is product-fatal.

    ## §GLOSSARY — draft, not signed

    | id | term | meaning-here | load-bearing properties | competing readings |
    |---|---|---|---|---|
    | G1 | Health HQ | Owner-facing Health AI layer for orchestrating achievement of the root health goal. | owns goal view, phase/milestones, metric gap view, strategic review loop, decision log, domain demand routing; does not execute domain artifacts | status dashboard/reviewer; god-agent; medical advisor |
    | G2 | root health goal | The health direction outcome: weight moves from 125 kg toward 90–95 kg, strength improves, systems persist through maintenance, Health AI supports the process. | long horizon; weight + strength + adherence + maintenance + AI support | short-term weight cut; training-only goal |
    | G3 | milestone / phase | A bounded segment of the root goal with target metrics, exit criteria, and dominant bottleneck class. | target/current separation; phase exit criteria; phase-specific domain demands | arbitrary calendar label; fixed medical prescription |
    | G4 | target/current metrics | Target = desired value/range/status for the phase; current = summary-level state or explicit pending/unknown reason. | no raw Direction OS diary; source is core/domain summary; can be pending | raw logs; dashboard telemetry |
    | G5 | strategic review loop | Owner-triggered process comparing target/current, naming verdict, bottleneck, domain demands, owner decisions, and missing metrics. | owner-triggered; summary-only; produces route, not silent edits | automatic polling; daily coach; diagnosis |
    | G6 | domain demand contract | Consumer-driven contract where HQ states what outcome/support/summary it needs from a domain. | responsibility, supported goals, report format, exposed signals, request types, boundaries | direct command; domain artifact mutation |
    | G7 | execution domain | Nutrition, training/activity, sleep/recovery, or future domain that owns its own artifacts and procedures. | domain owns execution and mutation; HQ can request/recommend; owner/governance gates approve material changes | HQ-owned submodule |
    | G8 | owner conversation surface | Plain-language entry points such as "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить процесс?" | maps to HQ intents; asks clarification only when material ambiguity blocks routing | chatty dashboard; general assistant |
    | G9 | summary-only technical slice | Existing x_health_hq proof that reads fixtures/summaries and emits non-mutating routed requests. | technical evidence only; not full product acceptance | sufficient HQ v0 |

    ## §WHAT — draft, not signed

    | id | status | kind | line |
    |---|---|---|---|
    | W1 | proposed | acceptance | Health HQ's positive essence is goal-achievement orchestration for G2, not status display, dashboard, prompt-only review, or generic dispatcher. →GLOSSARY:G1[owns goal view, phase/milestones, metric gap view, strategic review loop, decision log, domain demand routing] |
    | W2 | proposed | acceptance | Health HQ must represent at least three root-goal phases: first clinical/behavioral milestone, scale-to-athletic range, and maintenance. Each phase has target metrics, current metrics/pending reasons, exit criteria, and dominant bottleneck class. →GLOSSARY:G2[long horizon] →GLOSSARY:G3[target/current separation] |
    | W3 | proposed | acceptance | Target metrics must cover weight trend, adherence/nutrition support, strength/body-composition progression, activity/conditioning, recovery/sleep/pain/energy signals, and review cadence; exact formulas and thresholds are PLAN/research unless already fixed by CHARTER. →GLOSSARY:G4[target] |
    | W4 | proposed | acceptance | Current metrics must come from Health AI core/domain summary surfaces or be marked pending/unknown with reason; Direction OS receives only summary/decision/problem/next CALL, not raw data. →GLOSSARY:G4[current] |
    | W5 | proposed | acceptance | Strategic review loop must produce: progress verdict, bottleneck/uncertainty, strategy implication, routed domain demand/request, owner decision if needed, and metrics needed now/later. →GLOSSARY:G5[produces route, not silent edits] |
    | W6 | proposed | acceptance | Owner conversation surface must support at least: "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?" and route each to an HQ intent without requiring fixed wording. →GLOSSARY:G8[maps to HQ intents] |
    | W7 | proposed | acceptance | Nutrition demand contract must allow HQ to request/report on deficit support, satiety/hunger, protein/meal structure, adherence friction, fallback food, meal-prep/cooking bottlenecks, and nutrition review need; nutrition owns menus/recipes/logs and approved mutations. →GLOSSARY:G6[responsibility, supported goals, report format, exposed signals, request types, boundaries] |
    | W8 | proposed | acceptance | Training/activity demand contract must allow HQ to request/report on weekly load, strength progression readiness, completion/adherence, activity/conditioning volume, pain/fatigue/recovery constraints, substitutions, and program-foundation status; training/activity owns programs/weeks/sessions/logs and approved mutations. →GLOSSARY:G6[responsibility, supported goals, report format, exposed signals, request types, boundaries] |
    | W9 | proposed | acceptance | Sleep/recovery must be represented as a demand area even if not implemented as a full domain in this bet: HQ may request needed summary signals or recommend shaping a future domain, but must not diagnose or silently create a medical/sleep protocol. →GLOSSARY:G6[request types, boundaries] |
    | W10 | proposed | acceptance | Future domains must integrate through the same contract shape: responsibility, supported root-goal contribution, summary/report format, exposed metrics/signals, accepted request types, and non-mutation boundaries. →GLOSSARY:G6[responsibility, supported goals, report format, exposed signals, request types, boundaries] |
    | W11 | proposed | acceptance | Authority split: HQ may decide/recommend/request progress verdicts, bottleneck classes, needed metrics, strategy implications, domain demand shapes, and escalation routes; domains execute and mutate domain artifacts; owner/governance approves material plan changes, new domains, and any safety/medical escalation. →GLOSSARY:G1[does not execute domain artifacts] →GLOSSARY:G7[domain owns execution and mutation] |
    | W12 | proposed | research_needed | Before implementation, run deep research on evidence-based goal-achievement orchestration for this health context: milestone/phase model, metric hierarchy, behavior-change loop, review cadence, safety escalation, and domain demand contract checklist. Output must include 3–5 refuted model options and a recommended decision-class checklist for converge-verify. |
    | W13 | proposed | route | Current active bet is repairable only if narrowed now to WHAT/research/arch/verify; no new executor work should be issued from the summary-only proof. If owner rejects narrowing, kill/park Health HQ and return to nutrition/training execution. |
    | W14 | answered | imported_technical_slice | The existing x_health_hq proof is retained as lower-level technical evidence for summary-only input, fixture marking, non-mutating routed requests, and boundary flags; it is not product acceptance for W1-W13. |

    ## §COVERAGE — draft

    done_when coverage:
      - Health HQ as orchestrator of reaching root health goal -> W1, W2
      - milestones/phases and target/current metrics -> W2, W3, W4
      - strategic review loop and owner conversation surface -> W5, W6
      - domain demand contracts for nutrition/training/sleep/future -> W7, W8, W9, W10
      - what HQ may decide/recommend/request vs domains/owner/governance -> W11
      - research needed before implementation -> W12
      - whether active bet can be repaired or killed/re-shaped -> W13

    mechanism parameter coverage:
      - summary-only proof -> W14
      - owner-triggered review -> W5, W6
      - demand routing -> W7, W8, W9, W10, W11
      - metric model -> W2, W3, W4
      - boundary against silent edits/raw data/medical/dashboard/API/polling -> W4, W11, W13, W14

    ## §SIGNOFF

    Define:
      status: missing
      reason: owner has not yet signed G1-G9 meanings and competing readings after this converge checkpoint.

    Resolve:
      status: missing
      reason: owner has not yet approved route W13, and W12 research has not returned.

    ## recommended_next_if_owner_approves_A

    CALL c-health-hq-goal-achievement-model-research-001
    to: research
    direction: health
    play: research
    node: g-health-hq-goal-coordinator
    task: t-2
    parent: c-health-hq-orchestrator-converge-001
    goal: |
      Produce the evidence-backed goal-achievement orchestration model Health HQ needs before implementation.
    context: |
      Read:
      - live/health/CHARTER.md
      - live/health/TREE.md
      - live/health/NOW.md
      - live/health/knowledge/health-direction-os-tracking-boundary.md
      - live/health/history/2026-06-29-c-health-map-evidence-001.md
      - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
      - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
      - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md
      - live/health/history/2026-07-01-s-health-hq-scope-repair-001.md
      - work/converge-g-health-hq-goal-coordinator.md
      - health-ai @6ca3f18 x_health_hq/evidence-summary.md
      - health-ai @6ca3f18 x_health_hq/reviews/2026-07-01-dry-run-progress-review.md
      - health-ai @6ca3f18 tools/check_health_hq_thin_slice.py

      Health HQ must be goal-achievement orchestration, not a status dispatcher. Research should ground:
      - phase/milestone model for large weight-loss + strength/body-composition + maintenance;
      - metric hierarchy and target/current split;
      - owner-triggered strategic review loop;
      - domain demand contracts for nutrition, training/activity, sleep/recovery, future domains;
      - authority split: HQ decides/recommends/requests vs domains execute vs owner/governance approves.
    boundaries: |
      No medical diagnosis or treatment plan.
      No raw body/nutrition/training data in Direction OS.
      No Health AI implementation.
      No dashboard/API/polling/integration design.
      Do not accept the summary-only proof as product acceptance.
    done_when: |
      Research returns:
      - 3-5 refuted model options for Health HQ goal-achievement orchestration;
      - recommended model with reasons and failure modes;
      - minimum metric hierarchy for current phase + later phases;
      - milestone/phase model suitable for large weight loss, strength/body-composition, adherence, energy/recovery, and maintenance;
      - owner-triggered strategic review loop;
      - domain demand contract checklist for nutrition, training/activity, sleep/recovery, and future domains;
      - safety/recovery escalation boundaries;
      - decision-class checklist suitable for converge-verify;
      - explicit questions that must remain owner decisions.
    return: |
      RESULT to parent c-health-hq-orchestrator-converge-001 with evidence, recommended model, rejected options,
      checklist/canon candidates, owner-decision questions if any, and next route.
    budget: one research session

    END_OF_FILE: live/health/work/converge-g-health-hq-goal-coordinator.md

  live/health/LOG.md:
  - Append:
      2026-07-02 — health/g-health-hq-goal-coordinator converge checkpoint: imported HQ owner corrections and repair, triaged node as heavy/converge ON, drafted corrected Health HQ goal-achievement WHAT/route, and blocked on owner decision A narrow-to-research/arch/verify vs B kill/park vs C accept review-only slice. → history/2026-07-02-s-health-hq-orchestrator-converge-001.md
  - Maintain END_OF_FILE trailer.

  live/health/history/2026-07-02-s-health-hq-orchestrator-converge-001.md:
  - Add this full RESULT.
  - Maintain END_OF_FILE trailer.

captures:
  - future-canon: after research/verify, promote a health-goal-orchestration decision-class checklist to knowledge/ for future converge-verify sessions.
  - parked: visual Health HQ dashboard/cockpit can be revisited only after text-first orchestration proves value.
  - parked: sleep/recovery may become its own domain later, but current HQ work should only define demand-contract needs and boundaries.
  - risk: accepting fixture-backed summary proof as product acceptance would recreate the exact status-dispatcher drift repaired on 2026-07-01.

decisions_needed:
  - q: >
      Approve the recommended Health HQ route after converge checkpoint?
    why_it_matters: >
      This decides whether remaining appetite is spent on correct WHAT/research/architecture before implementation,
      or whether Health HQ is killed/parked and health work returns to nutrition/training execution.
    options:
      - A: approve recommended narrow route — keep Health HQ alive only as WHAT/research/architecture now; no new Health AI implementation until research + converge-arch + converge-verify pass.
      - B: kill/park Health HQ now and return to nutrition/training execution.
      - C: deliberately cut HQ to status/review-only and accept the existing summary-only technical slice as v0.
    bad_because:
      A: >
        Delays product build.
      B: >
        Leaves cross-domain goal management unmanaged.
      C: >
        Contradicts the owner repair and collapses HQ back into status dispatcher.
    recommendation: >
      A. It is the smallest route that preserves Health HQ's corrected positive essence — orchestrating achievement
      of the health goal through milestones, metrics, strategy loop, and domain demand contracts — while preventing
      further implementation on the rejected summary-only route.

play_check:
  - 1 Triage & import: done — imported owner-approved HQ node, shape approval, scope repair, Direction OS tracking boundary, and retained technical proof; triage: heavy — converge ON — because the node is model-bearing and cross-domain.
  - 2 Define: partial — seeded draft §GLOSSARY G1-G9 from done_when/lens words and known competing readings; not signed because owner must choose route/sign terms after checkpoint.
  - 3 Resolve: partial — drafted §WHAT W1-W14 covering all CALL done_when criteria and mechanism parameters; rows remain proposed/not signed; research-needed row W12 blocks responsible implementation.
  - 4 Close & route: checkpoint — coverage map exists, but converge is not forward-clean/backward-clean and cannot route to converge-verify; next is awaiting owner decision d-health-hq-converge-route-001.

log: |
  2026-07-02 — health/g-health-hq-goal-coordinator converge checkpoint: imported HQ owner corrections and repair, triaged node as heavy/converge ON, drafted corrected Health HQ goal-achievement WHAT/route, and blocked on owner decision A narrow-to-research/arch/verify vs B kill/park vs C accept review-only slice. → history/2026-07-02-s-health-hq-orchestrator-converge-001.md

next: |
  awaiting_decision d-health-hq-converge-route-001
END_OF_FILE: live/health/history/2026-07-02-s-health-hq-orchestrator-converge-001.md
