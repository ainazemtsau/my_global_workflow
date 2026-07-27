# RESULT s-map-g37a1-card-clarification-001

direction: indie-game-development
play: map (roadmap-node fast path — two done_when lines of one approved card)
node: g-37a1
call: none — opened from the owner's plain message per KERNEL §2 after the repair
  leg surfaced the contradiction and he asked for it to be fixed
date: 2026-07-27

## outcome

The one defect the repair leg deliberately refused to touch is now fixed with the
owner's verdict on the exact text. `g-37a1` done_when 2 and done_when 9 no longer
contradict each other.

The law did not change. Only its readable form did: the same rule now cannot be
read as banning the player from touching a door.

## evidence

THE CONTRADICTION, as an independent audit found it and this leg verified it.

- done_when 2 read: «Единственное взаимодействие игрока — с веществом: обнаружить
  его, пройти сквозь него, переместить его.» — which, read literally, forbade the
  player from touching anything that is not substance.
- done_when 9 read: «…и взаимодействие вещества с предметами.» — which, read
  literally, cut every door, hatch, vent, container and tool.
- Together they demanded that the player move the substance while removing every
  plausible means of moving it, and done_when 2 named no verb.

THE RECORDED INTENT the fix restores, from the owner on 2026-07-27: «мы всё
смотрели на то, чтобы газ мог взаимодействовать с другим лутом. То есть, я так
понимаю, тут это не надо будет. Ну, на игрока может взаимодействовать, на лут уже
не надо.» The scope cut he took was substance-to-LOOT, not substance-to-level.

OWNER VERDICT, on the exact replacement text shown before it was written: `да`.

APPROVED TEXT, before and after.

- done_when 2 — before: «Единственное взаимодействие игрока — с веществом:
  обнаружить его, пройти сквозь него, переместить его. Ни одной механики переноса
  грузов.»
- done_when 2 — after: «Всё, что делает игрок, направлено на вещество: обнаружить
  его, пройти сквозь него, переместить его. Устройства уровня и снаряжение
  существуют только как средство для этого, а не как отдельный слой игры. Ни одной
  механики переноса грузов.»
- done_when 9 — before: «…сюжет и взаимодействие вещества с предметами.»
- done_when 9 — after: «…сюжет, и физическое взаимодействие вещества со свободными
  предметами и лутом — это вырезано из симуляции. Вырез не распространяется на
  устройства уровня и на то, чем игрок перемещает вещество.»

WHY THE NEW WORDING IS STRICTLY BETTER, not merely looser. The old done_when 2
protected the law by banning everything; the new one protects it by naming the
failure it actually fears — level fixtures and equipment becoming their own layer
of the game, which is how an inventory, a crafting tree and a gear economy creep
in. That risk is now named and forbidden, and it was not before.

WHAT STAYS OPEN, and it is the important half: **by what means the player moves
the substance.** No verb is named anywhere in the card, deliberately. That is the
converge's, decided on real geometry rather than on paper, and it is recorded in
`i-substance-passage-open-questions`.

THE ~150-ROOM FIGURE, corrected by the owner in the same message and recorded so
no session takes it as a goal: «150 комнат — это как бы условное число, да, мы за
него не идём». It is an order of magnitude carried over from superseded plans, not
a target; the real number is whatever the first section needs, and done_when 7
already requires it to be fixed before the build and to not grow.

## state_changes

`live/indie-game-development/TREE.md`
- Replace `g-37a1` done_when 2 and done_when 9 with the exact owner-approved text
  above. No other line of that card, and no other card, is touched.
- Append the clarification and its `да` to `owner_approved`.

`live/indie-game-development/NOW.md`
- `updated: 2026-07-27 by s-map-g37a1-card-clarification-001`.
- `i-substance-passage-open-questions`: mark item 8 RESOLVED, record what the
  resolution was and that the verb itself remains open; restate the ~150-room
  figure as an order of magnitude and explicitly not a target, citing his words.
- Everything else preserved: `bet: null`, `tasks: []`, no lanes, forecast
  `no_basis`, every issue, the single open CALL unchanged.

`live/indie-game-development/LOG.md`
- Prepend this leg's line once.

`live/indie-game-development/history/`
- Save this RESULT as `2026-07-27-s-map-g37a1-card-clarification-001.md`.

## captures

- The failure the new done_when 2 names — level fixtures and equipment growing
  into their own layer of the game — is the cheapest scope creep to fall into and
  is now forbidden by the card rather than by good intentions.

## decisions_needed

[]

## play_check

- Roadmap-node fast path: two lines of one card under an approved parent.
  Skeleton, search and lens sweep skipped with reason — the tree's shape, order
  and lens coverage are unchanged, and this leg only removes an internal
  contradiction from a card the owner had already approved.
- 4 Cards: done — the exact replacement text for both lines was shown with its
  before-and-after and the reason for each change.
- 5 Per-node verdict (owner): done — `да` on that exact text.
- 9 Close (owner): done — TREE and LOG saved; the open CALL is untouched, so the
  handoff the owner already holds stays valid; no bet, task, track or lane
  created.
- Note: the CALL for the converge did not change and did not need to. The
  clarification narrows what the converge must decide — the verb — rather than
  changing its scope.

## log

g-37a1/card-clarification: the owner approved with «да» the exact replacement text for the two done_when lines that contradicted each other — done_when 2 required moving the substance while done_when 9 excluded «взаимодействие вещества с предметами», which read literally cut every door, tool and container; done_when 2 now reads that everything the player does is aimed at the substance and that level fixtures and equipment exist only as a means and never as their own layer of the game, and done_when 9 now excludes physical interaction of the substance with LOOSE OBJECTS AND LOOT specifically, with the exclusion explicitly not reaching level fixtures or whatever the player moves the substance with; the law is unchanged and only its readable form moved, the verb itself — by what means the substance is moved — stays open for the converge on real geometry; open question 8 is recorded as resolved with what remains of it named; the ~150-room figure is re-stated as an order of magnitude from superseded plans and explicitly NOT a target on his words «мы за него не идём»; no other card, no date and no other line touched.

## next

Unchanged: `c-converge-g-37a1-substance-passage-001` remains the single open CALL,
its text untouched, to run in a fresh chat with the owner present. Its first
business is still the grid and the size envelope, then at-a-glance legibility, and
now also the verb by which the substance is moved.

END_OF_FILE: live/indie-game-development/history/2026-07-27-s-map-g37a1-card-clarification-001.md
