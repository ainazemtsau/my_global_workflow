CALL c-map-g-37a1-core-requirements-001
to: session
direction: indie-game-development
play: map
node: g-37a1 (with a two-minute correction to g-5e8c)
goal: |
  The MINIMAL CORE stated as a requirement set the owner approves on exact text: which
  mechanics must work for this to be a game he wants to play and to keep developing —
  written WITHOUT any reference to the engine, and small enough to build, with room to
  grow rather than to be rebuilt.
context: |
  WHY THIS REPLACES THE PREVIOUS CALL. `c-map-g-37a1-verify-rows-001` was authored as
  five narrow rows off the failed verification, and it was amended three times in one
  evening as the owner's instruction got clearer. It is the wrong shape and is superseded
  unspent. His own words for the state it left him in: «сейчас у меня как бы каша в
  голове, то есть я немножко не понимаю, куда мы, что идем … я хочу привести всё в
  порядок». And his correction to that CALL's own entry point: «габариты участка я не
  представляю, как это обсуждать в отрыве от концепта … Сейчас нужно минимальное core,
  игра, да, там без оформления, без ничего, но чтобы все механики, которые являются
  ядром, работали. Это не значит, что нам нужно только габариты определить.» So the entry
  point is the MECHANICS, and the dimensions follow from them or stay open.

  AUTHORITY, in this order. `live/indie-game-development/TREE.md` (g-37a1 and g-5e8c),
  `live/indie-game-development/NOW.md`, `live/indie-game-development/CHARTER.md`, and
  `history/2026-07-27-s-converge-verify-g-37a1-digging-card-001.md` — the verification
  that failed and produced the evidence for why the requirement set is re-authored rather
  than patched. `work/converge-g-37a1.md` is design MATERIAL only: read §6-BIS and §4 for
  what the owner has already ruled, and treat everything engineering in it as OUT OF
  SCOPE for this leg (see the four hard rules below).

  THE FOUR HARD RULES OF THIS LEG, all from the owner on 2026-07-27.

  1. ENGINE-BLIND. «я не хочу, чтобы мы рассматривали функционал, да, как газ должен
     работать … Единственное, что мы можем рассматривать из-за технических ограничений в
     общем — чтобы это работало в кооперативе, на Unity, C#, и не требовало какой-то
     ядерный реактор.» Exactly THREE constraints may shape a requirement: co-op, Unity
     with C#, no nuclear reactor. No cell size, no transfer rate, no render format, no
     existing primitive, no measured number may enter this session. If a mechanic the
     game needs does not exist in the current simulation, that is a fact for the CHECK
     that comes after, not a reason to drop the mechanic: «если нам нужен какой-то прям
     хорошо видный жест, если его можно реализовать, но в нашей симуляции этого нет, то
     мы должны это реализовывать.»
  2. MINIMUM WITH HEADROOM, not maximum. He accepted the objection in full — «реально у
     меня не та формулировка» — and restated it himself: «вначале минимальный набор, с
     возможностью расширения … Но минимальный набор должен учитывать, чтобы это уже было
     интересно играть.» So each candidate mechanic faces two tests, both his: **if this
     does not work, is it still the game I want to play?** and **does this extend later
     rather than get rebuilt later?**
  3. NOTHING ALREADY SAID IS A REQUIREMENT UNTIL HE SAYS IT AGAIN HERE. «когда я говорил
     про джеты, про все какие-то текущие механики … это просто я как пример приводил. Не
     обязательно должны быть. То есть то, что я сказал, это не обязательно требования.»
     Jets, the growing seep, the graded ground mark, the air hand-off, two substance
     kinds, rotation, the blind digger — all of it enters this session as CANDIDATES with
     no standing. Do not carry any of them in as settled, and do not argue from «it is
     already recorded».
  4. NO TECHNICAL DISCUSSION. «я не шибко хочу техническую часть сейчас обсуждать. У меня
     сейчас в голове стоит главная цель — сформировать требования, стратегию, план, чтобы
     запустить разработку. И уже во время разработки обсуждать технические детали.» If a
     technical question is genuinely load-bearing for a requirement, name it in one line
     and route it to the check; do not answer it here.

  WHAT SURVIVES FROM THE APPROVED CARD, and is therefore not reopened unless he reopens
  it: the concept frame itself — a crew that cuts its own path through solid ground into
  pockets of a substance and pays in air — the objective as TRAVERSAL by digging with
  relocation refused, the cargo ban restated as the complex physical carry mechanic, no
  date being a condition, and co-op following the first playable core immediately. The
  requirement SET inside the card is what is being re-authored, not the concept.

  WHAT THE VERIFICATION LEFT AS EVIDENCE FOR THIS LEG, in plain terms and with no
  engineering detail: the card's twelve criteria contain about forty-five decidable
  clauses and roughly fifteen that are rules, permissions or predictions rather than
  outcomes; four whole classes of decision were never raised anywhere, and all four sit
  between the simulation and the man who plays it — the body, how the game is launched at
  all, how conditions are changed and compared, and what happens on death and restart;
  and two clauses cannot be read by an outsider at all. Those gaps are the agenda of this
  leg, translated into his language, not quoted as findings.

  THE TWO QUESTIONS THAT MUST BE ASKED AS CORE-MECHANIC QUESTIONS, because they were
  found unreadable and they are mechanics, not wording. (a) «Один проходим, второй нет» —
  is the second kind a physical wall you cannot enter, or an expensive road you can enter
  and pay for? The card says both in different places. (b) Are the two kinds two gases, or
  a gas and a LIQUID? He raised the second himself: «у нас, скорее всего, будет как
  минимум два — это газ и симуляция жидкости», and he treats liquid as a separate system
  and a separate question. Both are his, both are core, and (b) may answer (a).

  RIDING ALONG, two minutes at the end and unrelated to the core set: `g-5e8c` carries
  three clauses no owner verdict covers, one of which re-bans the inventory, crafting and
  loot he had just unbanned. Show him the three lines verbatim; he either signs them or
  they revert. Tracked as `i-g5e8c-unsigned-clauses`.
boundaries: |
  Map only. Do not build, shape, create a bet, tasks, tracks or lanes, do not emit an
  executor CALL, do not touch product or Steam state. Do not write `knowledge/`.
  Do not bring a single engine fact, measured number or existing mechanic into the
  requirement discussion — that is rule 1 and it is the whole point of the leg.
  Do not start from dimensions: they follow from the mechanics or stay open.
  Do not design a mechanic's insides — one line each, what must work, not how.
  Do not decide the gas/liquid question, the passability question, or anything else that
  is owner content; put each as a fork with options and a recommendation and stop.
  Do not reopen the concept frame, the objective, the dates or the cargo ban.
  Do not run the ladder of `i-engine-fit-decision-ladder` — this leg only produces its
  INPUT. Do not read `archive/**` or the frozen canon repository. No numeric release
  chance. Do not answer `d-air-counter-visibility-001`.
done_when: |
  1. A CORE SET exists in his own approved words: each mechanic one line, each passing
     both of his tests (without it, not the game; and it extends rather than gets
     rebuilt), ordered by how badly the game needs it.
  2. An explicit NOT-CORE list sits beside it: what was considered and deliberately left
     out of the first core, including the candidates that entered only as examples.
  3. The two core questions — passability, and gas-versus-liquid — are answered in his
     words, or recorded as an open fork with a recommendation if he wants them settled on
     a real level instead.
  4. Whatever of this belongs in the card is written into `g-37a1` with his verdict on the
     exact text, and `owner_approved` records the scope of what he actually approved.
     What does not belong in a card stays in the leg's artifact.
  5. `g-5e8c`'s three unsigned clauses are signed or reverted.
  6. The successor is issued: a fresh session that ATTACKS the core set, then the bounded
     technical check that feeds his ladder.
return: |
  One `map` RESULT with the core set in his verbatim words, the not-core list, the two
  answers or forks, the exact card text, and the successor CALL.
budget: one owner-present session, and it is allowed to be the longest of the week — this
  is the leg that decides what gets built
surface: a FRESH chat with the owner present

after: |
  1. A fresh session attacks the core set: is anything missing without which it is not a
     game, is anything in it that is not core, and can an outsider read every line.
  2. A bounded technical leg — in the product repo, with a named budget — answers per
     requirement: satisfied today, needs a fix, needs a rewrite of which layer, or
     impossible in co-op on Unity and C#. That is the input to `i-engine-fit-decision-ladder`.
  3. His ladder verdict, then `shape`, then development.

disposition: |
  DISCHARGED 2026-07-28 by `s-map-g-37a1-core-requirements-001`, owner present.
  Receipt: `history/2026-07-28-s-map-g-37a1-core-requirements-001.md`.
  Artifact: `work/core-requirements-g-37a1.md`.

  All six done_when are met. (1) The core set exists as seventeen lines in his words, ordered by
  priority. (2) The NOT-core list sits beside it, including the candidates that entered only as
  examples and one cut candidate that was considered and withdrawn on his own test. (3) Both core
  questions are answered in his words — passability is DELETED (any pocket may be entered, the
  kinds differ only by the price in air, an emptied pocket costs nothing) and the gas-versus-liquid
  fork is option C with his addition that liquid may later come in as a REPLACEMENT. (4) The card
  `g-37a1` grew from twelve criteria to fifteen under his verdict on exact text; what does not
  belong in a card stayed in the artifact. (5) `g-5e8c`'s three unsigned clauses are discharged —
  line 8 amended and signed, line 9 kept and signed, the `второй объект` removal confirmed. (6) Two
  successors are issued.

  ONE HARD RULE WAS WAIVED BY THE OWNER, and it is recorded as his: step 2's anti-anchoring
  requirement that he speak first. Asked for his own candidates, he declined to invent from a blank
  page and instructed the leg to analyse the accumulated record instead — «тебе нужно сейчас
  проанализировать то, что работа уже была сделана … я хочу в пределах этого контекста рассуждать».
  The play's explicit waiver branch was taken.

  THE OTHER FOUR RULES HELD. Engine-blind: no cell size, transfer rate, render format, existing
  primitive or measured number entered the discussion; the single technical sentence spoken was the
  one rule 4 permits, naming line 9 as the most expensive row and routing its price to the check.
  Minimum with headroom: every line passed both of his tests. Nothing already said counted as a
  requirement until he said it again. No technical discussion.

  SUCCESSORS: `c-converge-g-37a1-core-rows-001` (step 2) and, in PARALLEL on his standing
  instruction, `c-research-g-37a1-engine-fit-check-001` (step 4, read-only).

END_OF_FILE: live/indie-game-development/work/c-map-g-37a1-core-requirements-001-call.md
