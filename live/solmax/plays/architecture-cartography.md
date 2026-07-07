# Play: local/architecture-cartography

Purpose: map ONE operating-substrate architecture/spec cluster before any
architecture-forge session freezes answers. This play does not design the
substrate. It makes the next architecture questions clear: what must be
discussed first, what must be discussed together, what is downstream, what
needs best-practice research, what needs proof anchors, and what returns to
the graph if a later forge session finds a gap.

Reads: CHARTER.md, TREE.md, NOW.md, relevant knowledge/, named history/
sessions, source artifacts named in the CALL, and any owner-provided notes
for the cluster.

Writes: no architecture cards directly. RESULT may propose exact state
changes, work/ artifacts, knowledge candidates, LOG line, history file and
next CALL. CHARTER/TREE edits still require explicit owner approval per G9.

Precondition: owner or a prior checkpoint names an operating-substrate
architecture/spec cluster that is too broad, repeatedly mis-forged, or likely
to hide prerequisite questions.

## Steps

1. **Frame cluster** — name the cluster, anchor question, why cartography is
   needed, and the owner symptom or evidence that triggered it.
2. **Inventory** — list existing decisions, partial evidence, rejected
   alternatives, owner corrections, candidate source artifacts and known
   non-authorities. Do not answer the design.
3. **Plain questions** — rewrite each candidate node as a simple
   owner-facing question. If it cannot be stated plainly, mark it unclear.
4. **Classify graph** — for max 15 nodes, assign:
   `plain_question`, `why_it_matters`, `answer_shape`, `status`,
   `dependency_type`, `blocks`, `do_not_solve_here`, `needs_research`,
   `needs_anchor`, `confusion_traps`, `forge_handoff`.
5. **Route** — recommend the next architecture-forge call, 1-2 alternatives,
   and why the rejected routes are worse.
6. **Owner sign (owner)** — owner approves the map, steers it, or asks to
   split/re-run. No graph is treated as accepted without owner words. `(owner)`

## Field values

`answer_shape`: invariant / state_model / procedure_model / interface_model /
call_protocol / scenario_grammar / taxonomy / proof / evaluation_rubric /
repo_boundary / open_research.

`status`: ready / needs_preface / blocked / downstream / research_first /
proof_later / unclear.

`dependency_type`: hard_prerequisite / co_frame / downstream /
research_prerequisite / proof_downstream / implementation_downstream /
consumer_specific / owner_policy.

`needs_research`: none / best_practice / comparable_systems /
failure_cases / tool_capability / evaluation_methods.

`needs_anchor`: none / owner_transcript / scenario / diagram /
source_artifact / prototype_trace / external_case.

`forge_handoff` must include: `plain_question`, `why_now`, `must_decide`,
`must_not_decide`, `parent_locks`, `expected_answer_shape`,
`first_owner_question`, `return_to_graph_if`.

## Done when

RESULT contains an owner-readable architecture/spec cluster map; every node
has the graph fields above; dependencies explain WHY they block; next
architecture-forge CALL is ready; gap/rebalance rule is stated; owner
approval words are cited; no substrate answer is frozen.

## Gap rule

If later architecture-forge finds a hidden prerequisite, unclear plain
question, wrong answer shape, missing research/proof need, or owner says the
session is going the wrong way, it checkpoints a `gap_event` and returns to
this play instead of inventing architecture.

END_OF_FILE: live/solmax/plays/architecture-cartography.md
