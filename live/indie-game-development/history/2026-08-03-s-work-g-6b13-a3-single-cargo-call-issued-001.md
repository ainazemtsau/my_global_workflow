# RESULT — s-work-g-6b13-a3-single-cargo-call-issued-001

call: c-work-single-cargo-frontier-001
direction: indie-game-development
track: переноска
play: work
node/task: g-6b13 / a-3
date: 2026-08-03

## outcome

The a-3 engineering CALL is written and registered: `c-exec-one-carries-cargo-proba-001`, contract
36, mode ПРОБА, basis `cca530a01c49f38f676942a531c2ee837ebe2454`, slot WIN-U3. It carries the
non-negotiable form already recorded in NOW — the cargo is an independent object, never parented to
a player, and the host computes its pose from a holder LIST whose length is one in this task, with
each entry already carrying its own target, force and eviction right and the cargo carrying its home
point — plus the owner-visible two-window check and the one legitimate headless test class.

Nothing was launched: no slot claimed, no lease taken, no product byte written. The session CALL is
retired from dispatch and its file marked; the engineering root replaces it in `open_calls`.

Three things in the incoming CALL's own context were re-verified rather than trusted, and all three
held. The declared terminal tip IS the current `origin/main`. The real selector — not the previous
leg's report — says WIN-U3 is `CLEAN / AVAILABLE / lease none`. Contract 36 with PROBA as the
default really is the product's live contract.

One mechanical trap was found and defused for the executor: the slot selector must be run from a
worktree standing on the current base. `C:\projects\Unity\GasCoopGame` (primary, `main`) is still
parked on the pre-cut `c75015a8`, and that older `select-slot.ps1` looks for the shared state under
`.git\`, where it no longer lives — it throws for all four slots. The current selector reads
`C:\projects\Unity\GasCoopGame_slot-state\gascoop-slot-state.v1.json` and answers correctly. A leg
that had trusted the first, failing run would have reported a false blocker.

## evidence

- Direction base for this leg: `origin/main` = local `HEAD` = `52d1b6ac`, clean worktree, re-fetched
  immediately before writing state; the хозяин lane had committed nothing in the interval.
- Declared product basis verified: `git rev-parse origin/main` in `C:\projects\Unity\GasCoopGame`
  equals `cca530a01c49f38f676942a531c2ee837ebe2454` exactly, the tip the closing Control task
  recorded. `origin/dev` is the same commit.
- Slot authority, first-hand: `pwsh -NoProfile -File tools/select-slot.ps1 -Slot WIN-U3` run from
  `C:\projects\Unity\GasCoopGame_dev` printed `SLOT_SELECTION v3`, `state-authority:
  C:\projects\Unity\GasCoopGame_slot-state\gascoop-slot-state.v1.json`, `head:
  fa79613c4c0d4fc88115e733c8a9a468b72f2e01`, `state: CLEAN`, `lifecycle: AVAILABLE`, `lease: none`,
  `availability: AVAILABLE`. U1, U2 and U4 report the same availability; all four are free.
- `git merge-base --is-ancestor fa79613c cca530a0` succeeds, so bringing WIN-U3 to the declared base
  is a fast-forward, not a merge or reset. The CALL says so and names it as the first action.
- Contract: `validation.config` on `origin/main` carries `"synced_contract_version": 36` and the v36
  note "PROBA is the DEFAULT mode for every new leg"; `AGENTS.md:286` carries the Russian clause
  «ДВА РЕЖИМА, ПО УМОЛЧАНИЮ — ПРОБА (контракт v36)». The incoming CALL's claim is true.
- Every path named in the issued CALL was resolved with `git ls-tree cca530a0 -- <path>` in the
  product repository and its blob recorded in the CALL's own table — sixteen paths, all present.
  The four accepted movement blobs match the a-1b/a-2 baseline exactly: `MovementInput.cs`
  `6427b8091e84`, `PlayerMovement.cs` `2346fe651cff`, `PlayerMovement.Rule.cs` `bfe9aa1dd6cb`,
  `PlayerState.cs` `df4a754f6a34`.
- The seam the CALL builds on was read, not assumed: `AuthoritativeWalkerRoster` holds the walker
  list in the engine-free assembly and steps it through `PlayerMovement.Step`;
  `NetworkWalkerCourier` transports input to the server and publishes `WalkerSnapshot[]` from the
  server tick, applying the same snapshot locally; `NetworkPlaySettings` holds every tuning number.
  `TunnelCrew.Core.asmdef` still carries `noEngineReferences: true`.
- `core/TunnelCrew.Core.csproj` includes `..\Assets\TunnelCrew\Core\**\*.cs` recursively, so new
  rules-layer files reach the headless build and tests without project surgery. The CALL states this
  so the executor does not invent it.
- Sources read before writing: fresh `NOW.md`, `TREE.md` card g-6b13, `CHARTER`-approved lenses via
  NOW, `knowledge/how-the-game-is-built-layers.md`,
  `knowledge/no-checks-the-owner-makes-by-eye.md`, `knowledge/lobby-is-not-a-crutch.md`,
  `work/notes-two-carry-one-body-2026-08-02.md`, issues
  `i-owner-standing-rule-extend-never-rebuild-001`,
  `i-architecture-pass-skipped-for-this-bet-001`, `i-call-named-path-absent-on-declared-basis-004`,
  `i-closing-report-ownership-unclear-001`, `i-plan-receipt-fabricated-owner-verdict-001`,
  `i-ready-made-tools-scan-2026-08-03-001`, and the retired a-1b engineering CALL as a format
  reference.

## what the CALL had to carry, and why each line is there

- **No owner architecture pass is owed here.** `i-architecture-pass-skipped-for-this-bet-001` names
  exactly two places that need one — a-4 and b-2 — and lists «один несёт» among the nine tasks that
  do not. The layering decision this lane could have got wrong was already made and accepted after
  the a-2 rejection; the CALL cites it instead of reopening it.
- **The holder fields stay FIELDS.** The CALL states twice that force, eviction right and a second
  entry get no meaning, no computation and no test in this task, because deciding what two holders
  do would decide a-4 for the owner. It adds one zero-cost recommendation (with one holder the pose
  IS that entry's target) explicitly marked as not binding, so the fields do not end up decorative.
- **The four movement blobs are named byte-for-byte as unchangeable**, and «взять» is stated not to
  be movement, so it cannot leak into `MovementInput`. Their unchanged bytes were the acceptance
  proof of a-2 and a-1b.
- **The courier may grow, but may not get smart.** A new intent field and a new cargo entry in the
  snapshot are the courier doing its defined job with a wider payload; any decision inside the
  courier or the presentation is forbidden and is a STOP home. This is written as a boundary rather
  than left to reading, because the layering doc's STOP clause would otherwise be ambiguous exactly
  here and could produce a false blocker.
- **One packet, one world.** Cargo travels in the same snapshot and the same tick as the walkers,
  because a client that mixes a fresh walker with a stale cargo is precisely the two-screen
  divergence the done_when forbids.
- **`NetworkTransform` is banned by name** — its client-authoritative mode is the second
  NavMeshAgent living inside an already-accepted tool (issue `i-ready-made-tools-scan-…-001`, line
  1); this is the first CALL after that research where the temptation is real.
- **The sole-holder disconnect is answered without inventing gameplay**: the list empties and the
  cargo stays. The notes flagged «what the engine does with the cargo when a player leaves» as a
  courier-class STOP; the no-parenting rule structurally removes the danger, so the cheap true
  answer is stated instead of a question.
- **Tests are restricted to the one invisible thing** — the shape of the data and that the pose is
  computed outside Unity — with the by-eye class banned by name.
- **The closing report is assigned to the leg itself with an honest status**, and red `-Deliver` on
  a slot branch is declared normal. `i-closing-report-ownership-unclear-001` stays open until a leg
  reads that rule correctly; this CALL is the first test of the rewritten paragraph.
- **Verbatim-owner fields must hold his actual Russian words or stay empty** — carried forward from
  `i-plan-receipt-fabricated-owner-verdict-001` as that issue's `review_when` requires.
- **The lobby is protected**: the CALL says explicitly that it is not a crutch and stays, so the
  a-1b phrase «ни лобби, ни экранов» cannot be copied into a networked task.

## state_changes

- `NOW.md`: set `updated` to this session.
- `NOW.md/open_calls`: remove the completed session root `c-work-single-cargo-frontier-001` and add
  the engineering root `c-exec-one-carries-cargo-proba-001` (`to: executor`, `kind: engineering`,
  `status: ready`, contract 36, mode ПРОБА, basis `cca530a0…`, slot WIN-U3) with the first-hand
  verification note. The хозяин lane's `c-work-host-first-reaction-frontier-001` is untouched, so
  the owner-approved `track_wip_limit: 2` still holds with one root per lane.
- Add `work/c-exec-one-carries-cargo-proba-001-call.md` — the complete engineering CALL.
- Add a retirement banner to `work/c-work-single-cargo-frontier-001-call.md`; its prior bytes remain
  in Git and it is no longer dispatch authority.
- Prepend the LOG receipt. No task status, issue, forecast, bet, track, CHARTER, TREE, knowledge or
  product byte changes; a-3 stays `open` because only the owner's eye closes it.

## captures

- The owner asked in this leg whether the **Final IK** plugin is needed. It is not, and the answer
  needed no new research: the 2026-08-03 ready-made-tools sweep already placed Final IK in the
  ПОКАЗ/КРАСОТА band — «брать позже — единственное место, где он реально окупается» — with two parts
  (`Grounder`, Interaction System `pickUp`) to be forbidden by name because they would move «where
  the character is» and «where the cargo is» into a foreign asset. It buys nothing for a-3: the
  truth about the cargo is our own rules-layer arithmetic, and the stand runs on primitives with no
  rig at all. Recorded as a capture, not as a requirement or a purchase.
- Product-side observation worth one line for whoever next touches slots: the primary worktree
  `C:\projects\Unity\GasCoopGame` still sits on `c75015a8`, whose older `select-slot.ps1` looks for
  the shared slot state under `.git\` and therefore throws for all four slots. Run the selector from
  `GasCoopGame_dev`. Not filed as a Direction issue — it is a stale checkout, not a defect, and it
  disappears the moment that worktree is updated.

## decisions_needed

None. The CALL is dispatchable as written. The one gameplay-shaped detail inside it — which key
takes the cargo and from how close — is deliberately left to the ПРОБА loop rather than carried to
the owner as a menu: he runs it, and it changes in the same session on his word.

## play_check

- 1 recite: done — goal and done_when restated against task a-3 of the active bet g-6b13, lane
  переноска; the CALL serves the bet and no foreign work was selected.
- 2 owner inputs: **none required, and the reason is not silence.** The owner will operate the
  result, but every fact only he can know is already recorded: the task's own done_when («подошёл,
  взял, понёс, положил»), the mandatory form (independent cargo, holder list, no parenting), the
  seven-field seam from the b-1 expertise, and the standing extend-never-rebuild rule. The remaining
  open question of this lane — physical body versus computed pose — belongs to a-4 with two holders;
  for one holder NOW already fixes the computed form. G7 is satisfied: no product concept or
  gameplay was invented, and nothing was widened into a standing ban on asking.
- 3 do the work: done — the bounded outcome is the registered engineering CALL; product execution
  was NOT launched, per the incoming CALL's explicit return clause.
- 4 self-check against done_when, point by point: fresh exact v36 PROBA executor CALL — yes,
  contract 36 and mode ПРОБА named in the header; current product basis — yes, `cca530a0`, verified
  equal to `origin/main`; a real AVAILABLE slot — yes, WIN-U3 by the real selector, with the
  fast-forward stated; the independent-cargo / holder-list / host-authority invariant — yes, as its
  own non-negotiable section; the owner-visible two-copy check — yes, written in his language as the
  acceptance; focused headless evidence — yes, three shape tests plus build/check and the four
  unchanged blobs. No blocker was needed, and no route was invented.
- 5 close: done — same-lane continuation is the issued engineering root; a-3 is not the last bet
  task, so review is not opened. Unrelated state preserved.

## log

g-6b13/a-3: выпущен инженерный наряд ПРОБЫ на один самостоятельный груз; база, слот и контракт
перепроверены первой рукой, продуктовая работа не запускалась

## next

Dispatch `c-exec-one-carries-cargo-proba-001` to a product executor session as a fresh chat in
`C:\projects\Unity\GasCoopGame_win-u3`. It returns HOME to this direction on its terminal report or
a genuine blocker; the Direction close for a-3 needs the owner's own two-window verdict plus a fresh
refutation session, exactly as a-2 and b-1 closed. The хозяин lane continues independently on
`c-work-host-first-reaction-frontier-001`.

END_OF_FILE: live/indie-game-development/history/2026-08-03-s-work-g-6b13-a3-single-cargo-call-issued-001.md
