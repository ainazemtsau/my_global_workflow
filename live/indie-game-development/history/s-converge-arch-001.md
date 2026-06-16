# s-converge-arch-001 — converge-arch (g-9c41 Wave-2 contracts): declared the §WHAT-B cross-node + internal seams as consumer-driven observable contracts

- **date:** 2026-06-16
- **play:** converge-arch (heavy + sibling-bearing → DECLARE + DECOMPOSE + ARCHITECT)
- **node:** g-9c41 (Wave 2 scope)
- **CALL applied:** c-converge-002 (to: session)
- **role:** session → became its own writer after RESULT (agent-CLI on this repo)
- **products:** work/converge-g-9c41.md (+ §CONTRACTS / §SIGNOFF / play_check), work/converge-g-9c41-arch.md (NEW)

## Opening contract (recap)

Heavy + sibling-bearing → DECLARE (consumer-driven observable contracts for every §WHAT-B edge + the internal
grid↔gas + cross-layer seams; HOW→PLAN; completeness checked against the TREE; dangling producers named) +
DECOMPOSE (the 6 §3.9 components; internal seams → internal contracts) + a LIGHT ARCHITECT (the heavy
architecture-on-paper = brief v2 ARCH-1v2, imported born-closed, rides PLAN as input evidence — NOT re-run).
Boundaries honored: Wave 1 CLOSED; d-converge-001 = A (not re-asked); LOCK / C1–C22 / t-2 artifacts untouched;
no HOW magnitude decided; shape not launched; state written only via this RESULT.

## How the set was built + hardened (a 15-agent in-session pre-pass)

- **wf_c4e09962-08f** — 6 contract-family drafters (ingestion / grid↔gas / B31 oracle / gas-type seam / render
  seam / completeness sweep) → an adversarial FIREWALL per family (HOW-leak / consumer-observability / dangling-
  producer / does-it-bound-the-magnitude / LOCK-reopen) → 3 cross-cutting critics (completeness+dangling /
  firewall / B31-crosscut+consumer-driven). The contracts were authored folding this against my own reading, so
  the set is not a single-author artifact. This is an IN-SESSION pre-pass (same-session helpers); the BINDING
  independent refutation is the separate converge-verify session (the next CALL).
- Fixes folded: render-RN1 inlined-B31-formula → reference-by-name; render-RN4 "60-class" FPS leak → PLAN;
  ingestion-IN1 "byte-identical ids" → "logically identical"; ingestion-IN2 white-box → black-box conformance;
  gas-GT2 "per-cell packing" → "packing density"; gas-GT5 made the I12-removed-vs-parked supersede explicit;
  completeness-CS1 "lockstep-broadcast" → PLAN; the self-play lane reclassified as g-9c41-internal (carried by
  OR3+GT2), not a cross-node contract; the breach-portal canon deduped (GG3 = CS1 = one G:topology-change[breach]).
- The critics' biggest catch = a WHITE SPOT: done_when #10's own gas↔temperature cross-layer interaction seam +
  the layer-registry "new layer plugs in without core edits" extensibility had NO contract (the first draft was
  gas-centric; GT4 EventPlane is the OUTBOUND gameplay plane, a different edge). Added XL1 (multi-layer
  consistency; obligation = both-layers-together, decided on done_when #10 + ADR-0004 §T12 + RESOLVED-1) + XL2
  (whole-layer registry, distinct from the gas-domain species handler GT1).

## RESULT

```yaml
RESULT s-converge-arch-001 (call: c-converge-002)
direction: indie-game-development   play: converge-arch   node/task: g-9c41 (Wave-2 scope; CHECKPOINT)
outcome: |
  g-9c41's §WHAT-B cross-node edges + the internal grid↔gas + cross-layer seams are now declared as
  CONSUMER-DRIVEN OBSERVABLE contracts (work/converge-g-9c41.md §CONTRACTS), so the open→PLAN stream/sim
  magnitudes can be frozen against contracts that already constrain them. Families: IN (replaceable ingestion
  adapter / TopologyDocument — IN1 data/shape, IN2 adapter-replaceability, IN3 transport-vendor swap), GG
  (grid↔gas internal — GG1 topology-change feed, GG2 geometry/band sovereignty split, GG3 real-breach→vertical-
  portals, GG4 band-handoff support), OR (the ONE normative B31 field-sampling/ExposureQuery oracle — OR1 single-
  oracle sampling, OR2 thinnest-open-level resolution, OR3 ExposureQuery = volume integral, OR4 player-near
  seeding agrees on entry; all THREE consumers g-7e15/g-d3a8/g-9c41 sample one oracle), XL (the done_when-#10
  WHITE SPOT the miner gap-hunt caught — XL1 cross-layer multi-layer consistency, XL2 whole-layer registry
  extensibility), GT (gas-type seam, consumer g-d3a8 — GT1 handler seam, GT2 data-alone config, GT3 reaction
  registry, GT4 event plane, GT5 flagship custom-driver+exclusions; B6 self-play reclassified internal), RN
  (render seam, consumer g-7e15 — RN1 read-model+swap, RN2 derivation+blind-check, RN3 visual params, RN4 shared
  frame budget), CS (completeness — CS1 external breach edge dangling:destruction-consumer, CS2 co-op-roles G7
  row, B15–B26 honestly classified as acceptance/milestone, not data contracts). Every contract states the
  observable in behavioral terms with all HOW (push/poll, wire format, cadence, layout, magnitudes) routed
  →PLAN; NONE re-opens the LOCKED Wave-1 foundation (ADR-0004 §LOCK + ADR-0003 v2 C1–C22) — firewall-verified.
  The heavy architecture-on-paper (ARCH-1v2, brief v2) is imported born-closed and rides PLAN as input evidence
  (work/converge-g-9c41-arch.md) — no pick leaked into done_when. The band-handoff contract strength (GG4/OR4)
  is OWNER-SIGNED in-session (voice): loose spatial precision + exact source/emitter tracking + coarse tier =
  source of truth + a FIRM no-shimmer-on-handoff requirement. The set is a checkpoint product handed to the
  separate converge-verify session before shape consumes it.
evidence: |
  - work/converge-g-9c41.md gains §CONTRACTS (IN/GG/OR/XL/GT/RN/CS, ~24 contracts + honest non-contracts) +
    §SIGNOFF (incl. §SIGNOFF-BH band-handoff owner-signed, echoing the owner's voice) + a converge-arch play_check.
  - work/converge-g-9c41-arch.md (NEW): the ARCHITECT record — ARCH-1v2 imported born-closed (rides PLAN); a
    table of the 4 emergent contract-architecture high-risk questions (Q1 B31 cross-tier composition, Q2 multi-
    layer consistency, Q3 layer-registry extensibility, Q4 band-handoff strength) + their disposition; the miner
    gap-hunt result (the XL1/XL2 white spot); §SIGNOFF Architect. arch_in_context_only: PASS.
  - contract_coverage: every TREE g-9c41 interaction (B1–B31 + the internal grid↔gas + cross-layer seams) maps to
    a §CONTRACTS entry or an honest non-contract classification; build-order named for every produced-now-
    consumed-later / dangling edge (CS1 dangling:destruction-consumer named, not dropped).
  - firewall: the 3 cross-cutting critics confirmed (after fixes) no HOW token in any contract's observable_spec/
    acceptance_property, the B31 single-oracle invariant holds with the render seam REFERENCING (not duplicating)
    it, and no contract re-opens the LOCK. Hardening pass wf_c4e09962-08f (15 agents, ~1.17M tokens).
state_changes: |
  PRODUCTS (not state): work/converge-g-9c41.md += §CONTRACTS + §SIGNOFF(converge-arch) + play_check(converge-
    arch); + work/converge-g-9c41-arch.md (the ARCHITECT record). These are removable assembly/product surfaces,
    not state.
  NOW.md: open_calls — c-converge-002 status queued → checkpoint (converge-arch DECLARE done; note updated);
    ADD c-converge-verify (ready, the next converge-track CALL). decision_inbox += d-bandhandoff-001 (answered —
    band-handoff strength, owner voice). active_bet, active_tasks ([]), c-shape-wave2, c-map-003, and NOW.next
    (= c-shape-wave2) are UNTOUCHED — converge-arch is a PARALLEL refinement that FEEDS the Wave-2 shape, it does
    not gate the bet spine (d-converge-001 = A; the converge track lives in open_calls, not NOW.next).
  LOG.md: += one converge-arch line → history/s-converge-arch-001.md.
  history/: + s-converge-arch-001.md (this RESULT).
  No TREE.md / CHARTER.md change (G9 — no tree/charter edit this leg). knowledge/ untouched: two-sided contract
    canon is PROPOSED only (review/pulse promote — authorship rule).
captures:
  - "canon_proposed (review/pulse → knowledge/, two-sided read_by both nodes): G:topology-change (+[breach],
     read_by TopologyCore+GasDomain+destruction-consumer); IGasReadModel single-oracle invariant + point-
     resolution(thinnest-open-level) + ExposureQuery=volume-integral + band-handoff-continuity (read_by g-9c41+
     g-7e15+g-d3a8 — the highest-value cross-cutting invariant, promote as the IGasReadModel oracle canon);
     G:cross-layer-consistency + G:layer-registry-extensibility (read_by FieldFabric+GasDomain+future layers);
     G:meta-gas-seam / G:gas-config-acceptance / G:reaction-intensive / G:event-plane / G:gas-exclusions-dayone
     (read_by g-9c41 seam owners + g-d3a8); the IN/RN canon lines (read_by g-9c41 + DA/PGG / g-7e15)."
  - "Parked-sibling owner forks declared with DEFAULTS (owner may override at the sibling's own converge, NOT a
     Wave-2 fork): GT5 agent-substrate = single field pathway (I12/R5); RN2 menace-motion = strict derivation
     (crit-6 default); RN4 sim/visual frame-budget boundary owner = g-9c41 owns sim-side + names the boundary
     (A1.7). Surface at g-d3a8 / g-7e15 converge."
  - "Wave-2 shape inputs from this leg: (1) crit-10 tightening is now contracted — XL1 wants a FEEDBACK cross-
     layer interaction (not a sink) + XL2 wants a 3rd DEMONSTRATIVE layer actually plugged in (currently argued,
     not exercised); fold into c-shape-wave2's done_when. (2) the band-handoff 3-tier prep-window is the owner's
     HINT, not a locked mechanism — PLAN owns it; the owner flagged it «охренеть как важно» and open to deeper
     tightening in-shape."
  - "first-run note for converge-design.md: the heavy ARCHITECT step, when the architecture-on-paper already
     exists as a prior research product (brief v2), correctly REDUCES to import-born-closed + work only the
     EMERGENT contract-architecture questions — the play's 26-agent-style architecture pass is NOT re-run. The
     miner gap-hunt still earned its keep (caught the done_when-#10 cross-layer white spot the contract families
     missed). Candidate os/docs note (not fixed here; maintenance-gated)."
decisions_needed: []
  # The one genuine Wave-2-shaping fork (band-handoff strength) was SIGNED in-session by the owner (voice,
  # d-bandhandoff-001 / §SIGNOFF-BH). XL1 cross-layer consistency was DECIDED on done_when #10 + the LOCK (not an
  # open fork). The 3 parked-sibling forks were declared with defaults + deferred to the siblings' own converge
  # (captures), so nothing blocks here.
play_check:
  - "1 declare: done — §CONTRACTS: every TREE interaction (B1–B31 + internal grid↔gas + cross-layer seams) → a
     consumer-driven observable contract or an honest non-contract classification; HOW→PLAN; dangling producers
     named (CS1); two-sided canon proposed; no LOCK re-open (firewall-verified)."
  - "2 decompose (heavy): done — the 6 §3.9 components sketched; internal seams → internal contracts (GG1–GG4,
     XL1–XL2); GT1 (gas-domain species handler) separated from XL2 (FieldFabric whole-layer registry)."
  - "3 architect (heavy): done — ARCH-1v2 imported born-closed (rides PLAN, work/converge-g-9c41-arch.md); 4
     emergent contract-architecture questions worked observable-first (Q1 OR1 / Q2 XL1 / Q3 XL2 / Q4 GG4-OR4);
     one miner gap-hunt caught the XL1/XL2 white spot; picks signed (Q4 owner-voice; Q2/Q3 on #10+LOCK; Q1 via
     the contract). No pick in done_when."
  - "4 close & route: CHECKPOINT — contract_coverage PASS (every TREE interaction → a §CONTRACTS entry);
     arch_open 0; arch_in_context_only PASS; §SIGNOFF exists for Declare (BH owner-signed) + Architect. next =
     converge-verify (independent refutation) → then c-shape-wave2 consumes the verified contracts."
  - "owner steps (G7): band-handoff strength SIGNED in-session (owner voice, echoed in §SIGNOFF-BH /
     d-bandhandoff-001); cross-layer consistency decided on done_when #10 + the LOCK; 3 parked-sibling forks
     declared with defaults + deferred. Decisions batched, never scattered."
log: "2026-06-16 — converge-arch (g-9c41 Wave-2 contracts, c-converge-002): declared §WHAT-B + internal seams as consumer-driven observable contracts (IN/GG/OR/XL/GT/RN/CS) in work/converge-g-9c41.md §CONTRACTS + ARCHITECT record work/converge-g-9c41-arch.md (ARCH-1v2 imported born-closed). HOW→PLAN; nothing re-opens LOCK/C1–C22. 15-agent pre-pass (wf_c4e09962-08f) — biggest catch = WHITE SPOT: done_when #10's gas↔temperature cross-layer seam + layer-registry extensibility had no contract → added XL1/XL2. Owner SIGNED band-handoff (voice: loose spatial + exact source-tracking + coarse=truth + FIRM no-shimmer). Parked-sibling forks defaulted+deferred. Parallel refinement — bet/c-shape-wave2 untouched. next = converge-verify. → history/s-converge-arch-001.md"
next: |
  CALL c-converge-verify
  to: session
  direction: indie-game-development
  play: converge-verify
  node: g-9c41 (Wave-2 contract set)
  goal: |
    A FRESH-session independent refutation establishes that the §CONTRACTS set for g-9c41 Wave 2 is
    COMPLETE and that no contract leans on an unresolved question or leaks a HOW — so a clean verify gates
    the Wave-2 shape consuming the contracts. Attack "the set is complete" with an INDEPENDENT oracle (a
    networked-sim contract-class checklist + compete precedents — NOT the brief/converge sources this leg
    used), and "no contract smuggles a HOW or leans on an open question" by tracing each weight-bearing
    observable + each →PLAN routing.
  context: |
    - work/converge-g-9c41.md §CONTRACTS (IN/GG/OR/XL/GT/RN/CS) + §SIGNOFF (incl. §SIGNOFF-BH owner-signed
      band-handoff) + play_check (converge-arch pass).
    - work/converge-g-9c41-arch.md (the ARCHITECT record — ARCH-1v2 imported born-closed; the 4 emergent
      questions + the miner gap-hunt).
    - os/plays/converge-verify.md (procedure) + os/docs/converge-design.md (the independent-oracle discipline:
      an EMPTY oracle is a BLOCKED close, never auto-PASS — author the checklist from first principles since
      knowledge/ has no contract-class checklist yet).
    - The LOCKED foundation contracts sit ABOVE: GasCoopGame ADR-0004 §LOCK + ADR-0003 v2 C1–C22 (do not re-open).
    - The 15-agent build pass was an IN-SESSION pre-pass (wf_c4e09962-08f) — NOT the binding refutation; this
      verify is the binding one, in a SEPARATE session.
  boundaries: |
    Independent oracle ONLY (do not reuse the brief/converge-arch sources as the completeness checklist). Do
    NOT edit the LOCK / C1–C22 / t-2 artifacts, and do NOT decide HOW magnitudes (those stay →PLAN). converge-
    verify REFUTES; it does not author new contracts (a real gap → a blocked close + a named repair, not a
    silently-added contract). Do NOT run shape. Session writes state only via RESULT.state_changes.
  done_when: |
    The set is attacked on FOUR axes with an independent oracle: (1) COMPLETENESS — every networked-multi-layer-
    sim contract class a node like this needs has an entry (special attention: the 2 white-spot adds XL1 multi-
    layer consistency + XL2 layer-registry extensibility; the B31 single-oracle cross-tier-composition risk OR1;
    the band-handoff no-shimmer property GG4/OR4); (2) FIREWALL — no observable leaks a HOW (push/poll/format/
    cadence/layout/magnitude); (3) NO-LEANING — no contract's acceptance leans on a question still open elsewhere;
    (4) NO-LOCK-REOPEN — no contract silently re-decides the wire format / barrier / cross-layer GridEvent / cell-
    hash. A clean verdict (or a blocked close with named repairs) is the deliverable.
  return: |
    converge-verify RESULT — the independent-oracle verdict per axis; any blocked-close repairs (named, not
    authored); next = (clean) the Wave-2 shape consumes the verified contracts (c-shape-wave2 already ready), or
    (blocked) a repair CALL back to converge-arch.
  budget: one focused session; a fresh model family may be requested for extra rigor but is not required (G5
    = fresh SESSION is the binding gate; cross-family is optional).
  surface: claude or cli; owner reachable for any contract-completeness G7 fork the verify surfaces.
```

## Self-check vs the CALL done_when

- B-row cross-node contracts declared as consumer-driven observable specs (incl. B31's single normative field-
  sampling oracle) ✓; the heavy architecture-on-paper rides PLAN as input evidence, NOT in done_when ✓
  (arch_in_context_only: PASS); the open→PLAN magnitudes mapped to the contracts that bound them (every contract
  carries a `bounds` list) ✓.
- Primary targets covered in depth: ingestion adapter/TopologyDocument (IN), grid↔gas (GG), the B31 oracle (OR);
  secondary: gas-type seam (GT), render seam (RN) ✓. Steers honored: DA-structure-day-one/PGG-later (IN1/IN2),
  band-handoff (GG4/OR4, owner-signed) ✓.
- Closed as a CHECKPOINT with next = converge-verify ✓; bet / tasks / c-shape-wave2 / NOW.next untouched ✓;
  state written only via RESULT.state_changes ✓; LOCK / C1–C22 not edited ✓.

END_OF_FILE: live/indie-game-development/history/s-converge-arch-001.md
