# Grid V1 — контроль документационной истины перед разработкой

status: CORRECTION FIRST
prepared: 2026-07-21
scope: planning-only; no product launch

## Коротко

Владелец согласился с главным порядком: перед кодом Grid сначала нужно привести официальную
документацию продукта в непротиворечивое состояние. Но он не принял минимальную замену нескольких
пунктов. Требование сильнее: исполнитель должен видеть только одну актуальную документальную правду.

Поэтому запуск первого продуктового этапа сейчас **не допускается**. Сначала принятый Grid-план должен
получить отдельную поправку, которая либо доказывает механическую изоляцию всей старой документации,
способной повлиять на Grid-работу, либо требует удалить такие файлы из текущего рабочего дерева.
Удаление означает обычный tracked deletion commit: файлы исчезают из актуального checkout, но история
Git не переписывается и сохраняет их как прошлое evidence.

## Точные слова владельца

> «Окей, я согласен. Только единственное, нам не нужно делать минимальную задачу. По документации нужно
> вычистить, привести её полностью в порядок, убедиться, что нам никаким способом старая документация
> не сможет повлиять на работу. Нужно это прям гарантировать. Если мы не можем гарантировать, удалить
> всю старую документацию. Потому что у меня уже были проблемы, когда старая документация, ну, мы
> запускали задачу, и executor, натыкаясь на старую документацию, что-то менял. Я это не сразу замечал,
> и приводило к проблемам. Поэтому нужно строго гарантировать, что актуальна только новая документация.
> Что старая либо в архиве, притом гарантировать, что её никакой executor не начнёт считать правдой.
> Если не можем гарантировать, ещё раз говорю, удалить её тогда полностью. Но имею в виду физически,
> не из Git.»

Бинарное значение этих слов для launch control: **CORRECTION FIRST**. Общий порядок «документы перед
кодом» принят, но нынешняя граница первого документального этапа недостаточна и не является разрешением
на его запуск.

## Что должен был означать первый этап

Первый будущий продуктовый этап должен был менять только правила и документы: убрать конкуренцию между
старыми требованиями `LayerRegistry` / `RevisionFeed` и новым принятым Grid-маршрутом. Он не должен был
писать production code, создавать Wind или Water, удалять legacy source, запускать Unity или открывать
следующий этап Grid.

Эта идея остаётся верной, но одной декларации «старое больше не authority» недостаточно. Старый файл,
который по-прежнему лежит рядом с текущими документами и находится обычным поиском, уже создаёт тот риск,
который владелец запретил.

## Одна точная позиция для исправления

Исправляется `work/grid-v1-executor-plan.md`, раздел `G01 — Legacy fence / authority supersession`,
вместе с его `Outcome / Proof / Rollback`. Сейчас этот раздел требует только заменить активные clauses,
оставить historical ADR evidence и не открывать следующий этап при непринятой замене. Он не требует
полного inventory, единственного allowlist актуальной документации, механического запрета старой authority
и удаления файлов при недоказуемой безопасности архива.

Связанные строки `F1 — active legacy authority clauses` и `No-drift execution control` должны быть
приведены в соответствие с этой одной поправкой, но технический смысл Grid, одиннадцать этапов,
consumer ownership, Multiplayer gate и прочие принятые границы не пересматриваются.

## Что будет считаться гарантией

Поправка может быть принята только если будущий план задаёт проверяемую систему целиком:

1. **Полный inventory.** Перечислен каждый tracked документ, PLAN, SPEC, ADR, инструкция, dashboard или
   ссылка, которая может попасть в контекст Grid executor или направить его работу. Поиск не ограничивается
   файлами со словом `Grid`.
2. **Одна актуальная authority.** Есть точный allowlist current-документов с literal paths и identity;
   executor CALL и repo-level инструкции направляют исполнителя только туда.
3. **Ровно один disposition для старого.** Каждый старый файл либо остаётся в доказанно
   non-authoritative архиве, либо удаляется из актуального рабочего дерева. Неясный статус запрещён.
4. **Архив ограждён механически.** Repo authority прямо запрещает использовать архив и Git history как
   current instructions; validator проверяет активные ссылки, citations и зависимости; seeded negative
   control доказывает, что намеренная ссылка на старую authority ловится.
5. **Выход исполнителя тоже проверяется.** Review обязан искать не только прямые citations, но и решения,
   перенесённые из старых документов без current-authority основания.
6. **Удаление — обязательный fallback.** Если хотя бы один из этих controls нельзя реализовать или
   доказать, соответствующая старая документация удаляется из рабочего дерева обычным Git-коммитом.
   История репозитория не переписывается.
7. **Отдельное опровержение.** Свежая независимая сессия пытается найти любой путь, по которому старая
   документация всё ещё может направить executor. До verdict `could-not-refute` продуктовый старт закрыт.

Это процессная гарантия: старые байты могут существовать в Git history, как прямо потребовал владелец,
но ни один разрешённый вход, инструкция, ссылка, validation path или accepted output не может опираться
на них как на текущую правду. Если такую границу нельзя сделать проверяемой, рабочее дерево очищается.

## Чек-лист любого более позднего допуска

Даже после принятия поправки будущий запуск закрыт, пока одновременно не выполнено всё:

- свежо прочитаны product refs, root/Core instructions, действующий engineering contract и canonical
  worktree registry; текущий snapshot не переиспользуется как launch pin;
- подтверждены accepted-plan identity, поправка к документационной authority и их binding review receipts;
- старые Grid CALL, historical plans и dashboard rows признаны только evidence и не перезапускаются;
- владелец явно выбрал одну площадку, а read-only selector подтвердил fixed branch, clean checkout,
  `AVAILABLE` и `lease none`;
- нет другого mutating owner для Core или product-wide documentation, а integration остаётся serialized;
- будущий product CALL перечисляет literal allowed surfaces, полный documentation inventory, proof и rollback;
- следующий кодовый этап остаётся закрыт до принятой и опубликованной очистки документационной authority.

Любая неопределённость или материальный drift означает STOP, а не разрешение выбрать трактовку.

## Что этот handoff разрешает и не разрешает

Разрешено сейчас только одно: провести отдельную owner-present поправку принятого Direction-плана в
указанной позиции, после чего отдать её на свежую проверку.

Не разрешены: product mutation; удаление или перенос файлов; slot/branch/worktree/root/lease; Unity,
tests, build, benchmark или Deliver; product PLAN publication; G01; следующий кодовый этап;
PAIR-CANDIDATE; BUILD; Wind/Water placeholders; другая Grid implementation work.

## Зафиксированное основание

Direction authority:

- accepted audit `work/grid-current-authority-audit-2026-07-20.md` — blob
  `c1045c8d85f9dbfb2acfeb783bc5362512e888a9`;
- accepted master plan `work/grid-v1-critical-path-plan.md` — blob
  `5169e1cddc0380b1472961f23963f19204324279`;
- accepted executor plan `work/grid-v1-executor-plan.md` — blob
  `dfc8caa77a914ae08100d7c3ff3b174bce2be0ff`;
- executor-plan acceptance receipt — blob `431f9456df0eb0430b171c9d02130fddba1c9edb`;
- binding fresh review receipt `history/2026-07-21-s-review-grid-v1-executor-plan-001.md` — blob
  `53dc02bcd6ef164c51a74110e90a2b0a234da423`, verdict `could-not-refute`.

Read-only product observation, not a launch pin:

- repo `C:\projects\Unity\GasCoopGame` remained clean;
- locally observed `HEAD = main = origin/main = f6e4f725543514bd67441d4be9ca181392f48c73`;
- `validation.config` reports contract v31, blob `502d21a69404f7ec0c998333a2616fe9df1494ef`;
- canonical registry blob `85451b0770dc66fb137deec2396be5bccfcface6` showed all four permanent
  owner-selectable slots `AVAILABLE / lease none`, but no slot was selected or allocated;
- root instructions blob `4fa4b036a98f8ec1cdebcd6ac79c72e670190557`, Core instructions blob
  `f1e8449797ddf1514185b2fe798f3d71a6d9c39e`, living sim-core SPEC blob
  `2c275c49d0b1adcfd4064e8b4a3e6d4b8740c698` and historical ADR-0016 blob
  `996246183afc8d5bec3fac391d363cb8ceb93249` were pinned as later re-read inputs;
- no network fetch was performed.

## Текущее положение

Grid остаётся parallel и не retired. Product progress остаётся **0/11**. Surviving blocker один:
принятый executor plan ещё не содержит требуемую владельцем гарантию единственной актуальной
документационной authority. До owner-approved поправки и её binding review продуктовая работа закрыта.

Basis: owner words above; `NOW.md`; accepted Grid artifacts and receipts listed above; read-only current
product refs/contract/registry observation. External sources: none.

END_OF_FILE: live/indie-game-development/work/grid-v1-g01-launch-control-handoff.md
