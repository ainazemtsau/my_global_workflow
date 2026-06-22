# g-9c41 — LOCKED architecture + slice methodology (accepted 2026-06-22, owner «да»)

**Who reads this / when:** EVERY g-9c41 build session, at its PLAN, before any design — it is a mandatory ingest. The full
spec + slice graph + decision index is the SINGLE entry point: `work/dev-plan-graph-2026-06-22.md`.

## Accepted facts (LOCKED — change only via review/maintenance, never silently)

1. **NETCODE = input-lockstep** (D1): only player inputs cross the wire; every peer deterministically recomputes the full sim
   (integer/fixed-point + seeded RNG + pinned order + per-tick meaning-checksum; desync = loud stop). Binding scale limit =
   **weakest-peer CPU**, not bandwidth. Host-migration near-free. Supersedes ADR-0004/0005 host-broadcast authority → **ADR-0010**
   (game-repo writes it). Determinism-by-construction = integer-only authoritative path + a build-time zero-float scan + a
   loopback hash tripwire (cross-CPU determinism is a property of OUR code staying integer-only, NOT a CPU unknown; a 2nd physical
   machine is a cheap one-off confirmation, not a gate).

2. **ONE integer cell model, cell-SIZE LOD** (D2/D3/D11): near = full-3D grid + flow through **OPEN FACES** (area = open-face
   count, real height, no-through-walls — all emergent from geometry, free; supersedes the area-blind `t=mEq/kP` near). Far =
   room-graph **ROLLUP** (portal = cut-set aggregate of open faces). **ROOM = a LABEL/partition at EVERY tier** (the transport
   "pipe" is dropped near; the partition/region_id is kept everywhere — it is already in the §3.3 checksum). Two LOD axes: cell
   SIZE and multi-cell-vs-bucket (D5 big rooms stay spatial = the second axis). collapse/expand = the only conversion path
   (discard-on-leave under the local-detail model).

3. **DETAIL = a LOCAL non-authoritative refinement of a COARSE-authoritative truth** (the cost model): the coarse (room-level)
   sim is the SOLE shared truth — computed identically on every peer, in the checksum. The detailed bubble is computed ONLY where
   a peer's own player is (~1 bubble/peer, not N — ~8× CPU win), is OFF the checksum, and never writes coarse back. Hard shared
   consequences (reactions/damage/cross-room flow/explosions) are PROMOTED to **coarse EVENTS** computed from coarse state on
   every peer. Binding determinism probe = coarse bit-identical on 2 machines (NOT re-flux; re-flux → owner-eye no-pop feel,
   EXCEPT D5 spatial rooms / sub-room-AND-shared mechanics where it snaps back to a hard gate). Per-mechanic depth is classified
   at EACH slice's PLAN into ведро-1 (washes-out = free local feel) / ведро-2 (coarse-promotable event) / ведро-3 (sub-room AND
   shared = expensive, that room runs detail on all peers). **Default = room-granular (Variant A).**

4. **sparse dominant-gas** (D9, dominant type + amount + transient mix overlay on reaction; main saving = awake-cell-sparse via
   active-front); **integer chemistry collision table** (D10); §9 implementation seams reserved as DATA day-one.

5. **NO LATE-JOIN** (firm): lobby/base → press Start → raid begins with whoever is present; no mid-raid join (later maybe). →
   no full-state snapshot obligation for the first game; base↔raid is a clean session boundary.

6. **ZERO-LEGACY at completion** (firm): when a piece is done, no unused/legacy code in the working tree (it pollutes context +
   degrades the AI assistants); rollback only via git history; tests reviewed/rewritten, not dragged.

7. **reusable-engine DROPPED** (D12) — game-first; migration is a side-effect, not a goal. carve-corridor-by-hand CUT (D13).

## Methodology (accepted)

Delivered as **incremental VISIBLE slices** (S0 foundation → S1 burst/displace → S2 multiplayer-lockstep → S3 height → S4
coarse-rollup/LOD → S5 breach → S6+ from backlog). Each slice runs its own fresh session with the ritual: PLAN
(ingests-and-applies all decision docs + classifies the slice's mechanics) → RED-first independent test-author → build
(integer-deterministic, clean/zero-legacy, maximally extensible) → gate + fresh-session G5 → **owner-VISIBLE result** (debug
gizmo early, polished later; the slice is not closed until the owner SEES it) → integrate + promote new facts here. Slices are
TASKS (rolling wave), never tree nodes. marketing/devlog ([[marketing-we-are-nobody-is-starting-point]]) + lore run in parallel;
storefront gated on visual identity.

Relates to: [[g9c41-wave2-aplus-over-b-code-grounded]], [[g9c41-wave2-gload-probes-incomplete-plus4]],
[[g9c41-wave2-coarse-proof-not-resolution]], [[mechanic-lenses]].

END_OF_FILE: live/indie-game-development/knowledge/g9c41-architecture-locked-slices.md
