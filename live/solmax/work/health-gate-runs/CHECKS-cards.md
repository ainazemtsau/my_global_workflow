# Прогон проверок над входом из объявленных карточек

Воспроизводится: `cd live/solmax/work && python health-gate-cards-check-v3.py health-gate-runs/run-2026-07-21-cards.md health-gate-runs/run-2026-07-22-cards.md`

## 1. v2 НА ВХОДЕ ИЗ КАРТОЧЕК — КРАСНЫЙ (и это улика, а не поломка)

Гейт D требует побайтного равенства с `CURRENT.md`/`CONTINUATION.md` старого
пакета. Инструмент проверки был построен под вход, которого done_when 5 не
называет. Хуже: гейты A-C при этом дали «ok» — сочинённой частью для них
остался один билет, карточек они не видели вовсе.

```

==================== ГЕЙТ D — комплект и провенанс ====================
ok    day21/billet.md присутствует (сочинён этой ногой)
FAIL  нет файла day21/context/01-current-state.md
FAIL  нет файла day21/context/02-continuation.md
FAIL  нет файла day21/context/03-programme-and-menu.md
FAIL  нет файла day21/context/04-day-support-procedure.md
FAIL  нет файла day21/context/05-continuity-cards.md
ok    day22/billet.md присутствует (сочинён этой ногой)
FAIL  нет файла day22/context/01-current-state.md
FAIL  нет файла day22/context/02-continuation.md
FAIL  нет файла day22/context/03-programme-and-menu.md
FAIL  нет файла day22/context/04-day-support-procedure.md
FAIL  нет файла day22/context/05-continuity-cards.md

==================== САМОТЕСТ — регрессия к дефекту v1 ====================
ok    проба v1 годна на дне 21 (1 вхожд.) — гейт A её пропускает
ok    проба v1 ОТВЕРГНУТА на дне 22 (0 вхожд. в утаённом отчёте) — гейт A сработал
-- дефект v1 воспроизведён и перехвачен: ложный зелёный больше невозможен

==================== day21 (утаённый ответ: day-report-2026-07-21.md) ====================
ok    day21 проба «passata»: годна (ответ 3) · состояние 0 · вход 0
ok    day21 проба «does not silently rewrite»: годна (ответ 1) · состояние 0 · вход 0
ok    day21 проба «no missed-work debt exists»: годна (ответ 1) · состояние 0 · вход 0
ok    day21 проба «does not establish a comparable»: годна (ответ 1) · состояние 0 · вход 0
ok    day21 проба «unpalatable melon»: годна (ответ 1) · состояние 0 · вход 0
ok    day21 проба «Full-day disposition»: годна (ответ 1) · состояние 0 · вход 0
-- day21: годных проб 6, негодных 0

==================== day22 (утаённый ответ: day-report-2026-07-22.md) ====================
ok    day22 проба «durable correction»: годна (ответ 1) · состояние 0 · вход 0
ok    day22 проба «known-false stored premise»: годна (ответ 1) · состояние 0 · вход 0
ok    day22 проба «nutrition-menu-2026-07-22-v2»: годна (ответ 4) · состояние 0 · вход 0
ok    day22 проба «180 g drained weight»: годна (ответ 1) · состояние 0 · вход 0
ok    day22 проба «are not current menu suggestions»: годна (ответ 1) · состояние 0 · вход 0
ok    day22 проба «Persistent nutrition correction»: годна (ответ 1) · состояние 0 · вход 0
-- day22: годных проб 6, негодных 0

==================== ГЕЙТ F — структурная чистота билета day21 ====================
ok    day21: билет несёт только дословные реплики и нейтральную нумерацию

==================== ГЕЙТ F — структурная чистота билета day22 ====================
ok    day22: билет несёт только дословные реплики и нейтральную нумерацию

==================== ГЕЙТ E — комплаенс day21 ====================
SKIP  возврат прогона ещё не сохранён: /nonexistent

==================== ГЕЙТ E — комплаенс day22 ====================
SKIP  возврат прогона ещё не сохранён: /nonexistent

ИТОГ: КРАСНЫЙ — см. строки FAIL выше.
```

## 2. v3 — ЗЕЛЁНЫЙ

```

========= ГЕЙТ D — поданное множество равно объявленному списку (day21) =========
ok    day21: необязательная 16 `health.nutrition.preferences` подана с названным условием
ok    day21: необязательная 17 `health.nutrition.prep` подана с названным условием
ok    day21: необязательная 18 `health.nutrition.deviations_policy` подана с названным условием
-- day21: обязательных 15/15, необязательных 3, посторонних 0

========= ГЕЙТ D — поданное множество равно объявленному списку (day22) =========
ok    day22: необязательная 16 `health.nutrition.preferences` подана с названным условием
-- day22: обязательных 15/15, необязательных 1, посторонних 0

========= САМОТЕСТ 1 — регрессия к дефекту v1 =========
ok    проба v1 годна на дне 21 (1 вхожд.) — гейт A её пропускает
ok    проба v1 ОТВЕРГНУТА на дне 22 (0 вхожд.) — гейт A сработал

========= ГЕЙТЫ A/B/C — утечка ответа day21 =========
ok    day21 проба «passata»: годна (ответ 4) · срез 0 · билет 0 · карточки 0
ok    day21 проба «does not silently rewrite»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day21 проба «no missed-work debt exists»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day21 проба «does not establish a comparable»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day21 проба «unpalatable melon»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
SKIP  day21 проба «Full-day disposition»: ГЕЙТ B — 1 в срезе состояния, 0 в билете. Законная лексика, не след ответа.
ok    day21 проба «2,400»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day21 проба «190–210 g»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
-- day21: годных проб 7, негодных 1
-- day21: русских проб сработало 0 (не засчитываются в годные)

========= ГЕЙТ P — числовой провенанс карточек day21 =========
ok    day21: каждое число и каждая дата карточек прослеживаются к срезу 6192699

========= ГЕЙТ F — структурная чистота билета day21 =========
ok    day21: билет несёт только дословные реплики и нейтральную нумерацию

========= ГЕЙТЫ A/B/C — утечка ответа day22 =========
SKIP  day22 проба «durable correction»: ГЕЙТ B — 2 в срезе состояния, 0 в билете. Законная лексика, не след ответа.
ok    day22 проба «known-false stored premise»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day22 проба «nutrition-menu-2026-07-22-v2»: годна (ответ 4) · срез 0 · билет 0 · карточки 0
ok    day22 проба «180 g drained weight»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day22 проба «are not current menu suggestions»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day22 проба «Persistent nutrition correction»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day22 проба «550 g raw»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
-- day22: годных проб 6, негодных 1
     day22 русская проба «постоянн»: 1 вхожд. в карточках — смотреть глазами
     day22 русская проба «отцеженн»: 1 вхожд. в карточках — смотреть глазами
-- day22: русских проб сработало 2 (не засчитываются в годные)

========= ГЕЙТ P — числовой провенанс карточек day22 =========
ok    day22: каждое число и каждая дата карточек прослеживаются к срезу 78f8607

========= ГЕЙТ F — структурная чистота билета day22 =========
ok    day22: билет несёт только дословные реплики и нейтральную нумерацию

========= ГЕЙТ G — самотест утечки на отравленной карточке =========

========= ГЕЙТ P — числовой провенанс карточек day22 [чистая база самотеста] =========
ok    day22: каждое число и каждая дата карточек прослеживаются к срезу 78f8607

========= ГЕЙТЫ A/B/C — утечка ответа day22 [ОТРАВЛЕНО] =========
SKIP  day22 проба «durable correction»: ГЕЙТ B — 2 в срезе состояния, 0 в билете. Законная лексика, не след ответа.
ok    day22 проба «known-false stored premise»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
FAIL  day22 проба «nutrition-menu-2026-07-22-v2»: ГЕЙТ C — УТЕЧКА, 1 вхожд. в карточках (в ответе 4).
FAIL  day22 проба «180 g drained weight»: ГЕЙТ C — УТЕЧКА, 1 вхожд. в карточках (в ответе 1).
FAIL  day22 проба «are not current menu suggestions»: ГЕЙТ C — УТЕЧКА, 1 вхожд. в карточках (в ответе 1).
ok    day22 проба «Persistent nutrition correction»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
ok    day22 проба «550 g raw»: годна (ответ 1) · срез 0 · билет 0 · карточки 0
-- day22: годных проб 6, негодных 1
     day22 русская проба «постоянн»: 1 вхожд. в карточках — смотреть глазами
     day22 русская проба «-v2»: 1 вхожд. в карточках — смотреть глазами
     day22 русская проба «отцеженн»: 1 вхожд. в карточках — смотреть глазами
-- day22: русских проб сработало 3 (не засчитываются в годные)

========= ГЕЙТ P — числовой провенанс карточек day22 [ОТРАВЛЕНО] =========
FAIL  day22: числа в карточках, которых НЕТ в улике по срезу 78f8607: 123.9, 2550
ok    гейт C покраснел на отравленной карточке
ok    гейт P покраснел на отравленной карточке

========= ГЕЙТ E — комплаенс day21 =========
ok    day21 ПРОЧИТАНО называет billet.md
ok    day21 ПРОЧИТАНО называет context/01-owner.profile.md
ok    day21 ПРОЧИТАНО называет context/02-owner.mission.md
ok    day21 ПРОЧИТАНО называет context/03-health.nutrition.menu.current.md
ok    day21 ПРОЧИТАНО называет context/04-health.nutrition.budget.md
ok    day21 ПРОЧИТАНО называет context/05-health.nutrition.substitutions.md
ok    day21 ПРОЧИТАНО называет context/06-health.nutrition.corrections.md
ok    day21 ПРОЧИТАНО называет context/07-health.training.programme.current.md
ok    day21 ПРОЧИТАНО называет context/08-health.training.phase.md
ok    day21 ПРОЧИТАНО называет context/09-health.training.progression.md
ok    day21 ПРОЧИТАНО называет context/10-health.training.risk_branches.md
ok    day21 ПРОЧИТАНО называет context/11-health.training.recovery.md
ok    day21 ПРОЧИТАНО называет context/12-health.state.next_action.md
ok    day21 ПРОЧИТАНО называет context/13-health.metrics.baseline.md
ok    day21 ПРОЧИТАНО называет context/14-health.policy.unknowns.md
ok    day21 ПРОЧИТАНО называет context/15-health.observation.latest_training.md
ok    day21 ПРОЧИТАНО называет context/16-health.nutrition.preferences.md
ok    day21 ПРОЧИТАНО называет context/17-health.nutrition.prep.md
ok    day21 ПРОЧИТАНО называет context/18-health.nutrition.deviations_policy.md
-- day21: комплаенс подтверждён присутствием всех имён

========= ГЕЙТ E — комплаенс day22 =========
ok    day22 ПРОЧИТАНО называет billet.md
ok    day22 ПРОЧИТАНО называет context/01-owner.profile.md
ok    day22 ПРОЧИТАНО называет context/02-owner.mission.md
ok    day22 ПРОЧИТАНО называет context/03-health.nutrition.menu.current.md
ok    day22 ПРОЧИТАНО называет context/04-health.nutrition.budget.md
ok    day22 ПРОЧИТАНО называет context/05-health.nutrition.substitutions.md
ok    day22 ПРОЧИТАНО называет context/06-health.nutrition.corrections.md
ok    day22 ПРОЧИТАНО называет context/07-health.training.programme.current.md
ok    day22 ПРОЧИТАНО называет context/08-health.training.phase.md
ok    day22 ПРОЧИТАНО называет context/09-health.training.progression.md
ok    day22 ПРОЧИТАНО называет context/10-health.training.risk_branches.md
ok    day22 ПРОЧИТАНО называет context/11-health.training.recovery.md
ok    day22 ПРОЧИТАНО называет context/12-health.state.next_action.md
ok    day22 ПРОЧИТАНО называет context/13-health.metrics.baseline.md
ok    day22 ПРОЧИТАНО называет context/14-health.policy.unknowns.md
ok    day22 ПРОЧИТАНО называет context/15-health.observation.latest_training.md
ok    day22 ПРОЧИТАНО называет context/16-health.nutrition.preferences.md
-- day22: комплаенс подтверждён присутствием всех имён

ИТОГ: ЗЕЛЁНЫЙ — все гейты пройдены.
```

END_OF_FILE: live/solmax/work/health-gate-runs/CHECKS-cards.md
