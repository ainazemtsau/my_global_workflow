# Engineering CALL — cargo physics tuning structural safety

CALL c-exec-g-5a7c-cargo-tuning-safety-1-001
to: executor
direction: indie-game-development
play: work
node: g-5a7c
task: t-cargo-tuning-safety-1
repo: C:\projects\Unity\GasCoopGame_dev
kind: engineering
engineering_contract: 36
goal: |
  Все authored engine-facing cargo physics knobs остаются живыми в допустимом домене,
  invalid data не доходит до Unity, один game tick имеет конечную structural стоимость,
  а rollback engine ownership сохраняет честное исполнимое доказательство.
context: |
  Direction authority и dependency:
  - live/indie-game-development/work/2026-08-20-background-cargo-engineering-mandate.md
  - live/indie-game-development/cards/t-cargo-sleep-1.md
  - live/indie-game-development/cards/c-exec-g-5a7c-cargo-sleep-repair-1-002.md
  - live/indie-game-development/history/2026-08-20-s-work-g-5a7c-cargo-tuning-safety-001.md

  Этот CALL остаётся blocked, пока Repair A не пройдёт native Unity + binding fresh review,
  не будет принят Direction и интегрирован в fresh product main. При dispatch заново измерь
  fresh product basis и фактически свободный Unity slot; сейчас slot и basis не назначены.

  Current discovery на U2 basis 97ca2c98485f158d3367103b202000481e1e74d7 плюс
  uncommitted running Repair A — это evidence для постановки, не будущий execution basis:
  - Assets/TunnelCrew/Settings/GameRulesSettings.cs:161 пропускает +Infinity CargoGravity.
  - GameRulesSettings.cs:272-285 возвращает damping raw, max angular speed с finite-positive
    fallback, solver iterations только с lower clamp.
  - GameRulesSettings.cs:287-305 уже чинит sleep/contact field-specific fallback, но
    PhysicsStepsPerTick имеет только min clamp.
  - Assets/TunnelCrew/Network/CargoBody.cs:124-131,447-465 пишет значения в реальные
    Rigidbody/Collider; :511-532 пишет Physics.gravity и вызывает Physics.Simulate ровно
    PhysicsStepsPerTick раз.
  - Assets/TunnelCrew/Settings/GameRulesSettings.asset:22,181-188 содержит текущие valid
    authored knobs. Contract v36 (validation.config:5,9) держит tuning values вне frozen
    surfaces: их нельзя превращать в test-frozen feel constants.
  - Assets/Tests/TunnelCrew/ThreeRoomHouse/CargoSleepEditModeTests.cs:771-799 fault’ит Step
    через raw +Infinity gravity; CargoBody.cs:557-560 делает GiveBackSimulation(); throw;.
    Новая normalization обязана обезвредить этот seed, поэтому rollback proof нужен другой,
    production-used и честный.
boundaries: |
  Не трогать network snapshots, delivery, item-state lifecycle, scenes, art, screenshots,
  cargo dimensions/mass и их loud invalid-authoring path. Не расширять и не закрывать Repair A.
  Не запускать Unity и не занимать slot до unblock; не менять screenshot wave.

  GameRulesSettings остаётся единственным serialized authoring owner и один раз создаёт typed
  immutable engine-facing carrier. Конкретное имя/класс и внутренний HOW выбирает PLAN, но
  CargoBody не должен нести дублированную per-tick normalization policy.

  Поля получают собственные домены; один universal clamp запрещён. Engineering может выбрать
  и обосновать named structural ceilings ради engine/work safety, но Direction не задаёт guessed
  exact maxima и не превращает structural safety в gameplay/feel tuning.

  Доказательный seam обязан быть production-grade и реально использоваться production path.
  Запрещены reflection/string dispatch, private/test-only hooks, fault flags и «магические»
  raw knobs, которые сама normalization обязана обезвредить.
done_when: |
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
return: |
  Полный engineering RESULT/HOME по contract 36: fresh basis; commits/parents/manifests;
  diff summary; отдельная disposition и evidence для каждого из трёх done_when; native Unity
  commands/results; actual property/world/simulate-count evidence; seeded negative controls;
  rollback exception/ownership evidence; binding fresh review; assumptions/cuts; rollback.
budget: one focused half-day after unblock

END_OF_FILE: live/indie-game-development/work/2026-08-20-call-cargo-tuning-safety-1.md
