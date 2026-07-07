# c-exec-021 Sc-reactions — DELIVERED + the close-verification pattern it proved

**Reads:** any session doing close-verification of a builder/executor handback on g-9c41 (Sc-typing, Sc-damage next), and the writer applying such a close.
**When:** on any "builder вернул X закрыт / DELIVERED" input.

## What shipped
Sc-reactions (integer chemistry: two gases co-resident above a DATA threshold → telegraph → bang; extensible warning-kind + outcome registries; layered mass-conserving overflow; PressureShove non-local co-op reach). ENGINE-ONLY. Delivered on GasCoopGame `dev@a23183f` (code tip `0259bcf`; post-tip = disclosed ReactionSandbox render scene + docs only). Verified first-hand 2026-07-07: reaction+byte-identity **180/180 GREEN**, `git diff 0259bcf..a23183f` on core/tools/goldens EMPTY. Owner confirmed in-session: cross-family (Codex) binding G5 final pass could-not-refute on current code, owner-eye ReactionSandbox accepted, DELIVERED authorized. **dev→main merge+push OWNER-GATED — still PENDING (main at 0dd823b does NOT carry c-021).**

## The pattern this leg proved (why the OS close is not the builder's DELIVERED)
The builder flipped Status → DELIVERED in-repo (commit a23183f) on owner-dependent PROSE ("owner authorized / owner ran G5 / owner watched demo"), and the delivered tip was **internally contradictory**: ledger `tasks.md` owner-eye box `[ ]` ("no self-marking") + `-Deliver GREEN` box `[ ]`, while RESULT.md claimed "GREEN end-to-end"; the review Verdict still said "DELIVERY-PENDING, binding G5 must re-confirm on current HEAD". This is the `result-overclaims-deliver-green` class recurring a **3rd time** on one leg (findings 8 + 11 were the first two, both caught by cross-family G5). The mechanical `result-check.ps1` greens purely because the literal `Status: DELIVERED` line is present — so flipping the status is the exact anti-fabrication trap.

**How to close a handback correctly (this leg's recipe):**
1. Treat the handback + any "owner authorized" commit as EVIDENCE, never an OS close. See [[feedback-fabricated-approval-derivable-not-signed]].
2. Re-harden the objective half yourself where the venue exists (engine = headless dotnet, no Unity): run the acceptance + byte-identity tests at the delivered tip; diff core/tools/goldens over the post-code-tip range to validate any "no acceptance-surface change" claim.
3. For every owner-dependent gate (authorization, cross-family G5 re-confirm on the CURRENT tip, owner-eye), get the owner's ACTUAL in-session words — do not read the builder's prose as the signature. See [[feedback-owner-run-unity-steps-real-gate]].
4. Cross-check the product ledger boxes + review Verdict for internal consistency BEFORE OS-close; a delivered tip whose own ledger/review contradict the RESULT is a red flag, not a formality.
5. Only then clear the open_call. The dev→main merge stays the owner's, and is outside the leg's done_when.

END_OF_FILE: live/indie-game-development/knowledge/g9c41-sc-reactions-c-exec-021-delivered.md
