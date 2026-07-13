# RESULT — s-map-characters-track-p2a0-close-001

- direction: indie-game-development
- node: g-9c41 → g-6d4e (new)
- task: M1-P2a0
- play: map (owner-directed structural change: close P2a0 verdict + stand up the character track)
- date: 2026-07-13

## outcome

P2a0 network-ownership question is settled and recorded, and the character work now has a home in the tree.
The owner played the live PuppetMaster spike and rendered the verdict **Candidate A** (the deterministic
core/controller owns the authoritative body position; the PuppetMaster ragdoll is a cosmetic local view,
never authoritative; Candidate B rejected — non-deterministic PhysX on the authoritative path desyncs across
machines). Gameplay-physics (bodies fly / bounce / knock others / hit loot / break doors) is answered by
design as a deterministic **grid-ballistics** layer in the CORE (not a physics engine), named as a future
g-9c41 core slice. M1-P2a0 is done. A new parallel track **g-6d4e «Игровые персонажи»** (character
presentation/embodiment layer) is stood up (owner-approved), sibling of g-7e15, NOT a 2nd bet. The spike's
paid RootMotion vendor asset was gitignored (no push) so the product git panel is clean.

## evidence (matching done_when)

- Owner-eye gate (the binding gate for this DESIGN decision) PASSED: owner played the spike and confirmed
  in-session 2026-07-13 «Кандидат A — да» (+ «трек ... ок», «поехали»).
- Independent delivery verification (separate session from the one that did the work — G5 separation):
  product repo `origin/main@0e9eed02` carries `docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md`
  (verified present); spike stand branch `codex/c-exec-player-puppetmaster-p2a0-002-build@a6d9271f`
  (Assets/_PuppetSpike + OWNER-INSTRUCTION.md); PlayMode liveness smoke green (Норма→Сбит→Встаёт).
- Consciously-cut (owner-acked lean pivot): the heavy done_when's bounded-C kill-probe and a fresh-session
  code G5 were NOT delivered — the lean spike superseded the heavy live-source-proof approach; the binding
  gate for a head/design decision is the owner's eye, not an automated G5.
- RootMotion gitignored: product spike worktree commit `f2f860b7` (1 file, +6 lines, .gitignore only;
  no push; the spike's other proof changes left untouched).

## state_changes (applied by this self-writer session)

- NOW.md:
  - `updated:` → `s-map-characters-track-p2a0-close-001`.
  - forecast: replaced the "Параллельно P2a0 проверяет player root authority" line with P2a0-closed + track
    g-6d4e stood up + grid-ballistics = future g-9c41 core slice.
  - tasks/M1-P2a0: `status: active` → `done` + a `note:` recording the owner-eye verdict, the lean-pivot
    supersession, the owner-acked cut, and the single-source canonical pointer.
  - open_calls: removed `c-exec-player-puppetmaster-p2a0-lean-spike-build-001` (delivered + owner-accepted);
    added `c-plan-characters-001` (to session, READY parallel track).
  - next: UNCHANGED = `work/c-exec-near-gas-core-authority-001-plan-amend-001-call.md` (gas spine, priority 1).
- TREE.md:
  - map_order: appended the g-6d4e parallel-track note.
  - added node `g-6d4e` (goal/why/done_when/status active/detail), outcome-level, no tasks (G2), owner_approved.
- work/c-plan-characters-001-call.md: written (CALL packet).
- LOG.md: appended the session line.

## captures (triaged later, NOT acted on now)

- grid-ballistics = g-9c41 CORE slice (deterministic body-on-grid: DDA on the 25 cm grid, gravity, axis-aligned
  bounce, body-body/body-loot momentum, interactive-cell events; integer/fixed-point; Phase 1 first ≈ 80% feel,
  Phase 2 = chains + loot/doors). Blocked on the core route (NearGas L1→…→I2) delivering grid+Step+lockstep;
  schedule its own slice PLAN then. Owner-approved direction 2026-07-13.
- Mandatory network leg: 2-machine FishNet proof that "authoritative grid-ballistics + local cosmetic ragdoll"
  stays consistent across machines when bodies fly/bounce/chain. Queue with the grid-ballistics core slice.

## decisions_needed

None. (Owner gave the verdict + track/order approval + gitignore go-ahead in-session.)

## play_check

- Orient (read NOW/KERNEL/skill + verify delivery in product repo): done.
- Owner-eye gate for P2a0 (owner): done — owner's actual words «Кандидат A — да» (played the spike 2026-07-12,
  confirmed in-session 2026-07-13).
- Structure decision — where the follow-on work lives (owner): done — owner approved «трек ... ок» (Option A:
  character presentation track g-6d4e; grid-ballistics stays a g-9c41 core slice) and the plan-first / drop-in
  prefab-first ordering «поехали».
- Housekeeping (owner): done — owner «gitignore делай» → RootMotion ignored, product commit f2f860b7 (no push).
- Apply state_changes + LOG + history + commit (self-writer): done.

## log

2026-07-13 — map/close (g-9c41→g-6d4e/M1-P2a0, s-map-characters-track-p2a0-close-001): owner-eye closed P2a0 = Candidate A; M1-P2a0 done; parallel track g-6d4e «Игровые персонажи» stood up; grid-ballistics named as future g-9c41 core slice; PLAN c-plan-characters-001 opened; RootMotion gitignored@f2f860b7; gas spine L1 PLAN-amend stays next.

## next

- READY (parallel track, owner-cadence): `work/c-plan-characters-001-call.md` — character-system roadmap +
  first drop-in slice spec.
- Priority-1 spine (UNCHANGED NOW.next): `work/c-exec-near-gas-core-authority-001-plan-amend-001-call.md`.

END_OF_FILE: live/indie-game-development/history/2026-07-13-s-map-characters-track-p2a0-close-001.md
