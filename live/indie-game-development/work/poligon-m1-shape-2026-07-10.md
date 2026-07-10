# Shape — Полигон М1 (g-9c41)

owner_approved: 2026-07-10 — владелец выбрал «А»; history/2026-07-10-s-shape-poligon-m1-001.md
source_call: work/c-shape-poligon-m1-001-call.md

## Outcome

Полигон М1 — ближайшее интеграционное доказательство g-9c41: один регулируемый Dungeon Architect
уровень примерно на 150 комнат (ориентир владельца 8×8×4 м, около 360–370k клеток с проходами),
где источники имеют тип и силу, игрок трекается в газе, реакции и явный тестовый «взорвать здесь»
работают, один контролируемый стеновой пролом открывает поток по площади щели, sleeping-front и
S4 room-rollup видимы, газ может залить уровень, тот же прогон проходит на двух реальных машинах,
а стоимость записана на слабом железе.

Это представитель цели TREE g-9c41 и ступень к корневому исходу: выпускаемой co-op игре, а не
отдельный технический стенд.

## Appetite и outside view

Appetite: максимум 11 продуктовых легов, ступени 0–10. Это единицы ёмкости, не календарное
обещание. 2026-07-24 либо исчерпание 11 легов — обязательный review; продления нет.

Outside view: Phase 0, Sc-reactions и Sc-sense уже потребовали отдельных PLAN/BUILD/G5/owner-eye
циклов. Аудит g-9c41 фиксирует, что S4 — новый far-representation плюс вывод legacy, а не быстрая
замена тела. Поэтому весь Полигон не сжимается честно в 3–4 лега.

## Подход

Выбран A — S4-first rolling integration:

1. наблюдаемость;
2. дешёвый no-pop proof;
3. room-rollup и auto-subpartition;
4. только затем большой уровень и интеграция уже доставленных систем.

Отклонены:

- level-first, потом оптимизация — S4-триггер уже сработал; против слов владельца
  «оптимизация сначала, потом уровень»;
- меньший fully-fine уровень/кап — молча сдаёт цель 150 комнат; допустим только как последняя
  owner-signed ветка после измеренного провала;
- один монолитный S4-лег — скрывает главный риск перехода между представлениями.

## Лестница 0–10

0. Read-only ActiveCell-перечисление и счётчики шага.
1. Exact collapse/expand одной размеченной комнаты, cheap digest и no-pop proof.
2. Area-aware room-rollup без расширения CoarseBandStep.
3. Детерминированный auto-subpartition открытых объёмов, runtime near/far и видимый sleep/far overlay.
4. Реальный DA-уровень примерно на 150 регулируемых комнат, seed/ProfileHash, источники тип/сила.
5. Подключённый Sc-sense: игрок реально трекается в газе; без damage.
6. Реакции в Полигоне плюс тестовая команда «взорвать здесь» без предварительного газа.
7. Один контролируемый пролом стены; поток зависит от площади открытой щели.
8. Полное затопление уровня; sleeping-front и S4 остаются видимыми и честными.
9. Тот же прогон на двух реальных машинах без рассинхрона.
10. Замер на слабом железе, видео/телеметрия, binding fresh G5 и verdict владельца.

## Текущая rolling wave — ровно три задачи

1. Lv-ingest — уже активная Phase 0; завершает authoritative source seam.
2. M1-A0 — новый безопасный read-only шов в отдельном GasCoopGame_core; BUILD может идти
   параллельно Phase 0 только после доказанного непересечения diff, merge — строго после Phase 0.
3. M1-A1 — bounded S4 opening после MERGED Phase 0 + M1-A0: одна размеченная комната,
   exact collapse/expand, cheap digest, no-pop; production rollup/auto-partition остаются
   следующей rolling wave.

## Cut list

- Sc-damage остаётся HELD; damage/consequence не входит.
- Нет врагов, миссии, баланса, production UI/audio/VFX.
- Нет новой газовой энциклопедии; используются существующие тестовые типы.
- Только один контролируемый стеновой пролом; пол/потолок и полная разрушаемость вырезаны.
- Нет save/load, late join, matchmaking и host migration.
- Один Полигон и минимальный DA module set; не контент-производство.

## Lens sweep

- commercial / traction: ступень 10 даёт проверяемый capture-пакет; публикация остаётся
  в существующих visual/marketing линиях;
- core gameplay depth: ступени 5–7;
- co-op-first: ступень 9;
- technical feasibility: Lv-ingest, M1-A0, M1-A1 и ступени 2–4;
- scope / production: not_needed — держится cut list и одним уровнем;
- audience workflow: ступень 10 кормит существующую внешнюю линию, отдельная соцсеть-задача не нужна.

## Риски и kill

Главный риск: текущий sparse-field допускает mass/meaning-exact detail↔rollup без видимого
скачка и без переделки ядра. M1-A1 тестирует это сразу после минимальной наблюдаемости.
Следующие риски: digest действительно дешёвый и чувствительный к смыслу; auto-subpartition
стабилен без authored-room premise; 150-room flood укладывается на слабом пире; gas входит
в реальную input bus, а не только loopback.

Immediate kill/review: M1-A1 не даёт bit-exact/no-pop в одном bounded slice либо требует
вскрыть архитектурный лок. Performance на финальном профиле: ≤50 ms green; 50–100 ms
owner decision; >100 ms, desync или meaning-loss — ставка не закрыта. Next false:
сначала segment-authored halls / auto-subpartition / tick-divisor / deterministic multicore;
уменьшение уровня — последнее средство и только с подписью владельца.

Forecast: сохранённые S4-швы и доставленный Sc-kernel делают ступени 0–4 вероятными.
Against: S4 handoff, реальная network-input wiring, DA-авторинг и all-filled слабый пир могут
съесть appetite; именно поэтому продления нет.

## Параллельность и очередь

- Phase 0: GasCoopGame_dev, merge slot 1.
- M1-A0: новый GasCoopGame_core, diff-disjoint BUILD параллельно Phase 0; rebase на Phase 0 main,
  полный check и merge slot 2.
- M1-A1: тот же core-worktree после обоих MERGED; merge slot 3.
- Visual dev2, lab, network preparation, OS и fresh G5 идут параллельно только на своих
  поверхностях. Два мутирующих лега одного hot Core одновременно запрещены.

END_OF_FILE: live/indie-game-development/work/poligon-m1-shape-2026-07-10.md
