RESULT s-health-nutrition-reset-001 (call: owner-message-2026-06-13-reset-node-for-converge)
direction: health   play: repair   node/task: g-health-nutrition-system

outcome: |
  The nutrition node is RESET. Owner tested the v1 chat-first system live and it asked him
  "how many meals per day?" — revealing that the v1 approach is wrong: it offloads expert
  decisions to the owner instead of researching and deciding them. A first-pass converge
  analysis (this session) confirmed the defect is STRUCTURAL, not a wording slip.

  Owner instruction: do NOT run converge in this chat — just update Direction OS state to reflect
  the decision to restart the node, record that v1 did not work, and set up converge to run in a
  FRESH chat. This RESULT does exactly that (no converge run here).

  State now: active_bet none; node g-health-nutrition-system back to `parked`; NOW.next is the
  converge CALL `c-health-nutrition-converge-001` with everything marked dirty; the v1 product
  (repo health-ai) and all prior decisions are input evidence only, never authority.

evidence: |
  Contradiction (repair step 1): NOW/TREE held v1 as active/shipped (repair s-health-nutrition-repair-001),
  but the owner decided v1 did not work and the node must restart from scratch.

  Reconstruction (repair step 2): v1 = product repo health-ai (commit 27ff409, director + flat
  setup-gate). Live test surfaced the failure: the setup-gate asked the owner "сколько приёмов
  пищи в день" — an expert decision. Two independent converge first-pass agents this session
  located the same root cause: no typed boundary between owner-only facts and system-decided
  expert variables, so the flat gate structurally forces asking. Findings saved (dirty) at
  live/health/work/converge-health-nutrition-input.md.

  Owner instruction (repair step 4 / G9 for the TREE change), exact words:
  "надо, чтобы ты сейчас записал состояние ... ресетнул вот этот наш подход, написал, что вот
  этот не работал ... чтобы мы эту ноду обратно начали. Мы будем это делать в новом чате ...
  обновить стейт, чтобы сделать его актуальным по нашим решениям, а не проводить вот этот конверч".

owner_approved: true
approval_evidence: >
  Owner directly instructed the reset and the node return-to-start ("ресетнул вот этот наш подход
  ... чтобы мы эту ноду обратно начали ... обновить стейт ... а не проводить вот этот конверч").
  This approves: TREE g-health-nutrition-system active -> parked; active_bet cleared; next = converge CALL.

state_changes: |
  NOW.md:
  - active_bet -> status none, with a note recording the v1 reset + structural defect + dirty mandate.
  - tasks -> [] (t-1/t-2/t-3 from the prior repair are dropped).
  - decisions -> [] ; recurring -> [] ; open_calls -> [].
  - next -> CALL c-health-nutrition-converge-001 (play: converge, fresh chat, everything dirty,
    pointer to the dirty input doc, owner's research-and-decide bar).

  TREE.md:
  - g-health-nutrition-system: status active -> parked; dropped appetite and kill_by (no active bet).
    Reset rationale lives in NOW.note + LOG + this history (kept TREE node schema-clean).
  - Other nodes unchanged. g-health-ai-core stays done (its artifacts are dirty input for converge).

  CHARTER.md:
  - No change. product_repos still lists health-ai — the repo exists and will be reworked; its
    CONTENT is dirty, but it remains the product home.

  LOG.md:
  - Appended the reset line -> history/2026-06-13-s-health-nutrition-reset-001.md.

  work/:
  - Added live/health/work/converge-health-nutrition-input.md (DIRTY first-pass converge analysis,
    explicitly non-authoritative input for the converge chat).

captures:
  - The v1 failure pattern to feed converge: "system asked an expert question (meals/day) it should research and decide" -> the fix is a typed owner-fact vs system-decided boundary (research-and-decide by default).
  - Architecture recommendation to refute in converge (NOT adopt): Option E (typed split + generated plan artifact + per-process depth specs + thin router).
  - 4 evidence-base gaps still open for round-2 research inside converge: tracking precision, maintenance-vs-regain predictors, calorie floor / red-flag list, recalc / diet-break cadence.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done. NOW/TREE held v1 active/shipped; owner decided v1 failed and the node restarts.
  - 2 Reconstruct: done. v1 repo + live-test failure + two converge agents located the structural defect; findings saved as dirty input.
  - 3 Propose corrected state: done. NOW reset (bet none, tasks [], converge next), TREE node -> parked, each change justified.
  - 4 Confirm (owner): done. Owner directly instructed the reset and "update state, do not run converge here" — quoted in evidence.
  - 5 Friction: no NEW OS-rule defect — this is a product-v1 design failure handled by re-running converge; the underlying "built without deep derivation / self-cert" pattern is already logged (os/FRICTION.md, 2026-06-13). No duplicate line added.

log: "reset: v1 nutrition approach did not work (asked owner expert questions; structural defect); node -> parked, all v1 dirty; next = converge from scratch in a fresh chat."

next: |
  CALL c-health-nutrition-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-nutrition-system
  goal: |
    The nutrition system node is converged from scratch into a closed, owner-signed WHAT spec for a
    professional, research-and-decide nutrition system — ready for shape.
  context: |
    RUN IN A FRESH CHAT. Treat everything as dirty (product repo health-ai, evidence-base numbers,
    architecture, all prior decisions = input evidence only; import nothing as born-closed; auto-fill
    nothing). Owner's bar: research-and-decide everything expert (meals/day, timing, macros, food),
    ask only irreducible personal facts (allergies/dislikes/budget/cooking-time/equipment), each
    process deeply worked out, chat-first, GitHub source of truth, owner never edits files, extensible,
    not procrastination, light tracking, guarded safety. Dirty first-pass analysis at
    live/health/work/converge-health-nutrition-input.md (candidate set to refute, NOT answers).
    Read os/plays/converge*.md + os/docs/converge-design.md + live/health/CHARTER.md + TREE.md.
  boundaries: |
    Full converge with owner gates; do not skip questions. Nothing imported as authority. Converge only
    (then converge-arch, converge-verify, then shape). No raw daily data in Direction OS; no prescriptions.
  done_when: |
    work/converge-g-health-nutrition-system.md: triage, signed glossary, closed cited §WHAT, the
    research-and-decide principle ratified, coverage complete; next = converge-arch then converge-verify.
  return: |
    RESULT with the converge spec surface, owner §SIGNOFFs, decisions_needed, and next CALL or awaiting_decision.
  budget: converge movement (may span sessions; owner gates batched <=3)
  surface: fresh chat (Claude Code or ChatGPT/Claude project)

END_OF_FILE: live/health/history/2026-06-13-s-health-nutrition-reset-001.md
