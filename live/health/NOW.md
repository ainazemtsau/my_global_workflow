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
    design is preserved at work/core-kernel-governance-lifecycle-spec.md. No active bet
    until the kernel WHAT is converged and owner-approved.

tasks: []

open_calls:
  - id: c-health-core-kernel-converge-001
    status: ready
    note: >
      Converge the re-opened g-health-core at KERNEL scope (extend, do not rebuild the
      data/contract layer): runtime primitives + governance lifecycle, so nutrition and
      training attach as thin one-responsibility-per-procedure layers. Import the existing
      core WHAT and the governance spec; surface the 16 governance forks and the G7-2
      confirm-before-save reconciliation; no execution content; route to converge-arch.

recurring: []

decisions: []

next: |
  CALL c-health-core-kernel-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    g-health-core is extended into a provider-independent KERNEL that supplies reusable runtime
    primitives — per-domain memory/working-state, state machines, a single procedure-interpreter/
    router (each "term" = one bounded procedure the kernel runs), and a governance lifecycle
    (artifact SEED→PROPOSED→ACTIVE→SUPERSEDED + owner-approval gate + confirm-before-save +
    readable-for-owner presentation + writer/evidence-of-transition barrier + one-chat-one-job
    handoff) — so nutrition and training attach as thin one-responsibility-per-procedure layers
    and no domain reinvents the engine. An owner-approved kernel WHAT exists before any kernel
    build or domain rebuild.
  context: |
    Owner chose Variant 1 on 2026-06-20 (history/2026-06-20-s-health-core-kernel-reframe-001.md).
    RETROFIT converge: g-health-core already has a signed data/contract layer — IMPORT it, do not
    re-litigate it. Baselines to import / frame the open runtime layer against:
    - Existing core data/contract WHAT: live/health/work/converge-g-health-core.md (W1–W64,
      WA1–WA12, CA1–CA7) — born-closed where signed; the gap is the missing runtime layer.
    - Governance/lifecycle design to fold into the kernel:
      live/health/work/core-kernel-governance-lifecycle-spec.md (12 failure modes prevented,
      8 glossary terms, WHAT families, 16 owner forks F1–F16 + recommendations, residuals).
    - Owner architecture requirements R1–R8 (one procedure per term; single interpreter/router;
      kernel primitives memory/state-machine/launch/procedure-registry; layered dietitian-targets
      → menu → recipes → grocery; readable-for-owner + confirm-before-save; anti-fragile add/remove/
      fix a part independently; reuse for training; inspired by Direction OS).
    - Failure evidence: the nutrition saga (history 2026-06-13 … 2026-06-20) and the proof that
      nutrition reinvented its own engine (x_nutrition/workflow/*).
  boundaries: |
    Extend the core; do NOT rebuild or discard the working data/contract layer.
    No execution content (no real menu/recipe/grocery/program); no health-ai product-repo edits.
    Nutrition/training rebuild only AFTER the kernel WHAT is owner-approved.
    Do not silently override the signed G7-2 (decide-and-inform): surface the confirm-before-save
    change as an explicit owner decision (durable content gated; daily logging stays decide-and-inform).
    Surface, never auto-decide, the 16 governance forks F1–F16.
    Do not store raw daily data in Direction OS.
  done_when: |
    Owner has approved a kernel WHAT/structure defining: the runtime primitives (memory/working-state,
    state-machine object, single procedure-interpreter/router, procedure registry), the one-procedure-
    per-term decomposition + layering contract for thin domains, the governance lifecycle
    (SEED→PROPOSED→ACTIVE→SUPERSEDED + approval gate + confirm-before-save + readable-for-owner +
    writer/evidence barrier + one-chat-one-job handoff), and the anti-fragility/extension contract;
    the 16 governance forks and the G7-2 confirm-before-save reconciliation are resolved or routed to
    explicit owner decisions; no execution content produced; route to converge-arch.
  return: |
    RESULT with the owner-approved kernel WHAT, owner decisions, state_changes, and next CALL
    (converge-arch). No kernel build and no domain rebuild before the WHAT is signed.
  budget: one focused converge session

END_OF_FILE: live/health/NOW.md
