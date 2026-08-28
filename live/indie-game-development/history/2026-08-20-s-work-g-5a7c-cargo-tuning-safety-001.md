RESULT s-work-g-5a7c-cargo-tuning-safety-001
direction: indie-game-development
play: work
node/task: g-5a7c/t-cargo-tuning-safety-1
outcome: |
  Новая defect-class engine-facing cargo physics tuning отделена от running Repair A и оформлена
  как самостоятельный будущий engineering debt.

  Для неё определены отдельные issue `i-cargo-physics-knobs-unbounded-001`, blocked task
  `t-cargo-tuning-safety-1` и blocked engineering CALL
  `c-exec-g-5a7c-cargo-tuning-safety-1-001`. Они не запускают Unity, не занимают слот и не
  расширяют screenshot wave. Разблокировка наступает только после того, как Repair A пройдёт
  native Unity + binding fresh review, будет принят Direction и интегрирован в fresh product main.

  Acceptance держит одну tuning owner-boundary: `GameRulesSettings` остаётся serialized authoring
  owner и один раз выдаёт typed immutable engine-facing carrier; `CargoBody` не дублирует
  normalization policy в горячем пути. Домены задаются по полям, structural ceilings выбирает и
  обосновывает инженерия, arbitrary gameplay/feel maxima Direction не замораживает.

  Rollback proof связан с тем же production-used engine seam, который считает фактические
  `Simulate` calls: один runnable native test доказывает bounded loop, заставляет настоящий engine
  call бросить, проверяет bare rethrow и возврат `SimulationMode`/gravity. Reflection, string
  dispatch, private/test-only hooks и новый «магический» raw knob запрещены; нынешний
  `+Infinity`-seed можно удалить только вместе с доказанной честной заменой.
evidence: |
  Fresh Direction basis:
  - `git fetch origin main && git reset --hard origin/main` оставили HEAD на
    `58c365d686a4f2b077fa948ef1ad100dd9594e07`.
  - `osctl context --direction indie-game-development
    --for c-exec-g-5a7c-cargo-sleep-repair-1-002` показал текущий CALL как `running`,
    `slot: WIN-U2`, `basis: 97ca2c98485f158d3367103b202000481e1e74d7`,
    `engineering_contract: 36`.
  - `t-cargo-sleep-1` прямо запрещает light close: пункты поведения требуют fresh binding
    verification; текущий журнал говорит, что task не закрыта.
  - `work/2026-08-20-background-cargo-engineering-mandate.md` разрешает автономный технический
    разрез, запрещает расширять screenshot wave и резервировать слот до доказанной потребности.

  Read-only current product evidence from the running U2 tree
  `C:\projects\Unity\GasCoopGame_win-u2` at basis `97ca2c98485f158d3367103b202000481e1e74d7`
  plus its uncommitted Repair A work; это discovery evidence, а не будущий dispatch basis:
  - `Assets/TunnelCrew/Settings/GameRulesSettings.cs:161`:
    `CargoGravity => Mathf.Max(0f, _cargoGravity)` — `+Infinity` остаётся `+Infinity`.
  - `GameRulesSettings.cs:272-285`: linear/angular damping возвращаются raw; max angular speed
    имеет finite-positive fallback; solver iteration getters имеют только lower clamp.
  - `GameRulesSettings.cs:287-305`: repaired sleep/contact имеют field-specific finite fallback,
    а `PhysicsStepsPerTick` только min-clamp и не имеет structural upper bound.
  - `Assets/TunnelCrew/Network/CargoBody.cs:124-131,447-465` пишет tuning в реальные
    `Rigidbody` и `Collider`; `CargoBody.cs:511-532` пишет `Physics.gravity` и вызывает
    `Physics.Simulate(step)` ровно `PhysicsStepsPerTick` раз.
  - Поэтому nonfinite values могут достичь Unity, а raw `int.MaxValue` substeps превращает один
    game tick в практически неограниченную работу.
  - `Assets/TunnelCrew/Settings/GameRulesSettings.asset:22,181-188` содержит текущие валидные
    authored knobs; acceptance не замораживает эти feel values тестами, а доказывает identity для
    любого валидного authored значения и живое влияние каждого serialized knob.
  - `Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoSleepEditModeTests.cs:771-799` сейчас создаёт
    исключение `Step` через `_cargoGravity = float.PositiveInfinity` и проверяет возврат
    `Physics.simulationMode`/`Physics.gravity`.
  - `CargoBody.cs:557-560` сейчас выполняет `catch { GiveBackSimulation(); throw; }`; будущий тест
    обязан сохранить именно честный engine-call failure → bare rethrow → ownership rollback,
    а не только добиться любого исключения.
  - Нормализация обязана обезвредить `+Infinity`, поэтому этот raw knob больше не может быть fault
    source; удаление теста без production-used замены уничтожило бы claim.
  - `C:\projects\Unity\GasCoopGame_dev\validation.config:5,9` подтверждает contract 36 и его
    правило: tuning values находятся вне frozen surfaces и не test-freeze’ятся.

  Direction preflight:
  - `osctl check --direction indie-game-development` = exit 0, 61 существующее неблокирующее
    замечание, механических проблем нет.
  - `uv run --locked python panel/test_docs.py` = `ПРИНЯТО`.
  - owner panel для направления не объявлен.

  Direction engineering self-check / follow-up (не owner quote):
  - Фактический owner mandate — фоновая автономная работа, при необходимости отдельный слот,
    «ожидаем чистое решение, расширяемое, лучшее», «никаких костылей», «обязательно жёсткая
    проверка всего» и «нужна проверка кода» — хранится дословно в
    `history/2026-08-20-s-work-g-5a7c-client-state-owner-word-001.md:19-24`.
  - Production-used engine seam, raw `PhysicsStepsPerTick = int.MaxValue` с подсчётом фактических
    `Simulate` calls, deterministic engine throw с bare rethrow/rollback и запрет
    reflection/string/private/test-only hook — инженерное решение Direction, выведенное из
    Repair-A code evidence выше и этого owner mandate; это не точная acceptance-boundary владельца.
  - Причина correction: delegated engineering follow-up был ошибочно принят за owner word;
    forward repair: `history/2026-08-20-s-repair-g-5a7c-cargo-owner-provenance-001.md`.
state_changes: |
  1. Создать `work/2026-08-20-call-cargo-tuning-safety-1.md` с полным engineering CALL
     `c-exec-g-5a7c-cargo-tuning-safety-1-001`: to executor, direction/node/task/repo,
     kind engineering, `engineering_contract: 36`, budget one focused half-day after unblock.
     Context фиксирует перечисленные current evidence и требует re-derive на fresh post-Repair-A
     product main. Boundaries исключают network snapshots/lifecycle, scenes/art/screenshots,
     cargo dimensions/mass, изменения running Repair A и предварительный Unity-slot claim.
     Отдельно запрещены reflection/string dispatch, private/test-only hooks, fault flags и
     «магические» raw knobs; seam для proof обязан быть production-grade и реально использоваться
     production path, а конкретный класс/имя/HOW выбирает инженерия.

     В CALL ровно три done_when:
     1. **ОДНА OWNER-BOUNDARY И FIELD-SPECIFIC DOMAINS.** `GameRulesSettings` остаётся единственным
        serialized authoring owner и один раз создаёт typed immutable engine-facing carrier.
        Gravity, linear/angular damping, max angular speed, solver iterations/velocity iterations,
        sleep threshold, contact offset и physics steps имеют собственные finite/sign/range/fallback
        правила в этой границе; `CargoBody` не повторяет policy per tick. Где нужен structural
        ceiling, инженерия выбирает, именует и обосновывает его через engine/work safety; universal
        clamp и произвольные feel maxima запрещены.
     2. **VALID TUNING ОСТАЁТСЯ LIVE, ACTUAL UNITY PATH И BOUNDED LOOP ДОКАЗАНЫ ЧЕРЕЗ
        PRODUCTION-USED SEAM.** In-domain values проходят identity-mapping; serialized asset не
        получает guessed tuning edits, а каждый knob остаётся наблюдаемо живым через synthetic
        valid probes, не фиксирующие сегодняшние числа. Native tests проверяют фактические
        `Physics.gravity`, `Rigidbody` damping/maxAngularVelocity/solver properties,
        `Collider.contactOffset` и world progression. Nonfinite/out-of-domain probes не достигают
        Unity. Один production-grade engine-driver boundary или другой production-used честный seam
        проходит тем же runtime path, что игра; один runnable test подаёт raw
        `PhysicsStepsPerTick = int.MaxValue`, считает фактические simulate calls, доказывает не
        больше выбранного structural ceiling и ровно один tick суммарного world progression.
        Seeded bypass/removal mutants падают без запуска unbounded loop.
     3. **ТОТ ЖЕ SEAM СОХРАНЯЕТ BARE-RETHROW/ROLLBACK CLAIM И ЗАКРЫВАЕТСЯ NATIVE + BINDING
        REVIEW.** Тот же runnable test заставляет engine call детерминированно бросить и доказывает,
        что исходное исключение выходит через bare rethrow, `SimulationMode`/gravity возвращены,
        а последующая операция работает. Нынешний Repair A seed через `+Infinity` gravity удаляется
        только вместе с этой честной заменой; молчаливое удаление/ослабление, reflection/string
        invocation, private/test-only hook, fault flag или иной raw knob, который normalization
        обязана обезвредить, запрещены. Возврат несёт native Unity test/build evidence,
        per-field/actual-loop negative controls и binding fresh review.

  2. Создать issue `i-cargo-physics-knobs-unbounded-001`:
     - `_kind: issue`, `level: execution`, `route: work`;
     - `evidence: work/2026-08-20-call-cargo-tuning-safety-1.md`;
     - issue: «`GameRulesSettings` нормализует engine-facing cargo knobs несогласованно:
       nonfinite/отрицательные значения некоторых полей могут попасть в Unity, а min-only
       `PhysicsStepsPerTick` позволяет одному tick выполнить до `int.MaxValue` симуляций.
       Sleep/contact уже имеют repaired fallback; dimensions/mass принадлежат отдельному loud
       invalid-authoring path и сюда не входят.»
     - review_when: «После возврата `t-cargo-tuning-safety-1` на fresh post-Repair-A main с native
       Unity evidence и binding fresh review; закрыть только если valid tuning осталось live,
       actual Unity/world path и bounded loop доказаны через production-used seam, а rollback
       bare-rethrow proof сохранён.»

  3. Создать task `t-cargo-tuning-safety-1`:
     - `_kind: task`, `_bet: bet-g-5a7c-wave-5`, `status: blocked`;
     - goal: «Cargo physics tuning безопасно доезжает до Unity, а число substeps структурно
       ограничено»;
     - unblock_when: «Repair A принят после native Unity + binding review и интегрирован в fresh
       product main; слот не резервирован»;
     - body `done_when` — ровно три пункта CALL выше;
     - note: background engineering, не screenshot task и не gate волны; dependency =
       `c-exec-g-5a7c-cargo-sleep-repair-1-002`; slot выбирается только отдельной будущей выдачей;
       product HOW свободен внутри одной owner-boundary; доказательный seam production-used, а не
       test-only; dimensions/mass и другие перечисленные границы не входят.

  4. Создать call card `c-exec-g-5a7c-cargo-tuning-safety-1-001`:
     - `_kind: call`, `_bet: bet-g-5a7c-wave-5`, `status: blocked`, `to: executor`,
       `for: t-cargo-tuning-safety-1`, `play: work`, `issued: 2026-08-20`;
     - `call: work/2026-08-20-call-cargo-tuning-safety-1.md`;
     - `repo: C:\projects\Unity\GasCoopGame_dev`, `engineering_contract: 36`;
     - description: «Единая нормализация engine-facing cargo tuning и bounded physics-step loop»;
     - тот же compact unblock_when; поля `slot` и `basis` отсутствуют;
     - note: fresh post-Repair-A basis и свободный Unity slot выбираются только при dispatch;
       running Repair A не расширяется и не считается закрытым этой ногой; acceptance требует
       production-used actual-loop/throw seam без test-only обхода.

  5. Одним `osctl leg close` сохранить этот полный RESULT в
     `history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md` и добавить одну log-строку
     в журналы `i-cargo-physics-knobs-unbounded-001`, `t-cargo-tuning-safety-1` и
     `c-exec-g-5a7c-cargo-tuning-safety-1-001`.

  6. `NOW.md`, bet/node/CHARTER, существующие tasks/CALL/status/slot/basis, Repair A, screenshot
     work, network/lifecycle state, knowledge, product repositories и `archive/**` не менять.
     Треки не создавать и не удалять; owner panel отсутствует.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done — оформляется только будущая structural-safety defect-class фоновой cargo-программы; screenshot wave и running Repair A не расширяются.
  - 2 Owner inputs (owner): done — фактические слова владельца: работа «условно ... в бэкграунде»; «желательно, чтобы ты работал автономно»; «тебе самой нужно выстроить работу»; «если нужен слот, там я тебе могу выделить»; «ожидаем чистое решение, расширяемое, лучшее»; «никаких костылей»; «обязательно жёсткая проверка всего»; «нужна проверка кода».
  - 3 Do the work: done — подготовлены один issue, одна blocked task и один blocked CALL с единым tuning boundary, production-used actual-loop/throw seam, тремя done_when и без product implementation/Unity launch.
  - 4 Self-check: done — как Direction engineering self-check, а не owner words, перемерены current getters, actual Unity writes, raw `int.MaxValue` loop с counted `Simulate` calls, authored asset, `+Infinity` seed, production-used deterministic-throw seam, bare `throw;`, rollback, Repair A status/dependency и contract 36; reflection/string/private/test-only proof и запрещённые scope исключены.
  - 5 Close: done — будущая работа зарегистрирована blocked после Repair A, слот/basis не назначены, существующая task/CALL не закрыта; G5 не применяется, потому что никакой product claim этой ногой не закрывается.
log: cargo physics tuning оформлен отдельной blocked-задачей после Repair A — одна граница, bounded substeps и production-used rollback seam
next: |
  return-to-owner; writer после fresh semantic rebase применяет/коммитит/push’ит только объявленные
  Direction-state изменения и возвращает blocker frontier, не запуская новый или существующий CALL.
END_OF_FILE: live/indie-game-development/history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md
