RESULT s-frame-indie-october-route-revision-001 (call: owner-direct-save)
direction: indie-game-development   play: frame   node/task: g-0c26/framing

outcome: |
  Октябрьский Steam Next Fest остаётся ближайшим жёстким и основным маршрутом,
  но его пропуск больше не является условием закрытия игры или всего направления.
  После playable Core и не позднее 2026-08-15 достижимость октября пересматривается
  по фактической скорости; закрытие маршрута запускает явный выбор новой даты и
  способа публичного выпуска демо без автоматического ожидания февраля.

  Единственное оставшееся продуктовое решение по Core также закрыто: собственный
  остаток воздуха постоянно читается простым HUD-индикатором в углу. Текущие Core-
  задачи, lanes, WIP и все пять open_calls сохранены.

evidence: |
  - Владелец о воздухе: `Просто индикатор в углу`; красивый или диегетический
    вариант сейчас не нужен.
  - Владелец об октябре: попасть на Steam Next Fest очень желательно и жёсткий
    дедлайн полезен, но пропуск фестиваля не закрывает игру; после Core сроки
    пересматриваются, демо можно выпустить отдельно и ждать февраля не обязательно.
  - Exact owner verdict / G9 after the full CHARTER replacements, exact TREE root
    and NOW delta were shown: `Утверждаю эту точную редакцию`.
  - Current state bases: `live/indie-game-development/CHARTER.md`, `TREE.md`,
    `NOW.md`; prior owner words in
    `history/2026-07-27-s-map-g-37a1-digging-concept-001.md`.
  - Valve dates remain external facts rather than Core done_when:
    https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/2026october

state_changes: |
  Apply atomically against fresh current state by stable path/id and preserve every
  concurrent change outside this exact owner-approved frame intent.

  1. In `live/indie-game-development/CHARTER.md`:
     - replace success criterion 1 with the exact approved
       `Октябрьский Steam Next Fest — основной маршрут` text: the existing
       2026-08-31, 2026-10-05 and 19–26 October gates remain; missing October does
       not close the game or direction; after playable Core and no later than
       2026-08-15 the owner reviews feasibility; a closed/missed route triggers an
       explicit new public-demo date/method, with no automatic February wait or
       automatic game close;
     - replace the October hard-constraint line with the exact approved statement
       that October is the hard primary route but not a condition of continuation;
     - replace the guarded risk-posture paragraph with the approved conditional
       rule: cut scope first while the route stands; explicitly re-date after it
       closes; never drift silently;
     - replace pre-mortem item 1 with the exact approved failure class
       `Октябрьский маршрут был потерян, а следующий не выбран`, its mitigation
       and three boundaries;
     - preserve every other section and the EOF trailer unchanged.
  2. In `live/indie-game-development/TREE.md`, mutate root `g-0c26` only:
     - set the exact approved goal: paid Steam release plus a worthy public demo,
       with October pursued as primary or explicitly replaced by another public
       route, and the factual reusable solo-release path recorded;
     - replace done_when 1, 2 and 5 with the exact approved route-flexible text;
       preserve done_when 3, 4 and 6;
     - replace `why` with the exact approved statement that October is a hard
       forcing function but not a condition of the game's existence;
     - point root detail and owner_approved lineage at this receipt; preserve
       root status and every child byte-for-byte; maintain the EOF trailer.
  3. In `live/indie-game-development/NOW.md`:
     - set `updated` to this leg;
     - append the exact approved corner-HUD requirement to task `t-8.done_when`;
     - update `i-substance-passage-open-questions` to record that visibility is
       settled in t-8 and add this receipt to its evidence;
     - remove answered decision `d-air-counter-visibility-001` and leave
       `decisions: []`;
     - remove resolved issue `i-october-route-not-a-condition`, disposition:
       CHARTER and root now carry the exact owner-approved posture;
     - update `i-demo-scope-cap` and the no-basis forecast driver/update trigger
       to the exact approved October review rule;
     - preserve the active bet, every other task/issue, all five tracks, WIP=5,
       all five open_calls, recurring state and EOF trailer.
  4. Add this full RESULT once at
     `live/indie-game-development/history/2026-07-29-s-frame-indie-october-route-revision-001.md`
     and prepend the exact log line below once to `LOG.md`.

captures: []

decisions_needed: []

play_check:
  - "1 Interview (owner): done — narrow revision used the owner's actual words: `Просто индикатор в углу`; October is strongly desired and its hard deadline is useful, but missing it does not close the game; Core is built first and dates are reviewed from product evidence."
  - "2 Homework (outside view): skipped — this revision creates no new ambition, lens, quality bar, repo, owner edge or success number; current official Valve dates were already checked in-session and remain unchanged."
  - "3 Charter draft (owner): done — every replacement block was shown verbatim; exact verdict `Утверждаю эту точную редакцию`; owner_approved."
  - "4 Pre-mortem (owner): done — the exact replacement failure, mitigation and boundaries were shown verbatim and covered by `Утверждаю эту точную редакцию`; owner_approved."
  - "5 Root node (owner): done — only root g-0c26 goal/done_when/why changes; exact root was shown verbatim and approved; all children remain current October-route cards."
  - "6 Close (owner): done — exact save words were `сохраняй`, followed by exact-artifact approval `Утверждаю эту точную редакцию`; no map-evidence CALL is issued because this is a revision with no new candidate outcome or child edit, and the current October roadmap remains the primary route."

log: 2026-07-29 | s-frame-indie-october-route-revision-001 | frame | direction | g-0c26: октябрь остаётся жёстким основным маршрутом, но его пропуск больше не закрывает игру и запускает явный пересмотр дат; воздух читается простым HUD-индикатором в углу -> history/2026-07-29-s-frame-indie-october-route-revision-001.md

next: |
  return-to-owner

END_OF_FILE: live/indie-game-development/history/2026-07-29-s-frame-indie-october-route-revision-001.md
