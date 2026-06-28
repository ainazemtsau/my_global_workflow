# s-work-026 — writer (g-9c41 / S2a): apply the c-exec-017 (S2a) builder RESULT + roll to S2b

Date: 2026-06-28
Play: work / writer (apply an executor RESULT handed back by the owner)
Direction / node / task: indie-game-development / g-9c41 / S2a
Job: writer (validate-before-apply) + session continuation

## outcome

The c-exec-017 (S2a — ZERO-LEGACY retirement of the host-authoritative reconstruction spine) builder RESULT was applied
home after FIRST-HAND verification. S2a is DELIVERED (binding gates green on GasCoopGame dev @ec54d4f; merge dev→main +
push owner-gated). The bet rolls to S2b (c-exec-018, the load-bearing loopback — ready to author on the clean base).
I did NOT rubber-stamp the builder's report — I verified the deletes are real + reconciled three stale points + adjudicated
a flagged ADR conflict against the actual repo, then recorded the conflict for the owner rather than acting on the canon.

## evidence (first-hand verification)

- Deletes real: grep of GasCoopGame Assets/**.cs (non-test) for CoarseChunkFollower / IFieldStateChannel / FieldSnapshot /
  FieldStreamDriver / FieldHost / ChunkEncoder / RevisionBarrier = 0 production files each (a deletion leg's deliverable =
  the absence, confirmed).
- RESULT.md on dev = "DELIVERED (gates green on dev); merge dev→main + push OWNER-GATED."
- Gate numbers (857/857, -Deliver GREEN, mutation 87.96%, coverage 8/8) + fresh-session G5 COULD-NOT-REFUTE accepted from
  the build session's RESULT.md (the binding refutation; not re-run from the OS repo — the build env's domain).
- Full imported RESULT + reconciliations → history/c-exec-017-s2a-result-2026-06-28.md.

## reconciliations (builder report was stale vs the committed tip)

1. dev HEAD = ec54d4f (not 4cfc7b0); retirement ADR renumbered 0015→0016 (c-visual-001 S5 collision).
2. dev→main is NO LONGER a clean FF — the parallel visual track merged S5 to main (9780713); main…dev = 2/4 → a real
   (conflict-free-expected, Core-vs-Render) merge. The owner-gated merge must account for this.
3. Canon citation error (verified): the input-lockstep LOCK is ADR-0002 in the repo ("lockstep over FishNet"), while
   ADR-0010 is the test-sandbox. The canon + c-016/c-017 CALLs mis-cite the lock as ADR-0010 → d-adr-lockstep-citation-001
   (OPEN, owner decision; rec A = fix the canon citation). Pure citation error; lock semantics unchanged.

## play_check

1. Recite — DONE. Input = the c-exec-017 builder RESULT (DELIVERED). Reconciled vs committed state (NOW.md S2a + the dev tip).
2. Owner inputs (owner) — N/A (writer-apply; the owner-gated merge + owner-eye are recorded as pending, NOT self-marked done).
3. Do the work (writer validate-before-apply) — DONE. Verified deletes first-hand; reconciled 3 stale points; adjudicated
   the ADR conflict against the repo; applied state_changes; surfaced the ADR conflict as a decision rather than acting on
   the owner-signed canon.
4. Self-check — DONE. S2a marked done only after the deliverable (the absence) was confirmed; merge/owner-eye left pending
   (not self-marked); the ADR fix NOT applied to the canon in-session (out of writer scope + owner-signed).
5. Close — DONE (this RESULT). S2a done; S2b active/ready-to-author; next = author c-exec-018.

## state_changes
- NOW.md active_tasks: S2a → done (DELIVERED on dev, verified; merge owner-gated). S2b → active (UNBLOCKED, ready to author
  c-exec-018); S2b done_when "reopening ADR-0010" corrected → "reopening the input-lockstep lock (ADR-0002)".
- NOW.md open_calls: c-exec-017 → done (delivered on dev). c-exec-018 → ready-to-author (base exists; fold ADR-0002 +
  RNG-drop + chunk-span deferral).
- NOW.md decision_inbox: + d-adr-lockstep-citation-001 (OPEN, owner decision).
- NOW.md next: IMMEDIATE NEXT → author c-exec-018; owner-gated/pending items + the ADR decision surfaced. push += s-work-026.
- LOG.md: + one line.
- history/: c-exec-017-s2a-result-2026-06-28.md (imported + reconciled) + s-work-026.md (this).

## captures
- Chunk-span geometry full excision (CoarseChunkSpan / IsWireEncodable / ChunkSpan / ChunkCount) deferred to S4 — kept this
  leg because surviving far-tier consumers remain. Surfaces when S4 is shaped.
- Gates for S2a ran under PowerShell 5.1 (build env had no pwsh7); owner re-run on pwsh expected identical.

## decisions_needed
- d-adr-lockstep-citation-001 (OPEN): fix the canon's input-lockstep-lock citation ADR-0010 → ADR-0002 (ADR-0010 is the
  test-sandbox). Options A (fix now, review/pulse + owner ack — RECOMMENDED) / B (defer to a batched maintenance pass).
  Owner-gated because the canon is owner-signed.

## log
2026-06-28 — writer (g-9c41/S2a): applied c-exec-017 RESULT (S2a DELIVERED on dev, verified first-hand); bet rolls to S2b; surfaced d-adr-lockstep-citation-001.

## next
AUTHOR the S2b executor CALL c-exec-018 (a fresh OS work-session frames + hardens the load-bearing loopback proof on the
clean post-S2a base) — folding ADR-0002 (not ADR-0010) for the lock, the RNG-control drop, and the chunk-span S4-deferral.
OWNER-GATED + PENDING: merge S2a dev→main + push (a real merge now) + optional owner-eye (dotnet test 857). OWNER DECISION
OPEN: d-adr-lockstep-citation-001. next slice after S2 = S3 (height/layering).

END_OF_FILE: live/indie-game-development/history/s-work-026.md
