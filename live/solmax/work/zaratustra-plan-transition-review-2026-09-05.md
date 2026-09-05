# Zaratustra: переход на план владельца от 2026-09-05

Вердикт review: **obsolete** для ставки «Ядро текстом». Рекомендация: новая
реализация в чистом product repository; старые репозитории сохраняются как evidence.
Новый источник требований — `zaratustra-architecture-plan-2026-09-05.md`, дословный
текст владельца от заголовка до `END.`. Этот разбор не переписывает его требования.

## Основание и граница проверки

Владелец: «надо вот проект делаем точно по этому плану, который тебе ниже»;
«Но если ты видишь, что то, что сейчас есть, оно подходит под новый план, то можно оставить».
Полное исходное сообщение: `zaratustra-owner-message-2026-09-05.md`.
План §44 требует сначала перехода Direction OS state, затем продуктовой реализации.

Direction OS: свежий `origin/main` = `073648d352572c93bdd11c5be762793974a991dd`;
NOW указывает на `g-zara-w0-core-text`, четыре задачи не завершены, единственный
готовый CALL — `c-solmax-zaratustra-v2-w0-head-058`. Владелец ничего не должен на входе
по `osctl context --for g-zara-w0-core-text`. Этот review — отдельный физический чат
от shape 2026-09-04. Проверка не подтверждает выполнение старой или новой версии.

Исследованы актуальные удалённые refs после `git fetch origin`, отдельно от местных
checkout; изучены только названные продуктовые документы и исходники, без archive
и без чтения материалов личных процессов.

| Источник | Проверенный снимок | Что фактически есть | Решение |
|---|---|---|---|
| Старый `ainazemtsau/zaratusta`, актуальная main | `29562edff935a9d674b99856f2a9a17867b93e8c` | README объявляет Markdown-only manager contracts. Нет `src/` и `pyproject.toml`; относительно местной версии удалены рантайм, тесты, инструменты. Репозиторий private. | Не превращать эти contracts в новый Core. Сохранить историю и подходы к provenance, scoped approval, недостаточному контексту. |
| Его местный чистый checkout | `53a52cd24b1d05f658ed805bc533623905703db4` | Python vocabulary, runtime, foundation; это другой, старый снимок, не актуальная main. | Не объявлять его текущим продуктом и не откатывать main к нему. |
| `ainazemtsau/solmax-operating-substrate`, актуальная main | `05d3c95c0b80bca6008ba5cd9694f61b17fe88e6` | README: private monorepo с packs и материалами владельца, compiled runtime отсутствует; Python проверяет wiring, не transactional state. Местный HEAD `f1289413bf29eaf9bf205daf0d1506198e8183fd` отставал. | Сохранить как источник идей Process Pack. Не копировать private workspace в публичный продукт. |
| Предложенное новое имя `ainazemtsau/zaratustra` | authenticated `gh repo view` 2026-09-05 | GitHub не разрешил это имя для текущего аккаунта; в `C:/projects/` нет checkout под этим именем. | Новый bootstrap должен проверить доступность имени; это не доказательство глобального отсутствия repo. В этом review repo не создан. |

## Что подходит и что заменяется

| Требования нового плана | Старое основание | Перенос |
|---|---|---|
| §§0–3: сменяемые модели, Work, Process, единый Core | Устав: центр и эксперты, фиксированные пять сущностей; Wave 0 — ноль исполняемого кода | Старую Wave 0 снять. Термины и responsibilities брать из нового плана, без искусственной квоты сущностей. |
| §§4–5, 25–29: SQLite, единый Mutation API, migrations, CLI | Operational Markdown/Git; старые контракты не реализуют DB-транзакцию | Реализовать заново foundation. Python 3.13, uv, sqlite3, Pydantic v2, pytest, ruff, SHA-256 уже выбраны владельцем. |
| §§6–7, 24, 40–42: переносимый Handoff, свежий Work open, receipts | Есть идеи handback, source/freshness и ограниченных effects | Перенести проверяемые требования и отрицательные примеры; не старые payload/schema/layout. |
| §§8–10: Process contract и ограниченный context | В substrate есть packs и границы доступа; в старом vocabulary context/permission | Сохранять идею изоляции и provenance. Не копировать domain/state machinery. |
| §§11–17, 20, 32–34: память, персонализация, evals | Есть классификации owner-context, но доказанная новая learning loop отсутствует | Отложены по milestones; в M0 хранить только нужные source/evidence связи. |
| §§18–19, 21–23, 35–38: executors, routing, assistant, autonomy, UI | Старые ближайшие волны уже включали MCP, план дня, health и self-build | Не переносить в M0. MCP после основного CLI flow; старые сроки и волны не действуют как новая roadmap. |
| §§1, 14–16, 39, 43: no fine-tuning, anti-sycophancy, vertical slice | Часть прежних целей строилась вокруг ежедневного менеджера | Новые инварианты сохраняются целиком. Нельзя превратить будущие примеры в текущие requirements. |

Проверка возможности прямого reuse по конкретным файлам местного старого Python:

- `src/foundation/paths.py` ищет `pyproject.toml` как repo root. Новый workspace
  произволен и отделён от installed product: это неверная граница для `zara init`.
- `src/foundation/ids.py` даёт slug-vN, не globally unique operation id. Это не
  готовая реализация idempotency.
- `src/vocabulary/artifact.py` хранит opaque body и retention; нет необходимого
  SHA-256/versioned-file/transactional-active-revision протокола.
- `src/vocabulary/permission.py` хорошо отделяет текст от grant, но привязан к
  старым area/run/class enums. Сохранить смысл теста «надпись разрешено не grant»,
  а schema строить под Work authority нового плана.
- Актуальные `contracts/source-context.md` и `contracts/workspace-boundaries.md`
  дают полезные требования: scope, freshness, evidence, точное разрешение effects.

Поэтому найденная ценность — принципы и сценарии проверок. Готового подходящего
foundation не обнаружено. Массовое удаление ничего не ускоряет; старые refs полезны
для сравнения. Чистый checkout нового продукта не должен наследовать запреты и
схемы старого Markdown-only продукта. Продуктовые файлы этим review не меняются.

## Технические замечания к реализации, не новая спецификация

1. **Duplicate до изменяемых preconditions.** Буквальный порядок §5 проверяет
   expected_revision до operation_id. После первого успеха revision уже новая;
   повтор того же запроса иначе превратится в conflict вместо возврата receipt.
   Рекомендация для Work 3/5: после schema и проверки личности/доступа к receipt
   найти сохранённый operation_id и сравнить стабильный fingerprint запроса,
   включая actor/work/scope. Идентичный replay возвращает исходный receipt без
   эффекта; иной payload с тем же id — collision. Только новая операция проходит
   проверки текущего Work status/authority/revision. Нельзя позволять replay
   чужому actor читать чужой receipt. Это вывод из §§5, 6 и 28, а не новый feature.

2. **Одна DB-транзакция не охватывает обычные файлы.** SQLite атомарно фиксирует
   свои изменения; это не делает запись artifact и projection частью той же
   транзакции. Сначала полностью опубликовать immutable/versioned artifact и
   проверить SHA-256, затем одной DB-транзакцией связать artifact, state, event,
   operation receipt и revision. Сбой до DB commit может оставить бесхозный файл,
   но не активную ссылку на неполный файл. После commit сбой projection rebuild
   не означает, что mutation откатилась. Recovery/rebuild должен восстанавливать
   projection из DB; повтор mutation не должен создавать второй эффект.
   [SQLite atomic commit](https://www.sqlite.org/atomiccommit.html).

3. **Concurrency и transaction mode должны быть явными.** Проверка revision вне
   транзакции не предотвращает гонку. SQLite имеет одного одновременного writer;
   `BEGIN IMMEDIATE` может вернуть BUSY. Рекомендуются bounded busy handling и
   compare-and-set/проверка revision внутри write transaction. У Python connection
   context manager сам по себе не открывает транзакцию; режим выбрать явно.
   [SQLite transactions](https://www.sqlite.org/lang_transaction.html),
   [Python 3.13 sqlite3](https://docs.python.org/3.13/library/sqlite3.html#how-to-use-the-connection-context-manager).

4. **Снимок projections/context должен быть воспроизводим.** `generated_at` от
   текущих часов даёт разные байты для одной revision. Простое решение: timestamp
   исходного committed snapshot либо явно переданное фиксированное время сборки.
   Контекст собирать из согласованного снимка, manifest должен называть реальные
   revisions. Budget нельзя тихо превышать или резать acceptance/authority.
   Это требования §§4.4 и 10; точный формат выбирается ограниченной Work.

5. **Receipt trust приходит от caller, не из JSON.** Даже `owner_instruction.exact_text`
   — содержимое Handoff, пока trusted owner-mediated канал не подтвердил получение.
   File и stdin должны вызывать один importer/Core. Проверить попытку приписать
   `approved: true`, расширить scope, сослаться на чужой Process, подменить hash или
   выйти путём за workspace. Сильная модель не получает дополнительных прав.
   Foreign keys включать явно на connections, boundary validation не должна
   превращать строки в bool/int незаметно.
   [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html#fk_enable),
   [Pydantic strict validation](https://pydantic.dev/docs/validation/latest/concepts/strict_mode/).

6. **Не симулировать clean-chat proof одним тестом.** Unit/subprocess tests
   доказывают persistence, duplicate, stale, crash и isolation. Continuity требует
   отдельного нового чата, получающего только `work open` package: он должен назвать
   принятое решение, evidence, revision, полученный результат и следующий шаг без
   старой истории. В review этот эксперимент не проводился, PASS не заявлен.

## Проверяемый предел первой реализации

Работы 1–8 из §41 сохраняются в исходном порядке: foundation → records → mutation
→ artifacts/projections → handoff → context → result → end-to-end. Это продуктовые
Works плана; этот review не создаёт восемь задач внутри старой ставки.

М0 обязан показать init в пустой папке, fictional Process, Work/context, handoff
через file/stdin, mutation receipt, next Work и продолжение новым чистым чатом.
Дополнительно: один эффект от двух импортов (включая replay после завершения Work),
отказ stale revision, атомарность при прерывании процесса, permission denial,
отказ подложного external approval, отсутствие чужого контекста, audit и rebuild.
Падения нужно проверять до/после commit, а не только Python exception внутри `with`.
Второй различный Process — M1; для отрицательного isolation test M0 достаточно
чужого sentinel, это не реализация полноценного второго Process Pack.

После Work 8 — показ владельцу и остановка. Proof E и дальнейшие персональные evals
не объявляются выполненными из-за наличия policy; они требуют будущих реальных данных.

## Закрытие старой ставки и последствия

Шесть строк старого done_when не доказаны как завершённый набор: публичный новый
repo не подтверждён, прежний HEAD не актуальная main, полного CORE и его приёмки
в истории задачи нет. Вердикт **obsolete**, а не met/partial; вышеутверждённый план
снимает саму необходимость отдельной «нулевой волны» без кода.

По линзам: extensibility теперь проверяется Process contract (полное M1 позднее);
real depth — сменой сессии с осмысленным продолжением; agent-buildability — Works
1–8 без дополнительного дерева абстракций; dogfood — один реальный поток в M2 после
M0/M1; privacy — fictional данные в публичном продукте и authority внутри Work;
cost — deterministic CLI без API/router/авторасходов в M0.

Cut add-back: executable code, boundary schemas, migrations и failure tests стали
необходимы M0. CI workflow с расходованием Actions минут, настоящий health process,
автономные агенты, frontend и migration всего Direction OS не добавлены. Старый
лимит 2500 слов и запрет кода не продлеваются, потому что ставка закрывается.

Прогноз: **no_basis** для срока/числа сессий нового M0. Старый прогноз «~5 ног до
приёмки текста» потерял предмет; это не measured throughput новой архитектуры.
Сюрприз: новый запрос меняет критерий ценности до завершения первой текстовой
задачи. Из этого не выводится характеристика личности или memory preference.

Три рассмотренных направления продолжения: старую волну продолжать (против новой
инструкции), исправлять старый рантайм/Markdown state (не соответствует выбранному
storage), принять новый foundation (выбран владельцем текстом плана). Его слова
достаточны для снятия старой ставки; повторное голосование не требуется.

## Следующая граница Direction OS

Review закрывает старые bet/node/tasks/CALL, сохраняет точный план и source-priority
knowledge, помечает tree validity как ожидающее frame/map. Старые будущие узлы
остаются parked до map; новые задачи/ставка/полосы здесь не создаются.

Следующий единственный CALL: frame — привести CHARTER и корень к §§0–1, 26, 28–44
утверждённого плана. Затем map заменяет старые волны и shape допускает только M0.
Это оставшаяся часть перехода; продуктовую реализацию этот review не разрешает.
Ни новый успех 30-дневного менеджера, ни shutdown Workflow не должны автоматически
стать требованиями M0. Совместимые старые бюджет/приватность/приоритеты сохраняются,
содержательные отклонения от нового плана выносятся отдельно.

END_OF_FILE: live/solmax/work/zaratustra-plan-transition-review-2026-09-05.md
