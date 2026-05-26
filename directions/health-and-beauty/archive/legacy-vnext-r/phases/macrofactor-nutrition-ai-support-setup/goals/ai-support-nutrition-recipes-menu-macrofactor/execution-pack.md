# Execution Pack

WAVE LENGTH: 5 days

EXECUTION PACK

Goal:
Собрать AI-support чаты для тренировок и питания под Hevy + MacroFactor

Дата создания:
2026-05-03

Appetite:
5 days

Outcome:
После Goal существует минимальный GitHub-markdown-backed AI-support stack из трёх bounded ChatGPT-чats:

1. Training Coach
2. Nutrition / Menu Planner
3. Recipe Builder

Каждый чат имеет:
- compact context block;
- copy-paste-ready starter/restart package;
- понятные input requirements;
- output format;
- restart/context degradation rule;
- no-gos and surface boundaries.

Hevy остаётся местом тренировочного плана, выполнения и логирования.
MacroFactor остаётся местом nutrition targets, веса, food logging и recipes.
GitHub Direction files остаётся минимальным launch/storage layer для prompts, context blocks, restart instructions, reusable recipes, reusable menus, prep templates, MacroFactor entry notes и short handoff notes.

ChatGPT/GitHub files не становятся daily execution surface, daily food log, daily training log, full weekly review system, app setup project, automation layer или full health database.

Acceptance criteria:
1. Three bounded chat definitions exist.
  Observable proof:
  Есть отдельные definitions для Training Coach, Nutrition / Menu Planner и Recipe Builder: роль, inputs, outputs, что чат делает, что не делает.

2. Context blocks cut completed.
  Observable proof:
  Для каждого чата есть compact context block. Для nutrition и training baselines явно разделено:
  - required context;
  - reference-only;
  - do not include.

3. Starter/restart package exists for each chat.
  Observable proof:
  Для каждого из трёх чатов есть copy-paste-ready starter/restart package, который можно вставить в новый ChatGPT-chat и начать работу без доступа к GitHub Direction files.

4. Output templates exist.
  Observable proof:
  - Training Coach выдаёт practical decision/adaptation + Hevy handoff note.
  - Nutrition / Menu Planner выдаёт menu/prep под requested horizon + MacroFactor handoff note.
  - Recipe Builder выдаёт RU cooking/GitHub reusable recipe + EN MacroFactor entry version.

5. Minimal GitHub Direction files launch/storage layer is defined.
  Observable proof:
  Есть короткая GitHub Direction files-структура для хранения prompts, context blocks, restart instructions, reusable recipes, reusable menus, prep templates, MacroFactor entry notes и short handoff notes. Структура не является database, vault, taxonomy или daily log.

6. Manual handoff boundaries are clear.
  Observable proof:
  В финальном pack видно:
  - что запускать в ChatGPT;
  - что хранить в GitHub Direction files;
  - что вручную переносить в Hevy;
  - что вручную переносить в MacroFactor;
  - что не делать в ChatGPT/GitHub files.

7. Sample proof outputs exist.
  Observable proof:
  Есть минимум три sample outputs:
  - Training Coach: practical adaptation/answer по текущему training baseline;
  - Nutrition / Menu Planner: menu/prep на requested horizon;
  - Recipe Builder: reusable recipe RU + EN для GitHub Direction files и MacroFactor entry.

8. Scope protection is embedded.
  Observable proof:
  В каждом starter/restart package есть explicit boundary text против:
  - daily log;
  - app setup;
  - full training/nutrition redesign;
  - full weekly review system;
  - huge recipe vault;
  - automation/API/imports;
  - full GitHub Markdown database;
  - medical/clinical decision-making.

Scope in:
1. Three bounded AI-support chats:
  - Training Coach;
  - Nutrition / Menu Planner;
  - Recipe Builder.

2. Compact context blocks for each chat.

3. Required/reference/do-not-include cut for:
  - nutrition baseline;
  - training baseline.

4. Copy-paste-ready starter/restart package for each chat.

5. Output templates for:
  - training adaptation / exercise / progression / recovery answer;
  - menu/prep planning under requested horizon;
  - RU + EN recipe creation for GitHub Direction files and MacroFactor entry.

6. Minimal GitHub Direction files launch/storage structure for:
  - prompts;
  - context blocks;
  - restart instructions;
  - reusable recipes;
  - reusable menus;
  - prep templates;
  - MacroFactor entry notes;
  - short Hevy/MacroFactor handoff notes.

7. Sample proof outputs:
  - one Training Coach sample;
  - one Nutrition / Menu Planner sample;
  - one Recipe Builder sample.

8. Manual handoff rules:
  - ChatGPT prepares materials;
  - user manually transfers relevant changes/entries to Hevy or MacroFactor.

9. Placeholder support for missing live data:
  - [current Hevy week/session];
  - [current MacroFactor targets];
  - [current constraints];
  - [requested horizon];
  - [available ingredients/equipment].

Scope out:
1. App selection.
2. App comparison.
3. Return to wger.
4. Hevy setup.
5. MacroFactor setup.
6. Filling Hevy or MacroFactor as part of this Goal.
7. Daily food log in GitHub Direction files or ChatGPT.
8. Daily training log in GitHub Direction files or ChatGPT.
9. Full weekly review system.
10. Separate Weekly Review Chat.
11. Full separate training advisory architecture beyond Training Coach.
12. Full training redesign from zero.
13. Full nutrition redesign from zero.
14. Medical track, labs, diagnosis, treatment or clinical decisions.
15. Huge recipe vault.
16. Full GitHub Markdown database, taxonomy or ideal health knowledge base.
17. Codex/Trello bridge.
18. API automation.
19. Imports/integrations between apps.
20. Historical migration of old data.
21. Full productivity/workflow redesign.
22. Broader Direction-wide AI context architecture beyond these three practical chats.
23. Full live-cycle validation of Hevy + MacroFactor + AI-support stack.

No-gos:
1. Do not create a daily food log in GitHub Direction files or ChatGPT.
2. Do not create a daily training log in GitHub Direction files or ChatGPT.
3. Do not configure Hevy as part of this Goal.
4. Do not configure MacroFactor as part of this Goal.
5. Do not fill Hevy or MacroFactor as part of this Goal.
6. Do not create a full weekly review system or separate Weekly Review Chat.
7. Do not redesign training from zero.
8. Do not redesign nutrition from zero.
9. Do not build a huge recipe vault.
10. Do not design a full GitHub Markdown database, taxonomy or ideal health knowledge base.
11. Do not add API automation, imports, integrations or Codex/Trello bridge.
12. Do not make medical diagnoses, treatment recommendations, lab interpretations or clinical decisions.
13. Do not treat GitHub repository as source of truth for execution/tracking.
14. Do not let stale nutrition-only Goal title from Focus Register or stale active-goal file override this Execution Pack.

Rabbit holes:
1. Ловушка:
  “Давайте сразу настроим Hevy и MacroFactor.”
  Ответ:
  Stop. Leave only manual handoff notes: what to transfer manually into Hevy/MacroFactor. App setup is Scope out.

2. Ловушка:
  “Нужен полный weekly review system.”
  Ответ:
  Allow only ad hoc review questions inside Training Coach or Nutrition / Menu Planner. Separate weekly review handoff is deferred.

3. Ловушка:
  “Надо переписать тренировочный план с нуля.”
  Ответ:
  Use the 12-week training plan as baseline reference: current week/month, RIR, progression, Achilles/pain constraints, VR/cardio, check-in metrics. Full training redesign is Scope out.

4. Ловушка:
  “Надо переписать питание с нуля.”
  Ответ:
  Use nutrition baseline as reference: day-types, macro targets, timing, sweet-control, prep logic and adjustment rules. Full nutrition redesign is Scope out.

5. Ловушка:
  “Context block должен включать весь baseline.”
  Ответ:
  Cut context into required / reference-only / do-not-include. Full baseline docs remain reference-only.

6. Ловушка:
  “GitHub Direction files надо сделать красивой базой.”
  Ответ:
  Use only short tree/list storage. No database design, no tags schema, no taxonomy, no daily notes.

7. Ловушка:
  “Recipe Builder должен заранее создать много рецептов.”
  Ответ:
  Create template + one sample proof recipe. Additional recipes are created on demand.

8. Ловушка:
  “Нужна автоматизация импорта в Hevy/MacroFactor.”
  Ответ:
  Use manual handoff notes only. Automation/API/imports are Scope out.

9. Ловушка:
  “Sample outputs становятся реальным execution.”
  Ответ:
  Keep samples as artificial proof outputs. Do not create daily plan/log or final live plan inside S4/S5.

10. Ловушка:
  “ChatGPT начинает логировать день.”
  Ответ:
  Stop. Every relevant output ends with a handoff: what to transfer manually into Hevy/MacroFactor. Logging remains in apps.

11. Ловушка:
  “Нужны точные live targets/week before work can continue.”
  Ответ:
  Use placeholders:
  - [current MacroFactor targets];
  - [current Hevy week/session];
  - [current constraints].
  This Goal builds launch packages, not live app data extraction.

12. Ловушка:
  “Боль, травмы или симптомы требуют решения.”
  Ответ:
  Chat may provide conservative training adjustment framing and escalation note, but does not diagnose, treat or replace medical care.

Milestone map:
M1 — Boundary Lock
Observable proof:
Есть короткая рамка Goal:
- three bounded chats;
- Hevy role;
- MacroFactor role;
- GitHub Direction files role;
- no daily log;
- no app setup;
- no full weekly review system;
- no full training/nutrition redesign;
- baselines are starting materials, not immutable doctrine.

Binary acceptance:
Другой человек может открыть M1 note and answer within 2 minutes:
- what is being built;
- what is not being built;
- where execution/tracking lives.

M2 — Compact Context Blocks
Observable proof:
Есть compact context blocks для:
- Training Coach;
- Nutrition / Menu Planner;
- Recipe Builder.

Nutrition baseline cut:
Required context:
- current MacroFactor targets placeholder;
- day-types L/U/C/R;
- protein target logic;
- calories/macros by day type;
- meal timing around early schedule/training;
- sweet-control rules;
- plate logic / portion anchors;
- batch-prep structure;
- adjustment rules;
- practical preferences.

Reference-only:
- research rationale;
- full 12-week narrative;
- supplement details unless requested;
- health labs section unless explicitly outside this Goal;
- examples not needed for current output.

Do not include:
- Daily Operator;
- Google Sheets TSV workflow;
- old Weekly Planner / RecipeVault integration;
- anything implying ChatGPT logs food instead of MacroFactor.

Training baseline cut:
Required context:
- current Hevy week/session placeholder;
- home weeks 1–4 / gym weeks 5–12 structure as applicable;
- Lower/Upper structure;
- RIR rules;
- double progression;
- deload logic;
- VR/cardio rules;
- Achilles/pain constraints;
- sleep/pain/strength-drop quick rules;
- weekly check-in metrics.

Reference-only:
- full exercise tables unless current session requires them;
- full week-by-week narrative beyond requested context;
- equipment/shopping notes unless requested;
- nutrition note at end of training plan.

Do not include:
- full 12-week document;
- new training architecture;
- anything implying Training Coach logs instead of Hevy.

Binary acceptance:
Each context block can be pasted into a new chat and is usable without pasting full baseline documents.

M3 — Starter / Restart Packages
Observable proof:
For each chat there is a copy-paste-ready package with:
- chat role;
- required user input;
- compact context;
- default interaction pattern;
- output format;
- restart rule;
- context degradation rule;
- boundaries/no-gos.

Binary acceptance:
Each package can be pasted into an empty ChatGPT-chat, followed by a concrete user request, and produce the intended output without additional GitHub Direction files explanation.

M4 — Minimal GitHub Markdown Storage Layer
Observable proof:
There is a short GitHub Markdown structure for:
- prompts;
- context blocks;
- restart instructions;
- reusable recipes;
- reusable menus;
- prep templates;
- MacroFactor entry notes;
- short handoff notes for Hevy/MacroFactor.

Suggested structure:
Directions/Health and beauty/Active Goals/[Goal]/
 AI Support Stack/
   00 — Use Boundary
   01 — Context Blocks/
     Training Coach — Context Block
     Nutrition Menu Planner — Context Block
     Recipe Builder — Context Block
   02 — Starter Restart Packages/
     Training Coach — Starter Restart
     Nutrition Menu Planner — Starter Restart
     Recipe Builder — Starter Restart
   03 — Output Templates/
     Training Coach — Output Template
     Nutrition Menu Planner — Output Template
     Recipe Builder — Output Template
   04 — Sample Proof Outputs/
     Training Coach — Sample
     Nutrition Menu Planner — Sample
     Recipe Builder — Sample
   05 — Reusable Storage/
     Recipes/
     Menus/
     Prep Templates/
     MacroFactor Entry Notes/
     Hevy Handoff Notes/
   06 — Final Pack

Binary acceptance:
The structure is a short tree/list note, not a database, vault, taxonomy or daily note system.

M5 — Output Shape Proof
Observable proof:
There are three sample outputs:
1. Training Coach sample:
  - practical adaptation/answer;
  - conservative constraints if pain/recovery issue exists;
  - exact Hevy handoff note.

2. Nutrition / Menu Planner sample:
  - requested horizon menu/prep;
  - uses MacroFactor targets placeholder;
  - includes MacroFactor handoff note.

3. Recipe Builder sample:
  - RU version for cooking/GitHub reusable notes;
  - EN version for MacroFactor entry;
  - clear ingredients and portions;
  - notes for manual entry.

Binary acceptance:
Each sample visibly proves usable output shape. It is not merely a prompt, abstract advice or daily log.

M6 — Final Pack / Use Boundary
Observable proof:
There is one final copy-paste-ready pack containing:
- launch instructions;
- storage instructions;
- restart rules;
- context degradation rules;
- chat boundaries;
- manual Hevy handoff rules;
- manual MacroFactor handoff rules;
- what not to do in ChatGPT/GitHub files;
- what to save in GitHub Direction files;
- what to update in active-goal.md after S4.

Binary acceptance:
User can open M6 and begin using the stack without returning to S2/S4 context.

Replan triggers:
1. Three-chat stack does not hold.
  If usable result requires a fourth chat, separate weekly review layer or broader AI architecture, stop and replan.

2. Context blocks cannot stay compact.
  If one or more chats require full baseline documents instead of compact blocks, replan M2/M3.

3. Manual handoff is insufficient.
  If usability requires API/import/automation, replan. Do not add automation silently.

4. GitHub Markdown structure becomes database-like.
  If storage requires taxonomy, tags schema, daily notes, tables or vault design, replan M4.

5. Sample proof cannot be produced without real app setup.
  If M5 cannot be checked without configuring Hevy/MacroFactor, replace proof with placeholder-based samples or replan acceptance criteria.

6. Baseline conflicts with live reality.
  If nutrition or training baseline clearly does not fit current reality, record issue and route to separate future Goal/S2/S3. Do not redesign inside this Goal.

7. Medical/safety boundary is crossed.
  If request requires diagnosis, treatment, lab interpretation or clinical decision, stop current path and route outside this Goal.

8. Scope exceeds 5 days.
  If milestone output cannot be completed within 5-day appetite without losing observable proof, cut depth not quality. If cutting cannot solve it, replan.

9. Human Anchor contradicts Execution Pack.
  If final artifacts conflict with accepted M1–M6 boundary, Ready Gate fails and Execution Pack must be corrected.

10. Stale project files override current Goal shape.
  If stale nutrition-only Focus Register or active-goal framing reappears as authority, stop and restate: current GitHub Direction files/session-level Goal Brief and this Execution Pack win.

Reference bundle:
Decision Records:
none.

Canon entries:
1. Workflow/GitHub files must not become daily tracking or daily execution surface.
2. Stale active framing must be corrected, not carried forward.
3. Operational templates must reduce friction or be simplified/removed.

Workflow docs:
1. Master Spec v6.6:
  Use for S4 Plan, Execution Pack object, Ready Gate and S5 transition.

2. Context System v1.6:
  Use for GitHub repository source-of-truth rules, session-level context hierarchy and active-goal.md rebuild after Execution Pack creation.

Direction docs:
1. Health and beauty Direction Context:
  Use for Current Phase, Critical Constraint and Canon against daily tracking in workflow/GitHub Direction files.

Baseline docs:
1. Nutrition MasterPlan:
  Use as reference for day-types, macros, timing, sweet-control, prep and adjustment logic.

2. 12-week training plan v2:
  Use as reference for home/gym structure, Lower/Upper split, RIR, progression, VR/cardio, Achilles guardrails and check-in metrics.

Excluded / stale:
1. Focus Register old nutrition-only framing:
  Do not use as current Goal authority.

2. active-goal.md old pending nutrition-only Goal:
  Do not use as current Goal authority.

Post-S4 update instruction:
After this Execution Pack is accepted:
1. Save this Execution Pack in GitHub Direction files:
  Directions/Health and beauty/Active Goals/Собрать AI-support чаты для тренировок и питания под Hevy + MacroFactor/Execution Pack

2. Rebuild active-goal.md from:
  - current Goal Brief;
  - this Execution Pack.

3. Replace stale Project file active-goal.md.

4. Optionally update Focus Register manually:
  current_goal = Собрать AI-support чаты для тренировок и питания под Hevy + MacroFactor
  current_milestone = M1 — Boundary Lock
  current_wave_id = empty until S5 creates Wave Card
  current_task = empty until S5/S_E
