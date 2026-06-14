# NOW — health

active_bet:
  status: none
  note: >
    CORE-FIRST RE-FRAME (2026-06-14). Owner redirected the whole direction: build a strong,
    structured, provider-independent CORE first (programs-as-plan + daily tracking + records +
    shared metrics/phases/review, Markdown/YAML in git, NL/voice/photo input, self-extensible
    via workflow), then nutrition and training as MODULES attached to it. The tree was re-mapped
    and CHARTER amended with a system-architecture constraint (owner approved, "ok").

    g-health-ai-core (was done) is SUPERSEDED/dropped — its artifacts (product repo health-ai,
    contract/skeleton v0) are dirty input, not authority. The product repo health-ai will be
    CLEARED and rebuilt in place at build time (same repo, git history preserves v1); the actual
    wipe needs explicit owner confirmation at that step.

    CONVERGE g-health-core IN PROGRESS (2026-06-14): Define done — node typed HEAVY, 7 owner-approved
    decisions imported born-closed (I1–I7), ~30-term disputed glossary built + partitioned
    owner-vs-system, ~28 expert readings system-locked, safety floor charter-locked. Assembly surface
    = work/converge-g-health-core.md. AWAITING owner Define §SIGNOFF (3 batched G7 — see decisions).
    Resolve (§WHAT) does not start until signed. The paused nutrition Define
    (work/converge-nutrition-define-draft.md) + recon (work/health-core-recon-research.md) remain
    DIRTY input evidence, never authority.

tasks: []

recurring: []

open_calls:
  - id: c-health-core-converge-001
    play: converge
    node: g-health-core
    status: in-flight (parked at the Define gate)
    note: >
      Heavy-node converge. Define complete; surface at work/converge-g-health-core.md. Continuation
      = c-health-core-converge-002 (Resolve) once the 3 batched G7 decisions below are signed.

decisions:
  - id: G7-1
    movement: converge Define (g-health-core)
    question: >
      research-and-decide membership test + the askable personal-facts set (what the system DECIDES
      vs ASKS; which facts are your irreducible-personal).
    options:
      A: researchable-from-evidence+profile ⇒ DECIDE, else ⇒ ASK; carve-out only by NAMED constraint;
        askable = irreducible facts + logging cadence; goal-weight/protect-strength system-proposed,
        owner-ratified; cooking-time = personal fact; non-blocking skippable setup. (recommended)
      B: wide askable set (re-opens v1 over-asking).
      C: A but cooking-time = system-decided cadence.
    recommendation: A
    status: pending_owner
  - id: G7-2
    movement: converge Define (g-health-core)
    question: >
      the autonomy dial ("leader with brakes") — how much the system may auto-apply/commit vs must
      surface for explicit OK.
    options:
      A: decide-and-inform; asks only on an enumerable brakes-list; review proposes, OK on braked
        items only. (recommended, with C's dial available)
      B: propose-and-wait (= the v1 over-asker).
      C: configurable autonomy level, default = A.
    recommendation: A (+ optional C dial)
    status: pending_owner
  - id: G7-3
    movement: converge Define (g-health-core)
    question: >
      the Direction OS boundary — the closed upward set + the raw-vs-summary "never a diary" line.
    options:
      A: strict 4-item {summary, decision, problem, CALL}.
      B: 6-item {summary, problem, decision, incident, evidence-pointer, CALL}; raw never crosses;
        summary by significant milestone only. (recommended membership + strict raw rule)
      C: 4-item + periodic weekly summaries up.
    recommendation: B-membership + A-strictness
    status: pending_owner

next: |
  awaiting_decision — owner signs the 3 batched G7 Define decisions above (G7-1, G7-2, G7-3).
  On the owner's answer, a fresh session applies it as the writer of §SIGNOFF Define and runs Resolve:

  CALL c-health-core-converge-002
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    Apply the owner's Define §SIGNOFF (G7-1/2/3) with his exact words; lock the owner-gate readings;
    then run Resolve — build the cited §WHAT as a node-on-paper (three sources: each done_when
    criterion; each cross-node edge; mechanism decomposition of I2/I3/I4/I6/I7 + every committed
    mechanism, recursive), tag acceptance rows, firewall HOW→PLAN. Then route to converge-arch.
  context: |
    RUN IN A FRESH CHAT. Define is DONE — surface at work/converge-g-health-core.md (§TRIAGE,
    §IMPORTS I1–I7, §GLOSSARY A owner-gate / B system-locked / C charter-locked / D undisputed-named,
    §SIGNOFF Define = PENDING). FIRST step: write §SIGNOFF Define quoting the owner's words for
    G7-1/2/3, lock the recommended (or owner-amended) readings. System-locked readings (§GLOSSARY B)
    feed Resolve directly and are refuted later by converge-verify, NOT re-signed. PLAN-agenda is
    pre-seeded in the converge-001 RESULT captures (resolve-on-read vs materialize; EMA window;
    carb tiers; FDC schema; registry-line syntax). Owner gates already spent 1 of ≤3.
  boundaries: |
    Import nothing new as authority; auto-fill nothing. No raw daily data in Direction OS; no medical
    prescriptions. Converge only (then converge-arch, converge-verify, shape).
  done_when: |
    §SIGNOFF Define written (owner words); §WHAT closed (forward-clean: no open/deferred; backward-clean:
    every weight-bearing line + acceptance + glossary row cited); converge_coverage complete; next = converge-arch.
  return: |
    RESULT with the closed §WHAT surface, §SIGNOFF Resolve, decisions_needed (if any remaining gate),
    and next CALL (converge-arch).
  budget: converge Resolve movement (may span sessions; owner gates batched ≤3 across the set, 1 spent)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
