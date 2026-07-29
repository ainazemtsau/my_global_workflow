# converge-arch — g-health-hq-goal-coordinator

status: architecture_check_route
source:
  signed_what: live/health/work/converge-g-health-hq-goal-coordinator.md
  research_input: live/health/work/health-hq-goal-achievement-model-research-2026-07-03.md
  owner_signoff: live/health/history/2026-07-04-s-health-hq-what-signoff-001.md
constraints:
  - implementation_neutral
  - no Health AI implementation
  - no dashboard/API/polling/integration design
  - no raw body/nutrition/training data in Direction OS
  - no medical diagnosis or treatment plan
  - raw research is not executor input
  - domains execute and mutate through their own procedures; HQ routes non-mutating demands

## §CONTRACTS — Declare

declare_signoff:
  status: signed
  evidence: >
    Owner signed the research-integrated Health HQ WHAT/route on 2026-07-04 with
    "A — подписываю". The contracts below are a direct compression of signed W8-W16,
    W20-W21 and do not introduce a new fork.

contract_rule: >
  Contracts state behavioral content, direction, and trigger. They do not specify
  transport, storage, interface mechanics, timing machinery, or implementation structure.
  Any such mechanics remain outside this architecture/check route.

tree_coverage:
  - g-health-root: covered by C-ROOT-OS.
  - g-health-starter-kit: no direct current contract; historical seed only, consumed by nutrition/training domains if relevant.
  - g-health-ai-core: no contract; dropped and superseded by g-health-core.
  - g-health-core: covered by C-CORE.
  - g-health-nutrition-system: covered by C-NUTRITION.
  - g-health-first-nutrition-cycle: no live contract; dropped.
  - g-health-training-activity-system: covered by C-TRAINING-ACTIVITY.
  - g-health-hq-goal-coordinator: this node.
  - sleep/recovery future domain: covered as pending dependency by C-SLEEP-RECOVERY-PENDING.
  - future domains: covered as declared-only dependency by C-FUTURE-DOMAIN.

contracts:
  - id: C-ROOT-OS
    consumer: health root / Direction OS management layer
    producer: Health HQ
    direction: Health HQ -> health root / Direction OS
    trigger: owner-triggered HQ review closes, material decision is needed, a problem is found, or a next CALL is required
    flow: progress verdict, bottleneck, decision need, routed domain requests, problem summary, next CALL
    boundary: no raw body/nutrition/training data; no medical diagnosis or treatment

  - id: C-CORE
    consumer: Health HQ
    producer: g-health-core
    direction: g-health-core -> Health HQ
    trigger: HQ review needs current governance/domain/summary-source state
    flow: active domain availability, summary-source status, governance state, owner-approval state, review/decision log context
    reverse_flow: Health HQ -> g-health-core receives only HQ-owned review summaries and non-mutating demand records
    boundary: HQ does not rewrite core lifecycle/governance artifacts silently

  - id: C-NUTRITION
    consumer: Health HQ and g-health-nutrition-system
    producer: g-health-nutrition-system and Health HQ
    direction: nutrition summary -> HQ; HQ demand -> nutrition
    trigger: HQ review needs nutrition contribution to phase verdict or identifies nutrition as candidate bottleneck
    flow_to_hq: period, adherence verdict, blockers, phase-fit, weight-support status, meal-structure fit, lapse pattern, proposal options when requested
    flow_to_domain: review deficit sustainability, explain stall, prepare revised options, request recipe/process support, compare risk of options
    boundary: HQ must not silently rewrite menus, recipes, nutrition logs, canonical nutrition processes, or request unsafe deficit escalation

  - id: C-TRAINING-ACTIVITY
    consumer: Health HQ and g-health-training-activity-system
    producer: g-health-training-activity-system and Health HQ
    direction: training/activity summary -> HQ; HQ demand -> training/activity
    trigger: HQ review needs strength/activity/recovery contribution to phase verdict or identifies training/activity as candidate bottleneck
    flow_to_hq: planned-vs-completed state, recovery impact, activity/conditioning contribution, key movement status, soreness/pain interference, proposal options when requested
    flow_to_domain: review plan-fit, prepare simpler/harder variants, define baseline-marker options, compare load/recovery compatibility
    boundary: HQ must not silently edit programs, sessions, weeks, progression standards, movement canon, or force escalation despite red flags

  - id: C-SLEEP-RECOVERY-PENDING
    consumer: Health HQ
    producer: future sleep/recovery domain or pending summary source
    direction: sleep/recovery signals -> HQ; HQ demand -> future sleep/recovery producer when it exists
    trigger: HQ review needs recovery constraint state, or safety/recovery signals become decision-relevant
    flow_to_hq: green/yellow/red recovery state, top signals, pain/energy/day-function interference, review recommendation if available
    flow_to_domain: review compatibility of current deficit/load, classify escalation risk, prepare owner-reviewable recovery options
    boundary: no diagnosis, no treatment, no hidden sleep protocol; live capability cannot be claimed until producer exists and is converged
    build_order_dependency: >
      No sleep/recovery TREE node exists now. v0 may mark sleep/recovery as pending or use clearly marked fixtures only.
      Any claim of live sleep/recovery domain output requires a future shaped/converged producer first.

  - id: C-FUTURE-DOMAIN
    consumer: Health HQ and future declared domain
    producer: future declared domain and Health HQ
    direction: declared domain summary -> HQ; HQ demand -> declared domain
    trigger: owner/governance approves adding a future domain with explicit root-goal contribution
    flow: same minimum demand contract content as current domains, limited to declared responsibility and declared signals
    boundary: HQ must not invent hidden powers for undeclared domains
    build_order_dependency: >
      Future domain capability is absent until a TREE/domain route creates and converges the producer.

  - id: C-SUMMARY-SOURCE
    consumer: Health HQ
    producer: g-health-core and domain summary producers
    direction: summary-source status -> Health HQ
    trigger: any HQ review that uses a metric, signal, or domain report
    flow: source name, live/fixture/pending status, freshness, confidence, reason if pending, decision impact
    boundary: no invented numbers; no raw logs in Direction OS; one domain cannot silently become canonical source for all truth

contract_closure:
  no_dangling_consumed_contracts: PASS
  explanation: >
    Current producers are named where they exist. Sleep/recovery and future domains are explicit pending
    dependencies; v0 may not claim live producer output from them until producer nodes exist and pass their own route.
  no_open_what_terms: PASS
  source_terms: signed G1-G13 and W1-W21
  contract_coverage: PASS

## §DECOMPOSITION — heavy

subsystems:
  - id: S1-GOAL-PHASE-MILESTONE
    role: holds root-goal view, current phase, milestones, entry/exit conditions, phase-specific domain demands
    subnode_decision: internal seam, not a new TREE child now

  - id: S2-METRIC-SUMMARY-SOURCE
    role: separates current-phase minimum metrics, later metrics, and pending/non-mandatory metrics; tracks source/freshness/confidence/decision impact
    subnode_decision: internal seam, not a new TREE child now

  - id: S3-STRATEGIC-REVIEW-LOOP
    role: turns owner intent into progress verdict, bottleneck, strategy implication, domain demands, owner decision need, needed metrics, and next action
    subnode_decision: internal seam, not a new TREE child now

  - id: S4-BOTTLENECK-TAXONOMY
    role: classifies main constraint as adherence, plan mismatch, recovery/capacity, measurement gap, safety uncertainty, or governance gap, with confidence
    subnode_decision: internal seam, not a new TREE child now

  - id: S5-DOMAIN-DEMAND-ROUTER
    role: emits non-mutating demand objects toward nutrition, training/activity, sleep/recovery, and future domains
    subnode_decision: internal seam, not a new TREE child now

  - id: S6-DECISION-AUTHORITY-GATE
    role: classifies outputs as advisory, approval-required, or blocked; prevents silent material changes
    subnode_decision: internal seam, not a new TREE child now

  - id: S7-SAFETY-RECOVERY-GATE
    role: flags unsafe-to-escalate, holds deficit/load escalation, routes review, and raises owner-facing concern without diagnosis/treatment
    subnode_decision: internal seam, not a new TREE child now

  - id: S8-X-HEALTH-HQ-SUMMARY-SLICE
    role: old summary-only proof used for summary loading, fixtures/adapters, boundary flags, and non-mutating routed-request mechanics only
    subnode_decision: subcomponent only; not product definition

subnodes_created: []
future_split_candidates:
  - sleep/recovery full domain, only if recurring yellow/red signals make it decision-relevant and owner/governance approve shaping it
  - strength baseline marker canon, only through training/activity owner-reviewable options
  - future specialized domains, only through normal TREE/domain route

## §PHASE_MILESTONE_OBJECTS

required_object_content:
  - phase id and name
  - purpose
  - entry condition
  - exit condition
  - target metrics
  - current metric links by summary source
  - dominant bottleneck classes
  - phase-specific domain demands
  - safety/recovery gates
  - owner decision requirements

required_initial_phases:
  - P1 preparation/control capture
  - P2 first clinical milestone: 5-10% from 125 kg, i.e. 118.75-112.5 kg
  - P3 scale toward target corridor
  - P4 target range/recomposition
  - P5 maintenance for 12 months

verification_question: >
  Can Health HQ produce a phase-aware verdict that explains target vs current state and the next phase-relevant domain demand,
  rather than only displaying status?

## §METRIC_HIERARCHY_AND_SOURCE_CONTRACT

required_metric_groups:
  current_phase_minimum:
    - weight trend
    - distance to first 5-10% milestone
    - nutrition adherence/support
    - strength adherence
    - activity/conditioning volume
    - sleep/recovery
    - energy/pain/day function
    - review age
  later_only_when_decision_relevant:
    - strength baseline markers
    - waist or waist-to-height ratio
    - body-composition estimate
    - maintenance activity volume
    - target-corridor duration
  non_mandatory_v0:
    - exact daily calories in Direction OS
    - high-detail macro tables
    - wearable readiness signals
    - consumer-device body-fat estimates
    - VO2max estimates
    - detailed micronutrient analytics

summary_source_contract:
  every_metric_or_signal_must_state:
    - summary source
    - live/fixture/pending status
    - freshness
    - confidence
    - reason if pending
    - decision impact
  blocked:
    - invented numbers
    - raw logs in Direction OS
    - treating one domain as all-purpose truth owner without approval

verification_question: >
  Does every verdict-driving metric show source/freshness/confidence and decision impact, or is HQ drifting into decorative telemetry?

## §STRATEGIC_REVIEW_LOOP_OBJECT

owner_triggered_review_steps:
  - classify owner intent: today / week review / progress / bottleneck / add process
  - load only needed summaries and HQ decisions
  - check reviewability: source status, freshness, confidence, domain availability
  - compare phase target to current summary metrics
  - classify bottleneck and confidence
  - state strategy implication
  - produce non-mutating domain demands
  - request owner decision if material change is required
  - write short review/decision summary without raw data
  - state next owner-facing action

required_review_output:
  - progress verdict: on-track / at-risk / stalled / blocked / unsafe-to-escalate
  - main bottleneck: class + reason
  - confidence: high / medium / low
  - strategy implication
  - domain requests
  - owner decision required: yes/no
  - metrics needed now
  - metrics later
  - next owner-facing action

verification_question: >
  Does the review end in verdict + bottleneck + implication + demand + decision need + next action,
  or is it merely commentary?

## §BOTTLENECK_TAXONOMY

required_classes:
  - adherence: intended nutrition/training/activity execution is not sufficiently happening or not sustainable
  - plan mismatch: plan does not fit phase, owner constraints, or root-goal contribution
  - recovery_capacity: sleep, fatigue, pain, energy, or day function limits escalation or continuation
  - measurement_gap: source is missing, stale, fixture-only, low confidence, or not decision-grade
  - safety_uncertainty: symptoms, pain, too-fast/unexplained loss, or other red/yellow signals block escalation
  - governance_gap: material strategy, phase, domain, source, or boundary change requires owner/governance approval

required_properties:
  - confidence
  - reason
  - what would change classification
  - domain demand if actionable
  - owner decision if material

verification_question: >
  Can HQ name the main bottleneck and what would change the classification, instead of issuing a vague motivation label?

## §DOMAIN_DEMAND_OBJECTS

generic_demand_object_content:
  - target domain
  - responsibility being invoked
  - root-goal contribution
  - phase/milestone reason
  - requested non-mutating review/proposal/comparison
  - expected summary return content
  - exposed signals used
  - must-not-request boundary
  - owner/governance approval requirement
  - safety/recovery flags
  - live/fixture/pending status

allowed_demand_classes:
  - review phase-fit
  - prepare two or three owner-reviewable options
  - compare risks
  - check recovery compatibility
  - explain stall
  - prepare proposal through domain procedure
  - define candidate baseline markers for owner review

blocked_demand_classes:
  - silent domain artifact rewrite
  - raw diary export to Direction OS
  - unsafe deficit/load escalation
  - phase change without owner approval
  - medical diagnosis or treatment
  - hidden capability for undeclared domain

verification_question: >
  Are HQ outputs non-mutating demand objects, and do domains retain execution and mutation authority?

## §DECISION_AUTHORITY_GATE

decision_classes:
  advisory:
    HQ_may: explain, classify, recommend, request review, compare options, state insufficiency
    owner_requirement: no owner approval unless material change is implied
  approval_required:
    HQ_may: prepare options for material strategy, phase, boundary, domain, or canonical source change
    owner_requirement: owner/governance approval before mutation
  blocked:
    HQ_may: refuse or route away unsafe/out-of-scope action
    owner_requirement: no implementation; route to safety/domain review or owner decision

approval_required_by_default:
  - material strategy changes
  - phase changes
  - boundary changes
  - new domain classes
  - canonical metric/source changes
  - promotion of sleep/recovery into a full domain
  - maintenance corridor rule
  - final strength baseline markers
  - final athletic-look criterion

verification_question: >
  Does HQ clearly separate advisory output from approval-required and blocked output?

## §SAFETY_RECOVERY_BOUNDARY

rule: >
  Safety in HQ is a non-medical escalation and routing gate. HQ can hold escalation,
  flag risk, route review, and raise owner-facing concern. HQ cannot diagnose, treat,
  reassure away red flags, or frame rapid unexplained loss/symptoms as automatic success.

situations:
  - rising pain or degraded function: flag yellow/red, hold escalation when red or persistent yellow, route training/activity and sleep/recovery review
  - dizziness, extreme shortness of breath, or not-normal feeling during activity: treat as red flag, hold escalation, route review and owner-facing concern
  - chest pain/pressure or concerning combinations: flag danger, stop escalation, raise concern about urgent/professional evaluation
  - chronic poor sleep or day dysfunction: mark recovery-limiter, hold load/deficit escalation until clarified
  - too-fast or unexplained weight loss: flag uncertainty/safety concern, hold escalation until nutrition/safety review

verification_question: >
  Does HQ stop escalation and route review without acting as a medical advisor?

## §OLD_PROOF_SUBCOMPONENT

retained_from_x_health_hq:
  - summary loading
  - fixtures/adapters
  - boundary flags
  - non-mutating routed-request mechanics

not_proven_by_old_slice:
  - Health HQ product essence
  - phase/milestone model
  - metric hierarchy
  - bottleneck taxonomy
  - decision classes
  - domain demand contract authority
  - safety/recovery gate as strategic boundary

rule: >
  Later implementation evidence may use the old proof only under the full orchestration spine.
  It must not relabel the summary-only proof as Health HQ v0 acceptance.

verification_question: >
  Is x_health_hq a subordinate mechanism under the orchestration model, not the model itself?

## §ARCHITECTURE_PICKS — Architect

architect_signoff:
  status: signed
  evidence: >
    Owner signed the research-integrated WHAT/route on 2026-07-04 with "A — подписываю".
    High-risk picks below are derived from signed W1-W21 and the accepted research input.
    No new owner fork is introduced.

Q1_product_spine:
  question: What is Health HQ's product spine?
  options:
    - status_reviewer: rejected because it reports what is visible but does not orchestrate root-goal achievement.
    - dashboard_or_integration_hub: rejected because it turns v0 into visibility/infrastructure work.
    - autonomous_god_agent: rejected because it violates domain authority and safety/governance boundaries.
    - goal_achievement_orchestration_layer: selected.
  pick: owner-triggered goal-achievement orchestration layer
  signed_source: W1, W5, W8-W16, owner "A — подписываю"

Q2_phase_milestone_model:
  question: How should HQ represent long-horizon progress?
  options:
    - status_only: rejected because it cannot decide phase fit or milestone movement.
    - fixed_calendar_plan: rejected because it ignores summary confidence, recovery, and owner decisions.
    - phase_milestone_objects: selected.
  pick: explicit phase/milestone objects with entry/exit conditions, target/current comparison, and phase-specific domain demands
  signed_source: W2-W4, §PHASE_MODEL, owner "A — подписываю"

Q3_metric_source_model:
  question: How should HQ use metrics without becoming a raw-data dashboard?
  options:
    - raw_logs_in_HQ_or_Direction_OS: rejected by raw-data boundary.
    - broad_metric_zoo: rejected because non-decision telemetry creates noise and scope creep.
    - decision_grade_summary_sources: selected.
  pick: now/later/pending metric hierarchy with source/freshness/confidence and decision impact
  signed_source: W3-W4, §METRIC_HIERARCHY, owner "A — подписываю"

Q4_domain_authority:
  question: How should HQ coordinate nutrition/training/recovery/future domains?
  options:
    - direct_domain_mutation: rejected because domains own execution and mutation.
    - ad_hoc_messages: rejected because authority and evidence become unverifiable.
    - non_mutating_demand_contracts: selected.
  pick: structured domain demand contracts with explicit must-not-request and approval-required boundaries
  signed_source: W8-W14, §DOMAIN_DEMAND_CONTRACTS, owner "A — подписываю"

Q5_review_decision_loop:
  question: What loop turns owner intent into course correction?
  options:
    - automatic_background_checking: rejected by owner-triggered boundary and v0 scope.
    - generic_coaching_response: rejected because it lacks verdict, bottleneck, demand, and decision gate.
    - owner_triggered_strategic_review_loop: selected.
  pick: owner-triggered review loop with verdict, bottleneck, implication, domain demands, decision need, and next action
  signed_source: W5-W6, §STRATEGIC_REVIEW_LOOP, owner "A — подписываю"

Q6_safety_recovery:
  question: How should safety/recovery constrain HQ?
  options:
    - medical_advisor: rejected because HQ must not diagnose or treat.
    - ignore_as_domain_detail: rejected because recovery can block escalation and strategy.
    - non_medical_escalation_gate: selected.
  pick: safety/recovery gate that can hold escalation, route review, and raise owner-facing concern
  signed_source: W16, §SAFETY_BOUNDARIES, owner "A — подписываю"

Q7_old_proof_treatment:
  question: What role should the old summary-only x_health_hq proof play?
  options:
    - accept_as_product: rejected by owner route and research.
    - discard_completely: rejected because useful summary/request mechanisms exist.
    - subcomponent_only: selected.
  pick: retain as subcomponent only under the full orchestration spine
  signed_source: W17, W20, owner "A — подписываю"

miner_gap_hunt:
  question: Which architecture question was not asked?
  found_gap: >
    Summary-source authority and unbuilt sleep/recovery/future producer dependencies could be silently assumed.
  closure: >
    C-SUMMARY-SOURCE requires source/freshness/confidence/live-fixture-pending status for every metric/signal.
    C-SLEEP-RECOVERY-PENDING and C-FUTURE-DOMAIN block live capability claims until producer domains exist and pass their own route.
  arch_open_after_gap_hunt: 0

## §LATER_EXECUTOR_EVIDENCE

later_executor_must_return:
  - owner-triggered review examples for main intent classes: "что сегодня?", "разбери неделю", "проверь прогресс", "где bottleneck?", "добавить новый процесс?"
  - phase-aware progress verdict using phase/milestone objects
  - metric hierarchy with now/later/pending split and summary-source status
  - bottleneck classification with confidence and strategy implication
  - non-mutating demand objects for nutrition, training/activity, sleep/recovery, and future-domain handling
  - owner approval gate demonstration for material change
  - review/decision log demonstration without raw data in Direction OS
  - demonstration that x_health_hq summary-only proof is subcomponent only
  - safety/recovery boundary demonstration: unsafe-to-escalate without diagnosis/treatment
  - check output or equivalent implementation evidence from the product repo

later_executor_must_not_return_as_sufficient:
  - dashboard screen
  - API/integration/polling work
  - raw diary copied into Direction OS
  - autonomous silent domain edits
  - medical diagnosis or treatment plan
  - summary-only reviewer relabeled as product acceptance

executor_context_rule: >
  If converge-verify passes and an executor CALL is later emitted, the executor context should cite the signed WHAT
  and this architecture/check artifact as input evidence. Raw research must not be sent as direct executor instructions.

## §CONVERGE_VERIFY_CHECKLIST

checks:
  - id: CV1
    check: Positive essence
    pass_condition: HQ is goal-achievement orchestration, not status reviewer/dashboard/god-agent/medical advisor/integration hub.
  - id: CV2
    check: Contract coverage
    pass_condition: Every TREE interaction listed in tree_coverage maps to a contract or explicit no-current-contract reason.
  - id: CV3
    check: No dangling producers
    pass_condition: Sleep/recovery and future domains are marked pending dependency; no live capability is claimed.
  - id: CV4
    check: Phase/milestone object
    pass_condition: Phase object content can produce target/current comparison and phase-specific demands.
  - id: CV5
    check: Metric hierarchy/source
    pass_condition: Every decision-driving metric has source/freshness/confidence/status and decision impact.
  - id: CV6
    check: Strategic review loop
    pass_condition: Review produces verdict, bottleneck, implication, demands, decision need, needed metrics, next action.
  - id: CV7
    check: Bottleneck taxonomy
    pass_condition: At least the six signed classes exist and include confidence + what would change classification.
  - id: CV8
    check: Domain authority
    pass_condition: HQ routes non-mutating demands; domains execute and mutate through own procedures.
  - id: CV9
    check: Decision classes
    pass_condition: advisory / approval-required / blocked are explicit and material changes require owner/governance approval.
  - id: CV10
    check: Safety/recovery boundary
    pass_condition: HQ can hold escalation and route review without diagnosis/treatment.
  - id: CV11
    check: Old proof treatment
    pass_condition: x_health_hq is subcomponent only, not product acceptance.
  - id: CV12
    check: Executor firewall
    pass_condition: No executor implementation is authorized by this architecture artifact; next is converge-verify.

close_status:
  contract_coverage: PASS
  arch_open: 0
  arch_in_context_only: PASS
  executor_authorization: not_authorized

## §SIGNOFF

Declare:
  status: signed
  evidence: >
    Owner signed the research-integrated WHAT/route @ 2026-07-04 with "A — подписываю".
    The §CONTRACTS section compresses W8-W16/W20-W21 and introduces no new owner fork.

Architect:
  status: signed
  evidence: >
    Owner signed the research-integrated WHAT/route @ 2026-07-04 with "A — подписываю".
    High-risk architecture picks are derived from signed W1-W21 plus accepted research; arch_open is 0.

## §ROUTE

current:
  next: converge-verify

executor_authorization:
  status: not_authorized
  reason: >
    Owner signoff authorized converge-arch. This session authorizes only converge-verify next.
    Executor implementation remains blocked until converge-verify passes and emits a separate route.

END_OF_FILE: live/health/work/converge-g-health-hq-goal-coordinator-arch.md
