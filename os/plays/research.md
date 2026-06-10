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

END_OF_FILE: os/plays/research.md
