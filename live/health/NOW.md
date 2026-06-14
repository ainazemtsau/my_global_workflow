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
    1 (Define) — converge-arch added NO new owner decision (all picks system-decided). NEXT = converge-verify
    (separate refutation session) → then shape. Assembly surface = work/converge-g-health-core.md.
    The paused nutrition Define + recon remain DIRTY input evidence, never authority.

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
    status: ready (separate refutation session — attack completeness with an independent oracle + trace every value)
    note: >
      Precondition met: converge (Define+Resolve) + converge-arch closed. converge-verify re-derives independently
      (does NOT read the deciding sessions' reasoning), authors a node-class decision-class checklist if none exists,
      and only a clean verify reaches shape.

decisions: []

next: |
  CALL c-health-core-converge-005
  to: session
  direction: health
  play: converge-verify
  node: g-health-core
  goal: |
    Refute the closed g-health-core spec before shape consumes it: attack (1) the question set is COMPLETE and
    (2) no answer leans on an unresolved question — with an INDEPENDENT oracle. Only a clean verify reaches shape.
  context: |
    RUN IN A FRESH CHAT (independence matters — do NOT read the deciding sessions' reasoning; re-derive).
    converge (Define+Resolve) + converge-arch are closed in work/converge-g-health-core.md: §GLOSSARY (signed),
    §WHAT-A (12 binding acceptance WA1–WA12), §WHAT-R (W1–W64), §WHAT-C + §CONTRACTS (CA1–CA7), §ARCH (Q1–Q6
    picks riding PLAN), §PLAN-AGENDA (P1–P22), §DEFERRED, §SIGNOFFs (Define, Resolve, converge-arch).
    Attack completeness with a THIRD source: AUTHOR the node-class decision-class checklist for an
    "LLM-managed provider-independent flat-file life-OS core" (knowledge/ has none yet — an empty oracle is a
    BLOCKED close, never auto-PASS), name it, propose it as canon; split every compound done_when criterion
    atomically and map each to a §WHAT row; trace every weight-bearing value/acceptance to a cited resolved row
    or frozen canon (untraceable = smuggled → bounce). Re-check the firewall. Watch the gap-hunt residual
    (write-path → PLAN P3) is named, not smuggled into done_when.
  boundaries: |
    Refute or pass only; never answer a question (a finding bounces a row back to converge/converge-arch).
    No raw daily data in Direction OS; no medical prescriptions. Same row bouncing twice → two-strikes, handoff.
  done_when: |
    Both refutations fail to find a hole (or every hole is bounced + a later verify passes);
    §SIGNOFF converge-verify passed; shape's CALL carries the §WHAT-A acceptance + §CONTRACTS rows to COPY into
    the executor done_when + the §PLAN-AGENDA (P1–P22) as the PLAN agenda. next = shape.
  return: RESULT with verify verdict (complete=PASS/FAIL, smuggling=PASS/FAIL), the authored decision-class
    checklist (proposed canon), and next CALL (shape) or a bounce CALL.
  budget: converge-verify movement (single refutation session)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
