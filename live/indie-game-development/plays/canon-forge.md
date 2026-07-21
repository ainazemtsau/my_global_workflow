# Play: local/canon-forge — Canon Forge v3

status: ACTIVE
installed_on: 2026-07-12
owner_verdict: "УСТАНОВИТЬ V3 КАК ДЕЙСТВУЮЩИЙ ПРОЦЕСС"

Purpose: |
  Управлять единым переходом от Minimum Game Frame к owner-selected answer
  и отдельному owner-present canon
  admission. Тип вопроса определяет формат ответа. Selection, authority,
  canon admission и evidence остаются
  разными переходами.

Authority:
  - This play is the sole active design-to-canon route.
  - Canon Forge v2 is removed from live routing and is not a fallback.
  - Gates F/Q and text-candidate discipline come from:
    live/indie-game-development/work/
    canon-process-v3-paper-only-pilot-brief.md
  - Visual questions follow the current canon card:
    canon/c-003-visual-development-contract.md
  - For an explicit visual question, c-003 replaces only the pilot
    brief's text-only format restriction. Both gates and all authority
    transitions remain unchanged.
  - Current owner instruction and Direction OS state outrank stale
    sources.

Reads:
  - live/indie-game-development/NOW.md
  - live/indie-game-development/CHARTER.md
  - live/indie-game-development/TREE.md
  - live/indie-game-development/work/
    canon-process-v3-paper-only-pilot-brief.md
  - the current Minimum Game Frame and exact question artifacts named by
    the active CALL
  - canon repository:
    CONSTITUTION.md, CORE.md, INDEX.md, QUEUE.md,
    canon/c-003-visual-development-contract.md and directly relevant
    canon cards

Hard boundaries:
  - One Forge; format follows question.
  - Use text, diagram or sequence when sufficient. A visual question
    named by the active CALL may use c-003 formats and must obey c-003.
  - No Unity scene, greybox, runtime A/B build, setup, playtest, tuning,
    implementation or production-asset work.
  - No candidate generation before both FRAME READY and QUESTION READY.
  - A blocked gate stays on the same missing basis or question.
  - An OWNER-SELECTED PAPER ANSWER or OWNER-SELECTED PLATE is not canon.
  - Canon admission requires a separate owner-present verdict on the
    exact selected artifact.
  - No question auto-starts from QUEUE.md.
  - No process or canon mutation occurs before its owner verdict.
  - Stale v2 files, old chats and git-history text have no live authority.

Steps:
  1. Authority and scope:
     load the active CALL, current frame, process specification and current
     canon sources; state exactly what is and is not being decided.

  2. Gate F:
     establish or verify the current owner-readable Minimum Game Frame.
     Return FRAME READY, FRAME REVISED or FRAME BLOCKED with the owner's
     words recorded verbatim.

  3. Gate Q:
     for one sourced current question, establish frame location, exact
     unresolved player decision, provenance, why-now, blockers, entity
     meanings and non-scope. Return QUESTION READY or QUESTION BLOCKED with
     the owner's words recorded verbatim.

  4. Candidate comparison:
     only after both gates pass, choose the minimum useful format.
     Define local criteria and a shared situation when useful; generate
     privately, hard-kill weak directions and show one explanatory artifact
     or 2–3 comparable candidates.
     Visual work follows c-003. Otherwise return BLOCKED honestly.

  5. Owner selection:
     record the owner's exact words. Save the selected text answer or
     plate with its rules, placeholders, non-binding details, production
     check and unverified dimensions. It is paper/visual authority, not
     canon.

  6. Canon admission:
     run only as a separate owner-present CALL over one exact existing paper
     artifact. Allowed verdicts are ADMIT TO CANON, HOLD PAPER-ONLY or
     REJECT AS CANON CANDIDATE. No branch opens another design topic or
     implementation task.

  7. Close:
     emit one RESULT. The session never edits repositories directly.
     A writer applies only the owner-approved state/process/canon diff.

Done when:
  The active CALL reaches its bounded owner verdict; format matches the
  question; Frame and Question gates, owner selection, paper/visual
  authority, separate canon admission and evidence remain explicit; no stale
  route auto-starts; the RESULT cites every owner step verbatim.

Postconditions:

- The play remains the single Canon Forge.
- The play remains within the local-play 600-word budget.
- The paper-only pilot brief governs Gate F, Gate Q and text comparison.
- c-003 changes only the allowed format for an explicit visual question.

END_OF_FILE: live/indie-game-development/plays/canon-forge.md
