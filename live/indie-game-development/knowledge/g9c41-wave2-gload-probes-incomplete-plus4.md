# §G load-probes are INCOMPLETE — 4 added MANDATORY probes before any A+ bet

read_by: shape of the FIRST A+ bet of g-9c41 (the §G probes are the pre-bet kill-gate — this list is the hardened gate). Also the technical-feasibility lens.

Accepted 2026-06-20 by review s-review-002 (adversarial audit of the gas-model doc §G/§H against the real GasCoopGame core, HEAD a89b36b).

**Fact.** The doc's §G (7 pre-bet load-probes) is real, cheap, and mostly well-aimed — front/geodesic is covered twice (corner-around + integer incremental Dijkstra on breach), interest-grain by the "8 hot bubbles → per-tick cell ceiling + round-robin" probe, blast-as-transport+mass-conservation by the RED-test (and that narrowing is correct: plain mass-conservation is ALREADY a passing hard invariant, so #5's genuinely-new content is only blast-as-transport). BUT it is INCOMPLETE against its own stated new assumptions. Three of the six new A+ correctness rules have NO dedicated probe, and host-migration is dangerously bundled.

**The 4 added MANDATORY probes (do not let the first A+ bet skip these):**
1. **Two-machine awake-set / sleep-schedule DETERMINISM** — the same committed state must yield a byte-identical awake-set AND update order on every machine under the per-tick cell ceiling. This is the single most likely silent desync: A+'s entire perf story rests on sleep/interest-grain, and the LOCK forbids exactly this class of bit-exact break. UNPROBED today.
2. **Resident-gas-damage RED ledger** — a RED test that a front which only *touches-and-leaves* deals ZERO dose, while only RESIDENT gas accumulates dose. The doc itself (§E/§D.6) calls this a FIXED correctness LAW, yet it ships with no load-probe.
3. **Confirmed-colocation FALSE-reaction probe** — two mid-level coarse numbers in one room must NOT detonate without fine-grain co-location confirmation. Reactions are 100% unbuilt (ReactionLayer is a toy), so the false-positive path is wholly unverified.
4. **Real-DA(SnapGridFlow) at hundreds-of-rooms scale** — the geometry-derived-id pipeline is proven only at 6 sectors (t-4-da-output.json); the ~3,300-sector scale is validated on the SYNTHETIC CreateSynthetic graph. They have NEVER been exercised together. done_when #3's "real DA + hundreds of rooms" was split across legs this wave; an A+ bet on it needs them united.

**Also:** SPLIT host-migration out of the benign save/load cut (§H) — host loss = death of a 4–8 coop session, the value-prop killer; consider requiring a "host dies → session survives" spike in the FIRST A+ bet. Give blast-as-transport its own RED row (don't let it hide behind the already-passing mass-conservation tests). Edge-destructibility beyond ONE breach (runtime edge add/widen/split, "new barrier splits a room") and moving geometry (elevators/blast-doors closing on a non-empty gas column) are named §H unknowns that interact with the mass-conservation law at the edge-snap moment — name them, don't slip them into "solve later". Make the wire discipline a NUMBER: the LOCK barrier [7,chunkCount] has only 4 free plane-keys (2..5) before temperature at 6, so "capped active gases/node + hard wire cap" needs a chosen cap (a new plane = a SURFACED LOCK-EXT per ADR-0007).

**How to apply.** The first A+ shaped bet's done_when = the hardened §G set (§G's 7 + these 4) passing as RED ledgers / two-machine determinism checks, BEFORE any feature layer is committed. Probes must run on a topology-bound graph (capacity/back-pressure is geometry-bound — a t-1 factory graph won't exercise the hard cap).

Relates to [[g9c41-wave2-aplus-over-b-code-grounded]], [[g9c41-wave2-coarse-proof-not-resolution]].

END_OF_FILE: live/indie-game-development/knowledge/g9c41-wave2-gload-probes-incomplete-plus4.md
