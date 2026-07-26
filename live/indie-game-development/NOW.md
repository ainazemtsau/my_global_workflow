# NOW: indie-game-development

updated: 2026-07-26 by s-converge-verify-october-demo-basis-v2-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis now names eight MUST items but none carries an appetite or G5 evidence, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The owner approved the exact Demo Basis `work/october-demo-basis-v2.md` on 2026-07-26 with the words «да» on its exact eight-item MUST list, after revising the v1 he had approved the same day; v1 is now a tombstone and its full text lives in commit 3f135b9b. The fresh independent converge-verify ran the same day and FAILED with ten named findings: MUST 5 misattributes the recorded PGG verdict and its determinism-removal rationale is unsupported, and the two deferred hall mechanics left the danger stage, the causal-cooperation supports, falsifier 5 and the public-claim ceiling leaning on deferred or undecided content. No owner decision was reversed; procedural generation stays IN. The sole current frontier is the owner-present v3 revision `c-work-october-demo-basis-v3-revision-001`, then a fresh converge-verify against v3, then narrow review, and only then shape of g-37a1. Neither owner approval nor a failed verification closes g-12fd."
    - "Steam half A (name, base/demo AppID, tags/categories, descriptions, legal and page skeleton) is design-independent but remains parked until 2026-08-05 or the day a name exists; half B (capsules, screenshots and trailer) needs a presentable scene. Standing derived gates: page submitted 08-11, page public + registered 08-31, build candidate 09-03, demo live 09-15; 10-05 is the failure boundary, not the plan."
    - "Standing cut order, owner says the word every time, February only on exact owner words: 08-07 no approved Demo Basis -> demo scope is cut to the remaining calendar, date does not move; 08-31 page not public -> October route closed, explicit owner choice, silent slip forbidden; 09-03 no build candidate submitted -> demo content is cut to the CHARTER quality threshold and the remainder is discarded, not deferred."
  update_when: "A gate resolves, Valve changes a published date, or the first product outcome closes. A day brief recomputes SLACK, IDLE and COUNT from fresh receipts; those volatile values are not persisted without a changed fact."

issues:
  - id: i-steam-appid
    issue: "Name, base/demo AppID and Steam page half A are not started. The $100 fee is paid and the account is open with one unused credit; the name depends on the concept in flight."
    level: roadmap
    route: work
    review_when: "2026-08-05, or earlier on the day a name exists."
    evidence: "work/marketing/assets/checkpoint-2026-07-12/steamworks-no-app-one-credit.png; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest"

  - id: i-steam-sequence-tree
    issue: "TREE g-7b42.why puts Steam work after the first playable proof, but Next Fest registration requires an already published public store page, not a build. The owner accepted decoupling; TREE still says otherwise."
    level: roadmap
    route: map
    review_when: "Before the page is submitted, no later than 2026-08-11."
    evidence: "live/indie-game-development/TREE.md (g-7b42.why); https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest"

  - id: i-demo-scope-cap
    issue: "The owner approved the Demo Basis on 2026-07-26 and revised it to v2 the same day, ahead of the 2026-08-07 boundary, so the scope cut is not triggered by absence. The independent verification of v2 FAILED the same day with ten named findings, so no approved-and-verified Basis exists yet. The cut now depends on v3: if no Demo Basis has passed converge-verify by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move. The eight v2 MUST items still carry no appetites, and MUST 5 (procedural generation from authored modules) entered after the boundary was set with an unbounded technical dependency — verification finding F8."
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day a Demo Basis version passes converge-verify."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/october-demo-basis-v2.md; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md; work/c-work-october-demo-basis-v3-revision-001-call.md"

  - id: i-procgen-determinism
    issue: "The owner ruled procedural generation IN on 2026-07-26 as Demo Basis v2 MUST 5, and that decision stands. Its stated rationale does not: verification findings F1 and F2 show MUST 5 credits the recorded PGG verdict with approving Dungeon Architect as editor-time module authoring, while that verdict approves PGG for editor-time authoring only after a spike and gives Dungeon Architect the runtime-assembler role with hand-authored module shells; and the claim that host-side assembly plus a shipped layout removes the determinism requirement has no resolved support, since the cited pipeline assembles at runtime from a seed. So runtime determinism is NOT settled by the artifact, it is unresolved pending an engineering verdict. Open, all engineering, none canon: whether module authoring is reachable for one developer inside the October calendar (the verdict never verified Unity 6.3 — its own red flag 1, and the spike close receipt is archive-quarantined); how a finished layout would be replicated to the other clients; and whether determinism can be dropped at all."
    level: execution
    route: work
    review_when: "Before any level build CALL, and no later than the v3 Demo Basis revision."
    evidence: "work/pgg-analysis-2026-07-10.md:9-15,21-31,42; work/october-demo-basis-v2.md (MUST 5); history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (F1, F2, F8)"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame in work/concept-frame-v1.md, but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority. The Demo Basis was authored under it and v2 does not contradict it; v2's MUST 5 now uses the frame's own procedural-generation clause."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier if the Demo Basis contradicts the frame."
    evidence: "work/concept-frame-v1.md; work/october-demo-basis-v2.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

  - id: i-canon-repo-evidence-read
    issue: "The owner explicitly authorized one bounded read of the frozen canon repository C:\\projects\\gas_coop_game_canon during Demo Basis v1 authoring; the exact files used are listed in the artifact and carried forward into v2. The material entered as evidence only and gained no authority. The v2 revision read no legacy source. The default-closed guard is unchanged and no further legacy read is authorized."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or on any future request to reopen legacy canon."
    evidence: "work/october-demo-basis-v2.md; knowledge/canon-clean-authority-reset.md; .claude/settings.json"

open_calls:
  - id: c-work-october-demo-basis-v3-revision-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-26
    call: work/c-work-october-demo-basis-v3-revision-001-call.md
    note: "OWNER-PRESENT SPECIFICATION AUTHORITY. Returns the ten findings F1-F10 of the FAILED independent verification of v2 (receipt history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md) to the owner. No owner decision is reversed: procedural generation stays IN as MUST 5, the two hall mechanics stay deferred, terminology stays «вещество». F1 is a factual correction, F6/F10/D1 are mechanical and need only his confirmation; the rest need his words. Produces work/october-demo-basis-v3.md, then one fresh converge-verify against v3. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT, STEAM OR ARCHIVE/CANON-REPO READ OR MUTATION."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
