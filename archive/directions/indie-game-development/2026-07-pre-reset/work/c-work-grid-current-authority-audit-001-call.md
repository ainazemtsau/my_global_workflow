# CALL c-work-grid-current-authority-audit-001

to: session
direction: indie-game-development
track: grid
play: work
node: g-4b92
task: current-authority-audit
issued: 2026-07-20 (s-map-grid-track-resume-001)

goal: |
  Владелец получает проверенную по текущему продукту картину Grid / Layers / World Change и точный
  фронт решений, из которого без скрытых допущений можно собрать детальный план реализации для
  постоянной Integration Lab.

context: |
  Direction authority: `live/indie-game-development/NOW.md`, `TREE.md`, `CHARTER.md`,
  `work/program-v2-integration-lab-plan.md`, `knowledge/g9c41-gas-engine-SPEC.md` и текущие релевантные
  SPEC/ADR/PLAN/LOG/history.

  Главный planning input: `work/grid-object-layer-interaction-resolver-brief.md`. Это автономный вход
  для анализа, а не принятая архитектура и не BUILD authority. Его сильная постановка требует
  одинаково корректно замечать оба источника изменения: объект переместился в стабильный слой или
  сам слой дошёл до неподвижного объекта. Отдельный центральный Resolver остаётся гипотезой до
  сравнения с альтернативами.

  Владелец принял подготовительный маршрут словами «Принимаю активацию Grid по этому маршруту».
  Его приоритет: Grid должен завершиться раньше зависимых продуктовых треков; внутри Grid качество
  важнее скорости, а параллельность допустима только для действительно независимых работ после
  фиксации общих контрактов. Последовательный порядок обязателен, если он надёжнее.

  Из текущей Direction authority уже известны две разные линии долга, которые нельзя смешивать:
  Object ↔ Layer interaction, найденный из Gas-трека, и сохранённый aperture RED
  `5af1d8db931d10cc6149a2c1f8e1023bc3b9ffb1`, которому нужна свежая V31-совместимость и отдельный
  disposition. Предыдущий product snapshot `main@45b15623` — только evidence base, не freshness lock.
  Если готовый Program cleanup изменит продукт во время аудита, перед закрытием перечитать итоговый
  current authority.

  Принятая Gas SPEC сейчас описывает «wind» как gas-local forced-flow bias, а не самостоятельный
  layer authority. Владелец просит всерьёз проверить самостоятельный Wind Layer или более общий
  flow/field слой, потому что у ветра могут появиться другие потребители. Это вопрос аудита и
  последующего owner verdict, а не разрешение объявить текущий wind вторым готовым слоем.

boundaries: |
  Read-only preparation. Не запускать BUILD, не менять product code/tests/assets/scenes, не создавать
  ветки, реализации, заглушки, permanent Integration Lab или gameplay consequences. Не исполнять
  Program cleanup из этого трека.

  Water и Wind из planning brief — примеры. Water не проектировать и не создавать. Wind только
  классифицировать по текущим source/spec/tests и сравнить варианты: gas-local; самостоятельный Wind
  Layer; общий flow/field producer. Не выбирать отдельный слой только из-за возможного будущего и не
  создавать для него track/CALL/stub без отдельного owner verdict.

  Не превращать Grid в владельца газа, ветра, разрушения, персонажа, урона или сетевой сессии. Не
  объединять Object ↔ Layer и aperture RED в один BUILD. Не придумывать binding milliseconds,
  min-spec или multiplayer-complete claim без фактической authority и доказательства.

done_when: |
  1. Один owner-readable audit artifact называет точную проверенную product revision/refs и инвентаризирует
     реальные source, tests, fixtures, SPEC/ADR/PLAN для Grid coordinates/topology, layer storage/read models,
     commit/revision/events, object occupancy/contact, destruction/world change, Gas/Wind и multiplayer seams.
  2. Каждая найденная возможность классифицирована как `работает и доказано`, `есть, но не доказано`,
     `устарело/конфликтует`, `сломано` или `отсутствует`, с конкретным evidence pointer. Chat memory и старый
     SHA не выдаются за текущую истину.
  3. Отдельная defect/debt matrix различает Object ↔ Layer, aperture RED и любые новые проблемы; для каждой
     записаны симптом, затронутый контракт, текущая доказательная сила и lawful следующий disposition.
  4. Responsibility/contract map простым языком разделяет Grid, Structure/Destruction, Gas, Wind, object/actor,
     Multiplayer и Integration Lab: кто публикует состояние, кто потребляет, какой committed revision/event
     проходит между ними и где сейчас есть разрыв.
  5. Wind получает evidence-backed классификацию и сравнение трёх вариантов без скрытого выбора. Указано,
     может ли он уже служить реальным независимым consumer layer; если нет, это сказано прямо.
  6. Multiplayer inventory отделяет требования к детерминированному Grid-контракту от session/input/identity/
     transport authority и честно ограничивает текущий claim. Если нужна отдельная работа, сформулирован точный
     кандидат handoff, но новый трек не создан.
  7. Возвращён quality-first planning front: что обязано идти последовательно, что после frozen contract можно
     безопасно делать параллельно внутри Grid, какие межтрековые письма понадобятся и какие 2–3 bounded
     architecture/planning продолжения ведут к детальному master plan. Никакая реализация не открыта.
  8. Владелец получает краткое объяснение выводов и явно принимает или исправляет audit/priorities. Без его
     фактических слов сессия оставляет continuation CALL той же подготовки, а не открывает downstream BUILD.

return: |
  Один work RESULT: путь к audit artifact; точные product refs и evidence inventory; defect/debt matrix;
  responsibility/contract map; Wind и multiplayer verdicts в пределах аудита; quality-first dependency order;
  owner words; один bounded planning successor или точный blocker. Отдельно перечислить, что НЕ запускалось.

budget: one owner-present session
surface: owner-present

END_OF_FILE: live/indie-game-development/work/c-work-grid-current-authority-audit-001-call.md
