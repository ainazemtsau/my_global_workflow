# CALL c-work-near-gas-dashboard-close-002

to: session
direction: indie-game-development
play: work
node: g-9c41
task: NearGas-dashboard

goal: |
  NearGas-dashboard получает доказанный Direction-OS verdict, а направление честно маршрутизирует
  следующий допустимый gas-engineering шаг.

context: |
  Это продолжение checkpoint s-work-near-gas-dashboard-close-001. Текущее состояние:
  live/indie-game-development/NOW.md. Product repo: C:\projects\Unity\GasCoopGame_dev.

  Уже reconciled read-only evidence:
  - product commit 9bc577c7f2c0a068757474cc5ef5cb6f0e47603f, parent f5c1d650;
  - diff ровно AGENTS.md, docs/gas-simulation/dashboard.html,
    docs/results/c-exec-near-gas-dashboard-001.md; git diff --check green;
  - committed dashboard/root rule/source coverage green, эти три пути clean в working tree;
  - сохранённые builder desktop+narrow captures визуально читаемы;
  - все 10 заранее dirty/untracked путей всё ещё присутствуют; product RESULT фиксирует равные
    before/after SHA-256 snapshots.

  Единственный незакрытый гейт: fresh-session in-app Browser запретил file:// dashboard URL и
  одновременно запретил обход через другой browser/CDP/локальный server. Поэтому checkpoint не
  выдал met и не открыл L1.

boundaries: |
  Product repo read-only: ничего не менять, не stage/commit/push. Не обходить browser security policy.
  Не запускать Unity, tests, game build, L1 PLAN/BUILD или visual PLAN/BUILD. Не читать содержимое
  dirty c-visual-009 BUILD. Не закрывать g-9c41 или M1-P2a0. Product RESULT остаётся evidence input.

done_when: |
  1. Committed dashboard 9bc577c7 заново отрендерен и прочитан на desktop 1280×720 и narrow 390×844:
     первый экран читаем, русский UTF-8 корректен, карточки адаптивны, горизонтального page overflow нет.
  2. Render/readback согласован с уже reconciled committed diff, root AGENTS rule, source coverage,
     preservation evidence и сохранёнными captures; найденное расхождение даёт точный blocker, не pass.
  3. При verdict met NearGas-dashboard становится done; закрываются только
     c-exec-near-gas-dashboard-001 и c-work-near-gas-dashboard-close-002; M1-P2a0 и unrelated state
     сохраняются. Следующим готовится, но не запускается, отдельный owner-present PLAN CALL для L1
     c-exec-near-gas-core-authority-001. L1 BUILD не authored и не started.

return: |
  Один Direction RESULT с verdict, evidence по каждому пункту, точными state_changes и следующим
  ready CALL либо точным blocker.

budget: one focused fresh render/close session
surface: any

END_OF_FILE: live/indie-game-development/work/c-work-near-gas-dashboard-close-002-call.md
