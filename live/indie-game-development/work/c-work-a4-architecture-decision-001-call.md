# CALL — c-work-a4-architecture-decision-001

to: session
direction: indie-game-development
track: переноска
play: work
node: g-6b13
task: a-4
status: ready

## goal

Владелец понял риски, ограничения и цену конкретной архитектуры, по которой двое держат один
самостоятельный груз по сети, и своими точными словами принял, исправил либо отверг её до любого
инженерного наряда a-4.

## context

- `live/indie-game-development/NOW.md`: задача `a-4` и issue
  `i-architecture-pass-skipped-for-this-bet-001` с точными словами владельца о необходимости
  обсуждать архитектуру, а не перекладывать решение на него или исполнителя.
- Принятое устройство слоёв:
  `live/indie-game-development/knowledge/how-the-game-is-built-layers.md`.
- Исходные ограничения совместной переноски:
  `live/indie-game-development/work/notes-two-carry-one-body-2026-08-02.md`.
- Закрытая опора a-3: binding PASS
  `live/indie-game-development/history/2026-08-03-s-work-g-6b13-a3-close-verification-001.md`;
  product tip `8219f6c0bdc5e28d29353b2b29ed08932dc7253d`, candidate
  `22d55e775e1e606811c3dea50118d776ee2d8e6a`.
- Exact-код принятой опоры на published tip:
  `Assets/TunnelCrew/Core/Cargo/{CargoState,CargoHold,CargoPose,CargoRules,AuthoritativeCargoRoster}.cs`,
  `Assets/TunnelCrew/Network/NetworkWalkerCourier.cs` и
  `docs/results/c-exec-one-carries-cargo-proba-001.md` в `ainazemtsau/GasCoopGame`.

## boundaries

- Ничего не писать в продуктовый репозиторий и не выпускать инженерный наряд a-4 без фактического
  owner-verdict в этой owner-present ноге.
- Не выбирать схему за владельца и не превращать рекомендацию агента в согласие владельца.
- Не переоткрывать a-3 и не ломать её принятую форму: отдельный груз, judge-authority, список
  держателей, engine-free расчёт, один согласованный snapshot.
- Только схема двух держателей одного груза: владение решением, намерения и authoritative state,
  сведение целей/сил/права вытолкнуть, конфликт и отключение, сетевой снимок, цена расширения.
- Не строить a-4, второй способ переноски, второй груз, хозяина, копание, тоннель, exe, арт, IK или
  физику груза.

## done_when

- Сохранён один точный архитектурный артефакт
  `live/indie-game-development/work/a4-two-holder-architecture-v1.md`: инварианты, поток намерение →
  судья → правило → снимок, варианты, риски/ограничения и цена изменения принятой a-3.
- Владелец получил понятное объяснение, 2–3 реальных варианта с минусами и одну твёрдую
  рекомендацию; технические названия переведены на язык наблюдаемого поведения.
- Его фактические слова `принять / исправить / отвергнуть` записаны дословно. Без них артефакт не
  считается принятым, a-4 остаётся заблокированной и инженерный CALL не открывается.
- Принятая схема, если она есть, не отдаёт решение клиенту, не делает груз ребёнком игрока, не
  приписывает второй записи уже выбранное поведение и расширяет принятую a-3 вместо замены её
  сетевого и engine-free слоёв.

## return

Полный RESULT play `work`: архитектурный вердикт и exact owner words; a-4 остаётся `open` до
продуктовой реализации. При принятой схеме — отдельный same-task engineering handoff; при правке,
отказе или нехватке одного решения — checkpoint той же owner-present задачи без продуктового CALL.

budget: one owner-present physical session

END_OF_FILE: live/indie-game-development/work/c-work-a4-architecture-decision-001-call.md
