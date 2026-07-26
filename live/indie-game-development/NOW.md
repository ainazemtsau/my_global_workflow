# NOW: indie-game-development

updated: 2026-07-26 by s-work-october-demo-basis-authoring-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis now names eight MUST items but none carries an appetite or G5 evidence, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The owner approved the exact Demo Basis `work/october-demo-basis-v1.md` on 2026-07-26 with the words «принимаю». The sole current frontier is the fresh independent converge-verify of that exact artifact, then narrow review, and only then shape of g-37a1. Owner approval alone does not close g-12fd."
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
    issue: "The owner approved the Demo Basis on 2026-07-26, ahead of the 2026-08-07 boundary, so the scope cut is not triggered by absence. The cut now depends on the fresh converge-verify: if that verification has not passed by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move. The eight MUST items carry no appetites yet."
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day converge-verify passes or fails."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/october-demo-basis-v1.md; work/c-converge-verify-october-demo-basis-v1-001-call.md"

  - id: i-procgen-determinism
    issue: "The owner requires procedural level generation inside one biome for the demo, but the recorded PGG verdict rejects runtime Dungeon Architect generation on determinism (global static System.Random, float/Perlin, seed output changed across plugin versions). The approved Demo Basis places procedural generation in CUT and records the collision as unanswered content question 4; the owner has not decided. An engineering verdict is still needed, not a canon one."
    level: execution
    route: work
    review_when: "Before any level build CALL, or earlier on the day the owner rules on Demo Basis open question 4."
    evidence: "work/pgg-analysis-2026-07-10.md:19-22; work/october-demo-basis-v1.md; archive/directions/indie-game-development/2026-07-pre-reset/history/2026-07-11-s-spike-pgg-001-close-001.md"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame in work/concept-frame-v1.md, but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority. The Demo Basis v1 was authored under it and does not contradict it."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier if the Demo Basis contradicts the frame."
    evidence: "work/concept-frame-v1.md; work/october-demo-basis-v1.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

  - id: i-canon-repo-evidence-read
    issue: "The owner explicitly authorized one bounded read of the frozen canon repository C:\\projects\\gas_coop_game_canon during Demo Basis authoring; the exact files used are listed in the artifact. The material entered as evidence only and gained no authority. The default-closed guard is unchanged and no further legacy read is authorized."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or on any future request to reopen legacy canon."
    evidence: "work/october-demo-basis-v1.md; knowledge/canon-clean-authority-reset.md; .claude/settings.json"

open_calls:
  - id: c-converge-verify-october-demo-basis-v1-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-26
    call: work/c-converge-verify-october-demo-basis-v1-001-call.md
    note: "FRESH SEPARATE REFUTATION SESSION, never the authoring chat. verify_target: specification. Attacks the exact artifact work/october-demo-basis-v1.md (owner words «принимаю», 2026-07-26). No node-class checklist exists in knowledge/: author one from first principles or BLOCK. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT, STEAM OR CANON-REPO MUTATION. PASS opens exactly one narrow review; FAIL returns findings to owner-authority work."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
