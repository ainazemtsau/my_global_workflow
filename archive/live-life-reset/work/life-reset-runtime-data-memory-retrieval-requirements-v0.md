# Life-reset Runtime Data / Memory / Retrieval Requirements v0

Date: 2026-06-20
Status: required repair input for the runtime architecture skeleton

## 1. Why this exists

The active runtime route already required a separate Life-reset Runtime v0
repository/workspace and a full architecture skeleton before any concrete
Weekly Contract. The missing piece was explicit: durable Data / Memory /
Retrieval must be a first-class runtime layer, not an optional later feature.

Owner-approved correction from the repair CALL:

- The runtime must work across future chats/providers without relying on hidden
  chat memory.
- The assistant should be able to retrieve past weeks, decisions, process
  results, topic history and relevant details without loading the whole
  repository into context.
- Life-reset must not store raw health/game/Solmax data.

## 2. Source of truth

The source of truth for runtime operation is the separate runtime
repository/workspace.

Provider chat memory, including ChatGPT or Claude memory, is interface context
only. It may help a surface feel continuous, but it is not authority and must
not be required to continue work in a future chat/provider.

Direction OS remains the control plane. It records runtime pointers,
architecture summaries, governance RESULTs and accepted review decisions; it
does not become the daily runtime database.

## 3. Required architecture files

The runtime architecture skeleton must include these first-class files before
the skeleton can be accepted as ready for pilot:

- `DATA_MODEL.md` — durable entities and relationships for weeks, contracts,
  days, checkpoints, source summaries, decisions, ideas, topics, process
  trials, technique trials, reviews, mutations and retrieval references.
- `MEMORY_POLICY.md` — what is stored, summarized, linked, redacted, expired or
  excluded; the boundary against raw health/game/Solmax data; and the rule that
  provider memory is not source of truth.
- `INDEX_SCHEMA.md` — indexes, tags, IDs, backlinks and summary fields that
  let a future assistant retrieve bounded context by date, week, decision,
  topic, process, technique, source direction and review period.
- `RETRIEVAL.md` — query flows for loading only relevant bounded context and
  answering with evidence pointers instead of relying on chat recollection.

## 4. Retrieval acceptance cases

The architecture skeleton is incomplete unless retrieval design can answer
these cases from durable runtime files/indexes:

- "what happened two weeks ago?"
- "what did we decide about X?"
- "how did technique Y perform?"
- "what ideas were captured about Z?"
- "show process P progress over a month"

The answer path should identify which index or file is consulted, what bounded
documents are loaded, and what evidence pointer is returned.

## 5. Boundaries

This repair does not create a concrete Weekly Contract, run daily operation or
create the runtime repository/workspace.

The runtime may import summaries and pointers from health, game and Solmax when
those source directions provide them. It must not copy their raw data, detailed
tasks, medical/training/nutrition records, game production state or Solmax work
state.

END_OF_FILE: live/life-reset/work/life-reset-runtime-data-memory-retrieval-requirements-v0.md
