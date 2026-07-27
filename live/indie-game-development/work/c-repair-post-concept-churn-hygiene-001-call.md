CALL c-repair-post-concept-churn-hygiene-001
to: session
direction: indie-game-development
play: repair
goal: |
  Sweep the tails two concept changes left in hot state, so the next planning leg reads a
  file that means what it says. Hygiene only: no strategy, no content, no decisions, and
  nothing that belongs to the owner.
context: |
  WHY. The owner's own words on 2026-07-27: «сейчас у меня как бы каша в голове, то есть
  я немножко не понимаю, куда мы, что идем. Я хочу вот как-то привести в порядок». The
  mess is real and it has a cause: the concept turned over twice inside about thirty-six
  hours, and each turn left a tail. `NOW.md` now carries EIGHTEEN issues, several of which
  describe a concept that no longer exists or a question that a later leg already answered;
  one `open_calls` row is superseded and unspent; and `work/converge-g-37a1.md` still has
  four sections that route a reader at answers the owner has since refused.

  RUNS IN PARALLEL with `c-map-g-37a1-core-requirements-001`, which is step 1 of the agreed
  six-step route (`d-post-verify-route-001`, answered «порядок такой»). This CALL is not on
  that route and blocks nothing on it. If the two collide over a file, THIS one yields.

  AUTHORITY: `live/indie-game-development/NOW.md`, `TREE.md`, `CHARTER.md`, the LOG tail
  and recent git; `history/2026-07-27-s-converge-verify-g-37a1-digging-card-001.md` for the
  named stale sections; `os/plays/repair.md`, whose removal boundary governs this leg.

  WHAT TO SWEEP.
  1. THE ISSUE SET. Eighteen entries. Fold, retarget or mark answered where a later leg
     has already resolved the substance — `i-substance-passage-open-questions` in
     particular carries a long ORIGINAL paragraph whose questions are now answered
     elsewhere, and several issues cross-reference each other in circles. Every surviving
     issue keeps a stable id, a route owner, a review trigger and a pointer. Nothing is
     invented, nothing is declared done, and every removed entry gets its disposition in
     the RESULT.
  2. THE STALE ARTIFACT SECTIONS, tracked as `i-artifact-sections-stale`. Add compact
     RETIREMENT BANNERS — not rewrites — where `work/converge-g-37a1.md` still carries false
     routing authority: §11, whose problem 2 points at the relocation the owner refused and
     whose problem 3 cites a rule he softened; §6, stale on the loot horn; §9's census,
     which is five verified of nine and must never be read as a completeness claim; the Z1
     citation, which names a test file that does not exist; and §7's reconciliation
     sentence, which its own correction 1 falsified. Prior bytes stay in Git.
  3. SCHEMA HYGIENE. Dangling pointers, `END_OF_FILE` trailers, dedup, LOG rotation if it
     is over ceiling.
boundaries: |
  Repair only. Do NOT touch `CHARTER.md` or `TREE.md` — both cards carry the owner's
  verdict on exact text and any semantic change routes to frame/map/review.
  Do NOT touch `c-map-g-37a1-core-requirements-001` or anything it needs.
  Do NOT remove, retire or tombstone an open call, a knowledge entry, an execution lane, a
  local play, or the approved status of any artifact he signed, without his words naming
  THAT surface in this leg — general agreement with a cleanup is not that permission. In
  particular the superseded `c-map-g-37a1-verify-rows-001` row stays until he names it.
  Do NOT answer, close or pre-empt any owner decision: `d-air-counter-visibility-001`
  stays open, and `i-engine-fit-decision-ladder` is his.
  Do NOT write `knowledge/` beyond a stale banner that removes false routing authority.
  Do NOT invent progress, do not mark anything done, do not create a bet, task, lane or
  executor CALL. Do not read `archive/**`. No numeric release chance.
  If a surface is illegal only because a rule changed after it was created, STOP and ask.
done_when: |
  1. `NOW.md` matches reality and schema: issues mutually consistent, each with route and
     trigger; the forecast basis still honest; no lane, no bet invented.
  2. The named stale sections carry visible banners and no evidence is lost.
  3. ONE batched diff was shown to the owner and applied only after his explicit approval —
     this is the play's own step 4 and it is not optional, so the leg is owner-light rather
     than owner-free.
  4. Any OS-level hole found becomes one FRICTION line; the OS is not fixed here. One
     candidate is already known: an undispatched CALL was amended three times in one evening
     and then superseded, which is friction worth recording.
return: |
  One `repair` RESULT with the contradiction named, the batched diff, the disposition of
  every removed or folded issue, and the friction line.
budget: one short session, owner needed only to approve the single diff
surface: a FRESH chat

END_OF_FILE: live/indie-game-development/work/c-repair-post-concept-churn-hygiene-001-call.md
