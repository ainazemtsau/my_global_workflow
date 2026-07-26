# RESULT — s-repair-m1-acceptance-criteria-001 (2026-07-14)

## Owner summary

Владелец дословно ратифицировал все пять дополнений к приёмке Полигона М1. Живая цель теперь
требует замера на названном слабом железе, HUD-доказательства agree/divergence и видимого admission ceiling.
Для М1 потеря пира/хоста явно завершает текущий прогон; late join, host migration и production-звук остались вырезаны.
Исходное решение снято из inbox; открыт только узкий выбор конкретного binding min-spec железа.

~~~yaml
RESULT s-repair-m1-acceptance-criteria-001 (call: plain-owner-message/d-m1-acceptance-criteria-001)
direction: indie-game-development
play: repair
node/task: g-9c41 / d-m1-acceptance-criteria-001
outcome: |
  Все пять потерянных дополнений ратифицированы и возвращены в живую планку Полигона М1:
  финальный прогон идёт на названном слабом железе; HUD показывает deterministic agree/divergence и
  ловит planted divergence; admission ceiling виден в стенде; потеря пира/хоста явно и контролируемо
  завершает текущий прогон без host migration; production-звук сознательно остаётся за границей М1.
  Открыт один узкий owner-выбор: назвать конкретное binding min-spec железо с явным CPU.
evidence: |
  Owner verdict дословно: «ратифицировать все пять с этими уточнениями».
  Источник расхождения: work/board/dashboard.html карточка d-m1-acceptance-criteria-001 и
  history/2026-07-11-s-repair-board-m1-ladder-purge-001.md — пять пунктов пережили только в удалённой legacy-лестнице.
  Действующие опоры: work/poligon-m1-shape-2026-07-10.md уже требует две машины/слабое железо и режет
  host migration/audio; work/c-lab-p0-001-call.md уже определяет HUD-лампу с plant-divergence; knowledge/g9c41-gas-engine-SPEC.md
  содержит принятый admission ceiling; TREE.md называет только GPU 60-class + 16 GB RAM, поэтому CPU/min-spec выбор не выдуман.
  Product code, TREE.md, CHARTER.md, tasks, open_calls и NOW.next не менялись.
state_changes: |
  live/indie-game-development/NOW.md:
    - updated -> 2026-07-14 by s-repair-m1-acceptance-criteria-001.
    - bet.goal дополнен точными финальными доказательствами: названное слабое железо, HUD deterministic agree/divergence,
      видимый admission ceiling.
    - bet.cut_list явно оставляет production-звук за границей М1 и фиксирует минимальную disconnect-политику:
      потеря пира/хоста явно и контролируемо завершает текущий прогон; late join/host migration остаются вырезаны.
    - decisions remove d-m1-acceptance-criteria-001 as answered; add d-m1-min-spec-hardware-001 with three options
      and recommendation = available physical machine with explicit CPU/GPU/RAM.
    - tasks, open_calls, recurring and next preserve fresh current values unchanged.
  live/indie-game-development/work/board/dashboard.html:
    - regenerate M1 finish/evidence wording; replace the answered five-criteria card with the narrow min-spec hardware card;
      add the ratified outcome to recently closed and the 2026-07-14 journal.
  live/indie-game-development/LOG.md:
    - append the s-repair-m1-acceptance-criteria-001 line once.
  writer:
    - save this full RESULT to history/2026-07-14-s-repair-m1-acceptance-criteria-001.md and commit atomically.
captures: []
decisions_needed:
  - q: "Какое конкретное слабое железо становится binding min-spec финального прогона М1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; газ CPU-bound, поэтому CPU называется явно."
play_check:
  - "1 Name the contradiction: done — пять дополнений жили только в удалённой legacy-лестнице, а NOW не держал полную финальную планку."
  - "2 Reconstruct: done — сверены NOW/TREE, shape artifact, board-purge history, lab CALL, gas SPEC и 8-player knowledge; legacy-текст не использован как authority."
  - "3 Propose corrected state: done — предъявлены последствия каждого пункта; дифф ограничен NOW.goal/cut_list/decisions и render-панелью, без TREE/CHARTER/product изменений."
  - "4 Confirm (owner): done — фактические слова владельца: «ратифицировать все пять с этими уточнениями»."
  - "5 Friction: skipped — это одноразовая потеря пунктов при вырезании legacy-лестницы; повторяющийся OS-дефект не доказан."
log: |
  2026-07-14 — repair (g-9c41/d-m1-acceptance-criteria-001, s-repair-m1-acceptance-criteria-001): владелец «ратифицировать все пять с этими уточнениями» — в живую планку М1 вернуты названное слабое железо, HUD-детерминизм, видимый admission ceiling, controlled disconnect-stop и явный audio-cut; остался узкий выбор binding min-spec железа. → history/2026-07-14-s-repair-m1-acceptance-criteria-001.md
next: |
  CALL: work/c-exec-near-gas-core-authority-001-plan-amend-resync-002-call.md
~~~

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-repair-m1-acceptance-criteria-001.md
