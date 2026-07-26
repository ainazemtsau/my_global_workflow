# RESULT s-repair-archive-quarantine-001

direction: indie-game-development
play: repair
node/task: g-0c26/archive-quarantine
date: 2026-07-26

## outcome

The owner asked for cleanup mode: physically remove invalid material from the working
tree, keep required evidence only in a place agents do not read by default, and make
that boundary enforced rather than advisory. He chose option A (move to the frozen
archive rather than hard-delete) and required that Codex and Claude Code stop reading
there by default.

Named contradiction: `live/**` carried 1,250,000 words against 9,000 words of current
state (136:1). 205 CALL artifacts existed for one live CALL; 34 retired Launch Control
files still read `ACCEPTED`/`ПРИНИМАЮ`; the one knowledge entry every morning session is
obliged to read named a planning frontier that closed on 2026-07-25. An assistant asked
"what next" found dated Steam milestone tables only inside the retired track.

825 pre-reset files were moved to `archive/directions/indie-game-development/2026-07-pre-reset/`,
the ledger was rotated to the 2026-07-24 reset boundary, every hot-state pointer was
verified to resolve, and default archive reads are now blocked in both agent harnesses
with one named override token. No file was deleted; all bytes remain in Git and on disk.

Live direction: 900 files / ~1,250,000 words -> 74 files / ~110,000 words.

## evidence

- Kept live: `history/` 24 files (38,978 words, all dated >= 2026-07-24); `work/` 26 files
  (~53,000 words: the set cited by CHARTER/TREE/NOW/knowledge, plus one file named by a live receipt); `knowledge/` 25
  files; `plays/` removed (0 files).
- Moved: `history/` 484 files (674,725 words), `work/` 330 files (~524,000 words),
  `plays/` 11 files (4,019 words) = 825 files. 10 emptied directories pruned.
- Selection rule (mechanical, not judgement): a `work/` file stays live only if a current
  hot-state file names it. History cut at the 2026-07-24 reset boundary. All 11 local
  plays were obsoleted by that reset and none is named by hot state.
- `LOG.md`: 80 lines dated 2026-07-21..23 moved verbatim into the rotated ledger; 24 lines
  (2026-07-24..26) remain, matching the 24 kept receipts one-for-one; one pointer line
  remains.
- Pointer integrity: 11 hot-state citations of moved receipts repointed to their archive
  paths. 13 pointers that were ALREADY broken before this leg were diagnosed as mis-pathed
  rather than missing — 12 targets existed at `work/archive/<name>.md`, and
  one target was a knowledge entry recorded under a `work/` prefix. All 13
  repaired. Measured after repair: **0 dangling pointers** from CHARTER, TREE, NOW, LOG and
  all 25 knowledge entries.
- Enforcement, verified first-hand this session: `.claude/settings.json` denies
  `Read`/`Glob`/`Grep` on `archive/**` — a `Read` of `archive/README.md` and a `Grep` over
  `archive/` were both refused. `.codex/guard/` gained `blocks_archive_read`, wired into the
  existing `PreToolUse`/`PostToolUse` chain, gated by `owner_ack_archive_read:<id>`; writes
  INTO the archive stay allowed so material can always be moved in. Guard suite: 21 tests, all
  pass (5 new: read blocked, shell read blocked, ack override, write allowed, and a
  false-positive guard proving `LOG-archive-...md` is not treated as an archive path).
- `AGENTS.md` archive line now states the default-closed rule and the override token.

## state_changes

Applied to `live/indie-game-development/`:

1. `history/` — 484 pre-reset receipts moved to the archive; 24 remain.
2. `work/` — 330 uncited outputs moved to the archive; 26 remain (`canon-collaboration-profile-v1.md` kept live: a 2026-07-26 receipt names it).
3. `plays/` — all 11 local plays moved to the archive; the directory is removed.
4. `LOG.md` — 80 pre-boundary lines rotated verbatim into the archived ledger; pointer
   updated to the rotated ledger inside the archive.
5. `knowledge/strategy-reset-boundary.md` — false frontier corrected to the live authoring
   CALL `c-work-october-demo-basis-authoring-001`; the closed map CALL named as closed; the
   owner-approved concept frame named as a source but not canon; archive boundary recorded.
6. `knowledge/` — 4 entries repaired (13 mis-pathed pointers).
7. `NOW.md` — header `updated`; issues `i-history-integrity` and `i-knowledge-links` removed
   with disposition (both concerned pointer/receipt integrity, now measured at zero dangling);
   one issue added: `i-knowledge-concept-triage`.
8. `history/2026-07-26-s-repair-archive-quarantine-001.md` — this file.

Outside `live/**`: `archive/directions/indie-game-development/2026-07-pre-reset/**` created;
`.claude/settings.json` created; `.codex/guard/policy.json`, `.codex/guard/codex_guard.py`,
`.codex/guard/tests/test_codex_guard.py`, `AGENTS.md` amended.

Not changed: `CHARTER.md`, `TREE.md`, `os/**`, any play, the open CALL
`c-work-october-demo-basis-authoring-001`, product and Steam state. `bet` stays `null`;
`tasks` stays `[]`; no track, no dashboard, no numeric chance. Nothing was deleted.

## decisions

Owner words this session: `давай вариант A но нужно еще сделать так что бы codex и claude
code по умолчанию туда не лазили только если реально нужно`. Option A = move to the frozen
archive rather than hard-delete, plus enforced default-closed reads. Both realized.

## captures

- `TREE.md` `g-7b42.why` still orders the Steam branch after the first playable proof, which
  the owner reversed on 2026-07-25. Deliberately NOT touched here: TREE is G9 owner-approved
  content and belongs to `map`. Already routed as `i-steam-sequence-tree` (due 2026-08-11).
- The product repo `gas_coop_game` was deliberately not cleaned. It holds 10 laboratory
  scenes with only Unity's empty `SampleScene` in the build list; which of them survives is
  decided by the Demo Basis, and `CHARTER.md:78` forbids deleting existing code before its
  role is redecided.
- 23 of 25 knowledge entries were accepted in the gas/grid era. Their pointers now resolve
  but their meaning under the new concept is unverified — raised as `i-knowledge-concept-triage`.

## play_check

- Step 1 name the contradiction — done: dead artifacts indistinguishable from live ones,
  and one knowledge entry naming a closed frontier.
- Step 2 reconstruct — done newest-first from hot state and Git; selection is mechanical
  (hot-state citation closure), not model judgement.
- Step 3 corrected state — false routing surface fixed; every outstanding fact preserved;
  authority separated from evidence; no invented progress.
- Step 4 owner confirm — owner authorized option A and the read block in chat; the batched
  manifest is reported with this RESULT.
- Step 5 friction — none new. Physical relocation of `history/**` exceeds what `repair`
  normally authorizes (tombstones and banners); it proceeded on the explicit live owner
  instruction, which outranks the kernel per `os/KERNEL.md` authority order.

## log

2026-07-26 · s-repair-archive-quarantine-001 · repair · direction · g-0c26/archive-quarantine

## next

`c-work-october-demo-basis-authoring-001` remains the sole ready frontier, unchanged.

END_OF_FILE: live/indie-game-development/history/2026-07-26-s-repair-archive-quarantine-001.md
