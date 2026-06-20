RESULT s-health-core-kernel-reframe-001 (call: c-health-nutrition-system-rebuild-converge-001 → owner reframe "Вариант 1" 2026-06-20)
direction: health   play: repair (pivoted from converge)   node/task: g-health-core (re-opened) + g-health-nutrition-system (re-scoped)

outcome: |
  The nutrition converge frame was superseded by an owner architecture decision.
  Mid-converge the owner identified that the rejected nutrition slice is a symptom
  of a MISSING CORE LAYER, not a nutrition-only gap: g-health-core delivered the
  data/contract layer but never provided a runtime — per-domain memory/working-state,
  state machines, a single procedure-interpreter/router, and a governance lifecycle
  (artifact SEED→PROPOSED→ACTIVE→SUPERSEDED + owner-approval gate + confirm-before-save +
  readable-for-owner presentation + writer/evidence barrier + one-chat-one-job handoff).
  Because the core shipped no runtime, the nutrition module reinvented its own workflow
  engine (x_nutrition/workflow/graph.md + current-workflow cursor + workflow-router) and
  did so WITHOUT a governance gate — the root of the 2026-06-20 rejection. Training would
  reinvent it again.

  Owner chose Variant 1: EXTEND g-health-core into a provider-independent kernel
  (do not rebuild the working data/contract layer); nutrition and training become thin,
  one-responsibility-per-procedure layers; the governance/lifecycle design produced in
  this converge moves INTO the kernel rather than bolting onto nutrition.

  Direction OS state now reflects this: g-health-core re-opened (done→parked) for the
  kernel-runtime extension; g-health-nutrition-system re-scoped as a thin layer blocked
  on the kernel; the nutrition converge call superseded by a core-kernel converge call;
  the governance design preserved as a work/ import baseline.

evidence: |
  Owner words this session:
  - decision: "Вариант 1".
  - architecture: "у нас должен быть core, который позволяет построить вот это … у него
    должна быть память, какие-то state-машины, как запускаться, какие-то процедуры";
    "каждый термин … своя функция … единственное, что её запускает и эту функцию … интерпретирует";
    "разбить на слои и на процедуры"; "структура должна быть антихрупкой, чтобы я мог легко
    что-то починить, расширить, добавить, удалить, и чтобы это всё заработало";
    "тренировки … тоже что-нибудь похожее"; "вдохновляться нашим workflow";
    "Я не читаю файлы, которые предназначены для Врайтера … он должен написать в формате для
    меня … только после моего подтверждения в любом случае. Можно вначале так сделать";
    "возможно, ещё быть проблема в коре".

  Grounded core finding (read live/health/work/converge-g-health-core.md +
  knowledge/health-ai-core-guidance-governance.md):
  - core PROVIDES: data model (W1–W31, WA1–WA4), shared concepts (W29–W42),
    parse pipeline (W43–W52), module attach contract (W57–W61, CA1–CA7),
    an extension SEAM (procedure-definition contract W53–W55).
  - core LACKS: a first-class state-machine object, a single procedure interpreter/router,
    and a governance lifecycle/approval gate. Proof of the gap: the nutrition module had to
    build its own x_nutrition/workflow/{graph.md,current-workflow.md,workflow-router.md}.

  Governance design (this session's read-only 13-agent workflow, wf_0dfa63fb-a34):
  12 failure modes mined across all five prior nutrition failures, each shown mechanically
  prevented by the proposed lifecycle; preserved in
  work/core-kernel-governance-lifecycle-spec.md (8 governance glossary terms, WHAT-row
  families by dimension, failure→prevented coverage, 16 batched owner forks + recommendations,
  2 firewall fixes + 1 added freshness row + 1 flagged PLAN dependency).

state_changes: |
  1) live/health/TREE.md
  - g-health-core: status done → parked; goal prefixed with a RE-OPENED 2026-06-20 note
    (Variant 1: data/contract layer kept, runtime/state-machine/interpreter/governance layer
    missing and to be added as a kernel; nutrition/training become thin layers; governance
    design at work/core-kernel-governance-lifecycle-spec.md). Removed the prior appetite/kill_by
    from the re-opened node (re-set when it is re-shaped into a bet).
  - g-health-nutrition-system: appended a RE-SCOPED 2026-06-20 note to its existing RESET note
    (rebuilds as a THIN LAYER on the re-opened kernel; governance/lifecycle now kernel-owned;
    blocked until the kernel WHAT is owner-approved). Status stays parked.

  2) live/health/NOW.md
  - active_bet.note replaced to record the kernel reframe (status stays none).
  - open_calls: replaced c-health-nutrition-system-rebuild-converge-001 (superseded) with
    ready c-health-core-kernel-converge-001.
  - next: replaced with CALL c-health-core-kernel-converge-001 (converge the re-opened core
    at kernel scope; import the governance spec + R1–R8 + existing core data layer; resolve the
    16 governance forks + the G7-2 confirm-before-save reconciliation; route to converge-arch).
  - tasks/recurring/decisions kept [].

  3) live/health/LOG.md
  - Appended the 2026-06-20 reframe line pointing to this history file.

  4) live/health/work/core-kernel-governance-lifecycle-spec.md (NEW)
  - The preserved governance/lifecycle design (import baseline for the kernel converge):
    12 failure modes, 8 governance glossary terms, governance WHAT families by dimension with
    citations, failure→prevented coverage, 16 batched owner forks + recommendations, residuals.

  5) live/health/history/2026-06-20-s-health-core-kernel-reframe-001.md (NEW)
  - This full RESULT.

captures:
  - The kernel converge must surface (not auto-decide) the 16 governance forks F1–F16 and the
    G7-2 reconciliation (confirm-before-save for durable content vs decide-and-inform for daily
    logging) — the latter MODIFIES a previously owner-signed gate and needs an explicit re-sign.
  - FM11 closure (no self-cert) depends on the kernel PLAN making the approved_words field
    mandatory/materiality-checked; carry to PLAN so the bite is real.
  - Friction candidate (watch, not yet a maintenance edit): a converge marked a node `done`
    while it shipped data+contracts but no runtime, so each domain reinvented the engine —
    if the "layer reviewed done but missing a runtime capability" pattern recurs, open maintenance.
  - Later, still pending and unchanged: a bounded executor CALL to quarantine/archive/delete the
    nine dirty health-ai x_nutrition families — only after the kernel + thin-layer structure is
    owner-approved (Variant 1 leaves this downstream).
  - Owner format preference (durable): never present writer/YAML-format files to the owner;
    present a readable "result + what will be saved" and save only after his confirmation.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — the CALL framed a nutrition-only converge; the owner
    identified the defect as a missing CORE runtime/governance layer, contradicting the frame.
  - 2 Reconstruct: done — read the core converge (data/contract layer real; runtime/state-machine/
    interpreter/governance lifecycle absent) and nutrition history (module reinvented its own
    engine); verified the gap from committed artifacts.
  - 3 Propose corrected state: done — re-open g-health-core (done→parked) for a kernel-runtime
    extension; nutrition/training as thin layers; preserve the governance design as the kernel
    lifecycle spec; route to a kernel converge.
  - 4 Confirm (owner): done — owner chose "Вариант 1" and gave the architecture requirements
    R1–R8 ("должен быть core, который позволяет построить вот это … память, state-машины …
    каждый термин своя функция … антихрупкой … тренировки тоже похоже … вдохновляться нашим workflow").
  - 5 Friction: recorded as a capture (watch); not an os/ edit this session.

log: >
  2026-06-20 — health reframe to core-kernel: owner chose Variant 1; nutrition converge paused;
  g-health-core re-opened (done→parked) to add the missing runtime layer (memory/state-machine +
  single procedure-interpreter + governance lifecycle), nutrition/training become thin layers,
  governance design moved into the kernel (work/core-kernel-governance-lifecycle-spec.md);
  next = converge g-health-core at kernel scope.

next: |
  CALL c-health-core-kernel-converge-001
  to: session
  direction: health
  play: converge
  node: g-health-core
  goal: |
    g-health-core is extended into a provider-independent KERNEL that supplies reusable runtime
    primitives — per-domain memory/working-state, state machines, a single procedure-interpreter/
    router (each "term" = one bounded procedure the kernel runs), and a governance lifecycle
    (artifact SEED→PROPOSED→ACTIVE→SUPERSEDED + owner-approval gate + confirm-before-save +
    readable-for-owner presentation + writer/evidence-of-transition barrier + one-chat-one-job
    handoff) — so nutrition and training attach as thin one-responsibility-per-procedure layers
    and no domain reinvents the engine. An owner-approved kernel WHAT exists before any kernel
    build or domain rebuild.
  context: |
    Owner chose Variant 1 on 2026-06-20 (history/2026-06-20-s-health-core-kernel-reframe-001.md).
    RETROFIT converge: g-health-core already has a signed data/contract layer — IMPORT it, do not
    re-litigate it. Baselines to import / frame the open runtime layer against:
    - Existing core data/contract WHAT: live/health/work/converge-g-health-core.md (W1–W64,
      WA1–WA12, CA1–CA7) — born-closed where signed; the gap is the missing runtime layer.
    - Governance/lifecycle design to fold into the kernel:
      live/health/work/core-kernel-governance-lifecycle-spec.md (12 failure modes prevented,
      8 glossary terms, WHAT families, 16 owner forks F1–F16 + recommendations, residuals).
    - Owner architecture requirements R1–R8 (one procedure per term; single interpreter/router;
      kernel primitives memory/state-machine/launch/procedure-registry; layered dietitian-targets
      → menu → recipes → grocery; readable-for-owner + confirm-before-save; anti-fragile add/remove/
      fix a part independently; reuse for training; inspired by Direction OS).
    - Failure evidence: the nutrition saga (history 2026-06-13 … 2026-06-20) and the proof that
      nutrition reinvented its own engine (x_nutrition/workflow/*).
  boundaries: |
    Extend the core; do NOT rebuild or discard the working data/contract layer.
    No execution content (no real menu/recipe/grocery/program); no health-ai product-repo edits.
    Nutrition/training rebuild only AFTER the kernel WHAT is owner-approved.
    Do not silently override the signed G7-2 (decide-and-inform): surface the confirm-before-save
    change as an explicit owner decision (durable content gated; daily logging stays decide-and-inform).
    Surface, never auto-decide, the 16 governance forks F1–F16.
    Do not store raw daily data in Direction OS.
  done_when: |
    Owner has approved a kernel WHAT/structure defining: the runtime primitives (memory/working-state,
    state-machine object, single procedure-interpreter/router, procedure registry), the one-procedure-
    per-term decomposition + layering contract for thin domains, the governance lifecycle
    (SEED→PROPOSED→ACTIVE→SUPERSEDED + approval gate + confirm-before-save + readable-for-owner +
    writer/evidence barrier + one-chat-one-job handoff), and the anti-fragility/extension contract;
    the 16 governance forks and the G7-2 confirm-before-save reconciliation are resolved or routed to
    explicit owner decisions; no execution content produced; route to converge-arch.
  return: |
    RESULT with the owner-approved kernel WHAT, owner decisions, state_changes, and next CALL
    (converge-arch). No kernel build and no domain rebuild before the WHAT is signed.
  budget: one focused converge session

END_OF_FILE: live/health/history/2026-06-20-s-health-core-kernel-reframe-001.md
