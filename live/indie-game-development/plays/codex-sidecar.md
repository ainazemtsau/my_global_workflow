# Play: local/codex-sidecar

Purpose: run ONE Codex Sidecar session safely: read-only scout, owner-present Unity Pair-Lab, or Formal Leg preparation/execution. The play protects the active Cloud Code work while letting Codex contribute in small, recorded loops.

Reads: `NOW.md`; `work/codex-sidecar-track-2026-06-30.md`; `work/codex-sidecar/board.md`; product repo `AGENTS.md` when product files may be touched; relevant target files/scenes.

Writes: usually `work/codex-sidecar/board.md` + `LOG.md`; product repo files only inside the declared lock. `NOW.md` changes only when the session opens/returns formal CALLs. Never changes `TREE.md` or `CHARTER.md`.

Precondition: owner names, implies, or accepts a mode and target. Exact commands are optional: free-form owner phrases must be classified into Scout / Pair-Lab / Formal Leg before action. If target/worktree is unclear or overlaps active Cloud Code work, downgrade to Scout or stop with a decision.

## Steps

1. **Mode + target** — classify the owner phrase as `Scout`, `Pair-Lab`, or `Formal Leg`; name target repo/worktree, target scene/files, and what is explicitly forbidden. If the owner did not use a command, say the inferred mode in plain Russian before continuing.
2. **Lock + rollback** — before edits, state the file lock, active Cloud Code conflict check, rollback/checkpoint plan, and the one visible outcome. If this cannot be made concrete, stop.
3. **Plan the smallest move** — for Pair-Lab, one visible change only; for Formal Leg, use the normal engineering contour/OpenSpec and product `AGENTS.md` rules.
4. **Execute / inspect** — do the bounded work or read-only inspection. Do not broaden scope silently.
5. **Validate** — Pair-Lab: compile/play/screenshot/owner-eye as applicable. Formal Leg: runnable checks + RESULT evidence. Scout: source-grounded answer.
6. **Owner-eye gate (Pair-Lab only)** — owner says keep / tweak / revert / promote; record his words. `(owner, conditional)`
7. **Record** — update `work/codex-sidecar/board.md` with mode, target, touched files, evidence, owner verdict where applicable, end state, captures/promotion candidates; append one LOG line if state was written.
8. **Close** — RESULT with `checkpoint`, `promote`, `discard`, `blocked`, or `scout-only`; `next` preserves the main direction flow unless a new explicit sidecar CALL is the requested outcome.

## Done when

One bounded sidecar session is closed; no active Cloud Code work was silently overlapped; evidence/verdict is recorded; ideas are captured or promoted; the main `NOW.next` is preserved unless the owner explicitly asked to route elsewhere.

## Notes

- Pair-Lab is not a product done gate. It is a reversible Unity laboratory.
- Formal Leg is for anything load-bearing.
- If in doubt, choose Scout first.
- Exact trigger commands are optional; natural language is expected.
- A visual "looks better" claim needs owner-eye or before/after evidence.
- A scene tweak that grows architecture becomes a promotion, not a hidden refactor.

END_OF_FILE: live/indie-game-development/plays/codex-sidecar.md
