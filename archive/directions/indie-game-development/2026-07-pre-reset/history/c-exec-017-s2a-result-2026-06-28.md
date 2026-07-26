# c-exec-017 (S2a) RESULT — imported + reconciled — ZERO-LEGACY reconstruction-spine retirement

Imported + verified first-hand 2026-06-28 by s-work-026 from the GasCoopGame_dev build session. Source of truth =
GasCoopGame `dev` RESULT.md @ commit `ec54d4f`. S2a = the first half of the S2 split (d-s2-split-001).

## outcome (builder, verified)

ZERO-LEGACY retirement of the host-authoritative reconstruction spine, under input-lockstep. NO new behaviour.
**Status: DELIVERED — binding gates green on `dev`; merge dev→main + push are OWNER-GATED (pending).**

done_when 0–7 all reported met:
- 0 — Step-0 housekeeping: archived c-014/c-015 openspec (`f7e0146`). [NB: the "FF dev→main" framing is now stale — see reconciliation #2.]
- 1 — DELETE both families re-verified first-hand (19 prod .cs+.meta; 7-agent sweep proved 0 live non-test consumers).
- 2 — KEEP intact + pruned (FieldState/FieldStep de-host-authoritative-ified; dead EnsureWireEncodable/BarrierLayerCount removed; far-tier/input-bus untouched).
- 3 — tests rewritten not dragged (48 suites; 857/857 headless green; survivors extracted: mass+breach, DW9, AssertAdmitted helper).
- 4 — §7-burial re-check: no BandCount=2 authoritative-collapse coupling remains (G5-confirmed).
- 5 — check.ps1 -Deliver GREEN ("OK: all gates green" — build + 857 + scans + mutation 87.96% + spec-silence + coverage 8/8 + hygiene).
- 6 — ZERO-LEGACY 3-lens audit: production 0 / tests 0 / live-docs 0; no orphaned .meta/empty dirs.
- 7 — fresh-session G5: COULD-NOT-REFUTE all 3 lenses (delete/keep boundary, tests-rewritten, §7-burial).

Commits on dev: f7e0146 (housekeeping) → 8c020e8 (delete+prune+test-rewrite) → 4cfc7b0 (docs/ADR/openspec/RESULT) →
**ec54d4f (ADR renumber 0015→0016)**.

## first-hand verification (s-work-026, in the dev worktree)

- **Deletes real:** grep of Assets/**.cs (non-test) for CoarseChunkFollower / IFieldStateChannel / FieldSnapshot /
  FieldStreamDriver / FieldHost / ChunkEncoder / RevisionBarrier = **0 production files each.** ✅ (a deletion leg's
  deliverable IS the absence — confirmed.)
- **RESULT.md** on dev = "DELIVERED (gates green on dev); merge dev→main + push OWNER-GATED." ✅
- Gate numbers (857/857, -Deliver GREEN, mutation 87.96%, coverage 8/8) accepted from RESULT.md + the build session's
  fresh-session G5 COULD-NOT-REFUTE (the binding refutation; not re-run from the OS repo — that is the build-env's domain).

## RECONCILIATIONS — the pasted builder report was slightly stale vs the committed tip

1. **dev HEAD = ec54d4f, NOT 4cfc7b0** (the report's tip). A later commit renumbered the retirement ADR **0015 → 0016**
   to avoid a collision with c-visual-001 S5 (which merged to main using ADR-0015). The retirement ADR is **ADR-0016**.
2. **dev→main is NO LONGER a clean fast-forward.** Since the c-016 PLAN's "dev⊆main" snapshot, the parallel VISUAL track
   merged S5 to main (main is now `9780713`). `main…dev` = 2 / 4 → a **real merge** (conflict-free expected: S2a touches
   Core/Field reconstruction, the visual track touches the Render layer). The owner-gated merge must account for this.
3. **ADR CITATION ERROR — verified, real (planner item the builder flagged):** the actual repo ADR files are
   **ADR-0002 = "Network determinism: lockstep over FishNet (input-bus only)"** (THE input-lockstep lock) and
   **ADR-0010 = "Test sandbox: scenario-as-DATA (Wave A, t-1)"**. The CANON (g9c41-gas-engine-SPEC.md Факт-1/§2/§6/§7) and
   the c-016/c-017 CALLs derived from it cite the lock as **"ADR-0010"** — which is WRONG (that's the test-sandbox ADR).
   The lock is **ADR-0002**. ADR-0016 records the correction repo-side. The canon citation fix is owner-gated →
   d-adr-lockstep-citation-001. (Semantics of the lock are unchanged — pure citation/label error.)

## carried deferrals / notes

- **Chunk-span geometry retained (deferred to S4):** CoarseChunkSpan / IsWireEncodable / ChunkSpan / ChunkCount are now
  wire-purposeless but still have surviving FAR-TIER consumers → KEPT this leg; full excision flagged for the S4 cleanup.
- **Env:** the build env had no pwsh7 → gates ran under PowerShell 5.1 (parsed + ran clean; stryker 4.6.0). Owner re-run on
  pwsh should be identical. Deleted an untracked Assets/_Recovery/ Unity auto-recovery scaffold to pass hygiene (owner
  precedent c-012).

## owner-gated (pending)

- Owner-eye (confidence, NOT a gate): `dotnet test GasCoopGame.Core.slnx -c Release` → 857/857 on the retired tree.
- Optional MCP PlayMode: FishNetConvergenceTests (the DW9 input-bus survivor).
- **Merge dev→main + push** — NOT done (now a real merge, see reconciliation #2).

## next

The direction owns the next CALL = S2b / c-exec-018 (the load-bearing loopback proof), which builds on this clean base.
It MUST cite ADR-0002 (not ADR-0010) for the lock, and carry the chunk-span S4-deferral forward.

END_OF_FILE: live/indie-game-development/history/c-exec-017-s2a-result-2026-06-28.md
