superseded_by: work/c-map-g-37a1-core-requirements-001-call.md — UNSPENT, never dispatched.
  Amended three times in one evening as the owner's instruction sharpened, and then
  superseded on 2026-07-27 because its entry point was wrong: it opened on the section
  envelope, and he ruled that dimensions cannot be discussed apart from the concept and
  that what is needed first is the minimal CORE — which mechanics must work for this to be
  a game. Its rows are not lost: the passability row and the gas-versus-liquid row become
  core-mechanic questions in the successor, the g-5e8c row rides along there unchanged,
  the engine-blind rule and the decision ladder are recorded as issues, and the routing
  decision is superseded by his own answer (requirements first, then the check, then the
  plan). Kept for its record of how the instruction sharpened; it has no authority.

CALL c-map-g-37a1-verify-rows-001
to: session
direction: indie-game-development
play: map
node: g-37a1 (with a correction to g-5e8c)
goal: |
  Three things the owner alone can settle, taken to him as three short questions with
  options and a recommendation each, and nothing else. The card is NOT reopened: it
  carries his verdict on exact text twice, and two of the three rows are about clauses
  whose MEANING an outsider cannot read, not about clauses he should rewrite.
context: |
  AUTHORITY, in this order. `history/2026-07-27-s-converge-verify-g-37a1-digging-card-001.md`
  — the verification that FAILED and produced these rows; read its `## outcome` and
  findings V3, V4, V8 first. Then `live/indie-game-development/TREE.md` (g-37a1 and
  g-5e8c), `live/indie-game-development/NOW.md`, and
  `live/indie-game-development/work/converge-g-37a1.md` (§6-BIS, §4 R18/R23-R27, §7's
  four corrections — the CONSUMED banner tells you to read the amendments before the
  body they correct, and §11 is stale and warned about nowhere: see V9).

  WHAT THE VERIFICATION FOUND, in one paragraph, because it changes the tone of these
  questions. Most of what was attacked HELD: §6-BIS's reason survived its sharpest
  attack, all four of §7's first-hand corrections are confirmed, and §14 is the
  strongest verification instrument in either document. What failed is narrower and
  specific — the artifact never raised four whole classes of decision, all of them on
  the same side of it (the body, the venue, the experiment rig, the run lifecycle), and
  the flow claim under every hero frame is now CLOSED against the artifact: the
  numerator cannot move the burst timescale at all, because the per-tick move is capped
  at one twelfth of whatever drives it by a stability floor the engine enforces with a
  throw. That is not this leg's business, but it is why nobody should treat the
  substance step as cheap.

  ROW 0 — ADDED 2026-07-27 by writer amendment, and it comes FIRST, because the owner's
  own words re-order this leg: «Мы газ, мы отсюда запроектировали под другой концепт. Мы
  тогда думали, что у нас будут большие комнаты, то сейчас, я так понимаю, у нас по
  высоте, скорее всего, будет ограничено, ну там по ширине, по длине так же. И, то есть,
  я бы сначала хотел определить, какие требования четкие, понятные, да, мы хотим с
  Джетами, с чем-то еще, как проходить … Мы не можем взять то, что есть, и запихать новую
  концепцию. Так как минимум стоит проверить.»

  HE IS RIGHT, AND THE VERIFICATION'S OWN PRESENTATION WAS AT FAULT. Two different sorts
  of fact were reported as one. What is TRUE OF THE SOLVER regardless of any concept, and
  cannot be tuned away: the per-step transfer ceiling that comes from the stability floor;
  the fact that changing the flow numerator moves the ENDPOINT and never the TIMESCALE; the
  fact that a real per-cell capacity clamps the transfer DOWN; the frozen per-cell render
  payload that can depict only one kind per cell; the absence of any liquid model; and the
  absence of any runtime way to change a face from solid to open. What was merely the OLD
  CONCEPT'S PARAMETERS, inherited from a plan built for roughly 150 large rooms and one
  huge continuous level, and never recomputed since the concept shrank twice: the 50 cm
  substance cell and 25 cm structure cell; twelve co-resident kinds per cell; the pocket
  and room sizes every timing number was computed against; the occupancy figure; and the
  step rate — for which NO constant exists in the product at all, only an editable field in
  a demo director at 0.10-0.16 s. R1 in the artifact already says this in one line («Cell
  size (50 cm) was built for the previous concept; it may be recomputed»), and the
  verification quoted its consequences without leading with it.
  RECOMPUTED at a plausible NEW scale, and this is why the row matters: at a one-metre
  substance cell, a small pocket of one to two cubic metres vents in single-digit seconds
  through an open face, and the same pocket through a narrow notch takes tens of seconds —
  so «aperture buys time, not safety» WORKS at the new scale, while the same pocket at the
  old 50 cm cell is a minutes-long creep. The seconds-scale burst is not out of reach; it
  is out of reach ONLY at the old concept's numbers. This is a derivation, not a
  measurement, and it does not discharge the envelope decision.

  SO THE ORDER OF THIS LEG IS: requirements first, and the requirements are written
  ENGINE-BLIND. His second clarification of 2026-07-27 is stronger than the first and it
  governs: «я не хочу, чтобы мы рассматривали функционал, да, как газ должен работать …
  Единственное, что мы можем рассматривать из-за технических ограничений в общем, да, то
  есть, то, чтобы это работало в кооперативе, на Unity, C#, и не требовало какой-то
  ядерный реактор.» So exactly THREE constraints may shape a requirement: it must work in
  CO-OP, it must be buildable in Unity with C#, and it must not need a nuclear reactor.
  Nothing about how the current gas simulation happens to work may enter — not the cell
  size, not the transfer ceiling, not the render payload, not the impulse primitive. Those
  facts exist and are recorded in `i-engine-numbers-belong-to-the-old-concept`; they are
  for the CHECK that comes after, and quoting them while requirements are being written is
  the exact contamination he is objecting to.
  READING NOTE, flag it to him in one line rather than guessing: one sentence of his
  dictation reads «Я хочу, чтобы мы газ рассматривали с учетом каких-то особенностей
  текущей симуляции», which contradicts the sentence before it and the sentence after it.
  Everything around it says the opposite, so it is read here as a dictation slip for «не
  хочу». If that reading is wrong, ROW 0's rule inverts and he must say so.

  HIS DECISION LADDER, recorded verbatim in substance and NOT to be pre-empted by any leg.
  He states the reason first: «мы не хотим делать посредственно игру, да, потому что у нас
  уже есть движок … я столько симуляции газа сидел, я не хочу сейчас делать посредственную
  игру из-за legacy сейчас момента.» Then the branches, his: (1) write the requirements the
  game needs to be interesting to play and to develop; (2) check the engine against them —
  fits, OK; needs fixing, OK; (3) needs replacing entirely and the existing code actively
  gets in the way → then a completely different concept is on the table, possibly a
  different game, because gas is currently held only by the time already sunk into it;
  (4) if the requirements cannot be implemented AT ALL in co-op on Unity and C# → the
  requirements get cut; (5) if they can be implemented but not with our gas simulation →
  the gas simulation comes out and we look again. Liquid he treats as a separate system and
  a separate question.

  TWO OBJECTIONS THIS LEG MUST PUT TO HIM, because both change what the ladder returns,
  and neither is this leg's to decide.
  (a) «МАКСИМАЛЬНЫЕ требования» makes the gate vacuous. A maximal set always exceeds any
  engine, so branch 2 can only ever answer «replace entirely» and the ladder stops telling
  him anything. The recommendation is the MINIMUM set without which the game is not worth
  playing or developing — which is still engine-blind, still his, and is the only version
  of the test that can come back «fits» or «needs a fix» rather than always «rebuild».
  (b) «наша симуляция газа» is not one thing, and a rebuild verdict will overshoot by
  weeks if it is treated as one. It is at least four separable layers: the per-cell
  transport rule; the determinism-and-replication contract that makes two machines agree;
  the render contract; and the structure/topology layer. The middle one is
  CONCEPT-INDEPENDENT — it is what makes co-op possible at all, it is the most expensive
  thing already gate-proven, and ANY simulation he picks instead, liquid included, needs
  the same guarantee. So branch 5 must name WHICH layer comes out. The honest symmetric
  risk belongs in the same sentence: the failure mode opposite to «a mediocre game because
  of legacy» is arriving in month three with neither a game nor an engine and October gone,
  so the CHECK gets a named budget rather than being open-ended.
  ROUTE NOTE for branch 3: «a completely different concept, possibly a different game»
  collides with CHARTER's mission, which is to finish THIS cooperative game. `map` has no
  authority over CHARTER. If that branch ever fires it is a `frame` decision, and it joins
  the frame need already booked as `i-october-route-not-a-condition` and
  `d-october-route-charter`. Name the route; do not open it.

  WHAT THIS LEG TAKES FROM HIM, at ENVELOPE level and NOT as a full design: (a) the rough
  bounds of one section — height especially, since he expects it constrained now, and width
  and length; (b) which phenomena the game needs at all, jets named by him explicitly, and
  whether a phenomenon may be placed by an author or must always follow from a player's
  action; (c) how passing is meant to work, which joins ROW 1; (d) his answer to objection
  (a) above, because it decides what the requirement set even is. THEN a separate bounded
  engineering leg answers, per requirement: satisfied today / needs a fix / needs a
  rewrite and of which layer / impossible in co-op on this stack. That leg is technical and
  is not this one — his own rule, «технические решения … в технических чатах».
  NOTE A STANDING RULE HE IS OVERRIDING FOR THIS CLASS ONLY, so no future leg reads it as
  a contradiction: `i-substance-passage-open-questions` records his rule that a question is
  discussed only once a concrete task has stopped on it, and it books size and route as
  open owner content to be answered on a real level. For the SPACE ENVELOPE and the
  admitted phenomena he now wants the opposite — defined up front, before the engine is
  taken as given. That is his call and it is recorded as his.
  KEEP THIS ROW SMALL. The danger is obvious and it has already killed a node here:
  a requirements row can expand into a full design leg. Envelope, admission, and the
  minimum-versus-maximum ruling only.

  ROW 1 — V4, and it is the one that matters most here. Criterion 5 says «Один проходим,
  второй нет». That introduces PASSABILITY as a property of the substance, and nothing
  in this direction defines it: no substance law, no requirement R1-R27, and no line of
  engine code (the search returns zero). Worse, criterion 4 says the opposite in letter
  — a pocket IS «уже открытое пространство, в котором нечем дышать», i.e. you can walk
  in, you just cannot breathe. §6-BIS supplies only an ECONOMIC reading: «one is a road,
  the other a wall», conditioned on the per-kind air-rate gap being about an order of
  magnitude. So a person who did not write the card cannot tell whether the second kind
  is a physical wall or an expensive road, and that decides the air rate table, the
  legibility target, and whether a wall exists at all. Put it to him as a fork with a
  recommendation; do not decide it.

  ROW 2 — V8, and it is an approval-record defect, not a design question. `g-5e8c` now
  carries three clauses that no owner verdict covers, written by the leg that rewrote
  g-37a1: done_when 8's closing «Инвентарь, крафт и лут сверх этого не появляются»,
  done_when 9 (latency and loss), and the removal of «второй объект» from done_when 5.
  The first RE-BANS what he had just unbanned — he said «лут экономика не запрещена» and
  «R18 надо удалить, оно невалидно», criterion 10 of g-37a1 now reads «Лут и экономика
  не запрещены и входят по общему правилу», and the re-ban lands exactly where R18's
  surviving half places the subject (upgrades between sections). `TREE.md:3` attaches
  «g-5e8c edited 2026-07-27» to an approval whose quoted verdicts can only be g-37a1's:
  the twelve-criterion text plus «да, сохраняй» on lines 1, 8, 9 and 12, while g-5e8c
  has nine criteria. The map RESULT's own play_check says «One card, one verdict, on
  exact text» while its state_changes edited two cards. This direction has already paid
  once for treating a derivable approval as a signed one. Show him the three clauses
  verbatim and get a verdict, or revert them.

  ROW 3 — the routing decision `d-post-verify-route-001`, which is in `NOW.md` with its
  two options and a recommendation. Option A opens `shape` on his live instruction, with
  the verification's coverage rows discharged as tasks (a named build he launches twice;
  the legibility target; the experiment rig) instead of as more paper. Option B finishes
  the artifact first: a bounded converge, then a narrow verification rerun, then shape.
  A needs his instruction because the kernel's readiness router wants a passing
  verification before shape and only a live owner instruction outranks the kernel. State
  the g-12fd precedent honestly — three legs, eighteen findings, zero product — and
  state honestly that Option A carries the risk in the other direction: a bet sized
  against a card two of whose criteria are still ambiguous, which is why Row 1 comes
  first in the same leg.

  ROW 4 — ADDED 2026-07-27 by writer amendment, on the owner's own notes given after the
  verification closed, in his words: «мы как бы всё говорим, что вещество, но я видел,
  что ты тестировал именно симуляцию газа … я так понимаю, что у нас, скорее всего, будет
  как минимум два — это газ и симуляция жидкости. То есть, соответственно, это тоже надо,
  чтобы было продумано». He is right, and nobody had asked. Everything ever measured in
  this direction is a GAS model. The product contains ZERO liquid or fluid model — the
  search returns no file at all — and the only flat-surface notion anywhere is a
  READ-TIME projection inside the coarse solver, which is the tier §7's own correction 1
  retired as structurally unable to express digging. What state DOES record: R2 permits
  the simulation to change «up to a different state of matter», and the concept reset
  keeps the word «вещество» precisely so the kinds are not fixed as gases — but no leg
  has ever priced a liquid, and «two kinds» has been read as two gases by every leg
  since. Two things follow, and both are his to settle: (a) does «два вида вещества» in
  criterion 5 mean two gases, or a gas and a liquid; (b) if a liquid is in, it is a
  SECOND simulation model, not a parameter of the first — and it may be the natural
  reading of criterion 5's «Один проходим, второй нет» (ROW 1), because a liquid is the
  obvious impassable kind and a flat surface is the cheapest legibility there is. Put
  ROW 1 and ROW 4 to him TOGETHER; they may have one answer. Do not decide either, and do
  not let a liquid enter the card without his exact words. Tracked as
  `i-substance-states-unpriced`.

  ROW 5 — ADDED 2026-07-27 by the same amendment. His framing of the first outcome, in
  his words: «первая цель — я хочу какую-то там сцену или игру получить, в которую смогу
  сам заходить, спокойно играть в неё, да, там урезанно всё, но хотя бы чтобы руками
  трогать». This does not change the card — criterion 1 already says it — but it is the
  standing test for every row above: a row that does not move him closer to entering and
  touching a scene is not worth his session. He also asked for the near-term work list in
  plain language («там же нужен какой-то character, чтобы ходить, что-то, чтобы там
  прорубать, и симуляция газа»). That list is `shape`'s output, not this leg's, and it is
  the strongest argument for Option A of the routing decision.

  ALSO CARRY FORWARD, not as questions: `d-air-counter-visibility-001` is still open and
  is NOT to be auto-decided or inferred; and V3's canon question belongs to `review`,
  not here — may a rule decide WHERE substance can appear while the crew is already
  digging, or must every place it can appear be fixed before the build? Note in the
  RESULT that the engine cannot express the surviving form of that today, because
  `VoxelField.NotifyConductivityChanged` throws on a face that is not already open.
boundaries: |
  Map only. Do not build, shape, create a bet, tasks, tracks or lanes, do not emit an
  executor CALL, do not mutate product or Steam state. Do not write `knowledge/`. Do not
  reopen the objective, the demoted dates, the softened air rule, the restated cargo
  ban, or two-versus-four players — he has just decided all five. Do not rewrite any
  criterion he approved unless his own words in this leg ask for it. Do not put design
  into a card. Do not read `archive/**` or the frozen canon repository. Do not answer
  the air-counter fork. No numeric release chance.
done_when: |
  1. Criterion 5's «проходим / второй нет» has a recorded owner reading — physical wall
     or expensive road — in his own words, and whatever exact card text he approves for
     it, if any.
  2. `g-5e8c`'s three unsigned clauses each carry his verdict or are reverted, and
     `owner_approved` in TREE.md records the scope of what he actually approved.
  3. `d-post-verify-route-001` is answered in his own words, and the successor CALL
     matches his answer.
  4. V3's canon question is routed to `review` with its locator; the air-counter fork is
     carried forward unanswered.
return: |
  One `map` RESULT with his verbatim words per row, the exact text of anything changed,
  and the successor CALL — `shape` under Option A, or a bounded `converge` under B.
budget: one short owner-present session
surface: a FRESH chat with the owner present — never the verification chat, never the
  map chat that wrote the card

END_OF_FILE: live/indie-game-development/work/c-map-g-37a1-verify-rows-001-call.md
