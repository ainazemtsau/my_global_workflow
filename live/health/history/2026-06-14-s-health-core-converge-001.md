RESULT s-health-core-converge-001 (call: c-health-core-converge-001)
direction: health   play: converge   node: g-health-core   triage: heavy (converge ON)

outcome: |
  Converge Define done for g-health-core. Node typed HEAVY (model-bearing + cross-cutting +
  decomposes into subsystems). Imported 7 owner-approved decisions born-closed (I1–I7). Built the
  disputed-term §GLOSSARY (~30 terms) via a 6-agent miner sweep + an INDEPENDENT completeness
  oracle, partitioned owner-owned vs system-decided per the research-and-decide thesis. System
  locked ~28 expert/architecture readings with cited evidence (to be refuted by converge-verify);
  the floor of what the system may decide is the CHARTER-locked safety/medical layer. Stopped at
  the FIRST gate that needs the owner: the Define §SIGNOFF — 3 batched G7 decisions (G7-1 the
  decide-vs-ask membership test + askable personal-facts set; G7-2 the leader-with-brakes autonomy
  dial; G7-3 the Direction OS upward-set / no-diary line). Resolve does NOT start until these sign.

evidence: |
  work/converge-g-health-core.md: §TRIAGE (3 heavy triggers) · §IMPORTS I1–I7 (each with owner
  evidence + names_mechanism flag) · §GLOSSARY A(owner-gate, 3 batched)/B(~28 system-locked with
  →PLAN firewall)/C(charter-locked safety floor)/D(undisputed-but-named: criterion 1a store, 2d
  value-type grammar) · §SIGNOFF Define = PENDING · §WHAT = NOT STARTED.
  Define-phase coverage: all 9 done_when criteria → ≥1 glossary term; every compound criterion
  atomically split; the one mechanical-mining MISS (safety/medical floor) was caught by the
  independent oracle and added. Miner = workflow wf_1bd6272e-de9 (6 agents, real source citations).

state_changes: |
  work/:
  - CREATE work/converge-g-health-core.md (the converge assembly surface; product, not state).
  NOW.md:
  - active_bet: stays status none; note appended — "converge g-health-core IN PROGRESS: Define done,
    glossary at work/converge-g-health-core.md, awaiting owner Define §SIGNOFF (3 batched G7)."
  - open_calls: add c-health-core-converge-001 (play converge, node g-health-core) status in-flight,
    parked at the Define gate.
  - decisions: add the 3 batched G7 Define decisions (G7-1, G7-2, G7-3) — options + recommendation
    each; status pending_owner.
  - next: -> awaiting_decision (continuation CALL c-health-core-converge-002 = converge Resolve on
    g-health-core, precondition: §SIGNOFF Define exists).
  LOG.md:
  - append: "2026-06-14 — health/g-health-core converge (Define): heavy; imported I1–I7 born-closed;
    ~30-term glossary partitioned owner-vs-system (3 batched G7) + independent completeness oracle
    added the safety-floor miss; stopped at Define gate; next = owner signs, then Resolve."
  history/:
  - add 2026-06-14-s-health-core-converge-001.md (this full RESULT).

captures:
  - The one disputed term mechanical mining MISSED (safety/medical floor, read as system-guardrail
    vs hard-layer-above-the-engine) was surfaced by the SEPARATE completeness oracle — concrete
    evidence the converge-verify independent-oracle discipline earns its place even at Define.
  - Pre-load the PLAN agenda: recon open-Qs that are HOW→PLAN (resolve-on-read vs materialize Q3;
    EMA window; carb-by-day_type tiers Q4; FDC field schema Q5; registry-line syntax) are already
    firewalled in §GLOSSARY B and should ride converge-arch/shape as the PLAN-agenda, not WHAT.
  - Biofeedback objective-recovery metrics (HRV/RHR/sleep-device) DEFERRED pending a clean-evidence
    pass (marketing-dominated evidence; recon Q7); subjective 0–5 is IN.

decisions_needed:
  - id: G7-1
    question: research-and-decide membership test + the askable personal-facts set (what the system
      DECIDES vs ASKS, and which facts are your irreducible-personal).
    options:
      - A (recommended): researchable-from-evidence+profile ⇒ DECIDE, else ⇒ ASK; carve-out only by
        NAMED constraint, never by owner wish; askable = irreducible facts (dislikes/allergies/meds/
        schedule/budget/real cooking-time/equipment) + logging cadence; goal-weight & protect-strength
        = system-proposed/owner-ratified; sex/height objective; cooking-time = personal fact;
        non-blocking skippable setup.
      - B: wide askable set (goal-weight/protect-strength asked + owner wishes on expert vars) —
        re-opens the v1 over-asking defect.
      - C: A, but cooking-time treated as a system-decided cadence (tighter decide bias).
    recommendation: A
  - id: G7-2
    question: the autonomy dial ("leader with brakes") — how much the system may auto-apply / commit
      vs must surface for your explicit OK.
    options:
      - A (recommended): decide-and-inform — drives, logs/parses-commits silently when confident,
        asks ONLY on an enumerable brakes-list (safety, below calorie floor, intensity up, sharp
        course change); review PROPOSES target changes, OK needed only on braked items.
      - B: propose-and-wait (collaborative) — essentially the v1 over-asker.
      - C: configurable autonomy level (Coached/Collaborative/Manual) you flip over time, default = A.
    recommendation: A (default), with C's single dial available.
  - id: G7-3
    question: the Direction OS boundary — the closed set that may flow UP and the raw-vs-summary
      "never a diary" line.
    options:
      - B-membership + A-strictness (recommended): adopt the governance-doc 6-item upward set
        {summary, problem, decision, incident, evidence-pointer, CALL}; raw daily data NEVER crosses;
        "summary" only by significant milestone.
      - A: strict 4-item set {summary, decision, problem, CALL}.
      - C: 4-item set + periodic (weekly) summaries allowed up.
    recommendation: B-membership + A-strictness

play_check:
  - 1 Triage & import: done — heavy (3 triggers); imported I1–I7 born-closed; NOT imported:
    research-and-decide operational test (→G7-1), autonomy level (→G7-2), un-ratified glossaries/recon.
  - 2 Define: done up to the gate — terms seeded mechanically from the 9 done_when criteria + 6 lens
    nouns; ONE miner call:research run as a 6-agent sweep; §GLOSSARY built; disputed-term readings to
    SIGN are batched into G7-1/2/3. SIGN sub-step is (owner) — AWAITING (gate presented in
    decisions_needed; no owner words yet, so §SIGNOFF Define is unwritten).
  - 3 Resolve: NOT STARTED — stopped at the first owner gate (every §WHAT line cites a glossary
    reading; the owner-gate readings are not yet locked).
  - 4 Close & route: NOT REACHED.
  - imported: [I1,I2,I3,I4,I5,I6,I7]
  - converge_coverage (Define-phase): all 9 done_when criteria → ≥1 glossary term; lenses covered
    (medical-safety → safety-floor added; ai-system-data-architecture → the core glossary;
    weight/strength/activity/adherence → module-touching terms present, module specifics deferred).
  - canon_proposed: [research-and-decide, anchors-vs-derived, PLAN-vs-LOG, parse-vs-values-firewall,
    leader-with-brakes, direction-os-boundary] — proposed as decision-class canon for review/pulse
    (converge proposes; review/pulse promote; not written to knowledge/ here).

log: "converge g-health-core (Define): heavy; I1–I7 imported born-closed; ~30-term glossary partitioned
  owner-vs-system, independent oracle added the safety-floor miss; stopped at Define gate = 3 batched
  G7; next = owner signs, then Resolve."

next: |
  awaiting_decision (G7-1, G7-2, G7-3 — Define §SIGNOFF). On owner answer, a fresh session applies it:
  CALL c-health-core-converge-002
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    Apply the owner's Define §SIGNOFF (G7-1/2/3), then run Resolve — build the cited §WHAT as a
    node-on-paper (three sources: each done_when criterion; each cross-node edge; mechanism
    decomposition of I2/I3/I4/I6/I7 + every committed mechanism, recursive), tag acceptance rows,
    firewall HOW→PLAN. Then converge-arch (contracts + architecture).
  context: |
    Fresh chat. work/converge-g-health-core.md (§TRIAGE, §IMPORTS I1–I7, §GLOSSARY A/B/C/D, §SIGNOFF
    Define). First step: write §SIGNOFF Define with the owner's exact words; lock the owner-gate
    readings; THEN Resolve. System-locked readings (§GLOSSARY B) feed Resolve directly; converge-verify
    refutes them later. PLAN-agenda pre-seeded in the captures.
  boundaries: |
    Import nothing new as authority; auto-fill nothing. Owner gates already spent 1 of ≤3 (Define);
    converge-arch may spend the remaining budget. No raw daily data in Direction OS; no medical prescriptions.
  done_when: |
    §SIGNOFF Define written (owner words); §WHAT closed (forward-clean: no open/deferred; backward-clean:
    every weight-bearing line + acceptance + glossary row cited); converge_coverage complete; next = converge-arch.
  return: RESULT with the closed §WHAT surface, §SIGNOFF Resolve, and next CALL (converge-arch).
  budget: converge Resolve movement (may span sessions)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/history/2026-06-14-s-health-core-converge-001.md
