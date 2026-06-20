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
    data-layer precedent). next = converge-verify, then shape. No active bet until the kernel is shaped into a bet.

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
    status: ready
    note: >
      Refute the kernel §KERNEL-CONTRACTS (KC1-KC14) + §KERNEL-ARCH (4 picks) set in a FRESH session
      (separate refutation, G5): completeness vs §KW + WA-K1-K12; firewall re-sweep; build-order non-dangling;
      no architecture pick leaked into a done_when; the 5 just-bound orphan rows (KV6/KV7->KC6, KV8->KC9,
      KV12->KC7, KD2->KC1) verified homed; the KQ-rev "who authors the rebuilt cursor" system-locked demotion
      re-refuted. Clean verify -> shape.

recurring: []

decisions: []

next: |
  CALL c-health-core-kernel-converge-verify-001
  to: session
  direction: health
  play: converge-verify
  node: g-health-core
  goal: |
    The kernel converge SET is refuted clean in a FRESH session (G5, separate from the one that produced
    it): the §KERNEL-CONTRACTS (KC1-KC14) + §KERNEL-ARCH (4 picks) hold up against an independent
    completeness oracle and a weight-bearing-value trace, so only a clean set reaches shape.
  context: |
    converge-arch product to refute: live/health/work/converge-g-health-core-kernel-arch.md (KC1-KC14,
    seams S1-S7, KQ1-KQ3 + KQ-rev, §KP-ROUTING, §FIREWALL/§COVERAGE, §SIGNOFF owner_gate_batch=[]).
    Signed kernel WHAT (born-closed, do not re-open): live/health/work/converge-g-health-core-kernel.md
    (§KW rows, §WA-K1-K12, §OWNER DECISIONS Package A + B-1..B-4, KP1-KP12). Signed data layer (do not
    re-open): live/health/work/converge-g-health-core.md (CA1-CA9, P1-P27). Governance baseline:
    live/health/work/core-kernel-governance-lifecycle-spec.md. The first converge-arch already ran a
    3-attacker in-session pre-pass (workflow wf_4eee70ff-ec6) that bound 5 orphan rows and demoted one
    over-called owner fork; the BINDING G5 pass is THIS fresh session.
  boundaries: |
    Refute only; do NOT re-open the signed WHAT/data-layer/owner decisions or re-litigate signed forks.
    No execution content; no health-ai product edits. Verdict is PASS or a bounced should-fix/blocker list
    to close then re-verify (mirroring the data-layer §VERIFY-1 -> §VERIFY-2). HOW residuals stay on the
    KP/P agenda, never into done_when.
  done_when: |
    Independent completeness check (every §KW row + WA-K1-K12 has a contract home; no domain-inheritance
    flow uncovered; the 5 bound orphan rows verified; build-order non-dangling) AND a traceability trace
    (no contract/pick leans on an unresolved question; no HOW token in a flow; no pick leaked into
    done_when; the KQ-rev system-locked demotion holds) both PASS -> §SIGNOFF converge-verify; else a
    bounced list. Clean -> shape (shape copies §WA-K1-K12 verbatim into the executor done_when).
  return: |
    RESULT with the verify verdict (PASS or bounced list), state_changes, and next CALL (shape on PASS,
    else a close-and-re-verify CALL).
  budget: one focused converge-verify session

END_OF_FILE: live/health/NOW.md
