# s-decide-003 — owner decisions on temperature↔gas (defer feedback + inter-layer read architecture)

Session: decide (owner G7 design resolution) · direction indie-game-development · node g-9c41 (Wave 2) ·
parent s-converge-verify-001 (the BLOCKED-close verify surfaced the temperature/feedback question) ·
2026-06-16 · surface: claude/cli (voice + text conversation).

A design conversation followed the converge-verify BLOCKED close (Finding F2 = XL1 crit-10 feedback vs the
locked pure-sink proofs). The owner thought aloud about what temperature IS architecturally and how layers
with different coordinate systems should read each other, asked for critical/skeptical engagement, and
confirmed two decisions («все понятно со всем полностью согласен»). Recorded here + threaded into the pending
CALLs; no TREE/§CONTRACTS edits here (those happen in c-shape-wave2 / c-converge-003 under their plays + G9).

## RESULT

```RESULT
to: writer
direction: indie-game-development
play: decide
node: g-9c41 (Wave 2)
parent: s-converge-verify-001

outcome: |
  Owner resolved two tightly-coupled design questions raised by verify Finding F2, after a critical design
  conversation: (1) DEFER the temperature→gas FEEDBACK to a later wave (post-g-d3a8), keeping temperature a
  live network-consistent SINK at Wave-2 scale; (2) CONFIRM the inter-layer read architecture = grid as the
  shared address space + ownership map + event bus + revision/commit clock (NOT a data router), with each
  layer publishing events (push) + a read-model (pull) in grid-coords on a committed revision. Consequence:
  F2 largely dissolves (no feedback → temperature stays a sink → locked C21/§T12 hold, no new GridEventKind),
  so c-converge-003 shrinks to mainly F1 (coarse-tier replication); crit-10 is re-scoped honestly (feedback
  NAMED as deferred, the rewording is the shape's G9 job).

evidence: |
  - Decision is owner-confirmed in-session («все понятно со всем полностью согласен») after explicit critical
    analysis (the agent steelmanned both keep-vs-defer and the grid-as-router-vs-addresses options).
  - Defer rationale: the per-gas-type heat rule is GAME DESIGN worked in parallel (g-d3a8 / canon track);
    building it now = guaranteed rework (RESOLVED-3 minimal-impl principle). Nothing in the Wave-2 spine
    depends on it. Safe to defer: the new risk it adds (a consistency error propagating across a layer
    dependency) is the same locked machinery + surfaces cleanly via the existing host==client hash test the
    moment real feedback is built — no hidden risk accrues.
  - Architecture rationale: a grid-addressed read-model per source layer collapses N×N pairwise adapters → N
    and handles heterogeneous resolution (temperature answers a per-cell query from per-room storage); reads
    are against a COMMITTED revision (never live mid-tick) → deterministic / network-consistent. This matches
    the already-authored OR1/OR2 (single oracle) + GG2 (sovereignty); the only correction to the owner's first
    "grid routes the data" model is "grid carries addresses + ownership, not the data values".
  - This resolves the verify watch-item ("don't foreclose feedback"): the grid-addressed read seam IS the
    cheap forward constraint that keeps feedback open without wiring it now.

state_changes:
  - file: live/indie-game-development/NOW.md
    edit: decision_inbox — ADD d-tempfeedback-001 (status answered) recording both decisions + the forward
      constraint (the read seam must allow reading another layer's field at any resolution on a committed
      revision; don't optimize the band solver into a corner that forecloses feedback).
  - file: live/indie-game-development/NOW.md
    edit: open_calls — c-converge-003 note: append the UPDATE (F2 largely dissolves given the deferral;
      repair = mainly F1 + re-scope XL1 to sink-consistency-at-scale + the grid-addressed read-ready seam,
      feedback not required this wave).
  - file: live/indie-game-development/NOW.md
    edit: open_calls — c-shape-wave2 note: replace the crit-10 "require FEEDBACK" steer with the re-scope
      (feedback DEFERRED to a named later wave; Wave 2 requires sink consistency at coarse scale + the
      read-ready seam; name the deferral, don't silently drop it).
  - file: live/indie-game-development/LOG.md
    edit: append one line for this session.
  - file: live/indie-game-development/history/s-decide-003.md
    edit: create — this file.

captures:
  - "Inter-layer read architecture (grid = addresses + ownership + bus + commit clock; per-layer read-models;
     read committed revisions; push=events / pull=queries) is a reusable design fact — candidate for a
     §RESOLVED entry in work/converge-g-9c41.md at c-converge-003, and for knowledge/ promotion at review/pulse."
  - "Destructibility scope for Wave 2 vs later (wave_plan puts full destruction at Wave 4+; a controlled breach
     already works from Wave 1) is a shape-scope question for c-shape-wave2, not resolved here."

decisions_needed: []   # this RESULT records owner decisions already made; nothing outstanding to the owner

play_check:
  - "open: input = owner confirmation of two design decisions from a post-verify conversation; read NOW.md +
     the converge-verify findings; resolved against the LOCK facts + existing contracts (OR1/OR2/GG2)."
  - "work: captured the two decisions; verified they dissolve F2 and keep the architecture feedback-ready;
     threaded into the two pending CALLs; left TREE/§CONTRACTS rewording to the proper sessions (G9)."
  - "close: state recorded via NOW.md decision_inbox + open_call notes + this history file; next unchanged =
     c-shape-wave2 (spine) with c-converge-003 ready in parallel, both now carrying the deferral steer."

log: "indie-game-development decide g-9c41 Wave-2: owner DEFERRED temperature→gas feedback (post-g-d3a8; temperature stays a consistent SINK at scale; crit-10 re-scoped honestly) + CONFIRMED the inter-layer read architecture (grid=addresses+ownership+bus+commit-clock NOT a data router; per-layer read-models, read committed revisions; matches OR1/OR2/GG2). Verify F2 largely dissolves → c-converge-003 shrinks to mainly F1 (coarse-tier replication). d-tempfeedback-001 answered."

next: |
  Unchanged: NOW.next = c-shape-wave2 (the bet spine), with c-converge-003 (the contract repair, now mainly F1)
  ready in parallel. Both pending CALLs now carry the temperature-feedback deferral + the inter-layer read
  architecture steer. No new CALL minted by this decide session.
```

END_OF_FILE: live/indie-game-development/history/s-decide-003.md
