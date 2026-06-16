# s-decide-004 — incident review + owner decisions (g-9c41 Wave-2 t-1)

> Session type: **decide** (a plain owner message about a problem in the direction → KERNEL §2 OPEN → the
> active bet g-9c41). Recorded the owner's design clarifications + decisions and RE-OPENED t-1 after its
> returned build was rejected. NO build committed in GasCoopGame_dev (t-1 held uncommitted throughout).

## Trigger

Owner pasted the last two messages from a chat session (his + the chat's) that lacked full-workflow access:
he rejected the gas "80/20 bottom/top" fill he saw, and an independent Codex review flagged 2 P1 + 1 P2. He
asked for an INDEPENDENT deep analysis (not the chat's word), a plain-language account of WHERE 80/20 came
from and WHO decided it («саботаж?»), validation of the Codex findings, a process post-mortem, and a rebuild
direction — with nothing committed.

## What I verified directly (ground truth, not the chat's account)

The t-1 band-solver build is REAL and sits UNCOMMITTED in `C:\projects\Unity\GasCoopGame_dev` (branch dev,
HEAD == main == 9807bc3; the Coarse/*.cs is staged, the tests/ADR/measurements/openspec are untracked). An
earlier read of `main` (clean) was a worktree confusion — discarded.

- **80/20 origin (code):** `CoarseBandStep.cs` `LowerShare = total·eff/(eff+BuoyancyRef)`, BuoyancyRef=16,
  frozen weights {64,32,16,8}. Heaviest cold gas → 64/(64+16) = 0.80 → 80% lower / 20% upper. Crucially
  `targetLower = total × fraction` ⇒ a FIXED proportion of total, AMOUNT-INDEPENDENT (a puff still throws 20%
  to the ceiling). The owner's complaint is confirmed exactly.
- **Who decided it:** ADR-0005 **BS4** states "the exact integer m_eq DISTRIBUTION formula ... is the
  builder's, constrained by the BS10 battery — tests pin the behaviour + the frozen law, NOT the distribution
  formula." The owner ratified D1–D4 (integer / carrier / Q=16 / K=4) — engineering knobs — never the fill
  model. converge-g-9c41 decomposed the STREAM into C1–C22 but imported the settling/fill mechanism CLOSED
  (I17, "2–3 bands + derived interface") WITHOUT decomposing its parameters. So the gameplay-VISIBLE fill
  model was mis-classed as a builder detail. NOT sabotage — a mis-drawn decision boundary + a coverage gap.
- **The built model also diverges from the brief's OWN cited physics:** CFAST/CONTAM two-layer zone models
  have a MOVING interface that rises with the amount of dense gas — closer to the owner's fill model than to a
  fixed fraction. So the owner is right twice over.

## Codex findings — all 3 VALID

- **P1 #1 (real bug):** `CoarseBandStep.cs:144` `sectorTemp = (temp[lowerCell]+temp[upperCell])/2`, then the
  per-band eff uses that single AVERAGE for both bands. Invisible to the battery because every test uses
  UNIFORM per-band temperature (L7 sets both bands 260; others cold 0). No differential-band test existed.
- **P1 #2 (real):** `git status` confirms ADR-0005, tests/.../Coarse/, all measurements + the openspec change
  are UNTRACKED; only Coarse/*.cs is staged; RESULT.md modified. A staged-only commit loses the tests/ADR/
  measurements while RESULT claims 126 tests + committed measurements.
- **P2 #3 (real, unrelated):** `Unsafe.dll.meta` has an uncommitted, unstaged Editor-import flip
  (enabled 0→1). The headless coarse core never references Unsafe — safe to revert; cannot be dated from git.

## How it passed the gates (process post-mortem)

The battery (BS10/L6) asserts only the WEAK "heavy has STRICTLY more in the lower band" — both the 80/20 model
AND the owner's capacity-fill model pass it; no test varies the AMOUNT, none uses differential per-band temp.
The legibility pre-test (BS14/L20) only checks the render is non-empty/deterministic/≥2-bands — and the owner
saw a SINGLE near-full snapshot where 80/20 looks fine. The independent test-author + G5 + the Codex pre-pass
all score against the spec, and the spec under-specified the fill model + regimes — so a spec-conformant-but-
wrong implementation survived. Caught by the owner's eye (small amount) + Codex (free read).

## Architecture walkthrough (owner alignment)

Walked the whole system, plain-language + a diagram: grid = shared ADDRESS fabric (coordinates + point→room
ownership map + event bus + revision clock), NOT a data store; the coarse room-graph (sector=room, 2 bands,
doors=portals) runs EVERYWHERE (the workhorse); the fine 25cm cell grid is near-player only = Wave 3; rooms
come from the DA-composed scene via the generator-agnostic TopologyDocument (1 sector per room day-one); a
breach = a portal with an "opening-size NUMBER" (shape is fine-tier only); a whole-level explosion is handled
by the always-on coarse tier (wall→portal event + revision → coarse gas re-flows). Owner: «геймплейно как я и
представлял, структура чуть другая, окей; всё поддерживается».

## Decisions (recorded in NOW.decision_inbox)

- **d-fillmodel-001 (answered):** NO fixed proportions; coarse vertical distribution = CAPACITY-FILL + OVERFLOW
  (amount-dependent); heavy fills floor-first, light ceiling-first, temperature flips; multi-species layer by
  density; 2 bands OK for now (smooth = Wave-3 fine). Deferrals: Q1 size→flow (simple now / curve later), Q2
  explosion-magnitude→opening-size (later w/ destruction), Q3 far = opening-size-number-only (shape irrelevant
  far; a breach CAN drive other layers later — separate axis), Q4 repair (later / maybe-never).
- **d-return-reconstruction-001 (deferred → Wave 3):** coarse-always-on already gives the correct return
  AMOUNT (never instant-full); reconstruct the fine front from (source position + coarse amount), NOT a separate
  stored equation (single source of truth — confirms/refines d-bandhandoff-001 GG4/OR4); lazy-LOD detail
  retention; gas doesn't evaporate (for now, keep extensible). Deep-research DEFERRED to the Wave-3 shape
  (owner: «deep ресёрч очень не нужен»).

## State changes applied

active_bet.phase: t-1 re-open note. active_tasks t-1: status → reopened. open_calls c-exec-005: status →
reopened (verdict overturned, evidence summarized). decision_inbox: +d-fillmodel-001, +d-return-reconstruction-001.
next: a ⚠ SUPERSEDED banner + the 6-step model-rebuild re-PLAN (owner-approval-gated); the prior t-1 CALL framing
kept below it. LOG line appended.

## Next

The 6-step model-rebuild re-PLAN of t-1 (owner-approval-gated, in NOW.next): (1) re-PLAN the fill model with the
owner (capacity-fill+overflow already decided) + the few micro-params; (2) re-freeze ADR-0005 BS4 with the new
model + per-band temperature + explicit physical-REGIME test dimensions; (3) re-author independent tests
(fill-level + differential-band); (4) rebuild the solver (LowerShare → capacity-fill; Settle reads per-band temp,
no average); (5) re-validate (gate + fresh G5 + owner gamer-eye on MULTIPLE fill amounts + Codex); (6)
housekeeping at commit (stage ALL files; revert Unsafe.dll.meta; rewrite RESULT). A MAINTENANCE REQUEST
(feel-decisions delegated to the builder; converge under-decomposed the fill mechanism; spec-hardening must
enumerate regimes) runs in a SEPARATE session (never touches live/**), per the standing "additive, don't break
what works" guardrail.

END_OF_FILE: live/indie-game-development/history/s-decide-004.md
