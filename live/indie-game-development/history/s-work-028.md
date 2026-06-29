# s-work-028 — writer (g-9c41 / S2): apply the c-exec-018 (S2b) RESULT + CLOSE S2 + roll to S3

Date: 2026-06-29
Play: work / writer (apply an executor RESULT handed back by the owner)
Direction / node / task: indie-game-development / g-9c41 / S2 (S2b → done; S2 slice → done)
Job: writer (validate-before-apply) + session continuation

## outcome

The c-exec-018 (S2b — load-bearing lockstep loopback determinism proof) builder RESULT was applied home after FIRST-HAND
verification. S2b is DELIVERED + merged + pushed; its delivery CLOSES the whole S2 slice (S2a + S2b). The bet g-9c41 rolls
to S3 (height/layering). I did NOT rubber-stamp the determinism gate — I verified the harness deliverable exists, the lock
(ADR-0002) is intact, and the merge landed, then recorded the four findings the builder surfaced (incl. an honest
scope note: S2 proved LOOPBACK determinism by construction, NOT the full networked-gas integration — that is ~S4).

## evidence (first-hand verification)

- Merge: GasCoopGame origin/main = adb9255 (--no-ff merge; parents 2e24a24 (post-S2a) + 3197694 (S2b leg tip)).
- Deliverable EXISTS on main: Assets/GasCoopGame/Core/Field/Determinism/ = LockstepLoopback.cs +
  LockstepDivergenceException.cs (the loud halt) + MeaningMembers.cs + GasScenario.cs (a real harness, not a stub).
- ADR-0017 present; lock intact (S2a-deleted families CoarseChunkFollower/IFieldStateChannel/FieldSnapshot = 0 prod hits on
  main); RESULT.md on main = DELIVERED + MERGED + PUSHED.
- Gate evidence accepted from RESULT.md + the build session's binding fresh-session G5: -Deliver GREEN, 923/923 (902 baseline
  byte-identical), mutation 73.51% ≥70, coverage 10/10, G5 (Sonnet, different family) COULD-NOT-REFUTE on 9 targets + 3 Codex
  rounds + a 5-skeptic adversarial convergence panel (all COULD-NOT-REFUTE). Not re-run from the OS repo (build-env domain).
- Imported + verified record → history/c-exec-018-s2b-result-2026-06-29.md.

## play_check

1. Recite — DONE. Input = the c-exec-018 builder RESULT (DELIVERED + merged). Reconciled vs committed main + NOW.md S2b.
2. Owner inputs (owner) — N/A (writer-apply; the merge was already owner-authorized + done; owner-eye was optional/confidence).
3. Do the work (validate-before-apply) — DONE. Verified the harness deliverable exists first-hand + the lock intact + the
   merge; recorded findings; closed S2; rolled to S3 (did NOT design S3 — set the slice outcome + deferred architecture to
   its PLAN). Did NOT spawn a redundant G5 (the binding fresh-session G5 already ran in the build context).
4. Self-check — DONE. S2b marked done only after the deliverable (the determinism harness) + lock + merge were confirmed;
   the scope-honesty note recorded (loopback ≠ full networked integration); the 4 findings carried as captures/deferrals.
5. Close — DONE (this RESULT). S2 done; S3 active (CALL to be framed next).

## state_changes
- NOW.md active_tasks: S2b → done; S2 (umbrella) → done (both halves); + S3 (active, CALL-to-be-framed).
- NOW.md open_calls: c-exec-018 → done.
- NOW.md next: IMMEDIATE NEXT → frame the S3 executor CALL; the 4 findings + scope-honesty note carried; push += s-work-028.
- LOG.md: + one line. history/: c-exec-018-s2b-result-2026-06-29.md (imported) + s-work-028.md (this).

## captures (the 4 S2b findings)
1. Scan-root parity gap (HARDENING): Core/Field/{FieldStep,FieldState}.cs + Coarse/Chunks sit OUTSIDE both determinism scan
   roots; $DefaultRoots duplicated verbatim with no parity enforcement → vacuous-green risk. Fold a self-test (every
   authoritative Core/Field subdir in BOTH scans) into the S3 PLAN or a small hardening leg.
2. Gas-as-ITickInputBus-citizen (networked lockstep + per-peer-secret false-green guard) = a larger seam ~S4.
3. Chunk-span geometry retirement (CoarseChunkSpan/IsWireEncodable/ChunkSpan/ChunkCount) → S4 2-band far-tier cleanup.
4. ADR numbering across tracks: engine ADR-0017 vs visual dev2 (0013/0014/0015) — rename-by-track if a future visual ADR
   claims 0017.

## decisions_needed
- (none) — S2b delivered + owner-authorized merge done; the findings are captures/deferrals, not owner decisions. The
  S3-vs-S4 sequencing + far-rollup vertical-strata count are S3-PLAN decisions (owner present at the PLAN), not now.

## log
2026-06-29 — writer (g-9c41/S2): applied c-exec-018 (S2b) RESULT — S2b + the whole S2 slice DONE (verified first-hand); bet rolls to S3.

## next
FRAME the S3 executor CALL (a fresh OS work-session; height/layering slice — PLAN-first, ведро; resolve S3-vs-S4 far-tier
sequencing + fold the scan-root parity-gap hardening). Then a fresh GasCoopGame_dev session opens it with a PLAN (owner
present). CARRIED: gas-as-networked-citizen + chunk-span retirement → ~S4; ADR-numbering-by-track. next slice = S3 (or
S3-folded-into-S4 if the PLAN so decides).

END_OF_FILE: live/indie-game-development/history/s-work-028.md
