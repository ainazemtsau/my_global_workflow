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
    anti-fragility binding) in work/converge-g-health-core-kernel.md; next = converge-arch →
    converge-verify → shape. No active bet until the kernel is shaped into a bet.

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
    status: ready
    note: >
      Architect the kernel's cross-cutting CONTRACTS on top of the signed data-layer CA1–CA9:
      the runtime primitives (working-state cursor; state-machine definition/cursor split; the
      single procedure-interpreter/router; the procedure registry) and the governance lifecycle
      as declared, consumer-driven contracts every domain inherits unchanged; close the KP1–KP12
      PLAN-agenda routing; no execution content; next → converge-verify (separate refutation),
      then shape.

recurring: []

decisions: []

next: |
  CALL c-health-core-kernel-converge-arch-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-core
  goal: |
    The kernel's cross-cutting CONTRACTS are architected on paper on top of the signed data-layer
    CA1–CA9: the runtime primitives (working-state cursor; state-machine definition/cursor split;
    the single procedure-interpreter/router; the procedure registry) and the governance lifecycle
    expressed as declared, consumer-driven contracts every domain (nutrition, training, future)
    inherits unchanged — so no domain reinvents the engine. Architecture-on-paper only; HOW rides
    the KP-agenda.
  context: |
    Owner-signed kernel WHAT: live/health/work/converge-g-health-core-kernel.md (§KW rows, §WA-K
    binding acceptance WA-K1–K12, §OWNER DECISIONS, §KERNEL-PLAN-AGENDA KP1–KP12, §COVERAGE).
    Signed data/contract layer to build ON (do not re-open): live/health/work/converge-g-health-core.md
    (CA1–CA9, the §ARCH picks Q1–Q6/AA1–AA3, P1–P27). Governance baseline:
    live/health/work/core-kernel-governance-lifecycle-spec.md. Owner decisions locked: Package A
    (F1–F16), B-1 (G7-2 by layer), B-2 (scaffolding), B-3 (domain graph owner-approved), B-4
    (anti-fragility binding).
  boundaries: |
    Extend the kernel; do NOT re-open or rebuild the signed data/contract layer or the owner
    decisions. No execution content (no real menu/recipe/grocery/program); no health-ai product
    edits. HOW magnitudes/schemas (KP1–KP12, P1–P27) ride PLAN as input evidence, never into
    done_when. Surface any NEW owner-owned contract fork; do not silently auto-decide.
  done_when: |
    Every kernel runtime + governance contract is declared (consumer, producer, flow, direction,
    trigger) with build-order deps; firewall clean (no HOW token in a flow); the KP-agenda routing
    is recorded; coverage vs the §KW rows complete; routed to converge-verify (separate refutation)
    before shape.
  return: |
    RESULT with the declared kernel contracts, any owner decisions (or none), state_changes, and
    next CALL (converge-verify).
  budget: one focused converge-arch session

END_OF_FILE: live/health/NOW.md
