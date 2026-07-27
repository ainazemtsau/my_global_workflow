**WITHDRAWN 2026-07-26 — not failed, never dispatched.** The owner reset the
concept of `g-37a1` the same day: the carried ball and every cargo-transport
mechanic are out, and the whole game is interaction with the substance. This CALL
is written about the ball and the netcode under it, so it describes work that no
longer exists. Its successor is
`work/c-converge-g-37a1-substance-passage-001-call.md`. Kept as a receipt; do not
dispatch. Receipt of the decision:
`history/2026-07-26-s-map-substance-passage-concept-reset-001.md`.

CALL c-converge-g-37a1-core-loop-001
to: session
direction: indie-game-development
play: converge
node: g-37a1
goal: |
  The WHAT of the first outcome is locked to an owner-signed spec that `shape` can
  consume: two connected players carry one ball through the loop
  «набрал вещество → понесли шар вдвоём → сдали или не успели» in one hand-built
  room, in the real `gas_coop_game` build, and the owner plays it himself.
context: |
  AUTHORITY. `live/indie-game-development/CHARTER.md`;
  `live/indie-game-development/TREE.md` (g-37a1, and the sibling edge to g-2b7f);
  `live/indie-game-development/NOW.md`;
  `live/indie-game-development/history/2026-07-26-s-map-october-demo-order-reset-001.md`;
  `live/indie-game-development/knowledge/canon-clean-authority-reset.md`.
  Durable game Canon is NONE. `work/concept-frame-v1.md` is an owner-approved
  candidate, not admitted authority. `work/october-demo-basis-v3.md` is a SOURCE
  with zero authority — its eight-item MUST list carries the owner's «да» of
  2026-07-26 and its content now lives in the done_when of g-37a1 and g-5e8c.

  WHY THIS CALL EXISTS. On 2026-07-26 the owner replanned the roadmap
  (`Утверждаю точный TREE из семи результатов в этой редакции`). The Demo Basis
  node `g-12fd` was DROPPED: it required a readable moment and a public-claim
  ceiling to be fixed before any build could back them, and three legs produced
  eighteen independent findings and zero product evidence. His order is
  «нам нужно как можно быстрее к реализации». `g-37a1` is the new first outcome.
  Readiness route per KERNEL §2: no passing `converge-verify` RESULT exists and no
  `triage: ... converge OFF` is recorded, so the node goes to `converge`.

  THE LOAD-BEARING UNKNOWN, which is why this converge is not ceremony.
  `i-coop-carry-netcode`: two players carrying one physics object together over the
  network is unsolved in the chosen stack. FishNet allows exactly ONE owner per
  object and only the server may change ownership
  (https://fish-networking.gitbook.io/docs/guides/features/ownership); Unity's own
  netcode carries an OPEN feature issue literally titled «two players carrying a
  large object together» with no recommended solution
  (https://github.com/Unity-Technologies/com.unity.netcode.gameobjects/issues/2558);
  Unity PhysX is not deterministic across CPU vendors. The owner's single recorded
  support for why two players are needed rests on exactly this mechanic:
  «Большой шар несут вдвоём, они координируются — это уже двое.» A wrong stub here
  is fatal, so the node is expected to type `heavy` at triage step 1 — decide that
  in the leg, do not assume it.

  RECORDED OWNER DECISIONS THAT ENTER BORN-CLOSED and are not reopened here: the
  eight-item MUST list under his «да»; procedural generation is mandatory but lives
  in `g-5e8c`, not here; technique stays out of content documents; the two hall
  mechanics stay deferred; terminology is «вещество»; the provisional first-slice
  decisions (набор through E with a visible capacity, вещество подбрасывает или
  прижимает, no damage and no death, no procedural animation) are explicitly
  NOT-LAW and open work rather than constrain it.

  OWNER CONTENT RECORDED 2026-07-26 AND STILL UNDECIDED — input for this leg's
  owner questions, never to be answered by an agent: he REJECTED the «протискивают»
  dependency for the readable moment («протискивание ... как будто за собой оно
  несет еще несколько механик») and offered his own candidate instead — impact above
  a threshold produces cracks that leak («возможно даже сделать, что в нем могут
  появляться типа трещинки, да, из которых вытекает»), by analogy to carried loot
  taking damage on impact, with «прям типа взять как из репа» named as an
  undesirable last resort; on growth «чем больше, тем ... кратно больше он вмещает
  в себя ... закон куба условно. Но тем тяжелее нести», with «возможно не сейчас мы
  этот закон должны прорабатывать». Session length, the meaning of «не успели» and
  the level of art belong to `g-5e8c` and `g-2b7f`, not to this node.

  THE SIBLING EDGE THAT COSTS MONEY IF MISSED. `g-2b7f` needs five honest gameplay
  screenshots FROM THIS BUILD by 2026-08-10, because Steam requires five
  gameplay-only screenshots for a store page and the page must be PUBLIC by
  2026-08-31 or the October festival route closes. That is a cross-node edge and
  belongs in §WHAT coverage; it is not permission to do art work in this node.
boundaries: |
  Converge only. Do not build, do not shape, do not create a bet, tasks, tracks or
  execution lanes, do not emit an executor CALL (converge step 4 forbids it), do not
  mutate product or Steam state, do not create or change a repository.
  Do not reverse the recorded owner decisions listed above.
  Do not decide owner content: the ball's readable-moment rule, the cube law, what
  the substance does to the player as Basis law, session length, the meaning of
  «не успели», the art level. Surface each as a signed owner question or route it
  to the node that owns it.
  Do not reopen `g-12fd` or author a replacement specification document.
  Do not read `archive/**` or the frozen canon repository
  `C:\projects\gas_coop_game_canon`; no legacy read is authorized.
  Do not publish a numeric release chance.
  Do not move the 2026-08-07 boundary.
done_when: |
  1. `work/converge-g-37a1.md` exists with a recorded
     `triage: <type> — converge <ON|OFF> — because <...>` header and the list of
     imported owner-approved decision ids.
  2. §GLOSSARY signs every term read two or more ways — at minimum «вещество»,
     «шар», «петля», «совместная переноска», «сборка», «комната» — with its
     load-bearing properties and competing readings.
  3. §WHAT is a flat cited list derived from all three sources: every g-37a1
     done_when criterion; every cross-node edge the boundaries name (the g-2b7f
     screenshot edge; the g-5e8c generation edge); and every committed mechanism
     decomposed into the parameters it forces. The carry mechanism is decomposed at
     minimum into: authority model for the carried object, what each carrier's input
     does, behaviour under artificial latency and packet loss, behaviour on release
     and on disconnect mid-carry, and what «не проведёт через проём» means physically.
  4. Forward-clean and backward-clean per the play's done-when; `§SIGNOFF` recorded
     for Define and Resolve with the owner's exact words.
  5. Owner forks are batched and none is silently auto-decided.
  6. `next` routes to `converge-arch` if the node types heavy, otherwise to
     `converge-verify`. Shape runs only after verification passes.
return: |
  One `converge` RESULT with the triage line, the signed glossary and §WHAT,
  `converge_coverage`, the owner's verbatim signoffs, and the routing handoff.
budget: one owner-present session
surface: any session with the owner present; a fresh chat

END_OF_FILE: live/indie-game-development/work/c-converge-g-37a1-core-loop-001-call.md
