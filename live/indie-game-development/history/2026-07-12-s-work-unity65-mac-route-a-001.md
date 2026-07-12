# RESULT — s-work-unity65-mac-route-a-001 (2026-07-12)

## Owner summary

Владелец выбрал вариант `A` дословным ответом «A». Продолжаем exact Unity 6000.5.3f1, принимаем только уже
обнаруженную coordinated несовместимость FishNet scene-handle wire `int -> ulong` и требуем явный
protocol-version rejection gate для mixed builds. Это `revised`, а не разрешение на merge.

Открыт отдельный PLAN-only CALL. Он сохраняет старую frozen историю, заново проектирует независимые проверки и
закрытие всех refutation findings; BUILD, тесты и merge в этой сессии не начинались. Текущие две посторонние dirty
правки product checkout зафиксированы как неприкосновенная граница.

```text
RESULT s-work-unity65-mac-route-a-001 (call: owner-decision-d-unity65-mac-revision-route-001)
direction: indie-game-development   play: work   node/task: g-9c41/d-unity65-mac-revision-route-001
outcome: |
  Owner route A is ratified for the Unity 6000.5.3f1 Mac migration. The accepted revision is narrow: same-version
  peers may use the existing full-width FishNet scene-handle wire change, while mixed protocol versions must reject
  explicitly before incompatible decoding. c-exec-unity65-mac-revision-plan-001 is ready as a separate PLAN-only
  leg. The original c-exec-unity65-mac-001 remains blocked and unmerged; no product BUILD, test, merge or push ran.
evidence: |
  Owner actual words in the current session: `A`.
  Resolution token: owner-ack:owner-chat-2026-07-12-unity65-route-a.
  The option mapping is recorded in
  live/indie-game-development/history/2026-07-11-s-work-unity65-mac-closecheck-001.md:
  A = continue 6.5, accept coordinated FishNet wire break with mandatory protocol-version gate, repair/closeout,
  merge only on green. The same checkpoint records why df1e5ca is not merge-ready and keeps the engineering CALL open.
  Fresh refs on 2026-07-12: workflow main c57843f is one local checkpoint commit ahead of origin/main@2190d7a;
  product committed candidate remains df1e5ca, five commits over origin/main == origin/dev == a644e5db; dev2 is an
  ancestor. Product validation.config and Direction OS CONTRACT_VERSION both read v19.
  Product checkout status is now dirty only at `.vscode/settings.json` and
  `Assets/GasCoopGame/Levels/GasLab/Flow/CoopSmallSGF.asset`; read-only inspection showed local solution-name and
  editor graph-layout changes. This session did not edit, stage, clean or commit them.
state_changes: |
  Create the complete self-contained work/c-exec-unity65-mac-revision-plan-001-call.md artifact, including its
  END_OF_FILE trailer; `next` points to that committed CALL.
  NOW.md: set updated to `2026-07-12 by s-work-unity65-mac-route-a-001`; remove pending decision entity
  d-unity65-mac-revision-route-001; replace only open_calls[c-exec-unity65-mac-001].note with the owner-A/blocking
  wording; add open_calls[c-exec-unity65-mac-revision-plan-001] with its PLAN-only route; explicitly set NOW.next to
  `CALL: work/c-exec-unity65-mac-revision-plan-001-call.md`. Preserve all tasks, recurring, every other open_call and
  decision, and the active bet unchanged.
  LOG.md: append exactly the log line below once.
  work/board/dashboard.html: regenerate the Unity open-work cards, remove the resolved decision from «Ждёт тебя»,
  add its closed outcome, and add the 2026-07-12 journal day; preserve unrelated sections.
  Save this full RESULT once at history/2026-07-12-s-work-unity65-mac-route-a-001.md.
  No TREE.md, CHARTER.md, knowledge, task status, product repo, original CALL file, BUILD, test, merge or push change.
captures: []
decisions_needed: []
play_check:
  - 1 Recite: done — route A means exact 6000.5.3f1 + narrow coordinated FishNet wire break + mandatory version gate; original candidate remains not merge-ready.
  - 2 Owner inputs: done — this is not an owner-content artifact; the sole required owner verdict is present verbatim: `A`.
  - 3 Do the work: done — resolved the pending decision, preserved the original open BUILD as blocked, and authored a self-contained PLAN-only executor CALL with v19 phase separation and dirty-worktree boundary.
  - 4 Self-check: done — the new CALL grants no general network waiver, relabelled test independence, missing-gate waiver, BUILD, Windows work or merge; it maps every close-check class into PLAN done_when.
  - 5 Close: done — decision removed from pending-only NOW, PLAN CALL opened, next routed to it; continuation belongs to a fresh session.
log: 2026-07-12 — work/decision (g-9c41/Unity-6.5 route, s-work-unity65-mac-route-a-001): owner выбрал «A» — продолжать 6000.5.3f1 с узким coordinated FishNet wire break и обязательным protocol-version gate; открыт PLAN-only c-exec-unity65-mac-revision-plan-001, а исходный BUILD остаётся blocked/unmerged до нового owner-approved плана и всех зелёных ворот. → history/2026-07-12-s-work-unity65-mac-route-a-001.md
next: |
  CALL: work/c-exec-unity65-mac-revision-plan-001-call.md
```

END_OF_FILE: live/indie-game-development/history/2026-07-12-s-work-unity65-mac-route-a-001.md
