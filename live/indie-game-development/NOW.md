# NOW: indie-game-development

updated: 2026-07-27 by s-repair-post-concept-reset-consistency-001

bet: null

tasks: []

direction_forecast:
  status: no_basis
  target: "An accepted-quality demo in the October 2026 Steam Next Fest, followed by a paid Steam release and a reusable solo-release process"
  as_of: 2026-07-27
  basis: "Verified Valve gates plus derived last-safe dates are the standing basis. A numeric chance still has no denominator: no outcome carries an appetite or G5 evidence, no product evidence exists, the roadmap was just replanned, and deriving a number from direction leg counts is forbidden. The Next Fest wishlist reference class that now exists (February 2026 median 806 wishlists; entrants holding under 1,000 wishlists took a median of 322) is a reference class for RECEPTION, not for whether this direction ships; it does not become a release probability. A chance becomes legal only after >=3 outcomes close with appetites and G5 evidence."
  drivers:
    - "CONCEPT RESET on 2026-07-27. After an evidence pass the owner replaced the CONTENT of the first outcome while keeping the seven-outcome roadmap, all dates and every other card untouched. The carried ball and every cargo-transport mechanic are OUT; the whole game is interaction with the substance - detect it, pass through it, move it. Five laws now sit in `g-37a1` done_when and he approved the exact card text with `да`: (1) no cargo-transport mechanics at all; (2) the substance is an ENVIRONMENT, never a scripted pursuer; (3) one-way passage, no way back; rooms have real height and the substance's vertical distribution is part of the problem; (4) substance kinds are distinguishable at a glance without instrument or UI, verified on someone outside development; (5) air is the only counter and can be passed to a teammate. Two owner corrections are recorded so they are not re-introduced: light-versus-heavy is a testing basis and NOT law - the substances may have other properties or other states entirely, which is why the term stays `вещество` and not `газ`; and the ROUTE DIRECTION (down, up or across) is explicitly NOT decided, because difficulty comes from what a section is made of rather than from which way it runs. The structure is a chain of sections with rest stops between them; `g-37a1` is ONE section, `g-5e8c` is the whole chain. What this buys: the two-player carried-rigidbody netcode risk is GONE with the ball, and substance-to-object interaction leaves the simulation as an explicit scope cut."
    - "The roadmap was replanned on 2026-07-27 and the owner approved seven outcomes (`Утверждаю точный TREE из семи результатов в этой редакции`). SUPERSEDED IN PART, and the superseding driver is the one above: that leg's first outcome was two players carrying one ball, and the concept reset a few hours later replaced it with the substance passage. What survives from that leg unchanged is everything else. `g-12fd` (the Demo Basis document) is DROPPED as a node - it required a readable moment and a public-claim ceiling to be fixed before any build could back them, and three legs produced eighteen findings and zero product evidence. Nothing of its content is lost: the eight-item MUST list under the owner's `да` lives in the done_when of g-37a1 and g-5e8c, the per-stage `не делаем` lists live in each card, the public-claim ceiling lives in g-2b7f, and `work/october-demo-basis-v3.md` stays a source with no authority. Procedural generation stays IN and mandatory, relocated to g-5e8c after the loop is proven; technique stays OUT of content documents; the two hall mechanics stay deferred; terminology stays `вещество`; the provisional first-slice decisions stay explicitly not-law."
    - "Valve facts verified on 2026-07-27 against partner.steamgames.com, and three of our dates were self-imposed rather than Valve's. ACTUAL Valve deadlines: festival 19-26 October 2026; registration closes 2026-08-31 23:59 PDT; all required items submitted for review by 2026-10-05; demo build plus store page submitted by 2026-09-21 to be live for the 2026-10-08 Press Preview. HARD eligibility conditions, one of which we had not recorded: the base game store page must be PUBLISHED AND PUBLIC (not merely submitted) at registration; the base game must NOT release before 2026-10-26 10:00 PDT; one Next Fest per title, ever. Store page review is 3-5 business days, plan 7. The demo is a separate AppID with its own release checklist and build review, sequenced after store approval. DERIVED, ours not Valve's: 2026-08-11 page submitted, 2026-09-03 build candidate, 2026-09-15 demo live - the last one is now evidence-backed, since demos public more than a month before a fest earn roughly 2.5x the wishlists."
    - "The store page requirement of five GAMEPLAY screenshots (no concept art, no renders) collides with `арта ноль` and produces a new dated boundary: by 2026-08-10 the scene must yield five honest gameplay screenshots, or the look is cut to the cheapest wrapper - light, colour, fog, camera on primitive shapes - with no art or asset-kit purchase. This is the art-cut date the roadmap was asked to carry."
    - "Standing cut order, owner says the word every time, February only on exact owner words: 08-07 the g-37a1 section is not passed end-to-end by two connected players -> demo scope is cut to the remaining calendar, date does not move; 08-31 page not public -> October route closed, explicit owner choice, silent slip forbidden; 09-03 no build candidate -> demo content is cut to the CHARTER quality threshold and the remainder is discarded, not deferred; 09-15 strangers cannot finish unaided -> a smaller demo is published, not the same one."
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
    evidence: "https://partner.steamgames.com/doc/gettingstarted/onboarding; https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest; history/2026-07-27-s-map-october-demo-order-reset-001.md"

  - id: i-substance-passage-open-questions
    issue: "The concept reset fixed five laws and deliberately left everything else open. These are NOT to be answered ahead of the work that needs them - the owner's standing rule is that a question is discussed only once a concrete task has stopped on it. In his own stated order of importance: (1) GRID AND SIZE - how many rooms in one section, how much volume is simulated at once, hand-built or generated. His note: the simulation was planned around roughly 150 fairly large rooms as ONE level with optimisation still unwritten, and the new concept neither needs the whole space filled nor tolerates it being nearly empty; 150 is a candidate, not a given, and `g-37a1` done_when 7 requires the number to be fixed before the build and to not grow. (2) SUBSTANCES - how many, which properties, and whether they are gases at all rather than liquid or another state; light-versus-heavy is a testing basis only. (3) ROUTE DIRECTION - down, up or across. (4) DETECTION - one instrument per crew, several, different types, pickable; the owner rejected fixing one-per-crew. (5) REACTIONS - whether the first version needs them at all. (6) REST STOPS between sections - how they work and what they give. (7) SETTING and why the crew goes in; the plant framing was rejected, a mine was recommended but NOT chosen. The first section's geometry decides several of these, so they resolve on a real level, not on paper. (8) AN AMBIGUITY INSIDE THE APPROVED CARD, named by an independent audit on 2026-07-27 and left for the converge rather than patched here, because the card carries the owner's `да`: done_when 2 requires the player to MOVE the substance, while done_when 9 excludes `взаимодействие вещества с предметами`. The recorded intent of that exclusion is the scope cut the owner named - the substance no longer has to interact with LOOT or carried objects - not a ban on doors, hatches or vents. Read literally, though, done_when 9 would also cut any tool or container, and done_when 2 names no verb. The converge decides what moves the substance and, if the wording needs tightening, returns it to the owner as a card edit."
    level: execution
    route: work
    review_when: "Each in the converge of g-37a1 or when a build task stops on it; grid and size first, and no later than 2026-08-07."
    evidence: "live/indie-game-development/TREE.md (g-37a1 done_when 7); history/2026-07-27-s-map-substance-passage-concept-reset-001.md"

  - id: i-demo-scope-cap
    issue: "The 2026-08-07 scope-cut date stands and does not move - it is CHARTER risk posture («при конфликте сначала сокращается объём, а не переносится срок») and the owner's own words: «Время ограничено: 7 августа граница урезания объёма.» Its TRIGGER is re-expressed against the new first outcome, since the Demo Basis it used to wait on no longer exists: if on 2026-08-07 the g-37a1 section is not passed end-to-end by two connected players, the demo scope is cut to the remaining calendar; the date does not move. Facts that stand regardless: no product evidence exists under any artifact, art is at zero, and the store page needs five gameplay screenshots by 2026-08-10, so art-at-zero now has its own dated cut inside g-2b7f."
    level: roadmap
    route: work
    review_when: "2026-08-07."
    evidence: "live/indie-game-development/CHARTER.md (Risk posture; premortem 3 and 4); live/indie-game-development/TREE.md (g-37a1 done_when 11, g-2b7f done_when 2); history/2026-07-27-s-map-october-demo-order-reset-001.md; history/2026-07-27-s-map-substance-passage-concept-reset-001.md"

  - id: i-procgen-determinism
    issue: "Procedural generation is IN and mandatory; on 2026-07-26 it was relocated to g-5e8c, after the loop is proven, on the recorded evidence that hand-authored pieces come first and the generator only assembles them (Dead Cells, Enter the Gungeon; no postmortem was found advocating generation before an unproven loop). The owner's decision that generation is mandatory is unchanged - only its position moved. His exact intent, his words: «я хочу, чтобы PGG и Dungeon Architect работали вместе. PGG определяет структуру внутри модуля, Dungeon Architect собирает из модулей сам уровень. Это совпадает с записанным пайплайном в work/pgg-analysis-2026-07-10.md.» To be checked separately, his list: Unity 6.3 with PGG is not confirmed (kill-risk), zero precedents for the pair, zero art, 2-4 days to the first module. He also corrected this issue's own text: «Живая строчка i-procgen-determinism описывала вердикт неверно — там отклонён рантайм PGG, а не Dungeon Architect.» So the recorded 2026-07-10 rejection is of PGG generating at runtime; Dungeon Architect keeps the runtime-assembler role and was never rejected. Still engineering-open and none of it canon: how the assembled level reaches the other clients, and whether the recorded editor-time acceptance ever discharged its spike condition (that close receipt is archive-quarantined and the owner authorized no read of it)."
    level: execution
    route: work
    review_when: "Before any level build CALL, and no later than the shape of g-5e8c."
    evidence: "work/pgg-analysis-2026-07-10.md:9-15,21-31,42 (pipeline line 28); work/october-demo-basis-v3.md (MUST 5); history/2026-07-26-s-work-october-demo-basis-v3-revision-001.md (owner decision 2); history/2026-07-27-s-map-october-demo-order-reset-001.md"

  - id: i-frontier-knowledge-stale
    issue: "`knowledge/strategy-reset-boundary.md` still calls `c-work-october-demo-basis-authoring-001` «the sole lawful frontier» and still describes Demo Basis authoring as the only authorized work. That is now five frontiers out of date and, after 2026-07-26, factually wrong in substance too: `g-12fd` is dropped and the frontier is the converge of `g-37a1`. Its own `read_by` sends every day, frame and map session to it before planning, so the stale entry actively misinforms the next planning leg. Recorded as D2 by the v2 verification; `map`, `converge-verify` and `work` never write `knowledge/`."
    level: roadmap
    route: review
    review_when: "At the review that closes g-37a1, or earlier by repair if a day, frame or map leg is misled by it."
    evidence: "knowledge/strategy-reset-boundary.md:6; history/2026-07-26-s-converge-verify-october-demo-basis-v2-001.md (D2, captures); history/2026-07-27-s-map-october-demo-order-reset-001.md"

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
  - id: c-converge-g-37a1-substance-passage-001
    status: ready
    to: session
    for: g-37a1
    issued: 2026-07-27
    call: work/c-converge-g-37a1-substance-passage-001-call.md
    note: "Replaces the withdrawn c-converge-g-37a1-core-loop-001, which was written about a carried ball and the netcode under it and died with the concept reset. Readiness route per KERNEL §2 is unchanged: g-37a1 is an ordinary build node with no passing converge-verify and no recorded converge-OFF triage, so it goes to `converge`. The five approved laws are born-closed and are NOT reopened. The leg's own first business is the owner's stated priority: the grid and the size envelope - rooms per section, volume simulated at once, hand-built versus generated - then how the player reads the substance at a glance. Owner-content questions in `i-substance-passage-open-questions` are surfaced as signed owner forks, never answered by an agent. Boundaries: no build, no shape, no bet, no tasks, no product mutation, no Steam CALL; level generation belongs to g-5e8c; art is out of scope except that g-2b7f needs five honest gameplay screenshots from this build by 2026-08-10. Fresh chat, owner present; the 2026-08-07 boundary does not move."

recurring: []

decisions: []

END_OF_FILE: live/indie-game-development/NOW.md
