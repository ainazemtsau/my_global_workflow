# Knowledge — g-9c41 Wave 1: HOLD is a recovery MECHANISM (scene-size-independent); the lossy bandwidth projection is keyframe-blind

Established: 2026-06-16, review c-review-001 (independent G5 refutation of the Wave-1 kill-gate).

- The kill-gate **HOLD** is a **recovery-mechanism predicate** (per-tick bit-exact at settle under
  drop+delay+reorder, plus deferred-chunk backlog drain), **independently re-derivable from the committed
  lossless telemetry series alone** (no trust in the `clampVerdict` flag) and **scene-size-independent**.
  It is correctly NOT a throughput-at-scale proof. Verified: lossless 6/6 settles bit-exact, 0 bad settles in
  the steady window [301,900), backlog peak 4 drains within D=4 each cycle; negative control (resync keyframe
  off) trips a real BLOWN; live gate dotnet 103/103.
- The **lossless** projection (~4 899 cells @275 KB/s) is **conservative** (it scales offered demand 1796 B/s,
  which exceeds on-wire 1311 B/s).
- The **lossy** projection (~59 060 cells @275 KB/s) is **~5.3× OPTIMISTIC**: the harness divides by OFFERED
  demand (149 B/s) but the real lossy ON-WIRE rate is 793 B/s — the **on-quiesce full-INT32 resync keyframe**
  dominates the lossy wire and **scales with cell count**. Honest on-wire lossy basis ≈ **11 097 cells**.
- **Rule for Wave 2:** size the coarse-tier grid against the **on-wire keyframe-inclusive** budget (~11k lossy
  cells), NOT the 59k face value. The resync keyframe is also the **co-op late-join / desync-recovery path**,
  so this matters doubly for a co-op-first game.
- Folded into TREE g-9c41 criterion 9 (owner-approved 2026-06-16).

read_by: |
  converge / converge-arch when shaping g-9c41 Wave 2 grid sizing (the binding sizing input); the
  technical-feasibility and scope/production lenses when sizing the coarse tier against criterion 9.

related: [[gascoopgame-engineering-model-routing]]

END_OF_FILE: live/indie-game-development/knowledge/g9c41-wave1-hold-mechanism-lossy-projection.md
