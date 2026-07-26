# RESULT — s-cartography-core-concept-rebuild-001

session: s-cartography-core-concept-rebuild-001
date: 2026-07-09
direction: indie-game-development
node: g-d3a8
play: local/canon-cartography
call: c-cartography-core-concept-rebuild-001
canon_repo: gas_coop_game_canon @b77571b (CONSTITUTION @87a05a7)

## outcome
The core game concept now has an owner-signed rebuild spine that starts from the fixed foundations, not from the
old Bubble entrypoint. Two owner verdicts were recorded verbatim in one session:
1. CONSTITUTION.md RATIFIED — verdict «Б» (= ratify with edits П1/П2/П3). The constitution is no longer a draft.
2. Core-concept-rebuild QUESTION MAP SIGNED — verdict «А» (= «Подписываю карту»). It replaces the 2026-07-08
   QUEUE draft as the canon repo's live QUEUE.md; a full-field version lives in OS work/canon-maps/.
No canon card was frozen (INDEX still empty) — cartography maps questions, it does not answer the concept.

## evidence (matches play done_when)
- Owner-readable cluster map produced (steps 1–5), every node carries the play's step-4 graph fields
  (plain_question, why_it_matters, answer_shape, status, dependency_type, blocks, do_not_solve_here, needs_anchor,
  confusion_traps, forge_handoff with all 8 sub-fields): work/canon-maps/core-concept-rebuild-question-map-v0.1.md.
- Dependencies explain WHY they block (verbs-in-time precede tools/carry/co-op/phases; comfortable loop precedes
  reaction-layer and failure; motive gates value; promise is a synthesis, not an entry).
- Next canon-forge CALL ready: c-forge-q-ruki-001 (work/c-forge-q-ruki-001-call.md).
- Gap/rebalance rule stated (§6 of the map): a forge session hitting a hidden prerequisite / unclear question /
  wrong answer-shape / owner «не туда» checkpoints a gap_event back to the map, never invents canon.
- Owner approval words cited: step 0 «Б» (constitution), step 6 «А» (map). Both verbatim.
- No canon answer frozen; INDEX.md untouched/empty.
- П1–П3 applied to CONSTITUTION.md and committed @87a05a7; signed map committed as QUEUE.md @b77571b.

## constitution edits applied (owner verdict «Б», verbatim single word)
- П1 (palette / reactions): «Реакции — зафиксированный системный материал, но комфортная базовая игра не требует
  погони за реакциями или оптимизации дорогих газов.»
- П2 (pillar 4): «Столп не решает, что ядро игры — добыча ценности; он требует лишь: если ценность есть — она
  рождается из газа, а провал меняет мир.»
- П3 (pillar 6): «„Нового движка — ноль“ = ответ не требует движковых систем сверх существующего сима и уже
  запланированной дороги.»

## map — 10 nodes in dependency order (see work/canon-maps/ for full fields)
1 q-ruki — player verbs (МЕХАНИКА) — hard_prerequisite, blocks 2/4/5/6/7/9 — FIRST.
2 q-prostranstvo — space as a hand — co_frame to 1.
3 q-motiv — why enter the gas — blocks 4/8/10.
4 q-bazovaya-petlya — comfortable no-reaction-chase loop (from П1) — blocks 5/6/7/9/10.
5 q-reakcii-v-baze — where reactions live without becoming a required optimization (П1).
6 q-proval — failure as a world event (pillar 4).
7 q-koop — why co-op / anti-solo — mechanic-lenses gate.
8 q-cennost — value model — conditional on motive(3)=value.
9 q-fazy — run phases (quiet→scout→active) — sim-driven, not scripted.
10 q-obeshanie — one-line promise — SYNTHESIS after 1+3+4, not an entry.
PARKED with wake-nodes (nothing lost): bubble mechanic, carry, tools-list, economy+ЛЁГКИЕ/Вахта, bestiary, role
roster, title «ОНО ДЫШИТ», old canon/maps (salvage), gas visual style (track g-7e15), plus the carried-forward old
parking lot (voice/DSP, seeds, persistent floor, iron-watch, run artifact, field-brewing, contract types, trap doors).

## route (step 5)
Selected: node 1 q-ruki via local/canon-forge (Кузница v2), МЕХАНИКА mode; node 2 q-prostranstvo admissible as
co-frame. Rejected: q-motiv-first (drags extraction to center before verbs), q-obeshanie-first (whole-concept
compare, forbidden by CALL boundary), continue old Workbench Q1 spatial-form (assumes bubble-center as an entry).

## state_changes (applied by this session as its own writer, agent-CLI on this repo)
NOW.md:
  - updated: → s-cartography-core-concept-rebuild-001.
  - open_calls: removed c-cartography-core-concept-rebuild-001 (resolved); added c-forge-q-ruki-001 (READY,
    to: session, call: work/c-forge-q-ruki-001-call.md).
  - parallel_tracks g-d3a8.state: rewritten to CARTOGRAPHY DONE — constitution ratified (Б, П1–П3 @87a05a7), map
    signed (А) = QUEUE.md @b77571b + full-field work/canon-maps/, 10-node dependency order, parking with wake-nodes,
    next route node 1 q-ruki, gap rule, no canon frozen, TREE/CHARTER untouched.
  - next: → CALL c-forge-q-ruki-001 → work/c-forge-q-ruki-001-call.md.
LOG.md: one line appended (this session).
history/: this file.
work/ (products, not state): canon-maps/core-concept-rebuild-question-map-v0.1.md; c-forge-q-ruki-001-call.md.
canon repo (write access, applied after verdict + committed): CONSTITUTION.md @87a05a7 (П1–П3); QUEUE.md @b77571b
  (signed map). No canon card, INDEX untouched.

## captures
- (none new) — side ideas were already parked in the map's parking lot with wake-nodes; no fresh out-of-scope idea
  surfaced this session.

## decisions_needed
- (none) — both required owner verdicts (constitution «Б», map «А») were obtained in-session.

## play_check (local/canon-cartography)
1 Frame cluster — done: cluster = core concept rebuild from foundations; anchor + symptom (owner stopped Bubble
  route) named.
2 Inventory — done: fixed foundations, draft material, refusals (constitution NEGATIVE + pitch negative prompt),
  old canon as evidence; no design answered.
3 Plain questions — done: 10 owner-facing plain questions; none left unclear.
4 Classify graph — done: 10 nodes (≤15) with all required fields + full forge_handoff each.
5 Route — done: node 1 q-ruki recommended; 3 alternatives rejected with reasons.
6 Owner sign (owner) — done: owner verdict «А» = «Подписываю карту» (verbatim). Step-0 constitution ratification
  verdict «Б» also verbatim. Both cited above.

## log
canon-cartography (g-d3a8/core-concept-rebuild): constitution ratified «Б» (П1–П3 @87a05a7) + owner-signed 10-node
rebuild map «А» written as canon QUEUE.md @b77571b + full-field work/canon-maps/; next = q-ruki forge (МЕХАНИКА);
no canon frozen.

## next
CALL c-forge-q-ruki-001 → work/c-forge-q-ruki-001-call.md (Кузница v2, play: local/canon-forge, node q-ruki
МЕХАНИКА, node 2 co-frame admissible).

END_OF_FILE: live/indie-game-development/history/2026-07-09-s-cartography-core-concept-rebuild-001.md
