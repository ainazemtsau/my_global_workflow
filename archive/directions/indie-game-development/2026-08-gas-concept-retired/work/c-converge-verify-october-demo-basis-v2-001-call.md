> **RETIRED 2026-07-31 — DO NOT DISPATCH.** The bet `g-37a1` was closed with verdict `obsolete` (the owner changed the game concept). Every CALL issued under it is dead regardless of the status written below. This file is preserved as evidence of what was decided, never as a frontier. The live frontier is `live/indie-game-development/NOW.md`, which currently has `bet: null` and no open calls. See `history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md`.

CALL c-converge-verify-october-demo-basis-v2-001
to: session
direction: indie-game-development
play: converge-verify
node: g-12fd
verify_target: specification
goal: |
  A fresh independent session tries to BREAK the exact owner-approved artifact
  `live/indie-game-development/work/october-demo-basis-v2.md` before any narrow
  review closes the parked specification outcome `g-12fd`.
context: |
  Exact artifact identity: `october-demo-basis-v2`, node `g-12fd`.
  Owner approval receipt: 2026-07-26, exact words «да» on the artifact's exact
  eight-point MUST list, recorded in
  `history/2026-07-26-s-work-october-demo-basis-v2-revision-001.md`. That receipt
  also carries the owner's verbatim revision words.

  `october-demo-basis-v1` is superseded and exists only as a tombstone; its full
  text lives in commit `3f135b9b`. Its verification CALL
  `c-converge-verify-october-demo-basis-v1-001` was withdrawn before dispatch and
  produced no findings, no oracle and no evidence.

  Current authority to read: `CHARTER.md`; `TREE.md` (`g-12fd` done_when);
  `NOW.md`; `knowledge/canon-clean-authority-reset.md`;
  `knowledge/strategy-reset-boundary.md`; `work/concept-frame-v1.md`;
  `work/pgg-analysis-2026-07-10.md`; the exact artifact above; and this CALL.

  Two done_when sets bind the artifact: `g-12fd` in `TREE.md`, and the revision
  CALL `c-work-october-demo-basis-v2-revision-001` quoted in full in the history
  receipt named above.

  Caveats carried forward from the withdrawn v1 CALL:

  - The authoring leg reordered the concept frame's DEMO-BLOCKING questions on
    explicit owner instruction: substance behaviours were derived last, not
    chosen first. Verify that the artifact still satisfies every atomic done_when
    clause under that order.
  - During v1 authoring the owner explicitly authorized one bounded read of the
    frozen canon repository `C:\projects\gas_coop_game_canon` as evidence only;
    it is recorded as issue `i-canon-repo-evidence-read`. Its exact files are
    listed in the artifact under «На чём это стоит». Treat every one of them as
    historical evidence with zero authority. A claim resting only on a legacy
    file's former accepted status is a smuggling FAIL. No new legacy read is
    authorized by this CALL.
  - No node-class checklist exists in `knowledge/` for the node class
    "owner-approved demo boundary specification". Per the play, author one from
    first principles before the attack and propose it; an empty oracle BLOCKS.

  Known tensions the v2 revision introduced. They are named here as attack
  surface, not as verdicts, and the revision leg did not resolve any of them:

  1. Two former MUST items («зал плодит сам, минимум два источника, и заглушение
     физически меняет зал»; «уборка будит остаток») moved to «потом
     рассмотреть». §2 «Опасность и задача» and §4 were edited to stop asserting
     them. Attack whether the demo's danger, its twenty minutes and its causal
     cooperation still stand on what remains.
  2. Falsifier 5 («Заглушение источника не меняет зал физически») was kept
     verbatim by owner instruction while its subject is deferred, so it can no
     longer fire. Attack it as a dormant or unfalsifiable falsifier.
  3. MUST 5 says the recorded PGG verdict approved editor-time module authoring.
     `work/pgg-analysis-2026-07-10.md` approves PGG as the editor-time authoring
     assistant and rejects PGG at runtime; Dungeon Architect appears there as the
     runtime assembler of already-authored static modules, and the file records
     that Unity 6.3 compatibility is unverified. Attack the attribution and every
     weight-bearing part of MUST 5 against what that file actually says.
  4. MUST 5's own claim that host-side assembly and a shipped layout remove the
     determinism requirement is untested. Issue `i-procgen-determinism` was
     narrowed, not closed.
  5. Open question 7 («чем заняты двадцать минут помимо набора и переноски») is
     declared answerable only from a playable scene. Attack whether any done_when
     clause or MUST item silently depends on its answer.
boundaries: |
  Refute or pass. Never answer an open question, never repair the artifact,
  never choose content, never treat agent recommendation as owner approval.
  Do not read the authoring or revision session's reasoning; attack the artifact
  itself. Do not open shape, bet, tasks or tracks. Do not mutate product, Steam
  state, the canon repository or `CHARTER.md`/`TREE.md`. Do not publish an
  uncalibrated numeric release chance.

  The artifact's seven unanswered content questions are a declared legitimate
  result. An unanswered question is a FAIL only where a done_when clause or a
  MUST item silently depends on its answer.
done_when: |
  1. Every atomic clause of `g-12fd` done_when and of
     `c-work-october-demo-basis-v2-revision-001` done_when is split and mapped to
     an exact artifact section; an uncovered clause is named, never filled.
  2. Every weight-bearing claim required by done_when names its supporting
     value/fact with a resolved citation; untraceable or legacy-status-only
     support is FAIL.
  3. The causal-cooperation test, the readable moment, the falsifiers and the
     invalidation list are attacked for circularity, unfalsifiability and hidden
     dependence on the open questions, including every tension listed above.
  4. The eight-item MUST list is attacked for October feasibility by one solo
     developer against the standing cut dates in `NOW.md`; procedural generation
     from authored modules is attacked as the newest and largest of them. A MUST
     that cannot be built is named, not silently downgraded.
  5. Outcome is PASS with `§SIGNOFF: converge-verify passed @ <date>` and
     play_check `verify_target: specification complete=PASS smuggling=PASS`, or
     FAIL with named findings returned to owner-authority `work` on `g-12fd`.
  6. On PASS, exactly one narrow `review` CALL is opened naming the node, the
     exact artifact identity, the owner receipt and this verification receipt.
     No shape is opened either way. `g-12fd` stays parked.
return: |
  One converge-verify RESULT with verify_target, the atomic clause map, the
  smuggling audit, the authored node-class oracle, PASS/FAIL and either the
  signoff plus one narrow review CALL, or named findings for the owner-authority
  work continuation.
budget: one fresh session, no owner presence required
surface: any, but NEVER the authoring or revision chat

disposition: |
  DISCHARGED 2026-07-26 by s-converge-verify-october-demo-basis-v2-001 (fresh
  session, neither the authoring nor the revision chat).
  Outcome: FAIL. play_check `verify_target: specification complete=FAIL
  smuggling=FAIL`. Ten findings F1-F10 named, none filled or repaired.
  Oracle authored, so the leg was not blocked:
  `work/oracle-demo-boundary-specification-v1.md`.
  Receipt: `history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md`.
  Findings returned to owner-authority work:
  `work/c-work-october-demo-basis-v3-revision-001-call.md`.
  Verification reruns against v3. This CALL is spent, not withdrawn: it produced
  an oracle and findings, and both are carried forward.

END_OF_FILE: live/indie-game-development/work/c-converge-verify-october-demo-basis-v2-001-call.md
