# Play: local/canon-cartography

Purpose: map ONE canon cluster before `local/canon-forge` freezes cards. This play does not answer canon. It makes the next canon questions clear: what must be discussed first, what must be discussed together, what is downstream, what needs visual/proof anchors, and what returns to the graph if a forge session finds a gap.

Reads: the cluster's open question notes, frozen parent cards, area MOC, relevant `live/indie-game-development/history/` sessions, `TREE.md` node `g-d3a8`, `CHARTER.md`, and mechanic/lore/art knowledge gates when relevant.

Writes: no canon cards directly. RESULT may propose exact question-note/MOC/play updates for a writer. OS state changes only through RESULT: LOG line, history file, captures, decisions, next CALL.

Precondition: owner or a prior checkpoint names a canon cluster that is too broad, repeatedly mis-forged, or likely to hide prerequisite questions.

## Steps

1. **Frame cluster** — name the cluster, anchor question, why cartography is needed, and the owner symptom that triggered it.
2. **Inventory** — list existing frozen parents, open/downstream questions, rejected alternatives, and owner corrections. Do not answer the design.
3. **Plain questions** — rewrite each candidate node as a simple owner-facing question. If it cannot be stated plainly, mark it unclear.
4. **Classify graph** — for max 15 nodes, assign:
   `plain_question`, `why_it_matters`, `answer_shape`, `status`, `dependency_type`, `blocks`,
   `do_not_solve_here`, `needs_anchor`, `confusion_traps`, `forge_handoff`.
5. **Route** — recommend the next canon-forge call, 1–2 alternatives, and why the rejected routes are worse.
6. **Owner sign (owner)** — owner approves the map, steers it, or asks to split/re-run. No graph is treated as accepted without owner words. `(owner)`

## Field values

`answer_shape`: invariant / payload_model / loop_spine / scenario_grammar / taxonomy / visual_plate / equipment_model / economy_model / proof.

`status`: ready / needs_preface / blocked / downstream / proof_later / unclear.

`dependency_type`: hard_prerequisite / co_frame / downstream / visual_anchor / implementation_downstream / economy_downstream / proof_downstream.

`needs_anchor`: none / verbal_scene / diagram / visual_plate / greybox.

`forge_handoff` must include: `plain_question`, `why_now`, `must_decide`, `must_not_decide`, `parent_locks`, `expected_answer_shape`, `first_owner_question`, `return_to_graph_if`.

## Done when

RESULT contains an owner-readable cluster map; every node has the graph fields above; dependencies explain WHY they block; next canon-forge CALL is ready; gap/rebalance rule is stated; owner approval words are cited; no canon answer is frozen.

## Gap rule

If later canon-forge finds a hidden prerequisite, unclear plain question, wrong answer shape, visual/proof need, or owner says the session is going the wrong way, it checkpoints a `gap_event` and returns to this play instead of inventing canon.

END_OF_FILE: live/indie-game-development/plays/canon-cartography.md
