# CALL c-shape-near-gas-l1b-001

to: session
direction: indie-game-development
play: shape
node: g-9c41
task: NearGas-L1B
issued: 2026-07-16 (s-review-poligon-m1-route-reset-001)
parent: s-review-poligon-m1-route-reset-001

goal: |
  У g-9c41 есть утверждённая владельцем ограниченная ставка L1B: доставленный L1a становится внутренне
  наблюдаемым в retry/fault/handler/kernel/loopback сценариях и честно продвигает gas-authority трассу M1.

context: |
  Fresh review s-review-poligon-m1-route-reset-001 закрыл старую Poligon M1 ставку с verdict NOT MET: полезные
  foundations существуют, но ни один критерий не закрыт end-to-end в общей representative scene. Владелец после
  полного review-брифа выбрал следующую ставку фактическими словами: «L1B».

  NearGas L1a DELIVERED через owner-authorized experimental skeleton → independent genuine RED → BUILD → fresh
  refutation. Product remote dev/main на закрытии были exact 400ef8eca1e747378493c97530770286c7e26ff1; focused
  71/71, tick types 8/8, normal 1714/1714, full 1793/1793, Deliver GREEN, binding fresh G5 PASS. L1a остаётся
  dormant engine-free single-writer authority с atomic generation replacement и deterministic Step.

  Engineering maintenance B1–B4 завершена до OS contract v26, и владелец сообщил о terminal GasCoopGame v26
  Re-sync. Старый v22 PLAN-AMEND packet/carrier RETIRED / FORBIDDEN и не является launch authority.

  Текущая product authority `docs/neargas-L1-decisions.md` отдаёт L1b только внутренние observation seams:
  retry snapshot, fault injection, handler classification, kernel rows и loopback trace; их нельзя выдумывать или
  молча расширять. Frozen child acceptance для L1b ещё не существует. L1b — instrumentability L1a, а не Unity,
  gameplay, ресурсный admission или готовая сцена.

  Принятый cross-bet M1 route остаётся work/poligon-m1-integration-route.md: 34 обязательных логических product
  legs плюс условные — ledger, не cap. 24.07 — контрольный review, не остановка. Каждая отдельная ставка всё равно
  получает собственный bounded appetite по G3. g-9c41 остаётся активным multi-bet node; сейчас активной ставки нет.

boundaries: |
  Direction shape only. Не менять product, Unity, canon или CHARTER; не выпускать executor/PLAN/RED/BUILD CALL до
  owner-approved закрытия shape. L1a остаётся DELIVERED, старый v22 route — forbidden. Не включать в L1B молча L2
  resource admission, C1 committed digest, Unity cutover, workers/concurrency, S4, Level/DA/PGG или common M1 scene.
  Не превращать cross-bet no-cap instruction в безграничный appetite одной ставки.

done_when: |
  1. NOW содержит owner-approved bounded L1B bet с проверяемым outcome, appetite, kill_by, forecast и against.
  2. Scope L1B явно покрывает только пять назначенных observation-seam families и имеет реальные cuts.
  3. Evidence bar различает instrumentability L1a от Unity/gameplay/M1 delivery и сохраняет L1a/v22 truth.
  4. No-cap cross-bet route и 24.07 control review сохранены без расширения одной ставки.
  5. Первая работа следующей ставки имеет ready CALL; до approval этой shape-сессии продукт не меняется.

return: |
  RESULT с owner-approved L1B bet и ready первым CALL либо checkpoint без активации, если ставка не принята.

budget: one owner-present shape session
surface: any

END_OF_FILE: live/indie-game-development/work/c-shape-near-gas-l1b-001-call.md
