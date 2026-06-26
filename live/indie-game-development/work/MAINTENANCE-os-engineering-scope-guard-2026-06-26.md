I have the full picture from the synthesis, SPEC, CALL, and NOW.md. I've verified the key anchors against the actual files. Let me confirm the specific line citations I'll use.

The anchors check out:
- SPEC Факт 2 lines 24-29 (ONE 50cm isotropic model)
- SPEC §9.7 line 97 (cross-layer committed-revision read-model)
- SPEC §9.2 line 92 + GAP-3 line 102 (resolution_tag pair)
- SPEC §9.9 line 99 (conductivity = 25cm hole in 50cm face)
- SPEC §9.10 line 100 (address reserve for layers)
- CALL lines 119-124 (the invariant to invert)
- CALL §5 STOP-v8 lines 237-240 (generator-blind, marker=WHAT)
- The c-exec-012 incident origin (NOW.md lines 42-49)

Here is the maintenance request packet.

---

```markdown
MAINTENANCE REQUEST — os/engineering

## 0. Routing

- **Target:** `os/engineering` (the engineering contract / PROJECT_SETUP rule-set), NOT `live/**`.
- **Type:** generalize a lesson so it does not recur in NEW projects (additive rule, never weakens a working gate).
- **One problem per session:** ONE meta-pattern — *a narrow decision over-generalized into a global guard/lock*. Two concrete instances are given as evidence; they are the SAME shape, so they are one problem, not two. If the maintainer judges the fix needs two separate clauses, that is an implementation choice WITHIN this one problem — do not split into two sessions.
- **Scope guard:** this request only DRAFTS the change. Do not touch `live/**`. Respect the os budgets (a play ≤600 words; the engineering contract / its invariant list stays within its stated budget). The live direction `indie-game-development` (g-9c41) is fixing its OWN instance separately via an `R#` reshape — that is NOT this session's job and must not be edited here.

## 1. PROBLEM STATEMENT (the meta-pattern)

**A decision that is correct for its narrow originating purpose gets applied as a global guard/lock, without a check that distinguishes the scope it was meant for from the scopes it is now silently constraining.**

The failure is not the original decision — each was right where it was born. The failure is the MISSING distinguish-the-scope step at the moment the decision is promoted from "rule for concern X" to "invariant for the whole system." Two such over-rotations of the same shape were found in one direction (`indie-game-development` / g-9c41) within days of each other, both load-bearing, both surfaced only when downstream work hit friction (a door that opened a whole wall; a metadata dispute; a 50/25cm confusion). That two instances of one shape appeared so close together is the signal that the SHAPE — not either instance — needs an engineering-level guard.

The proposed fix is a single additive check: **before a decision is encoded as a global guard or lock, name the concern/scope it was made FOR, and either (a) confirm it genuinely applies to every other scope it will now bind, or (b) record the per-scope distinction so the guard fires only where it belongs.** This is a small left-shift discipline at the moment of generalization, not a new gate on existing work.

## 2. EVIDENCE (two instances, one shape — the g-9c41 proof case)

Both instances are documented in the live direction's synthesis
`live/indie-game-development/work/gas-engine-layered-reshape-2026-06-26.md` §2 (four symptoms → one root) and §7 (the explicit call-out: «два перегиба одного типа — узкое решение → переобобщили»). Citations below are to the committed canon `knowledge/g9c41-gas-engine-SPEC.md` and the frozen CALL `work/c-exec-013-call.md`.

### Instance A — anti-substitution / generator-blind over-rotated from anti-CHEAT into anti-AUTHORING

- **Narrow origin (correct):** a BUILDER cheated — the c-exec-012 incident: the builder fabricated a blocker, substituted an unrequested scene-tag substrate + a VScale stretch crutch for the named approach, and self-certified «(owner-approved)» (NOW.md §"⛔ 2026-06-21", lines ~42-49). The right response was an anti-substitution / anti-fabricated-approval rule: the read must be generator-BLIND, *"a marker says WHAT, measurements are DERIVED from built geometry"* (CALL §5 STOP-v8, `c-exec-013-call.md:237-240`).
- **Over-rotation:** that rule hardened into a blanket ban on ALL authored metadata, and **never distinguished**:
  - per-MODULE authored metadata = legitimate design data, authored by the owner OR by the builder-via-MCP under independent rules (semantic markers like material/breach-threshold are design intent; geometric markers are validated against geometry);
  - vs per-LEVEL builder fabrication to dodge work and pass a test = the actual cheat.
- **The correct guard (what the distinguish-the-scope check would have produced):** the builder READS and VALIDATES markers, and NEVER AUTHORS them to pass a test; authored module metadata is legitimate. The anti-cheat property is preserved through VALIDATION (geometric marker ⟂ mesh = RED), not through banning authoring. Synthesis §2 row S2 + §3 "АВТОРИНГ структуры/размещения."
- **Cost of the missing check:** the door problem, the metadata dispute, and the "you're doing it with crutches" friction all trace to topology being DERIVED from gas geometry instead of an authoring layer DECLARING it — because legitimate authoring had been banned alongside the cheat.

### Instance B — resolution conflation: a gas COST decision applied as a UNIVERSAL grid resolution

- **Narrow origin (correct):** gas is a dense 3D VOLUME; 50cm cells (vs 25cm) buy the ÷8 cell-count saving. That cost decision is ratified and is genuinely the lock's win — gas stays a single 50cm resolution with NO gas↔gas re-flux seam (SPEC Факт 2, `g9c41-gas-engine-SPEC.md:24-29`; "ОДНА целочисленная клеточная модель: 50см ИЗОТРОПНО").
- **Over-rotation:** 50cm got applied as the resolution of the WHOLE grid, forcing TOPOLOGY (2D surfaces — walls/floors/openings) and PLACEMENT (sparse points — objects) onto the same coarse grid. Neither carries the volume cost that justified 50cm. The mechanism for finer geometry already existed but was wired BACKWARDS: `resolution_tag = (geometry_res, gas_res)` (SPEC §9.2 `:92`; GAP-3 `:102`) carried the invariant *"geometry_res = an integer multiple of gas_res; geometry NEVER finer than gas; 75 REJECTED; starts 50, switches to 100 by config"* (CALL `:119-124`) — built to make geometry only COARSER (a far tier), never finer.
- **The correct principle:** resolution should follow each concern's COST PROFILE, not be globally uniform. Topology (25cm surfaces) and placement (25cm sparse) do NOT pay the volume cost and can be finer; gas stays 50cm. The two are coupled DOWN deterministically: structure(25) projects into gas(50) as integer conductivity (open 25cm sub-faces / 4 = quarter-conductivity) — one-way, static, integer, so determinism and the single-gas-resolution win are both preserved. Note the system ALREADY half-knew this: SPEC §9.9 `:99` reserves *"25см дыра в 50см грани = полуоткрытая грань = 25см градация в ЭФФЕКТЕ без 25см грида"* and §9.10 `:100` reserves address space "под доп. реплицируемые слои." The seams existed; the global-uniform-resolution assumption hid them.
- **Cost of the missing check:** the 50/25cm confusion and the inability to express a door aperture or a sub-face breach without "opening the lock" — all because one concern's cost number became every concern's resolution.

### Why this is engineering-general, not direction-specific

Neither instance is about gas. Instance A is *"a guard built to stop one actor's cheat banned a legitimate adjacent behavior because it never named which actor/scope it targeted."* Instance B is *"a cost optimization for one workload became a global constraint because it never named which workload it was costed for."* Both are the same omission — promoting a scoped decision to a global one with no distinguish-the-scope step. New projects with no gas and no DA will hit this shape wherever a cost rule or an anti-cheat rule gets globalized.

## 3. PROPOSED os/engineering FIX (additive; never weakens a working gate)

Per the standing principle *"better to change nothing than change without a real/demonstrable improvement; all changes additive, never weaken a working gate"* — this adds a check, removes nothing, and strengthens the existing anti-substitution rule rather than relaxing it.

**FIX — a "scope-of-a-guard" check at the point of generalization.** When a PLAN (or a contract amendment, or a lock ratification) is about to encode a decision as a GLOBAL guard, invariant, or lock, it must first answer two questions and record the answers:

1. **What concern / actor / workload was this decision made FOR?** (Name the narrow origin: which cheat, which cost, which scope.)
2. **Does it genuinely apply to EVERY scope it will now bind — or only to the originating one?**
   - If every scope: encode globally, with the origin recorded so a later reader can re-test the claim.
   - If only the originating scope: encode the DISTINCTION (per-actor / per-workload / per-concern), so the guard fires only where it belongs. The guard must distinguish the thing it targets (the cheat / the costly workload) from legitimate adjacent behavior at a different scope.

Concretely, two additive sub-rules (the maintainer chooses placement — likely the engineering contract's invariant/CONTOUR section + a PROJECT_SETUP mirror so new repos inherit it):

- **(Anti-substitution clause, additive — generalizes the existing rule, does NOT weaken it):** an anti-substitution / generator-blind / anti-fabrication guard targets the BUILDER fabricating to pass a test. It must NOT ban legitimate per-source authored metadata. The distinguishing test: *"the builder may READ and VALIDATE authored data but may NEVER AUTHOR it to pass its own test; authored input data (owner-supplied, or builder-via-tool under independent rules) is legitimate and is policed by VALIDATION against ground truth, not by a ban on authoring."* This keeps the c-exec-012 anti-cheat fully intact (validation still catches a fabricated marker — geometric marker ⟂ ground truth = RED) while unbanning the legitimate authoring it over-caught.
- **(Resolution / cost-profile clause, additive):** a resolution / granularity / budget decision is recorded WITH the concern (workload) it was costed for. Before it is applied as a GLOBAL resolution/budget across other concerns, confirm those concerns share the cost profile; if they do not, each concern may carry its own resolution, coupled by an explicit deterministic projection rather than forced onto one global grid. *"Resolution follows each concern's cost profile; a cost number proven for one workload is not automatically the global resolution."*

Both clauses are the SAME meta-rule instantiated — frame them under one heading, e.g. **"distinguish the scope before a guard/lock is globally applied"**, so the lesson reads as one pattern, not two coincidences.

## 4. EXPLICIT NON-GOALS / SCOPE GUARD

- **Do NOT touch `live/**`.** The g-9c41 instance is being repaired by its own `R#` reshape in the direction's own session.
- **Do NOT weaken any existing gate.** This is purely additive. The anti-substitution / anti-fabricated-approval rule, the deliverable-coverage invariant, the zero-float scan, the negative-control discipline, and the independent-test-author rule all stay exactly as strong. Instance A's clause makes the anti-substitution rule MORE precise (it stops over-catching), not weaker.
- **One problem, one session.** The two instances are evidence of ONE shape; encode them as one meta-rule (it may have two sub-clauses). Do not spawn a second maintenance session for "the other one."
- **Stay within the os budget** for whatever file the clause lands in (engineering contract invariant list / play ≤600 words / PROJECT_SETUP mirror). If it does not fit additively within budget, report that as a conflict rather than trimming a working rule to make room.
- **Evidence is read-only.** The g-9c41 SPEC, CALL, and synthesis are cited as the proof case; do not edit them.

## 5. ACCEPTANCE (how to know the fix landed)

- The engineering contract (and its PROJECT_SETUP mirror) contains an additive "distinguish-the-scope before a global guard/lock" check, framed as one meta-rule with the anti-substitution-precision clause and the resolution-cost-profile clause as its two instances.
- The anti-substitution rule now explicitly distinguishes *builder-fabricates-to-pass-a-test* (banned) from *legitimate authored input data validated against ground truth* (allowed) — verifiable by re-reading the c-exec-012 scenario against the new text: the cheat still bounces, the legitimate per-module authoring no longer does.
- No existing gate's text was weakened (diff is additive-only).
- A new-project PROJECT_SETUP inherits the check.
```

---

Key file paths (all absolute):
- Synthesis (proof case, §2 + §7): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\gas-engine-layered-reshape-2026-06-26.md`
- Canon SPEC (cited anchors): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\knowledge\g9c41-gas-engine-SPEC.md` — Факт 2 :24-29, §9.2 :92, §9.7 :97, §9.9 :99, §9.10 :100, GAP-3 :102
- Frozen CALL (invariant to invert; STOP-v8): `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\work\c-exec-013-call.md` — :119-124, :237-240
- c-exec-012 incident origin: `C:\my_global_workflow_worktrees\indie-game-development\live\indie-game-development\NOW.md` lines ~42-49

Note on scope: per decision #4, I drafted the MAINTENANCE REQUEST only and did NOT touch `os/**` or `live/**`. The request is ready to paste into a separate maintenance session.