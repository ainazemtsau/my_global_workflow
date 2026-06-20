# NOW — health

active_bet:
  status: none
  note: >
    2026-06-20 owner reframe (Variant 1). Mid-converge the owner identified that the
    rejected Health AI nutrition slice is a symptom of a MISSING CORE LAYER, not a
    nutrition-only gap: g-health-core delivered the data/contract layer but never
    provided a runtime — per-domain memory/working-state, state machines, a single
    procedure-interpreter/router, and a governance lifecycle (artifact SEED→PROPOSED→
    ACTIVE→SUPERSEDED + owner-approval gate + confirm-before-save + readable-for-owner +
    writer/evidence barrier + one-chat-one-job). g-health-core is re-opened (parked) to
    be EXTENDED into a kernel; nutrition and training become thin layers; the governance
    design is preserved at work/core-kernel-governance-lifecycle-spec.md. The kernel WHAT is
    converged + owner-signed 2026-06-20 (Package A = F1–F16 at recommended readings; B-1
    G7-2 re-signed by layer; B-2 scaffolding; B-3 domain graph owner-approved; B-4
    anti-fragility binding) in work/converge-g-health-core-kernel.md. converge-arch is now CLOSED
    (2026-06-20, s-health-core-kernel-converge-arch-001): the 14 engine-inheritance contracts KC1-KC14 +
    7 internal seams + 4 architecture picks (writer-locus, cold-start bootstrap, lifecycle/state-machine
    orthogonality, definition-reversion vs in-flight cursor) declared in
    work/converge-g-health-core-kernel-arch.md, owner_gate_batch = [] (zero new owner gates, matching the
    data-layer precedent). converge-verify is now CLOSED (2026-06-20, s-health-core-kernel-converge-verify-001):
    BINDING G5 PASS in a FRESH session (42-class independent oracle authored blind + 4 attackers + 2-skeptic
    adversarial verify; 90/90 §KW rows homed, the 5 orphans verified, WA-K1-K12 carried, firewall clean, no pick/KP
    leaked into done_when, the KQ-rev system-locked demotion holds; 5 candidate holes raised and ALL refuted; 2
    HOW-only PLAN residuals — KQ-rev orphan-detection/repair-format via KP2/KP10, KQ-concurrent one-liner). The kernel
    converge SET is COMPLETE + refuted-clean; §SIGNOFF converge-verify in work/converge-g-health-core-kernel-arch.md.
    next = shape (copies §WA-K1-K12 verbatim into the executor done_when). No active bet until the kernel is shaped.

tasks: []

open_calls:
  - id: c-health-core-kernel-converge-001
    status: done
    note: >
      DONE 2026-06-20 (s-health-core-kernel-converge-001): kernel WHAT converged + owner-signed.
      Package A (16 forks F1–F16 at recommended readings) + B-1 (G7-2 re-signed BY LAYER:
      confirm-before-save on first-time authored owner-facing content + ACTIVE flips;
      decide-and-inform on daily logging AND review-driven adjustments of already-ACTIVE anchors)
      + B-2 (confirm-before-save = initial scaffolding with an explicit later relax path) + B-3
      (a domain's state-machine graph is an owner-approved ACTIVE artifact) + B-4 (anti-fragility
      is a binding acceptance invariant). Assembly: work/converge-g-health-core-kernel.md.
      Routed to converge-arch.
  - id: c-health-core-kernel-converge-arch-001
    status: done
    note: >
      DONE 2026-06-20 (s-health-core-kernel-converge-arch-001): kernel cross-cutting CONTRACTS declared on
      paper over the signed data-layer CA1-CA9. 14 engine-inheritance contracts KC1-KC14 (4 runtime
      primitives: single router/KC1, working-state cursor/KC2, state-machine def-cursor split/KC3, procedure
      registry/KC4; 7 governance: lifecycle status/KC5, approval gate/KC6, writer-applier barrier/KC7,
      confirm-by-layer/KC8, render-before-decision/KC9, one-chat-one-job+handoff/KC10, provenance/KC11; 3
      engine invariants: thin-attach/KC12, anti-fragility/KC13, cold-start+journey/KC14) + 7 internal seams
      S1-S7 + a 3-tier build-order stack, every domain inherits unchanged. 4 architecture refuted-chains
      (writer-locus = separate context; cold-start = kernel-owned universal bootstrap machine; lifecycle vs
      state-machine = ORTHOGONAL with one render-before-decision seam; definition-reversion = impact-classified
      fail-closed re-validation). owner_gate_batch = [] (zero new owner gates; a miner over-call demoted to
      system-locked by two attackers). All 90 §KW rows homed, firewall clean, KP1-KP12 routed. Assembly:
      work/converge-g-health-core-kernel-arch.md. Routed to converge-verify.
  - id: c-health-core-kernel-converge-verify-001
    status: done
    note: >
      DONE 2026-06-20 (s-health-core-kernel-converge-verify-001): BINDING G5 refutation PASS in a FRESH session.
      Workflow wf_924f181d-c2d (16 agents): an INDEPENDENT 42-class kernel-node-class oracle authored blind from
      first principles + 4 attackers (completeness / smuggling / firewall+build-order+done_when-leak / arch-pick
      re-refutation) + 2-skeptic adversarial verify per finding. Both propositions PASS: completeness (all 90 §KW
      rows homed, zero orphans/phantoms; the 5 just-bound orphans KV6/KV7->KC6, KV8->KC9, KV12->KC7, KD2->KC1
      verified genuinely homed; WA-K1-K12 carried; every one of the 42 decision-classes covered; build-order
      non-dangling) AND traceability (firewall clean; no pick/KP leaked into a done_when line; the KQ-rev
      "who authors the rebuilt orphan cursor" system-locked demotion HOLDS via KM11+KV20+KV21+KS6+W21;
      owner_gate_batch = [] sound). 5 candidate holes raised, all 5 refuted. 2 HOW-only PLAN residuals (KQ-rev
      orphan-detection/repair FORMAT -> KP2/KP10; KQ-concurrent -> one-line PLAN note); zero out-of-scope.
      §SIGNOFF + §PROPOSED-CANON (the 42-class checklist) recorded in work/converge-g-health-core-kernel-arch.md.
      Routed to shape (c-health-core-kernel-shape-001).

recurring: []

decisions: []

next: |
  CALL c-health-core-kernel-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-core
  goal: |
    Shape the refuted-clean kernel converge SET into a committed bet the executor can build: a shaped node
    (appetite + kill_by), a cut list with >=1 real cut, a per-lens sweep verdict, and a task testing the
    riskiest assumption; the executor done_when copies §WA-K1-K12 VERBATIM (binding by G5). Decide here
    whether the kernel ships as one TIER-2 engine bet and the parked domains (nutrition, training) re-enter
    TRIAGE later, or whether to split now.
  context: |
    Refuted-clean set (converge-verify PASS @ 2026-06-20): live/health/work/converge-g-health-core-kernel-arch.md
    (§KERNEL-CONTRACTS KC1-KC14 + seams S1-S7 + §KERNEL-ARCH KQ1-KQ3 + KQ-rev + §VERIFY + §SIGNOFF converge-verify
    + §PROPOSED-CANON 42-class checklist). COPY VERBATIM into the executor done_when (G5): §WA-K1-K12 in
    live/health/work/converge-g-health-core-kernel.md. Architecture-on-paper INPUT EVIDENCE (never into done_when):
    KC1-KC14 + the 4 arch picks. PLAN agenda: KP1-KP12 + the 2 converge-verify PLAN residuals (KQ-rev
    orphan-detection/repair-format via KP2/KP10; KQ-concurrent one-liner). Data layer imported born-closed
    (live/health/work/converge-g-health-core.md: CA1-CA9, WA1-WA12). Owner format prefs (durable): never show
    writer/YAML files; present a readable "result + what will be saved". Product repo for execution = health-ai
    (github.com/ainazemtsau/health-ai, C:\projects\health-ai).
  boundaries: |
    Do NOT re-open the signed WHAT/data-layer/owner decisions or the refuted picks. HOW residuals stay on the
    KP/P PLAN agenda, never into done_when. The kernel is ONE indivisible TIER-2 engine (KC12 forbids a domain
    owning an engine part) — do not fragment the runtime primitives across nodes. TREE/CHARTER edits need the
    owner's explicit in-session approval (G9). The journey-proof (WA-K10) + KC5/KC6/KC7/KC14 green are a HARD
    precondition before any TIER-3 domain reaches ACTIVE.
  done_when: |
    A shaped g-health-core kernel bet exists in NOW.md with appetite + kill_by + tasks (<=3 active, each <= half a
    focused day); a cut list with >=1 real cut; a lens-sweep verdict per CHARTER lens; a task testing the riskiest
    assumption (G6). The executor done_when copies §WA-K1-K12 VERBATIM (G5). shape's RESULT carries either the
    executor CALL into the health-ai repo or an owner-approved child-split routing the parked domains back to TRIAGE.
  return: |
    RESULT with the shaped node/bet (state_changes to TREE/NOW), the executor CALL (or child-split decision),
    play_check, and next.
  budget: one focused shape session

END_OF_FILE: live/health/NOW.md
