# NOW — life-reset

active_bet:
  node: g-lr-run
  status: active
  shaped_by: 2026-06-21 s-life-reset-shape-run-v1-001 (owner-approved G9: "да")
  goal: |
    ONE tiny real composed pulse on REAL owner data that closes the one-real-run gate — not
    "architecture exists". Two files (a sealed-core file + a week-file) + ONE real run: a week
    composed in strict order with the filter biting, a day derived with the R11 gate, one real
    protect episode, one review→one decision, all durable + portable across a chat restart,
    owner attests it was real.
  appetite: |
    ~3 focused hours to author the 2 v1 files. The real run is OWNER-PACED and is NOT in the
    build budget. Not extended — if it needs more, re-shape a SMALLER run (over-appetite dies,
    G3). Build to the end without mid-stream rebuilds; evaluate only at the checkpoint (R12).
  kill_by:
    metric: real end-to-end runs on live data
    threshold: 0 runs while the v1 files exist
    soft: 2026-07-05  # 2 weeks → pause & sit down to run (anti-paper brake, pre-mortem #11)
    hard: 2026-07-19  # 4 weeks → kill → re-shape a smaller run / tiny-probe
    note: owner-paced; re-anchor to build-complete +2wk/+4wk if the build starts later.
  next_if_true: |
    the run closes the one-real-run gate → the next node opens (protect/integrate deeper) or a
    review confirms v1 and unlocks g-lr-grow extensions.
  next_if_false: |
    no real run by the hard date → kill the bet; re-shape an even smaller run (or a tiny-probe).

  done_when: |
    On live data: ≥1 real week composed in strict order (tier-1 floors+rest+recovery first ·
    ≥1 wish through the filter OR rejected-with-reason · ≥1 explicit cut · ≥2 neighbor
    summaries present · ≥1 stream conflict surfaced+routed), ≥1 real day derived (R11 fired
    ≥1), ≥1 real protect episode, ≥1 saved review→decision; all durable; a fresh chat resumes
    the live running-state by delta; owner attests the run was REAL (not paper/demo).

  week_layout: |
    ONE week-file, four sections in FIXED file-position order (position = "big rocks first"):
      1. PROTECTED TIER-1  — Musts + Floors + Routine-rest + Recovery (rest/recovery off the
         top, uncuttable; the filter cannot touch this; "musts first" = ORDER, not size).
      2. Routine          — the current schedule.
      3. Wishes-through-filter — each admitted-with-reason OR rejected-to-backlog-with-reason;
         mark the ≤1 experiment; the burden of proof is on the wish.
      4. Cuts             — explicit; a `displaces:` line whenever a cut is a displacement
         (if no displacement actually happened in the run, `displaces:` is labelled untested).

  resolved_gaps:
    recovery_vs_slide: |
      Distinguished NOT by the activity but by 3 observable signs — named/sanctioned ·
      floors-still-stand · bounded-with-return. Anti-gaming without punishment: the owner may
      CALL anything recovery (default = treat-as-recovery, never punished, G3), but the
      owner-authored floor tripwires watch the FLOORS, not the label — a fallen floor fires the
      tripwire as a PROTECT episode (reach-in / name the falling pillar), not a verdict.
      THREE response altitudes (t-1 audit): (1) default = treat-as-recovery; (2) fallen floor
      = in-system PROTECT reach-in; (3) a pre-named CLINICAL-RISK sign = route OUT to
      professional support, never intensify discipline (sealed, lives in the t-2 core).
    floors: |
      1. Sleep — not broken 2 nights running. 2. Not smoking again. 3. No binge-eating.
      4. Not vanishing / zoning-out for days. (A 5th "training/practice discipline" floor is
      captured for a gated future mutation once a training process exists — NOT in v1.)
    integrate_present_minimal: |
      The manager only READS a short neighbor summary (health, game — source of truth stays
      inside the direction); thin/missing → owner tops up in words; NEVER ingests raw, NEVER
      touches a neighbor's internal process; a stream conflict surfaces as an explicit line +
      a route ("→ health" / "owner decides"). No raw neighbor data stored (G4). Streams = the
      neighbor directions (read-only) + the owner's backlog.

  lens_sweep:
    - weekly-execution: TASK (t-3/t-4 — compose in strict order, filter bites, explicit cuts).
    - daily-discipline: TASK (t-3/t-4 — MIT-style day-derivation + the R11 gate).
    - cross-direction-integration: TASK (t-3/t-4 — read-only neighbor summaries, present-minimal).
    - improvement-and-learning: TASK (t-4 — one review→one decision, default {hold}); the full
      self-rewrite engine is deferred to g-lr-learn.
    - spirit-and-transcendence: not_needed (v1 — a terminal value / a grow-program, excluded).
    - inner-work-and-disclosure: not_needed (v1 — same, deferred).
    - fatherhood-and-example: not_needed (v1 — a quality criterion, not a first-run mechanism).
    - system-quality: TASK/condition (stays-light enforced by the appetite cap + kill_by
      bureaucracy brake + the no-mid-stream-churn run model).
    - safety: TASK (t-1/t-2 — recovery carve-out + floors/tripwires + inviolable override +
      CLINICAL-RISK ROUTING: a clinical-risk sign routes OUT to professional support, not an
      in-system reach-in — restored by the t-1 plan audit). CRITICAL.

  cut_list: |
    NOT in v1 (≥1 real cut, G6) → captures / g-lr-grow backlog: typed-commitment DAG / Kanban
    board (Q1); N-of-1 evaluate-and-swap loop (Q2); baseline-relative surge-governor/ACWR (Q3
    → g-lr-protect); automated post-rewrite gate w/ auto-revert (Q4); process-trace proxy
    "unreliable-narrator" detector (Q5); track-record ledger / per-domain trust accounts (Q6);
    two-key (subjective OR behavioral) hollow-veto (Q7); dormancy auto-prune + hard WIP cap on
    rules (Q8); gap-length tiered re-entry (Q9); fresh adversarial self-cert session (Q10);
    routed-request-to-source for neighbor summaries (integrate — v1 = read + owner top-up).

  forecast: |
    Likely to close the gate: the slice is tiny, inherits the existing OS substrate, and its
    HOW was already multi-agent-verified in research. The cheapest risk (recovery-vs-slide) is
    tested FIRST (t-1) on past data, so a fatal flaw surfaces before any file is built.
  against: |
    Top risk: a flat 4-layer file may not hold real integrate-streams + day-derivation + drift
    on the first real week, OR the manager cannot reliably tell recovery from slide → t-1 +
    t-4 are exactly where that shows. The gate rests on owner self-attestation (deferred
    hardening = the adversarial self-cert session, Q10).

tasks:
  - id: t-1
    kind: session
    status: done   # 2026-06-21 s-life-reset-run-v1-t1-plan-audit-001
    goal: |
      RE-SCOPED by live owner instruction: the narrated back-test was dropped as self-graded
      theater (owner: "Это нахуй не проверка, … проверяй на консистентность данных, на план …
      что всё покрыто, каждая процедура"). New job: audit the v1 plan for coverage +
      consistency + data-flow before building, confirm the recovery-vs-slide rule (3 signs) +
      the 4 floor-tripwires are build-ready, fix any gap.
    done_when: |
      DONE. Audit ran (wf_35ccf508, 24 agents, adversarially verified): 62 required
      procedures COVERED; rule + 4 tripwires build-ready; no contradictions; all 4 v1
      data-flows close. ONE load-bearing defect found+fixed — the sealed core (t-2) had
      dropped the charter's clinical-risk routing rule. Verdict: BUILD-READY. The 3 signs +
      the 4 floors + the 3 response altitudes live in resolved_gaps; a clinical-risk sign
      routes OUT (to professional support), NOT an in-system reach-in. Evidence:
      work/life-reset-v1-plan-audit-001.md.

  - id: t-2
    kind: executor
    status: active
    goal: |
      Author the sealed-core file ONCE (serves Q4/Q5/Q9): inviolable override path (incl. the
      R11 refusal) · protected class (recovery/safety/floors incl. routine-rest) · manual
      rollback (git-revert, no automation overclaim) · "rules change only via the gate" (every
      ACTUAL rewrite is gate-checked — not "provably sealed forever") · the 4 tripwires (from
      t-1) · the non-punishing-return invariant (hosted HERE, not on the override path) ·
      CLINICAL-RISK ROUTING (t-1 audit fix): on a pre-named clinical-risk sign the manager
      routes OUT to professional support and does NOT intensify discipline or prescribe
      treatment — a sealed class, distinct from the in-system recovery reach-in.
    done_when: |
      The sealed-core file exists, durable, listing all of the above INCLUDING the clinical-
      risk routing rule (its specific signs co-created with the owner when authoring this file
      — owner-content); v1 performs NO rewrite (that is g-lr-learn) — this only authors the
      core + a repeatable 2-assertion hand-run smoke check (override still works + floors
      intact). No surfaced numbers (G2).

  - id: t-3
    kind: executor
    status: pending
    goal: |
      Author the week-file template: the 4 fixed-position sections · read-only neighbor-summary
      slots + owner top-up + conflict→route (no raw) · MIT-style day-derivation + the R11 gate
      + where "yesterday's review" lives · the review template (default {hold}, the hollow-week
      veto WITH the recovery carve-out, no numbers) · the realness card (anti-paper
      artifact-existence + one mandatory BITE slot) · the live running-state fields for
      portability (cycle position, current protections, autonomy rung) + delta re-entry.
    done_when: |
      The week-file template exists with every section above; the displacement test is
      non-vacuous (a real cut must be loud; `displaces:` fires on a real displacement else is
      labelled untested); the realness card binds on artifact-existence + one bite event.

  - id: t-4
    kind: owner-run
    status: pending
    goal: |
      THE REAL RUN (owner-paced): compose one real week (floors first · filter bites ≥1 · ≥1
      explicit cut · ≥2 neighbor summaries · ≥1 conflict routed) — the first compose also does
      a LIGHT intake (manager asks missing facts) + picks ≤1 working technique (owner-reported,
      heuristic best-bet; on a recovery week a technique is PAUSED not failed) — derive one
      real day (R11 fires), one real protect episode fires, save one review→one decision.
    done_when: |
      All of the above happened on live data and is durable; the filter genuinely BIT (a real
      cut gave something up OR it bit the owner's own pull OR recovery was protected against a
      real temptation — the bite slot is non-empty and not invented).

  - id: t-5
    kind: session
    status: pending
    goal: |
      Portability + owner attestation: a FRESH chat resumes the LIVE running-state (cycle
      position, current protections) via delta-only re-entry ("what changed?"), no full
      re-intake; the owner attests the run was REAL and actually worked.
    done_when: |
      A fresh chat continued the running-state (not just the archive), and the owner explicitly
      attests it was a real run (closes the one-real-run gate / criterion ① + ②).

recurring: []

open_calls: []   # t-1 done; the t-2 CALL is `next`, not yet in-flight.

decisions: []

preserved_evidence:
  - live/life-reset/work/life-reset-manager-vision-capture-v1.md
  - live/life-reset/work/life-reset-implementation-research-v1.md
  - live/life-reset/history/2026-06-21-s-life-reset-frame-root-001.md
  - live/life-reset/history/2026-06-21-s-life-reset-map-manager-tree-001.md
  - live/life-reset/history/2026-06-21-s-life-reset-research-build-manager-001.md
  - live/life-reset/history/2026-06-21-s-life-reset-shape-run-v1-001.md
  - live/life-reset/work/life-reset-v1-plan-audit-001.md
  - live/life-reset/history/2026-06-21-s-life-reset-run-v1-t1-plan-audit-001.md

next: |
  CALL c-life-reset-run-v1-t2-sealed-core-001
  to: session
  direction: life-reset
  play: work
  node: g-lr-run
  task: t-2
  goal: |
    Author the sealed-core file ONCE (the manager's non-amendable safety layer), listing: the
    inviolable override path (incl. R11 refusal) · the protected class (recovery/safety/floors
    incl. routine-rest) · manual git-revert rollback (no automation overclaim) · "rules change
    only via the gate" · the 4 floor-tripwires (sleep / not-smoking / no-binge / not-vanishing,
    from resolved_gaps.floors) · the non-punishing-return invariant (hosted HERE) ·
    CLINICAL-RISK ROUTING (a pre-named clinical-risk sign → route OUT to professional support,
    never intensify discipline — the t-1 audit's load-bearing fix). v1 runs NO rewrite; this
    only authors the core + a 2-assertion hand-run smoke check.
  context: |
    - live/life-reset/NOW.md (the v1 bet; resolved_gaps = the 3 recovery-vs-slide signs + the
      4 floors + the 3 response altitudes incl. clinical-risk route-OUT; t-2 goal/done_when)
    - live/life-reset/work/life-reset-v1-plan-audit-001.md (the t-1 audit: build-ready; the
      clinical-risk defect + its fix)
    - live/life-reset/work/life-reset-implementation-research-v1.md (Q4 sealed core / Q5
      tripwires / Q9 non-punishing return — mechanics + required-fixes)
    - live/life-reset/CHARTER.md (guardrails G1-G4; authority_and_boundaries clinical-risk
      routing; risk_posture asymmetric rigor)
  boundaries: |
    Co-create with the owner — the CLINICAL-RISK SIGNS and what "professional support" means
    are owner-content (his signs, his words); do NOT invent them generically. Author ONLY the
    sealed core (not the week-file — that is t-3). NO rewrite engine (that is g-lr-learn). No
    surfaced numbers (G2). The override path stays inviolable; the non-punishing-return
    invariant lives in the core (NOT on the override path); clinical-risk routes OUT (not an
    in-system reach-in). Keep it light — a short readable file, not bureaucracy.
  done_when: |
    The sealed-core file exists (durable, in work/), listing all of the above INCLUDING the
    clinical-risk routing rule with owner-co-created signs; plus a repeatable 2-assertion
    hand-run smoke check (override still works + floors intact). next = t-3 (week-file template).
  return: RESULT with the sealed-core file, the smoke check, next = t-3 CALL.
  budget: one work session (co-creation with the owner).

END_OF_FILE: live/life-reset/NOW.md
