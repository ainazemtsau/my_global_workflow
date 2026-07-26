# Markdown-first Visual Portal Contract v1

status: OWNER-APPROVED PROCESS COMPONENT
selected_on: 2026-07-22
authority: |
  Binding input to the replacement demo-driven design workflow.
  Not game canon, not a complete workflow, not a renderer implementation
  specification and not production-asset authority.
owner_verdict: |
  «ПРИНИМАЮ MARKDOWN-FIRST VISUAL PORTAL: источник истины —
  Demo Experience Tree, Canon Ledger и media-файлы; многостраничный
  сайт является только автоматически генерируемым read-only
  представлением; первым renderer-кандидатом проверяем Zensical;
  custom web app, Trilium и AI asset pipelines сейчас не строим.»

## 1. Source of truth

Authoritative content exists only in:

1. Demo Experience Tree;
2. Canon Decision Ledger;
3. media files and their minimal node-linked metadata;
4. NOW/CALL execution state for current work.

Generated HTML, navigation, search indexes, cards, galleries and dashboards
are views. They never hold unique design decisions, canon rules, priorities,
statuses, owner verdicts or replacement history.

Deleting the generated site must lose no authoritative information.

## 2. Portal role

The portal is an automatically generated multi-page read-only surface for:

- understanding the Demo Contract;
- navigating the Demo Experience Tree from whole demo to detail;
- reading beat pages;
- reading accepted Canon Decision Ledger entries;
- comparing linked visual references and candidates;
- viewing evidence and unresolved gaps without internal CALL ids as the
  primary language.

It may be opened locally, served from a home lab or published as static
files. Hosting does not alter authority.

## 3. First renderer candidate

Zensical is the first renderer candidate.

It is not a selected permanent dependency.

A renderer pilot passes only if it can:

- build from portable Markdown and ordinary media files;
- generate working multi-page navigation and cross-links;
- render images and comparison pages without manual HTML duplication;
- work locally or from a simple static host;
- be removed or replaced without rewriting authoritative content.

The pilot fails if it requires:

- authoritative data inside renderer-specific storage;
- extensive custom components;
- duplicate manual status maintenance;
- a custom backend;
- content structure distorted primarily to satisfy the renderer.

## 4. Minimum page families

The generated surface may contain:

1. Demo overview;
2. Demo Experience Tree;
3. beat or situation pages;
4. Canon Decision Ledger pages;
5. media gallery and comparison pages;
6. generated management views where Launch Control separately defines them.

Exact templates, theme, CSS, page count and visual polish remain OPEN.

## 5. Visual work placement

Visual work is attached to a concrete Demo Experience Tree node or one of
its explicit decision gaps.

A visual artifact must say what player-visible distinction, relationship,
situation or decision it helps resolve.

Visual work does not maintain an independent scheduling roadmap and cannot
become active merely because a visual prerequisite was completed.

Applicable c-003 rules remain in force:

- only explicitly enumerated visual rules and named relations may bind;
- placeholders gain no silent authority;
- unlisted generated details remain accidental;
- selected references are not automatically final production assets;
- empirical runtime claims require later evidence.

## 6. Minimal media metadata

Initial media metadata is limited to:

- linked_node;
- purpose;
- status:
  scratch | candidate | selected | superseded | evidence;
- source;
- accepted_rules;
- non_binding.

More provenance fields are added only when a real production pipeline
demonstrates a need.

## 7. Future pipelines

Image-generation, image-assembly, manual-retouch, sound-generation and other
AI asset pipelines are possible future production capabilities.

They are not part of this contract's current implementation.

A future pipeline may consume:

- a Demo Experience Tree node;
- applicable Canon Decision Ledger rules;
- selected references;
- placeholders;
- production envelope.

It may return candidates, provenance and production assets.

Canon stores accepted design rules and references, not pipeline internals.

## 8. Explicit current exclusions

This contract does not authorize:

- building the portal;
- installing or configuring Zensical;
- creating a custom web application;
- adopting Trilium or Notion as authority;
- building an image AI pipeline;
- building a sound AI pipeline;
- choosing final site styling;
- choosing hosting or CI;
- generating new visual candidates;
- altering game canon;
- importing unresolved historical questions into the Demo Experience Tree.

END_OF_FILE: live/indie-game-development/work/demo-workflow/markdown-first-visual-portal-contract-v1.md
