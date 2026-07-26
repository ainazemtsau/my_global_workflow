# s-decide-005 — g-9c41 Wave-2 t-1: Codex P1 (buoyancy cross-band eff) disposition + kill-gate verdict confirm

- **date:** 2026-06-17
- **play:** decide (session→writer, agent CLI on this repo)
- **node/task:** g-9c41 / Wave 2 / t-1 (executor leg c-exec-005, GasCoopGame)
- **input:** owner relayed the GasCoopGame executor's status — a Codex review found a P1 on the
  rebuilt coarse buoyancy settle; the executor refused to snap-fix it, ran a 4-lens analysis, concluded
  the code is correct + Codex's fix would introduce an oscillation, recorded the disposition in
  ADR-0005 §Verdict, and HELD for the owner's verdict confirmation + dev→main merge-go. Owner: «принимаю
  твою рекомендацию», + «обязательно занести, что каждый газ должен нести свою температуру, чтобы не забыть».

## Decision (owner, this session)

**Codex P1 = spec-clarity, NOT a code bug. No code change. Kill-gate verdict CONFIRMED → merge-go.**

1. **No code change.** The t-1 rebuild's `CoarseBandStep.Settle` fills the lower band densest-first in
   species-id order, throttled by the LOWER band's OWN temperature (capacity-fill + overflow,
   d-fillmodel-001). This is the COHERENT model and matches d-fillmodel-001 ("layer by density, heaviest
   at the bottom"). Codex's suggested fix (sort the floor by per-species CROSS-band `eff`) is REJECTED:
   temperature is a per-BAND-cell property, so a cross-band per-species sort has NO fixed point — a
   period-2 oscillation. Applying the reviewer's advice would INTRODUCE the bug.
2. **Frozen BS4 prose narrowed — at the t-2 SHAPE, not now.** The BS4 parenthetical "a hot heavy species
   inverts past a cold light one" over-specifies that incoherent cross-band behaviour and is UNTESTED (the
   throttle delivers "a hot floor drives gas up"; it does NOT deliver "this gas overtakes that specific
   colder gas"). BS4 is builder-IMMUTABLE/frozen → the narrowing is a PLANNER action at the t-2 shape
   (owner present), NOT a t-1 builder edit. ADR-0005 §Verdict already records the disposition + flags it home.
3. **Named future seam (recorded so it is not lost):** true cross-band per-species inversion requires
   **each gas to carry its own temperature** (per-species temperature), not the band's. DISTINCT from the
   per-species buoyancy RATE seam BS4 already names; both sit on the per-species-buoyancy line. Per-species
   temperature is added to the BS4 named seam at the t-2 shape.
4. **Kill-gate VERDICT confirmed.** ADR-0005 §Verdict = PASS_WITH_NITS (198/198, 0 skipped; mutation
   76.76% ≥70; boundary 0/0; `-Deliver` green; fresh-session G5 PASS `failedHalf:none`; owner
   multi-quantity legibility PASS). Owner CONFIRMS → dev→main merge-go (NIT checklist below).

## Evidence (independent verification — not taken on the executor's word, per G5 discipline)

- Read `Assets/GasCoopGame/Core/Field/Coarse/CoarseBandStep.cs:187-252`: the settle reads `temp[lowerCell]`
  (the lower band's own temperature, line 202) for the capacity throttle — never an average; fills species
  0..3 (line 211) justified because MW is descending in species id, so `eff` is monotone in id at a shared
  band temperature ⇒ densest-first == id order, no sort needed.
- Read the frozen eff law (ADR-0005 BS4): `eff(s,cell) = max(1, MolecularWeight[s] − (Temperature[cell] >>
  BuoyancyTempShift))`, `MolecularWeight = {0:64,1:32,2:16,3:8}`, `BuoyancyTempShift = 2`.
- Re-ran the oscillation arithmetic against that law (L25 regime, hot floor=260 / cold ceiling=0):
  `eff(0,260)=max(1,64−65)=1` vs `eff(3,0)=max(1,8−0)=8` ⇒ swap ⇒ `eff(3,260)=max(1,8−65)=1` vs
  `eff(0,0)=64` ⇒ swap back. Period-2, no fixed point — the executor's claim holds.
- ADR-0005 §Verdict (FINAL PASS_WITH_NITS) read in full: gate 198/198, orifice now BS3 capacity-relative,
  transactional-tick atomicity, guard/overflow classes closed, artifact gate split, N1 (`Unsafe.dll.meta`)
  resolved via `skip-worktree`. The "Codex P1" disposition block matches the owner's decision above.

## state_changes (applied)

- `NOW.md` decision_inbox += `d-crossband-inv-001` (status: answered).
- `LOG.md` += the 2026-06-17 decide line.
- **NOT changed** (rides the executor RESULT, not a chat transcript): `t-1`/`c-exec-005` status, NOW.next,
  active_bet. The formal t-1 PASS → t-2 close lands when the executor RESULT comes home.

## next

- Paste-ready instruction returned to the owner for the waiting GasCoopGame executor (confirm verdict +
  accept P1 disposition + pre-merge NIT checklist + merge dev→main, do NOT push, emit the t-1 RESULT home).
- When the executor RESULT lands: a writer applies it → closes c-exec-005 / t-1 (PASS) → t-2 next; carry the
  cross-band-inversion + per-species-temperature seam as a t-2 shaping input.
- Memory: `gascoopgame-buoyancy-perband-ratified` (cross-session record of the disposition + seam).

END_OF_FILE: live/indie-game-development/history/s-decide-005.md
