# RESULT s-work-poligon-a0-build-call-001 (call: owner-message-2026-07-10-poligon-a0-build)

Отдельный BUILD-only handoff для M1-A0 готов. Он сохраняет leg-id
`c-exec-poligon-a0-001`, но запускается новым packet-файлом строго от owner-approved
frozen PLAN commit `f80bf700c26376edb7965eef3481cc04607834c3`. BUILD начинается с отдельного
independent RED-first test-author; merge остаётся запрещён до MERGED Phase 0,
post-rebase полного прогона и binding fresh G5.

~~~yaml
RESULT s-work-poligon-a0-build-call-001 (call: owner-message-2026-07-10-poligon-a0-build)
direction: indie-game-development   play: work   node/task: g-9c41/M1-A0
outcome: |
  Для c-exec-poligon-a0-001 существует отдельный FIRE-READY BUILD-only CALL: он
  закрепляет exact frozen PLAN/base f80bf700c26376edb7965eef3481cc04607834c3,
  owner-ack:owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved,
  независимого RED-first test-author до production-кода и hard merge dependency
  от MERGED c-exec-lv-ingest-phase0-001.
evidence: |
  live/indie-game-development/work/c-exec-poligon-a0-001-build-call.md содержит
  самостоятельный BUILD packet с exact SHA/approval, отдельным RED-author gate,
  исходными A0 acceptance properties, zero-overlap pre/post report и merge slot 2.
  NOW.md open_calls/next указывают на новый packet; оригинальный
  work/c-exec-poligon-a0-001-call.md сохранён как outcome contract и помечен новым
  launch pointer. Фактические слова владельца в этой сессии: «Сформируй отдельный
  BUILD CALL для c-exec-poligon-a0-001 по frozen commit
  f80bf700c26376edb7965eef3481cc04607834c3 в GasCoopGame_core. Учти owner approval
  owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved, обязательный independent
  RED-first test-author и зависимость merge от MERGED Phase 0.»
state_changes: |
  live/indie-game-development/work/:
    - add c-exec-poligon-a0-001-build-call.md as the separate BUILD-only launch packet.
    - prepend c-exec-poligon-a0-001-call.md with the frozen-plan BUILD pointer; preserve
      the original outcome contract beneath it.
  live/indie-game-development/NOW.md:
    - updated → 2026-07-10 by s-work-poligon-a0-build-call-001.
    - M1-A0.done_when pointer → work/c-exec-poligon-a0-001-build-call.md and add exact
      frozen-plan + independent RED-author evidence obligations; status stays open.
    - c-exec-poligon-a0-001.call → work/c-exec-poligon-a0-001-build-call.md; replace note
      with exact SHA/approval, RED-first and Phase-0 merge dependency; id stays pending.
    - next → one-line pointer to work/c-exec-poligon-a0-001-build-call.md.
  live/indie-game-development/LOG.md:
    - append the s-work-poligon-a0-build-call-001 line below.
captures: []
decisions_needed: []
play_check:
  - "1 Recite: done — M1-A0 serves g-9c41 by exposing byte-neutral read-only activity evidence; this leg only prepares its separate BUILD handoff."
  - "2 Owner inputs (owner): skipped — no, the CALL is a machine artifact, not owner-content; actual owner words applied: «Учти owner approval owner-chat-2026-07-10-c-exec-poligon-a0-001-plan-approved, обязательный independent RED-first test-author и зависимость merge от MERGED Phase 0»."
  - "3 Do the work: done — issued a full executor CALL without designing beyond the frozen PLAN; the original c-exec id remains the pending engineering leg."
  - "4 Self-check: done — exact SHA and venue present; approval is exact-plan-only; independent RED precedes production code and builder cannot edit it; BUILD may run in parallel but merge requires verified MERGED Phase 0, rebase, rerun and binding G5."
  - "5 Close: done — M1-A0 remains open and NOW.next launches the separate BUILD packet."
log: 2026-07-10 — work/handoff (g-9c41/M1-A0, s-work-poligon-a0-build-call-001): отдельный BUILD-only CALL c-exec-poligon-a0-001 привязан к owner-approved frozen plan @f80bf700; independent RED-first test-author обязателен, а merge slot 2 остаётся закрыт до MERGED Phase 0 + post-rebase rerun + binding G5.
next: |
  CALL c-exec-poligon-a0-001 → work/c-exec-poligon-a0-001-build-call.md
~~~

END_OF_FILE: live/indie-game-development/history/2026-07-10-s-work-poligon-a0-build-call-001.md
