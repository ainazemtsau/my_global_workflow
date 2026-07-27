# RESULT s-map-october-demo-order-reset-001

direction: indie-game-development
play: map
node: g-0c26 (roadmap, children)
call: c-map-october-demo-order-reset-001
date: 2026-07-27

## outcome

`TREE.md` now holds an owner-approved roadmap of SEVEN outcomes in which the FIRST
outcome is the owner's own playable gameplay in the real build. His exact words:
`1 принимаю  все карточки` and
`2 Утверждаю точный TREE из семи результатов в этой редакции`.

The order reset he ordered on 2026-07-26 is executed:

- **g-37a1 — Ядро** (rewritten, keeps its id and its anti-eternal-lab clause). Two
  connected players carry one ball through «набрал вещество → понесли шар вдвоём →
  сдали или не успели» in one hand-built room; the owner plays it himself; the
  hardest unknown — two players carrying one physics object over the network — is
  done FIRST and tested under artificial latency and loss; dated cut 2026-08-07.
- **g-2b7f — Витрина** (NEW). The Steam page is PUBLIC and the festival
  registration is saved by 2026-08-31 23:59 PDT. Runs parallel to g-37a1 from day
  one and depends on it only for five gameplay screenshots by 2026-08-10.
- **g-5e8c — Заход** (rewritten, keeps its id). The whole 2–4 player session: real
  fail, clean install, relaunch, two physical machines, and the level assembled by
  a generator from hand-made modules that exist BEFORE the generator; dated cut
  2026-09-03.
- **g-8a41 — Чужие люди** (NEW). Strangers play the build continuously from
  mid-August through Steam Playtest, thresholds written before each round, fixes
  only for what two participants independently hit; dated cut 2026-09-15.
- **g-7b42 — Фестиваль** (resized). Page and registration moved out to g-2b7f;
  what remains is demo AppID, build review, the quality threshold, the demo public
  by 2026-09-15, submission by 2026-10-05 and the festival itself.
- **g-9d16** and **g-c4af** — carried verbatim, unchanged.
- **g-12fd — DROPPED**, kept in the tree as one-line history.

`CHARTER.md` is untouched. Mission, success criteria and the October target are
unchanged. No bet, task, track, execution lane, product CALL or Steam CALL was
created. One `converge` CALL is open for g-37a1.

## evidence

OWNER PRESENCE AND EXACT VERDICTS. The whole leg ran with the owner present.

- Step 2 (his candidates, human-first): he waived the interrogation and supplied
  his own candidates in prose — «представь свое видение сейчас»; «в начале мы
  должны какое-то сетапить ядро, что-то около того, и потом его расширять»;
  «нам нужно будет запускать ... много параллельной работы»; «некогда там обсуждать
  ... полное демо»; «чтобы мы там не залипались на документации»; «чтобы у нас были
  такие цели, чтобы мы ... могли адаптироваться. То есть, да, что-то не пошло,
  переработать, чтобы мы быстро поняли, что что-то не идет».
- Step 2 (evidence): he did NOT waive research — he ordered it: «поэтому делай
  ресёрч, смотри, делай, как проходит, какие лучшие практики». Four independent
  research children were run in-leg rather than checkpointing to a separate
  research leg, because he had just said «у меня уже времени нету».
- Step 3 (skeleton) + the four batched decisions: `согласен со всеми
  рекомендациями` — i.e. A on all four: drop g-12fd as a node, network inside the
  first outcome, accept the 2026-08-10 screenshot boundary, generation after the
  proven loop.
- Step 5 (per-card verdict): `1 принимаю  все карточки` — given on the exact card
  text as it now stands in `TREE.md`, shown card by card before the verdict.
- Step 9 (G9): `2 Утверждаю точный TREE из семи результатов в этой редакции`.

RESEARCH THAT CHANGED THE PLAN. Four parallel children (Valve gates; solo/small-team
demo ordering postmortems; adaptive kill-signal mechanisms; parallelisation and
Unity/FishNet). Findings that moved the map, each with its source:

- **The binding external gate is a PUBLIC store page, not a build.** Next Fest
  eligibility, verbatim: «The base game store page must be published and public.»
  Registration closes 2026-08-31 23:59 PDT.
  https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october
- **A store page requires at least five gameplay-only screenshots** — no concept
  art, no renders, minimum 1920×1080.
  https://partner.steamgames.com/doc/store/assets/standard
  This collides with «арта ноль» and is the origin of the 2026-08-10 art-cut date.
- **Three of our recorded dates were ours, not Valve's**: 2026-08-11 page
  submitted, 2026-09-03 build candidate, 2026-09-15 demo live. Valve's real dates:
  2026-08-31 registration, 2026-09-21 demo build + page submitted for the
  2026-10-08 Press Preview, 2026-10-05 all required items, 19–26 October the
  festival. Store review 3–5 business days, plan 7.
- **Two Valve constraints were missing from our record entirely**: the base game
  must NOT release before 2026-10-26 10:00 PDT, and the demo is a SEPARATE AppID
  with its own release checklist and build review sequenced AFTER store approval.
  https://partner.steamgames.com/doc/store/application/demos
- **Two players carrying one physics object over the network is unsolved in the
  chosen stack.** FishNet: exactly one owner per object, only the server may change
  ownership. Unity's own netcode: an OPEN feature issue titled «two players carrying
  a large object together», no recommended solution. Unity PhysX is not
  deterministic across CPU vendors.
  https://fish-networking.gitbook.io/docs/guides/features/ownership ;
  https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/2558
- **A single-player build cannot answer whether a co-op loop works.** R.E.P.O.
  began as a single-player cleaning game and the cleaning was CUT once it was
  co-op. Retrofit costs on record: Subnautica never («almost have to start over …
  it affects everything»), Stardew Valley ~2.5 years with a dedicated specialist,
  Human: Fall Flat ~15 months. The fast co-op successes (Content Warning, PEAK,
  R.E.P.O.) were networked from day one. Semiwork, who shipped in months: «Making
  all the physics feel smooth for clients was something we struggled with for a
  long time.»
- **Generation before a proven loop is a documented trap.** Dead Cells and Enter
  the Gungeon both hand-author pieces and let the generator only ASSEMBLE them; no
  postmortem was found advocating generation before an unproven loop.
- **A demo debuting AT the festival is a documented loss.** Demos public more than
  a month before a fest earn roughly 2.5× the wishlists; February 2026 median was
  806 wishlists and entrants holding under 1,000 wishlists took a median of 322;
  entrant count rose 66% year over year.
  https://howtomarketagame.com/2026/04/13/making-sense-of-the-february-2026-steam-next-fest/
- **Steam Playtest is a free instrument we were not using**: a child appID whose
  review needs only capsules and icons — no screenshots, no trailer — up to 50,000
  keys, and it does NOT consume the one-per-title Next Fest slot.
  https://partner.steamgames.com/doc/features/playtest

THE NON-OBVIOUS CARD AND ITS ONE RARE SEED (map step 4). `g-8a41` is the
non-obvious path: not «build the demo, then test it» but strangers on the build
continuously from mid-August, with the threshold written BEFORE each round. Its
single far-domain seed is the RECOVERY trial (Oxford, March 2020): conception to
first randomised patient in NINE days by deleting the document — a two-page
information sheet, a one-page case report form, ONE primary outcome — and
pre-committing to the stopping rule while inverting the review cadence to daily
and fortnightly instead of half-yearly; twelve weeks later it produced the
dexamethasone result. The transferable point is that speed came from deleting the
document and fixing the decision rule in advance, which is exactly the failure this
direction just suffered.
https://www.ndph.ox.ac.uk/longer-reads/how-to-set-up-a-trial-in-nine-days
Supporting solo-specific mechanisms adopted into card wording rather than into a
process: thresholds written before the round (blind analysis), fixing only what two
participants independently hit (Nielsen five-user rounds), and a dated cut in every
card instead of a movable date.

AMENDMENTS A, B AND C — ALL THREE VISIBLE IN THE APPROVED TREE.

- **A (behavioural, dated done_when).** g-37a1 done_when 3 makes the owner's
  verdict decide WHAT HAPPENS NEXT rather than whether the outcome was reached;
  done_when 1 requires repeatable end-to-end runs from a named build; done_when 6
  carries the 2026-08-07 cut. Every other card carries the same shape with its own
  date. His pre-existing done_when «Сцена остаётся частью пути демо, а не отдельной
  игрой, вечной лабораторией» is preserved verbatim as g-37a1 done_when 4.
- **B (network early).** Strengthened beyond the amendment on the evidence above:
  the two-player carry is not a smoke check after the loop, it is INSIDE the first
  outcome and is its riskiest element, tested under artificial latency and packet
  loss (g-37a1 done_when 1, 2). The owner approved this explicitly as decision 2.
- **C (art-cut date).** g-2b7f done_when 2: five honest gameplay screenshots by
  2026-08-10 or the look is cut to the cheapest wrapper — light, colour, fog,
  camera on primitive shapes — with no art or asset-kit purchase.

DISPOSITION OF `g-12fd` (CALL done_when 2). DROPPED, on the owner's approval of
recommendation A. `outcome_kind: specification` is removed with the node; nothing
in the tree now claims that a versioned owner-approved specification exhausts a
done_when. Its content is preserved and relocated, not deleted: the eight-item MUST
list under his «да» lives in the done_when of g-37a1 and g-5e8c; the per-stage
«не делаем» lists live inside each card, which satisfies CHARTER premortem 4 better
than one document did; the public-claim ceiling lives in g-2b7f done_when 5;
`work/october-demo-basis-v3.md` is untouched and remains a SOURCE with zero
authority. Neither oracle file was promoted.

`i-steam-sequence-tree` RESOLVED (CALL done_when 4). The tree no longer says the
Steam branch starts after the first playable technical-stack proof. `g-2b7f` is its
own outcome running parallel from day one, and its `why` records the reason: Valve
requires an already public page, not a build. The issue is removed from `NOW.md`
with this disposition.

DEPTH AND LENS SWEEP (steps 7, 8). Seven top-level outcomes; deeper splits happen
later in shape. Coverage against the six CHARTER lenses, approved by the owner in
the same verdict: (1) October demo and release — all seven; (2) player clarity and
quality — g-8a41, for the first time a separate outcome; (3) solo feasibility —
every card carries its own «не делаем» list and its own dated cut; (4) new approved
canon — `not_needed` as a node: content is decided inside the outcome that owns it,
Canon stays NONE and `concept-frame-v1` stays a candidate; (5) paid product and
commercial learning — g-9d16, g-c4af, and g-2b7f as the entry to both; (6) reliable
owner work — `not_needed` as a node: «сначала режем объём, а не двигаем срок»
appears as a date in every card.

NEGATIVE EVIDENCE AND WHAT WAS NOT DONE. No shape, bet, task, track or execution
lane was created. No product or Steam CALL was issued. `CHARTER.md` was not
edited. No archive and no frozen-canon read occurred. No numeric release chance was
published, and the new Next Fest wishlist reference class was explicitly recorded as
a reference class for RECEPTION, not a release probability. No recorded owner
decision was reversed: procedural generation stays IN and mandatory and only
changed position, technique stays out of content documents, the two hall mechanics
stay deferred, terminology stays «вещество», the provisional first-slice decisions
stay not-law. The ball's readable-moment rule, the cube law, session length, the
meaning of «не успели» and the art level were NOT decided here; each is routed to
the outcome that owns it.

ONE FACT NAMED TO THE OWNER AND RECORDED. None of the comparable co-op physics
successes won through a Next Fest — PEAK went announce-to-launch in five days,
Content Warning surprise-launched free, R.E.P.O. and Lethal Company went straight
into Early Access. The October target is CHARTER and does not move; the fact is
recorded so the festival is understood as a marketing route rather than the proven
path of the genre, and so g-9d16 stays the real objective.

## state_changes

`live/indie-game-development/TREE.md`
- Preserve root `g-0c26` verbatim — goal, done_when, why, `status: shaped`, detail.
- Replace the six children with the exact seven-card G9 artifact in this order:
  `g-37a1`, `g-2b7f`, `g-5e8c`, `g-8a41`, `g-7b42`, `g-9d16`, `g-c4af`; each
  `status: parked`, each with goal, measurable done_when, one-line why, empty
  children. Changed and new cards point `detail:` at this history file; `g-9d16`
  and `g-c4af` keep their existing text and detail pointer verbatim.
- Rewrite `g-37a1` and `g-5e8c` in place, keeping their ids; resize `g-7b42` by
  removing page and registration.
- Append `g-12fd` last with `status: dropped`, a one-line goal, and a `why` that
  records the reason and where its content went. Remove `outcome_kind:
  specification` with it.
- Update `owner_approved` to add the 2026-07-26 order reset and his three exact
  verdict strings.

`live/indie-game-development/NOW.md`
- Set `updated: 2026-07-26 by s-map-october-demo-order-reset-001`.
- Preserve `bet: null`, `tasks: []`, `recurring: []`, `decisions: []`; no track,
  no lane.
- Keep `direction_forecast.status: no_basis`; replace the basis and drivers with
  what actually changed: the approved seven-outcome roadmap and the dropped
  specification node; the verified Valve gates with the three self-imposed dates
  named as ours; the five-gameplay-screenshot collision producing the 2026-08-10
  art-cut date; the standing cut order re-expressed with the new triggers. Record
  the Next Fest wishlist reference class as reception-only and keep the numeric
  chance forbidden.
- Remove `i-steam-sequence-tree` with the disposition above.
- Re-express `i-demo-scope-cap`: the 2026-08-07 date is unmoved; its trigger
  becomes «the g-37a1 loop does not run end-to-end with two connected players».
- Update `i-steam-appid` to name g-2b7f and the public-page-by-2026-08-31 gate.
- Update `i-procgen-determinism` to record that generation moved to `g-5e8c` and
  that its `review_when` is now the shape of `g-5e8c`.
- Re-point the dead `g-12fd`-based review triggers of `i-frontier-knowledge-stale`,
  `i-concept-frame-admission` and `i-canon-repo-evidence-read` at the review that
  closes `g-37a1`, and record that the stale frontier line is now also wrong in
  substance.
- Add `i-coop-carry-netcode` (unsolved two-player carry over FishNet/Unity; the
  kill-risk of g-37a1) and `i-steam-demo-gates-unverified` (whether the 30-day
  post-fee wait applies to releasing a demo, and whether withdrawing registration
  restores the one-per-title Next Fest slot — both to be verified with Steamworks,
  not inferred).
- Clear the returning CALL `c-map-october-demo-order-reset-001` and register
  exactly one ready continuation `c-converge-g-37a1-core-loop-001`, `to: session`,
  `for: g-37a1`, pointer `work/c-converge-g-37a1-core-loop-001-call.md`.

`live/indie-game-development/work/`
- Add `c-converge-g-37a1-core-loop-001-call.md` — the full converge CALL for
  g-37a1, carrying the load-bearing unknown, the born-closed owner decisions, the
  undecided owner content, the g-2b7f screenshot edge and the 2026-08-07 boundary.

`live/indie-game-development/LOG.md`
- Prepend the one-line log entry from `log` exactly once.

`live/indie-game-development/history/`
- Save this full RESULT once as
  `2026-07-27-s-map-october-demo-order-reset-001.md`.

## captures

- The owner's own candidate rule for the readable moment — impact above a threshold
  produces cracks that leak, by analogy to carried loot taking damage — is stronger
  than the rejected «протискивают» dependency and needs no deformation mechanic. It
  is undecided content carried into the g-37a1 converge, not a requirement.
- His cube-law growth rule («чем больше, тем ... кратно больше он вмещает ... но тем
  тяжелее нести»), with his own «возможно не сейчас мы этот закон должны
  прорабатывать».
- Steam Playtest was available the whole time and unused; it may be worth a standing
  entry in the direction's knowledge once g-8a41 proves it.
- The research child noted that a co-op demo has a documented gap nobody has
  measured: empty-lobby / «no one to play with» effects at Next Fest. Worth a
  bounded research question before 2026-09-15.

## decisions_needed

[]

## play_check

- 1 Recite: done — mission, the four success criteria, the six-outcome tree and the
  factual state (no bet, no product evidence, art at zero, twelve days to
  2026-08-07) were restated in plain words before anything was proposed.
- 2 Candidates & evidence (owner): done — nothing was shown before he answered.
  He supplied his own candidates («в начале мы должны какое-то сетапить ядро ... и
  потом его расширять»; parallel work; no full demo document) and ORDERED research
  rather than waiving it («делай ресёрч ... какие лучшие практики»). Four
  independent research children were run in-leg, per KERNEL §2 `call:research` and
  map step 2's search-first clause, because he said «у меня уже времени нету»; their
  merged findings are in `evidence`.
- 3 Skeleton (owner): done — the whole map was shown on one screen as four waves
  plus seven one-line outcomes, together with the facts forcing it and four batched
  decisions. Owner: `согласен со всеми рекомендациями`.
- 4 Cards: done — seven cards elaborated with goal, verifiable done_when, root-facing
  why, a named failure signal and a dated cut. The non-obvious card is g-8a41,
  seeded from exactly one rare far-domain outlier (the RECOVERY trial), not from a
  moodboard of game-industry hits.
- 5 Per-node verdict (owner): done — the exact card text was shown card by card and
  the verdict was given on that text: `1 принимаю  все карточки`. No card was
  accepted silently; `g-12fd`'s drop was a separately named decision he answered
  before the cards were written.
- 6 Order (owner): done — accepted inside the same verdict: g-37a1 → g-2b7f
  (parallel from day one) → g-5e8c → g-8a41 (continuous from mid-August) → g-7b42 →
  g-9d16 → g-c4af, with the riskiest assumption first INSIDE the first outcome.
- 7 Depth check: done — top level only, seven outcomes, deeper splits deferred to
  shape.
- 8 Lens sweep: done — verdict per lens with two explicit `not_needed` entries
  (separate canon node; separate health/rhythm node), recorded in `evidence`.
- 9 Close (owner): done — G9 verdict `2 Утверждаю точный TREE из семи результатов в
  этой редакции`. TREE and LOG saved; one continuation CALL registered; no
  execution lane created.

## log

g-0c26/october-demo-order-reset: the owner approved a seven-outcome roadmap in which the FIRST outcome is his own playable gameplay in the real build («1 принимаю  все карточки»; «2 Утверждаю точный TREE из семи результатов в этой редакции») — g-37a1 is rewritten as two connected players carrying one ball through the loop in one hand-built room with the hardest unknown first and a 2026-08-07 cut date, g-2b7f is a NEW outcome making the Steam page public and the festival registration saved by 2026-08-31 running parallel from day one, g-5e8c becomes the whole 2-4 player session with generation relocated after the proven loop, g-8a41 is a NEW outcome putting strangers on the build continuously from mid-August through Steam Playtest with thresholds written before each round, g-7b42 keeps only qualification and the festival, g-9d16 and g-c4af are unchanged, and g-12fd is DROPPED with its content preserved in the cards; he accepted all four recommendations («согласен со всеми рекомендациями») after fresh research corrected three facts the plan was wrong about — registration requires an already PUBLIC store page and five gameplay-only screenshots so art-at-zero gets a dated cut on 2026-08-10, two players carrying one object over the network is unsolved in FishNet and open in Unity's own netcode, and generation before a proven loop is a documented trap; i-steam-sequence-tree resolved by the decoupling, i-demo-scope-cap re-expressed against the loop with 2026-08-07 unmoved, two new issues opened for the unsolved co-carry netcode and two unverifiable Steam gates; no bet, task, lane, product or Steam CALL created, CHARTER untouched, one converge CALL open for g-37a1.

## next

CALL c-converge-g-37a1-core-loop-001
to: session
direction: indie-game-development
play: converge
node: g-37a1
goal: |
  The WHAT of the first outcome is locked to an owner-signed spec that `shape` can
  consume: two connected players carry one ball through the loop in one hand-built
  room, in the real `gas_coop_game` build, and the owner plays it himself.
context: |
  Full CALL text: `work/c-converge-g-37a1-core-loop-001-call.md`. Readiness route
  per KERNEL §2: `g-37a1` is an ordinary build node with no passing
  `converge-verify` RESULT and no recorded converge-OFF triage, so it goes to
  `converge`. The load-bearing unknown is the ownership/authority model for a ball
  two networked players carry together (`i-coop-carry-netcode`), so the node is
  expected to type `heavy` — decide that at triage, do not assume it.
boundaries: |
  Converge only: no build, no shape, no bet, no tasks, no lanes, no executor CALL,
  no product or Steam mutation. Do not reverse the recorded owner decisions. Do not
  decide owner content. Do not reopen `g-12fd` or author a replacement
  specification. No archive or frozen-canon read. Do not move 2026-08-07.
done_when: |
  As in the CALL file: triage line recorded, glossary and §WHAT signed, the carry
  mechanism decomposed into its forced parameters, forward- and backward-clean,
  owner forks batched, and `next` routed to `converge-arch` if heavy else
  `converge-verify`.
return: |
  One `converge` RESULT with the triage line, signed glossary and §WHAT,
  `converge_coverage`, the owner's verbatim signoffs and the routing handoff.
budget: one owner-present session
surface: any session with the owner present; a fresh chat

END_OF_FILE: live/indie-game-development/history/2026-07-27-s-map-october-demo-order-reset-001.md
