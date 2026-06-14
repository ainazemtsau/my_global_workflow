RESULT s-health-core-converge-003 (call: c-health-core-converge-003)
direction: health   play: converge   node: g-health-core   movement: Resolve (§WHAT)

outcome: |
  Resolve built the cited §WHAT node-on-paper for g-health-core. A 4-slice workflow (wf_c4459fb4-86f)
  derived 127 rows from THREE sources (each done_when criterion; cross-node edges; recursive mechanism
  decomposition of imports I2/I3/I4/I6/I7 + committed mechanisms); an INDEPENDENT coverage oracle and a
  firewall/owner-gate auditor checked it. Consolidated to: 12 binding ACCEPTANCE criteria (§WHAT-A,
  shape copies verbatim into the executor done_when), W1–W64 requirements (§WHAT-R), CA1–CA7 cross-node
  contracts routed to converge-arch (§WHAT-C), and P1–P22 HOW magnitudes/formats firewalled → PLAN
  (§PLAN-AGENDA). Coverage: all 9 done_when criteria atomically split → ≥1 row; all named-mechanism
  imports decomposed; firewall clean (no HOW magnitude in any acceptance/WHAT line). OWNER GATE AT
  RESOLVE = NONE NEW: the auditor's owner_gate_batch = [] — every owner-relevant reading was already
  signed at Define (G7-1/2/3); the §WHAT is derived + system-decided evidence. Resolve therefore closes
  with a lightweight owner CONFIRM (ratification of §WHAT-A), not a new decision. Stopped at that confirm.

evidence: |
  work/converge-g-health-core.md: §WHAT — Resolve section added (§WHAT-A WA1–WA12; §WHAT-R W1–W64;
  §WHAT-C CA1–CA7; §PLAN-AGENDA P1–P22; §DEFERRED objective-recovery; §SIGNOFF Resolve = PENDING CONFIRM).
  Independent coverage oracle verdict: SUBSTANTIALLY COMPLETE; 4 reconcilable defects FIXED in the written
  spec — (1) +1 missing row W56 (menu = system-generated under research-and-decide); (2) 3 dup-merges with
  tags reconciled (protein-ref W19; safety-floor W22/W38; phase ownership/enum W34/W35); (3) 3 mis-deferred
  →G7 rows closed by the system per the signed readings (program-start W26, autonomy-dial W40, phase-enum
  W35). Firewall auditor: firewall_fixes = [] (clean). Workflow = wf_c4459fb4-86f (6 agents).

state_changes: |
  work/converge-g-health-core.md:
  - REPLACE the "§WHAT — Resolve / NOT STARTED" stub with the full §WHAT (§WHAT-A / §WHAT-R / §WHAT-C /
    §PLAN-AGENDA / §DEFERRED) and §SIGNOFF Resolve = PENDING OWNER CONFIRM.
  NOW.md:
  - active_bet note: Resolve built; owner gate at Resolve = none new; awaiting lightweight confirm, then converge-arch.
  - open_calls: c-health-core-converge-003 status -> done-pending-confirm.
  - decisions: add RESOLVE-CONFIRM (ratification of §WHAT-A; type = NOT a new decision; recommendation = confirm).
  - next: -> awaiting confirm; continuation CALL c-health-core-converge-004 (play converge-arch).
  LOG.md:
  - append the Resolve line.
  history/:
  - add 2026-06-14-s-health-core-converge-003.md (this RESULT).

captures:
  - The independent coverage oracle EARNED its place at Resolve too: it caught 1 genuinely-missing row
    (menu = system-generated) and, more importantly, 3 rows the deriving agents had mis-parked as fresh
    →G7-owner gates that the signed Define readings already CLOSE (program-start under G7-1; autonomy-dial
    under G7-2; phase-enum is system-locked). Without the auditor, Resolve would have manufactured a
    spurious owner gate — exactly the over-gating the owner objected to.
  - PLAN agenda is now a clean 22-item HOW list (P1–P22) for converge-arch/PLAN; CA1–CA7 are the
    cross-node contracts for converge-arch (distinct from PLAN magnitudes).
  - Objective recovery metrics (HRV/RHR/sleep-device) remain DEFERRED pending a clean-evidence pass.

decisions_needed:
  - id: RESOLVE-CONFIRM
    type: ratification (owner_gate_batch was empty — NOT a new owner decision)
    question: Confirm the §WHAT, specifically the 12 binding acceptance criteria (§WHAT-A WA1–WA12) that
      shape copies verbatim into the executor done_when. Everything derives from the Define signoff +
      system-decided evidence; flag any criterion to fix, else confirm to route to converge-arch.
    recommendation: confirm

play_check:
  - 3 Resolve: DONE — flat cited §WHAT built from the three sources; every weight-bearing row carries an
    inline citation; mechanism decomposition of I2/I3/I4/I6/I7 recursive; acceptance rows tagged; HOW
    firewalled → PLAN. SIGN sub-step (owner) is a CONFIRM/ratification — AWAITING (owner_gate_batch empty;
    §SIGNOFF Resolve unwritten until the owner confirms).
  - 4 Close & route: routed — next = converge-arch (c-health-core-converge-004) on confirm.
  - converge_coverage: all 9 done_when criteria → ≥1 §WHAT row (independent oracle); all named-mechanism
    imports I2/I3/I4/I6/I7 + e1RM/EMA/expenditure/protein/floor decomposed; forward-clean (open/deferred
    rows are all legitimate HOW→PLAN or converge-arch forks, none a system gap); backward-clean (every
    weight-bearing row cited; 4 oracle defects fixed).
  - firewall: PASS (no HOW magnitude in any acceptance/WHAT line; firewall_fixes = []).
  - owner_gates_spent: 1 of <=3 across the converge set (Define). Resolve adds NO new owner decision
    (ratification only); converge-arch may use the rest.

log: "converge g-health-core (Resolve): §WHAT built (12 binding acceptance + W1–W64 + CA1–CA7 + P1–P22),
  independent coverage oracle (all 9 done_when + mechanism imports covered, firewall clean, 4 defects
  fixed); owner gate at Resolve = NONE NEW; awaiting lightweight confirm, then converge-arch."

next: |
  awaiting owner CONFIRM of §SIGNOFF Resolve (RESOLVE-CONFIRM — ratification of §WHAT-A, not a new decision).
  On confirm, a fresh session writes §SIGNOFF Resolve with the owner's words and runs converge-arch:
  CALL c-health-core-converge-004
  to: session
  direction: health
  play: converge-arch
  node: g-health-core
  goal: |
    Close cross-node CONTRACTS (CA1–CA7) as consumer-driven contracts and, heavy, work the high-risk
    architecture as a refuted chain into an architecture-on-paper that rides PLAN as input evidence.
    Then route to converge-verify.
  context: |
    Fresh chat. converge (Define+Resolve) closed: work/converge-g-health-core.md has §GLOSSARY (signed),
    §WHAT-A (12 binding acceptance), §WHAT-R (W1–W64), §WHAT-C (CA1–CA7), §PLAN-AGENDA (P1–P22). First:
    write §SIGNOFF Resolve with the owner's confirm words. Then close CA1–CA7; HOW magnitudes stay → PLAN.
  boundaries: |
    Import nothing new as authority; auto-fill nothing. No raw daily data in Direction OS; no medical
    prescriptions. Architecture-on-paper rides PLAN as input evidence only — never into done_when.
  done_when: |
    §CONTRACTS: every TREE interaction has an entry; no dangling consumed contract; no HOW token; §SIGNOFF
    for Declare (+ heavy Architect); next = converge-verify.
  return: RESULT with §CONTRACTS (+ arch-on-paper), §SIGNOFFs, and next CALL (converge-verify).
  budget: converge-arch movement (may span sessions; owner gates batched ≤3 across the set, 1 spent)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/history/2026-06-14-s-health-core-converge-003.md
