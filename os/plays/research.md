# Play: research

Purpose: answer one bounded question for a parent session (child session; children may spawn their own children the same way).

Reads: the CALL packet only — it must be self-contained (pointers to any needed files).
Writes: nothing directly; findings return via RESULT to the parent. A knowledge candidate may be proposed, never written.

## Steps

1. **Recite** — restate the question, the expected return format, and the budget from the CALL. If the question is actually several questions, answer the first and report the split — do not silently expand.
2. **Investigate** — within budget. Web, documents, analysis of provided material — whatever the question needs. Track sources.
3. **Confidence** — separate what is established (with sources) from what is inference. State what would change the answer.
4. **Close** — RESULT: findings in the requested format, sources, confidence and limits, optional knowledge candidate, log line, next = return-to-parent marker (the parent's id from the CALL).

## Done when

The question is answered in the requested format within budget, or a budget/feasibility limit is reported with partial findings.

## Notes

- A research child never makes decisions for the parent and never touches state. It informs.
- If the answer reveals work to do, that is a capture in the RESULT — the parent or shape triages it.
- Respect the budget literally: better a partial answer on time than a perfect answer that burned the budget twice over.
- Multiple generator children on one question run independently in parallel (nominal group); merge and dedupe afterwards — never a shared brainstorm thread.
- A parent may request a strategic_search child: pick ONE operator per brief (baseline-deletion / constraint-inversion / far-analogy / small-team-asymmetry / AI-leverage-with-named-evaluator / failure-inversion), ask for a distribution of structurally different variants including low-probability ones (cull weak tails), collapse synonyms with a log, return 3–5 survivors distinct on target, mechanism, proof-channel, or main assumption — each refuted once — plus a recommended first probe. The child informs, never decides.
- A parent may also send miner briefs: fetch one rare case, one far analogy, or the strongest argument against the default path — raw material for generation, not advice.
- A parent or the owner may fire `map_evidence` before a map session (standing brief; rerunnable — later runs read current state): return, each item with dated sources — (1) the current-year baseline: what the competent default path looks like NOW, with numbers; (2) how comparable ambitions actually reached this charter's success criteria, split by branch class (money/audience/distribution vs tech/gameplay), favoring rare verified cases over genre hits; (3) 2–3 evidence-anchored non-obvious path candidates; (4) the strongest argument against the baseline. Best fired on a deep-research-capable model; findings return as captures for the map session.
- An owner may fire `outside_review` as a standalone session on one direction (no parent CALL; KERNEL §2 owner-initiated research): read CHARTER.md, TREE.md, NOW.md, knowledge/; check the current course against external evidence — comparable cases, published practice, research literature, market numbers — every judgment cites its source. Return ≤5 findings, each `keep | change | investigate` with evidence and confidence; "everything holds" is a first-class outcome. Findings return as captures/decisions_needed like any research RESULT, next = awaiting_decision; tree/charter moves stay behind their gates. Best fired on a deep-research-capable model, at the owner's whim; kill the mode if two consecutive runs yield nothing the owner acts on.

END_OF_FILE: os/plays/research.md
