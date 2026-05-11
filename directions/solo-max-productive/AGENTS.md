# Solo Max Productive Direction Instructions

Status: active

Direction path: `directions/solo-max-productive`

Rules:
- Use only this Direction folder unless a task explicitly names another Direction.
- Do not invent Direction, Phase, Goal, Portfolio Queue, Context Loading Index, or execution state.
- Runtime Direction state belongs in `project_files/`.
- Reusable Direction knowledge, canon, decisions, patterns, and reviews belong in `knowledge/` and are canonical only when present as GitHub files.
- External personal notes are not runtime sources; promote needed material into this Direction folder first.
- If required state is missing, return `NEEDS_INPUT`; do not fabricate it.
