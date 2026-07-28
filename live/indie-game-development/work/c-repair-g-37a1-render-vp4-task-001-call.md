# CALL c-repair-g-37a1-render-vp4-task-001

to: session
direction: indie-game-development
track: t-render
play: repair
node: g-37a1
task: t-4
for: t-4
issued: 2026-07-28 by s-work-g-37a1-render-backend-owner-verdict-003
budget: one short owner-visible state diff

## goal

У t-render есть ровно одна ограниченная исполнимая задача по первой интеграции Voxel Play 4 под
Core-grid и законный root CALL; ответственность за критерии визуальной читаемости больше не висит
на закрытой decision-only t-4.

## context

- Владелец дал точный вердикт: "Покупаем Voxel Play 4 и ставим его под нашу логическую сетку".
- t-4 законно закрыта: она оценивала полный горизонт и закрывала только buy/no-buy.
- `bet.lens_verdicts.l2_player_clarity` требует, чтобы два вида различались на глаз и порода
  читалась до реза, но после закрытия t-4 ни одна активная задача этим не владеет.
- Пакет в этой ноге не покупался, не импортировался и не проверялся в продукте.
- Основание и неподвижная граница:
  `work/voxel-play-4-backend-evaluation-2026-07-28-v2.md`; Core-grid хранит единственную правду,
  host упорядочивает команды и публикует `TopologyCommit`, VP4 получает производное зеркало.
- Отдельные sim-task gap и решение `d-sim-build-task-001` не относятся к этой ноге.

## boundaries

- Repair меняет только Direction state после явного одобрения владельцем показанного batched diff;
  он не покупает пакет, не импортирует его и не меняет product repository.
- Не переоткрывать buy/no-buy, полный расчёт, cubic ruling или F3.
- Не создавать и не удалять lanes; не менять чужие tasks, calls, issues или decisions.
- Первая implementation-задача должна помещаться в одну атомарную product-ногу, не более половины
  сфокусированного дня, и доказывать только текущую совместимость с Core-grid плюс явно назначенную
  ей visual responsibility; она не обещает сразу весь будущий VP4 horizon.
- Если пакет фактически ещё недоступен, engineering root получает честный waiting/blocked status,
  а не ложный ready.
- Любой product root обязан назвать разрешённый owner-selected slot, соблюдать product AGENTS и
  закрепить действующий engineering contract до dispatch.

## done_when

Владелец одобрил один точный batched NOW diff; t-render перенаправлена с done t-4 на ровно одну
bounded render implementation-task и один законный ready/waiting root; task проверяет, что VP4
может стоять за F3, и несёт текущую visual responsibility; фактическая доступность пакета и
slot/contract routing записаны честно; `i-render-task-missing-after-vp4-decision-001` закрыта;
несвязанный state сохранён.

## return

RESULT с точными словами одобрения владельца и применённым task/track/root diff; без одобрения -
checkpoint той же repair-ноги.

END_OF_FILE: live/indie-game-development/work/c-repair-g-37a1-render-vp4-task-001-call.md
