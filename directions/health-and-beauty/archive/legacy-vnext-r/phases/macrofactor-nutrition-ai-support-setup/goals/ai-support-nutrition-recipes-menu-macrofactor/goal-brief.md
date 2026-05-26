# Goal Brief

GOAL BRIEF

Название:
Собрать AI-support чаты для тренировок и питания под Hevy + MacroFactor

Direction:
Health and beauty

Дата создания:
2026-05-01

Intended outcome:
После Goal существует минимальный GitHub-markdown-backed AI-support stack из трёх bounded чатов, которые живут вне workflow и используются по необходимости:

1. Training Coach
Чат для работы с текущим тренировочным baseline, текущей неделей/месяцем, вопросами по упражнениям, прогрессии, восстановлению, боли/ограничениям и адаптации плана.

Он помогает:
- понять, что делать сейчас;
- применить текущую тренировочную программу;
- адаптировать программу под живую ситуацию;
- разобрать pasted данные, ощущения или проблему после тренировки;
- подготовить понятное решение для ручного переноса или изменения в Hevy.

Training Coach не ведёт лог вместо Hevy и не строит новую тренировочную систему с нуля. Существующий training baseline используется как стартовый материал, а не как неизменная догма.

2. Nutrition / Menu Planner
Чат для работы с MacroFactor targets, nutrition baseline, day-types, расписанием, предпочтениями, нагрузкой и requested horizon.

Он помогает:
- собрать питание под текущую цель;
- составить меню;
- подобрать структуру еды под тренировочные и восстановительные дни;
- сделать prep-блок;
- адаптировать питание под фактическую нагрузку, аппетит и удобство;
- подготовить материалы, которые пользователь вручную переносит в MacroFactor.

Horizon не hardcoded. Пользователь может запросить один приём пищи, один день, несколько дней, 5 дней, 7 дней, неделю, prep-блок, список рецептов или другой practical horizon.

Nutrition / Menu Planner не логирует питание вместо MacroFactor и не заменяет MacroFactor targets.

3. Recipe Builder
Чат для создания reusable recipes, пригодных для чтения, готовки, хранения в GitHub Direction files и ручного занесения в MacroFactor.

Минимальное требование:
- русская версия рецепта — для пользователя, готовки и GitHub Direction files;
- английская версия рецепта — для MacroFactor entry;
- ингредиенты и порции должны быть достаточно понятны, чтобы пользователь мог вручную занести рецепт в MacroFactor.

Recipe Builder создаёт usable recipes по мере необходимости. Он не строит заранее огромный recipe vault.

GitHub Direction files после Goal содержит минимальный reusable launch/storage layer:
- copy-paste-ready context blocks для запуска чатов;
- starter prompts / restart instructions для трёх чатов;
- reusable recipes;
- reusable menus;
- prep templates;
- MacroFactor entry notes;
- короткие notes о том, что вручную переносить в Hevy или MacroFactor.

Hevy остаётся местом тренировочного плана, выполнения и логирования.
MacroFactor остаётся местом питания, веса, targets, food logging и recipes.
ChatGPT-чаты помогают думать, адаптировать, объяснять, собирать меню/рецепты/prep и готовить материалы для ручного переноса.
GitHub Direction files не становится daily food log, daily training log или daily execution surface.

Существующие nutrition и training baselines используются как стартовые рабочие материалы. Они не высечены в камне: чаты должны уметь применять их, объяснять их и адаптировать под реальную ситуацию.

Why now:
После остановки wger и выбора Hevy + MacroFactor нужно проверить не новые приложения, а рабочую связку: специализированные приложения для tracking/execution + bounded AI-support для вопросов, адаптаций, меню, рецептов и prep.

Без этого слоя есть два плохих сценария:
1. Hevy и MacroFactor остаются трекерами без удобного advisory/context слоя.
2. GitHub Direction files или ChatGPT снова начинают превращаться в daily execution surface, что противоречит текущей Phase и Canon.

Этот Goal нужен сейчас, потому что самый короткий путь к live operational stack — не новый redesign питания или тренировок, а простые bounded чаты, которые помогают использовать уже выбранные приложения и уже существующие baselines в реальной жизни.

Appetite:
5 days

Signal strength:
strong

Kill criterion:
Goal нужно остановить или reshape’ить, если usable результат нельзя удержать в форме трёх bounded чатов + минимального GitHub Direction files launch/storage layer, и для продвижения приходится строить одно из следующего:
- daily log в GitHub Direction files или ChatGPT;
- full weekly review system;
- full training redesign from zero;
- full nutrition redesign from zero;
- huge recipe vault;
- full GitHub Markdown database;
- app setup project;
- API automation/imports/integrations;
- Codex/Trello bridge;
- broader Health AI architecture.

Open questions before planning:
1. Какие compact context blocks обязательны для каждого из трёх чатов, чтобы они были useful, но не перегружались полными документами.
2. Какие части nutrition baseline должны попадать в Nutrition / Menu Planner как обязательный context, а какие остаются reference-only.
3. Какие части training baseline должны попадать в Training Coach как обязательный context, а какие остаются reference-only.
4. Какие минимальные поля нужны в Recipe Builder output, чтобы рецепт был удобен на русском, пригоден для GitHub Direction files и достаточно легко переносился в MacroFactor на английском.
5. Какую минимальную GitHub Direction files-структуру использовать для prompts, restart instructions, recipes, menus, prep templates и MacroFactor entry notes, не превращая её в database design.
6. Какой restart rule принять для каждого чата: weekly, by menu/training cycle, by purpose switch или by context degradation.
7. Как разрешить ad hoc review-вопросы внутри Training Coach и Nutrition / Menu Planner, не создавая отдельный full weekly review flow.
8. Что считать достаточным proof в S4/S5: какие observable outputs покажут, что чаты реально можно использовать, а не просто сохранить как красивые prompts.

Scope out:
- App selection.
- App comparison.
- Return to wger.
- Настройка Hevy.
- Настройка MacroFactor.
- Заполнение Hevy и MacroFactor как часть Goal.
- Daily food log в GitHub Direction files или ChatGPT.
- Daily training log в GitHub Direction files или ChatGPT.
- Full weekly review system.
- Отдельный Weekly Review Chat.
- Full separate training system / long-term training advisory architecture beyond Training Coach.
- Full training redesign from zero.
- Full nutrition redesign from zero.
- Medical track, анализы, лечение, клинические решения.
- Huge recipe vault.
- Full GitHub Markdown database / taxonomy / ideal health knowledge base.
- Codex/Trello bridge.
- API automation.
- Imports/integrations between apps.
- Historical migration of old data.
- Full productivity/workflow redesign.
- Broader Direction-wide AI context architecture beyond these three practical chats.
