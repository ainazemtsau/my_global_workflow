---
id: g-zara-trusted-context-state
_kind: node
_parent: g-zara
status: dropped
label: Доверенный контекст и переносимое состояние
hook: Fresh run получает только разрешённый контекст и продолжает без старого чата.
_pos: 1
---

## goal
A fresh run or different qualified executor receives exactly the permitted,
current and provenance-bearing context it needs and can resume useful work
without the previous transcript or automatic loading of unrelated history.
## done_when
1. Each Area/Capability/Workflow declares required and optional sources,
   freshness, sensitivity, size budget and read/write authority.
2. Context is assembled only from explicit typed references; whole history,
   archives, neighboring Areas and personal data never enter "just in case".
3. Every included datum records source, version/hash, acquisition time,
   privacy class and reason for inclusion; the owner can see why a model saw it.
4. Facts, decisions, statuses, references and transitions are structured;
   notes and model outputs remain opaque artifacts and are never mined by
   Python into facts.
5. One authoritative owner exists for each fact. Other capabilities/Areas use
   typed references or projections rather than divergent copies.
6. A fresh run resumes from a versioned continuation without prior chat and
   does not present stale/incompatible context as current.
7. Tests cover missing required source, stale data, forbidden source, changed
   reference, budget overflow, conflicting versions and read-only boundary.
8. Every source/reference carries an explicit trust/taint classification.
   Instructions are separated from untrusted data, and a run consuming
   untrusted content receives least-privilege tool/effect scopes. Adversarial
   tests cover indirect prompt injection, cross-source instruction conflict
   and attempted privilege escalation.
9. The web UI shows state/provenance/continuation in owner language through
   projections, not direct database or filesystem interpretation.
## why
Trustworthy continuity is what turns isolated model calls into a personalized
exocortex and enables depth across Areas without contaminating contexts.
## edge
The owner already operates several real Git-backed processes and understands
contracts, provenance and audit. Those give unusually strong test material for
selective context and recovery.
## risk
Provenance machinery may add more burden than manual file selection. Revisit
if real runs still require the owner to assemble most context or the projection
is less understandable than a small explicit file set.
## журнал
2026-09-04 · dropped — содержание разошлось по волнам и перестало быть отдельной целью: слои информации, объявленные ссылки, потолок бюджета и только дописываемый журнал стали текстом ядра волны 0, сбор контекста с бюджетом — командой волны 1. Единственное, чего в плане не было — отделение инструкций от недоверенного содержимого и урезанные права у работы, читающей чужой текст, — внесено строкой 4 done_when волны 0. · history/2026-09-04-s-solmax-zaratustra-v2-map-055.md
2026-08-13 · converge Health WHAT signed: thin shared Area-creation/context/web-writer spine exercised by Nutrition+Training Health; 43 answered/5 open/0 deferred, A1-A20 complete; fresh converge-verify opened · history/2026-08-13-s-solmax-zaratustra-health-converge-027.md
2026-08-13 · map Zaratustra finalized: owner-approved six-node 1→6 roadmap recorded with four evidence-backed boundaries, old unfinished operating-manager branch dropped, and Health converge opened as the sole frontier · history/2026-08-13-s-solmax-zaratustra-map-finalize-026.md
END_OF_FILE: live/solmax/cards/closed/g-zara-trusted-context-state.md
