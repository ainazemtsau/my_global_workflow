# s-converge-verify-001 — converge-verify of g-9c41 Wave-2 §CONTRACTS (BLOCKED close)

Session: converge-verify · direction indie-game-development · node g-9c41 (Wave-2 §CONTRACTS set) ·
parent s-converge-arch-001 (c-converge-002) · CALL c-converge-verify · 2026-06-16 · surface: claude/cli.

This is the BINDING independent G5 refutation (a SEPARATE fresh session) of the §CONTRACTS set authored by
converge-arch — NOT the 15-agent in-session pre-pass (wf_c4e09962-08f), which was a same-session self-check.
The verdict is recorded both here (full reasoning) and as §VERIFY in work/converge-g-9c41.md.

## RESULT

```RESULT
to: writer
direction: indie-game-development
play: converge-verify
node: g-9c41 (Wave-2 §CONTRACTS set)
parent: s-converge-arch-001 (converge-arch DECLARE; c-converge-verify)

outcome: |
  converge-verify (binding fresh-session G5 refutation) ran the §CONTRACTS set (IN/GG/OR/XL/GT/RN/CS) of
  g-9c41 Wave 2 against FOUR axes with an INDEPENDENTLY-AUTHORED oracle (ORACLE-NMTL, built from first
  principles + competing precedents; knowledge/ had no checklist). VERDICT = BLOCKED CLOSE. 16 contract
  classes covered + firewall substantially clean + no silent LOCK re-open (XL2 table-resize correctly
  follows the LOCK's own instruction) — BUT two real holes found, each named with a non-author repair
  bounced to converge-arch. Shape may NOT consume the contracts as verified until a clean re-verify.

evidence: |
  - COMPLETENESS attacked with ORACLE-NMTL (25 contract classes for a networked multi-TIER multi-LAYER
    host-authoritative field-core; precedents = Quake/Source/Overwatch delta-netcode, SS13/SS14/Stationeers/
    Noita chunked single-writer atmos, layered data-oriented ECS, LOD/streaming) — recorded in §VERIFY of
    work/converge-g-9c41.md. 1 hard FAIL (class: COARSE-tier network replication + consistency obligation).
  - FIREWALL/SMUGGLING/NO-LEANING traced per weight-bearing observable. 1 leaning/smuggling hole = the same
    coarse-tier-replication gap (OR2 "coarse=floor on every consumer", crit-3, crit-9 ~11k on-wire cells,
    GG4/OR4 "amount never changes crossing tiers" all lean on an UNCITED coarse-replication+consistency
    decision). Otherwise clean (HOW correctly ->PLAN; XL1 MECHANISM-para borderline but restates LOCKED
    foundation, not a new smuggle).
  - NO-LOCK-REOPEN checked against the VERBATIM locked artifact (ADR-0004 §LOCK + ADR-0003 C1–C22, read
    read-only from the product repo): wire header {layerKey,chunkIndex,resolutionKey,revision}; barrier
    per-(layerKey,chunkIndex) high-water, table [layerCount=2,chunkCount=4], "any Wave-2 layer/grid
    extension SHALL re-size"; channel unreliable-sequenced; GridEvent{Revision,Source,Kind,CellIndex,
    Magnitude}, GridEventKind{GasChanged=1,Breach=2,Reaction=3}, phases P0->P3, single-writer-per-(LayerKey,
    phase); ReactionHeat=32 pinned pure-sink; §T12 temp pure-sink-consistent; C21 gas byte-identical;
    CellHash.FoldLayer Fnv1a64. XL2/GG1/XL1 reference (not redefine) — PASS, EXCEPT 1 hole = XL1 crit-10
    FEEDBACK requirement is unreconciled with the locked pure-sink proofs (C21/§T12 byte-identical) AND the
    gas/breach-only locked GridEventKind enum (a temperature-sourced feedback event would extend a locked
    enum; XL2's "generalized C21 byte-identical" literally contradicts XL1's feedback once both are present).
  - ADVERSARIAL self-check: both findings steelmanned against a PASS reading and survived (coarse-replication
    is an UNCITED weight-bearing assumption, not a derivable HOW; XL2-vs-XL1 byte-identical is a literal
    incoherence, not a charitable-reading nit).

state_changes:
  - file: live/indie-game-development/NOW.md
    edit: |
      open_calls — c-converge-verify: status checkpoint->done; note replaced with the BLOCKED-close verdict
      (F1 coarse-tier replication, F2 XL1 feedback/enum reconcile) + pointers to §VERIFY + this history file.
  - file: live/indie-game-development/NOW.md
    edit: |
      open_calls — ADD c-converge-003 (status ready): repair CALL back to converge-arch carrying F1+F2;
      a clean re-run of converge-verify follows before shape binds the contracts.
  - file: live/indie-game-development/NOW.md
    edit: |
      open_calls — c-shape-wave2 note: append a contract-gate clause — §CONTRACTS BLOCKED pending
      c-converge-003 + re-verify; the bet-SPINE shape may proceed but MUST NOT bind unverified §CONTRACTS
      into executor done_when (contracts = DRAFT until re-verify clean).
  - file: live/indie-game-development/work/converge-g-9c41.md
    edit: |
      Append §VERIFY (converge-verify pass — c-converge-verify, 2026-06-16): BLOCKED verdict, ORACLE-NMTL
      class checklist + coverage table, the 2 findings + named repairs, the clean axes, the play_check;
      END_OF_FILE trailer moved to the new end.
  - file: live/indie-game-development/LOG.md
    edit: append one line for this session (link to this file).
  - file: live/indie-game-development/history/s-converge-verify-001.md
    edit: create — this file.

captures:
  - "GG4 bounds list omits C22 though its acceptance ('amount never changes crossing tiers') depends on the
     lossy mass bound; OR4 twin cites C22 — fold C22 into GG4 bounds at the converge-arch repair (minor)."
  - "XL1 MECHANISM paragraph carries a pub/sub communication model inside a contract — firewall-borderline;
     it restates LOCKED foundation so not a new smuggle, but the repair should trim it to the observable +
     route the model to PLAN."
  - "Protocol/schema version-handshake across builds is only IMPLICITLY deferred (via B17 non-contract +
     I20 late-join-OUT); make the deferral explicit when the distributable build edge (g-5b07) is worked."

canon_proposed:
  - "ORACLE-NMTL — contract-class checklist for a networked multi-TIER multi-LAYER host-authoritative
     field-simulation core serving sibling consumers (25 classes). Authored this session from first
     principles + precedents. PROPOSE to knowledge/ (serves: g-9c41 + future networked-sim nodes; read_by:
     converge-verify of this node-class). converge-verify proposes; review/pulse promote."

decisions_needed: []   # verify routes findings; no new owner G7 fork (owner-signed properties stand)

play_check:
  - "1 recite: stated the two propositions (set COMPLETE; no answer leans/leaks) — done."
  - "2 attack-completeness (INDEPENDENT oracle): ORACLE-NMTL authored from first principles + precedents (NOT
     the brief/converge-arch sources), named, proposed as canon; 25 classes mapped; FAIL=1 (COARSE-tier
     network replication+consistency obligation has no contract) — F1."
  - "3 attack-smuggling (firewall + no-leaning + no-lock-reopen): firewall substantially PASS (HOW->PLAN; XL1
     MECHANISM borderline, not new); no-leaning FAIL=1 (= F1, the uncited coarse-replication lean);
     no-lock-reopen PASS except F2 (XL1 feedback unreconciled with locked C21/§T12 pure-sink + locked
     GridEventKind enum; XL2 generalized-C21 contradicts XL1 feedback). Checked against verbatim ADR-0004/
     ADR-0003."
  - "4 close: BLOCKED close — next = c-converge-003 (repair to converge-arch carrying F1+F2); verify re-runs
     after re-close; NO §SIGNOFF: converge-verify passed written (holes found). Not two-strikes (first bounce
     of these rows)."

log: "indie-game-development converge-verify g-9c41 Wave-2 §CONTRACTS: BLOCKED close — independent oracle (ORACLE-NMTL) found 2 holes (F1 no coarse-tier replication contract; F2 XL1 feedback vs locked pure-sink/GridEventKind enum); 16 classes + firewall + no-lock-reopen otherwise clean; bounced to converge-arch (c-converge-003), shape may not bind contracts until re-verify."

next: |
  CALL c-converge-003 — repair the g-9c41 Wave-2 §CONTRACTS set (2 verify-bounced findings), then re-run converge-verify.
  to: session   direction: indie-game-development   play: converge-arch   node: g-9c41 (Wave-2 contract repair)
  parent: s-converge-verify-001 (converge-verify BLOCKED close)
  goal: |
    The §CONTRACTS set closes the two holes the independent verify found, observable-first, HOW->PLAN, nothing
    re-opening the LOCK; then a fresh converge-verify re-runs and passes clean so shape can consume the contracts.
  context: |
    - work/converge-g-9c41.md §CONTRACTS + §VERIFY (the BLOCKED verdict, ORACLE-NMTL, the 2 findings) +
      work/converge-g-9c41-arch.md (ARCHITECT record). history/s-converge-verify-001.md (full reasoning).
    - F1 (completeness + smuggling): declare a COARSE-tier network-replication + consistency contract,
      observable-first — does coarse band-state reach every client-side consumer (vs host-only); carrier
      (locked-stream resolutionKey vs a separate plane); consistency standard (bit-exact / bounded-divergence
      / host-only) + the coarse-solver determinism obligation; resolve the latent float-Patankar-vs-locked-
      integer-bit-exact conflict at the contract level. HOW (plane/granularity/interest-management) ->PLAN.
      This is what crit-3 (clients consistent), crit-9 (on-wire ~11k cells), OR1/OR2/OR3-on-a-client, and
      GG4/OR4 ("amount never changes crossing tiers") all silently lean on.
    - F2 (no-lock-reopen + internal contradiction): reconcile XL1's crit-10 FEEDBACK requirement with the
      LOCK — state feedback = read-based-in-phase-order (locked GridEventKind enum untouched; Wave-1 sink/
      ReactionHeat=32/C21 stays a frozen control) OR event-based (then SURFACE the locked-enum extension like
      the barrier-table resize, never silent in PLAN); and re-baseline XL2's isolation proof (demonstrative
      layer == gas+temp, NOT == gas-only) so it stops re-using the locked C21 "byte-identical to gas-only".
    - Minor (captures): fold C22 into GG4 bounds; trim the XL1 MECHANISM paragraph to observable + route the
      model to PLAN; make the version-handshake deferral explicit at the g-5b07 build edge.
    - The LOCKED foundation is verbatim in this history file's §APPENDIX (do NOT re-open it).
  boundaries: |
    Repair ONLY the two found holes (+ the named minors) — do not re-litigate the clean contracts or the
    owner-signed band-handoff/feedback properties. Do NOT edit the LOCK / C1–C22 / t-2 artifacts; HOW
    magnitudes -> PLAN. converge-arch authors observable contracts; it does not decide HOW. State written only
    via RESULT.state_changes. After re-close, hand back a fresh converge-verify CALL.
  done_when: |
    F1 + F2 closed as observable-first contracts (or honest non-contracts) with HOW->PLAN and no LOCK re-open;
    §CONTRACTS coverage re-checked; next = a fresh converge-verify CALL on the repaired set.
  return: |
    converge-arch RESULT — the repaired §CONTRACTS entries + a converge-verify CALL; or, if a repair needs an
    owner G7 fork, that batched with options+recommendation.
  budget: one focused session.
  surface: claude or cli; owner reachable only if a repair opens a genuine G7 fork.
```

## §APPENDIX — verbatim locked facts used for the NO-LOCK-REOPEN axis

Read read-only from the product repo for the binding check (do NOT re-open these in the repair):
- ADR-0004: `C:/projects/Unity/GasCoopGame/docs/adr/ADR-0004-sustained-load-verdict-lock.md`
- ADR-0003 v2: `C:/projects/Unity/GasCoopGame/docs/adr/ADR-0003-gas-field-state-stream.md`

ADR-0004 §LOCK (verbatim excerpts):
- Wire format: 7-byte header `{layerKey:byte, chunkIndex:byte, resolutionKey:byte, revision:int32}`; payload
  `resolutionKey 0=FULL-INT32` (4 B/cell int32), `1=QUANT8` (1 signed B/cell = `round(raw/Q)`, reconstructed
  `qv·Q`); fp16 forbidden; QUANT8 signed-byte overflow escalates to FULL-INT32; `chunkSpan=4` agreed
  out-of-band (no wire length field).
- Revision barrier: per-`(layerKey,chunkIndex)` high-water; apply IFF `incomingRevision > stored` (strict;
  ties/stale rejected); same rule for keyframes and deltas; first revision is 1; backing
  `int[layerCount,chunkCount]` sized `[layerCount=2, chunkCount=4]` for the locked scene — an out-of-range
  `(layerKey,chunkIndex)` is an `IndexOutOfRange` throw, so **any Wave-2 layer/grid extension SHALL re-size
  the table** (not rely on a silent reject).
- Channel semantics (T7): unreliable-sequenced; correctness guaranteed by the barrier under
  drop+delay+reorder.
- Cross-layer contract: `GridEvent{Revision,Source,Kind,CellIndex,Magnitude}`;
  `GridEventKind{GasChanged=1,Breach=2,Reaction=3}`; `IGridEventBus`; pinned phases `P0→P1→P2→P3`;
  single-writer-per-`(LayerKey,phase)` token. Reaction firing contract: `Reaction` fires at the breach cell
  on each portal-open transition; `TemperatureLayer` adds the frozen `ReactionHeat=32` to `temp[c]`
  (DISTINCT from `BreachHeat=64`) — pinned so a Wave-2 author cannot silently move the
  reconstructed-Temperature trajectory.
- Cell-hash domain: `CellHash.FoldLayer` over `(layerKey,chunkIndex,cellIndex,value)` via `Fnv1a64` (LE) —
  distinct from `FieldState.Hash()`/`SimState.Hash()`.
- §T12: under the sustained wave the temperature layer's reconstructed cells stay host==clients on
  `CellHash.FoldLayer(Temperature)` at every settle (in both the with- and suppressed-reaction arms —
  temperature is a pure sink with no feedback to gas, so it always converges).

ADR-0003 v2 (C1–C22, summary): C1 cell type & hash fold; C2 Q=16; C3 |client−host|≤Q; C4 deadband=Q +
flush-on-quiesce; C5 per-client clamp 150 KB/s; C6 aggregate clamp 275 KB/s; C7 channel reliability; C8
settle N=16; C9 keyframe K (no periodic K in t-2); C10 wire format; C11 single-writer per-(layerKey×phase);
C12 revision barrier; C13 fault scope (drop+delay); C14 min-resend (dropped t-2); C15 scene profile (2 rooms,
16 gas + 16 temp, chunkSpan=4, 1 breach portal); C16 repro constants; C17 peers 1 host + 2 clients; C18
measurement schema; C19 client recon rule (pure integer `qv*Q`); C20 apply-order (disjoint chunks commute);
C21 RNG conservation (gas+temp keeps gas hash byte-identical; temp consumed zero gas RNG); C22 lossy
convergence (host-side per-cell error-feedback, bounded |client−host|≤Q, bit-exact at settle via C4 flush).

END_OF_FILE: live/indie-game-development/history/s-converge-verify-001.md
