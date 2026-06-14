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

    CONVERGE g-health-core IN PROGRESS (2026-06-14): Define DONE + §SIGNOFF applied. Node typed HEAVY,
    7 owner-approved decisions imported born-closed (I1–I7), ~30-term disputed glossary built +
    partitioned owner-vs-system, ~28 expert readings system-locked, safety floor charter-locked.
    Owner signed the 3 batched G7 (2026-06-14): G7-1 = A (research-and-decide membership test); G7-2 =
    A's drive posture but ASKING amended — system may ask freely yet every question is NON-BLOCKING
    with a graceful default on decline and no re-pestering (a system-wide invariant); G7-3 = REFRAMED
    to a ONE-WAY visibility (Direction OS reads ALL of Health AI; Health AI carries zero reference to
    Direction OS — a cross-repo contract for converge-arch). RESOLVE built + owner-CONFIRMED (2026-06-14,
    "CONFIRM"): §WHAT closed and binding — 12 acceptance criteria + W1–W64 + CA1–CA7 contracts-for-arch +
    P1–P22 PLAN-agenda (§SIGNOFF Resolve written). CONVERGE-ARCH IN PROGRESS: closing the 7 cross-node
    contracts (CA1–CA7) + heavy architecture. Owner gates spent: 1 (Define). Assembly surface =
    work/converge-g-health-core.md. The paused nutrition Define + recon remain DIRTY input evidence, never authority.

tasks: []

recurring: []

open_calls:
  - id: c-health-core-converge-001
    play: converge
    node: g-health-core
    status: done (Define complete + §SIGNOFF applied 2026-06-14)
    note: >
      Heavy-node converge Define + owner gate. Surface at work/converge-g-health-core.md (§SIGNOFF Define).
  - id: c-health-core-converge-003
    play: converge
    node: g-health-core
    status: done (Resolve §WHAT built + owner-confirmed "CONFIRM" 2026-06-14; §SIGNOFF Resolve written)
    note: >
      §WHAT closed + binding at work/converge-g-health-core.md (§WHAT-A 12 acceptance, §WHAT-R W1–W64,
      §WHAT-C CA1–CA7, §PLAN-AGENDA P1–P22). Owner gate at Resolve = none new.
  - id: c-health-core-converge-004
    play: converge-arch
    node: g-health-core
    status: in-flight (closing CA1–CA7 contracts + heavy architecture)
    note: >
      Consumer-driven contracts for CA1–CA7 + high-risk architecture as a refuted chain → architecture-on-paper
      riding PLAN. HOW magnitudes stay → PLAN (P1–P22). Owner gates: 1 of ≤3 spent; contract/arch picks may use the rest.

decisions: []

next: |
  awaiting owner CONFIRM of §SIGNOFF Resolve (RESOLVE-CONFIRM above — a ratification of §WHAT-A, not a new
  decision). On confirm, a fresh session writes §SIGNOFF Resolve with the owner's words and runs converge-arch:

  CALL c-health-core-converge-004
  to: session
  direction: health
  play: converge-arch
  node: g-health-core
  goal: |
    Close the cross-node CONTRACTS (§WHAT-C CA1–CA7) and, heavy, work the high-risk architecture as a refuted
    chain into an architecture-on-paper that rides PLAN as input evidence. Then route to converge-verify.
  context: |
    RUN IN A FRESH CHAT. converge (Define + Resolve) is closed: work/converge-g-health-core.md has §GLOSSARY
    (signed), §WHAT-A (12 binding acceptance), §WHAT-R (W1–W64), §WHAT-C (CA1–CA7), §PLAN-AGENDA (P1–P22).
    converge-arch closes CA1–CA7 as consumer-driven contracts (one-way Direction OS↔Health AI visibility;
    resolve-on-read layout; {phase,week,day} carrier; module attach-point + x_<domain>_* consume; day_type
    provenance; nutrition-as-template recursion; core parse/library/extensibility contract) and works the heavy
    architecture questions. HOW magnitudes stay → PLAN (P1–P22). Owner gates: 1 of ≤3 spent (Define); a contract
    sign-off and/or architecture picks may use the rest, batched.
  boundaries: |
    Import nothing new as authority; auto-fill nothing. No raw daily data in Direction OS; no medical
    prescriptions. Architecture-on-paper rides PLAN as input evidence only — never into done_when.
  done_when: |
    §CONTRACTS: every TREE interaction has an entry; no dangling consumed contract; no HOW token; §SIGNOFF for
    Declare (+ heavy Architect); next = converge-verify.
  return: RESULT with §CONTRACTS (+ arch-on-paper), §SIGNOFFs, and next CALL (converge-verify).
  budget: converge-arch movement (may span sessions)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
