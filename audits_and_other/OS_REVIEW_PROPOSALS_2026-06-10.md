# Ревью Direction OS: сквозной прогон, найденные разрывы, предложения

Дата: 2026-06-10. Это внешнее ревью `os/**` по просьбе владельца: система прогнана насквозь на сложном направлении (соло-разработка коммерческой инди-игры: код + геймдизайн + арт + маркетинг + бизнес, горизонт — годы) и сверена со свежими вводными владельца, которых нет в REQUIREMENTS. Документ самодостаточен — читать переписку ревью не нужно.

Резюме: ядро выдерживает прогон целиком — механику (KERNEL, гейты, пакеты, plays, engineering-контур) менять не предлагается. Найдено 3 настоящих разрыва, 1 недостающее правило маршрутизации и 2 усиления. Все предложения аддитивны: новые файлы и точечные вставки, ни один гейт, схема или бюджет не переопределяется. Сейчас FRICTION.md пуст и формально правки делать не по чему — но это design-stage ревью ДО пилота: дешевле закрыть известные разрывы до первых сессий, чем собирать по два трения на каждый предсказуемый случай. Решение, разумеется, за владельцем по G7: по каждому П — принять / принять с правками / отклонить с причиной.

---

## 1. Новые вводные владельца (контекст для предложений)

1. **Интерактивные сессии, где исполнитель — владелец.** «Надо в Blender что-то сделать, MCP не подключали — хочу чат с активным диалогом: скидываю скриншот, задаю вопрос, получаю пошаговую инструкцию, делаем вместе; с завершением и подтверждением результата». То же относится к ручным шагам в Unity-редакторе после инженерной работы.
2. **Покрыть всё сейчас невозможно — расширение должно быть лёгким.** «Workflow должен покрывать все стадии, но мы сейчас всё не покроем, поэтому нужна возможность легко кастомизировать и расширять, и даже для конкретного direction делать его собственную кастомизацию».
3. **Каждый следующий шаг определён.** «Не должно быть никаких разрывов: если процедура есть — она расписана; где сознательно оставлена свобода — обоснование, почему» (свобода внутри сессии уже обоснована в RESEARCH_BASIS §1–2: раздутые правила снижают исполнение; 44% отказов — спецификация, не исполнение; это ревью её не трогает).

## 2. Сквозной прогон: ситуация → покрытие → вердикт

| Ситуация | Покрытие в os/ | Вердикт |
| --- | --- | --- |
| Завести направление | BOOTSTRAP + frame (интервью → CHARTER, пре-мортем, outside view, корень дерева) | ✓ |
| Узел слишком большой для бета | shape Note: split на 2–4 дочерних outcome-узла | ✓ |
| Спланировать ближайшую работу | shape: аппетит → minimal → scope hammer → lens sweep → RAT → задачи → kill_by | ✓ |
| Сделать задачу-текст/анализ | work play | ✓ |
| Написать код | work → executor CALL → engineering CONTOUR (план-гейт → автономная сборка → G0–G6 → отчёт) | ✓ |
| Побочный вопрос из любой сессии | call:research, дети рекурсивно, return-to-parent | ✓ |
| Идея посреди работы | capture → G8 parked → триаж в shape/pulse | ✓ |
| Бет протух / аппетит съеден | kill_by / G3 → review, продолжение = новый shape | ✓ |
| Проверить «готово» | review свежей сессией, опровержением (G5) | ✓ |
| Ждём внешнего события (плейтест) | task → blocked + unblock_when; pulse следит | ✓ |
| Состояние разъехалось | repair | ✓ |
| Решения владельца | decisions inbox, батч с опциями (G7) | ✓ |
| Новая платформа | adapters/other-platforms (~2 мин) | ✓ |
| Автономия | adapters/autonomy: 3 стадии, тиры | ✓ |
| Изменение системы | FRICTION ≥2 + бюджеты (KERNEL §7) | ✓ |
| **«Сделай со мной в Blender» — владелец исполняет, сессия ведёт по скриншотам** | не покрыто: work подразумевает, что работает сессия; executor — что работает агент; здесь работает владелец | **разрыв → П1** |
| **Повторяющиеся обязательства (devlog раз в неделю, тренировки)** | не покрыто: задачи живут только в активном бете (G2), бет умирает — devlog нет | **разрыв → П2** |
| **Кастомизация направления (свои процедуры/политики/параметры)** | линзы per-direction есть; своих plays/политик у направления нет | **разрыв → П3** |
| Свободный брейншторм с сохранением идей | полу-разрыв: read-only exception запрещает изменения, а брейншторм рождает captures | **правило → П7a** |
| Чтение правил/состояния GitHub-коннектором в чат-платформах | молчаливая обрезка файлов коннектором не адресована | **усиление → П4** |
| Сетап продуктового репо под конкретный стек | PROJECT_SETUP — общая процедура; уроки стека (Unity и т.п.) между проектами не накапливаются | **усиление → П5** |
| Самоисправление продуктового репо | в OS — FRICTION.md; в репо — только «prune AGENTS.md on every mistake» | **усиление → П6** |
| Крупные бинарники в work/ (.blend, арт) | не оговорено | минор → П7b |
| Перенос старых направлений | DESIGN §5: перенос только содержимого | ✓ |

## 3. Предложения

### П1. Новый play: guide (закрывает разрыв №1)

`os/plays/guide.md`, обычный формат play, ≤600 слов. Назначение: сессия, где **исполнитель — владелец** (инструмент без агентного доступа: Blender, Unity-редактор, DAW, железо, физический мир), а сессия ведёт пошагово. Черновик:

```markdown
# Play: guide
Purpose: side-by-side execution — the OWNER operates a tool the agents
cannot reach; the session instructs, verifies by screenshots, adapts.
Reads: the CALL; NOW.md if pointed to; owner's screenshots/answers in-session.
Writes: nothing directly; RESULT as always.

Steps:
1. Recite — goal, done_when, the owner's skill level with the tool
   (ask once; calibrate instruction granularity to it).
2. Path — 3–7 checkpoints from current state to done_when. Show the path.
3. Per checkpoint, loop: ONE action at a time → owner does it → owner
   confirms with a screenshot or a short answer → verify against the
   expected state; on mismatch, diagnose from the screenshot and adjust.
   Two failed adjustments on the same step → propose an alternative route
   or close the checkpoint as blocked (two-strikes, KERNEL §2).
4. Evidence — owner's confirmation per checkpoint + final screenshot or
   artifact; done_when decides, not the session's impression.
5. Close — RESULT: outcome, evidence, captures (ideas/problems seen on
   the way), log line, next.

Done when: the CALL's done_when is met and the owner confirmed it, or a
checkpoint is blocked with the reason recorded.

Notes:
- The session never batches several actions into one instruction; the
  owner's hands are the bottleneck and the error surface.
- A guide CALL is a normal task inside the active bet (G2 applies).
- Engineering reports (VALIDATION G6) may emit a guide CALL for manual
  acceptance/setup steps instead of a flat instruction list.
```

Интеграция: одна строка в KERNEL §6 (список plays) и в schema/packets.md (`play:` enum). Связь с инженерным контуром: G6 «manual acceptance instructions» получает естественное продолжение — если ручные шаги нетривиальны, отчёт порождает guide CALL.

### П2. Recurring-обязательства (закрывает разрыв №2)

Повторяющаяся работа направления (devlog, тренировки, еженедельная рассылка) — это обязательство направления, а не задача бета: она переживает беты и не должна нарушать G2. Предложение:

- В `NOW.md` — секция `recurring:` (бюджет ≤3 на направление): `id, goal, cadence, lens, last_done, call_template`.
- В `pulse` — 10-й пункт чеклиста: «recurring к сроку? → готовый work CALL в decision batch» (pulse уже единственный регулярный сторож — инстанцирование recurring ему органично; сам pulse не исполняет, G7 сохраняется).
- Schema `direction-files.md` — добавить секцию в шаблон NOW.md.

### П3. EXTENDING.md — модель расширения (закрывает разрыв №3 и вводную №2)

Новый файл `os/EXTENDING.md`. Сейчас у направления есть ровно одна точка кастомизации — линзы. Этого мало: у направления появятся свои методики (протокол плейтестов, чек-лист релиза, тренировочная процедура), свои параметры. Куда им деваться — не определено, значит они осядут в чатах и потеряются. Предлагаемая модель:

```text
Уровень            Что можно                                Как
направление        свои линзы                               CHARTER.lenses (уже есть)
направление        свои процедуры                           live/<id>/plays/<name>.md;
                                                            в CALL: play: local/<name>;
                                                            формат и бюджет обычного play
направление        свои политики и параметры                knowledge/ с read_by;
                                                            аппетиты/пороги в CHARTER
продуктовый репо   пороги валидации, рубрика ревью          validation.config, REVIEW.md
система            новые модули (engineering — первый;      os/<module>/ самостоятельной
                   будущие: marketing, content, finance)    папкой; подключается линзами
                                                            и CALL'ами, kernel не правит
```

Три правила: (1) **аддитивность** — гейты G1–G8, схемы пакетов и шесть типов state-файлов не переопределяются никаким уровнем; (2) локальный play подчиняется бюджету и формату os/plays; (3) **путь наверх** — локальный play, повторившийся в ≥2 направлениях, — friction-кандидат на повышение в os/plays/. Так кастомизация направления = один файл в его собственной папке, а ядро остаётся единым и маленьким.

### П4. Транспортная гарантия против молчаливой обрезки (усиление)

Факт: GitHub-коннектор в чат-платформах обрезает длинные файлы **молча** — модель не сообщает об обрезке и работает по хвосту, которого не видела (это документированная проблема чат-коннекторов, не гипотеза). Файлы os/ уже заканчиваются `END_OF_FILE: <path>` — маркер есть, но правило проверки не сформулировано. Предложение, две строки:

- В SESSION_PAYLOAD (Hard habits): «Any file read via a connector must end with its END_OF_FILE marker; a missing marker means the file was truncated — say so and do not rely on the unseen tail».
- В adapters/coding-agent.md (writer): команда `collect`: по CALL собрать единый паст-блок «payload: CALL + relevant play + NOW.md» — канонический вход для chat-платформ без надёжного коннектора (сейчас это делает владелец вручную из трёх источников; writer уже стоит на репо и делает это бесплатно).

### П5. Библиотека профилей стеков (усиление engineering)

`os/engineering/profiles/<stack>.md` (unity.md, python-service.md, web-app.md; ≤100 строк каждый): конвенции структуры модулей для стека, инструмент границ (asmdef / import-linter / dep-cruiser), дефолтные пороги validation.config, известные грабли стека и их механические решения (Unity: одна зарегистрированная test-scene root и `_scratch/` — уже в VALIDATION §hygiene, профиль делает это переносимым). PROJECT_SETUP шаг 1: «если профиль стека существует — он входная точка; нет — сетап создаёт его как побочный продукт». Эффект: уроки сетапов накапливаются между проектами, а не переоткрываются.

### П6. FRICTION в продуктовых репо (усиление engineering)

Симметрия с KERNEL §7: в каждом продуктовом репо `docs/FRICTION.md` (формат как в os/FRICTION.md) + правило: REVIEW.md / validation.config / профиль стека правятся только по точке с ≥2 записями. Сейчас репо-уровень чинится «prune AGENTS.md on every mistake» — это правка по одному случаю, против собственной философии системы. Получается трёхуровневое самоисправление: репо (FRICTION репо) → стек (профиль) → система (os/FRICTION.md).

### П7. Две мелочи

- **a. Маршрут свободного брейншторма.** Read-only exception запрещает изменения, но брейншторм рождает идеи, которым нужно в captures. Одна строка в SESSION_PAYLOAD: «Owner-initiated exploration runs as a research CALL (goal: explore X with the owner); its captures return via RESULT as usual. Pure questions about state stay read-only».
- **b. Бинарники.** Строка в schema/direction-files.md (work/): крупные бинарники (.blend, арт, видео) — git-lfs или внешнее хранилище со ссылкой и заметкой о доступе; в git — только то, что diff-абельно.

## 4. Что сознательно НЕ предлагается

Не трогать: гейты G1–G8, схемы CALL/RESULT, шесть типов state-файлов, бюджеты KERNEL §7, контракт сессии, инженерные гейты G0–G6 и retry-политику, тиры действий и стадии автономии. Прогон показал, что эта механика покрывает всё остальное; предложения — это недостающие поверхности вокруг неё, не её ремонт. Если какое-то из П дублирует уже задуманное — тем лучше, отклоняйте со ссылкой.

## 5. Формат решения

По каждому из П1–П7: **принять / принять с правками / отклонить с причиной** — батчем (G7). После решения правки вносятся обычной maintenance-сессией; FRICTION при этом не нарушается: это design-stage ревью до пилота, зафиксированное этим документом.

END_OF_FILE: OS_REVIEW_PROPOSALS_2026-06-10.md
