# Expedition Gameplay Recovery Handoff

## Назначение

Это самостоятельный handoff для новой design-сессии. Он фиксирует реальные
ограничения, открытые вопросы, неудачные попытки предыдущего чата и правила
следующей работы. Это не канон, не Demo Contract, не build-задача и не
разрешение выбрать какую-либо конкретную механику.

Немедленная цель новой сессии: найти или отвергнуть небольшой закон игры,
который многократно производит нарастающие ситуации для игроков. Нельзя
сначала придумать красивую сцену, а затем объявить ее системой.

## Что требуется от игры

Игра рассчитана на меняющуюся mixed-skill группу примерно из 4-8 игроков.
Базовый social-play вектор:

`смотреть -> сделать одно понятное полезное действие -> добровольно разогнать`

Менее опытный игрок должен понимать происходящее и иметь простой вклад.
Опытные игроки могут добровольно сделать ту же ситуацию более рискованной,
сложной и смешной. Игра не должна требовать постоянной тревоги, набора
постоянных классов, рецептов или инженерной процедуры.

Экспедиция должна быть игрой сама по себе, а не демонстрацией симуляции или
транспортной задачей. Повторный заход должен обещать новые ситуации, а не
более точное повторение одного физического трюка.

Требование к давлению времени строгое:

- условия ухудшаются с ходом экспедиции, даже если команда не совершает
  явной ошибки;
- нельзя 30-60 минут безопасно и продуктивно бродить, ждать или чистить
  уровень одним безопасным действием;
- ухудшение должно быть читаемым следствием мира, газа, геометрии и действий,
  а не голым countdown, случайным директором или AI-монстром;
- раннее отступление и частичный успех остаются правильными исходами.

## Действующий paper baseline

Ниже перечислены parent locks. Они не доказывают fun или реализацию.

1. Газ является регулярной физической ценностью экспедиции. Capture сам по
   себе не banking; устойчивый результат появляется только при safe return.

2. Sphere/Bubble является центральной fantasy добычи и custody. В простом
   owner-origin варианте игрок подходит к газу с компактной оболочкой,
   открывает ее, газ видимо входит, Sphere растет, затем игрок закрывает его.
   После этого Sphere остается свободным физическим cargo, а не inventory.

3. Газ внутри Sphere продолжает иметь значение. Газ задает читаемую физическую
   тенденцию, а объем усиливает последствия. Shell является общей прочностью,
   а не матрицей gas-to-shell compatibility.

4. Короткие стропы и body impulses являются текущим paper baseline контроля
   закрытого Sphere. Повреждение или перегрузка с утечкой/выпуском газа -
   допустимая owner-origin возможность, но точный rupture law пока OPEN.

5. Один игрок может контролировать маленький Sphere. Другие игроки должны
   добавлять направление, торможение, rescue и control margin, а не служить
   бинарным `requires N players` замком.

6. Минимальное различие газов - movement/control job. Газ обязан создавать
   реальную работу Counter, Brake или Time: менять позицию добычи, объем,
   момент закрытия, положение тела/строп, торможение, направление или маршрут.
   Другой цвет и другая численная сила не являются новой gameplay ролью.

7. У газа нет brains по умолчанию. Не решать loop через aggro, target choice,
   атаки, HP, creature AI или encounter director.

8. Ошибка должна оставлять мир в измененном состоянии: выпущенный газ,
   ухудшенный маршрут, потерянный cargo, разделение группы, rescue или
   вынужденное отступление. Она не должна быть только health penalty или reset.

9. Свободные world-clots не выбраны. Они сохранены лишь как research hypothesis.
   Их formation, behavior, value и technical lifecycle не приняты.

## Что не выбрано

Не подменять эти OPEN вопросы ложной конкретикой:

- существуют ли clots вообще и нужны ли они demo;
- число и roster газов, реакции, damage, radiation и modifiers;
- Sphere count, capacity, collision model, rupture threshold, controls,
  helper count, lift capacity и networking;
- global timer, finite source profile, pressure-topology rule, destruction
  model, field-to-object force law или activation/temperature scalar;
- tools, artifacts, economy, progression, death/recovery и procedural design;
- доказательство fun, replay, causal co-op, readability, performance или
  production feasibility.

## Что было попробовано и почему это не работает

| Попытка | Зачем ее рассматривали | Почему она не прошла | Статус |
| --- | --- | --- | --- |
| Газ при плотности/объеме становится свободным сгустком | Ограничить клетки, облегчить визуал, создать события | Не был доказан player job, escalation grammar, lifecycle или защита от lootification и waiting. Детали начали изобретаться без закона. | Preserved hypothesis only. |
| Field плюс player-made Sphere, а конечный источник сам выпускает газ | Сделать давление без HUD timer и выбор field/cargo | Конечный обратимый источник выходит на plateau. Возникают wait, cleanup, retry и source-camping exploits. Описанные сцены были cargo stunts, а не масштабируемой грамматикой. | Не использовать как самостоятельный pressure solution. |
| Light/active gas в вертикальной шахте с все более буйными Sphere | Дать яркий visual finale | Это оказался постановочный obstacle course из произвольных сил, геометрии и порогов. Он описывал почти только удачный перенос, не ошибки, не новые решения, не replay. | Явно отвергнуто владельцем. Не оживлять. |
| Глобальная activation, растущая с временем в поле и Sphere | Убрать ожидание после окончания источника | Без пространственных конкурирующих целей это становится "собери максимум и немедленно выйди". Это timer в физической маске, а не gameplay generator. | Не использовать как самостоятельный ответ. |
| Pressure-network cascade: перепады давления, двери/венты, Sphere как pressure vessel | Создавать player-caused cascades и изменение уровня | Это было только последним поспешным seed. Оно не проверено, не раскрыто и не принято владельцем. | Не рекомендация; только невыбранный вопрос. |

## Ошибки предыдущей работы

Новая сессия не должна повторять следующее:

1. Сначала придумывать cinematic scene, потом пытаться подогнать под нее law.
   Нужен generator, а не один stunt.

2. Бросать фразы о ricochet, split/merge, "поймать Sphere", особых дверях,
   лифтах, эффектах, инструментах или thresholds без вывода из закона.

3. Называть источником сложности то, что не меняет следующее действие игрока.
   "Газ сильнее" и "маршрут хуже" сами по себе не являются gameplay answer.

4. Описывать flawless hauling вместо цепочки:
   normal choice -> visible change -> new constraint -> error or voluntary push
   -> persistent world state -> recovery or partial success -> next decision.

5. Превращать примерные числа владельца вроде "20 клеток" в design parameter.

6. Подменять ответ о масштабировании одной картой, шахтой или setpiece.

7. Отвечать на критику новым непроверенным набором идей вместо выявления
   исходного пропущенного вопроса.

## Реально отсутствующий вопрос

Не надо начинать с вопроса "что делает сгусток?" или "как движется Sphere?".

> Какой один небольшой физический закон создает продолжающуюся цепь новых
> решений, ошибок, rescue, partial success и добровольной эскалации, пока газ
> остается главным medium, а Sphere остается интерфейсом capture/custody?

Этот law обязан генерировать ситуации. Он не может только наращивать число,
заполнять комнату, делать cargo тяжелее/легче или сужать один маршрут.

До предложения сцены требуется назвать:

1. State: что сохраняется и меняется - mass, connectivity, pressure, charge,
   phase, structural tolerance или другое?
2. Autonomous change: что ухудшается со временем при competent play?
3. Intervention: как open/close/move/damage/abandon Sphere меняет state?
4. Cascade: какое следующее событие из этого следует без AI/director?
5. Recovery: что группа еще может спасти, перенаправить или пожертвовать?
6. Escalation: почему "еще один шанс" создает качественно другую проблему,
   а не только больший number?
7. Variation: как тот же law дает разные уровни без новой игры на каждом?

## Логическое ограничение, которое нельзя скрывать

Конечная, полностью обратимая и детерминированная система газа имеет
anti-wait проблему. После equilibrium игроки часто могут retry бесконечно.
Чтобы этого не было, должно быть хотя бы одно из следующего:

- продолжающийся physical process;
- видимая необратимая потеря opportunity или route;
- evolving gas/structure state, который не откатывается;
- player commitment of mass, topology или cargo, который нельзя trivially undo.

Это не просьба добавить generic countdown. Это обязательное противоречие,
которое новая сессия должна решить явно. Конечный source сам по себе его не
решает.

## Обязательная форма проверки одного кандидата

Не выдавать десять vague ideas. Проверять один candidate law за раз.

### A. One-line law

Одно физическое правило в одном понятном предложении.

### B. Minimal state and verbs

Назвать только persistent states и player verbs. Для каждого нового tool
объяснить, какой существующий state variable он меняет.

### C. Causal chain

Показать один короткий exact chain:

`ordinary choice -> visible state change -> new constraint on another player ->
mistake or voluntary push -> persistent world change -> recovery/partial
success -> next harder decision`.

Каждая стрелка должна следовать из law или явно объявленного geometry fact.

### D. Three divergent runs in one small topology

На одних комнатах и с одним газом показать:

- cautious early return;
- competent greedy push, который качественно отличается, а не длится дольше;
- error, после которого игра продолжается в измененном мире.

Если все три отличаются только количеством газа, candidate надо отвергнуть.

### E. Scale test

Показать как один law дает минимум три разных level conditions за счет
topology, source/state placement или доступных вмешательств. Не добавлять для
этого монстра, recipe table или отдельную minigame.

### F. Tool test

Каждый tool должен менять уже существующую переменную системы. Tool без
изменяемого state обычно является произвольным контентом.

### G. Hard refutation

Попытаться убить candidate через:

- "подождать, пока все уляжется";
- "один игрок делает все, остальные смотрят";
- "всегда один размер Sphere, route и timing";
- "это просто scripted timer race";
- "то же дешевле дает обычный flow, door или source";
- "наблюдать весело, но действия не меняются".

Если candidate выживает только после добавления многих исключений, gases,
tools, thresholds и bespoke setpieces, он слишком дорог для demo question.

## Правило для будущего разговора о сгустках

Возвращаться к clots можно лишь если baseline доказанно не решает конкретную
нужду. Новый clot proposal обязан объяснить:

- какой player job он делает лучше field gas plus Sphere;
- почему это не loot, projectile, pet или monster;
- почему ждать его не оптимально;
- как сохраняется mass;
- как casual player может проигнорировать или легко затронуть его;
- как advanced player добровольно использует или усиливает ситуацию;
- почему его object lifecycle оправдан технически.

## Стартовая инструкция для новой сессии

> Нужен масштабируемый expedition gameplay generator, а не Sphere-hauling
> setpiece. Сохрани Sphere capture/custody fantasy и mixed-skill 4-8 target.
> Время должно ухудшать условия даже без ошибок, но давление обязано создавать
> читаемые player-caused chains, а не скрытый countdown. Сначала найди и
> критически проверь один law, создающий evolving decisions, errors, recovery
> и voluntary escalation. Не считай selected ни clots, ни pressure cascades,
> ни buoyancy, ни activation, ни sources, ни tools, ни map props.

Первый полезный ответ должен назвать точный gameplay generator и путь его
проверки. Он не должен начинаться с длинного сценария, каталога эффектов или
заявления, что один cinematic moment доказывает replay.

## Workspace references

- `live/indie-game-development/work/minimum-game-frame-v2.md`
- `live/indie-game-development/work/gas-sphere-extraction-custody-frame-v1.md`
- `live/indie-game-development/work/q-gas-behavior-jobs-paper-decision-v1.md`
- `live/indie-game-development/history/2026-07-23-s-repair-gas-phase-condensate-preservation-packet-001.md`
- `live/indie-game-development/history/2026-07-24-s-repair-demo-working-hypothesis-checkpoint-g10-001.md`

END_OF_FILE: work/2026-07-24-expedition-gameplay-recovery-handoff.md
