# A+ re-plan under the LOCKED gas-model architecture — v1 (DRAFT, owner-approval-pending G9)

> **Status:** DRAFT proposal for owner sign-off (G9). NOT yet applied to TREE/NOW. Produced by the re-plan impact workflow
> (wf_1a13feb0-a5f: 3 independent impact analysts → 3 adversaries attacking the LOCKED architecture AND the re-plan + a
> completeness critic → 1 synthesizer) over the locked architecture doc + the current wave plan + g-9c41 + NOW.
> **Inputs:** work/gas-model-architecture-decision-2026-06-21.md (D1–D13), work/aplus-wave-map-v1.md, work/aplus-breakdown-v1.md
> (now STALE — see §0), live/indie-game-development/{TREE.md (g-9c41), NOW.md}.
> **Verdict in one line:** the OUTCOME STRUCTURE is intact; node **g-9c41's content** changes (a contained TREE-diff, owner-G9 +
> a new ADR) AND the **waves re-sequence substantially**. D1 (input-lockstep) is adopted as the owner's **leading hypothesis
> pressure-tested in Wave A**, NOT hard-re-locked.

## 0. The one thing that makes the old breakdown STALE

`aplus-breakdown-v1.md` was written BEFORE the architecture lock. Its §5 KEEP list still names **host-broadcast
follower-RECONSTRUCTION** (`CoarseChunkFollower reconstructs-not-recomputes`, "the LOCKed stream") as untouched core, and its
DAG (`visibility-as-truth = host one shared field`, geodesic-front-as-the-core) is built on the host-broadcast model. **D1
supersedes exactly that.** Building the breakdown as written would bake in the authority model D1 replaces. This doc is the
D1-reconciled re-plan; the breakdown stays as the pre-lock record.

## 1. Tree or waves? — BOTH, but the tree change is surgical

- **Structure intact.** No node added/removed. Root g-a7f2, g-9c41 (engine), g-d3a8 (design), g-7e15 (visual), g-5b07
  (storefront), g-e6f2 (audience), g-2f8c (marketing) all keep their place + goals.
- **Node g-9c41 content changes** — and it touches an owner-LOCKED criterion, so it needs the same G9 gate the A+ re-frame (#11)
  itself passed, plus a NEW ADR (proposed **ADR-0010**) that SUPERSEDES the ADR-0004/0005 authority assumption. A wave re-plan
  alone CANNOT do this — the LOCK must never be cracked silently.
- **Waves re-sequence** because the prior plan was host-broadcast-shaped.

## 2. Tree-diff — node g-9c41 (each from → to; owner-G9 + ADR-0010)

| # | field | from (current) | to (proposed) | severity |
|---|---|---|---|---|
| **#2** | replication model | "host/server-authoritative sim + chunked-delta gas stream; … rollback/lockstep at most one 1-2-week timeboxed spike" | **INPUT-LOCKSTEP (D1)** — only player inputs cross the wire; every peer deterministically recomputes the full sim (integer + seeded RNG + pinned (PeerId,Command) order + per-tick **meaning**-checksum; desync = loud stop). No per-tick gas-state on the wire. Binding limit = **weakest-peer CPU**, not bandwidth. Host-migration near-free. The chunked-delta stream (ADR-0004/0005) is **SUPERSEDED for the live authority path** and **REPURPOSED to the snapshot/late-join channel**; kept in git as a reversible fallback until lockstep is proven on the real gas kernels at ~300-room scale. GPU still never authoritative. **CHOSEN model, pressure-tested in Wave A — not hard-re-locked; gameplay DEPTH is the binding property.** | **must-change (P1)** |
| **#9** | scale / bandwidth budget | "bandwidth budget … from the ON-WIRE rate INCLUSIVE of the resync-keyframe flush … ~11k cells … size the grid against the on-wire number" | Under D1 the per-tick gas wire is gone → the on-wire bandwidth ceiling **dissolves** as the binding limit. New binding limit = **per-tick SIM CPU on the weakest peer** (every peer recomputes), with the **active-front/dirty-set** lever (doc §8, day-one) + **sparse dominant-gas** (D9) as the affordability mechanism. The old keyframe byte-arithmetic **survives, repurposed** to size the late-join/onboarding **snapshot** cost. ADD the §13 open cost: 3D-near at 25 cm in a big hangar (~256k cells) needs a measured weakest-peer budget + a degradation path. Reconcile scale UNITS (R17 ~300 rooms vs tree "≥1000 volumes"). | **must-change (P1)** |
| **goal** | prose | "2-4 players … host-authoritative multi-gas simulation on sector-band grid" | "2-8 players … player-hosted **input-lockstep** session (host = lobby/connection-point + migration anchor; every peer deterministically authoritative), multi-gas sim on a room+opening graph with **cell-SIZE LOD** (near = full 3D ~25 cm; far = room-bucket), destruction = pre-declared latent openings flicked open." | should-change (same RESULT) |
| **#3** | clients see consistent gas | "2+ networked clients see consistent gas behavior" | mechanism-neutral: consistency by **deterministic independent recompute + per-tick checksum agreement** (peer A == peer B, NOT a follower reconstructing a host stream); desync = loud checksum stop. Expose the checksum in debug surfaces. (Note: a strictly HARDER bar than reconstruction-parity.) | should-change |
| **#11** | A+ re-frame text | "bit-exact networked **replication** KEPT (criteria 2/3) … B rejected because it reopens the solved network-determinism problem" | bit-exact **DETERMINISM** KEPT (now load-bearing) — **replication-of-state SUPERSEDED by recompute-on-every-peer**; the determinism core (integer math, seeded RNG, pinned order, checksum, SimCore) transfers wholesale, only the host-broadcast wire is dropped/repurposed. Restate the "B rejected for reopening net-determinism" line — D1 **deliberately** reopens per-peer determinism (judged cheaper net: migration near-free, no meaning-hash, no wire pages). Concretize to ONE integer cell model at cell-SIZE LOD (D2/D3), sparse dominant-gas (D9), integer chemistry table (D10), real height via 3D-near (D11 — 2 bands declared INADEQUATE for the detailed tier), collapse/expand the only tier path, big/important rooms hold state on return (D5), carve-corridor CUT (D13). ROOM capacity + back-pressure KEPT (now the far-tier bucket). | should-change |
| **#1 / #10** | min-spec / layered consistency | "#1 perf on min-spec GPU/VRAM"; "#10 networked-consistent at coarse scale" | #1: add a per-tick **SIM-CPU** budget on the weakest-peer min-spec (lockstep runs the full sim on every peer — GPU/VRAM alone measures the wrong resource). #10: "networked-consistent" = covered by the per-tick **meaning-checksum**, NOT host-broadcast replication; distinguish a **derived/read-only** new layer (plugs in via the RN1 read seam, no core edits) from a new **authoritative** layer (must join the meaning-checksum = a SURFACED determinism-contract extension). | should-change |
| **#4 / #5 / #6** | reconcile (no contradiction) | #4 "3rd gas by data alone"; #5 "reusable agent-drivable harness"; #6 "gas render proof slice locks stylization" | #4: 3rd gas = a collision-table row + buoyancy coeff + sparse-store entry (D9/D10), passing the meaning-checksum (no wire plane to reserve). #5: **KEPT, orthogonal to D12** — D12 drops a reusable ENGINE, not the reusable test HARNESS; under D1 its deterministic-seed/headless/telemetry clauses are PROMOTED to determinism infrastructure. #6: render-pipeline-seam decision now lives in Track V (g-7e15); the §11 FEEL grey-box (owner-eye) replaces the "lock stylization" framing; check against near-3D (D3). Soften the node `why` "tech stays reusable" → reusable engine is a welcome SIDE-EFFECT, not a goal (D12). | should-change (#4/#6) / confirm-kept (#5) |

## 3. Re-planned waves (under the locked architecture)

**Wave A — Lab + de-risk wall + FEEL (active).** *Outcome:* the test LAB exists (owner opens ONE scene, picks a DATA scenario,
watches near-3D + coarse gas; Claude reads snapshots) AND two make-or-break verdicts land — **(1) owner-EYE "is near-3D gas FUN
at cheap settings?"** on a grey-box, and **(2) a signed verdict that the core has no load-bearing blind spot under input-lockstep**:
the gas-sim runs bit-identically when recomputed **independently on 2 machines** on the **five hard kernels** (orifice flow,
layer-sort tie-break, collapse/expand largest-remainder, chemistry collision table, awake-set canonical order), each with a RED
negative control; plus a measured **weakest-peer min-spec per-tick CPU budget INCLUDING the player-inside-a-big-hangar case**.
*Riskiest:* whole-gas-sim cross-CPU bit-exact determinism is categorically harder than the proven host→follower reconstruction
(any peer's stray float / unpinned order / libm diff desyncs all 2-8), and §14 admits the gas-sim has NEVER run under SimCore.
Co-riskiest: the §13 hangar 3D-near cost is now paid simultaneously on every peer.
*Delta:* re-center the binding probe from "host+2-follower reconstruction stays bit-exact" → "every peer recomputes
identically"; ADD the FEEL grey-box leg; ADD "wire the gas-sim under SimCore lockstep on a small level"; EXPAND the determinism
probe to all five kernels + RED controls + a COMBINED proof (lockstep + active-front + LOD-switch + re-fluxing TOGETHER, not
composed-by-assumption in Wave B); ADD a weakest-peer hangar CPU probe; RE-SCOPE the §G harness from reconstruction-parity (MOOT)
to independent-recompute parity; FIX §9.5 (meaning-checksum) + §9.8 ((byte)c guard) BEFORE any LOD/wake feature.

**Wave B — Where is the gas.** *Outcome:* on a real DA level of hundreds of rooms, every peer deterministically shows where each
gas is + its advancing edge; near the player a full-3D cell field answers "where exactly"; collapse/expand keeps tier transitions
mass-lossless + pop-free. *Riskiest (CATCH-ALL risk — the owner's #1 fear):* active-front + segment-merge + wake + cell-size-LOD +
representation-switching were each spiked in isolation, never together under bit-exact lockstep — Wave B must NOT assume they
compose (the combined proof moves into Wave A). R-NO-PROXIMITY-POP now spans EVERY tier boundary T0/T1/T2/T3. *Delta:* unify the
3-part B story (RectDecomposition + interest-grain + sleep) into ONE cell-size-LOD model; DEMOTE the integer geodesic FRONT from
"the answer" to the far-tier accuracy upgrade (graph-fronts = Wave-3); FLIP "visibility-as-truth: host computes one shared field"
(host-authoritative — contradicts D1) → "every peer computes the same field; the awake/detail SET is deterministic + checksum-covered".

**Wave C — Consequence.** *Outcome:* gas does things identically on every peer — damage only where gas sits, reactions that
telegraph then fire (queue on overflow), explosion = mass-conserving transfer + next-tick cascade, ventilation as an integer
edge-modifier (no float solver). *Riskiest:* the detonate decision must read refinement-invariant coarse totals (§3.5) or a
player's near approach self-detonates a cloud (a gameplay pop); a pump/vent keeps a region perpetually awake (§3.8) — an always-hot
edge threatening the sleep economy. *Delta:* re-anchor reactions/damage on the SPARSE dominant-gas model (D9) + integer chemistry
TABLE (D10); bind detonate to refinement-invariant totals (NEW gameplay-determinism invariant); add a NAMED SINK for ventilation;
reconcile D9's transient-mix overlay with the reaction QUEUE; loot (D6) dose-accumulator is authoritative integer state — checksum-covered
+ budgeted against the sleep economy.

**Wave D — Robustness.** *Outcome:* break walls (Case A opens / Case B splits via pre-cut break-lines); a host can leave/crash and
the 2-8 session survives; a blast-door closing on a gas column conserves mass — all deterministic across peers. *Riskiest:*
**late-join is quietly re-opened** as a real co-op obligation — a mid-session joiner can't replay from t=0, so they need a full-state
SNAPSHOT (the repurposed ChunkEncoder, which inherits the (byte)c overflow at 300-room scale). Moving-geometry mass transition is
authoritative state every peer recomputes. *Delta:* host-migration IMPL drops from "unsolved chunk" → near-trivial "promote a peer
with ZERO state transfer" (the co-op value-prop KILLER is **largely dissolved** — a real win); FLAG late-join-via-snapshot as a
NAMED-OPEN obligation before Wave D; the moving-geometry probe must also assert bit-identical recompute on 2 machines; under D1
anti-cheat is HARDER (symmetric trust, no host referee, forced checksum-desync = a DoS vector) — keep §H griefing named-OPEN but
flag the protocol dimension in ADR-0010.

**Track V — Visual GASG (g-7e15, parallel, unchanged in approach).** D1 STRENGTHENS the decouple invariant (every peer holds the
full local field → the visual never waits on a host broadcast). Two CONTENT corrections only: the render-pipeline-seam decision
done_when#6 used to own now lives here; the swap-TARGET is the **sparse dominant-gas cell field (D9) + near-3D field (D3)**, NOT a
geodesic front (which D2/D3 demote to a far-tier read). Design/feel pass first (already queued), then c-visual-001.

## 4. Leg plan + sequencing (G1 ≤ 3 active tasks)

| leg | status | scope | sequence |
|---|---|---|---|
| **t-1** reader + sandbox + FEEL grey-box | **re-scope** | KEEP as the netcode-agnostic FOUNDATION (every later wave runs on it) **and FOLD IN the FEEL grey-box** as an integral owner-EYE acceptance axis; reserve the §9 foundation seams as DATA. Feel needs a real GRID, not a real LEVEL — but since t-1 already builds the sandbox/grid, co-developing keeps G1=3 and gives the owner ONE place to see both "the level reads" and "the gas feels fun". Build **integer-only with a cheap 2-instance hash tripwire** so fun is judged on bit-portable behaviour. | **LEADS.** Opens with a PLAN (owner present); ADR-0010 + the tree-diff must be owner-G9-signed in/before this leg. |
| **FEEL prototype** | folded into t-1 | the §11.1 near-3D grey-box FUN test (owner-EYE, NOT unit-testable, P10) — make-or-break for the BINDING requirement (depth) vs the HUNCH (cell-size LOD). Does NOT need a separate active task (G1). Run PARALLEL to the determinism spike, capture fun as a signed PROPERTY separate from the mechanism, so a failed determinism/hangar spike re-shapes the TIER without discarding the proven fun target. | FIRST, co-developed with t-1. |
| **t-2** de-risk probe-gate / kill-gate | **re-scope** | binding KILL-GATE, scorecard re-authored for D1: (a) REPLACE reconstruction-parity probes (MOOT) with 2-machine **independent-recompute** bit-identical + checksum agreement under SimCore; (b) EXPAND to all five kernels + RED controls + a build-time **zero-float-in-authoritative-path** scan; (c) ADD a weakest-peer min-spec CPU/tick probe incl. the **hangar** case; (d) ADD a **collapse/expand idempotence + order-invariance + re-flux-aggregate-equality** probe (the linchpin, currently one line); (e) make §9.5 meaning-checksum a RED control per dimension, BEFORE the gas-sim is wired under SimCore; (f) re-home the cap-number from wire-plane units → CPU + sparse-store + snapshot-format units. | After t-1/feel (needs the lab). Binding verdict = independent fresh-session G5 refutation. |
| **t-3** host-migration spike | **re-scope** | D1 makes migration NEAR-FREE → DOWNGRADE from a heavy reconstruction spike to a cheap CONFIRMATION ("any peer becomes input-ordering authority with zero state transfer") + re-aim at the **cold/late-peer bit-exact snapshot** probe (the real residual). FOLD into t-2 to hold G1. Surface to the owner: the co-op KILLER is largely dissolved. | Folded into t-2. No longer a Wave-B-gating heavy spike. |
| **c-visual-001** Track V P1 | **keep** | grid→GPU read-only pipe over RN1, decoupled, develops on fake data. UNCHANGED; only the swap-target note changes (sparse dominant-gas cell field + near-3D, not a front). | Parallel track ~40-60 min/day, after the design/feel pass. |

## 5. §9 seams to reserve — and which are LOCK-touching (need ADR-0010)

| seam | where | LOCK-touching? |
|---|---|---|
| §9.3 integer flux-register per EDGE day-one | t-1 foundation | no — but foundation-first, non-negotiable timing (substrate for collapse/expand + active-front) |
| §9.2 representation_tag + resolution_tag per region | t-1 (sandbox carries per-region tags + renders near-3D) | no — but the backbone of D2; coordinate with §9.5 |
| §9.1 opening-AREA in the flow law | t-1 foundation | no (additive) — owner-BINDING (R-AREA-ALWAYS); land day-one or every later breach/vent inherits the size-blind bug |
| §9.4 collapse()/expand() as the ONLY conversion path | reserve Wave A, prove Wave B | no by itself, architecturally central — define the idempotence invariant before any 2nd tier |
| **§9.5 checksum-covers-MEANING** | t-1/t-2 RED control per dimension | **YES** — under D1 the checksum is the SOLE desync detector; widening it changes the determinism contract → ADR-0010, BEFORE any LOD/wake feature |
| §9.8 ChunkEncoder (byte)c guard | FIX NOW (t-1/Wave A) | LOCK-adjacent — repurposed to the snapshot/late-join path; bugfix isn't a model change but record the repurposing in ADR-0010 |
| **§9.6 temperature = {energy_sum, capacity_sum}** | Wave-A data-shape decision | **YES** — re-shapes the LOCKed/replicated plane-6; needed for idempotent collapse; coordinate with the per-species-temperature keep-open re-expressed in STORE/checksum terms (not wire-plane) |
| §9.7 FluxAcross(opening,rev) + separate player-kinematics hash | reserve NOW (don't build); decide before the first force mechanic | LOCK-adjacent — the gas checksum does NOT catch player kinematics → a future force mechanic can desync invisibly; named-now, ADR when it lands |
| §9.9 edge attributes (one-way mask, conductivity, blast threshold) | reserve schema headroom in t-1; populate Wave C/D | no (unless replicated in snapshots — note in ADR snapshot section) |
| **§9.10 plane-address headroom** | t-2 with the cap-number, in **STORE/checksum-address** terms | **YES** — the [7,chunkCount] barrier; D1 removed the wire-plane budget, so the breakdown's "reserve the plane before the wire number" fix must be re-expressed in store terms or it evaporates; any new authoritative plane = a SURFACED LOCK-EXT |

## 6. Sparring flags — the hardest tensions, surfaced loud

1. **D1 trades a SOLVED problem for a RE-OPENED one.** Wave 1+2 BUILT, PROVED gate-green, LOCKED host-broadcast replication.
   D1 supersedes exactly that and re-opens cross-CPU determinism of the WHOLE gas sim — categorically harder than the proven
   reconstruction. §14 admits the gas-sim has NEVER run under SimCore (proven only on a toy field). NOT a free upgrade.
2. **Don't re-lock D1 as gospel.** The doc says D1 is "ЗАЛОЧЕНО" but wave-map §4.3 is explicit: the BINDING requirement is
   gameplay DEPTH; the MECHANISM is the owner's LEADING HYPOTHESIS, modifiable. The doc is internally inconsistent here.
   Reword #2 as "input-lockstep is the CHOSEN model, pressure-tested in Wave A" — not a hard re-lock.
3. **"Don't break what works" — the honest ledger.** KEEP (transfers): integer water core, SimCore reducer (now load-bearing),
   determinism discipline, geometry-id, TopologyConformance, RN1, ROOM capacity. REPURPOSED: ChunkEncoder/follower codec →
   snapshot/late-join. SUPERSEDED-for-live (NOT deleted): host-broadcast authority + per-tick chunked-delta — kept in git as a
   reversible fallback. The discard is honest ONLY IF (a) the expanded determinism spike clears AND (b) D1 stays
   adopted-pending-spike. Lock D1 hard only AFTER the 2-machine kernel spike + cold-peer late-join probe + min-spec hangar probe pass.
4. **Build FEEL before FAITH — but not feel-INSTEAD-of-faith.** The fun grey-box is rightly first, but if fun is validated on
   near-3D behaviour the later spike proves non-bit-portable/unaffordable, fun locks onto a mechanism that can't ship. Mitigation:
   integer-only grey-box + a cheap 2-instance hash tripwire + capture fun as a PROPERTY separate from the mechanism.
5. **Late-join serialization is quietly re-opened.** D1 removes the PER-TICK wire, NOT full-state serialization: a mid-session
   joiner needs a SNAPSHOT (the repurposed ChunkEncoder, inheriting the (byte)c overflow at 300 rooms). Flag before Wave D.
6. **3D-near in a big HANGAR is an unbounded-cost hole, and D1 makes it WORSE** (~256k cells at 25 cm, paid on EVERY peer,
   bounded by the weakest laptop, no degradation path). Promote from "open item" to a Wave-A kill-probe; the likely fix
   (near-tier cell SIZE scales up in large open volumes — still "one model, cell-size LOD") must be designed + no-pop proven.
7. **The candidate breakdown-v1 is STALE** (its KEEP list names host-broadcast reconstruction; its DAG is host-shared-field).
   Do not approve as-is — reconcile to D1 first (this doc).
8. **WIP + milestone honesty.** active_tasks is already at G1=3 (t-1/t-2/t-3). Naively adding a feel leg = 4 = a G1 violation →
   fold feel into t-1, fold the near-free migration confirm into t-2. The 2026-07-24 A→B milestone risks becoming a MOVED WALL
   because D1 adds determinism + CPU + meaning-checksum + collapse/expand + feel scope to a pre-D1 wave: move the TAIL (de-scope
   where-is-gas feature depth past 07-24), not the wall.

## 7. Recommended FIRST CALL (draft — gated on §8 sign-off)

- **leg:** t-1 (re-issued / hardened) — generator-blind GEOMETRY reader + test LAB + near-3D FEEL grey-box.
- **goal (outcome):** a sandbox where the owner SEES real near-field 3D gas behave on a real generated level — crawls, pools,
  drains, stratifies by height; a door/vent visibly gates flow; a wall blocks; the SAME reader reads a DA-generated AND a
  hand-placed level identically — and where Claude drives saved-DATA scenarios + dumps structured per-tick snapshots.
- **done_when:** (1) ONE harness scene, scenario from a DATA asset, Play → gizmos show level→topology→grid; pause/step/tick-rate +
  snapshot work. (2) reader generator-blind (marker=WHAT; bounds/sill/connectivity DERIVED; a too-short room = an admission ERROR
  via TopologyConformance, never a silent VScale stretch). (3) **OWNER-EYE (binding, non-unit-testable, P10):** near-field 3D
  grey-box — gas crawl/pool/drain, one telegraphed reaction blink-then-bang, a vent pull — owner renders "is this FUN / worth the
  engine spend?", owner-run, no self-marking. (4) §9 foundation seams present as DATA day-one (§5). Built **integer-only** with a
  **cheap 2-instance per-tick hash tripwire** on the grey-box kernels (fun judged on bit-portable behaviour).
- **boundaries:** DO NOT crack the LOCK silently — D1/D2 supersession recorded as **ADR-0010**, owner-G9-signed in the tree-diff
  BEFORE lockstep wiring is trusted; host-broadcast stays in git as a reversible fallback. DO NOT re-lock D1 as gospel (leading
  hypothesis; binding = depth). KEEP the proven sim + TopologyDocument + TopologyConformance + RN1 + ROOM capacity; DELETE
  SnapGridFlowRoomReader + VScale + DA-internal-model reading. NO features (front/reactions/destructibility = later waves).
  Owner-run Unity steps NOT done until the owner confirms. Render/feel grey-box lives in the GasCoopGame render layer, never the
  gated Core.
- **approach token:** `geometry-derived-generator-blind-reader + feel-first-grey-box (integer-only, 2-instance determinism tripwire) + §9 foundation seams as DATA`.

## 8. Open questions for the owner (batched — G7)

1. **G9 sign-off on the tree-diff (§2):** approve rewording g-9c41 #2 (→ input-lockstep) + #9 (→ weakest-peer-CPU-bound) + the
   goal/#3/#10/#11 reconciliation, recorded under ADR-0010 superseding ADR-0004/0005's authority assumption? (Same gate the A+
   re-frame #11 passed.)
2. **Is D1 LOCKED or adopted-PENDING the Wave-A spikes?** Rec = **adopted-pending** — keep host-broadcast in git as a reversible
   fallback until the 2-machine kernel-determinism spike + cold-peer late-join probe + min-spec hangar probe pass.
3. **Player-count range:** goal says 2-4; R2/§8/host-resilience assume 4-8 (you've said up to 8). State the supported range once
   (1..N) so the CPU budget + snapshot obligation are sized right.
4. **Late-join for real co-op:** under lockstep a mid-session joiner needs a snapshot. Save/load is currently CUT ("ephemeral").
   Name late-join-via-snapshot a real Wave-D obligation now (plan the repurposed codec + its (byte)c bugfix), or is mid-session
   join out of scope for the first playable?
5. **2026-07-24 A→B milestone:** D1 adds real determinism/CPU/feel scope to a pre-D1 wave. Move the TAIL (de-scope "where-is-gas"
   feature depth past 07-24; keep lab + de-risk + composed-LOD proof + feel), or hold the date and cut elsewhere?
6. **Scale UNITS for #9:** ~300 real rooms (R17) vs ≥1000 volumes (tree). Which is authoritative for the weakest-peer-CPU budget,
   and the volumes-per-room factor? (Also informs tier radii / cell sizes left open in doc §13.)

## 9. Owner decisions + methodology steer (2026-06-22, session continued — co-creation, pending the closing RESULT)

FIRM (owner-stated; to enter decision_inbox at the closing RESULT):
- **NO LATE-JOIN (firm).** Players assemble in a LOBBY/BASE; press Start → the raid/expedition begins with whoever is present.
  Nobody joins mid-raid. Missed the start → you don't enter THIS raid (can join the base, not the running raid). Later we MAY
  add join; not now. → KILLS the late-join snapshot obligation for the first game; base↔raid is a clean session boundary.
  (Owner: "запиши, запомни".)
- **ZERO-LEGACY AT COMPLETION (hard requirement).** When a piece is done, NO legacy/unused code remains in the working tree —
  it must be clean. Reason: leftover code pollutes context + degrades the AI assistants. Conditional-delete (keep in git as
  rollback until the replacement's 2-machine spike passes) is OK only as a TRANSIENT; the END STATE is clean. Tests likely need
  full review or rewrite — do not drag stale tests. (Owner.)
- **GRAPH re-role AGREED** (owner "с тобой согласен"): rooms = LABEL everywhere, PIPE dropped at near (grid-vs-graph-resolution §1).
- Conditional-delete discipline ACCEPTED with the zero-legacy-end caveat above.

CLARIFIED-PENDING (owner asked for plain re-explanation; not yet signed): decision-1 (pipe-out / label-everywhere) +
decision-3 (re-flux / no-pop door-flux) — re-explained simply in chat; awaiting owner OK.

METHODOLOGY STEER UNDER DISCUSSION (owner proposal, pressure-tested): shift g-9c41 from "build core → then promo" to
INCREMENTAL VISIBLE SLICES — a spine of small, showable, deterministic gas-GAMEPLAY slices on the test sandbox, each adding one
high-leverage gas capability; audience/devlog (seed) + lore run in PARALLEL from early; storefront still gated on visual identity.
Critique surfaced 3 guards: (a) foundation de-risk (the binding determinism / re-flux probes) woven into the FIRST slices, not
deferred — else a demo pile on sand = the rebuild trap; (b) early marketing = DEVLOG / systems-sim seed channel (raw tech is the
draw there), NOT a premature Steam page/capsule (that needs the visual identity, burns the one-time impression); (c) bound the
feature set + keep a THIN GAME FRAME (players, a room, danger, a goal) so each slice reads as the FANTASY, not gas-in-a-vacuum.
To be folded into the wave re-shape at the closing RESULT.

GAMEPLAY-EXPRESSIVENESS (owner asked — gameplay, not visual): walk-through-splits-a-cloud / blow-air-to-split are AUTHORITATIVE
gameplay behaviors. Cheap+deterministic now: player/object DISPLACEMENT (occupied cells push gas to neighbors, mass-conserving =
the moving-geometry mechanic). The PERSISTENCE of a split (stays two clouds) + directional "blow" need the integer
momentum-drift / wind-edge-modifier layer (advection-lite, deterministic) — additive, parked (§8 ILGA is the named richer lever).
Decide HOW MUCH at the grey-box (feel-driven), don't pre-build heavy advection. Float velocity solver = OUT (non-deterministic).

END_OF_FILE: live/indie-game-development/work/aplus-replan-under-locked-arch-v1.md
