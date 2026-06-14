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
    "CONFIRM"): §WHAT closed and binding (12 acceptance criteria + W1–W64 + P1–P22). CONVERGE-ARCH DONE
    (2026-06-14): §CONTRACTS CA1–CA7 closed (consumer-driven; all TREE interactions covered; build-order deps
    for the parked modules) + §ARCH architecture-on-paper (Q1–Q6 refuted chains → picks: pure resolve-on-read,
    read-only git/connector, one-entity-per-file, additive namespaced extension, two extension classes,
    one-entity-commit+lint-barrier write-path; ride PLAN, refuted by converge-verify). Owner gates spent: still
    1 (Define) — converge-arch added NO new owner decision (all picks system-decided). CONVERGE-VERIFY done
    (2026-06-14): pass1 caught real holes (blockers DC17 versioning/migration + DC3 rounding, + should-fix
    cluster, all system-decidable), closed them (W65–W79 + firewall fixes + P23–P27), pass2 = verify=PASS,
    firewall clean. **CONVERGE SET COMPLETE + refuted-clean** (Define+Resolve+converge-arch+converge-verify).
    NEXT = shape (turn the spec into a committed bet; owner-approved appetite/kill_by/tasks). Assembly surface =
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
    status: done (Resolve §SIGNOFF applied + CA1–CA7 contracts closed + §ARCH Q1–Q6; verifier PASS; no new owner gate)
    note: >
      §CONTRACTS + §ARCH at work/converge-g-health-core.md. owner_gate_batch = []; architecture-on-paper rides
      PLAN as input evidence. Reconciled an agent's partial §CONTRACTS write to the authoritative CA1–CA7.
  - id: c-health-core-converge-005
    play: converge-verify
    node: g-health-core
    status: done (pass 1 bounced B1–B14 → all closed system-decided → pass 2 verify=PASS; §SIGNOFF converge-verify passed)
    note: >
      Independent 21-class oracle. Pass1: traceability PASS, completeness FAIL (blockers DC17 versioning/migration,
      DC3 rounding) + firewall FAIL + should-fix cluster — all SYSTEM-DECIDABLE. Closed as W65–W79 + WA3-note +
      §ARCH AA1–AA3/CA8–CA9 + P23–P27 + 5 firewall rewrites (no new owner gate). Pass2 (wf_883c7f32-050):
      verify=PASS, firewall clean, still_open=[]. CONVERGE SET COMPLETE + refuted-clean → ready for shape.
      Decision-class checklist (DC1–DC21) proposed as knowledge/ canon (promote at review/pulse).

decisions: []

next: |
  CALL c-health-core-shape-001
  to: session
  direction: health
  play: shape
  node: g-health-core
  goal: |
    Turn the converged, refuted-clean g-health-core spec into a committed BET: appetite + kill_by + ≤3 tasks,
    a cut list (≥1 real cut), a lens sweep verdict, and a task testing the riskiest assumption (G6). Shape may
    split g-health-core into child nodes (G9), each re-entering TRIAGE. The executor CALL is emitted by shape, not here.
  context: |
    RUN IN A FRESH CHAT. converge for g-health-core is COMPLETE + refuted-clean (work/converge-g-health-core.md:
    §GLOSSARY signed, §WHAT-A WA1–WA12 + pass-2 acceptance W69/W70/W72/W73/W74, §WHAT-R W1–W79, §CONTRACTS CA1–CA9,
    §ARCH Q1–Q6 + AA1–AA3, §PLAN-AGENDA P1–P27, §SIGNOFFs Define/Resolve/converge-arch/converge-verify=PASS).
    BINDING by G5 — shape COPIES into the executor done_when: the §WHAT-A acceptance criteria WA1–WA12 + the pass-2
    acceptance rows (W69 minimum-viable-data, W70 red-flag-halt, W72 slug-immutability, W73 core-only-buildable,
    W74 cold-start-reduced-mode) and the §CONTRACTS CA1–CA9. CARRY as PLAN-agenda + architecture-on-paper input
    evidence: §PLAN-AGENDA P1–P27 + §ARCH Q1–Q6/AA1–AA3 (PLAN owns the binding ADRs; never into done_when).
    Build at the product repo health-ai (DIRTY — cleared + rebuilt in place at build time; explicit owner
    confirmation required before the wipe). Owner gates: 1 of the converge set spent (Define); shape's bet
    commitment (appetite/kill_by/tasks, G6) + any tree split (G9) are owner-approved.
  boundaries: |
    One active bet (G1). Appetite set before tasks + never extended (G3). No raw daily data in Direction OS;
    no medical prescriptions. The product-repo wipe needs explicit owner confirmation.
  done_when: |
    A shaped bet on g-health-core (appetite, kill_by, ≤3 tasks, cut list ≥1, lens sweep, riskiest-assumption task),
    owner-approved (G6/G9); the executor CALL carries the copied acceptance + contract done_when + the PLAN agenda.
  return: RESULT with the shaped bet (or tree split), owner approval, and the next CALL (executor/work or PLAN).
  budget: one shape movement
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
