RESULT s-life-reset-setup-product-repo-001 (owner architecture decision, applied)
direction: life-reset   play: frame (charter touch)   node: g-lr-run (active bet)

outcome: |
  The life-reset manager RUNTIME gets its own PRODUCT REPO. The owner argued for a separate
  repo and explicitly invited refutation ("ты можешь критиковать… если убедит — окей"). I
  tried to hold my prior "build here, port later" deferral and it did not survive: I had
  CONFLATED "a separate repo" with "heavy infrastructure". What invalidated the old tree
  (2026-06-20) was building a heavy runtime (DATA_MODEL/MEMORY/RETRIEVAL) BEFORE any use —
  not a folder. A repo can be two markdown files. So I conceded with reasons. The owner's
  distinction is correct and is already the OS pattern: governance (charter/tree/bets/history)
  ≠ the running product; every other direction (GasCoopGame, health-ai, solmax) keeps its
  product in its own repo, and life-reset's product_repos was simply empty. The one nugget
  that survived from my side — LIGHTNESS — is carried as a hard rule on the new repo.

evidence: |
  - Product repo created + pushed: github.com/ainazemtsau/life-reset-manager (owner created
    the empty remote; I initialized local C:\projects\life-reset-manager on main, README only,
    commit d9115dc, pushed). markdown-only scaffold — no infra.
  - CHARTER.md: product_repos filled with the repo + `holds` (runtime + memory, NOT
    governance) + `lightness_rule` (markdown-only until a real run earns more); owner_approved
    evidence += the G9 line ("конечно, нужен отдельный репозиторий…" → "создал репозиторий…
    (дальше ты сам)").
  - Governance stays in live/life-reset/; the runtime is bridged by executor/work CALLs +
    commit evidence (the native G4 source-boundary mirror), as with the other directions.

state_changes: |
  CHARTER.md:
    - product_repos: [] → the life-reset-manager repo, with holds + lightness_rule.
    - owner_approved.evidence += the separate-repo + lightness-rule G9 approval line.
  NOW.md:
    - active_bet += runtime_home (the 2 v1 files + manager memory live in the product repo,
      not live/life-reset/work/; markdown-only).
    - tasks t-2, t-3 done_when: re-pointed to the product repo (commit SHA = evidence).
    - next CALL (t-2): context/boundaries/done_when re-pointed to the product repo + the
      lightness_rule; output committed/pushed there, RESULT carries the SHA.
  LOG.md: appended the 2026-06-21 frame (charter touch) line.
  history/: this file.
  Product repo (github.com/ainazemtsau/life-reset-manager): new README.md (commit d9115dc).
  (No TREE change; g-lr-run unchanged in scope — only the product's HOME is set.)

captures:
  - The "build here then port" instinct was a real anti-pattern of MINE this time — a repo is
    an address, not infra. Keep the distinction: defer heavy BUILD, not a cheap folder.

decisions_needed: []   # owner already decided (separate repo) + approved the package (created the remote, "дальше ты сам").

play_check:
  - "1 (owner argument): the owner made the case for a separate repo and invited refutation; I steelmanned the deferral, found my reason was a conflation (repo ≠ infra), and conceded with reasoning — not capitulation (held the lightness line). His words are the basis (G9)."
  - "2 (charter change, G9): CHARTER product_repos + lightness_rule changed only with explicit owner approval — 'конечно, нужен отдельный репозиторий' + 'создал репозиторий … (дальше ты сам)'; recorded in owner_approved.evidence."
  - "3 (apply): product repo initialized + pushed (d9115dc); governance re-pointed; t-2/t-3 + next CALL updated; committed."

log: "frame (charter touch, owner G9): manager runtime moved to its own PRODUCT REPO (github.com/ainazemtsau/life-reset-manager; local init + README pushed, d9115dc). Owner overturned my build-here-then-port deferral — I'd conflated 'separate repo' with 'heavy infra'; governance stays in live/life-reset/, runtime + memory in the product repo, bridged by CALLs + commit evidence (native OS pattern; product_repos had been empty). Carried lightness_rule = markdown-only until a real run. t-2/t-3 re-pointed. next unchanged c-life-reset-run-v1-t2-sealed-core-001."

next: |
  CALL c-life-reset-run-v1-t2-sealed-core-001  (unchanged target; now writes to the product repo)
  to: session
  direction: life-reset
  play: work
  node: g-lr-run
  task: t-2
  goal: |
    Author the sealed-core file ONCE (the manager's non-amendable safety layer) IN THE PRODUCT
    REPO (C:\projects\life-reset-manager), listing: the inviolable override path (incl. R11
    refusal) · the protected class (recovery/safety/floors incl. routine-rest) · manual
    git-revert rollback · "rules change only via the gate" · the 4 floor-tripwires (sleep /
    not-smoking / no-binge / not-vanishing) · the non-punishing-return invariant (hosted HERE) ·
    CLINICAL-RISK ROUTING (a pre-named clinical-risk sign → route OUT to professional support,
    never intensify discipline). v1 runs NO rewrite; this only authors the core + a 2-assertion
    hand-run smoke check.
  context: |
    - WRITE in the PRODUCT REPO C:\projects\life-reset-manager (remote
      github.com/ainazemtsau/life-reset-manager); markdown-only; commit + push; RESULT carries
      the commit SHA back to this direction.
    - live/life-reset/NOW.md (the v1 bet; runtime_home; resolved_gaps; t-2 spec)
    - live/life-reset/work/life-reset-v1-plan-audit-001.md (the t-1 audit: build-ready + the fix)
    - live/life-reset/work/life-reset-implementation-research-v1.md (Q4/Q5/Q9 mechanics)
    - live/life-reset/CHARTER.md (G1-G4; product_repos lightness_rule; clinical-risk routing)
  boundaries: |
    Co-create with the owner — the CLINICAL-RISK SIGNS + what "professional support" means are
    owner-content (his signs, his words); do NOT invent generically. markdown-only, no infra.
    Author ONLY the sealed core (week-file is t-3). NO rewrite engine (g-lr-learn). No surfaced
    numbers (G2). Override path inviolable; non-punishing-return lives in the core; clinical-risk
    routes OUT. Keep it a short readable file, not bureaucracy.
  done_when: |
    The sealed-core file exists in the product repo (committed + pushed; evidence = commit SHA),
    listing all of the above incl. clinical-risk routing with owner-co-created signs, + a
    2-assertion hand-run smoke check. next = t-3 (week-file template).
  return: RESULT with the sealed-core file (product-repo SHA), the smoke check, next = t-3 CALL.
  budget: one work session (co-creation with the owner).

---

Product repo: https://github.com/ainazemtsau/life-reset-manager  (local C:\projects\life-reset-manager)
Governance (this direction): live/life-reset/ — CHARTER.md product_repos, NOW.md runtime_home.

END_OF_FILE: live/life-reset/history/2026-06-21-s-life-reset-setup-product-repo-001.md
