# Sunday Planning Packet v0 — life-reset

Repair note, 2026-06-20:

This packet is input evidence, not the current next step. The owner clarified
that Direction OS should create and govern a separate life-reset runtime rather
than become the weekly/daily runtime itself. Current authority is
`live/life-reset/NOW.md`; run the runtime-boundary CALL there before using this
packet for the first real Weekly Contract.

Target planning session: Sunday evening, 2026-06-21
Target week: 2026-06-22..2026-06-28
Output to produce: `live/life-reset/work/week-2026-06-22-contract-v0.md`

## 0. What this packet is

This is the small owner-facing packet for accepting the first real Weekly
Contract. It is intentionally not a new planning system, daily runtime, backlog,
module framework, tool choice, or source-direction roadmap.

Use this packet in ChatGPT Project, Claude Web, Codex, or Claude Code as a
Direction OS `work` session. The session drafts the contract from the inputs
below and ends with one RESULT. Durable writes happen only through the existing
session/writer flow:

- ChatGPT Project / Claude Web: session only; emit RESULT or write request.
- Codex / Claude Code: may run the session and then mechanically apply its own
  RESULT as writer under `os/adapters/coding-agent.md`.
- No chat history is durable state. The accepted contract file and RESULT are.

Basis:

- `live/life-reset/NOW.md`
- `live/life-reset/CHARTER.md`
- `live/life-reset/TREE.md`
- `live/life-reset/work/weekly-operating-graph-dry-run-v0.md`
- `os/KERNEL.md`
- `os/plays/work.md`
- `os/adapters/SESSION_PAYLOAD.md`
- `os/adapters/chatgpt-project.md`
- `os/adapters/claude-project.md`
- `os/adapters/coding-agent.md`

The larger dry-run is evidence and background. Do not copy it into the contract.
The contract should only contain the refreshed week facts, selected slices,
explicit cuts, change rule, owner acceptance, and evidence pointers.

## 1. Sunday inputs

Collect these before selecting the week.

### 1.1 Calendar and capacity

```yaml
week:
  dates: 2026-06-22..2026-06-28
  planning_date: 2026-06-21
  fixed_commitments:
    - ""
  family_obligations:
    - ""
  immovable_errands:
    - ""
  low_capacity_windows:
    - ""
  likely_interruption_risks:
    - ""
  desired_focus_windows:
    - ""
  deep_work_blocks_available:
  admin_light_blocks_available:
  owner_decision_blocks_available:
  recovery_buffer:
```

If the calendar or capacity is unknown, do not fake precision. Use conservative
capacity, make the contract smaller, and record what remains unknown.

### 1.2 Owner state and intention

This is planning signal, not diagnosis.

```yaml
owner_state:
  energy_now:
  practical_stability:
  biggest_pressure:
  what_would_make_week_successful:
  what_would_be_too_much:
  likely_overpromise:
  likely_avoidance:
  one_alive_but_not_overloading_thing:
```

### 1.3 Source refresh

Read fresh NOW files or accepted summaries. Life-reset imports summaries only;
the source directions remain source of truth.

```yaml
sources:
  indie_game_development:
    current_next:
    status: ready | blocked | active | held | awaiting_owner | done
    owner_decisions:
    risks:
    week_candidate:
    life_reset_can_import:
    life_reset_must_not_touch:

  health:
    current_next:
    status: ready | blocked | active | held | awaiting_owner | done
    owner_decisions:
    risks:
    week_candidate:
    life_reset_can_import:
    life_reset_must_not_touch:

  solmax:
    current_next:
    status: ready | blocked | active | held | awaiting_owner | done
    owner_decisions:
    risks:
    week_candidate:
    life_reset_can_import:
    life_reset_must_not_touch:

  life_reset:
    current_next:
    status: ready | blocked | active | held | awaiting_owner | done
    owner_decisions:
    risks:
    week_candidate:
    life_reset_can_import:
    life_reset_must_not_touch:
```

Default source boundaries for this week:

- Game direction owns game production, architecture, roadmap, and task state.
- Health direction owns nutrition, training, body data, health protocols, and
  medical questions.
- Solmax/W0 remains cut unless the owner explicitly resumes it in a separate
  valid Solmax session and removes competing volume from the week.
- Life-reset owns the week contract, cuts, capacity, mutation rule, and
  weekly-level evidence only.

### 1.4 Candidate intake

Capture candidate cards before selecting. New ideas are not commands.

```yaml
candidate_intake:
  source_direction_slices:
    - ""
  maintenance_floors_from_sources:
    - ""
  standalone_activities:
    - ""
  owner_ideas_to_capture_not_commit:
    - ""
  decisions_needed:
    - ""
```

## 2. Card fields

Use one compact card per possible weekly item.

```yaml
card:
  id:
  title:
  source:
  kind: direction_slice | floor | activity | idea | decision | blocker | evidence
  status: inbox | candidate | selected | doing | blocked | done | cut | parked
  why_now:
  done_when:
  capacity_cost: deep_work | admin_light | owner_decision | recovery_buffer | family_life
  dependency:
  owner_decision_needed:
  source_of_truth:
  life_reset_role:
  cut_if:
  evidence_to_capture:
```

Selection rule for v0:

- Choose at most one primary direction outcome.
- Choose at most one secondary bounded outcome.
- Treat the first Weekly Contract as the life-reset experiment.
- Add optional activity only if it does not steal capacity from selected work.
- If capacity is low, reduce the week instead of adding discipline theater.

## 3. Contract skeleton

The Sunday session writes the contract in owner-facing language, then stores the
accepted version in `live/life-reset/work/week-2026-06-22-contract-v0.md`.

```yaml
weekly_contract:
  id: lr-week-2026-06-22
  status: draft | accepted
  dates: 2026-06-22..2026-06-28
  basis:
    planning_packet: live/life-reset/work/sunday-planning-packet-v0.md
    dry_run_evidence: live/life-reset/work/weekly-operating-graph-dry-run-v0.md

  source_snapshots:
    - direction:
      status:
      current_next:
      selected_import:
      explicit_non_ownership:

  capacity:
    fixed_commitments:
    deep_work_blocks_available:
    owner_decision_blocks_available:
    low_capacity_windows:
    recovery_buffer:
    assumptions:

  selected:
    primary:
      card_id:
      source:
      outcome:
      done_when:
      success_check:
    secondary:
      card_id:
      source:
      outcome:
      done_when:
      success_check:
    experiment:
      card_id:
      source: life-reset
      outcome: first Weekly Contract v0 is accepted and reviewable
      done_when:
        - contract accepted
        - changes use the change rule
        - weekly review can compare promised vs actual
    optional:
      - card_id:
        rule:

  explicit_cuts:
    - Solmax/W0
    - permanent provider, chat, repo, board, or external-tool architecture
    - daily method selection and full daily runtime protocol
    - process/activity modules
    - full backlog system
    - nutrition, training, medical, or psychiatric prescription
    - game production roadmap or tasks authored by life-reset
    - source-direction raw data ownership
    - automation
    - planning beyond 2026-06-22..2026-06-28

  change_rule:
    required_for_new_current_week_commitment:
      - name the new fact
      - explain why it beats the accepted contract
      - remove or shrink a competing commitment of comparable size
      - record the mutation in the contract evidence
      - get owner acceptance

  backlog_or_idea_handling:
    default: capture, classify, and do not commit
    statuses: inbox | candidate | parked | routed | dropped

  owner_acceptance:
    accepted: yes | no
    owner_words:
    accepted_selected_items:
    accepted_cuts:
    accepted_change_rule:
    accepted_session_writer_rule:
```

## 4. Acceptance checklist

The contract is accepted only when all lines are true.

- The owner gave enough real calendar and capacity information, or accepted a
  deliberately smaller conservative contract.
- Source snapshots are refreshed or explicitly marked as stale/unknown.
- Selected items are fewer than the candidate list.
- Every selected item has `done_when`, success check, source of truth, and
  evidence to capture.
- Solmax/W0 is cut unless resumed in a separate valid Solmax session.
- Life-reset does not prescribe nutrition, training, medical care, psychiatric
  care, game architecture, or game production tasks.
- Permanent tooling, daily method selection, modules, automation, and full
  backlog are cut.
- The change rule is written into the contract.
- The owner explicitly accepts selected items, cuts, change rule, and the
  session/writer rule.
- The session ends in one RESULT with state_changes for the writer.

## 5. Superseded next CALL

The original Sunday-contract CALL was superseded by the 2026-06-20 repair.
Do not copy a CALL from this packet. Use `live/life-reset/NOW.md -> next`.

END_OF_FILE: live/life-reset/work/sunday-planning-packet-v0.md
