# A law that has not been computed must not be frozen

accepted: 2026-07-31
source: review g-37a1 — history/2026-07-31-s-review-g-37a1-obsolete-concept-change-001.md; the witness is product commit `a3fc1546` in GasCoopGame
status: current

fact: |
  The single most expensive failure of g-37a1 was structural, not conceptual,
  and it will recur under any concept that has a simulation in it.

  The 29 July plan froze a gas transfer law whose load-bearing derivation was
  admitted UNPROVED in the plan's own text — §8 said the descent argument
  "must be discharged as a written proof at PAIR-CANDIDATE, not asserted" — and
  §7 named its failure a STOP. It was frozen anyway. Two hours and forty-three
  minutes later one commit, `a3fc1546`, carried 3,162 lines of tests, fixtures,
  negative controls and a measurement harness written against that law AND the
  383-line proof that refutes it. Everything downstream was void.

  Two details make this a law rather than an anecdote. First, the refutation
  needed no run at all: it substitutes an inequality the plan itself had already
  derived and takes five lines of algebra — it was available at PLAN. Second,
  the rejected alternative was the RIGHT one: the plan struck an explicit
  threshold on the ground that it "inherits the same conductivity dependence",
  which confused face conductivity with a cell's face count; the true bound is
  a constant. The owner signed a menu whose correct option had been removed by
  a substitution error.

  The rule that follows: if a leg asserts a bound, a law or a ground that
  nobody has executed, that claim is computed FIRST — a throwaway harness under
  `_scratch/`, an hour, a number — and only the measured result is frozen. This
  route is already legal and already has committed precedent in the product;
  it was simply not taken.

read_by: |
  Any session issuing an engineering CALL whose `done_when` contains a law,
  bound, threshold or invariant that has not been run; and any PLAN stage
  about to freeze one. If the plan is writing the words "to be discharged
  later", stop and discharge it now.

END_OF_FILE: live/indie-game-development/knowledge/compute-a-law-before-freezing-it.md
