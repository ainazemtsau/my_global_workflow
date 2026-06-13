# s-work-004 — work (g-9c41 / t-2): shape t-2 + frame executor CALL c-exec-003

- **date:** 2026-06-13
- **play:** work (one task of the active bet)
- **task:** t-2 — toy gas field + custom chunked-delta stream + breach + first wire measurement
- **CALL applied:** c-work-002 (work, owner present for the architecture/PLAN acceptance-bar step)
- **role:** session → became its own writer after RESULT (agent-CLI on this repo)

## Recite

t-2: build a TOY gas field + our OWN custom chunked-delta stream + a scripted breach + the FIRST
honest wire measurement, ON the t-1 engine-free core (3-mode composition root + the proven
`ITickInputBus` seam). It introduces the real fabric contracts (layer registry + revision feed) and
our quantized delta channel — the contracts that must survive to the real band sim. Serves bet g-9c41,
whose kill-gate is networked chunked-delta gas consistency under a breach.

## The one acceptance-bar decision (owner present) — kill-gate definition

Cross-checking t-2's done_when against the REAL t-1 code surfaced a tension that had to be settled
before framing the executor CALL, because it defines the bet's kill-gate:

- **t-1 = lockstep:** only INPUTS cross the wire; every peer recomputes the field; the field is never
  networked; per-tick bit-exact hash is free.
- **t-2 = the opposite:** the host is the single writer of the field and streams **quantized chunked
  deltas**; clients **reconstruct** without running the sim. With **deadband** ON (done_when p3) the
  client is, by construction, a lossy/lagging replica — so done_when p2's literal "per-tick hash host
  vs clients equal" cannot hold in the same run as p3.

Presented as one decision with a recommendation (enterprise analogy: event-sourcing vs a primary DB +
CDC-fed read-replicas with eventual consistency). **Owner chose "A" — the dual guarantee:**
- **(i) LOSSLESS** (deadband off): per-tick host-vs-each-client FIELD-cell hash **bit-exact** over the
  whole run incl. the breach — the correctness oracle.
- **(ii) LOSSY** (deadband + per-client clamp + aggregate host clamp): **bounded divergence** (≤ the
  quantization step Q) every tick **+ convergence to bit-exact at settle/keyframe points** — where the
  honest wire numbers are measured.

This resolves p2-vs-p3 as two runs, not one. Prerequisite (baked into the CALL): an integer/fixed-point
authoritative truth so "bit-exact" is well-defined (consistent with t-1's integer-only core).

## How the CALL was hardened (8-agent pass, wf_7dbb52a9-1c1)

Ground (3 readers: real product repo / brief v2 + NOW.md / engineering contour + packet schema) →
Draft → 4 adversarial verifiers (testability, boundary, build-on-t1, completeness). All 4 verdicts =
"revise" (skeleton sound). Folded-in fixes:

- **Reproducibility contract** — fixed seed, run length, deterministic breach tick (over the lockstep
  input plane), defined target-tick = peak-dirty-chunk tick; frozen scene profile committed as a
  config/seed file so t-3 reuses byte-for-byte. Separated peer count (1 host + 2 clients = 3) from the
  brief's scene-load "профиль 32/12/2" (scene size, not peers).
- **Validator-reproducible oracle** — the dual-mode hash/divergence proof runs headless in pure dotnet
  over an in-memory analogue of the delta channel (mirrors t-1's in-memory convergence + golden vector),
  which read-only Codex/GPT-5.5 CAN reproduce; the FishNet/PlayMode run is the transport-axis
  confirmation (Unity MCP or owner) that may wait for the owner without failing an overnight leg.
- **Exact hash domain** — FNV-1a (reuse Fnv1a64, pinned order) over the RECONSTRUCTED FIELD CELLS ONLY,
  not the whole `SimState.Hash()` (which folds Delta + RNG the non-simulating client lacks).
- **Artifact contract** — committed machine-readable schema under a named path OUTSIDE `_scratch`; full
  per-tick series with the peak flagged; both modes emit distinct artifacts (a dropped mode = mechanical
  FAIL); 0.6–6 KB = logged sanity reference, not a gate (t-2 records, t-3 judges the steady rate).
- **Boundary tightening (demote to PLAN/ADR-0003)** — the wire resolution-key, single-writer/phase-
  ordering hard-gating, the gas-plane channel reliability (unreliable-sequenced vs reliable), and all
  concrete design values (Q/threshold/N/K/clamps) are PLAN decisions frozen in ADR-0003 + the G0 ledger,
  not pre-decided by the direction. p1 gates only what NOW.md t-2 gates (layer registry + revision feed).
- **Fault injection** — recommend t-2 inject seeded chunk drop/reorder (assert revision barrier + resend
  recovers to bit-exact); if deferred to t-3, downgrade p2's claim to "serialization/round-trip (clean
  channel)" and define gap-recovery — so the CALL never overclaims what a clean-loopback green proves.
- **Operational catch** — `dev` is 5 commits behind `main @7af478a` (MCP/tooling cleanup, no core/sim);
  the CALL says sync dev first.

## Self-check vs done_when (this session's deliverable)

t-2 shaped ✓; executor CALL c-exec-003 framed with all six fields (goal/context/boundaries/done_when/
return/budget) + leg_opens_with + model_routing ✓; each CALL done_when point traces to NOW.md t-2's 4
authoritative points, made machine-testable ✓; direction↔contour boundary preserved (WHAT + acceptance
bar here; HOW deferred to PLAN/ADR-0003) ✓; t-2 → active awaiting the executor return ✓.

## play_check

- **1 Recite:** ✓ — restated t-2 goal/done_when + bet g-9c41 (kill-gate).
- **2 Owner inputs (owner):** N/A — t-2 is engineering infrastructure, not owner-content (play step 2:
  "No → one line why, move on"). Continuation authorized by the owner's words "продолжаем
  indie-game-development"; owner present for the step-3 acceptance-bar call instead.
- **3 Do the work:** ✓ — framed c-exec-003 (no solution design — PLAN/ADR-0003 owns HOW); surfaced the
  single acceptance-bar decision (kill-gate definition); owner's word: **"A"**. Hardened via the 8-agent pass.
- **4 Self-check:** ✓ — done_when traces point-by-point to NOW.md t-2; boundary preserved; 4 verdicts folded in.
- **5 Close:** ✓ — this RESULT; t-2 → active; next = c-exec-003.

## State changes (applied by this session as writer)

- NOW.md active_tasks **t-2 → active** (kill-gate dual-guarantee "A" recorded; dispatched as c-exec-003).
- NOW.md open_calls **+= c-exec-003** (status: dispatched).
- NOW.md `next:` reframed **c-work-002 → c-exec-003** (full executor CALL).
- LOG.md entry appended.
- history/s-work-004.md (this file) saved.

## Captures (not acted on — triage at pulse/review)

- `CoreBuildMarker.cs` is a deletable t-1 setup placeholder still in core/ — drop opportunistically
  during a t-2 leg; not a t-2 requirement.
- Once t-2 proves the dual-guarantee, consider promoting its definition into `knowledge/` as the durable
  net-consistency acceptance bar that t-3 and future net work read.

## Next

**c-exec-003** — executor leg for t-2. Opens with an interactive PLAN (owner present, plan mode) in the
product-repo dev worktree, produces ADR-0003 (the custom field-state stream) + a frozen G0 ledger BEFORE
any code, then runs autonomous build legs (dotnet/in-memory dual-mode proof as the primary night path;
FishNet/PlayMode confirmation via Unity MCP or owner). VALIDATE = Codex/GPT-5.5 (read-only, different
family). This is the owner's mandatory architectural appearance until the final report.

END_OF_FILE: live/indie-game-development/history/s-work-004.md
