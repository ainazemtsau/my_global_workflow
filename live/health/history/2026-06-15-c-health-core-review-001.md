outcome:
  status: checkpoint
  review_verdict:
    node: g-health-core
    verdict: partially_met
    close_bet: false
    reason: >
      Product evidence for the core-only slice appears to satisfy the acceptance/contract
      surface with zero product blocker gaps, but binding G5 is not satisfied because the
      required fresh cross-family verification has not happened. Codex/OpenAI t-3 evidence
      and this OpenAI/ChatGPT review are same-family/pre-pass evidence only under NOW.evaluator.
  what_changed: >
    g-health-core has a verified review checkpoint: product acceptance evidence is clean enough
    to send to cross-family G5, but the bet remains active/pending until Claude or another
    non-OpenAI family performs binding refutation.

evidence:
  state_read:
    - live/health/CHARTER.md: readable; END_OF_FILE present.
    - live/health/TREE.md: readable; END_OF_FILE present.
    - live/health/NOW.md: readable; END_OF_FILE present.
    - live/health/work/converge-g-health-core.md: readable; END_OF_FILE present.
    - os/KERNEL.md and os/plays/review.md: readable; END_OF_FILE present.
  reviewed_product_commits:
    - a67a34e109aac5f70284b048af4480be38fb8cd5: "core acceptance harness: map converged spec"
    - ee25a894e22d83485525f7d798f02e0fa9d48189: "core slice: replace v1 structure"
    - 8bc980ad21d3f54cbd27b28dcb363e0198c46751: "core evidence: package t-3 dry-run proof"
  refutation_summary:
    attempted_to_refute:
      - missing copied acceptance rows
      - missing contract rows
      - product blocker gaps
      - P8/existing-v1-input gap severity
      - missing owner confirmation before destructive clear
      - module/runtime scope creep
      - raw daily data leaking into Direction OS
      - Health AI dependency/upward write path to Direction OS/external workflow
      - absence of core-only WA73 fixture
      - check script superficiality or unknown check refs
      - binding cross-family G5 status
    found:
      product_acceptance_rows:
        WA1: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA2: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA3: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA4: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA5: PASS in evidence summary; check scans for forbidden external workflow terms and upward dependency.
        WA6: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA7: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA8: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA9: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA10: PASS in evidence summary; matrix target/check refs present; no blocker gap.
        WA11: PASS in evidence summary; check scans for forbidden external workflow terms and upward dependency.
        WA12: PASS in evidence summary; dummy module attach shared-state scenario covered.
        W69: PASS in evidence summary; minimum tracked-signal principle declared.
        W70: PASS in evidence summary; red-flag halt/non-diagnostic behavior covered.
        W72: PASS in evidence summary; slug immutability covered.
        W73: PASS in evidence summary; core-only program/day fixture covered.
        W74: PASS in evidence summary; no fabricated irreducible owner facts; reduced mode for pending anchors.
      contract_rows:
        CA1: PASS in evidence summary; read-only external visibility/no upward write path.
        CA2: PASS in evidence summary; daily prescription resolve-on-read.
        CA3: PASS in evidence summary; phase/week/day back-reference.
        CA4: PASS in evidence summary; namespaced module writes only.
        CA5: PASS in evidence summary; day_type provenance contract only.
        CA6: PASS in evidence summary; reusable template core-owned.
        CA7: PASS in evidence summary; reusable parse/library/value/procedure surface.
        CA8: PASS in evidence summary; schema_version and forward migration.
        CA9: PASS in evidence summary; convention-carrier determinism checklist.
      check_output:
        check_acceptance_matrix.py: >
          Evidence summary reports PASS; 17 acceptance rows, 9 contract rows, 27 PLAN rows,
          9 architecture inputs, blocker gaps 0.
        check_core_slice.py: >
          Evidence summary reports PASS; 32 core files, schema/frontmatter OK, matrix target files OK,
          WA73 formula OK, PLAN/LOG separation OK, forbidden module/runtime directories absent.
        check_core_evidence.py: >
          Evidence summary reports PASS; 11 dry-run scenarios, 26 acceptance/contract rows pass,
          0 fail, blocker gaps 0.
      gap_classification:
        blocker_gaps: 0 product blocker gaps found in committed evidence.
        non_blocking_gaps:
          - id: P8
            classification: non_blocking
            reason: source PLAN agenda has no P8 row; carried as source numbering gap.
          - id: existing-v1-input
            classification: non_blocking_closed
            reason: closed by t-2 destructive-clear after explicit owner confirmation.
        review_gate_gap:
          id: cross-family-G5
          classification: binding_review_blocker
          reason: >
            NOW.evaluator says Codex validator is only intra-family pre-pass and binding G5
            needs a separate cross-family pass, ideally Claude. This session cannot count as that.
      owner_clearance:
        status: present
        evidence_path: acceptance/core/clearance.md
        owner_quote: "давай стерем старую структуру я подтвержадю это"
      scope_boundary:
        status: product_scope_appears_respected
        notes:
          - t-3 evidence says synthetic/minimal seed data only.
          - t-3 evidence says no nutrition, training/activity, UI, runtime, DB, server, cron, or scheduler.
          - external-read-boundary says external strategic systems may read, Health AI has no dependency or upward write path, and raw operational data remains owned in Health AI.
  limits:
    - >
      I inspected committed files, scripts, diffs, and recorded outputs through the GitHub connector.
      I did not freshly execute the product repo scripts locally in this session.
    - >
      Because this session is OpenAI/ChatGPT, it cannot satisfy the requested cross-family G5 pass
      against Codex/OpenAI t-3.

forecast_check:
  forecast_from_NOW: >
    A hard core-only cut should produce a buildable Health AI foundation without spending the bet
    on module details or product UI.
  against_from_NOW: >
    The strongest case against was that the acceptance/contract matrix was too large for 3 focused
    half-days or provider-independence could not be evidenced without a heavier harness.
  observed: >
    Product evidence supports the forecast on buildability and scope control: the matrix/check/dry-run
    harness reports zero product blocker gaps and no module/runtime scope creep.
  surprise: >
    Pessimistic on product buildability; wrong-timeline on closure. The core-only evidence package
    appears sufficient as a product pre-pass, but the binding cross-family G5 gate was not completed
    in the executor/review routing.

harvest_per_lens:
  weight-nutrition:
    learned: >
      The core can carry weight/trend and minimum tracked-signal mechanics without building menus,
      recipes, grocery lists, or nutrition reviews.
    consequence: >
      g-health-nutrition-system should consume the core and not redefine metrics, PLAN/LOG, phase,
      review, or parsing conventions.
  strength-body-composition:
    learned: >
      The core exposes phase/value grammar and additive module contracts without implementing training
      progression or Hevy/Strava/VR/wearable integrations.
    consequence: >
      Training/activity can be shaped as a module on top of core-owned phase and metrics.
  activity-conditioning:
    learned: >
      Generic phase/LOG/module hooks are enough at core level; concrete activity mechanisms remain
      correctly parked.
    consequence: no TREE change.
  adherence-relapse:
    learned: >
      Non-blocking questions, reduced mode, no re-pester behavior, minimum tracked-signal principle,
      and adherence-over-completeness are now load-bearing core concepts in the evidence package.
    consequence: >
      Future nutrition/training bets should test whether this reduces friction in real owner use.
  medical-safety:
    learned: >
      Red-flag halt and non-diagnostic medical-check language are represented in product evidence;
      no medical prescriptions were added.
    consequence: >
      Future module work must consume the core safety floor rather than create separate safety wording.
  ai-system-data-architecture:
    learned: >
      The provider-independent core can be represented as Markdown/YAML + convention carriers +
      formula/check harness, but provider-independence claims require explicit cross-family verification.
    consequence: >
      Add a durable knowledge rule for future reviews: same-family product checks are not binding G5
      when the bet itself requires cross-family validation.

tree_update:
  proposed_diff: []
  owner_approval_required: false
  rationale: >
    No TREE.md change is proposed in this checkpoint. g-health-core cannot be marked done until
    binding cross-family G5 passes. Existing parked next nodes remain structurally correct.

add_back_check:
  cut_list_checked:
    - nutrition module
    - training/activity module
    - app UI/server/DB/runtime/cron/schedulers
    - full food/exercise library
    - objective recovery metrics
    - automatic cross-provider sync
    - raw daily data in Direction OS
    - product repo wipe authorization from shape
  missed_cut_items: []
  ratio_observation: >
    0/8 cut items turned into required add-backs during this review. For this bet, the cuts were not
    too aggressive; sample is still too small to conclude cuts are generally too timid.

knowledge:
  promote:
    - path: live/health/knowledge/health-core-g5-evidence-rule.md
      content: |
        # health-core-g5-evidence-rule

        accepted: 2026-06-15
        fact: >
          For Health AI provider-independence/core bets, Codex/OpenAI implementation evidence and
          OpenAI-family validation are pre-pass evidence only when the active bet's evaluator requires
          cross-family G5. Closing the bet requires fresh refutation by a different model family
          (Claude preferred for g-health-core).
        read_by:
          - play: review
            when: before marking provider-independent Health AI bets done
          - play: shape
            when: designing evaluator routing for cross-provider/provider-independence claims
        source: c-health-core-review-001

state_changes:
  - file: live/health/NOW.md
    op: edit
    owner_approved: not_required
    change: |
      Keep active_bet g-health-core active.
      Add/record review checkpoint on active_bet:
        review_status: partially_met_pending_cross_family_g5
        review_checkpoint: 2026-06-15 c-health-core-review-001
        product_evidence_status: clean_prepass
        product_evidence_commits:
          - a67a34e109aac5f70284b048af4480be38fb8cd5
          - ee25a894e22d83485525f7d798f02e0fa9d48189
          - 8bc980ad21d3f54cbd27b28dcb363e0198c46751
        product_blocker_gaps: 0
        non_blocking_gaps:
          - P8
          - existing-v1-input
        binding_g5_status: missing_cross_family
        verdict: partially_met
      Remove open_calls item id c-health-core-review-001.
      Add open_calls item:
        id: c-health-core-cross-family-g5-002
        to: session
        for: g-health-core binding cross-family G5 review
        issued: 2026-06-15
        note: >
          Product evidence pre-pass is clean, but g-health-core cannot close until a non-OpenAI
          family, ideally Claude, freshly tries to refute WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9,
          check output, gap classification, and Direction OS boundary.
      Add decisions item:
        id: d-health-next-bet-after-core-g5
        status: awaiting_owner
        question: >
          If cross-family G5 returns met, which next bet should health shape next?
        options:
          - A: Shape g-health-nutrition-system next.
          - B: Shape g-health-training-activity-system next.
          - C: Pause the direction after core and review priorities.
        recommendation: A
        activation_condition: only after binding cross-family G5 returns met.
      Set next to the CALL c-health-core-cross-family-g5-002 below.
  - file: live/health/TREE.md
    op: none
    owner_approved: not_required
    change: >
      No TREE changes. g-health-core remains active until cross-family G5 passes; parked module nodes remain unchanged.
  - file: live/health/LOG.md
    op: append
    owner_approved: not_required
    change: >
      2026-06-15 — c-health-core-review-001 review: g-health-core verdict partially_met.
      Product evidence at a67a34e/ee25a89/8bc980a is clean pre-pass: WA1-WA12 + W69/W70/W72/W73/W74
      + CA1-CA9 mapped and reported PASS, checks reported PASS, product blocker gaps 0,
      add-back 0/8. Binding G5 remains open because required cross-family review is missing.
      Next: c-health-core-cross-family-g5-002, surface Claude preferred.
  - file: live/health/knowledge/health-core-g5-evidence-rule.md
    op: create
    owner_approved: not_required
    change: see knowledge.promote[0]
  - file: live/health/history/2026-06-15-c-health-core-review-001.md
    op: create
    owner_approved: not_required
    change: Store this full RESULT.

captures: []

decisions_needed:
  - id: d-health-next-bet-after-core-g5
    when: after c-health-core-cross-family-g5-002 returns met
    question: >
      Which next bet should health shape after g-health-core closes?
    options:
      - id: A
        label: Shape g-health-nutrition-system
        why_now: >
          Nutrition is the highest-leverage first module for the weight outcome and will test
          whether core-owned program/tracking/review mechanics produce real food outputs without
          Direction OS becoming a diary.
      - id: B
        label: Shape g-health-training-activity-system
        why_now: >
          Training/activity tests the body-composition, safety, and module-attach contracts through
          strength/activity loops, but it is less primary than nutrition for the first weight-loss phase.
      - id: C
        label: Pause this direction
        why_now: >
          Honest option if owner wants to stop system-building after the core and return later.
    recommendation: A
    recommendation_reason: >
      After core closure, nutrition should come first because it directly drives the first clinical
      weight-loss milestone and will validate the core in daily use without duplicating training complexity.

play_check:
  - step: 1 Verify by refutation
    status: done
    note: >
      Checked committed evidence, matrix, scripts, gap classification, owner clearance, scope cuts,
      Direction OS boundary, and G5 status. Verdict = partially_met.
  - step: 2 Harvest per lens
    status: done
    note: >
      Harvested consequences for all CHARTER lenses: weight-nutrition, strength-body-composition,
      activity-conditioning, adherence-relapse, medical-safety, ai-system-data-architecture.
  - step: 3 Update the tree
    status: done
    note: >
      No TREE diff proposed because binding G5 is missing. No owner approval required because no TREE
      changes enter state_changes.
  - step: 4 Add-back check
    status: done
    note: >
      Cut list checked; 0/8 missed cut items. Observation recorded in log line.
  - step: 5 Knowledge
    status: done
    note: >
      Proposed one durable knowledge entry: cross-family G5 evidence rule for provider-independence/core bets.
  - step: 6 Select next
    status: done
    note: >
      Prepared conditional next-bet decision: nutrition vs training/activity vs pause; recommendation = nutrition
      after binding G5 passes.
  - step: 7 Close
    status: done
    note: >
      Closing as checkpoint RESULT, not bet closure. Next CALL routes binding cross-family G5.

log: >
  2026-06-15 — c-health-core-review-001 review: g-health-core partially_met; product evidence clean
  pre-pass, product blocker gaps 0, add-back 0/8, binding cross-family G5 missing; next
  c-health-core-cross-family-g5-002.

next: |
  CALL c-health-core-cross-family-g5-002
  to: session
  direction: health
  play: review
  node: g-health-core
  goal: |
    g-health-core has a binding cross-family G5 verdict: met, partially met, or not met.
  context: |
    Previous review checkpoint: c-health-core-review-001 returned partially_met because product
    evidence is clean but binding cross-family G5 is missing.

    Direction OS state:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-core.md

    health-ai product evidence:
    - t-1 commit a67a34e109aac5f70284b048af4480be38fb8cd5
      "core acceptance harness: map converged spec"
    - t-2 commit ee25a894e22d83485525f7d798f02e0fa9d48189
      "core slice: replace v1 structure"
    - t-3 commit 8bc980ad21d3f54cbd27b28dcb363e0198c46751
      "core evidence: package t-3 dry-run proof"
    - key paths:
      acceptance/core/matrix.json
      acceptance/core/evidence-summary.md
      acceptance/core/fixtures/core-only/fixture.json
      acceptance/core/clearance.md
      tools/check_acceptance_matrix.py
      tools/check_core_slice.py
      tools/check_core_evidence.py

    Same-family pre-pass findings to refute:
    - matrix carries WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
    - evidence-summary reports:
      python tools/check_acceptance_matrix.py => PASS; 17 acceptance rows, 9 contract rows,
      27 PLAN rows, 9 architecture inputs, blocker gaps 0.
      python tools/check_core_slice.py => PASS; 32 core files, schema/frontmatter ok,
      matrix target files ok, WA73 formula ok, PLAN/LOG separation ok,
      forbidden module/runtime directories absent.
      python tools/check_core_evidence.py => PASS; 11 dry-run scenarios, 26 acceptance/contract
      rows pass, 0 fail, blocker gaps 0.
    - non-blocking gaps: P8 and existing-v1-input; existing-v1-input should be checked against
      acceptance/core/clearance.md owner confirmation.
    - binding G5 has NOT yet happened; do not treat Codex/OpenAI evidence as binding.
  boundaries: |
    Do not store raw daily health data in Direction OS.
    Do not build or change product repo implementation during review.
    Do not build nutrition/training/activity modules, app UI, runtime, DB, server, cron, or scheduler.
    Do not make medical prescriptions.
    Do not treat Codex/OpenAI t-3 or ChatGPT review as binding cross-family G5 evidence.
  done_when: |
    - Fresh cross-family refutation explicitly handles WA1-WA12 + W69/W70/W72/W73/W74 + CA1-CA9.
    - It explicitly handles check output, gap classification, product scope cuts, owner clearance, and Direction OS boundary.
    - It returns a binding G5 verdict: met, partially met, or not met.
    - If met, it prepares owner-facing decisions for approving any TREE status change and choosing the next bet.
    - If not met or partially met, it returns exact blocker/refutation gaps and the next CALL.
  return: |
    RESULT with binding cross-family verdict, refutation evidence, state_changes, decisions_needed, and next CALL/awaiting_decision.
  budget: one focused cross-family review session
  surface: Claude preferred / non-OpenAI family required for binding G5

END_OF_FILE: live/health/history/2026-06-15-c-health-core-review-001.md
