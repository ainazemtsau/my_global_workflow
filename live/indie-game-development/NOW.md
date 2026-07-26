# NOW: indie-game-development

updated: 2026-07-26 by s-repair-live-hygiene-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis has no per-item MUST appetites, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The sole current frontier is the owner-present g-12fd Demo Basis authoring route, followed by fresh converge-verify, narrow review and only then shape of g-37a1."
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
    issue: "If no approved Demo Basis exists by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move."
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day the Demo Basis is approved."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/c-work-october-demo-basis-authoring-001-call.md"

  - id: i-procgen-determinism
    issue: "The owner requires procedural level generation inside one biome for the demo, but the recorded PGG verdict rejects runtime Dungeon Architect generation on determinism (global static System.Random, float/Perlin, seed output changed across plugin versions). Unresolved; an engineering verdict is needed, not a canon one."
    level: execution
    route: work
    review_when: "At shape of the level lane, before any level build CALL."
    evidence: "work/pgg-analysis-2026-07-10.md:19-22; archive/directions/indie-game-development/2026-07-pre-reset/history/2026-07-11-s-spike-pgg-001-close-001.md"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame in work/concept-frame-v1.md, but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier if the Demo Basis contradicts the frame."
    evidence: "work/concept-frame-v1.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

open_calls:
  - id: c-work-october-demo-basis-authoring-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-25
    call: work/c-work-october-demo-basis-authoring-001-call.md
    note: "OWNER-PRESENT CLEAN-ROOM CANON AUTHORITY. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT OR STEAM MUTATION. Owner-named source: work/concept-frame-v1.md; take its DEMO-BLOCKING questions in the listed order, question 1 (substance behaviours) first because it alone can invalidate merged Core code."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
