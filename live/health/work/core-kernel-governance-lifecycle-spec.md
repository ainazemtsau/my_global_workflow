# Core-Kernel Governance / Lifecycle Spec (import baseline)

> Produced by the read-only governance workflow wf_0dfa63fb-a34 during the nutrition converge
> (session s-health-core-kernel-reframe-001, 2026-06-20), then RE-HOMED to g-health-core by the
> owner's Variant-1 decision. Assembly surface / work product, NOT a state file and NOT authority.
> The kernel converge (c-health-core-kernel-converge-001) imports this: rows tagged born-closed are
> settled; the 16 forks below are OPEN owner decisions; the G7-2 reconciliation MODIFIES a signed gate.
> Originally scoped to nutrition; the design is domain-agnostic governance and now belongs to the
> kernel so every domain (nutrition, training, future) inherits it instead of reinventing the engine.

## Why this exists
g-health-core delivered a data/contract layer but no runtime. With no kernel-provided state-machine /
procedure-interpreter / governance lifecycle, the nutrition module hand-rolled its own workflow engine
(x_nutrition/workflow/graph.md + current-workflow cursor + workflow-router) WITHOUT a governance gate —
so AI authored owner-facing content AND activated it as accepted authority. The owner rejected the slice
2026-06-20. This spec is the lifecycle/governance the kernel must provide so that defect is structurally
impossible for ALL domains.

## §FAILURE MODES (must-prevent; mined from the 2026-06-13 … 2026-06-20 saga)
- FM1 — system asked the owner an expert variable (meals/day) as a preference. Must-prevent: expert vars
  are SYSTEM-DECIDED from evidence; only irreducible owner facts are askable; asking an expert var is gate-rejected.
- FM2 — startup dumped a wall of menu/recipe/grocery/log content ("AI как-то порешает"). Must-prevent:
  no AI-produced owner-facing content is authority in ANY state until owner-approved; one bounded job per chat.
- FM3 — bootstrap/carrier invented ad-hoc in chat; trust collapsed. Must-prevent: carrier is a durable repo
  artifact (never per-chat) and a repo-owned end-to-end journey proof is an approval precondition.
- FM4 — a durable state transition was CLAIMED ("пакет применен") without proof. Must-prevent: no transition
  trusted without commit/diff/re-read evidence, refuted outside the producing chat.
- FM5 — seed/placeholder content treated as active authority. Must-prevent: explicit lifecycle; existence/
  location never equals activation; PROPOSED is a first-class non-authoritative status.
- FM6 — a render (menu) produced before/without its upstream decision (program/cycle) and justification.
  Must-prevent: renders may only become PROPOSED/ACTIVE after upstream is ACTIVE, carrying a justification chain.
- FM7 — pending medical/allergy (safety) facts were deleted. Must-prevent: owner safety facts are owner-authored,
  AI-non-deletable; a preservation check FAILS if any disappears without an owner-resolution record.
- FM8 — best-practice/nutrition claims asserted without sources / with stale sources. Must-prevent: every ACTIVE
  material claim cites a repo-backed, current-evidence source with a freshness marker; stale fails closed.
- FM9 — one chat bundled program+cycle+menu+recipes+grocery+log+review. Must-prevent: one-chat-one-job enforced
  by a writer/applier check (reject >1 content family per non-logging job), DAY_LOOP the one same-state exception.
- FM10 (ROOT) — AI authored owner-facing content AND self-activated it with no co-creation/approval gate.
  Must-prevent: PROPOSED→ACTIVE requires explicit owner approval (words+date+scope); writer reject-barrier
  refuses any ACTIVE-targeted write lacking that marker; no role both authors and activates.
- FM11 — self-cert: green automated checks masked unapproved content as "done". Must-prevent: closure is
  content-approval-gated and FAILS if any ACTIVE family lacks an owner-approval marker, regardless of green
  checks; refutation runs in a separate session.
- FM12 — dirty prototype/evidence reused as authority by location. Must-prevent: namespace-distinct provenance
  space; authority is a per-artifact property; reuse only via re-import through the gate, never inherited by folder.

## §GLOSSARY (new governance terms the kernel introduces)
- Content authority lifecycle — mandatory status on every owner-facing artifact: SEED → PROPOSED → ACTIVE →
  SUPERSEDED/ARCHIVED. Only ACTIVE is authority; existence/location never confers it.
- PROPOSED — first-class third status between SEED and ACTIVE. AI-authored content always lands here; never
  authority; never consumed by a downstream render.
- Content co-creation / owner-approval gate — kernel-local instance of KERNEL G9: PROPOSED→ACTIVE presents one
  artifact at a time and requires the owner's explicit echoed words scoped to a named artifact+version, dated.
  Distinct from the settled input-fact boundary — it gates OUTPUTS.
- Content-authority writer gate — the applier reject barrier (a G9 analog): rejects any ACTIVE-targeted write
  lacking an owner_approved marker AND evidence-of-transition, on top of retained graph/shape checks.
- Evidence-of-transition — commit/diff/re-read proof that repo state actually changed, refuted outside the
  producing chat (G5 discipline). A transition merely claimed in chat is invalid.
- Provenance space — namespace-distinct, clearly non-authoritative store for SEED/evidence/prototype; authority
  is a tracked property of each artifact, never inherited by folder.
- Render-before-decision block — menu/grocery/fallback/log are projections; may become PROPOSED/ACTIVE only
  after their upstream program+cycle are ACTIVE, each carrying its justification chain.
- Nutrition/domain handoff packet — a RESULT-equivalent closing every job (outcome, evidence-of-transition,
  owner-approval status, what became ACTIVE) handing the single next card; the next chat opens from it.

## §WHAT FAMILIES (governance rows by dimension — cited; firewall G7 unless noted PLAN)
Roles & authority — four roles, no role both authors and activates: PROPOSER (chat-AI, writes only PROPOSED),
  OWNER (only approver), WRITER-APPLIER (persists ACTIVE with reject-barrier + evidence), SEED/EVIDENCE
  (never authority). Authority order: owner-approved-ACTIVE > PROPOSED > SEED; live owner instruction above all.
  Mirrors the Direction-OS session/writer split. [FM10, FM1, FM4]
Artifact lifecycle & status — mandatory status field; SEED→PROPOSED→ACTIVE→SUPERSEDED; only ACTIVE is authority;
  single-hop SEED→ACTIVE and PROPOSED→ACTIVE-without-approval forbidden; one ACTIVE per family; authority is a
  per-artifact property, not a folder. [FM5, FM12, GAP: no PROPOSED middle, seed=active collapse]
Owner-approval gate — PROPOSED→ACTIVE only on explicit owner words + echo/R-number + named artifact+version,
  recorded with date; one artifact at a time; silence/non-answer never promotes (no timeout-to-active); batched
  per movement. [FM10, FM11]
Recipe/menu/grocery/program lifecycle — families = program, cycle, week-plan, menu, recipe, grocery, fallback,
  log-template, review/mutation; program & cycle exist+approved before any menu/recipe/grocery; a born PROPOSED
  artifact carries rationale + current-evidence sources; render-before-decision blocked; menu cites only ACTIVE
  recipes; grocery derives from ACTIVE menu+base-prep and must not lie (base-prep counted once). Base-prep reuse
  ALGORITHM → PLAN; the no-lie property is the binding acceptance. [FM6, FM8, FM5]
One-chat-one-job & handoff — a job = one bounded deliverable (one artifact in one state, OR one owner question,
  OR one DAY_LOOP block); closed job-type enum; mandatory 4-field handoff (outcome+status, evidence-of-transition,
  owner-approval, single next card); next chat opens from the prior handoff; DAY_LOOP is the one same-state
  logging exception (≤1 clarifier, no content artifact); enforced by a writer/applier reject at apply time.
  Handoff/next-card schema → PLAN. [FM9, FM2]
Writer behavior / evidence — reject set: unverified transition; content reaching ACTIVE without owner_approved
  marker; skip-hop; render-before-decision; safety-fact deletion; sourceless OR stale-sourced material claim
  (freshness fails closed independent of citation presence); multi-job bundle outside DAY_LOOP; write outside the
  job's authorized target + domain namespace + cursor records. Freshness threshold VALUE → PLAN; the presence-and-
  non-stale CHECK is G7. [FM4, FM7, FM8, FM10, FM9]
Safety facts — irreducible owner safety facts (medical/allergy) are owner-authored, AI-non-deletable, carried
  forward; a before/after preservation check FAILS if any disappears without an owner-resolution record. [FM7]
Cleanup/rebuild boundaries — this work produces only structure (no execution content, no product-repo edits);
  cleanup of dirty families is a later bounded executor CALL after owner approves structure; fixed governance-
  first rebuild order: (1) governance/runtime spine → (2) program/principles → (3) recipes → (4) menu →
  (5) grocery → (6) LOG → (7) review; each stage one job, none starts before the prior is owner-approved;
  prior control-plane + the two nutrition G5 reviews are tainted-drop (evidence only). Exact paths/schema → PLAN.
  [FM2, FM6, FM9, FM10, FM12]

## §COVERAGE (failure → prevented)
FM1✔ FM2✔ FM3✔ FM4✔ FM5✔ FM6✔ FM7✔ FM8✔(after the added freshness row) FM9✔ FM10✔(root, mechanically closed by
the approval gate + writer barrier) FM11✔(closure content-approval-gated; refute in a separate session)
FM12✔. Firewall clean after two re-tags (provenance-space-exists guarantee and evidence-before-authoring
ordering are owner-design → G7, only path/schema/threshold values stay PLAN).

## §RESIDUALS to carry to the kernel converge / PLAN
- FM8 freshness: added rule — an ACTIVE material claim with no freshness marker, or one older than the source-
  currency boundary, is writer-rejected; staleness fails closed independent of citation presence. Threshold VALUE → PLAN.
- FM11 bite depends on PLAN making the approved_words field MANDATORY + materiality-checked; flag for PLAN.

## §OPEN OWNER FORKS (16 — surfaced, NOT auto-decided; recommendation in parentheses)
F1 governance model — full mini-OS (roles+RESULT/CALL+PROPOSED→ACTIVE+gate+barrier) vs lighter. (mini-OS)
F2 writer locus — same chat after RESULT / separate writer-phase with git / owner commits. (separate writer-phase)
F3 lifecycle states — four (SEED→PROPOSED→ACTIVE→SUPERSEDED) vs five+ vs three. (four)
F4 authority by property vs by folder vs delete-old. (property, not location)
F5 which families gate vs derive — approve program+cycle+menu+recipes+fallback+base-prep, grocery DERIVED;
   resolves an internal seam (one row treats grocery as derived, another as approved). (grocery derived)
F6 approval granularity — per-artifact vs two-tier (program/cycle individually; renders one derived stage-packet
   shown one-at-a-time) vs one blanket gate. (two-tier)
F7 what counts as "yes" — explicit words+echo+artifact+version in RESULT vs short "да" vs timeout. (explicit+echo+version)
F8 journey as acceptance precondition — durable repo journey artifact vs prose vs retro-doc. (durable journey artifact)
F9 evidence-of-transition strictness — commit+diff vs commit+diff+re-read vs +owner-confirm-each. (commit+diff+re-read)
F10 authority vs durability split — owner "да"=AUTHORITY, writer step=DURABILITY vs hard vs soft. (two-tier)
F11 pre-approval content visibility — full PROPOSED draft in provenance space vs skeleton vs none. (full draft, provenance-separated)
F12 refute-session for heavy decisions — program/cycle only vs none vs every artifact. (program/cycle only)
F13 one-chat-one-job strictness — hard stop+card always (DAY_LOOP excepted) vs soft "продолжаем" vs hybrid. (hard at start)
F14 supersede retention — keep SUPERSEDED in non-authoritative provenance space vs archive vs delete. (keep in provenance space)
F15 cleanup of dirty files (later) — hybrid (safety+research→archive, owner-facing content→delete) vs archive-all vs delete-all. (hybrid)
F16 rebuild from zero vs re-import — re-import only via gate, default rebuild-fresh vs clean-slate. (re-import via gate)

## §G7-2 RECONCILIATION (MODIFIES a previously owner-signed gate — needs an explicit re-sign)
Signed core G7-2 = decide-and-inform (system parses-and-commits when confident, asks only on brakes). Owner's
new "только после моего подтверждения, вначале" tightens this by LAYER, not a blanket override:
  - durable content + status flips (program, cycle, menu, recipe, ACTIVE transitions) → confirm-before-save +
    readable-for-owner presentation;
  - daily logging / low-stakes parsing → stays decide-and-inform ("может что-то не записал … голову не дурить").
The kernel converge must present this split and get the owner's explicit re-sign.

## §OWNER FORMAT PREFERENCE (durable)
Never present writer/YAML-format files to the owner. Present a readable "result + what will be saved", and save
only after his confirmation. Applies to every kernel surface that proposes a durable write.

END_OF_FILE: live/health/work/core-kernel-governance-lifecycle-spec.md
