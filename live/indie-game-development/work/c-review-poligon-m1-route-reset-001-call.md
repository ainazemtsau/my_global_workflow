# CALL c-review-poligon-m1-route-reset-001

to: session
direction: indie-game-development
play: review
node: g-9c41
task: Poligon-M1-bet-review
issued: 2026-07-14 (s-work-poligon-m1-integration-route-001)
parent: s-work-poligon-m1-integration-route-001

goal: |
  Текущая ставка g-9c41 имеет честный проверенный verdict и owner-approved следующую ставку, которая сохраняет
  принятый маршрут сильной сцены M1 без числового потолка product legs и использует 24.07 только как контрольный review.

context: |
  В `work/poligon-m1-integration-route.md` владелец принял единый маршрут шести трасс, finish line, cuts,
  dependency/parallelism map и прозрачный текущий ledger: 34 обязательных логических product legs плюс условные.
  Это accounting, не новый cap. Actual owner words этой сессии: «Да, именно так» — про отсутствие числового
  ограничения и 24.07 как review, не stop; затем «Маршрут принимаю».

  Живой `NOW.md` всё ещё хранит старую активную ставку с appetite «максимум 13» и kill_by «24.07 либо 13».
  Work-play не имеет права молча продлить или переписать её: по G3 текущая ставка должна быть закрыта через fresh
  review, а продолжение оформлено следующей ставкой. Принятый маршрут является cross-bet direction route и не
  доказывает, что текущая ставка выполнена.

  Product truth отдельно: NearGas L1 = CHECKPOINT / NOT DELIVERED; единственный текущий product call разрешает
  только PLAN-AMEND/Re-sync v20→v21 и затем требует fresh Direction binding review. Ни один BUILD не разрешён.

boundaries: |
  Direction review; product, TREE, CHARTER и canon read-only. Не продлевать старую ставку, не объявлять её met только
  из-за принятого маршрута и не выпускать executor/BUILD CALL. Сохранить принятый M1 finish, cuts и no-cap instruction.
  Сохранить точную NearGas planning truth и все независимые open calls. Любая новая ставка требует actual owner words.

done_when: |
  1. По каждому done_when текущей ставки есть met/partial/missed с проверяемым evidence и честный verdict всей ставки.
  2. Forecast показывает оставшийся объём, текущие blockers и что принятый 34+ ledger не является выполненной работой.
  3. Все lens verdicts и reusable learning собраны без переписывания product/canon.
  4. Старые «13 / стоп 24.07» получают G3-совместимую диспозицию: текущая ставка закрывается, не продлевается.
  5. Владелец получает 2–3 варианта следующей ставки и рекомендацию; выбранная ставка сохраняет no-cap route,
     24.07 как контрольный review и текущий NearGas planning gate.
  6. Только actual owner choice открывает следующую ставку/задачи. До этих слов open_call остаётся pending checkpoint.
  7. RESULT прямо подтверждает отсутствие product mutation, executor CALL и BUILD.

return: |
  RESULT с verdict/evidence по текущей ставке, forecast, lens harvest, G3 disposition, вариантами следующей ставки,
  рекомендацией и actual owner words. Если owner choice не получен, вернуть checkpoint и оставить этот CALL открытым.

budget: one fresh owner-present review session; checkpoint rather than invented choice
surface: any

END_OF_FILE: live/indie-game-development/work/c-review-poligon-m1-route-reset-001-call.md
