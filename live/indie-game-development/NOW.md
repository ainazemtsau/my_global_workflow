# NOW: indie-game-development

updated: 2026-07-26 by s-work-october-demo-basis-v3-revision-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis still names eight MUST items and none carries an appetite or G5 evidence, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The single live Demo Basis is `work/october-demo-basis-v3.md`, written 2026-07-26 from the owner's five recorded decisions on the ten findings of the FAILED v2 verification; v1 and v2 are tombstones with full texts in commits 3f135b9b and c982c79a. What stands on his verbatim words: MUST 5 reduced to «Процедурная генерация уровня из модулей» with all technique removed from the Basis, the «обязательно двое» requirement removed with one physical support left, four provisional first-slice decisions marked explicitly not-law, and an ordered engineering read. MUST 1-4 and 6-8 carry v2's «да» verbatim. The other eight findings he delegated with «чини сам, ко мне не возвращайся с ними», so they were repaired mechanically and each repair is named in the artifact and in the verification CALL. No owner decision was reversed; procedural generation stays IN and generation is mandatory. There is no separate «да» on the assembled v3 text and none was requested. The sole current frontier is the fresh `c-converge-verify-october-demo-basis-v3-001`, then narrow review, and only then shape of g-37a1. Neither owner approval nor a failed verification closes g-12fd."
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
    issue: "The owner's Demo Basis reached v3 on 2026-07-26, ahead of the 2026-08-07 boundary, so the scope cut is not triggered by absence. No Basis version has passed converge-verify yet: v2 FAILED on 2026-07-26 and v3's verification is open. The cut depends on v3: if no Demo Basis has passed converge-verify by 2026-08-07, demo scope is cut to fit the remaining calendar and the October date does not move. The eight MUST items still carry no appetites. MUST 5 entered after the boundary was set and its technical dependency is now unbounded OUTSIDE the Basis — the owner removed all technique from the artifact on 2026-07-26 and ordered a separate engineering read (`i-procgen-determinism`); his own words in that leg: «Время ограничено: 7 августа граница урезания объёма.»"
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day a Demo Basis version passes converge-verify."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/october-demo-basis-v3.md; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (F8); history/2026-07-26-s-work-october-demo-basis-v3-revision-001.md"

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
  - id: c-converge-verify-october-demo-basis-v3-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-26
    call: work/c-converge-verify-october-demo-basis-v3-001-call.md
    note: "FRESH INDEPENDENT REFUTATION of the exact artifact work/october-demo-basis-v3.md, identity october-demo-basis-v3. Never the v1 authoring, v2 revision or v3 revision chat. The CALL carries the disposition of every v2 finding F1-F10 so each can be checked against the text, and it names the narrower approval binding: the owner's verbatim words cover MUST 5, the technique removal, the removed «обязательно двое» requirement, the not-law provisional decisions and the ordered engineering read, while the other eight findings were repaired mechanically under his explicit delegation «чини сам, ко мне не возвращайся с ними» — that repair class is attack surface, and there is no separate «да» on the assembled v3 text. Sharpest tension to attack: MUST 5's unresolved external dependency versus his order that technique leave the Basis. PASS opens narrow review only; FAIL returns to owner-authority work. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT, STEAM, KNOWLEDGE OR ARCHIVE/CANON-REPO READ OR MUTATION."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
