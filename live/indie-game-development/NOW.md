# NOW: indie-game-development

updated: 2026-07-26 by s-work-october-demo-basis-v4-revision-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: no MUST item carries an appetite or G5 evidence, no product evidence exists under any Basis version, the roadmap order itself is now being replanned, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. On 2026-07-26 the owner STOPPED the Demo Basis revision loop and ruled the roadmap order wrong: «задача явно неправильная. Ну, вернее, она как бы правильная, но она не должна сейчас стоять первой»; «в начале я хочу как можно быстрее получить геймплей для себя ... первая задача будет, первый критерий»; «нужно сделать пересборку дерева». `c-work-october-demo-basis-v4-revision-001` is WITHDRAWN by that decision, not failed (`history/2026-07-26-s-work-october-demo-basis-v4-revision-001.md`). The diagnosis he acted on: `g-12fd` done_when requires the Basis to fix a readable moment and a public-claim ceiling before any build exists, and both are properties of a finished demo verified against a build - so the artifact had to make claims nothing could back, and independent verification correctly reported exactly that twice (ten findings, then eight). Three legs, three Basis versions, zero product evidence; `CHARTER.md` premortem 3 has a standing boundary for that and it was not applied. Nothing is reversed by the stop: the eight-item MUST list keeps his «да», procedural generation stays IN and mandatory, technique stays OUT of content documents, the two hall mechanics stay deferred, terminology stays «вещество», the provisional first-slice decisions stay not-law, and `work/october-demo-basis-v3.md` stays the single live Basis text - unverified, a source and not authority. The eight findings V1-V8 remain valid against the OLD done_when and are recorded in `work/c-work-october-demo-basis-v4-revision-001-call.md`. The sole current frontier is the owner-present `c-map-october-demo-order-reset-001`; the route after it is shape of whatever the new first outcome becomes, then the product build. `g-12fd` stays parked and its fate is the map leg's business, not this leg's."
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
    issue: "The 2026-08-07 scope-cut date stands and does not move — it is CHARTER risk posture («при конфликте сначала сокращается объём, а не переносится срок») and the owner's own words: «Время ограничено: 7 августа граница урезания объёма.» What no longer matches the roadmap is its TRIGGER. The trigger was «no Demo Basis version has passed converge-verify», and on 2026-07-26 the owner withdrew the Basis revision loop and ordered a roadmap replan, so a passed Basis is no longer the thing the calendar is waiting on. The trigger must be re-expressed against whatever the new first outcome becomes — that is `c-map-october-demo-order-reset-001`'s business, not an agent's. Facts that stand regardless: two Basis versions failed independent verification on 2026-07-26 (ten findings, then eight), no version passed, three legs produced zero product evidence, the eight MUST items carry no appetites, and art is at zero — the owner's words «арта ноль», «в начале мы к первой версии стремимся, хоть вообще без арта ... что-то самое примитивное добавить, чтобы не блочилось», «На визуал вообще похуй». Art at zero eight weeks out is the fact most likely to force a cut, and the map leg is asked to put its date on the roadmap."
    level: roadmap
    route: map
    review_when: "In `c-map-october-demo-order-reset-001`, and no later than 2026-08-07."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 3 and 4); work/october-demo-basis-v3.md; history/2026-07-26-s-converge-verify-october-demo-basis-v3-001.md (V3); history/2026-07-26-s-work-october-demo-basis-v4-revision-001.md"

  - id: i-procgen-determinism
    issue: "Procedural generation is IN and mandatory as Demo Basis MUST 5; all technique left the Basis on 2026-07-26 and lives here instead. The owner's exact intent, his words: «я хочу, чтобы PGG и Dungeon Architect работали вместе. PGG определяет структуру внутри модуля, Dungeon Architect собирает из модулей сам уровень. Это совпадает с записанным пайплайном в work/pgg-analysis-2026-07-10.md.» To be checked separately, his list: Unity 6.3 with PGG is not confirmed (kill-risk), zero precedents for the pair, zero art, 2-4 days to the first module. He also corrected this issue's own text: «Живая строчка i-procgen-determinism описывала вердикт неверно — там отклонён рантайм PGG, а не Dungeon Architect.» So the recorded 2026-07-10 rejection is of PGG generating at runtime; Dungeon Architect keeps the runtime-assembler role and was never rejected. Still engineering-open and none of it canon: how the assembled level reaches the other clients, and whether the recorded editor-time acceptance ever discharged its spike condition (that close receipt is archive-quarantined and the owner authorized no read of it)."
    level: execution
    route: work
    review_when: "Before any level build CALL, and no later than the shape of g-37a1."
    evidence: "work/pgg-analysis-2026-07-10.md:9-15,21-31,42 (pipeline line 28); work/october-demo-basis-v3.md (MUST 5); history/2026-07-26-s-work-october-demo-basis-v3-revision-001.md (owner decision 2)"

  - id: i-frontier-knowledge-stale
    issue: "`knowledge/strategy-reset-boundary.md` still calls `c-work-october-demo-basis-authoring-001` «the sole lawful frontier». That CALL was discharged on 2026-07-26 and the frontier has moved twice since (v2 verification, then the v3 revision). Its own `read_by` sends every day, frame and map session to it before planning, so the stale line misinforms the next planning leg. Recorded as D2 by the v2 verification; `converge-verify` and `work` never write `knowledge/`."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier by repair if a day, frame or map leg is misled by it."
    evidence: "knowledge/strategy-reset-boundary.md:6; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (D2, captures)"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame in work/concept-frame-v1.md, but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority. The Demo Basis was authored under it and v3 does not contradict it; MUST 5 still uses the frame's own procedural-generation clause, now without any technique."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or earlier if the Demo Basis contradicts the frame."
    evidence: "work/concept-frame-v1.md; work/october-demo-basis-v3.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

  - id: i-canon-repo-evidence-read
    issue: "The owner explicitly authorized one bounded read of the frozen canon repository C:\\projects\\gas_coop_game_canon during Demo Basis v1 authoring; the exact files used are listed in the artifact and carried forward into v3. The material entered as evidence only and gained no authority. Neither the v2 nor the v3 revision read any legacy source, and on 2026-07-26 the owner declined to authorize the one archived source that finding F1 would have needed (the PGG spike close receipt) — he ordered a fresh engineering read instead. The default-closed guard is unchanged and no further legacy read is authorized."
    level: roadmap
    route: review
    review_when: "At the narrow review that closes g-12fd, or on any future request to reopen legacy canon."
    evidence: "work/october-demo-basis-v3.md; knowledge/canon-clean-authority-reset.md; .claude/settings.json"

open_calls:
  - id: c-map-october-demo-order-reset-001
    status: ready
    to: session
    for: roadmap (g-0c26 children)
    issued: 2026-07-26
    call: work/c-map-october-demo-order-reset-001-call.md
    note: "OWNER PRESENT REQUIRED (G9 — TREE changes only on his approval of the exact card text). Replan the roadmap so the FIRST outcome is the owner's own playable gameplay in the real build, and the demo-boundary specification is resized and repositioned. His words: «в начале я хочу как можно быстрее получить геймплей для себя ... первая задача будет, первый критерий»; «нужно сделать пересборку дерева»; «никаких костылей, как правильно». Mission, success criteria and the October target do NOT change — only order and content. The CALL carries the diagnosis (done_when demanded a readable moment and a public-claim ceiling before any build could back them), what must not be lost (the eight-item MUST list under his «да», the CUT list, generation mandatory, technique out, «вещество», the not-law provisionals, v3 as a source), his new unrecorded content on the ball/session length/«не успели»/art, three candidate tree shapes with none approved, and three agent amendments the owner ACCEPTED on 2026-07-26 («я с тобой согласен по поправкам»): A the first outcome's done_when must be behavioural and dated rather than a matter of taste, B the network is the riskiest thing before October and needs an early two-player smoke check right after the loop, C the map must carry the date after which art-at-zero becomes an explicit cut. His acceptance settles the principles, not the card text — every done_when still needs his per-card G9 verdict. Fold in `i-steam-sequence-tree`. Do not believe `knowledge/strategy-reset-boundary.md`'s frontier line — it is four frontiers stale. NO SHAPE, BET, TASK, TRACK, LANE, PRODUCT OR STEAM CALL; NO CHARTER EDIT (route to frame if it is wrong); NO ARCHIVE OR CANON-REPO READ; NO NUMERIC CHANCE; NO ORACLE PROMOTION."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
