RESULT s-repair-kernel-converge-overclose (call: owner-fix-converge-overclose)
direction: solmax   play: repair   node/task: g-kernel/converge

outcome: |
  The g-kernel converge retrofit was repaired after owner objection.
  The useful part remains: it identified W0 white spots. The invalid part is corrected:
  model-proposed interpretations are no longer represented as owner-signed answers.

  `work/converge-g-kernel.md` is now a FORM/AGENDA artifact:
  - §BORN-CLOSED contains only imports already decided by CHARTER/TREE/NOW/history.
  - Q1-Q15 are explicitly marked as needing owner signoff before t-2/t-3 freeze kernel API.
  - `c-converge-arch-kernel-001` is blocked until those questions are resolved or explicitly
    deferred by the owner.

evidence: |
  - Owner objection: "Слушай, как ты мог закрыть белые пятна без меня? ... Тебя что,
    там что-то придумал и закрыл?"
  - Owner repair approval: "чини".
  - Current state before repair had `work/converge-g-kernel.md` status `RESOLVE pass`
    and §SIGNOFF saying W0-internal mechanism rows were forward-clean.
  - Current NOW before repair had `c-converge-arch-kernel-001` as ready.
  - Repaired artifact now says `NOT RESOLVED. NOT SIGNED` and lists Q1-Q15 as owner agenda.

state_changes: |
  work/converge-g-kernel.md:
    - Replace RESOLVE/signoff language with FORM/AGENDA repair note.
    - Keep born-closed imports only for decisions actually supported by existing state.
    - Convert former W0-internal "answered" rows into Q1-Q15 `needs owner signoff`.
    - Add owner discussion agenda with options A/B/C and recommendation A.

  NOW.md:
    - Update `c-converge-kernel-001` note to say the converge output was repaired from
      over-closed RESOLVE into FORM/AGENDA.
    - Change `c-converge-arch-kernel-001.status`: ready -> blocked.
    - Add decision inbox item:
      "How should the g-kernel converge white spots Q1-Q15 be handled before t-2?"
      with options to hold t-2 and discuss/sign, proceed with scaffold defaults, or explicitly
      approve the candidate recommendations.
    - Set `next` to awaiting_decision for owner resolution of Q1-Q15 before converge-arch or t-2.

  LOG.md:
    - Add newest-first:
      "2026-06-16 — repair g-kernel/converge: over-closed converge retrofit downgraded
      to owner-signoff agenda; c-converge-arch-kernel-001 blocked until Q1-Q15 are resolved.
      → history/2026-06-16-s-repair-kernel-converge-overclose.md"

  os/FRICTION.md:
    - Add one watching line for the converge silent-close failure mode; no OS maintenance
      change is made in this repair session.

captures: |
  - Candidate maintenance follow-up if this repeats: harden converge.md / writer checks so
    `answered` can only mean born-closed import or explicit owner quote; model proposals must
    use a separate status such as `proposed_owner_signoff`.

decisions_needed: |
  - q: "How should the g-kernel converge white spots Q1-Q15 be handled before t-2?"
    options:
      - "Hold t-2 and discuss/sign Q1-Q15 in `work/converge-g-kernel.md`."
      - "Let t-2 proceed with scaffold defaults and accept drift risk."
      - "Explicitly approve the candidate recommendations in Q1-Q15 as written."
    recommendation: "Hold t-2 and discuss/sign Q1-Q15; these choices can freeze the kernel API."

play_check:
  - "1 Name the contradiction: done — converge artifact/history said W0-internal terms were signed/answered; owner objected that those white spots were not discussed with him."
  - "2 Reconstruct: done — commit 5f40d33 produced useful question discovery but invalid signoff status; history is append-only, so the repair supersedes rather than edits it."
  - "3 Propose corrected state: done — downgrade work artifact to FORM/AGENDA, block converge-arch, add owner decision for Q1-Q15."
  - "4 Confirm: done — owner explicitly approved repair with: \"чини\"."
  - "5 Friction: done — one watching line added to os/FRICTION.md; no maintenance rule change in this session."

log: "repair g-kernel/converge: over-closed converge retrofit downgraded to owner-signoff agenda; c-converge-arch-kernel-001 blocked until Q1-Q15 are resolved"

next: |
  awaiting_decision:
    owner should choose how to handle Q1-Q15 in `work/converge-g-kernel.md` before
    converge-arch or t-2. Recommendation: hold t-2 and discuss/sign Q1-Q15.

END_OF_FILE: live/solmax/history/2026-06-16-s-repair-kernel-converge-overclose.md
