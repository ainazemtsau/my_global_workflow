# RESULT — s-work-011 (g-9c41 Wave 2): triage 2 Codex reviews → frame c-exec-009 consolidation+hardening leg; repair stale t-3/t-4 sequencing

direction indie-game-development / bet g-9c41 / Wave 2 / play work (executor-leg framing, owner present).

## outcome

- TWO owner-pasted Codex reviews (review #1 correctness/robustness; review #2 structural/architecture) TRIAGED into ONE review-driven CONSOLIDATION+HARDENING executor leg **c-exec-009** (new task t-5), framed + adversarially red-teamed (workflow wf_619b23cd, verdict SOUND-WITH-FIXES, 6 gaps folded), owner «го».
- **REPAIR (stale input):** the handed CALL ("frame+open the next Wave-2 leg; owner picks t-3/t-4 sequencing, rec t-4") was STALE — it predated **s-work-010**, which had already answered d-wave2-seq-001 = **C** (run t-3 ∥ t-4) and OPENED both legs (c-exec-007 t-3, c-exec-008 t-4 with owner R1/R2/R3). Caught it by re-reading committed NOW.md (`git show HEAD:NOW.md`, HEAD da5a195) before writing; did NOT re-litigate the sequencing or duplicate s-work-010's work. (This worktree has concurrent OS sessions; a handed CALL can lag the committed state.)
- Surfaced previously-SHADOW dev work: GasCoopGame_dev advanced UNPUSHED past 7987506 to **3be28df** (4 tooling commits: 166d159 scaffold-noise / 5393c84 debug-tooling restriction / e58a33d MCP player-strip / 3be28df NuGet-meta) + an uncommitted **ADR-0008 replication-seam→Core move** (read-only headless gate = build 0/0, **372/372**, hygiene OK; coherent — **KEEP, no revert**).
- Triage of ~16 findings: **3 confirm-only** (P0 STALE = all 4 leg-8 artifacts exist + c-exec-006 archived; MCP-strip already durable @e58a33d via IFilterBuildAssemblies; the ADR-0008 seam move = keep, confirm through the gate); **3 fix-now** through the contour (FieldDelta validate-before-mutate; chunk apply-before-advance; StableId→Core+conformance — all `no-silent-state-corruption`, each red-test-first by an independent test-author + ENROLLED as a frozen change with its own mutation-<id>.json ≥ floor); **5 named owner-ack deferrals**; rest hygiene.
- **SEQUENCING corrected:** c-exec-009 LEADS Wave-2; **t-4 (c-exec-008, render + real DA) CONTINUES ∥** (untouched by both reviews — render path, reads the FROZEN RN1); **t-3 (c-exec-007) HELD** pending the clean baseline (it edits the Core/Field + Coarse/Replication seam the ADR-0008 move + the 3 fixes touch — direct collision).

## evidence

- Committed state verified: `git show HEAD:NOW.md` → t-3/t-4 active, d-wave2-seq-001 answered C, c-exec-007/008 open (HEAD da5a195, worktree clean).
- GasCoopGame_dev read-only inspection (workflow inspect agent + my own git/glob): dev HEAD 3be28df (4 tooling commits since 7987506) + dirty ADR-0008 move; headless gate build 0/0, 372/372, hygiene OK; the 4 leg-8 artifacts present; c-exec-006 change archived; canonical spec openspec/specs/sim-core/spec.md present.
- Red-team verdict SOUND-WITH-FIXES; all 6 gaps folded into the CALL below (per-change mutation enrollment; R13/R14 no-engine-refs proof; v7 over ALL promises; _Recovery untracked-disk-delete vs slnx git-rm; path/namespace precision; PlayMode-hygiene scan-scope statement).
- No code/spec touched in GasCoopGame this session (framing + triage only). The builder executes c-exec-009.

## state_changes

- NOW.md active_bet.phase: appended the 2026-06-19 s-work-011 line.
- NOW.md active_tasks: added **t-5** (consolidation+hardening, active, opened as c-exec-009); **t-3 → blocked_on c-exec-009** (HELD). t-4 unchanged (active).
- NOW.md open_calls: added **c-exec-009** (open, full note); **c-exec-007 → held** (note).
- NOW.md next: replaced — RUN c-exec-009 (leads) ∥ c-exec-008 continues; c-exec-007 held; push owner-gated.
- d-wave2-seq-001 left ANSWERED (C) — not re-opened.
- LOG.md: appended the s-work-011 line.

## captures

- The owner's default fix-method (one finding per chat + a custom instruction) = the review→fix STAIRCASE; the corrective is ONE batched gated hardening leg (classify-by-invariant + red-test-first + gate + G5). Saved to auto-memory.
- This worktree runs CONCURRENT OS sessions (s-work-010, s-canon-008 committed during this session) → a handed CALL can be stale; re-verify committed NOW.md / git HEAD against the CALL before acting or writing. Saved to auto-memory.

## decisions_needed

- none — owner already «го» on the plan; the sequencing was REPAIRED against committed state, not re-decided.

## play_check

- "1 Recite — done: restated the Wave-2 bet, the two reviews, and the in-flight state."
- "2 Owner inputs — engineering leg, not owner-content; owner present for the triage + «го» (owner words: «го»; earlier «по нашей инструкции … не просто пластырь … только потом запускать задачи»)."
- "3 Do the work — framed c-exec-009 via a triage + red-team workflow; repaired the stale sequencing against committed NOW.md."
- "4 Self-check — red-team verified the CALL (6 gaps folded); re-read committed NOW.md/git HEAD to avoid a bad write (caught the stale CALL)."
- "5 Close — RESULT; next = run c-exec-009 ∥ c-exec-008, hold c-exec-007."

## log

work (g-9c41/Wave2, s-work-011): 2 Codex reviews triaged → c-exec-009 consolidation+hardening leg framed + red-teamed (wf_619b23cd); repaired stale t-3/t-4 sequencing (s-work-010 already opened both); t-5 added, t-3 HELD, t-4 ∥, c-exec-009 leads.

## next

Run c-exec-009 (t-5) in GasCoopGame ∥ c-exec-008 (t-4); hold c-exec-007 (t-3) until the clean baseline; then review the Wave-2 node. Full CALL below.

---

## §c-exec-009 — full CALL

```
CALL c-exec-009 (GasCoopGame_dev / sim-core hardening + boundary-correction consolidation)

GOAL
Land ONE clean, gate-green, owner-acked dev baseline that (1) consolidates the in-flight ADR-0008 coarse-replication-seam->Core move plus the 4 already-committed Unity-tooling cleanup commits into a coherent dev tip with nothing correct lost; (2) fixes — THROUGH the gated contour — the two Core atomicity defects and the StableId-derivation seam-leak surfaced by both reviews; (3) batches all hygiene; (4) carries every out-of-scope finding as a NAMED owner-ack deferral, never a silent drop. Binding verdict is a FRESH-SESSION G5 refutation on the hardened tree.

CONTEXT
- Committed dev HEAD = 3be28df (4 unpushed tooling commits already landed: 166d159 scaffold-noise, 5393c84 debug-tooling restriction, e58a33d build-strip IFilterBuildAssemblies, 3be28df NuGet-meta baseline). main = ce79e10 (behind dev). Canonical spec = openspec/specs/sim-core/spec.md.
- Working tree is DIRTY but COHERENT and headless-gate-green (verified read-only: core boundary build 0warn/0err, 372/372 tests, hygiene OK): the ADR-0008 move renamed ICoarseChunkLink / LoopbackCoarseChunkHub / CoarseChunkFollower from Adapters/GasDebug into Core/Field/Coarse/Replication (GUIDs preserved; the moved follower KEEPS namespace GasCoopGame.Core.Field.Coarse even though it sits under the Replication/ folder), deleted the redundant FishNetCoarseChunkLink wrapper, made FishNetChunkChannel ': ICoarseChunkLink' directly, added ADR-0008 + Replication.meta + RESULT.md/FRICTION.md edits. KEEP all of it — there is NO revert candidate. Staging is split (renames staged, content-edits unstaged) — a commit-hygiene artifact only.
- core/GasCoopGame.Core.csproj GLOBS ..\Assets\GasCoopGame\Core\**\*.cs, so the moved seam/follower files are already in the headless build — which is WHY the tree is headless-green. A boundary regression (an engine using-directive in a moved file) would not surface unless explicitly checked — see BOUNDARIES + done_when #1b.
- Two reviews triaged: R2's two P1s are NOT open (replication move = the ADR-0008 work already-in-progress; MCP/NuGet tooling = already fixed durably in e58a33d via StripAgentToolingFromBuild.cs + hygiene gate — CONFIRM, do not re-open, do NOT add the rejected .meta-edit gate). R1's P0 is stale (all 4 leg-8 artifacts exist + c-exec-006 archived — verified).
- FIX-NOW (these are CHANGES -> same gated contour, red-test-first, classify by invariant, NO symptom hotfix). Each must be ENROLLED as a frozen change in validation.config with its OWN recorded docs/measurements/mutation-<id>.json (>= mutation_kill_floor) — else -Deliver passes without mutation-testing it:
  1. FieldDelta.Apply (Core/Field/FieldDelta.cs) — mutate-before-validate: the state.Set loop runs with no precheck of ChangedIndices/ChangedZones length-equality or index-range -> a mismatched-length or out-of-range delta throws mid-loop after partial mutation. Invariant: no-silent-state-corruption.
  2. RevisionBarrier.TryAccept + ChunkDecoder.Apply + CoarseChunkFollower.Apply (Core/Field/Events/RevisionBarrier.cs, Core/Field/Chunks/ChunkDecoder.cs, Core/Field/Coarse/Replication/CoarseChunkFollower.cs) — advance-before-apply: CoarseChunkFollower.Apply calls _barrier.TryAccept (advances high-water and returns true) BEFORE ChunkDecoder.Apply, which can throw on a short/out-of-range payload — leaving the follower partial AND the high-water past a never-applied chunk, so the correct re-send is permanently rejected. Invariant: no-silent-state-corruption.
  3. StableId derivation (Adapters/Topology/TopologyIds.cs) — adapter-owned law; Core/Field/Topology/Coarse/TopologyConformance.cs checks StableId UNIQUENESS only, never id == derive(geometry), so a divergent adapter derivation silently corrupts the canonical topology replication keys on. Move the derivation into Core/Field/Topology, adapter calls it, add a derive-mismatch check to TopologyConformance.Check. Invariant: no-silent-state-corruption / determinism. NO formula-duplication band-aid.
- All three fix-now items live in the same Core seam ADR-0008 is moving -> fold into the SAME structural leg, share ONE fresh-session G5.
- HYGIENE to batch: AGENTS.md one-line bless of Assets/GasCoopGame/Net as the transport-edge root (UnityEngine-allowed, same as Adapters) — do NOT physically move FishNet; GasDebug FishNet private-field reflection wrapped in a version-checked debug bootstrap that throws on field-shape drift (GasDebug asmdef is already autoReferenced:false — do not chase that stale claim); replace blanket LogAssert.ignoreFailingMessages=true with targeted LogAssert.Expect in the FishNet PlayMode tests; DELETE the on-disk Assets/_Recovery/ dir (it is UNTRACKED on disk, NOT git-cached — a disk delete, not git rm) and add a hygiene.ps1 scaffold-dir rule; git rm --cached GasCoopGame.slnx (it IS tracked despite .gitignore *.slnx — keep file on disk); fix swapped expected/actual at CoarseBreachReplicationTests.cs:105 + CoarseParityAndAdditiveTests.cs:184; extend tools/hygiene.ps1 to flag runtime Assert.Ignore/Assert.Assume in test bodies AND _Recovery/_scratch_* scaffold dirs — and STATE which file-set hygiene.ps1 scans: if the PlayMode tests under Net/ are outside the headless scan, the runtime-Assert.Ignore rider is owner-run-verified and the binding artifact for the UDP path stays the YELLOW-not-green report.

BOUNDARIES
- R13 sim core = pure C#, zero Unity refs, headless. R14 networking = edge wrapper only; only the socket-bound FishNet impl is edge. R12 one host, no dedicated server. The moved seam/loopback/follower stay in Core and MUST compile under core/GasCoopGame.Core.csproj with noEngineReferences:true AND carry ZERO UnityEngine/FishNet using-directives (the mechanical R13/R14 proof — do not rely on 'it builds headless', the csproj auto-globs them).
- "A FIX IS A CHANGE": every fix-now item rides the full contour — INDEPENDENT test-author writes the RED test FIRST from the spec (builder cannot edit it), classify by the invariant it restores, NO in-session symptom band-aid. Hygiene is not a fix and needs no new test-author, but must not regress the gate.
- Do NOT touch LOCKed codec/barrier/hash BEHAVIOUR — these fixes add validation/ordering guards only; host->2-client bit-exact acceptance must stay byte-identical. Do NOT re-do the ADR-0008 move or re-open the MCP/NuGet strip. Do NOT build anything in the deferred classes.
- Do NOT push (owner-gated). Do NOT self-mark the owner-run Unity gate as done.
- Run the gate explicitly: powershell -NoProfile -ExecutionPolicy Bypass -File tools/check.ps1 (and -Deliver). pwsh7 is not on PATH; check.ps1 is 5.1-compatible.

DONE_WHEN (each item VERIFIABLE with named evidence)
1. Consolidated baseline: the ADR-0008 changeset committed as ONE coherent boundary-correction commit (renames + same-file content edits + ADR-0008 doc + Replication.meta + RESULT.md/FRICTION.md together), on top of the 4 kept tooling commits. Evidence: git status clean; git log --oneline tidy tip; git show --stat of the seam commit lists the moved Core types (GUIDs preserved), the deleted FishNetCoarseChunkLink, the FishNetChunkChannel ': ICoarseChunkLink' edit.
1b. R13/R14 mechanical proof: the moved Core/Field/Coarse/Replication/* types compile under core/GasCoopGame.Core.csproj with noEngineReferences:true and contain ZERO UnityEngine/FishNet using-directives. Evidence: headless build transcript + a grep over the three moved files showing no engine refs.
2. Gate-honesty proven: tools/check.ps1 -Deliver GREEN on a CLEAN tree; transcript attached to RESULT.md. Confirms R1-P0 was the dirty tree, not a delivery lie.
3. FieldDelta.Apply fix: an INDEPENDENT-authored RED test (mismatched-length / out-of-range ChangedIndices -> assert follower state untouched, no partial Set) red pre-fix, green post-fix; validation precedes the first state.Set. Evidence: test name + pre/post run, classified no-silent-state-corruption; change enrolled in validation.config with mutation-<id>.json >= floor.
4. Chunk apply-before-advance fix: an INDEPENDENT-authored RED test (short/out-of-range chunk payload -> assert reconstruction array UNCHANGED AND barrier high-water NOT advanced, and the correct re-send still accepted) red pre-fix, green post-fix. Evidence: test name + pre/post run; change enrolled with mutation-<id>.json >= floor.
5. StableId derivation fix: an INDEPENDENT-authored RED test (geometry whose adapter-emitted StableId != core-derived id -> assert TopologyConformance REJECTS) red pre-fix, green post-fix; derivation now lives in Core/Field/Topology and the adapter calls it (no duplicated formula). Evidence: test name + pre/post run + the file move; change enrolled with mutation-<id>.json >= floor.
6. Hygiene batch landed and verified: AGENTS.md Net-edge-root line present; GasDebug reflection bootstrap throws on field-shape drift; LogAssert blanket-suppression replaced with targeted Expect; Assets/_Recovery deleted from disk (test -d Assets/_Recovery is false) and a hygiene.ps1 scaffold-dir rule flags it; git ls-files GasCoopGame.slnx empty (file still on disk); both swapped asserts corrected; hygiene.ps1 now flags runtime Assert.Ignore/Assert.Assume + _Recovery/_scratch_* (a deliberate probe line is flagged, then removed; plus a statement of which file-set is scanned). No NUnit analyzer warnings at the two sites.
7. Full close on a clean tree: tools/check.ps1 -Deliver GREEN; the strong-check enablement section shows ALL THREE new change-ids with recorded mutation scores >= mutation_kill_floor (not just an aggregate suite pass); deliverable-coverage v7 disposed for ALL TEN done_when promises (each -> a real existence artifact — including #1 = the seam commit git show --stat and #2 = the attached clean-tree -Deliver transcript); spec-silence audit clean.
8. Defer list carried as NAMED owner-ack deferrals in RESULT.md (untrusted-peer/PeerId-spoofing; topology int-overflow on pathological volumes — name the real location TopologyDocument.cs MaxX/Y/Z = Min+Extent-1 unchecked int; broadcast-registration leak on reconnect/late-join; real-UDP FishNet env-blocked/owner-run with the YELLOW-not-green reporting rider; CoarseReconstructionHarness.Follower 2nd-source-of-truth Constitution-#3 follow-on) — each named, owner-acked, not-built-now.
9. Binding verdict: a FRESH-SESSION G5 refutation (different model, tries to REFUTE) ran on the HARDENED committed tree and failed to refute. Evidence: the refutation note in RESULT.md stating it was a fresh session, not an in-session pre-pass.
10. RESULT.md reconciled to the ACTUAL delivered state, trailers maintained.

RETURN
A RESULT packet with: the consolidated git shape (commit list, status clean); the -Deliver green transcript (build/test/hygiene/coverage/per-change mutation); for each of the 3 fixes the independent RED-test name + pre/post-fix run + the invariant it restored + its change-id and recorded mutation score; the R13/R14 no-engine-refs proof for the moved files; the hygiene checklist with evidence; the NAMED defer list; the fresh-session G5 refutation outcome; and the TWO owner-gated blockers stated explicitly and NOT self-resolved: (i) Unity-side compile + PlayMode CoarseVisibleSliceReplicationTests re-run via MCP (edge FishNetChunkChannel change under Net/, excluded from the headless csproj — a real open owner-run gate; not done until the owner confirms), (ii) real-UDP FishNet stays deferred (WSAENOBUFS), loopback is the binding transport. Hand back the next CALL = after owner confirms (i) and acks the defer list, single merge dev->main then owner-gated push.

BUDGET
One leg. 3 fix-now changes (each with one independent RED test + a validation.config enrollment + a recorded mutation-<id>.json) + hygiene batch + consolidation commit + one fresh-session G5. No new feature work, no deferred-class work, no git surgery beyond restage+commit of existing coherent WIP. If any fix-now item proves larger than a guarded validation/ordering change (e.g. the StableId move ripples beyond TopologyConformance), STOP and return a conflict rather than expanding scope.
```

END_OF_FILE: live/indie-game-development/history/s-work-011.md
