# Executor RESULT — c-exec-020 Sc-weight (per-type vertical buoyancy) — returned HOME 2026-06-30

This is the executor's exit report for the CHARACTER ROAD's slice 2 (Sc-weight), returned to the
direction. Applied by s-work-033 (the OS work-session) after a BINDING fresh-session G5. The full
product-repo exit report is committed at `GasCoopGame:RESULT.md` (main @61b7923).

## Merge facts (verified first-hand, GasCoopGame)

- main @**61b7923** = `Merge c-exec-020 Sc-weight ... into main` (--no-ff).
- merge parent dev = **833433c**; chain: EXEC **95629be** → PLAN-freeze **d265607** → base Sc-types merge **7d08882**.
- Diff `7d08882..61b7923` is ENGINE-ONLY: Core/Field/{Types,Voxel} (5 files), tools/type-hardcode-scan.ps1,
  ADR-0019, openspec/changes/c-exec-020-sc-weight/**, mutation-c-exec-020-sc-weight.json, 6 ScWeight* tests,
  RESULT.md, + additive engine GasBuoyancyDemoScene.unity / BuoyancyDemoDirector.cs. ZERO deletions.
  The parallel dev2 VISUAL track (Render/GasVisual/LabGasViewSource.cs, Render/Contracts/LabGasField.cs,
  ADR-0016) is PRESENT + unmodified on main — the deletions in the raw EXEC diff were a cross-branch artifact
  and did NOT propagate (boundary held).

## Owner-pasted RESULT packet (verbatim)

```
RESULT — c-exec-020 Sc-weight · статус DELIVERED (слито в main + запушено)

outcome: per-type вертикальная плавучесть — тяжёлый тонет / лёгкий всплывает / нейтральный стоит,
ползучим смещением потока (не сортировка); все 10 done_when закрыты с доказательствами.
evidence: dev 833433c → merge origin/main 61b7923 (--no-ff). -Deliver EXIT 0: 979/979 на dev,
1059/1059 на merged-main; мутации 73.23% ≥ 70; сканы (zero-float / int-overflow / type-hardcode);
coverage 10/10; G5 (свежий) — все 10 швов COULD-NOT-REFUTE.
assumptions: тест-веса (±64/0) — данные, не прод; «feel = выраженный» (Cap=64/Denom=128, тюнится
данными); температурный член зарезервирован/занулён.
cuts: нет (температура / скорость-адвекция / реакции / визуал-трек — вне scope по спеке, не срезы).
cost: одна EXEC-сессия (Opus билдер + Sonnet тест-автор + Sonnet G5), 2 прогона мутаций.
manual-acceptance: owner-eye ✅ («работает») + merge ✅ — оба выполнены.
review round (Codex): все 6 находок отработаны (P2#4 фикс кода, P1#3 задокументирован+тест,
P1#2 честно сужен, P2#5/#6 тесты, P1#1 коммит).
next: домой в направление (OS) — следующий CALL = Sc-reactions; билдер карту не заводит.
⚠ В RESULT отмечено: ADR-0019 пересекается номером с визуальным треком — направление перенумерует при кросс-треке.
```

## Owner-ack tokens carried by the product RESULT (no fabricated approval)

- `owner-ack:esc-c-exec-020-test-assertions-2026-06-29` — owner «A»: 3 independent RED assertions over-constrained
  beyond the spec's own tolerance clauses, corrected by the independent test-author to spec tolerance; NO impl /
  flow-law change (same class as c-019's settle-criterion amendment).
- `owner-ack:esc-c-exec-020-codex-review-2026-06-29` — owner «документируем»: Codex P1#3 (sub-quantum low-mass
  no-drift) DOCUMENTED as a spec-silence row + pinning test, not a redesign.

## Binding fresh-session G5 (s-work-033, separate from the EXEC session) — PASS

Workflow wf_ea71e2d6-f1c: 6 adversarial seam-refuters + a live gate-runner + a referee, over the MERGED code at
main @61b7923. Verdict = **PASS_COULD_NOT_REFUTE** on all 10 seams + headless-gate + visual-track-boundary; zero
blocking findings. Live gate re-run: `dotnet test` Core = 1059 passed / 0 failed / 0 skipped (ScWeight 31/31);
zero-float + int-overflow + type-hardcode scans pass RED-control self-tests AND the gate; committed mutation json
= 73.23% (181 killed + 5 timeout / 254 valid) ≥ 70. Far-tier CoarseSpecies/CoarseBandStep git-diff EMPTY.

Two NOTE-ONLY weaknesses (recorded as captures in s-work-033, neither verdict-affecting):
1. ScWeightBuoyancyTests planted-instant-sort sub-assertion is an arithmetic tautology (vacuous test
   DISCRIMINATOR; the no-pop property is still independently guaranteed by face-adjacency + the outflow clamp).
2. owner-eye-checklist.md cites a stale "977 tests" vs the real 1059 (non-gate confidence doc).

END_OF_FILE: live/indie-game-development/history/2026-06-30-c-exec-020-sc-weight-result.md
