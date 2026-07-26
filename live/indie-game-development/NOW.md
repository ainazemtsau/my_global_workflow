# NOW: indie-game-development

updated: 2026-07-26 by s-work-october-demo-basis-v2-revision-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis now names eight MUST items but none carries an appetite or G5 evidence, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The owner approved the exact Demo Basis `work/october-demo-basis-v2.md` on 2026-07-26 with the words «да» on its exact eight-item MUST list, after revising the v1 he had approved the same day; v1 is now a tombstone and its full text lives in commit 3f135b9b. The sole current frontier is the fresh independent converge-verify of the v2 artifact, then narrow review, and only then shape of g-37a1. Owner approval alone does not close g-12fd."
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
    issue: "The owner approved the Demo Basis on 2026-07-26 and revised it to v2 the same day, ahead of the 2026-08-07 boundary, so the scope cut is not triggered by absence. The cut now depends on the fresh converge-verify of v2: if that verification has not passed by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move. The eight v2 MUST items carry no appetites yet, and procedural generation from authored modules entered MUST after the boundary was set."
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day converge-verify passes or fails."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/october-demo-basis-v2.md; work/c-converge-verify-october-demo-basis-v2-001-call.md"

  - id: i-procgen-determinism
    issue: "The owner ruled procedural generation IN on 2026-07-26 as Demo Basis v2 MUST 5: the level is assembled from modules authored in the editor, the host performs the assembly and ships the finished layout rather than a seed, so generator determinism is not required. Runtime determinism is therefore no longer the open question. What remains open is engineering, not canon: whether module authoring is reachable for one developer inside the October calendar (the recorded verdict never verified Unity 6.3 compatibility), and how the host's finished layout is replicated to the other clients."
    level: execution
    route: work
    review_when: "Before any level build CALL."
    evidence: "work/pgg-analysis-2026-07-10.md:9-15,21-31,42; work/october-demo-basis-v2.md (MUST 5); work/c-converge-verify-october-demo-basis-v2-001-call.md"

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
  - id: c-converge-verify-october-demo-basis-v2-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-26
    call: work/c-converge-verify-october-demo-basis-v2-001-call.md
    note: "FRESH SEPARATE REFUTATION SESSION, never the authoring or revision chat. verify_target: specification. Attacks the exact artifact work/october-demo-basis-v2.md (owner words «да» on its exact eight-item MUST list, 2026-07-26). Replaces the withdrawn c-converge-verify-october-demo-basis-v1-001, which was never dispatched and produced no findings. No node-class checklist exists in knowledge/: author one from first principles or BLOCK. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT, STEAM OR CANON-REPO MUTATION. PASS opens exactly one narrow review; FAIL returns findings to owner-authority work."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
