# Migration runbook: split g-7e15 (visual) into its own direction `gas-visual`

Owner-approved 2026-07-04 (Fork A): visual becomes its own PEER direction with a FOCUSED/INSTRUMENTAL
charter (money/Steam/pride stay owned by `indie-game-development`); split ONLY visual now (marketing/canon
stay — not colliding). Belt-and-suspenders during migration: the concurrency-hygiene fix on
`os/adapters/worktrees.md` (@c3a7002 — distinct session-id prefixes + re-sync-before-every-apply).

This is a FRAME + migration job. Run it as a FRESH, dedicated session (clean context; 30-file surgery).
Do NOT execute mid another job. Every stage = its own commit → reversible until push (push owner-gated).

## Target shape

Two directions sharing canon + sim-SPEC + product repo, fully parallel writers (worktrees.md model):
- `indie-game-development` — bet g-9c41 (engine/sim); worktree GasCoopGame **dev**; session-id `eng-NNN`.
- `gas-visual` (NEW) — bet = gas visual identity; worktree GasCoopGame **dev_2**; session-id `vis-NNN`.
- SHARED (single source, referenced not duplicated): canon repo `gas_coop_game_canon`; sim-SPEC
  `indie-game-development/knowledge/g9c41-gas-engine-SPEC.md` (engine owns, visual READS read-only);
  product repo `GasCoopGame`.

## gas-visual CHARTER (owner-approved draft 2026-07-04 — the frame session presents THIS at Stage 1 for the formal G9 «да»)

Focused/instrumental. The jewel criterion is REMOVED (it was the owner's illustration that sim+visual are
the game's FOUNDATION, not a success metric).

- **Mission.** gas-visual gives the game's gas a distinct, readable, spectacular PROCEDURAL visual identity
  derived from simulation state — turning real gameplay into storefront-ready proof. Rationale (owner): the
  SIMULATION and its VISUAL are the FOUNDATION of the game; most of our force/resources go here, so the look
  is a first-class parallel effort, not an afterthought. INSTRUMENTAL: money/Steam/pride outcomes stay owned
  by `indie-game-development`.
- **Success criteria** (measurable):
  1. Generic gas types read clearly at a glance (no labels/overlay) AND look good on a MID-SPEC Steam machine
     (average requirements).
  2. A gas's visual reflects its ENVIRONMENTAL RESPONSE (e.g. temperature: slows / gains effects / stays
     stable when hot vs cold) and matches sim state.
  3. Blind check: a vision-agent over a captured clip (how many gases / where danger / where flow) matches
     sim state + the owner's gamer-eye verdict.
  4. Anomalous gases pass the MENACE test (a 10-30s out-of-context clip reads as threat / creepy / intriguing);
     a flagship anomalous gas MAY carry a baked visual motif or even a model beyond pure procedural.
  5. The pipeline is a PROCEDURAL derivation of sim state — SHARED base params + PER-TYPE UNIQUE params —
     behind the g-9c41 render seam (not hand-staged VFX).
  6. Clip material flows to the game's marketing (g-5b07 / g-e6f2).
- **Constraints:** secondary to the engine bet (owner-set cadence, no fixed hour quota); RENDER-ONLY (reads
  the authoritative sim, ZERO Core/** edit, never writes sim truth); gated on engine milestones (Sc-kernel
  GREEN — done; W1b — done; later stages may re-gate with a fresh owner check); solo art-scope (asset-ease
  over beauty; low-poly + gallows-deadpan register B; cuts normal); reads shared canon + sim-SPEC read-only;
  worktree GasCoopGame_dev_2 (never dev).
- **Lenses:** (1) readability/legibility; (2) art-scope / solo-feasibility; (3) render-performance (min-spec
  ms-budget); (4) marketing-feed (does it produce storefront-ready proof).
- **Owner edges:** gamer-eye taste; asset-ease references (Prey 2017, Breathedge); the shipped render
  foundation (W1a DELIVERED).
- **Risk posture:** guarded (inherits the game's posture; look-dev is exploratory but gated on engine + owner-eye).
- **Repos:** GasCoopGame (render layer, worktree dev_2) + gas_coop_game_canon (read); sim truth = a read-only
  pointer to indie-game-development/knowledge/g9c41-gas-engine-SPEC.md.
- **Pre-mortem (>=5):** (1) gas reads as noise/hazard-gimmick not identity -> sim-derived visual language per
  type + blind test; (2) over-scoped art (custom VFX per gas) breaks solo -> derivation-not-VFX, asset-ease,
  cuts; (3) drifts off-contour like the source-scan leg (undeclared Core/net/shader) -> render-only boundary,
  slices come HOME, owner-eye gate, review-scope v15 + source-scan-ban v17; (4) generic env-response or
  anomalous menace unreadable at mid-spec -> readability lens + ms-budget gate; (5) canon/SPEC forks and drifts
  -> ONE source + read-only pointer, visual never copies sim truth; (6) builds on a stale/contaminated dev_2 ->
  reset dev_2 to clean main before build (c-visual-005 step 0).

## Gas visual concept (owner-described 2026-07-04 — DIRECTION, NOT frozen spec; capture as a knowledge/ note in gas-visual)

The visual system is PROCEDURAL, driven by sim state. Gas types share COMMON parameters (a baseline gas
look) and each type MAY carry its OWN UNIQUE parameters/effects the visual must render (illustrative: сполохи
/ flashes — not a commitment). Two broad families the owner is leaning toward (nothing final):
- **Generic gases** (understandable — hot, cold, …): read clearly by their nature; their visual RESPONDS to
  environmental conditions (temperature etc.) — somewhere slowing, somewhere gaining effects, somewhere
  unchanged — and the visual SHOWS that response. Must look good + read clearly on a mid-spec Steam machine.
- **Anomalous gases** (unusual, creepy): rarer (maybe ~one per zone — undecided), meant to instill DREAD and
  CURIOSITY ("what else could be down there"). May carry a baked visual motif or even a model beyond pure
  procedural — owner's illustrative example: fog creeping, smoky arms growing out of it (an example, not a
  requirement). The menace test lands here.
This is intent/feeling to steer look-dev, not a numbered requirement list — freeze specifics only at each
slice's own shape with owner-eye (canon: vibe != requirements).

## Manifest — MOVE / STAY / SHARED

MOVE to `live/gas-visual/` (use `git mv` so per-file history is preserved):
- work/: gas-visual-research-2026-06-21, gas-visual-architecture-2026-06-26, gas-visual-rd-center-2026-06-29,
  gas-visual-wave-plan-2026-06-29, gas-visual-plan-v2-2026-07-02, c-visual-001..005-call.md
- history/: s-visual-001..012, s-research-gas-visual-tech-001, s-work-visual-rd-center-001,
  c-visual-002-s1-result-2026-06-29, 2026-07-03-s-work-040-visual-stage1-unhold,
  2026-07-04-s-work-044-visual-sourcescan-retirement-binding-g5,
  2026-07-04-s-work-046-visual-sourcescan-route-resolve
- NOW content: the parallel_tracks/g-7e15 block → becomes the new direction's BET; open_calls c-visual-004
  (open) + c-visual-005 (framed); decisions d-visual-sourcescan-route-001 (answered A) + d-finer-grid-fork-001;
  the visual next-lines.

STAY in `indie-game-development`:
- all g9c41-* knowledge, engine work/history, marketing + canon plays/tracks, codex-sidecar
- CHARTER (game charter unchanged — visual is now a peer direction serving the same mission)
- TREE: g-7e15 node → collapse to a one-line pointer `status: dropped — migrated to live/gas-visual/ (2026-07-04)`
  (tree rule: a dropped node keeps one line with the reason); update root map_order narrative.

SHARED (reference, do NOT duplicate):
- g9c41-gas-engine-SPEC.md — stays engine-owned; add a read-only POINTER note in gas-visual/knowledge/.
- canon repo + product repo — both charters list them; engine→dev, visual→dev_2.

BORDERLINE (decide explicitly):
- review-gas-sim-visual-2026-07-02.md (joint sim+visual) — STAYS with engine (engine decisions were born
  from it); gas-visual references it.
- s-canon-visual-style-minimal-gas-stage-001.md (canon×visual) — POINTER copy in gas-visual (canon original stays).

## Cross-direction edges (keep them working)

| Edge | Post-split mechanism |
|---|---|
| engine unblocks visual (Sc-kernel GREEN / W1b landed — both already done) | engine review on the milestone emits a handoff CALL/capture to gas-visual; gas-visual NOW carries `depends_on: <engine milestone>` |
| visual reads sim-SPEC | read-only pointer in gas-visual/knowledge/ |
| clips → marketing (g-5b07/g-e6f2, stay with game) | gas-visual drops a clip artifact in product/work → game marketing track picks it up (handoff CALL) |
| W1b (d-w1b-window-001) | already RESOLVED; recorded closed in both histories |

## Execution — staged, reversible, verifiable

- [ ] Stage 0 — quiesce + re-sync. No open visual session; `git fetch && reset --hard origin/main` before EACH write.
- [ ] Stage 1 — FRAME gas-visual (G9): CHARTER (focused/instrumental) + root TREE + empty LOG/NOW. Owner-approves each artifact in-session before it is written.
- [ ] Stage 2 — `git mv` the visual work/history files into live/gas-visual/**; add SPEC pointer + canon-style pointer.
- [ ] Stage 3 — build gas-visual NOW: bet (from g-7e15 goal/done_when), open_calls c-visual-004/005, decisions d-visual-*, next (continue Stage 1 / fire c-visual-005), `depends_on` engine milestones, id-prefix vis-.
- [ ] Stage 4 — clean indie: remove g-7e15 track + c-visual open_calls + d-visual decisions + visual next-lines from NOW; TREE g-7e15 → migrated pointer; update map_order; id-prefix eng-.
- [ ] Stage 5 — commit (one per direction; disjoint paths → parallel-safe) + LOG line each. Push owner-gated.

## Acceptance — "works as expected"

1. `audit gas-visual` and `audit indie-game-development` both clean (END_OF_FILE trailers; six file types; cross-refs resolve; G1–G4 hold).
2. Nothing lost: visual history file count before == after (`git log --follow` per file).
3. indie NOW no longer contains g-7e15 / c-visual / d-visual; gas-visual NOW contains them and only them.
4. Pointers resolve: SPEC pointer opens; canon repos valid; `depends_on` names real engine milestones.
5. G1 in both: exactly one active bet per direction (engine g-9c41; visual = identity). No parallel_tracks drift.
6. Isolation proven: two concurrent sessions (eng- / vis-) write to DIFFERENT NOW files + counters → collision impossible by construction (the goal).
7. Product intact: GasCoopGame main untouched; dev = engine, dev_2 = visual.

## Risks + rollback

- Dangling cross-ref (visual waits on an engine milestone nobody emits) → `depends_on` in gas-visual NOW + the rule "engine review on an unblocking milestone emits a handoff CALL"; record the rule in both NOWs.
- Canon/SPEC forks and drifts (the exact thing we fixed) → ONE source + pointers; visual NEVER copies sim truth, read-only.
- Migration on a dirty dev_2 → the dev_2 reset is c-visual-005 step 0; it does NOT block the OS-state migration (state move never touches dev_2), but visual BUILD work waits on it.
- Rollback: all in git, stage by stage; before push → `reset`; after → reverse `git mv` + restore NOW from history; unpushed gas-visual = does not exist (`git worktree remove`).

## In-flight visual work (not lost)
- c-visual-004 (Stage 1 stand, open) + c-visual-005 (framed clean re-derive) → move as gas-visual open_calls, continue there (worktree dev_2).
- d-visual-sourcescan-route-001 (owner chose A) → moves as an answered decision.

END_OF_FILE: live/indie-game-development/work/gas-visual-split-migration-plan.md
