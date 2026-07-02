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
| W12 | deferred | research_needed | Before implementation, run deep research on evidence-based goal-achievement orchestration for this health context: milestone/phase model, metric hierarchy, behavior-change loop, review cadence, safety escalation, and domain demand contract checklist. Output must include 3–5 refuted model options and a recommended decision-class checklist for converge-verify. Deferred to c-health-hq-goal-achievement-model-research-001. |
| W13 | answered | route | Owner approved route A on 2026-07-02 with "A": current active bet is repairable only by narrowing now to WHAT/research/arch/verify. No new executor work is authorized from the summary-only proof. |
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

Route:
  status: signed
  evidence: >
    owner approved route A @ 2026-07-02 — "A"

Define:
  status: missing
  reason: >
    Glossary G1-G9 remain draft until research returns and owner signs the final meanings/properties.

Resolve:
  status: partial
  reason: >
    W13 route is signed; W12 is deferred to research; W1-W11/W14 remain draft until research and owner signoff.

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
