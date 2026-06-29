# c-visual-002 (S1) RESULT — imported + verified first-hand — unclipped gas-lab + vertical-column jet (RENDER-ONLY)

Imported + verified first-hand 2026-06-29 by s-visual-009 (writer) from the GasCoopGame_dev_2 build session. Source of
truth = GasCoopGame `origin/main` @ the merge `f7efbea`. S1 = the FIRST sub-leg of the gas-lab look-development leg
c-visual-002 (owner-signed split: lab+motion first → the two-type probe rolls to S2). VISUAL track, node g-7e15. RENDER-ONLY.

## first-hand verification (s-visual-009, writer)

- Merge: GasCoopGame `origin/main` = `main` = `f7efbea` (`--no-ff` merge; parents `2117341` (engine main tip, the
  post-S2 hygiene HEAD) + `04a93ea` (dev2 leg tip)). `origin/dev2` = `04a93ea`. EXACT match to the RESULT.
- Deliverables EXIST on `main` (the deliverable-exists invariant — a built-artifact bullet needs real existence, not a
  test name): `Assets/GasCoopGame/Render/GasVisual/GasLabScene.unity` (the unclipped lab scene), `Render/Contracts/
  LabGasField.cs`, `Render/GasVisual/LabGasViewSource.cs`, the independent `tests/GasCoopGame.Core.Tests/Render/
  LabGasFieldEdgeTests.cs`, `docs/measurements/c-visual-002-s1-owner-eye-checklist.md` (the owner-eye sign), and the
  frozen `openspec/changes/c-visual-002-s1-gas-lab/`.
- ADR collision CONFIRMED first-hand: BOTH `docs/adr/ADR-0016-gas-visual-s1-gas-lab.md` AND `docs/adr/
  ADR-0016-s2a-zero-legacy-reconstruction-retirement.md` exist on `main` → the visual ADR series collides by NUMBER with
  the engine ADR-0016 (c-exec-017). The renumber flag the RESULT raised is REAL.
- Deliverable reconciliation vs the CALL's own `done_when` (work/c-visual-002-call.md): every bullet carries a
  disposition (PLAN owner-signed ✅; unclipped-lab existence ✅; characteristic-motion ✅; two-type probe DEFERRED→S2 with
  owner-ack "owner-signed split" — the CALL pre-authorized "lab+motion first → then the two-type probe"; headless «точно»
  ✅; owner-eye binding signed Variant A ✅, natural-jet deferred owner-ack:esc-c-visual-002-s1-natural-jet-deferred-
  2026-06-29; comes HOME ✅). No bounce: the soft-falloff data-side no-rectangle approach MATCHES the CALL's named
  approach; the analytical `LabGasViewSource` is the PLAN-decided "scripted motion source" option the CALL offered, not a
  silent substitution; the 977→923 engine-test baseline shift is from the ENGINE legs (S2a/S2b deletions), NOT this
  visual leg — `git diff Core/**` empty + dev2 didn't touch Core confirms the render-only invariant held.

---

## RESULT (verbatim, owner-pasted from the build session)

RESULT — c-visual-002 S1: unclipped gas-lab + vertical-column jet
Status: DELIVERED + MERGED + PUSHED (2026-06-29). origin/main=f7efbea (--no-ff, parents 2117341+04a93ea), origin/dev2=04a93ea. Owner-signed (Variant A). Branch dev2, VISUAL track, node g-7e15. RENDER-ONLY.

outcome
Построена выделенная gas-lab: один аналитический газ проигрывает spawn-bloom → вертикальную струю-колонну → slow-creep в открытом пространстве, которое НИКОГДА не клипуется в прямоугольник (фикс «блекло»). Гарантия no-rectangle — data-side (мягкий edge-falloff гонит плотность в ровно 0 в наружном margin), поэтому ноль правок шейдера/GPU-layout и ноль правок симуляции. Против done_when S1:

LAB FIELD / NO-RECTANGLE / MOTION / FRONT-DERIVED / FILL-CONTINUITY — headless ✅
LAB VIEW SOURCE + scene (engine) ✅; READ-ONLY / no-sim-change ✅; OWNER-EYE #1 — подписан (Variant A) ✅

evidence
tools/check.ps1 -Deliver GREEN на смёрдженном main: 1003 теста (923 движок baseline + 80 S1 Lab Render), все 5 frozen-папок strong-check OK (c-017 87.96 / c-018 73.51 / cv1-seam 82.54 / cv1-s5 76 / cv2-s1 75.63%), coverage 8/8.
Render-only инварианты: Core/** diff пустой; нет AsyncGPUReadback/.GetData под Render/Adapters; stride-gate зелёный = zero-layout; GasUber шейдер supported. dev2 не трогал Core с merge-base (проверено перед мёрджем).
Артефакты: LabGasField+LabGasViewSource+GasLabScene.unity, ADR-0016 (visual), frozen openspec/changes/c-visual-002-s1-gas-lab/, независимые тесты LAB1–6 + LAB8 (колонна), 5 owner-eye стиллов.
Процесс-качество: 3 раунда owner-run Codex review закрыты (r1 — S6 GasConceptPresets P2/P3 фикс; r2 — P1 spec↔impl капсулы исправлен правильно: спека обновлена + Requirement LAB8 + отдельный независимый test-author, builder-тест удалён; r3 — синхронизация доков); fresh-context validator COULD-NOT-REFUTE 1–6.

assumptions
Газ в лаборатории — аналитический (не сим): цель S1 — судить ЛУК в движении в открытом пространстве, развязанном от стен (реальный sim-swap уже сделан в S5). Движение лаборатории — render-only display, не второй источник правды.
DefaultShape (spawn/jet/радиусы/softness/margin) — builder-tuned look-дефолты + живые ручки; owner реагирует на owner-eye.
Min-spec GPU только НАЗВАН (low-end/integrated); перф-проход DEFERRED (S4, look-first).

cuts
Два типа газа (тяжёлый тонет / лёгкий всплывает через reserved RiseSinkBias) + свет сквозь объём (scatter-glow) = S2 (owner-signed split).
Естественный/клубящийся джет — DEFERRED: колонна растёт как «жёсткая капсула/пластилин», не течёт; owner вывел качественный джет за scope S1. owner-ack:esc-c-visual-002-s1-natural-jet-deferred-2026-06-29.
S4 perf; screen-door/dither текстура (look-polish).

cost
Одна build-сессия (Opus builder + 2 независимых Sonnet test-author'а + Sonnet validator + Stryker + MCP capture). Отдельно не метрилось.

manual-acceptance
Owner прогнал GasLabScene live в Play, подтвердил spawn→jet→creep + НЕТ прямоугольника с любого угла; принял колонну как ожидаемую форму-заглушку S1 (Variant A), подписал docs/measurements/c-visual-002-s1-owner-eye-checklist.md. «весело» excluded; «точно» = зелёный suite.

next (route HOME — planner владеет следующим CALL)
S2 (следующая под-нога c-visual-002): два разнохарактерных газа в одном объёме (heavy-sinks dark&dense / light-rises wispy&pale через reserved RiseSinkBias per-type buoyancy — reserved-field path, без layout-правок) + первый ДИФФЕРЕНЦИРУЮЩИЙ look-рычаг «свет сквозь объём» (scatter-glow, глобальный shader-knob). Owner-signed FEEL + рычаг зафиксированы на плане ([[c-visual-002-plan]]).
DEFERRED natural jet (owner-ack:...-2026-06-29): запланировать настоящий текущий/турбулентный джет (curl-noise advection / формирование из поднимающихся клубов, не растягивающаяся капсула) — кандидат в S2/S6 look-development.
⚠ ADR renumber: визуальный ADR-0016-gas-visual-s1-gas-lab конфликтует по НОМЕРУ с движковым ADR-0016 (c-exec-017) — перенумеровать визуальную ADR-серию (не builder-действие; зафлажено в merge-commit).
S5 follow-up (pre-existing, не S1): GasGridBounds.TexelIndex int-overflow — задокументированное предусловие (guarded MaxGridDim 256³); захардить против raw-bounds = правка frozen S5-кода → отдельная нога.
Возможный look-development pass по лаборатории (dither/шум-полиш, отложенный S3/S5 polish — теперь оцениваемо в движении).

END_OF_FILE: live/indie-game-development/history/c-visual-002-s1-result-2026-06-29.md
