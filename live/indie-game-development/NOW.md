# NOW: indie-game-development
updated: 2026-07-16 by s-shape-near-gas-l1b-001

bet:
  node: g-9c41
  goal: |
    Доставленный NearGas L1a проверяемо наблюдаем через ровно пять internal observation families:
    retry snapshot, fault injection, handler classification, kernel rows и loopback trace; observer не меняет authority, atomicity и deterministic Step.
  appetite: |
    3 focused days; владелец выбрал «а» 2026-07-16. Шесть задач по ≤0.5 focused day; продления нет.
  kill_by: |
    Automatic review 2026-07-24 или при исчерпании 3 focused days, что раньше. Kill без продления, если acceptance <5/5,
    любая family требует cut capability, observer меняет L1a semantics/order/atomicity или fresh G5 опровергает любую family.
  forecast: |
    Ранний сигнал = L1B-Acceptance: 5/5 falsifiable positive/negative oracles на реальном L1a path без excluded dependency.
    Ожидаем внутреннюю instrumentability + binding evidence за 6 half-day tasks, но не Unity/gameplay/M1 delivery.
    Cross-bet 34+ route остаётся ledger, не cap; 24.07 остаётся контрольным review, не stop.
    next_if_true: fresh review закрывает L1B только как internal instrumentability и возвращает владельцу выбор следующей ставки из route; нет automatic L2/C1/Unity launch.
  against: |
    Логи могут наблюдать суррогат, неоднозначно связывать retry/fault/handler или влиять на timing/order. Любой такой сигнал
    переключает ставку в NOT MET/review; fake-harness обход запрещён.
    next_if_false: L1a остаётся DELIVERED, v22 — FORBIDDEN; L1B закрывается NOT MET с названной failed family и возвращается на owner review без surrogate workaround.
  cut_list:
    - Нет L2 resource admission, work/memory bounds и performance ceiling.
    - Нет C1 committed digest или новой checksum authority.
    - Нет Unity cutover, debug UI и gameplay wiring.
    - Нет workers/concurrency.
    - Нет S4, Level/DA/PGG, common scene, real network и two-machine proof.
    - Нет общего telemetry/export/persistence/replay framework.
  lens_verdicts:
    commercial_traction: "not_needed: внешнего сигнала нет; это короткий capped технический мост к M1."
    core_gameplay_depth: "not_needed: механики и player decisions не заявляются."
    coop_first: "not_needed: loopback = internal diagnostic, не co-op evidence."
    technical_feasibility: "L1B-Acceptance→L1B-G5: falsifiability, passive observer, deterministic integrated trace и fresh refutation."
    scope_production: "L1B-Acceptance + L1B-G5: cuts проверяются до PLAN и на close."
    audience_workflow: "not_needed: internal trace не объявляется публичным артефактом."

tasks:
  - id: L1B-Acceptance
    goal: "[session] Frozen owner-approved child acceptance различает real L1a observability и surrogate evidence для 5/5 families."
    done_when: "5/5 families имеют falsifiable positive/negative oracle; adversarial dry-run не требует cut capability; владелец принял artifact."
    status: active
  - id: L1B-PLAN
    goal: "[executor] Owner-approved product PLAN фиксирует evaluator, rollback и disjoint observation ownership без authority/Unity/C1/L2 expansion."
    done_when: "PLAN frozen по current v26 contract; владелец принял; next handoff соблюдает compiled-carrier/RED guards."
    status: open
  - id: L1B-Capture
    goal: "[executor] Retry snapshot и fault injection дают стабильное пассивное наблюдение реального L1a path."
    done_when: "Genuine RED ловит retry/fault planted controls; delivery не меняет L1a result/order/atomicity."
    status: open
  - id: L1B-Classify
    goal: "[executor] Handler classification и kernel rows однозначно связывают attempt/generation/phase."
    done_when: "Planted misclassification ловится; rows коррелируются без C1 digest и authority change."
    status: open
  - id: L1B-Trace
    goal: "[executor] Loopback trace сводит 5/5 families в один детерминированный internal scenario."
    done_when: "Trace различает agree/planted divergence и не заявляет real-network, gameplay или M1 delivery."
    status: open
  - id: L1B-G5
    goal: "[session] Fresh binding refutation даёт честный verdict по 5/5 families, passive-observer invariant и cuts."
    done_when: "Separate fresh review reruns first-hand gates, пытается опровергнуть каждую family и закрывает только по 5/5 + scope GREEN."
    status: open

open_calls:
  - id: c-work-near-gas-l1b-acceptance-001
    to: session
    for: g-9c41 / NearGas L1B task L1B-Acceptance
    issued: 2026-07-16
    note: |
      PRIMARY / ACTIVE BET TASK 1 / OWNER-PRESENT: freeze falsifiable child acceptance for exactly retry snapshot,
      fault injection, handler classification, kernel rows and loopback trace. Direction-only; no product/Unity/
      PLAN/RED/BUILD and no L2/C1/workers/S4. work/c-work-near-gas-l1b-acceptance-001-call.md.
  - id: c-research-level-module-standard-v1-001
    to: research
    for: g-9c41 / Level-DA-PGG project Standard v1 candidate and old-task recovery
    issued: 2026-07-14
    note: |
      READY PARALLEL / DIRECTION-ONLY: reconstruct established seams versus the missing project-owned standard;
      produce the two-contract Standard v1 candidate, validator/fixture matrices and old-task disposition package.
      No product/Unity/PLAN/BUILD, no Phase 0 revival, no owner acceptance implied.
      work/c-research-level-module-standard-v1-001-call.md.
  - id: c-research-q-coop-interdependence-002
    to: session
    for: g-d3a8 / co-op composition question
    issued: 2026-07-14
    note: |
      READY PARALLEL / PAPER-ONLY: g-d3a8 Frame-v2 reconciliation
      closed owner-approved. Resume the exact preserved co-op
      composition question under Frame v2 and the mandatory
      eight-player requirement. It may return an
      OWNER-SELECTED PAPER ANSWER or an honest block; canon admission
      remains a separate owner-present CALL and Sc-damage remains
      HELD. Full CALL:
      history/2026-07-14-s-repair-minimum-game-frame-v2-001.md.
  - id: c-exec-unity65-mac-revision-002-build-001
    to: executor
    for: g-9c41 / local .NET gate runner prerequisite
    issued: 2026-07-12
    note: "HELD / NON-RUNNABLE: pre-v21 CALL and PLAN refs 7a3e747/8a344e9 do not resolve from fetched refs. After repo v21 Re-sync it still needs its own current-v21 full-packet check; CALL content is unchanged. work/c-exec-unity65-mac-revision-002-build-001-call.md."
  - id: c-shape-sc-damage-001
    to: session
    for: Sc-damage
    issued: 2026-07-09
    note: "HELD until ready canon spec; work/c-shape-sc-damage-call.md."
  - id: c-visual-009
    to: executor
    for: g-7e15 / preserved visual motion work
    issued: 2026-07-10
    note: "LOCKED until M0+C1+L3+I1 delivered/reviewed; motion also needs immutable per-Step data, later visuals wait E1/D1/X1."
  - id: c-marketing-wake-001
    to: session
    for: g-2f8c / minimal marketing wake
    issued: 2026-07-11
    note: "READY from the 2026-07-11 wake brief; owner mandate includes INOMAND research/substrate and no public action or spend without a separate owner yes. Route is known stale against the committed INOMAND checkpoint: dr-20260712-001."
  - id: c-exec-char-v2-reaction-core-repair-002
    to: executor
    for: g-6d4e / В2 Leg 1 — close the un-gated-seed CLASS (repair-001 was RED; owner chose option A)
    issued: 2026-07-15
    note: |
      RUNNABLE (character track, parallel). Supersedes c-exec-char-v2-reaction-core-repair-001, which is CONSUMED
      and CLOSED-RED. Chain: binding G5 found R1 → repair-001 (b6c6f2b7) → cross-family G4 (Codex, the FIRST
      independent family on this code) returned RED → the G5 session CONFIRMED Codex with its own differential
      probe → AGENTS.md "same failure class twice = stop" fired → owner decided **option A**.
      ROOT CAUSE IS THE G5's OWN CALL, NOT THE BUILDER: repair-001 done_when #2 named a WEAK invariant
      ("IsReady==true ⟹ Current обtained from inner, not the Origin placeholder"). A pose obtained from the inner
      *while gated* SATISFIES that and is still an F1 leak (spec §6 killing force). The builder closed exactly the
      class named; the independent test-author tested exactly the class named. Both did their jobs.
      FULL invariant (use THIS): the wrapper may vouch for a pose (IsReady==true — the socket's only licence to
      trust Current) ONLY if it LEGITIMATELY ACQUIRED it: inner sampled while State==Normal, or a restPose via
      GetUp. Having acquired none, it MUST report not-ready. Provenance, never value (sniffing Origin is banned —
      a body legitimately at zero stays ready; the frozen suite's discriminator pins this).
      CLASS = ONE line, THREE entries (KnockdownAwareBodyState.cs @ b6c6f2b7): root line 112
      `if (!_held.HasValue && _inner.IsReady) _held = _inner.Current;` — the SAME assignment line 65 gates with
      `_reactions.State == Normal`, minus the state term. Entries: line 82 (IsReady) and line 57 (ctor).
      IsReady was NEVER gated, before or after; the repair changed WHAT the un-gated path writes, not that it is
      un-gated. The CTOR site was missed by G4, by the G5, AND by Codex — present identically at e64f070f and
      b6c6f2b7. Proof it is ONE class: Codex's P1 is R1 with two steps transposed (order A ok / order B violates);
      one condition closes both orders and the ctor at once.
      COVERAGE TRAP: the frozen suite is 106/106 against BOTH the bug and the candidate fix — it cannot tell them
      apart. 106/106 is NOT evidence here; the RED must discriminate.
      ACCEPTED COST of A (recorded, not a defect): in the "inner comes online mid-knockdown" / "never ready"
      regimes the wrapper honestly reports not-ready, so PlayerBodySocket returns its own _lastPose (initialised to
      Origin) → body at world origin for the whole knockdown (~3 s vs ~2 frames). That is DF-13, NOT A's fault —
      verified: a bare never-ready source with NO wrapper at all yields socket.Current == (0,0,0,0). DF-13's site
      is PlayerBodySocket = the FROZEN seam (done_when #5) → do NOT fix it here; it is the owner's call.
      REJECTED (probed): B (ctor demands ready inner) breaks 9/21 independent tests; G (spawn-pose ctor arg) has
      the best behaviour 6/6 but breaks 21 call sites at compile time — the builder may edit neither. G2
      (A + explicit Place(pose)) is 21/21 with no origin but adds a SECOND unbound caller obligation (the C1 class).
      work/c-exec-char-v2-reaction-core-repair-002-call.md; full evidence + the corrected invariant in
      knowledge/g6d4e-char-v2-leg1-reaction-core.md. THIRD pass at one class — if it does not close here, the next
      step is not a fourth patch but re-scoping the leg with the owner.
  - id: c-exec-char-v2-body-rig-ragdoll-build-001
    to: executor
    for: g-6d4e / В2 Leg 2 — rig + procedural locomotion + cosmetic PuppetMaster ragdoll + character material
    issued: 2026-07-14
    note: |
      HELD until c-exec-char-v2-reaction-core-repair-002 closes and Leg 1 is G5-CONFIRMED (binding G5 returned NOT
      CONFIRMED 2026-07-14; repair-001 was itself RED on the SAME class — cross-family Codex G4 caught it — so
      repair-002 is the owner-decided option-A close; the repair's own binding G5 issues the runnable Leg 2 CALL).
      Spec: work/c-plan-characters-002-plan.md §4 Leg 2. PuppetMaster ragdoll = isolated cosmetic layer (base prefab
      works without gitignored RootMotion); magenta fix = own character material only (URP-default guid 31321ba1…
      untouched, F2).
      MANDATORY carry-forwards the Leg 2 CALL must bind (from the G5, knowledge/g6d4e-char-v2-leg1-reaction-core.md):
      C1 — the inner-source RE-SEED on get-up is mechanically UNBOUND (no test, no ledger row, no gate). Omit it and
      the authoritative pose teleports by the full gated-phase drift (probed: 4.5–5.2 m) the instant Normal resumes,
      annihilating the GetUp(rest) reconcile; the ONLY catcher is owner-eye "no jerk". Make it a ledger row / RED test
      at Leg 2 ENTRY. (Disclosed 4× by Leg 1 and spec-routed to Leg 2 — a boundary, not a Leg 1 defect.)
      C2 — TRAP: PlayerBodyView.GetUp() (В1, already wired) forwards to the parameterless IBodyReactions.GetUp() and
      SILENTLY SKIPS the wrapper's reconcile. The obvious-looking call is the wrong one; Leg 2 must call
      wrapper.GetUp(restPose).
      C3 — the driver's TIMED auto-rise never reconciles (no call site; IBodyReactions gives the wrapper no way to
      learn a get-up began). Documented as S2; Leg 2 must handle it.
      C4 — F2/F3 P3s, with their rationales CORRECTED by the repair (the old "self-healing" wording was false).
      Engine existence proof + owner-eye LOOK + cross-family G4 + binding fresh G5.
recurring: []

decisions:
  - q: "d-m1-min-spec-hardware-001 — какое конкретное слабое железо становится binding min-spec финального прогона М1?"
    options: ["Доступная физическая машина", "Точный CPU/GPU/RAM-класс с арендой/покупкой к финалу", "Только throttled-прокси — финал не закрывает"]
    recommendation: "Доступная физическая машина; газ CPU-bound, поэтому CPU должен быть назван явно."

next:
  CALL: work/c-work-near-gas-l1b-acceptance-001-call.md

END_OF_FILE: live/indie-game-development/NOW.md
