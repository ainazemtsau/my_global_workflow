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
    Direction OS — a cross-repo contract for converge-arch). Assembly surface =
    work/converge-g-health-core.md (§SIGNOFF Define). NEXT = Resolve (§WHAT). The paused nutrition
    Define + recon remain DIRTY input evidence, never authority.

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
    status: in-flight (Resolve — §WHAT)
    note: >
      Build the cited §WHAT on the SIGNED readings (G7-1 A; G7-2 ask-freely-but-non-blocking;
      G7-3 one-way visibility). Three-source derivation + recursive mechanism decomposition of
      I2/I3/I4/I6/I7. Then converge-arch. Owner gates: 1 of ≤3 spent.

decisions: []

next: |
  CALL c-health-core-converge-003
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    Run Resolve — build the cited §WHAT node-on-paper for g-health-core from THREE sources (each
    done_when criterion; each cross-node edge; recursive mechanism decomposition of I2/I3/I4/I6/I7 +
    every committed mechanism), tag acceptance rows, firewall HOW→PLAN, then route to converge-arch.
  context: |
    RUN IN A FRESH CHAT. Define is SIGNED — surface at work/converge-g-health-core.md (§SIGNOFF Define +
    §GLOSSARY A ✅ SIGNED, B system-locked, C charter-locked, D undisputed-named). Build §WHAT on the
    SIGNED readings: G7-1 A membership test; G7-2 amended = ask-freely BUT non-blocking +
    graceful-default-on-decline + no-re-pester (a SYSTEM-WIDE invariant on parse/clarify/setup/review) +
    decide-and-inform + review-proposes + conservative-default on safety brakes; G7-3 = one-way
    visibility (Direction OS reads all Health AI; Health AI zero-reference to Direction OS; raw
    owned/stored in Health AI). System-locked readings (§GLOSSARY B) feed Resolve directly;
    converge-verify refutes them later. PLAN-agenda pre-seeded in the converge-001 captures
    (resolve-on-read vs materialize; EMA window; carb tiers; FDC schema; registry-line syntax).
    FIRST: if the owner flags any echo (R2–R5 in §SIGNOFF) as misread, correct it before building §WHAT.
  boundaries: |
    Import nothing new as authority; auto-fill nothing. Owner gates: 1 of ≤3 spent (Resolve +
    converge-arch share the rest). No raw daily data stored in Direction OS; no medical prescriptions.
  done_when: |
    §WHAT closed (forward-clean: no open/deferred; backward-clean: every weight-bearing line +
    acceptance + glossary row cited); converge_coverage complete; §SIGNOFF Resolve; next = converge-arch.
  return: |
    RESULT with the closed §WHAT surface, §SIGNOFF Resolve, decisions_needed (if any remaining gate),
    and next CALL (converge-arch).
  budget: converge Resolve movement (may span sessions; owner gates batched ≤3 across the set, 1 spent)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/NOW.md
