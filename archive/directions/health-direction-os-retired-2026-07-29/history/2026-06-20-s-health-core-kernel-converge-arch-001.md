# RESULT — s-health-core-kernel-converge-arch-001

direction: health
node: g-health-core (KERNEL scope)
play: converge-arch (heavy node, retrofit)
call: c-health-core-kernel-converge-arch-001
date: 2026-06-20

## outcome
The kernel's cross-cutting CONTRACTS are architected on paper on top of the signed data-layer CA1–CA9. The kernel
ENGINE — runtime primitives (single router/interpreter, working-state cursor, state-machine definition/cursor split,
procedure registry) + the governance lifecycle (status property, owner-approval gate, writer-applier barrier,
confirm-by-layer dispatch, render-before-decision gate, one-chat-one-job+handoff, provenance) + the engine invariants
(thin-domain attach, anti-fragility, cold-start+journey) — is declared as **14 consumer-driven contracts KC1–KC14**
that every domain (nutrition [parked], training [parked], future) inherits UNCHANGED, so no domain reinvents the engine
(the defect that got the nutrition slice rejected). 7 internal kernel seams (S1–S7) and a 3-tier build-order stack
(signed data layer → kernel runtime+governance → thin domains) are recorded. 4 high-risk architecture questions are
worked as refuted chains. converge-arch closes with **owner_gate_batch = []** (zero new owner gates), matching the
data-layer converge-arch precedent. Routed to converge-verify. Product: work/converge-g-health-core-kernel-arch.md.

## evidence (matching done_when)
- **Every kernel runtime + governance contract declared** (consumer, producer, flow, direction, trigger, build-order):
  KC1–KC14 in §KERNEL-CONTRACTS of the arch file. Producer = g-health-core kernel for all; consumers = all domains.
- **Firewall clean (no HOW token in a flow):** §FIREWALL verdict CLEAN; independent firewall attacker confirmed flows
  KC1–KC14 + seams S1–S7 are behavioral-WHAT only; signed WHAT-language that looks like HOW (YAML/KV21, trigger set/
  KG8, commit+diff+re-read/WA-K5, echoed-words+version+date/WA-K3) is not HOW; all magnitudes/schemas ride KP/P.
- **KP-agenda routing recorded:** §KP-ROUTING maps every KP1–KP12 + reused P-slots (P5/P11/P20/P21/P23/P25) to a
  contract/pick; no KP orphaned; no KP leaks into a WA-K/done_when line.
- **Coverage vs §KW rows complete:** all 90 normative §KW rows (KM1–11, KS1–10, KR1–13, KG1–9, KV1–21+KV-B2, KL1–10,
  KA1–10, KD1–5) have a contract home; WA-K1–K12 each carried. The adversarial completeness pass caught 5 rows missing
  from the authored kw_rows bindings (masked by a coverage-oracle numbering divergence) and BOUND them: KV6/KV7→KC6,
  KV8→KC9, KV12→KC7, KD2→KC1.
- **Architecture-on-paper, not done_when:** arch_open = 0; arch_in_context_only = PASS (no pick in any done_when; all
  ride PLAN as input evidence).
- **Routed to converge-verify** (separate refutation) before shape: §ROUTE + the next CALL.
- Assembly + verification: workflow wf_4eee70ff-ec6 (9 agents: declare + independent §KW-coverage oracle + 4
  architecture refuted-chains + 3 attackers). Two independent attackers corrected the draft.

## architecture picks (refuted chains; all system-decided, ride PLAN as input evidence)
- **KQ1 writer-applier locus** → SEPARATE context from the authoring chat (fresh session OR headless one-shot; both
  satisfy no-role-both + evidence-outside-producing-chat). Refuted: same-chat second pass (FM10/KS7/WA-K3), owner-commits
  (struck/W4), daemon (no-runtime/KR5/KG8). HOW → KP6. new_owner_fork: NO (F2 already signed).
- **KQ2 cold-start bootstrap recursion** → a kernel-owned UNIVERSAL bootstrap state-machine every domain starts in,
  whose sole output authors THIS domain's definition (PROPOSED → gate → ACTIVE). Refuted: ad-hoc in-chat (FM3),
  hardcode-per-domain (KA2/KG6/WA-K8/KL1), definition-ACTIVE-at-attach (KV2/WA-K4/FM5), empty-ACTIVE-placeholder
  (FM5/KV2). Forced by KD3 + KR10 + KL1/WA-K9 + KA6. new_owner_fork: NO.
- **KQ3 lifecycle vs state-machine** → ORTHOGONAL two axes joined by ONE one-way render-before-decision seam (INV-ORTH;
  internal seam S5). Refuted: unified machine (FM5/FM6), status-by-folder (FM12), shared alphabet (KL3/KS9). new_owner_fork: NO.
- **KQ-rev (miner gap-hunt) definition-reversion vs in-flight cursor** → impact-classified fail-closed re-validation:
  still-valid cursors proceed (WA-K8); orphaned cursors BLOCK-to-repair, rebuild from durable artifacts+handoff
  (KR4/KM2/KM7) under the readable owner-confirmed gate (KV21). "WHO authors the rebuilt position" is FORCED to
  system-proposes/owner-confirms by KM11 (cursor exempt) + KV20 (adjustment axis) + KV21 + KS6 + W21 — the miner's
  initial new-owner-fork (KD6) was DEMOTED to system-locked by two independent attackers. PLAN residual rides existing
  KP2 + KP10 (NOT minted as new KP slots into the signed agenda). new_owner_fork: NO.

## state_changes
- **work/converge-g-health-core-kernel-arch.md** (NEW product file): §SCOPE, §DECOMPOSE (sub-systems, sub-node NONE,
  seams S1–S7, 3-tier build stack), §KERNEL-CONTRACTS (KC1–KC14, 5 orphans bound), §KERNEL-ARCH (KQ1–KQ3 + KQ-rev),
  §KP-ROUTING, §FIREWALL/§COVERAGE, §SIGNOFF (CLOSED, owner_gate_batch=[]), §ROUTE → converge-verify.
- **NOW.md** active_bet.note: converge-arch CLOSED, 14 contracts + 4 picks, zero new gates, next = converge-verify.
- **NOW.md** open_calls: c-health-core-kernel-converge-arch-001 → done (with note); added
  c-health-core-kernel-converge-verify-001 → ready.
- **NOW.md** next: the converge-verify CALL (play: converge-verify).
- **NOW.md** decisions: unchanged ([] — no owner decision; converge-arch closed clean).
- **LOG.md**: appended the converge-arch line.
- **history/**: this RESULT.

## captures
- KQ-concurrent (two sessions opening the same domain cursor concurrently): largely absorbed by KM7 (handoff =
  single-open-card token) + git-merge surfacing the conflict loudly; no owner fork. Worth a one-line PLAN note at PLAN.
- KQ-rev orphan-cursor re-validation + definition-level re-version detection is a genuine new PLAN residual on KP2/KP10;
  PLAN may cut a dedicated slot if warranted (not stamped into the signed KP1–KP12 here).

## decisions_needed
NONE. converge-arch closed with owner_gate_batch = []. The only candidate fork the miner surfaced (orphan-cursor repair
authority, KD6) was refuted by two independent attackers as already-settled by signed rows (KM11+KV20+KV21+KS6+W21) and
demoted to a system-locked pick — surfacing it as a gate would have re-opened a signed row, which the play forbids.

## play_check
- **Step 1 Declare:** done — 14 consumer-driven contracts KC1–KC14 frozen before build, each with consumer/producer/
  flow/direction/trigger; completeness checked against the §KW rows (all 90 homed; 5 orphans bound after the adversarial
  pass); every consumed contract names its producer (the kernel) with an explicit build-order dependency; no HOW token
  in any flow. Contracts signed system-side (G7: owner_gate_batch=[], no owner-owned fork).
- **Step 2 Decompose:** done — kernel sketched into 10+ sub-systems; sub-node decision NONE (mirrors data-layer); 7
  internal seams S1–S7 recorded (WHAT side; HOW → PLAN); 3-tier build-order stack stated.
- **Step 3 Architect:** done — 4 high-risk questions (KQ1 writer-locus, KQ2 cold-start, KQ3 orthogonality, KQ-rev
  definition-reversion) worked as refuted chains (3–5 options each, signed-consistent pick); one miner gap-hunt ran
  ("which architecture question did we NOT ask?" → KQ-rev, with KQ-concurrent/KQ-pending-staleness/KQ-removed-stage
  surfaced and dispositioned). Picks signed system-side (G7); no pick leaked into done_when.
- **Step 4 Close & route:** done — closure verified; play_check emitted: `contract_coverage: every §KW row + WA-K → a
  §KERNEL-CONTRACTS entry` (PASS), `arch_open: 0`, `arch_in_context_only: PASS`. §SIGNOFF (Declare + Architect) exists.
  Set handed to converge-verify before shape. next = converge-verify.

## next
CALL c-health-core-kernel-converge-verify-001 — play: converge-verify, node: g-health-core. Refute the
§KERNEL-CONTRACTS (KC1–KC14) + §KERNEL-ARCH (4 picks) set in a FRESH session (G5): independent completeness oracle +
weight-bearing-value trace; verify the 5 bound orphan rows + the KQ-rev system-locked demotion; PASS → shape, else a
bounced close-and-re-verify list. (Full CALL in NOW.md → next.)

END_OF_FILE: live/health/history/2026-06-20-s-health-core-kernel-converge-arch-001.md
