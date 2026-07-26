# NOW: indie-game-development

updated: 2026-07-26 by s-converge-verify-october-demo-basis-v3-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: the Demo Basis still names eight MUST items and none carries an appetite or G5 evidence, two Basis versions have now failed independent verification, no relevant empirical reference class exists for a solo Unity co-op demo in 8 weeks, and deriving a number from direction leg counts is forbidden. A chance becomes legal only after >=3 MUST items close with appetites and G5 evidence."
  drivers:
    - "There is no active bet, task or execution lane. The single live Demo Basis is `work/october-demo-basis-v3.md`, and it FAILED independent verification on 2026-07-26 with eight named findings V1-V8 (`history/2026-07-26-s-converge-verify-october-demo-basis-v3-001.md`). v1 and v2 are tombstones with full texts in commits 3f135b9b and c982c79a. Every owner decision still stands and none is reopened: procedural generation IN and mandatory, technique OUT of the Basis, the two hall mechanics deferred, terminology «вещество», the provisional first-slice decisions explicitly not-law, the engineering read in `i-procgen-determinism`. The v2 finding F8 (MUST 5's disclosure) is judged DISCHARGED by the pointer line plus that live engineering read. What failed: the readable moment of §3 - required by g-12fd done_when 1 and by CHARTER quality - has none of its three physical dependencies in MUST while the artifact asserts it does (V1, the one large content finding); art does not exist and appears nowhere in the scope partition after the technique deletion took its only trace with it (V3); the not-law provisional section carries a public prohibition in §5 (V4); MUST 7's «не успели» branch has no mechanism that is not CUT or deferred (V5). Four further findings are defects of the mechanically delegated repair round: «двадцать минут» still stands in §1 and §2 while the artifact twice says it does not (V2) and the «Можно» list still permits «абсурдный мир» that no MUST produces (V7) - both are the SAME point failing a second time, so KERNEL two-strikes is live on each; the null-exceptions statement collides with the dormant falsifier (V6); and the artifact reproduces the technique it declares removed (V8). Effort split as verified: one real content decision, four small ones, three text corrections. The sole current frontier is the owner-present `c-work-october-demo-basis-v4-revision-001`, then a fresh converge-verify against v4, then narrow review, and only then shape of g-37a1. Neither owner approval nor a failed verification closes g-12fd."
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
    issue: "TWO Basis versions have now failed independent verification on 2026-07-26: v2 with ten findings, v3 with eight. No version has passed. The cut rule is unchanged: if no Demo Basis has passed converge-verify by 2026-08-07 — twelve days from 2026-07-26 — demo scope is cut to fit the remaining calendar and the October date does not move. The remaining route is one owner-present revision leg plus one fresh verification, so the boundary is now two legs away rather than one. The eight MUST items still carry no appetites. Verified this round: the artifact's scope partition is also silent on art, which MUST 5 requires and which the owner's own words put at zero (V3) — that is scope, not technique, and it is the finding most likely to matter for the cut. MUST 5's technical dependency stays OUTSIDE the Basis by the owner's order, in `i-procgen-determinism`; his words: «Время ограничено: 7 августа граница урезания объёма.»"
    level: roadmap
    route: review
    review_when: "2026-08-07, or earlier on the day a Demo Basis version passes converge-verify."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 1 and 4); work/october-demo-basis-v3.md; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (F8); history/2026-07-26-s-converge-verify-october-demo-basis-v3-001.md (V3, V1)"

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
  - id: c-work-october-demo-basis-v4-revision-001
    status: ready
    to: session
    for: g-12fd
    issued: 2026-07-26
    call: work/c-work-october-demo-basis-v4-revision-001-call.md
    note: "OWNER PRESENT REQUIRED. Return the eight findings V1-V8 of the failed v3 verification and produce work/october-demo-basis-v4.md from the owner's actual words. Every owner decision stands and none is reopened; F8/v2's disclosure question is closed as discharged. One real content decision (V1 — the readable moment has no MUST support and the artifact claims it does), four small content choices (V3 art in the partition, V4 the not-law section carrying a public prohibition, V5 «не успели» with no mechanism, V7 «абсурдный мир» in «Можно»), three text corrections needing only his confirmation (V2 «двадцать минут», V6 null-exceptions vs the dormant falsifier, V8 the technique quoted back into the Basis). KERNEL two-strikes is LIVE on V2 and V7: both are the same point failing a second time because the previous repair was item-scoped, so this round must fix the rule and state it in the artifact. If he delegates again, every repair must be checked against every other repair before assembly — four of the eight findings came from that class. 2026-08-07 is twelve days out and the boundary is now two legs away. g-12fd stays parked. NO SHAPE, BET, TASK, TRACK, PRODUCT, STEAM, CHARTER/TREE/KNOWLEDGE OR ARCHIVE/CANON-REPO READ OR MUTATION."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
