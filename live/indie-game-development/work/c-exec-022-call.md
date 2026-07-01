# CALL c-exec-022 — Sc-rep: SPARSE-DOMINANT RE-REPRESENTATION (ENGINE-ONLY)

Direction: indie-game-development / g-9c41 / Sc-rep — the sparse-dominant representation slice inserted AFTER Sc-weight
and BEFORE Sc-reactions (owner «беру рекомендации», 2026-06-30, s-reshape-sparse-dominant-001). Builds on the post-Sc-weight
base (GasCoopGame `main` at-or-after @61b7923 — the c-exec-020 Sc-weight merge; small repo-hygiene-only commits atop it are
expected). Executor: a FRESH `C:\projects\Unity\GasCoopGame_dev` session. Opens with a PLAN (owner present). State source =
NOW.md (task Sc-rep active). Canon = `knowledge/g9c41-gas-engine-SPEC.md` (Fact 4 sparse-dominant lock; §5 dynamic typing
requirement; §9.5 checksum stamp+overlay; §6 p.3 hangar; §4 seams 2/4/5/7 collapse/expand). Shape basis =
`work/character-road-shape-2026-06-29.md` §SLICE Sc-rep. Sibling context = `work/c-exec-021-call.md` RE-SCOPE banner
(reactions HELD until after Sc-rep).

HARDENED 2026-07-01 (wf_codex_sc_rep_2026-07-01: same-session 12-lens adversarial pass; no product repo build/touch in the
framing thread). Key folds: contract drift v8→v9 made a first PLAN step; overflow narrowed to LOUD THROW only (no
drop-smallest / declared sink in this slice); the stamp fold split into three independent RED controls plus an overlay
identity falsifier; conversion requires throw-path atomicity; the no-regression golden must be verified first-hand at tip;
fixed-inline is bound by structural + GC-zero gates, not prose; ZERO-LEGACY is sequenced after a read-path/dev2-boundary
check; scan roots must stay paired; hangar is measure-only and cannot self-pass/fail the slice; the split seam cannot defer
the stamp.

## Why this slice (and the lock id)

Sc-types and Sc-weight shipped on the current dense near representation (`int[species][cell]`). The owner then locked the
future architecture to **sparse-dominant**: per active cell, store a dominant TypeId + amount + a bounded inline mix-overlay.
That decision is not cosmetic. It is the cheapest moment to replace dense planes before reactions, dynamic typing, and
condition-waves pile on top of the old layout.

Sc-rep lays the representation that later mechanics key off:
- sparse active cells make a large roster cheap;
- the per-cell dominant-type STAMP is the socket for env-derived dynamic typing and condition-waves;
- the bounded overlay is the native place where reactions later see co-resident gas;
- the collapse/expand seam must remain open for future S4/big-space work.

Lock = **ADR-0002** (input-lockstep) is preserved, not reopened. Sc-rep claims **ADR-0021** (supersedes the ADR-0018 dense
decision recorded by Sc-types/Sc-weight history). The PLAN verifies the ADR number mechanically at the product tip across
main and dev2 docs/adr; if taken, it bumps and records the chosen number. This framing session did not read the product repo.

## goal (outcome, not method)

The near gas field is re-represented from dense `int[species][cell]` planes into a SPARSE-DOMINANT cell store:
`{dominant TypeId, dominant amount, K bounded inline overlay slots}` per active cell. Every active cell carries a mutable
dominant-type STAMP folded into `MeaningChecksum` cell-keyed. Roster size is config, not hardcoded. A single-type run remains
BYTE-IDENTICAL to the post-Sc-weight golden. Dense-to-sparse conversion conserves per-cell total mass exactly; >K co-resident
types throw loudly and atomically. The collapse/expand seam remains open. The first hangar number is measured honestly.

**ENGINE-ONLY.** No visual-track hookup. No typing mechanism. No reactions. No S4/big-space build.

**approach token = `sparse-dominant-inline-cell-store-with-cell-keyed-dominant-stamp`** — the named approach this leg exists
to prove. A delivered artifact whose recorded `approach:` differs (dense planes kept as the authority, a per-cell
Dictionary/hashmap, a parallel overlay beside dense, a stamp not folded cell-keyed, a silent overflow/drop path, or a
coarsened-gas-cell fallback) is an approach substitution requiring `owner-ack:<sig|esc-id>`; otherwise STOP-escalate.

## context (read first — applied, not just cited)

1. **§Re-sync GasCoopGame contract FIRST.** Direction OS engineering contract is v9; the known GasCoopGame run contract in
   the owner-provided repo instructions was v8. Re-sync v8→v9 before planning: wire the escape-class registry walk into
   deliver/spec-silence as the contract requires, add a seeded miss, and bump `validation.config` only when the repo-side
   gate is actually synced. If re-sync cannot be done safely inside this leg, STOP and return a blocker — do not run Sc-rep
   on a stale contract.
2. **Sc-rep shape:** `work/character-road-shape-2026-06-29.md` §SLICE Sc-rep. This is the authoritative gate battery:
   sparse-dominant layout, stamp checksum, exact conversion, roster config, no-regression golden, determinism scans, seam,
   ZERO-LEGACY, hangar measure, -Deliver, mutation, independent REDs, fresh G5, owner-eye.
3. **Canon:** `knowledge/g9c41-gas-engine-SPEC.md` Fact 4 sparse-dominant representation; §5 dynamic typing socket; §6 p.3
   hangar; §9.5 checksum members; §4 seams 2/4/5/7; §1 ADR correction (lock = ADR-0002).
4. **Design lock:** `work/gas-reaction-typing-design-2026-06-30.md` — sparse-dominant is the owner-locked keystone for
   roster size, dominant stamp, reactions overlay, and env-derived dynamic typing. The typing/reaction mechanism is CUT here.
5. **Sibling:** `work/c-exec-021-call.md` RE-SCOPE banner. c-exec-021 is HELD until after Sc-rep. Do not fire it. Reuse only
   the hardening principles: no dense fallback, no old GridEvent bus expansion, forks resolved at their proper future shape.
6. **Boundary to visual dev2:** g-7e15 visual track lives separately. This slice may verify compatibility/read-paths, but it
   does not edit dev2 or the visual track. If avoiding breakage requires dev2 edits, STOP and surface the conflict.

## the representation crux — replace the authority, do not build a palimpsest

The representation authority becomes the sparse-dominant store. Dense planes are a migration input and test oracle only; they
are not kept as a parallel source of truth. A "sparse overlay" beside still-authoritative dense planes is a palimpsest and
fails ZERO-LEGACY. A per-cell `Dictionary<TypeId,int>` or heap object is also wrong: it hides a scaling/memory cliff exactly
where this slice is supposed to buy cache friendliness.

The PLAN owns the exact structs and filenames, but the properties are binding:
- per active cell store is a contiguous fixed-size value shape, with K bounded overlay slots inline;
- inactive/empty cells are represented without per-cell heap allocation on the steady-state hot path;
- the dominant TypeId is stored as mutable per-cell state, not inferred ad hoc by `argmax` at every consumer;
- overlay slot identity + amount are folded deterministically by canonical cell coordinate and slot/type order;
- dense-to-sparse conversion is exact per cell before the dense path is removed.

## done_when (verifiable)

1. **PLAN (owner present):** §Re-sync v8→v9 FIRST; ingest Sc-rep shape + SPEC Fact 4/§5/§6 p.3/§9.5/§4 seams + design lock
   + c-021 RE-SCOPE banner. DECIDE and RECORD: (i) the concrete inline cell layout and K; (ii) overflow policy = LOUD THROW
   only for this slice (declared sink/drop-smallest is a reactions-design choice later, not legal here); (iii) the stamp
   checksum fold (own member vs rebuilt sparse-layout fold is the PLAN's call, but the 3 RED controls bind either way);
   (iv) the roster-size config mechanism and default value; (v) the post-Sc-weight golden to preserve, verified first-hand at
   the tip (pinning a pre-Sc-weight golden = STOP); (vi) ADR number (Sc-rep expected ADR-0021, verify across main+dev2 and
   record siblings); (vii) hangar harness + weak-profile-proxy method; (viii) exact ZERO-LEGACY read-path plan, including the
   dev2 visual boundary.
2. **Sparse-dominant layout shipped + cache-shape gated:** structural assertions prove the active-cell store is contiguous
   fixed-size inline data (not per-cell hashmap/Dictionary/heap object). A GC-zero steady-state test over an active scene
   proves N ticks allocate zero per-cell heap on the hot path. A planted Dictionary/per-cell `new` realization MUST trip.
3. **Dense→sparse conversion conserves cell-total mass exactly and atomically:** for every cell,
   `sum(dense species masses) == dominant amount + sum(overlay amounts)`. Stamp = max-mass species; tie = lowest TypeId.
   A >K co-resident cell THROWS loudly; the throw path leaves the field byte-unchanged and tick/commit state unchanged.
   RED controls: a naive drop-smallest remainder fails conservation; a highest-TypeId stamp under non-highest max-mass fails;
   a partial mutation before throw fails atomicity.
4. **Dominant STAMP present + folded CELL-KEYED:** the mutable per-cell dominant TypeId is folded by canonical X/Y/Z, never
   as a bag/sum/sort-by-value. THREE required RED controls: (a) ISOLATION — masking the stamp member (`All & ~member`) fails
   parity when stamps are non-trivial; (b) DISTINCTNESS single-endpoint — two fields identical in per-type masses but with
   different stamp TypeId or stamp location diverge; (c) cross-peer divergence — peers with different dominant assignment
   diverge. Overlay identity also has a falsifier: same cell total/dominant amount but different overlay TypeIds or slot order
   must not collapse to the same meaning unless the canonicalized semantic content is truly identical.
5. **Roster size = config, not code:** roster ceiling/default is data/config (`~128` is a suggested starting value, not a
   constant welded into logic). RED: changing the roster limit/default touches data/config only and changes the registry or
   handshake content hash as appropriate; no C# branch/table edit is required.
6. **No-regression BYTE-IDENTICAL:** a single-type run reproduces the committed post-Sc-weight gas golden byte-identically.
   The PLAN verifies first-hand which golden covers the Sc-weight-inclusive gas path; do not rebaseline or regenerate goldens
   to hide representation drift. The two-endpoint MeaningChecksum loopback is the determinism tripwire, not the golden.
7. **Determinism preserved (ADR-0002):** integer-only authoritative path; new code covered by BOTH zero-float and
   int-overflow scans. If code lands under existing scanned roots, demonstrate coverage; if a new authoritative directory is
   introduced, add it to BOTH root lists (kept identical) with planted-float and unguarded-int*int RED self-tests. Loopback
   two-endpoint MeaningChecksum green over a multi-type sparse run; planted float/order-dependence controls trip. The v9
   escape-class registry walk is included in deliver/spec-silence after §Re-sync.
8. **Collapse/expand seam preserved:** per-region structure remains intact; `representation_tag {fine-3D|coarse|bucket}` /
   collapse/expand is not welded shut. A body-identity or explicit seam test proves S4 can plug in later without core edits.
   This slice does not build S4 or a bucket/rollup implementation.
9. **ZERO-LEGACY dense near path removed after read-path check:** the dense `[species][cell]` near authority is deleted once
   the sparse path passes. Before deletion, run a §Re-sync read-path check for live consumers, including the visual-track
   boundary (`RealGasViewSource` / `VoxelField` render-only). Main/dev code must not break; dev2 is not edited by this leg.
   If compatibility requires dev2 edits or preserving dense as a second truth, STOP-escalate.
10. **FIRST hangar measurement (MEASURE-ONLY, honest partial):** record active_cells/cores (x4-8) on the owner machine plus
    a documented weak-profile-proxy method. The result explicitly says: strong-machine + proxy, not the SPEC §6 p.3 weakest
    peer absolute ceiling. No pass/fail budget is set here.
11. **check.ps1 -Deliver GREEN:** build + headless tests + zero-float + int-overflow + type-hardcode where relevant +
    mutation >=70 on new Core + spec-silence + deliverable-coverage + v9 escape-class walk + RESULT.md. G0-frozen if the
    repo opens an OpenSpec change: frozen spec, ledger, spec-silence audit, deliverable coverage, mutation json.
12. **Independent REDs + fresh G5 + owner-eye:** independent test-author writes RED acceptance tests before build; builder
    does not edit them. Fresh-session G5 (different session/model-family per repo contract) tries to refute: layout inline
    not hashmap, conversion exact/atomic, stamp cell-keyed distinctness, overlay identity fold, no-regression golden, scan
    coverage, ZERO-LEGACY/read-path boundary, collapse/expand seam, and hangar honesty. Owner-eye is confidence only: owner
    sees the same scenes behave identically post-representation and sees the hangar number; no self-marking.

## boundaries / STOP-escalate if tempted

- NO typing mechanism (exposure accumulator/flip), NO condition-waves, NO reactions, NO damage, NO temperature.
- NO S4/big-space rollup build; preserve the seam only.
- NO visual-track hookup and NO dev2 edits.
- NO dense authority kept as a parallel truth; git is the rollback path.
- NO per-cell hashmap/Dictionary/heap hot-path representation.
- NO silent overflow, saturate/drop-smallest, wrap, or declared sink in this slice. >K = loud throw and atomic no-mutation.
- NO coarsening gas cells / changing the 50cm gas lock as a hangar fallback.
- NO float on the authoritative path; no unseeded RNG; no wall-clock; ADR-0002 not reopened.
- NO product-side build starts before the owner-present PLAN records the decisions in done_when #1.

## ведро classification (PLAN reconfirms)

**Ведро-2**: sparse layout + per-cell dominant stamp + overlay identity are authoritative shared state in the checksum.
**Ведро-1**: absent. **Ведро-3**: absent. The typing/reaction gameplay that will use the stamp arrives later.

## discipline / gates (carried)

RED-first by an independent test-author · builder cannot edit the independent RED tests · Core/** authoritative placement ·
named approach token recorded in deliverable coverage · -Deliver GREEN · mutation >=70 · v9 escape-class registry walk ·
fresh-session G5 refutation · STOP-discipline on substitution/crutches · small build steps · owner-present PLAN.

## return

A RESULT routed HOME to Direction OS: outcome + evidence (commits/PR, -Deliver transcript, mutation json, v9 re-sync proof,
independent RED list + pass output, fresh G5 verdict, owner-eye note, chosen ADR number and sibling check, chosen K/layout,
roster config, post-Sc-weight golden identity, conversion exact/atomic evidence, stamp/overlay checksum RED-control trips,
GC-zero/cache-shape evidence, ZERO-LEGACY/read-path/dev2-boundary result, collapse/expand seam proof, hangar measurement and
its honesty caveat). dev→main merge + push owner-gated. On GREEN, OS rolls the road to Sc-reactions and re-hardens/fires the
held c-exec-021 on the post-Sc-rep base.

## budget

One executor slice. Split only by machinery if genuinely oversized: leg1 MUST include the sparse-dominant cell layout,
dominant STAMP field, cell-keyed stamp checksum fold, no-regression golden, determinism scan coverage, and first hangar
measure. Leg2, if needed, may carry K/overflow-policy refinement and the collapse/expand seam-preservation check. The stamp
and its checksum fold are intrinsic to the representation and may not be deferred out of leg1. The typing mechanism is cut
entirely.

END_OF_FILE: live/indie-game-development/work/c-exec-022-call.md
