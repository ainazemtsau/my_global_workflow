# NOW — indie-game-development

active_bet: none

active_tasks: []

recurring: []

open_calls:
  - id: c-map-001
    to: session
    direction: indie-game-development
    play: map
    node: g-a7f2
    goal: |
      Build the first co-created goal map for the newly framed indie-game-development direction, starting from the approved charter and root. Produce candidate top-level branches one artifact at a time for owner approval. Include a bounded, selective archive analysis plan rather than blind migration.
    context: |
      Read:
      - live/indie-game-development/CHARTER.md
      - live/indie-game-development/TREE.md
      - archive/directions/indie-game-development/** only as evidence, not state

      Approved frame summary:
      - Mission: solo-developed co-op Steam game around gas + grid + expedition systems; both technical pride and real revenue matter.
      - Six-month money gate: by 2026-12-11, some external paid validation must exist; recommended stronger signal is at least $1,000 gross external money or signed funding commitment.
      - Concept status: gas+grid / expedition is the default foundation, but can be challenged by a dedicated evidence-based audit.
      - Archive status: old material is evidence-only; import selectively with explicit justification.
      - Product repo is unresolved: options include nearly empty current repo, old repo with existing code, or fresh start.
      - Owner has strong engineering/time availability but weak existing audience/social workflow.
      - No site/marketing/Steam materials repo exists yet.

      Candidate map outcomes captured during frame:
      - commercial validation / six-month money gate branch;
      - technical proof branch for gas+grid/destruction/networking feasibility;
      - co-op gameplay proof branch;
      - audience workflow branch;
      - Steam product/release path branch;
      - concept positioning audit branch;
      - archive/code/docs selective audit branch;
      - product repo decision branch.
    boundaries: |
      Do not create implementation tasks.
      Do not shape a bet yet.
      Do not import archive material wholesale.
      Do not lock the product repo without explicit owner approval.
      Do not revise CHARTER.md or TREE.md root unless the session explicitly becomes a charter/root revision under the proper play.
      Follow G9: present each tree node/artifact one at a time and require explicit owner approval before it enters state_changes.
    done_when: |
      TREE.md has an owner-approved first-level goal map under root, with each child carrying id, goal, why, done_when, status.
      Any archive-derived item included in the map has an explicit source pointer and justification.
      NOW.md points to the next appropriate session after map: likely shape for the riskiest early bet.
    return: |
      RESULT packet with exact TREE.md/NOW.md state_changes, captures, decisions_needed, log line, and next CALL.
    budget: one session

decision_inbox: []

next: |
  CALL c-map-001
  to: session
  direction: indie-game-development
  play: map
  node: g-a7f2
  goal: |
    Build the first co-created goal map for the newly framed indie-game-development direction, starting from the approved charter and root. Produce candidate top-level branches one artifact at a time for owner approval. Include a bounded, selective archive analysis plan rather than blind migration.
  context: |
    Read:
    - live/indie-game-development/CHARTER.md
    - live/indie-game-development/TREE.md
    - archive/directions/indie-game-development/** only as evidence, not state

    Approved frame summary:
    - Mission: solo-developed co-op Steam game around gas + grid + expedition systems; both technical pride and real revenue matter.
    - Six-month money gate: by 2026-12-11, some external paid validation must exist; recommended stronger signal is at least $1,000 gross external money or signed funding commitment.
    - Concept status: gas+grid / expedition is the default foundation, but can be challenged by a dedicated evidence-based audit.
    - Archive status: old material is evidence-only; import selectively with explicit justification.
    - Product repo is unresolved: options include nearly empty current repo, old repo with existing code, or fresh start.
    - Owner has strong engineering/time availability but weak existing audience/social workflow.
    - No site/marketing/Steam materials repo exists yet.

    Candidate map outcomes captured during frame:
    - commercial validation / six-month money gate branch;
    - technical proof branch for gas+grid/destruction/networking feasibility;
    - co-op gameplay proof branch;
    - audience workflow branch;
    - Steam product/release path branch;
    - concept positioning audit branch;
    - archive/code/docs selective audit branch;
    - product repo decision branch.
  boundaries: |
    Do not create implementation tasks.
    Do not shape a bet yet.
    Do not import archive material wholesale.
    Do not lock the product repo without explicit owner approval.
    Do not revise CHARTER.md or TREE.md root unless the session explicitly becomes a charter/root revision under the proper play.
    Follow G9: present each tree node/artifact one at a time and require explicit owner approval before it enters state_changes.
  done_when: |
    TREE.md has an owner-approved first-level goal map under root, with each child carrying id, goal, why, done_when, status.
    Any archive-derived item included in the map has an explicit source pointer and justification.
    NOW.md points to the next appropriate session after map: likely shape for the riskiest early bet.
  return: |
    RESULT packet with exact TREE.md/NOW.md state_changes, captures, decisions_needed, log line, and next CALL.
  budget: one session

END_OF_FILE: live/indie-game-development/NOW.md
