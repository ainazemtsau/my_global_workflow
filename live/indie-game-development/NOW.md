# NOW: indie-game-development

updated: 2026-07-26 by s-day-manager-layer-install-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis; slack in days against them is a fact and is reported daily. A numeric chance still has no denominator: the Demo Basis has no per-item MUST appetites, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "Three daily numbers replace prose: SLACK (hard gate date - today - preparation time), IDLE (days since a commit ADDED lines to engine C#), COUNT (k of 6 external receipts). Today: slack 16-X on the Steam branch, IDLE 7 days (last authored engine C# 2026-07-19; merged to main 2026-07-20), COUNT 0 of 6. IDLE leads the brief whenever it is >=3."
    - "Steam branch splits: half A (name, base/demo AppID, tags/categories, descriptions, legal, page skeleton) is design-independent, ~2h, delegable; half B (4 capsules, 5+ screenshots, trailer) needs a presentable scene, so the 2026-08-11 page-submission date is a hard date on development. $100 paid and account open (credit unused), so the 30-day Steam Direct wait expires ~2026-08-11 and no longer binds. Derived: name+AppID by 08-05, page submitted 08-11, page public + registered 08-31, build candidate 09-03, demo live 09-15; 10-05 is the failure boundary, not the plan."
    - "Measured: engine C# not authored since 2026-07-19; 43 direction legs and 0 product commits over 07-23..07-26; product commits per week 334 (W29) then 40 (W30) while direction legs held 17-30/day. Assets/GasCoopGame Core=120 files, Characters=13, Net=4, Scenes=0, Levels=0 — a deep simulation with no game around it. Parallel execution lanes stay illegal until a bet exists, so the only door out of the reset quarantine is g-12fd -> converge-verify -> review -> shape."
    - "Standing cut order, owner says the word every time, February only on exact owner words: 08-07 no approved Demo Basis -> demo scope is cut to the remaining calendar, date does not move; 08-31 page not public -> October route closed, explicit owner choice, silent slip forbidden; 09-03 no build candidate submitted -> demo content is cut to the CHARTER quality threshold and the remainder is discarded, not deferred."
  update_when: "A gate resolves, Valve changes a published date, or the first product outcome closes. Not daily; a saved forecast delta without a changed fact is fabrication."

issues:
  - id: i-program-custody
    issue: "The preserved Program legacy-lab purge candidate and WIN-U1 custody were never released."
    level: execution
    route: repair
    review_when: "Before any product cleanup or Program admission."
    evidence: "work/c-exec-program-v2-legacy-lab-purge-release-001-call.md; history/2026-07-20-s-work-program-v2-legacy-lab-purge-deliver-blocked-001.md"

  - id: i-level-close
    issue: "LV0 has product PLAN evidence but no binding Direction close."
    level: execution
    route: review
    review_when: "Before Level is admitted to a future objective."
    evidence: "work/c-exec-level-module-standard-v1-lv0-plan-001-call.md"

  - id: i-character-close
    issue: "Character V2 still needs its binding Direction close, and the older P2a0 lifecycle finding must not be mistaken for G5."
    level: execution
    route: review
    review_when: "Before Character work is admitted or relaunched."
    evidence: "work/c-exec-char-v2-body-rig-ragdoll-build-001-call.md; work/review/findings.md#dr-20260711-001"

  - id: i-visual-legacy
    issue: "Presentation root c-visual-009 is a legacy route whose prerequisites were never reconciled to current authority."
    level: execution
    route: repair
    review_when: "Before Presentation is admitted."
    evidence: "work/c-visual-009-movement-data-plan-call.md"

  - id: i-marketing-route
    issue: "Marketing checkpoint routing is stale and can repeat the completed INOMAND start."
    level: objective
    route: repair
    review_when: "Before Marketing/Audience is admitted."
    evidence: "work/review/findings.md#dr-20260712-001; work/marketing/claude-code-handoff-c-marketing-wake-001-2026-07-12.md"

  - id: i-grid-admission
    issue: "G02 evidence is preserved but Grid has not been admitted to the new demo roadmap."
    level: roadmap
    route: work
    review_when: "During g-12fd Demo Basis authoring, before any Grid launch."
    evidence: "work/c-exec-grid-v1-g02-common-spatial-map-002-call.md; history/2026-07-22-s-repair-grid-v1-g02-false-g01-blocker-001.md; history/2026-07-25-s-map-october-demo-release-roadmap-001.md"

  - id: i-gas-admission
    issue: "Gas V1 node-1 plan evidence is preserved but Gas has not been admitted to the new demo roadmap."
    level: roadmap
    route: work
    review_when: "During g-12fd Demo Basis authoring, before any Gas launch."
    evidence: "work/c-work-gas-v1-live-composition-plan-001-call.md; history/2026-07-21-s-work-gas-v1-master-plan-accepted-001.md; history/2026-07-25-s-map-october-demo-release-roadmap-001.md"

  - id: i-steam-appid
    issue: "Name, base/demo AppID and Steam page half A are not started. The $100 fee is paid and the account is open with one unused credit; the name depends on the concept in flight."
    level: roadmap
    route: work
    review_when: "2026-08-05, or earlier on the day a name exists."
    evidence: "work/marketing/assets/checkpoint-2026-07-12/steamworks-no-app-one-credit.png; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest"

  - id: i-steam-sequence-tree
    issue: "TREE g-7b42.why and the prior forecast put Steam work after the first playable proof, but Next Fest registration requires an already published public store page, not a build. The owner accepted decoupling; TREE still says otherwise."
    level: roadmap
    route: map
    review_when: "Before the page is submitted, no later than 2026-08-11."
    evidence: "live/indie-game-development/TREE.md (g-7b42.why); https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest"

  - id: i-demo-scope-cap
    issue: "If no approved Demo Basis exists by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move."
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day the Demo Basis is approved."
    evidence: "live/indie-game-development/CHARTER.md (Отношение к риску; премортем 1 и 4); work/c-work-october-demo-basis-authoring-001-call.md"

  - id: i-procgen-determinism
    issue: "The owner requires procedural level generation inside one biome for the demo, but the recorded PGG verdict rejects runtime Dungeon Architect generation on determinism (global static System.Random, float/Perlin, seed output changed across plugin versions). Unresolved; an engineering verdict is needed, not a canon one."
    level: execution
    route: work
    review_when: "At shape of the level lane, before any level build CALL."
    evidence: "work/pgg-analysis-2026-07-10.md:19-22; history/2026-07-11-s-spike-pgg-001-close-001.md"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame («Принимаю эту форму.») but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier if the Demo Basis contradicts the frame."
    evidence: "work/concept-frame-v1.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

  - id: i-history-integrity
    issue: "Seven LOG/history links or trailers from the legacy ledger remain unresolved."
    level: direction
    route: repair
    review_when: "Before relying on the affected legacy receipts."
    evidence: "work/review/findings.md#dr-20260711-002"

  - id: i-knowledge-links
    issue: "Twenty-one legacy knowledge/TREE pointers resolve to fifteen missing target paths."
    level: direction
    route: repair
    review_when: "Before importing any affected legacy knowledge."
    evidence: "work/review/findings.md#dr-20260711-003"

open_calls:
  - id: c-work-october-demo-basis-authoring-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-25
    call: work/c-work-october-demo-basis-authoring-001-call.md
    note: "OWNER-PRESENT CLEAN-ROOM CANON AUTHORITY. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT OR STEAM MUTATION. Owner-named source: work/concept-frame-v1.md — take its DEMO-BLOCKING questions in the listed order; question 1 (substance behaviours) first, because it alone can invalidate merged Core code."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
