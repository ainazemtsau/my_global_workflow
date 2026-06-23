# g-9c41 — LOCKED architecture + slice methodology (accepted 2026-06-22, owner «да»)

> 🔵 **УТОЧНЕНИЕ (s-research-017, 2026-06-22; POINTER, НЕ правка лока).** Пункт 2 «cell-SIZE LOD» и пункт 3 (пузырь/discard)
> УТОЧНЕНЫ синтезом `work/gas-cellsize-levelscale-2026-06-22.md` §10-§12: газ = **50см ГЛОБАЛЬНО** (авторитетная ось LOD =
> ПРОСТРАНСТВЕННЫЙ room-rollup, НЕ покомнатный cell-SIZE; cross-resolution re-flux шов убран); 25см = off-checksum визуал +
> авторитетные высотные полосы. Залоченные факты этим указателем НЕ изменены; формальная ратификация уточнения в лок =
> owner-signed re-shape (отдельная сессия).

**Who reads this / when:** EVERY g-9c41 build session, at its PLAN, before any design — it is a mandatory ingest. The full
spec + slice graph + decision index is the SINGLE entry point: `work/dev-plan-graph-2026-06-22.md`.

## Accepted facts (LOCKED — change only via review/maintenance, never silently)

1. **NETCODE = input-lockstep** (D1): only player inputs cross the wire; every peer deterministically recomputes the full sim
   (integer/fixed-point + seeded RNG + pinned order + per-tick meaning-checksum; desync = loud stop). Binding scale limit =
   **weakest-peer CPU**, not bandwidth. Host-migration near-free. Supersedes ADR-0004/0005 host-broadcast authority → **ADR-0010**
   (game-repo writes it). DETERMINISM — read carefully (owner-flagged drift 2026-06-22): integer arithmetic is bit-identical
   across ALL CPUs — this is an ESTABLISHED real-world fact (banking/accounting software relies on it). We do NOT "prove" it and
   we do NOT need a second physical machine (the owner has ONE machine — that is fine). The ONLY real cross-CPU risk is a FLOAT
   sneaking into the authoritative path → caught by a build-time ZERO-FLOAT scan ON ONE MACHINE (that scan IS the cross-CPU
   guarantee, by construction). A 2-PROCESS loopback hash (two processes on the SAME one machine) is an OPTIONAL cheap tripwire
   for the OTHER bug class (non-canonical iteration order / unseeded RNG) — it is NOT "two machines" and NOT a proof of the
   integer fact. A real 2-PHYSICAL-machine run is NEVER a gate (an optional one-off confidence check, much later, if ever). So:
   enforce integer-only + canonical order + seeded RNG (a cheap LINT); do NOT re-prove the given.

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
   every peer. Determinism is GUARANTEED BY CONSTRUCTION (integer-only; cross-CPU is GIVEN — see point 1, NOT re-proven, NO 2nd
   machine needed) and verified by the cheap ONE-MACHINE lint (zero-float scan + optional 2-process loopback hash). "Coarse the
   same on every peer" FOLLOWS from integer-only — it is not a 2-machine gate. (re-flux → owner-eye no-pop feel, EXCEPT D5
   spatial rooms / sub-room-AND-shared mechanics where it snaps back to a hard gate.) Per-mechanic depth is classified
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
