# converge — g-health-hq-goal-coordinator

imported:
  - live/health/history/2026-06-29-c-health-map-evidence-001.md
  - live/health/history/2026-06-30-s-health-owner-wants-planning-001-continue.md
  - live/health/history/2026-06-30-s-health-shape-hq-goal-coordinator-001.md
  - live/health/history/2026-07-01-s-health-shape-hq-goal-coordinator-approval-001.md
  - live/health/history/2026-07-01-s-health-hq-scope-repair-001.md
  - live/health/history/2026-07-02-s-health-hq-orchestrator-converge-001.md
  - live/health/history/2026-07-02-s-health-hq-orchestrator-route-approval-001.md
  - live/health/history/2026-07-03-c-health-hq-goal-achievement-model-research-001.md
  - live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md
  - live/health/knowledge/health-direction-os-tracking-boundary.md
  - health-ai @6ca3f18 / 9ad9330 technical proof

triage:
  type: heavy
  converge: ON
  because: >
    The node defines a cross-domain, model-bearing product layer: root-goal achievement
    orchestration, phase/milestone/metric governance, strategic review loop, domain demand
    contracts, decision classes, and authority/safety boundaries. Wrong stub is product-fatal.

research_return:
  source_artifact: live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md
  status: integrated_into_owner_review_candidate
  constraints:
    - research is input only, not product acceptance
    - research does not initialize Health HQ
    - research does not authorize implementation
    - raw research must not be sent directly to executor

## §GLOSSARY — owner-review candidate

| id | term | meaning-here | load-bearing properties | competing readings rejected or constrained | status |
|---|---|---|---|---|---|
| G1 | Health HQ | Owner-facing Health AI layer for orchestrating achievement of the root health goal. | owns goal view, phase/milestones, metric gap view, bottleneck classification, strategic review loop, decision log, and domain demand routing; does not execute or silently mutate domain artifacts | status dashboard/reviewer; dashboard/cockpit; prompt-only coach; god-agent; medical advisor; polling/API hub | answer_candidate |
| G2 | root health goal | Direction outcome: weight moves from 125 kg toward 90–95 kg, strength improves, systems persist through maintenance, Health AI supports the process without Direction OS raw diary. | long horizon; weight + strength + adherence + maintenance + AI support | short-term cut; training-only goal; product-building goal detached from body execution | answer_candidate |
| G3 | milestone / phase | Bounded segment of G2 with purpose, entry condition, exit condition, target/current metric relationship, dominant bottleneck class, and phase-specific domain demands. | target/current separation; exit criteria; domain demands change by phase | arbitrary calendar label; fixed medical prescription | answer_candidate |
| G4 | decision-grade metric hierarchy | Minimum set of metrics/signals that can change a decision now, later, or only after becoming reliable. | now/later/pending split; no metric zoo; source/freshness/confidence required | dashboard telemetry; raw logs; decorative analytics | answer_candidate |
| G5 | current summary state | Summary-level state exposed by Health AI core/domain surfaces or marked pending with reason, source, freshness, and confidence. | Direction OS receives summaries/decisions/problems/next calls only; raw body/nutrition/training data stay outside Direction OS | raw diary in HQ/Direction OS; invented numbers | answer_candidate |
| G6 | strategic review loop | Owner-triggered process turning an owner intent into progress verdict, bottleneck, strategy implication, routed domain demands, owner decision need, needed metrics, and next owner-facing action. | owner-triggered; summary-only; produces route and decisions, not silent edits | automatic polling; daily unsolicited coach; generic commentary | answer_candidate |
| G7 | bottleneck class | Decision-facing classification of the main constraint on progress. | at least: adherence, plan mismatch, recovery/capacity, measurement gap, safety uncertainty, governance gap; includes confidence | vague motivational label; medical diagnosis | answer_candidate |
| G8 | domain demand contract | Consumer-driven contract where HQ states what outcome/support/summary it needs from a domain. | responsibility, root-goal contribution, report format, exposed signals, accepted request types, must-not-request boundary, approval-required changes, safety flags, freshness/fixture/pending status | direct command; domain artifact mutation | answer_candidate |
| G9 | execution domain | Nutrition, training/activity, sleep/recovery, or future domain that owns its own artifacts and procedures. | domain owns execution and mutation; HQ can request/recommend/route; owner/governance gates approve material changes | HQ-owned submodule | answer_candidate |
| G10 | owner conversation surface | Plain-language entry points such as "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить процесс?" | maps owner intent to HQ review types; asks clarification only when material ambiguity blocks routing | chatty dashboard; general assistant | answer_candidate |
| G11 | decision class | Authority category for an HQ output. | advisory, approval-required, blocked; material strategy/boundary changes require owner/governance | autonomous optimization | answer_candidate |
| G12 | safety/recovery boundary | Non-medical escalation gate: HQ can stop escalation, flag risk, request domain review, and ask owner about professional input; HQ must not diagnose or treat. | stop/hold escalation; route to domain review; owner-facing concern; no diagnosis/treatment | medical advisor; “push through red flags” | answer_candidate |
| G13 | summary-only technical slice | Existing x_health_hq proof that reads fixtures/summaries and emits non-mutating routed requests. | technical evidence only; reusable subcomponent; not product acceptance | sufficient HQ v0 | answered |

## §WHAT — owner-review candidate

| id | status | kind | line |
|---|---|---|---|
| W1 | answer_candidate | acceptance | Health HQ's positive essence is owner-triggered goal-achievement orchestration for G2, not status display, dashboard/cockpit, prompt-only review, generic dispatcher, polling system, integration hub, god-agent, or medical advisor. →GLOSSARY:G1[owns goal view, phase/milestones, metric gap view, bottleneck classification, strategic review loop, decision log, domain demand routing] |
| W2 | answer_candidate | acceptance | Health HQ must represent the root-goal phase model with at least: preparation/control capture, first clinical milestone, scaling toward target corridor, target range/recomposition, and 12-month maintenance. Each phase has purpose, entry/exit condition, target/current relationship, dominant bottleneck classes, and phase-specific domain demands. →GLOSSARY:G3[target/current separation; exit criteria; domain demands change by phase] |
| W3 | answer_candidate | acceptance | Metric hierarchy must distinguish current-phase minimum metrics, later metrics, and parked/non-mandatory metrics until decision impact. Current minimum covers weight trend, distance to first 5–10% milestone from 125 kg, nutrition adherence/support, strength adherence, activity/conditioning volume, sleep/recovery, energy/pain/day function, and review age/cadence. →GLOSSARY:G4[now/later/pending split; no metric zoo] |
| W4 | answer_candidate | acceptance | Current metrics must come from Health AI core/domain summary surfaces or be marked pending with reason/source/freshness/confidence; Direction OS receives only summary/decision/problem/next CALL, not raw body/nutrition/training logs. →GLOSSARY:G5[Direction OS receives summaries/decisions/problems/next calls only] |
| W5 | answer_candidate | acceptance | Strategic review loop must produce: progress verdict, bottleneck class + confidence, strategy implication, routed non-mutating domain demands, owner decision need if material, needed metrics now/later, and next owner-facing action. →GLOSSARY:G6[produces route and decisions, not silent edits] |
| W6 | answer_candidate | acceptance | Owner conversation surface must support at least: "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?", and route each to a defined HQ review type without requiring fixed wording. →GLOSSARY:G10[maps owner intent to HQ review types] |
| W7 | answer_candidate | acceptance | Bottleneck taxonomy must include at least: adherence, plan mismatch, recovery/capacity, measurement gap, safety uncertainty, and governance gap; HQ must name confidence and what would change the classification. →GLOSSARY:G7[decision-facing classification] |
| W8 | answer_candidate | acceptance | Every current/future domain integrates through the same demand contract shape: responsibility, root-goal contribution, summary/report format, exposed metrics/signals, accepted request types, must-not-request classes, approval-required changes, safety/recovery flags, and freshness/fixture/pending status. →GLOSSARY:G8[responsibility, report format, signals, requests, boundaries] |
| W9 | answer_candidate | acceptance | Nutrition demand contract must allow HQ to request/report on deficit sustainability, satiety/hunger, protein/meal structure, adherence friction, fallback food, meal-prep/cooking bottlenecks, lapse patterns, and nutrition review need; nutrition owns menus/recipes/logs and approved mutations. →GLOSSARY:G8[non-mutating requests] →GLOSSARY:G9[domain owns execution and mutation] |
| W10 | answer_candidate | acceptance | Training/activity demand contract must allow HQ to request/report on planned vs completed sessions, weekly load, strength progression readiness, activity/conditioning volume, pain/fatigue/recovery constraints, substitutions, and program-foundation status; training/activity owns programs/weeks/sessions/logs and approved mutations. →GLOSSARY:G8[non-mutating requests] →GLOSSARY:G9[domain owns execution and mutation] |
| W11 | answer_candidate | acceptance | Sleep/recovery must be represented as a demand area in v0 even if not a full implemented domain: HQ may request summary signals or recommend shaping a future domain, but must not diagnose, treat, or silently create a medical/sleep protocol. →GLOSSARY:G12[non-medical escalation gate] |
| W12 | answer_candidate | acceptance | Future domains must enter through the same contract shape and explicit contribution to G2; HQ must not invent hidden powers for a new domain or treat an undeclared capability as present. →GLOSSARY:G8[contract shape] |
| W13 | answer_candidate | acceptance | Authority split: HQ may review, classify, recommend, request, route, and ask for owner decisions; domains execute and mutate domain artifacts through their own procedures; owner/governance approves material strategy changes, boundary changes, new domain classes, and safety/medical escalation choices. →GLOSSARY:G11[advisory, approval-required, blocked] |
| W14 | answer_candidate | acceptance | HQ outputs are non-mutating request objects such as: review phase-fit, prepare 2–3 options, compare risks, check recovery compatibility, prepare owner-reviewable proposal. HQ must not issue commands like “rewrite plan to X calories,” “reduce training by 30%,” “change phase without approval,” “ignore pain,” or “copy raw logs into Direction OS.” →GLOSSARY:G8[accepted request types; must-not-request classes] |
| W15 | answer_candidate | acceptance | Decision classes are: advisory = explanation/verdict/request with no mutation; approval-required = material strategy/boundary/phase/domain change; blocked = unsafe/out-of-scope action such as diagnosis/treatment, raw-data leak, silent domain edit, or dashboard/API/polling implementation creep. →GLOSSARY:G11[authority category] |
| W16 | answer_candidate | acceptance | Safety/recovery boundary: HQ can mark unsafe-to-escalate, hold deficit/load escalation, request domain review, and ask owner to consider professional/medical input; HQ must not diagnose, treat, reassure away red flags, or frame rapid unexplained loss/symptoms as automatic success. →GLOSSARY:G12[stop/hold escalation; no diagnosis/treatment] |
| W17 | answered | imported_technical_slice | Existing x_health_hq proof is retained as technical evidence for summary loading, fixtures/adapters, non-mutating routed requests, and boundary flags. It is not product acceptance for W1-W16 or W18-W21. →GLOSSARY:G13[technical evidence only] |
| W18 | answered | route | Owner approved route A on 2026-07-02 with "A": current active bet is repairable only by narrowing now to WHAT/research/architecture/verify. No new executor work is authorized from the summary-only proof. |
| W19 | answered | research_input | Deep research returned and was accepted as input on 2026-07-03. Source artifact: live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md. Parent converge converted it into this owner-review candidate; raw research must not be sent directly to executor. |
| W20 | answer_candidate | acceptance | Next Health AI implementation, after owner signoff + converge-arch + converge-verify, must return evidence for: owner-triggered reviews for main intent classes, phase-aware verdict, bottleneck classification + strategy implication, non-mutating requests across at least nutrition/training/sleep-recovery, owner approval gate on material change, review/decision log without raw data, x_health_hq used as subcomponent only, and safety boundary demonstration. |
| W21 | answer_candidate | acceptance | Dashboard/API/polling/integration design is outside v0. Health HQ may have bounded owner-facing summary views, but v0 must not depend on dashboard UI, wearable/API integrations, background polling, database architecture, or automatic self-checking. |

## §PHASE_MODEL

| phase | purpose | entry condition | exit condition | dominant bottlenecks | nutrition demand | training/activity demand | sleep/recovery demand | review trigger |
|---|---|---|---|---|---|---|---|---|
| P1 preparation/control capture | Obtain a minimally reliable governed system. | Root goal exists and at least summary-capable domain surfaces or fixtures exist. | Baseline, phase target, owner-approved initial strategy, and usable summaries for 2–3 weeks. | measurement gap; too-complex plan; early adherence failure | Prepare 1–3 realistic reduced-intake strategies and adherence summary format. | Provide minimum viable training/activity template with planned-vs-completed summary. | Provide basic green/yellow/red signals for sleep, energy, pain. | No usable summaries; early red flags; no downward trend after starter window. |
| P2 first clinical milestone | Reach 5–10% loss from 125 kg with acceptable sustainability. | Baseline fixed and initial strategy running. | 118.75–112.5 kg or equivalent percent loss with controlled recovery signals. | adherence drift; weekends; excessive deficit; low activity; recovery friction | Determine whether nutrition strategy holds and where it breaks. | Achieve minimum activity floor and strength adherence. | Check whether sleep/energy/pain now blocks progress. | 2–4 weeks stagnation; rising pain/fatigue; compliance drop; data uncertainty. |
| P3 scale toward target corridor | Continue from first milestone toward near-target range without losing operability. | First milestone reached or nearly reached. | About 95–100 kg range with continued operability. | adaptive slowdown; accumulated fatigue; demotivation; strength decline | Adjust strategy without breaking adherence. | Preserve strength and increase activity contribution as appropriate. | Prevent recovery degradation during long process. | Stall over 3–4 weeks; meaningful strength decline; worsened sleep/energy. |
| P4 target range/recomposition | Enter 90–95 kg and shift emphasis toward strength/composition/owner-visible look. | Weight close enough to target corridor for composition decisions to matter. | 90–95 kg plus owner-confirmed target-range strategy. | too-fast pace with strength loss; look vs performance conflict; unreliable body-comp proxies | Move from pure deficit to sustainable composition support. | Use owner-approved strength markers and progression compatible with body mass. | Prevent chronic under-recovery. | Weight falls while strength/function declines; owner rejects visual criterion. |
| P5 maintenance | Hold 90–95 kg or owner-approved corridor for 12 months. | Entry into target corridor. | 12 months maintained by owner-approved corridor rule. | regain creep; reduced self-monitoring; activity drop; poor lapse response | Maintenance nutrition support, relapse prevention, response plans. | Maintain activity and strength base at maintenance standard. | Maintain stable sleep/recovery baseline. | Exit from corridor; repeated lapse cycles; activity drop; unresolved fatigue. |

## §METRIC_HIERARCHY

Current-phase minimum metrics:

| metric | target | current/source rule | decision impact |
|---|---|---|---|
| weight trend | Phase-consistent downward trend, not daily noise. | Latest weekly or 7-day aggregate from tracking/body summary; if absent, mark pending with reason. | Continue strategy; request nutrition review; check adherence; hold load escalation. |
| first 5–10% milestone | 118.75 kg for 5%; 112.5 kg for 10% from 125 kg. | Baseline + weight trend summary. | Phase transition; strategy sustain/revise/escalate. |
| nutrition adherence/support | Enough adherence/support to plausibly create sustainable deficit. | Nutrition summary: on-track/partial/off-track + blocker. | Request nutrition review; change structure; avoid blaming training for stall. |
| strength adherence | Agreed minimum strength sessions/key movement exposure completed. | Training/activity summary planned vs completed. | Simplify/hold/escalate training template. |
| activity/conditioning volume | Phase-appropriate floor first, higher later for maintenance if needed. | Training/activity summary minutes/steps/sessions. | Add NEAT/cardio; hold; delay escalation. |
| sleep/recovery | No evidence that deficit/load breaks recovery. | Sleep/recovery or training summary green/yellow/red + top signal. | Block escalation; request recovery review. |
| energy/pain/day function | Compatible with continuation. | Interference level from sleep/recovery or training summary. | Deload, pause escalation, domain review, owner decision. |
| review age/cadence | Not older than owner-approved cadence for active phase. | HQ review log. | Require review before strategy change. |

Later metrics, only when they change decisions:

| metric | activation condition | source rule | decision impact |
|---|---|---|---|
| strength baseline markers | Owner has chosen 3–5 reproducible markers. | Training domain. | Protect strength/body composition during weight loss. |
| waist or waist-to-height ratio | Reliable repeatable measurement exists. | Tracking/body summary. | Clarify body-composition progress when scale is noisy. |
| body-composition estimate | Reliable method exists and affects decisions. | Pending until reliable source exists. | Recomposition-phase decisions. |
| maintenance activity volume | Target corridor reached or near. | Training/activity summary. | Maintenance standard and relapse response. |
| target-corridor duration | In 90–95 kg or owner-approved corridor. | HQ phase state + weight trend summary. | Maintenance success / relapse response. |

Non-mandatory in v0 until decision impact:
- exact daily calories in Direction OS
- high-detail macro tables
- HRV/resting-HR/wearable readiness
- consumer-device body-fat estimates
- VO2max estimates
- detailed micronutrient analytics

## §STRATEGIC_REVIEW_LOOP

Owner-triggered only; no polling, cron, or hidden background review.

| step | HQ action | required property |
|---|---|---|
| 1 intent routing | Classify owner intent: today / week review / progress / bottleneck / add process. | Plain-language routing; clarification only if material ambiguity blocks routing. |
| 2 load summary state | Load only needed domain summaries and HQ decisions. | No raw logs. |
| 3 reviewability check | Check data freshness, fixture/live status, domain availability, and confidence. | If insufficient, return explicit insufficiency and next data need. |
| 4 target vs current comparison | Compare phase target to current summary metrics. | Decision-grade comparison, not passive display. |
| 5 bottleneck classification | Name main bottleneck and confidence. | Uses G7 classes; can mark uncertainty. |
| 6 strategy implication | State what bottleneck means for course. | continue / revise / hold escalation / domain review / owner decision. |
| 7 routed domain demand | Produce non-mutating request objects. | Domain executes inside its own procedure. |
| 8 owner decision if needed | Formulate A/B/C decision if material change is required. | No silent material changes. |
| 9 review/decision log | Write short summary of decision/problem/next call. | Direction OS boundary preserved. |
| 10 next owner-facing action | State next management step. | Actionable and bounded. |

Required review output shape:
- Progress: on-track / at-risk / stalled / blocked / unsafe-to-escalate
- Main bottleneck: class + short reason
- Confidence: high / medium / low
- Strategy implication: what changes or holds
- Domain requests: nutrition / training-activity / sleep-recovery / future domain when applicable
- Owner decision required: yes/no; if yes, options and recommendation
- Metrics needed now
- Metrics later
- Next owner-facing action

Owner intent routing:
- "что сегодня?" -> operational review: today's focus, risk, next action.
- "разбери неделю" -> cadence review: weekly verdict, deviations, bottleneck.
- "проверь прогресс" -> milestone/phase review: whether moving toward phase exit.
- "где bottleneck?" -> bottleneck review: main limiting factor and domain demand.
- "добавить новый процесс?" -> governance/capability review: whether new domain/procedure is justified and what boundary changes it needs.

## §DOMAIN_DEMAND_CONTRACTS

Generic contract fields required for every domain:
- responsibility
- root-goal contribution
- summary/report format
- exposed metrics/signals
- accepted non-mutating request types from HQ
- what HQ must not request
- approval-required changes
- safety/recovery flags
- freshness / fixture / pending status

Domain contracts:

| domain | responsibility | root-goal contribution | summary/report for HQ | exposed metrics/signals | accepted HQ requests | HQ must not request | approval-required changes | safety/recovery flags |
|---|---|---|---|---|---|---|---|---|
| Nutrition | Nutrition strategy, adherence support, recipe/process support. | Sustainable deficit, satiety, recovery support, maintenance nutrition. | Period, adherence verdict, blockers, phase-fit, 1–3 proposal options. | weight-support status, adherence status, meal-structure fit, lapse pattern. | Review deficit sustainability; explain stall; prepare revised options; request recipe/process support. | Silent plan rewrite; raw diary in Direction OS; unsafe deficit. | Material strategy change; aggressive deficit escalation; canon process change. | excessive hunger, dizziness, persistent energy crash, rapid unexplained loss, inability to sustain. |
| Training/activity | Strength work, activity, conditioning, progression. | Strength retention/gain, energy expenditure, functional capacity, maintenance activity floor. | Planned vs completed, recovery impact, bottlenecks, proposal options. | session completion, activity minutes/frequency, key movement status, soreness/pain interference. | Review plan-fit; propose simpler/harder variants; adjust volume/frequency options; define baseline tests. | Silent edits; unsafe escalation despite red flags; medical restrictions. | Baseline movement canon; material progression standard; new compulsory process. | pain escalation, dizziness, extreme shortness of breath, severe functional drop. |
| Sleep/recovery | Sleep, fatigue, pain, day-function signals. | Constraint management, sustainability, capacity to continue deficit/load. | Green/yellow/red state, top signals, interference level, review recommendation. | sleep duration/regularity status, daytime sleepiness, fatigue, pain interference. | Review compatibility of current load/deficit; propose recovery options; classify escalation risk. | Medical diagnosis; “clearance” of red symptoms; hidden sleep protocol. | Promoting sleep/recovery into a full domain; recovery gating changes. | persistent poor sleep, daytime dysfunction, rising pain, signs incompatible with escalation. |
| Future domain | Declared specialized function. | Only after explicit root-goal contribution. | Same summary contract. | Declared signals only. | Declared non-mutating requests only. | Hidden powers or undeclared capability. | Any new domain class. | Safety fields required before inclusion. |

## §DECISION_CLASSES

| class | HQ may do | example | owner/governance requirement |
|---|---|---|---|
| advisory | Explain, classify, recommend, request review, compare options, state insufficiency. | “Nutrition adherence is the likely bottleneck; request nutrition review.” | No owner approval unless it implies material change. |
| approval-required | Prepare options for material strategy, phase, boundary, domain, or canonical metric/source changes. | “Move from first milestone phase to target/recomposition phase.” | Owner/governance approval required before mutation. |
| blocked | Refuse or route away unsafe/out-of-scope action. | “Ignore pain and increase load”; “copy raw logs into Direction OS”; “build polling/API dashboard now.” | No implementation; route to safety/domain review or owner decision. |

Default owner-signoff recommendations embedded in this WHAT:
- Tempo default: moderate sustainable cut, not aggressive deficit and not strength-first slow cut by default.
- Approval default: all material strategy changes and all boundary changes require owner/governance approval.
- Review cadence default: support ad hoc owner-triggered reviews plus weekly deep review during active phase; no automatic background polling.
- Recovery domain default: sleep/recovery is represented as a demand area now; it becomes a full domain only if recurring yellow/red signals make it decision-relevant.
- Strength markers: HQ must not invent final markers; it can request training domain to prepare 3–5 reproducible owner-reviewable options.
- Athletic look: HQ must not reduce this to a medical metric; it must keep owner-visible criterion as owner decision.
- Maintenance corridor: 90–95 kg remains charter target; any practical corridor rule must be owner-approved before maintenance success is declared.
- Canonical summary sources: v0 must define a summary-source contract and mark fixture/live/freshness/confidence; executor must not silently decide that raw logs or one domain own all truth.

## §SAFETY_BOUNDARIES

Safety in HQ is not medical diagnosis or treatment. It is an escalation and routing gate.

| situation | HQ may do | escalation rule | required routing | never do |
|---|---|---|---|---|
| rising pain or degraded function | Flag yellow/red; mark unsafe-to-escalate. | Hold escalation at red; hold at persistent yellow until review. | training/activity + sleep/recovery review; owner concern if repeated or impairing. | Diagnose cause or prescribe treatment. |
| dizziness, extreme shortness of breath, or “not normal” during activity | Treat as red flag. | Immediate hold. | training/activity review and owner-facing concern. | Say “this is normal, continue.” |
| chest pain/pressure or concerning combinations | Only flag danger and stop escalation. | Immediate hold. | owner-facing concern about urgent/professional medical evaluation. | Interpret as benign or reassure without basis. |
| chronic poor sleep/day dysfunction | Mark recovery-limiter. | Hold load/deficit escalation until clarified. | sleep/recovery review; owner concern if recurring or impairing. | Treat sleep disorder. |
| too-fast or unexplained weight loss | Flag uncertainty/safety concern. | Hold escalation until nutrition/safety review. | nutrition review; owner concern if symptomatic/uncontrolled. | Declare automatic success. |

## §OWNER_DECISION_BLOCK

Immediate owner decision required:
- d-health-hq-what-signoff-001

Plain question:
Should the owner sign this Health HQ WHAT/route as the basis for converge-arch, or send it back / kill the bet?

Options:
- A: Sign this WHAT/route. Health HQ remains goal-achievement orchestration; next is converge-arch; no executor implementation yet.
- B: Request amendments before signoff. Keep t-2 active but return to converge with owner-specified correction.
- C: Kill/park Health HQ and return direction focus to narrower nutrition/training/body-execution work.

Recommendation:
- A, because the research returned sufficient evidence to define the product essence and boundaries, and the WHAT preserves owner route A while preventing implementation from the rejected summary-only proof.

Bad because:
- A: delays implementation behind arch/verify and signs a strong product canon.
- B: consumes appetite and leaves Health HQ active without a closed route.
- C: leaves cross-domain root-goal achievement unmanaged, though it is safer than accepting a status-dispatcher HQ.

## §COVERAGE

done_when coverage:
  - Health HQ as orchestrator of reaching root health goal -> W1, W2
  - milestones/phases and target/current metrics -> W2, W3, W4, §PHASE_MODEL, §METRIC_HIERARCHY
  - strategic review loop and owner conversation surface -> W5, W6, §STRATEGIC_REVIEW_LOOP
  - domain demand contracts for nutrition/training/sleep/future -> W8, W9, W10, W11, W12, §DOMAIN_DEMAND_CONTRACTS
  - decision classes and authority split -> W13, W14, W15, §DECISION_CLASSES
  - safety boundaries -> W16, §SAFETY_BOUNDARIES
  - research input before implementation -> W19
  - old proof as technical evidence only -> W17
  - no dashboard/API/polling/integration creep -> W21
  - no executor implementation from converge -> §ROUTE

mechanism parameter coverage:
  - summary-only proof -> W17
  - owner-triggered review -> W5, W6, §STRATEGIC_REVIEW_LOOP
  - demand routing -> W8-W14, §DOMAIN_DEMAND_CONTRACTS
  - metric model -> W3, W4, §METRIC_HIERARCHY
  - phase model -> W2, §PHASE_MODEL
  - bottleneck classification -> W7
  - decision classes -> W15, §DECISION_CLASSES
  - safety/recovery escalation -> W16, §SAFETY_BOUNDARIES
  - boundary against silent edits/raw data/medical/dashboard/API/polling -> W13-W16, W21
  - implementation evidence requirements -> W20

converge_coverage:
  every criterion + edge + mechanism parameter is covered by §WHAT rows or tables above; owner signoff remains the only gate before converge-arch.

canon_proposed:
  - G1 Health HQ
  - G3 milestone / phase
  - G4 decision-grade metric hierarchy
  - G6 strategic review loop
  - G8 domain demand contract
  - G11 decision class
  - G12 safety/recovery boundary

## §SIGNOFF

Route:
  status: signed
  evidence: >
    owner approved route A @ 2026-07-02 — "A"

Define:
  status: awaiting_owner_signoff
  decision: d-health-hq-what-signoff-001
  reason: >
    Glossary G1-G13 is now research-integrated and owner-reviewable. No owner signoff is claimed in this session.

Resolve:
  status: awaiting_owner_signoff
  decision: d-health-hq-what-signoff-001
  reason: >
    WHAT W1-W21 is now research-integrated and mechanically covered. Owner-owned product meaning and authority defaults must be signed before converge-arch.

## §ROUTE

current:
  awaiting_decision: d-health-hq-what-signoff-001

if_owner_chooses_A:
  next: converge-arch
  reason: >
    Node is heavy/model-bearing. Architecture must compress this WHAT into implementation-neutral architecture/check requirements before converge-verify and any executor task.

if_owner_chooses_B:
  next: converge
  reason: >
    Owner amendments must be integrated into glossary/WHAT before arch.

if_owner_chooses_C:
  next: review_or_shape_body_execution_route
  reason: >
    Current Health HQ bet should be killed/parked and direction should return to narrower nutrition/training/body-execution work.

executor_authorization:
  status: not_authorized
  reason: >
    Converge never emits executor CALL. Owner signoff, converge-arch, and converge-verify must happen first.

END_OF_FILE: live/health/work/converge-g-health-hq-goal-coordinator.md