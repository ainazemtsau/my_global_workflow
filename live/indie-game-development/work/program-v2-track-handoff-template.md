# Program v2 — track handoff template

owner: g-9c41 / Integration Lab & Product Proof
approved: 2026-07-20 — s-map-program-v2-hot-migration-route-001

## Когда использовать

Добавляй этот блок в RESULT каждого bounded task, если его результат может:

- изменить прогресс общей тестовой сцены;
- разблокировать или заблокировать другой трек;
- дать Integration Lab новый capability drop;
- изменить глобальный приоритет или обнаружить конфликт authority.

## Ровно шесть строк

```text
status: accepted-candidate | blocked | not-ready | superseded
result: <одно фактическое предложение о результате>
proof: <first-hand checks, revision, capture и/или negative control>
scene_drop: <точный принимаемый артефакт/contract либо none>
blocker: <none либо один точный blocker / CONFLICT / NEEDS RECONCILIATION>
next: <один bounded шаг, complete CALL или owner decision>
```

## Значения status

- `accepted-candidate` — трек доказал свой bounded результат; Integration ещё должна проверить drop.
- `blocked` — done_when не достигнут из-за названного факта, зависимости или конфликта.
- `not-ready` — работа корректно остановилась до реализации, потому что entry/unlock не доказан.
- `superseded` — текущий путь больше не нужен; строка `proof` обязана назвать заменившую authority.

## Обязательные правила

1. `proof` не может состоять из слов «готово», «ревью пройдено» или ссылки на чужой пересказ.
   Нужны first-hand проверки и точная revision/evidence location.
2. `scene_drop` описывает capability, contract и способ проверки. Внутренняя ветка или набор файлов
   без принятого proof не является drop.
3. Если карточка расходится с current product/SPEC/ADR, используй `blocked` и явно напиши
   `CONFLICT / NEEDS RECONCILIATION`; молчаливый выбор запрещён.
4. Один handoff не закрывает Integration milestone автоматически. Integration Lab отдельно проверяет
   seam, общий smoke и отсутствие regression.
5. Трековая сессия не редактирует `program-v2-integration-lab-plan.md` или dashboard напрямую.
   Handoff входит в валидный Direction RESULT; writer обновляет authoritative state и render.
6. Если глобальный прогресс не меняется, handoff всё равно может зафиксировать `scene_drop: none`,
   но нельзя изображать занятость как продвижение сцены.

## Пример формы, не готового результата

```text
status: accepted-candidate
result: universal committed topology event доставлен двум независимым test consumers
proof: validator X GREEN at revision <sha>; stale-revision negative control RED→GREEN
scene_drop: GridTopologyDrop v1 + fixture seed <id> + smoke command <command>
blocker: none
next: Integration Lab проверяет drop против своего M3 smoke
```

END_OF_FILE: live/indie-game-development/work/program-v2-track-handoff-template.md
