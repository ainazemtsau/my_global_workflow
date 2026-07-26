# CALL c-shape-sc-damage-001 — shape Sc-damage (first gas CONSEQUENCE on the character road)

**STATUS: READY — issued 2026-07-09 (s-review-sc-sense-close-001) after Sc-sense close-verification.** This is a
**shape session** (`play: shape`), owner-present. It produces a fire-ready **executor CALL** for Sc-damage; it
BUILDS NOTHING. Activates on owner approval (owner may instead pick the parallel-ready canon front
c-forge-q-ruki-001).

## goal (outcome, not method)

A fire-ready Sc-damage executor CALL exists: the FIRST gas CONSEQUENCE slice that CONSUMES the Sc-sense
accumulated dose and turns it into a readable in-world effect on a player-actor — deterministic, lockstep-safe,
engine-first — so that "standing in the wrong gas long enough" produces a consequence the owner can see and a
co-op crew must react to. The shape output carries the mandatory shape artifacts: appetite, a real cut list
(≥1 cut), a lens-sweep verdict per CHARTER lens, and a task testing the riskiest assumption (G6).

## context (read first)

- **Sc-sense wiring contract** — `knowledge/g9c41-sc-sense-delivered-unwired.md`: Sc-sense is DELIVERED but
  UNWIRED into `SimInstance`; Sc-damage is the leg that wires it (feed the COMMITTED post-step field once per
  committed sim tick; preserve the byte-identical dose invariant; consume the generic per-TypeId socket, don't
  re-derive; own thresholds/policy here).
- **g9c41 SPEC** — `knowledge/g9c41-gas-engine-SPEC.md` (§3 what BITES reads the authoritative field; §4 seams).
- **Scale-watchmen home** — `knowledge/g9c41-scale-watchmen.md` + SPEC §6 п.9–10. TIER-2/3 remain armed
  reserves, not authorized work: this shape must carry the open-space owner-eye re-triggers and the named
  cross-type-capacity seam without silently choosing either outcome.
- **Sc-reactions evidence boundary** — `knowledge/g9c41-sc-reactions-c-exec-021-delivered.md`: the recorded
  owner-eye proves only «два облака → телеграф → взрыв»; it does NOT prove «одна детонация в открытом поле
  без стен». The Sc-damage shape must present that missing clause to the owner again and may not mark it passed.
- **Engineering contract v19** — the produced executor CALL MUST mandate: PLAN/BUILD separate sessions +
  owner-readable PLAN; independent RED test-author first; `check.ps1 -Deliver` green at tip; mutation ≥70 on new
  Core; negative-control per acceptance property; a fresh-session binding G5 (cross-family) could-not-refute.
- **Base** — GasCoopGame `origin/main` @defade72 (post-c-exec-035; §Re-sync at the then-tip; confirm synced
  contract + honour v19).
- **Product anchors** — `Assets/GasCoopGame/Core/Field/Sense/PlayerSense.cs` (dose read + snapshot socket);
  ADR-E-0008; the reactions/telegraph engine (Sc-reactions) if a consequence keys off reaction outcomes.

## decisions to resolve in the shape (owner-present)

- **Armed open-space richness check** — the executor CALL must require owner-eye «одна честная струя в открытом
  поле без стен». Separately present the still-unproved Sc-reactions open-space/no-walls detonation clause to the
  owner; only his actual verdict may discharge or revise it. Failure may open a signed TIER decision, never an
  automatic escalation.
- **Cross-type total capacity** — decide no later than this Sc-damage PLAN whether the first consequence needs
  true total-cell capacity / cross-type displacement, or explicitly keeps today's per-type capacity with a named
  later trigger. Do not let the current 4×MaxCellMass co-residency become a silent default.
- **What "consequence" means for the first proof** — the smallest legible dose→effect (e.g. a health/condition
  meter, an incapacitation, a forced action) WITHOUT exploding scope into full combat/status systems. One
  effect, deterministic, engine-first.
- **Co-op interdependence (decision d-coop-interdependence-repin-001)** — FOLD the "gas world forces co-op"
  obligation into the Sc-damage framing as a required owner-eye/gameplay axis (the recommended option): the
  first consequence should create a rescue/dependency/communication moment, not a solo hazard. Record the
  owner's choice.
- **Detection socket** — Sc-damage may READ the Sc-sense readout to drive the consequence, but decide whether
  any detection/diagnosis surfaces now or stays a socket (owner's «пока не делаем» on detection stands unless
  reopened).
- **The player-actor** — still a capsule/minimal actor for owner-eye; decide whether Sc-damage needs a real
  controller or stays on the lockstep-position input (keep scope tight).

## boundaries (out of scope for THIS shape session)

- SHAPE only — produce the executor CALL, build no product code, author no RED tests here.
- No new gas types / no Sc-catalog revival. No visual/shader pipeline. No reopening ADR-0002.
- Do not pre-commit the executor's realization — the produced CALL frames the OUTCOME; its PLAN owns the how.

## done_when

- A fire-ready Sc-damage executor CALL is drafted and owner-approved-to-fire, carrying: goal (outcome), context
  pointers (incl. the Sc-sense wiring contract), the co-op-interdependence axis, boundaries, done_when
  (deterministic dose→consequence + wire-into-SimInstance-correctly + owner-eye), contract v19 discipline, and
  a budget.
- Shape artifacts present (G6): appetite, cut list (≥1 real cut), per-lens sweep verdict, riskiest-assumption
  task (candidate: the deterministic wiring of Sc-sense into the live tick loop).
- The executor CALL carries the mandatory honest open-space jet owner-eye; the shape records the owner's actual
  verdict on the still-unproved open-space Sc-reactions clause and on cross-type total capacity by PLAN close.
- NOW.md would gain Sc-damage as the active task and the executor CALL as the open_call (applied by the shape
  session's RESULT).

## budget

One shaping session, owner-present. Keep the consequence scope minimal (first proof, not a combat system).

END_OF_FILE: live/indie-game-development/work/c-shape-sc-damage-call.md
