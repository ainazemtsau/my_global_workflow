# NOW: indie-game-development

updated: 2026-07-26 by s-map-october-demo-order-reset-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-26
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: no outcome carries an appetite or G5 evidence, no product evidence exists, the roadmap was just replanned, and deriving a number from direction leg counts is forbidden. The Next Fest wishlist reference class that now exists (February 2026 median 806 wishlists; entrants holding under 1,000 wishlists took a median of 322) is a reference class for RECEPTION, not for whether this direction ships; it does not become a release probability. A chance becomes legal only after >=3 outcomes close with appetites and G5 evidence."
  drivers:
    - "The roadmap was replanned on 2026-07-26 and the owner approved seven outcomes (`Утверждаю точный TREE из семи результатов в этой редакции`). The FIRST outcome is now g-37a1: two connected players carry one ball through the loop in the real build and the owner plays it himself. `g-12fd` (the Demo Basis document) is DROPPED as a node - it required a readable moment and a public-claim ceiling to be fixed before any build could back them, and three legs produced eighteen findings and zero product evidence. Nothing of its content is lost: the eight-item MUST list under the owner's `да` lives in the done_when of g-37a1 and g-5e8c, the per-stage `не делаем` lists live in each card, the public-claim ceiling lives in g-2b7f, and `work/october-demo-basis-v3.md` stays a source with no authority. Procedural generation stays IN and mandatory, relocated to g-5e8c after the loop is proven; technique stays OUT of content documents; the two hall mechanics stay deferred; terminology stays `вещество`; the provisional first-slice decisions stay explicitly not-law."
    - "Valve facts verified on 2026-07-26 against partner.steamgames.com, and three of our dates were self-imposed rather than Valve's. ACTUAL Valve deadlines: festival 19-26 October 2026; registration closes 2026-08-31 23:59 PDT; all required items submitted for review by 2026-10-05; demo build plus store page submitted by 2026-09-21 to be live for the 2026-10-08 Press Preview. HARD eligibility conditions, one of which we had not recorded: the base game store page must be PUBLISHED AND PUBLIC (not merely submitted) at registration; the base game must NOT release before 2026-10-26 10:00 PDT; one Next Fest per title, ever. Store page review is 3-5 business days, plan 7. The demo is a separate AppID with its own release checklist and build review, sequenced after store approval. DERIVED, ours not Valve's: 2026-08-11 page submitted, 2026-09-03 build candidate, 2026-09-15 demo live - the last one is now evidence-backed, since demos public more than a month before a fest earn roughly 2.5x the wishlists."
    - "The store page requirement of five GAMEPLAY screenshots (no concept art, no renders) collides with `арта ноль` and produces a new dated boundary: by 2026-08-10 the scene must yield five honest gameplay screenshots, or the look is cut to the cheapest wrapper - light, colour, fog, camera on primitive shapes - with no art or asset-kit purchase. This is the art-cut date the roadmap was asked to carry."
    - "Standing cut order, owner says the word every time, February only on exact owner words: 08-07 the g-37a1 loop does not run end-to-end with two connected players -> demo scope is cut to the remaining calendar, date does not move; 08-31 page not public -> October route closed, explicit owner choice, silent slip forbidden; 09-03 no build candidate -> demo content is cut to the CHARTER quality threshold and the remainder is discarded, not deferred; 09-15 strangers cannot finish unaided -> a smaller demo is published, not the same one."
  update_when: "A gate resolves, Valve changes a published date, or g-37a1 or g-2b7f closes. A day brief recomputes SLACK, IDLE and COUNT from fresh receipts; those volatile values are not persisted without a changed fact."

issues:
  - id: i-steam-appid
    issue: "Name, base AppID and the Steam page are not started, and they are now the binding external path: Next Fest registration requires an already PUBLISHED, PUBLIC store page by 2026-08-31 23:59 PDT, not a build. The $100 fee is paid and the account is open with one unused credit. This issue is now the opening work of g-2b7f."
    level: roadmap
    route: work
    review_when: "2026-08-05, or earlier on the day a name exists."
    evidence: "work/marketing/assets/checkpoint-2026-07-12/steamworks-no-app-one-credit.png; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest; live/indie-game-development/TREE.md (g-2b7f)"

  - id: i-steam-demo-gates-unverified
    issue: "Two Steam process facts are undocumented by Valve and must be verified with Steamworks support rather than inferred, because both can silently close the October route. (1) Whether the 30-day waiting period between paying the app fee and releasing applies to releasing a DEMO app, and whether the clock runs from the already-paid fee or from app-credit activation - the onboarding doc says only `release your game`. (2) Whether deselecting the Next Fest registration checkbox restores the title's one-and-only Next Fest slot - Valve documents the mechanism but says nothing about slot restoration. Community sources on both are hearsay."
    level: roadmap
    route: work
    review_when: "Before registration is saved, and no later than 2026-08-20."
    evidence: "https://partner.steamgames.com/doc/gettingstarted/onboarding; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest; history/2026-07-26-s-map-october-demo-order-reset-001.md"

  - id: i-coop-carry-netcode
    issue: "Two players carrying one physics object together over the network is an unsolved problem in the chosen stack, and it is the load-bearing mechanic of the whole demo (`Большой шар несут вдвоём, они координируются — это уже двое`). FishNet has exactly one owner per object and only the server may change ownership; Unity's own netcode carries an OPEN feature issue titled `two players carrying a large object together` with no recommended solution; Unity PhysX is not deterministic across CPU vendors. This is the kill-risk of g-37a1 and the reason its done_when requires the carry to be tested under artificial latency and packet loss rather than on zero-latency loopback."
    level: execution
    route: work
    review_when: "In the converge of g-37a1, and no later than 2026-08-07."
    evidence: "https://fish-networking.gitbook.io/docs/guides/features/ownership; https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/2558; history/2026-07-26-s-map-october-demo-order-reset-001.md"

  - id: i-demo-scope-cap
    issue: "The 2026-08-07 scope-cut date stands and does not move - it is CHARTER risk posture («при конфликте сначала сокращается объём, а не переносится срок») and the owner's own words: «Время ограничено: 7 августа граница урезания объёма.» Its TRIGGER is re-expressed against the new first outcome, since the Demo Basis it used to wait on no longer exists: if on 2026-08-07 the g-37a1 loop does not run end-to-end with two connected players, the demo scope is cut to the remaining calendar and the carry mechanic is replaced with a cheaper one; the date does not move. Facts that stand regardless: no product evidence exists under any artifact, art is at zero, and the store page needs five gameplay screenshots by 2026-08-10, so art-at-zero now has its own dated cut inside g-2b7f."
    level: roadmap
    route: work
    review_when: "2026-08-07."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 3 and 4); live/indie-game-development/TREE.md (g-37a1 done_when 6, g-2b7f done_when 2); history/2026-07-26-s-map-october-demo-order-reset-001.md"

  - id: i-procgen-determinism
    issue: "Procedural generation is IN and mandatory; on 2026-07-26 it was relocated to g-5e8c, after the loop is proven, on the recorded evidence that hand-authored pieces come first and the generator only assembles them (Dead Cells, Enter the Gungeon; no postmortem was found advocating generation before an unproven loop). The owner's decision that generation is mandatory is unchanged - only its position moved. His exact intent, his words: «я хочу, чтобы PGG и Dungeon Architect работали вместе. PGG определяет структуру внутри модуля, Dungeon Architect собирает из модулей сам уровень. Это совпадает с записанным пайплайном в work/pgg-analysis-2026-07-10.md.» To be checked separately, his list: Unity 6.3 with PGG is not confirmed (kill-risk), zero precedents for the pair, zero art, 2-4 days to the first module. He also corrected this issue's own text: «Живая строчка i-procgen-determinism описывала вердикт неверно — там отклонён рантайм PGG, а не Dungeon Architect.» So the recorded 2026-07-10 rejection is of PGG generating at runtime; Dungeon Architect keeps the runtime-assembler role and was never rejected. Still engineering-open and none of it canon: how the assembled level reaches the other clients, and whether the recorded editor-time acceptance ever discharged its spike condition (that close receipt is archive-quarantined and the owner authorized no read of it)."
    level: execution
    route: work
    review_when: "Before any level build CALL, and no later than the shape of g-5e8c."
    evidence: "work/pgg-analysis-2026-07-10.md:9-15,21-31,42 (pipeline line 28); work/october-demo-basis-v3.md (MUST 5); history/2026-07-26-s-work-october-demo-basis-v3-revision-001.md (owner decision 2); history/2026-07-26-s-map-october-demo-order-reset-001.md"

  - id: i-frontier-knowledge-stale
    issue: "`knowledge/strategy-reset-boundary.md` still calls `c-work-october-demo-basis-authoring-001` «the sole lawful frontier» and still describes Demo Basis authoring as the only authorized work. That is now five frontiers out of date and, after 2026-07-26, factually wrong in substance too: `g-12fd` is dropped and the frontier is the converge of `g-37a1`. Its own `read_by` sends every day, frame and map session to it before planning, so the stale entry actively misinforms the next planning leg. Recorded as D2 by the v2 verification; `map`, `converge-verify` and `work` never write `knowledge/`."
    level: roadmap
    route: review
    review_when: "At the review that closes g-37a1, or earlier by repair if a day, frame or map leg is misled by it."
    evidence: "knowledge/strategy-reset-boundary.md:6; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (D2, captures); history/2026-07-26-s-map-october-demo-order-reset-001.md"

  - id: i-concept-frame-admission
    issue: "The owner approved the exact concept frame in work/concept-frame-v1.md, but durable game Canon stays NONE; the frame is an owner-approved candidate in work/, not admitted authority. Its content-bearing clauses now reach the roadmap through the done_when of g-37a1 and g-5e8c rather than through a specification document."
    level: roadmap
    route: review
    review_when: "At the review that closes g-37a1, or earlier if a built outcome contradicts the frame."
    evidence: "work/concept-frame-v1.md; work/october-demo-basis-v3.md; history/2026-07-26-s-research-canon-clean-room-dialogue-20260726-001.md; knowledge/canon-clean-authority-reset.md"

  - id: i-canon-repo-evidence-read
    issue: "The owner explicitly authorized one bounded read of the frozen canon repository C:\\projects\\gas_coop_game_canon during Demo Basis v1 authoring; the exact files used are listed in that artifact. The material entered as evidence only and gained no authority. No later leg read any legacy source, and on 2026-07-26 the owner declined to authorize the one archived source that finding F1 would have needed (the PGG spike close receipt) - he ordered a fresh engineering read instead. The default-closed guard is unchanged and no further legacy read is authorized."
    level: roadmap
    route: review
    review_when: "At the review that closes g-37a1, or on any future request to reopen legacy canon."
    evidence: "work/october-demo-basis-v3.md; knowledge/canon-clean-authority-reset.md; .claude/settings.json"

open_calls:
  - id: c-converge-g-37a1-core-loop-001
    status: ready
    to: session
    for: g-37a1
    issued: 2026-07-26
    call: work/c-converge-g-37a1-core-loop-001-call.md
    note: "Readiness route per KERNEL §2: g-37a1 is an ordinary build node with no passing converge-verify and no recorded converge-OFF triage, so it goes to `converge`. Converge locks WHAT is built - the disputed terms, the requirements as a cited node-on-paper, and every committed mechanism decomposed into the parameters it forces. The load-bearing one is the ownership/authority model for a ball two networked players carry together (`i-coop-carry-netcode`): FishNet allows exactly one owner and Unity's own netcode has this as an OPEN unsolved issue, so the wrong stub here is fatal and the node is expected to type `heavy`. Boundaries: no build, no shape, no bet, no tasks, no product mutation, no Steam CALL; generation belongs to g-5e8c and is out of scope here; art is out of scope except that g-2b7f needs five honest gameplay screenshots from this build by 2026-08-10. The 2026-08-07 boundary is real: if the loop does not run end-to-end with two connected players by then, demo scope is cut and the carry mechanic is replaced with a cheaper one."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
