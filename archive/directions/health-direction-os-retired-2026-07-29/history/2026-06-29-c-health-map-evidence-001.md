RESULT c-health-map-evidence-001 (call: c-health-map-evidence-001)
direction: health   play: research   node/task: g-health-root
outcome: |
  Fresh map_evidence exists for parent c-health-owner-wants-planning-001.

  Bottom line:
  - Candidate 1, cross-domain Health AI aggregation/review/customization, is the only candidate that may deserve a new TREE child, but only if narrowed to a thin review/reconciler layer over summaries. It should not become a second kernel, cockpit, or routine tracker.
  - Candidate 2, gameful activity/training, belongs under g-health-training-activity-system as a motivation/adherence layer after the training/activity safety/research boundary is cleared.
  - Candidate 3, separate cooking domain, should stay parked as a nutrition child/capsule unless cooking complexity becomes a distinct bottleneck not covered by the existing nutrition domain.
  - Candidate 4, automation/integrations, should be explicitly deferred into an integration lane until manual data contracts and domain value are stable.

evidence: |
  State evidence:
  - NOW.md: active_bet is none; no tasks are active; Direction OS must not track Health AI projects/processes or raw body/nutrition/training data by default.
  - NOW.md open_call c-health-map-evidence-001: owner candidates are cross-domain Health AI review/aggregation, gameful activity/training, separate cooking domain, and automation/integrations.
  - health-direction-os-tracking-boundary.md: accepted owner decision is "мы не трэкаем проекты если только я прямо не попрошу"; Health AI may run internally; Direction OS handles process development, architecture/state repair, major decisions, bounded routing, and summary-level state only when explicitly requested.
  - TREE.md: g-health-core is done and already owns common metrics, phase, PLAN vs LOG separation, review mechanism, and module data exchange.
  - TREE.md: g-health-nutrition-system is parked with partial current progress and already includes menus, recipes, grocery/meal-prep, fallback food, nutrition reviews, and extension points.
  - TREE.md: g-health-training-activity-system is done as product/process work but current authority says PROGRAM awaiting Deep Research; it already names VR, bicycle, Strava-like/self-hosted mechanics, Hevy-like strength interfaces, and raw-data boundary.

  External evidence used:
  - CDC Adult Activity overview, Dec. 20 2023: adults need at least 150 minutes moderate activity weekly and 2 days muscle-strengthening weekly.
    URL: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
  - NIDDK Choosing a Safe & Successful Weight-loss Program: initial 5–10% weight-loss goal within 6 months; programs should include realistic goals, healthy eating, physical activity, habit support, monitoring, feedback, social support, and maintenance planning.
    URL: https://www.niddk.nih.gov/health-information/weight-management/choosing-a-safe-successful-weight-loss-program
  - WHO Physical activity fact sheet: about 31% of adults globally, 1.8B people, did not meet 150 minutes/week; projected 35% by 2030 if trend continues.
    URL: https://www.who.int/news-room/fact-sheets/detail/physical-activity
  - WHO 2025 guidance on large multi-modal models for health: LMMs have potential in health care/research/public health, but broad general-purpose ability is not yet proven; governance is required.
    URL: https://www.who.int/publications/i/item/9789240084759
  - Digital Weight Management Interventions, 2026 preprint: commercial DWMIs commonly include self-monitoring/goal-setting/BCTs, but lack social support, VR applications, and adaptive personalization.
    URL: https://arxiv.org/abs/2604.06181
  - PEARL RL physical-activity nudge RCT, 2025 preprint: RL-personalized Fitbit nudges increased steps vs control at 1 and 2 months; effect size was useful but modest.
    URL: https://arxiv.org/abs/2508.10060
  - Health Wearables, Gamification, and Healthful Activity, 2023 preprint: leaderboard/gamification effects were heterogeneous; average +370 steps/day, sedentary users benefited more, highly active users could be harmed.
    URL: https://arxiv.org/abs/2301.02767
  - Strava API v3 docs: activities, uploads, streams, webhooks, and authenticated API surfaces exist.
    URL: https://developers.strava.com/docs/reference/
    URL: https://developers.strava.com/docs/webhooks/
  - Strava API policy reporting, Nov. 2024 and Jun. 2026: API data-use restrictions, AI model-training restrictions, user-display limits, and 2026 paid/subscription tightening increase platform dependency risk.
    URL: https://www.theverge.com/2024/11/19/24301056/strava-api-ai-data-sharing-policy-change-fitness-tracking
    URL: https://www.theverge.com/gadgets/940854/strava-restricts-api-access-ai-apps
  - 2025 reporting on minimally processed vs ultra-processed diet RCT: minimally processed meals produced more weight loss than ultra-processed meals under healthy-eating-guideline matched conditions; supports cooking/meal-prep as adherence/nutrition infrastructure, not as a separate top-level domain by itself.
    URL: https://www.theguardian.com/society/2025/aug/04/home-cooking-and-minimally-processed-foods-best-for-weight-loss-upf-study-finds

  Confidence:
  - Established from state: Direction OS boundary, current no-active-bet state, core/nutrition/training TREE overlap, and the exact four owner candidates.
  - Established from external sources: baseline lifestyle-program elements, activity guideline minimums, global inactivity scale, Strava API existence and policy risk, and directionally positive but bounded evidence for gameful/adaptive activity nudges.
  - Inference: candidate routing is a strategic interpretation from state + evidence, not an owner decision.
  - What would change the answer: owner explicitly asks Direction OS to track Health AI projects; returned training/activity Deep Research makes gameful challenge loops urgent; current nutrition/cooking workflow fails in a way not covered by nutrition; Hevy/Strava official API feasibility is proven against the owner’s exact data contract.

candidate_routing_table: |
  1. Cross-domain Health AI aggregation/review/customization service
     - Maps to: sc-health-ai-system, sc-maintenance-system, adherence-relapse, medical-safety, ai-system-data-architecture.
     - Leverage: high if it reconciles nutrition/training/activity summaries, catches contradictions, detects safety/adherence drift, and proposes bounded improvements.
     - Risk/overlap: very high if it duplicates g-health-core, becomes a second runtime, or creates routine tracking/polling. Also risks Health AI procrastination over body-value.
     - Sequence: after domains produce summary-level outputs or after an explicit cross-domain inconsistency appears; do not start from architecture breadth.
     - Verdict: TREE-worthy child only as thin "cross-domain review/reconciler layer"; otherwise parked capture.

  2. Gameful activity/training, Strava-like challenges
     - Maps to: activity-conditioning, adherence-relapse, strength-body-composition, sc-maintenance-system.
     - Leverage: medium-high for motivation/adherence, especially if calibrated to baseline and safety gates.
     - Risk/overlap: competition can increase overload/injury/social-comparison risk; novelty can decay; Strava clone/API work can distract from actual activity.
     - Sequence: after training/activity has approved evidence-backed program boundary; start as low-friction challenge generation from summaries, not raw logs.
     - Verdict: child under g-health-training-activity-system; parked until safe program/research boundary is cleared.

  3. Separate cooking domain
     - Maps to: weight-nutrition, adherence-relapse, sc-weight-maintenance, sc-maintenance-system.
     - Leverage: medium; cooking can improve repeatability, taste, satiety, meal-prep, and lower reliance on ultra-processed/default convenience food.
     - Risk/overlap: duplicates the existing nutrition system, which already owns menu, recipes, grocery, meal-prep and fallback variants; can become recipe research instead of execution.
     - Sequence: keep inside nutrition unless cooking becomes a distinct operational bottleneck: kitchen workflow, inventory, batch-cooking, taste/family constraints, or recipe execution failures.
     - Verdict: parked nutrition child/capsule, not top-level TREE node.

  4. Automation/integrations with apps such as Strava and Hevy
     - Maps to: ai-system-data-architecture, activity-conditioning, strength-body-composition, adherence-relapse.
     - Leverage: medium-high only as friction reduction after a manual workflow is proven.
     - Risk/overlap: platform/API dependency, privacy, data-use restrictions, and yak-shaving. Strava API is real but more constrained; Hevy feasibility was not confirmed from accessible text.
     - Sequence: manual/export/import first; API only after stable source-of-truth contract and explicit owner value.
     - Verdict: integration lane / explicit defer; not TREE-worthy now.

overlaps_conflicts: |
  - Candidate 1 vs g-health-core: core already owns common metrics, phase, review, data exchange and source-of-truth boundaries. A cross-domain service is valid only as evaluator/reconciler, not as another core.
  - Candidate 2 vs g-health-training-activity-system: training node already names VR, bicycle, gameful/competitive loops, Strava-like mechanics and specialized apps. Therefore this is a child/layer, not a new sibling.
  - Candidate 3 vs g-health-nutrition-system: nutrition already owns cooking-adjacent functions. A cooking split is justified only if cooking has its own bottleneck and artifacts.
  - Candidate 4 vs all domains: integrations should serve stable workflows, not create workflows. API work before manual proof increases architecture/procrastination risk.

non_obvious_path: |
  Build the cross-domain idea as a referee, not a cockpit:
  - Trigger only on owner-requested review, milestone review, or contradiction between domain summaries.
  - Consume summary-level outputs only.
  - Produce one of: consistency verdict, safety/adherence warning, proposed bounded change, or CALL back to a domain.
  - First proof: catch one real contradiction or unsafe mismatch and route it cleanly.
  - Gameful challenges, cooking capsules and integrations become optional probes feeding summaries into the referee, not separate systems or routine tracking loops.

recommended_skeleton_input: |
  For the parent map skeleton, do not create four new nodes.

  Recommended skeleton shape:
  - candidate_node:
      id: g-health-cross-domain-review-layer
      parent: g-health-core or g-health-root, to be decided by parent map
      goal: >
        Health AI has a thin cross-domain review/reconciler layer that reads only domain summaries,
        detects contradictions between nutrition/training/activity/maintenance plans, flags safety or
        adherence risks, and proposes bounded improvements without raw-data tracking or routine project polling.
      why: >
        The health direction now has multiple domain wants; the next leverage is coherence and decision routing,
        not another raw tracker or a second core.
      done_when_candidate:
        - Summary-only input contract exists.
        - Review can classify: consistent / conflict / missing info / safety concern / owner decision needed.
        - It proves one realistic cross-domain reconciliation without storing raw daily logs in Direction OS.
        - It cannot customize domain procedures unless the change is routed through existing governance/owner gates.
      cuts:
        - no dashboard
        - no daily polling
        - no raw body/nutrition/training data in Direction OS
        - no Strava/Hevy API implementation
        - no separate cooking domain
        - no gameful challenge engine in this bet

  Parked inputs for later:
  - gameful challenge layer under g-health-training-activity-system after training/activity research/approval.
  - cooking capsule under g-health-nutrition-system if recipe/cooking friction becomes concrete.
  - integration adapter lane after manual workflow and source-of-truth contract are stable.
  - Hevy API feasibility probe only when exact data contract is known.

state_changes: |
  No TREE or NOW content edits proposed by this research child.
  Return result to parent c-health-owner-wants-planning-001.
  Writer/parent may remove open_calls[c-health-map-evidence-001] after ingesting this RESULT.

captures:
  - parked: gameful activity/training challenge layer should be treated as a training/activity child after safety/research boundary clears, not as a standalone Strava clone.
  - parked: cooking should remain a nutrition capsule unless cooking workflow friction becomes a distinct blocker.
  - parked: integrations should start from manual/export/import contracts; Strava/Hevy API work is deferred until workflow proof.
  - risk: cross-domain Health AI review becomes a second kernel/cockpit unless explicitly bounded as summary-only referee.

decisions_needed: []

play_check:
  - 1 recite: done — question, return format, boundaries and one-session budget were restated in the opening contract.
  - 2 investigate: done — read KERNEL, research play, packet schema, CHARTER, TREE, NOW, tracking-boundary knowledge file, and fresh external sources.
  - 3 confidence: done — separated state-established facts, source-backed external facts, inference, and answer-changing conditions.
  - 4 close: done — RESULT returns findings to parent c-health-owner-wants-planning-001 without selecting or activating a bet.

log: "research c-health-map-evidence-001: routed four owner health candidates into cross-domain review child candidate, training gameful child, nutrition cooking capsule, and deferred integration lane."
next: |
  return-to-parent c-health-owner-wants-planning-001

END_OF_FILE: live/health/history/2026-06-29-c-health-map-evidence-001.md
