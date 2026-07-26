# Session s-canon-013 — author the local/mechanic-forge play

date: 2026-06-20
role: session (own writer; agent CLI on this repo)
play: local/canon-track (canon-forge process improvement, follow-on to s-canon-012)
node: g-d3a8 (canon track)
trigger: owner — "why is the kickoff message so complex / full of instructions? the instruction must be BAKED INTO the
  structure, not pasted separately each chat; state must persist and we must work normally from any chat".

## What happened

The owner was right, and the bloated hand-written Codex kickoff was a symptom: the mechanic-mode PROCEDURE was not in
the repo yet (held back by the s-canon-012 adoption gate), so it had to be inlined every time. His principle — the
structure carries the instruction, the kickoff is a short CALL that points at a play — is the OS working as designed
(exactly how the original c-coop-shape-001 CALL pointed at `local/canon-forge`).

Resolution: the adoption gate ("prove before encode") is superseded by the stronger structure principle. Encoding now is
safe — it is a LOCAL play, ADDITIVE (the working lore `canon-forge` is untouched), already research-backed +
stress-tested, and easy to revise. "Prove first" becomes "ship v1, refine after run 1".

## state_changes applied

1. CREATE `live/indie-game-development/plays/mechanic-forge.md` (≤600w) — the mechanic-mode forge recipe, sibling to
   `canon-forge` (lore mode, untouched). Terminus = a WORKED PLAYABLE LOOP (verb table + numbered second-by-second cycle
   + separated-player scenario), the one-line label is only an index. Steps: frame-the-real-question-in-plain-words +
   decompose → verbs-before-names → worked loop + spar → run `knowledge/mechanic-lenses.md` in order (1-5 paper =
   UNVERIFIED, 6 grey-box = CERTIFIED) → owner freeze. A "Rules of engagement" section bakes in the anti-patterns the
   prior Codex run hit (no premature A/B/C; no slogan/umbrella-jargon; no rephrasing-without-new-verb-consequence;
   ONE-on-one not a fan-out; "sim runs" ≠ fun; co-creation binding). Mechanics-first default; ONE web with lore.
2. APPEND one LOG line.

NOT touched (G1 / canon parallel): NOW.md, the active bet, TREE.md, CHARTER.md, the canon repo, and the working
`canon-forge` play.

## Effect

The Codex kickoff is now a short CALL: `to: session · play: local/mechanic-forge · node: g-d3a8 · question:
q-expedition-loop` — the procedure, lenses, rules and read-list live in the play + `knowledge/mechanic-lenses.md`. Cross-
repo note: the play + lenses live in this OS repo; the frozen canon cards live in `gas_coop_game_canon` — a forge chat
needs both, exactly as `canon-forge` already requires.

## next

First real run = forge `q-expedition-loop` ("зачем идти вглубь") via `local/mechanic-forge`. This run is also the v1
shakedown of the play — refine the play if the run surfaces gaps.

state: committed locally, merged to main + pushed (owner-requested, so other chats / Codex see it).

END_OF_FILE: live/indie-game-development/history/s-canon-013.md
