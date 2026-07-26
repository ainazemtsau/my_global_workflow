# RESULT — s-shape-poligon-m1-001 (2026-07-10)

## Owner summary

Владелец выбрал «А». Ставка g-9c41 пересобрана вокруг Полигона М1: лестница 0–10,
appetite 11 продуктовых легов, три горячие задачи и ранний no-pop kill-test. Линия A
получила отдельный GasCoopGame_core: безопасный read-only A0 может строиться параллельно
Phase 0 только после нулевого overlap-preflight, но не мержится до Phase 0; S4 BUILD ждёт
MERGED Phase 0 + A0. Код продукта и сам worktree эта shape-сессия не трогала.

~~~yaml
RESULT s-shape-poligon-m1-001 (call: c-shape-poligon-m1-001)
direction: indie-game-development
play: shape
node/task: g-9c41 / Полигон М1
outcome: |
  Утверждена владельцем и установлена rolling-wave ставка «Полигон М1»: один end-to-end
  профиль примерно на 150 регулируемых DA-комнат с источниками, tracking, реакциями,
  стеновым проломом, видимыми sleeping-front+S4, полным flood, двумя реальными машинами
  и слабым железом. Appetite = 11 продуктовых легов (ступени 0–10), kill/review =
  2026-07-24 либо исчерпание appetite. Текущих задач ровно три: in-flight Lv-ingest
  Phase 0, параллельный diff-disjoint M1-A0 и blocked M1-A1 no-pop micro-proof.
  Отдельный GasCoopGame_core назначен линии A; merge queue = Phase 0 slot 1 → A0 slot 2
  → A1 slot 3. Production S4 не стартует до MERGED Phase 0+A0.
evidence: |
  Owner verdict: после полного shape-брифа и отдельного простого объяснения качества/
  параллельности владелец выбрал option A дословно: «А». Option A = создать отдельный
  GasCoopGame_core, сейчас параллелить только read-only A0, а S4-код запускать после
  MERGED Phase 0; любой overlap с Phase 0 → STOP.
  Approved shape artifact: work/poligon-m1-shape-2026-07-10.md.
  Fire-ready A0: work/c-exec-poligon-a0-001-call.md — outcome-goal, ≤half-day,
  CREATE/VERIFY core-worktree, overlap gate, byte-neutral evidence, LAUNCH и merge slot 2.
  Ready-on-deps A1: work/c-exec-poligon-s4-opening-001-call.md — one-region exact/no-pop
  micro-proof, cheap digest, owner-eye, explicit cut of production rollup/auto-partition,
  LAUNCH и merge slot 3.
  Durable venue map updated: knowledge/g9c41-lanes-venues.md. TREE/CHARTER/SPEC unchanged.
  Writer pre-apply re-sync caught and preserved concurrent commits through
  s-work-canon-process-v3-publish-002; working diff passed git diff --check, and every
  written file carries its END_OF_FILE trailer.
  Honest boundary: product worktree is NOT created by this OS shape session. A0 executor
  creates/verifies it before code. Product base a644e5db is only the last verified live-state
  SHA; A0 must fetch/§Re-sync and record the actual tip.
state_changes: |
  live/indie-game-development/NOW.md:
    - updated-by → s-shape-poligon-m1-001.
    - bet replaced by approved Polygon M1 goal, appetite, dated/metric kill_by, forecast,
      against, cut_list and all six charter-lens verdicts; full ladder points to
      work/poligon-m1-shape-2026-07-10.md.
    - tasks replaced by exactly three hot tasks: Lv-ingest active; M1-A0 open; M1-A1
      blocked until Phase 0 MERGED + A0 MERGED.
    - open_calls add c-exec-poligon-a0-001 (lane A/core, diff-disjoint, merge slot 2) and
      c-exec-poligon-s4-opening-001 (blocked deps, merge slot 3); all concurrent existing
      open_calls preserved.
    - next → one-line pointer to work/c-exec-poligon-a0-001-call.md.
  live/indie-game-development/knowledge/g9c41-lanes-venues.md:
    - lane A venue → C:\projects\Unity\GasCoopGame_core (branch core).
    - hard rule adds owner-approved narrow A0 exception: only new read-only diagnostics/API
      + tests after zero-overlap report; any shared/hot file STOP; merge waits Phase 0.
    - core-worktree creation/verification/rebase checklist added.
  live/indie-game-development/work/:
    - add poligon-m1-shape-2026-07-10.md.
    - add c-exec-poligon-a0-001-call.md.
    - add c-exec-poligon-s4-opening-001-call.md.
  live/indie-game-development/LOG.md:
    - append the s-shape-poligon-m1-001 line.
  writer:
    - save this full RESULT to history/2026-07-10-s-shape-poligon-m1-001.md and commit.
captures:
  - c-lab-p0-001, c-prep-net-spike-001 и c-repair-watchmen-001 остаются готовыми
    параллельными артефактами из s-lanes-install-001; NOW.next теперь по схеме хранит
    ровно один приоритетный CALL, A0.
  - A0 может честно вернуть STOP/checkpoint, если executor обнаружит требуемое касание
    Phase-0 diff или hot Core; это quality gate, не провал параллельности.
  - Direct product-repo preflight из OS-сессии был заблокирован safety hook; поэтому
    никакая существующая/свободная ветка core здесь не выдумана — проверка первая в A0.
decisions_needed: []
play_check:
  - "1 recite: done — g-9c41 representative networked co-op scene и родительский released Steam-product исход предъявлены."
  - "2 appetite first: done — предложены 11 продуктовых легов и review 2026-07-24; владелец выбрал «А» после разъяснения."
  - "3 approaches: done — сравнены S4-first, level-first, fully-fine cut и monolith; владелец выбрал «А» = S4-first с отдельным core-worktree."
  - "4 scope hammer: done — реальные cuts: damage, full destruction/floor breach, content roster, mission/production UX, save/late-join/host-migration."
  - "5 lens sweep: done — verdict дан по всем шести CHARTER lenses в NOW и shape artifact."
  - "6 riskiest assumption: done — top risk = exact/no-pop fine↔collapsed handoff; M1-A1 тестирует его до большого уровня."
  - "7 tasks: done — три задачи: существующая Phase 0, новый ≤half-day A0 и blocked ≤half-day A1; merge slots 1→2→3."
  - "8 kill criteria: done — immediate A1 gate + 2026-07-24/11-leg review + 50/100 ms performance thresholds; true/false branches записаны."
  - "9 close (owner): done — фактические слова владельца: «А»."
  - "triage: reshape of already-active g-9c41 — converge OFF — because Polygon M1 is an owner-selected rolling-wave refocus inside the same already-converged node; no TREE activation/retargeting."
log: |
  2026-07-10 — shape (g-9c41/Полигон М1, s-shape-poligon-m1-001): владелец «А» —
  ставка пересобрана в лестницу 0–10 с appetite 11 легов; отдельный GasCoopGame_core
  открывает diff-disjoint A0 параллельно Phase 0, S4-build ждёт MERGED Phase 0+A0,
  merge slots 1→2→3. → history/2026-07-10-s-shape-poligon-m1-001.md
next: |
  CALL c-exec-poligon-a0-001 → work/c-exec-poligon-a0-001-call.md
~~~

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-shape-poligon-m1-001.md
