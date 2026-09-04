---
id: i-the-shipped-householder-body-is-not-in-the-repository-001
_kind: issue
level: execution
route: shape
status: open
evidence: history/2026-09-03-s-review-g-5a7c-wave-11-close-001.md
_pos: 225
---

## issue
**ПОСТАВОЧНОЕ ТЕЛО ХОЗЯИНА НЕ СОБИРАЕТСЯ ИЗ РЕПОЗИТОРИЯ, И ИМЕННО НА НЁМ ДОКАЗАНО РАВНОВЕСИЕ.**

Замер review 2026-09-03 на `2d2c27ff`, чисто файловый:

1. `Settings/PresentationSettings.asset` даёт хозяину `_prefab` guid `ede90d4d…` =
   `Art/Bodies/Prefabs/Householder.prefab` и `_puppetPrefab` guid `65cc9d73…` =
   `Householder_Puppet.prefab`. У мыши `_puppetPrefab: {fileID: 0}` — **куклу несёт только хозяин**.
2. `Householder.prefab` — **вариант**: его модификации нацелены на источник с guid
   `ed10d0e3cb6b7e245880793a95212970`.
3. Этого guid **не несёт ни один из 1545 `.meta` в `Assets/**`** этого чекаута (проверено
   `find … -print0 | xargs -0 grep -l`) и ни один отслеживаемый файл коммита `2d2c27ff`, кроме
   самого префаба (`git grep`). `Assets/TunnelCrew/Art` при этом отслеживается git целиком и
   джанкшенов не содержит.

**ЧЕГО ЭТОТ ЗАМЕР НЕ ГОВОРИТ.** Открывается ли проект в Unity — этой ногой не проверялось; у ноги,
делавшей равновесие, живой прогон был. Речь строго о том, что **из репозитория это тело не
восстанавливается**.

**ЧТО ЭТО ДЕЛАЕТ С ВЫРЕЗОМ ВОЛНЫ И С ПЛАНОМ.**

- `cut_list` одиннадцатой волны, пункт 10: «Виктор рабочим телом больше не будет». **Он им и есть**:
  `Sources/Anton/homeowner.fbx.meta` несёт `animationType: 3` и `avatarSetup: 1` — валидный
  Humanoid, и кукла построена прямо на нём.
- План, 1.5: «Виктор (Character Creator) в сборку не входит»; Р4 (01.10): «Виктор и его инструменты
  вне сборки». Замена заказана к 22.09.
- **Запасной путь плана называет не то тело.** Риск 9 и таблица входов обещают «текущее
  низкополигональное тело на кукле». В сборке стоит не оно.

**И ОСТАТОК ОТМЕНЁННОЙ ВЕТКИ ЛЕЖИТ В ПОСТАВОЧНОЙ ПАПКЕ.** Три префаба `Mixamo_YBot`,
`Mixamo_YBot_Puppet`, `Mixamo_YBot_Ragdoll` в `Art/Bodies/Prefabs`; guid Y Bot (`f8f93ec8…`) в
настройках не встречается вовсе. Плюс `Quaternius_CasualMale*` — и `Casual_Male.fbx.meta`
по-прежнему `animationType: 2` (Generic): переимпорта, ради которого разворачивалась вся ветка,
не было.
END_OF_FILE: live/indie-game-development/cards/i-the-shipped-householder-body-is-not-in-the-repository-001.md
