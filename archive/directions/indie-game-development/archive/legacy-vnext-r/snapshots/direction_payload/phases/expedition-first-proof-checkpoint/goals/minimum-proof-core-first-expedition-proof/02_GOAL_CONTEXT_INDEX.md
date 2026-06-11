# 02 Goal Context Index

## Load rules

```
goal_context_loading:
  default_when_triggered:
    - "00 Goal Contract / Brief"
  request_only:
    - "01 Goal Working Context"
    - "Sessions"
    - "Wave Cards"
    - "Decisions"
    - "Goal Brief"
    - "Execution Pack"
    - "Game Documentation / Expedition Skeleton Document"
    - "Game Documentation / Expedition Proof Handoff"
    - "Game Documentation / Expedition Experience Model"
    - "Game Documentation / Technical Foundation - Gas and Grid Contract"
  pointer_only:
    - "03 Waves"
    - "04 Execution Log"
  archive:
    - "archived/historical material"

```

## Stop rules

Stop before execution if acceptance criteria, validation, active project root, AGENTS.md, Codex setup, or Game Documentation freshness is unclear.
