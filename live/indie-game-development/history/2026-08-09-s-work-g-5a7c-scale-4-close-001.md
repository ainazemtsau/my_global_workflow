RESULT s-work-g-5a7c-scale-4-close-001 (call: c-exec-g-5a7c-loot-inactive-until-held-001)
direction: indie-game-development   play: work   node/task: g-5a7c/t-scale-4
close: light — because каждая строка done_when заново разрешается точными commit/parent/tree/manifest,
записанными outputs проверок и дословными словами владельца, уже сохранёнными в опубликованном RESULT;
ни одного оставшегося качественного вердикта эта нога не додумывает

outcome: |
  `t-scale-4` закрыта по прямому слову владельца. Живой груз получил настоящую host-owned высоту,
  падает после отпускания и ровно один раз создаёт ситуацию посадки; лежащий груз физически
  деактивирован и потому не производит следующих тиков контакта/шума. Любой груз остаётся низким
  ориентированным препятствием для мышей, кроме собственного держателя; в сцене четыре одинаковых
  куска. Финальный owner-run подтвердил видимую реакцию хозяина.

  Product bytes сохранены на `origin/slot/win-u1`, но НЕ выдаются за доставленные в `dev/main`:
  accepted product commit `e7dc8f5bcc1df598ca30ebf74df711ba4cca0400`, docs-only RESULT tip
  `d9518538d0aa6d402493ef6465b26936fa0567fd`. WIN-U1 освобождён.

  Обнаруженная слабость структуры не расширяет эту задачу: текущий cargo-specific bridge закрывает
  ПРОБУ, но не выбран как общая event/situation architecture. Для Direction заведена отдельная
  issue с триггером до второго типа ситуации/потребителя или на review ставки.

evidence: |
  **CALL done_when 1 — lifecycle, посадка, structural silence. ЗАКРЫТА.** Product commit
  `e7dc8f5bcc1df598ca30ebf74df711ba4cca0400` имеет единственного родителя — точную базу
  `102af1b1c076148ff6a7af7591f92b6880cdc70d` — и дерево
  `8dcd8b1850b60393551e7760bf1e1a0fedbdd466`. Его 23-path manifest содержит host state/Y,
  `CargoBody` lifecycle/contact, snapshot/presentation и focused lifecycle tests. Опубликованный
  `docs/results/c-exec-g-5a7c-loot-inactive-until-held-001.md@d9518538` построчно фиксирует:
  inactive collider/contact/simulation off; next-tick zero reads/noise; typed one-shot `Landed`;
  separate support point; no forged force. Headless output там же: **135 passed, 0 failed,
  0 skipped**; hygiene: **OK**.

  **CALL done_when 2 — ящик, несколько кусков, gravity. ЗАКРЫТА.** Тот же manifest содержит
  `CargoAwareWalkSpace` и `CargoWalkSpaceTests`: own top before sides, rotated local frame,
  activity-independent obstacle, one-sided answer, own-holder exception and a real gap between
  pieces. `NetworkPlaySettings.asset@e7dc8f5b`: `_walkerGravity: 3`, `_cargoGravity: 3`, четыре
  одинаковых spawn `(0,2.5)`, `(-2.5,-0.35)`, `(-2.5,0)`, `(-2.5,0.35)`, размер
  `0.192 × 0.04 × 0.04`. `ProjectSettings/**`, cargo-class seam и delivery не входят в manifest.

  **CALL done_when 3 — сохранённые границы, Unity, owner-eye, rollback. ЗАКРЫТА.** В принятом asset
  остались `_cargoMaxHolders: 2`, pickup/carry/grip `1.28 / 0.8 / 1.6`, thresholds
  `60 / 150 / 400`; X/Z наклон тела по-прежнему заморожен. RESULT `d9518538` содержит direct
  WIN-U1 synchronous import/compile evidence без Error/Exception/Assert, точный rollback
  `git reset --hard 102af1b1c076148ff6a7af7591f92b6880cdc70d` и readback базового tree
  `900bc02baf933ab9e46ffa59e657abb1284af505`, затем восстановление exact candidate.

  **Слово владельца, дословно и уже закоммичено в `d9518538`:** «Так, я прогнал, протестировал,
  сейчас работает. Сейчас хозяин пойдет, закрывать». До фикса он называл единственный остаток:
  «работает НО я не вижу реакцию хозяина когда отпускаю груз»; после typed-situation iteration этот
  остаток снят его повторным прогоном. Затем он прямо поручил самому закрыть продукт и записать
  задачу в Direction.

  **Публикация/слот перемерены этой ногой:** `origin/slot/win-u1` =
  `d9518538d0aa6d402493ef6465b26936fa0567fd`; selector WIN-U1 = `state: CLEAN`,
  `lifecycle: AVAILABLE`, `lease: none`, `availability: AVAILABLE`.

  **Deliverable reconciliation:** все три bullets issued CALL имеют отдельные диспозиции выше;
  построенные product paths и recorded run artifact названы. Ничего не закрыто обещанием
  «посмотреть позже». `review: n/a — light change` по venue `plays/work.md`; frozen/openspec
  change-id CALL не объявлял.

state_changes: |
  1. Закрыть task card `t-scale-4`: terminal status `done`, closure/history
     `history/2026-08-09-s-work-g-5a7c-scale-4-close-001.md`.
  2. Закрыть возвращённую call card `c-exec-g-5a7c-loot-inactive-until-held-001`: status `closed`,
     та же history. Не менять другие calls/tasks, `NOW.bet` или статус `g-5a7c`.
  3. Добавить pointer issue `i-world-situations-need-extensible-reaction-architecture-001`:
     `level: objective`, `route: review`, evidence — product RESULT `d9518538`; точные body и
     review trigger заданы этой транзакцией. Issue не авторизует BUILD и не становится задачей.
  4. Создать `work/c-work-g-5a7c-scale-6-call-001.md` и зарегистрировать call card
     `c-work-g-5a7c-scale-6-call-001`: `status: ready`, `to: session`, `play: work`,
     `for: t-scale-6`, `issued: 2026-08-09`. Это следующая локальная нога активной ставки; она
     сначала учитывает честную product disposition (`origin/slot`, не `dev/main`) и пишет законный
     executor CALL, не чиня архитектурную issue внутри `t-scale-6`.
  5. Одним `osctl leg close` сохранить этот полный RESULT в
     `history/2026-08-09-s-work-g-5a7c-scale-4-close-001.md` и добавить log ровно один раз в
     журналы `g-5a7c`, `t-scale-4`, returning call, новой issue и нового continuation call.

captures: []

decisions_needed: []

play_check:
  - 1 recite: done — task/card и issued CALL сведены попунктно; задача обслуживает активную ставку g-5a7c
  - 2 owner inputs (owner): done — владелец дословно сказал «я прогнал, протестировал, сейчас работает… закрывать» и поручил самому записать Direction
  - 3 do the work: done — product commits/readbacks, result, remote slot ref и terminal selector перемерены; архитектурная находка вынесена issue без реализации шины
  - 4 self-check: done — три CALL bullets имеют отдельные evidence tokens; task done_when покрыта; недоставка в dev/main названа, а не скрыта
  - 5 close: done — current task/call закрываются, issue регистрируется, следующая local continuation служит t-scale-6

log: лут живёт только в луче или падении, после посадки структурно молчит и остаётся низким препятствием — задача закрыта повторным прогоном владельца; общий situation-layer вынесен отдельным вопросом архитектуры

next: |
  CALL `c-work-g-5a7c-scale-6-call-001` — session work на готовый к отправке наряд для `t-scale-6`:
  четверо могут держать один груз, усилие суммируется с потолком на руку, а числа с текстурой
  «лёгкий — один, средний — двое» при отсутствии решения возвращаются владельцу.

END_OF_FILE: live/indie-game-development/history/2026-08-09-s-work-g-5a7c-scale-4-close-001.md
