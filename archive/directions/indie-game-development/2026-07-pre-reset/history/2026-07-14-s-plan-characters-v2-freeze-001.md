RESULT s-plan-characters-v2-freeze-001 (input: plain owner message — plan В2 for character track g-6d4e)
direction: indie-game-development   play: shape/plan (local character-track planning, как c-plan-characters-001)   node/task: g-6d4e / В2 (тело)

outcome: |
  Co-created В2 (body) spec FROZEN with owner approval and the first BUILD leg opened. В2 adds, through the
  BYTE-IDENTICAL В1 seam (IAuthoritativeBodyState/PlayerBodySocket/BodyPose): a headless reaction state machine +
  a knockdown-aware source wrapper (Leg 1), then rig + procedural locomotion + an isolated cosmetic PuppetMaster
  ragdoll + the character's own material (Leg 2). Two first-hand code findings reshaped the naive plan and are baked
  into the spec: (F1) a "cosmetic ragdoll never touches authoritative position" guarantee does NOT hold on the В1
  input placeholder — the reaction must GATE the source while State≠Normal and reconcile authoritative←rest on GetUp,
  done via a new source behind the unchanged seam (this is the riskiest assumption, proven HEADLESS in Leg 1);
  (F2) the magenta guid 31321ba1… is the URP package default Lit.mat referenced project-wide (URP GlobalSettings +
  two gas scenes, not only the 4 character assets), so guid-pinning is forbidden — the fix is the character's own
  material. v20→v21 gating decided in PLAN: a one-time idempotent contract-text re-sync at Leg-1 entry, В2 not blocked
  behind the NearGas critical path. Owner decision d-char-v1-post-g5-001 resolved (Вариант 1). No build started; nothing merged.

evidence: |
  Owner approval words (this session): «1 да» (spec к заморозке) · «2 да» (PuppetMaster изолированным косметическим
  слоем — рекомендация) · «3 как ты рекомендуешь» (две BUILD-ноги: headless-реакция + engine-тело раздельно).
  Prior owner verdict carried in from the opening message: «Вариант 1» on d-char-v1-post-g5-001 (product merge В1
  launched separately, no Codex pass).

  First-hand code (product worktree C:\projects\Unity\GasCoopGame_p2a0_002 @db69aba6, branch
  c-exec-char-v1-socket-dropin-build-001):
  - Seam surface read in full: Assets/GasCoopGame/Characters/{IAuthoritativeBodyState,BodyPose,BodyReactions,
    PlayerBodySocket}.cs + Adapters/Characters/{PlayerBodyView,InputBodyStateSource}.cs. PlayerBodyView already
    exposes SetReactions(IBodyReactions) and forwards Knockdown/GetUp; NullBodyReactions is the no-op default В2 fills.
  - F1 proof: InputBodyStateSource.Update() integrates WASD unconditionally; PlayerBodyView.Update() writes
    _socket.Current to transform unconditionally — neither is reaction-aware, so knockdown-while-holding-input slides
    the authoritative root. Refuted the naive "cosmetic ragdoll never affects authoritative" claim (adversarial verify).
  - F2 proof: git grep — guid 31321ba15b8f8eb4c954353edc038b1d owned by
    Library/PackageCache/com.unity.render-pipelines.universal@…/Runtime/Materials/Lit.mat.meta (fileID 2100000,
    type 2 = material); no tracked Assets/**/*.mat.meta owns it; referenced by UniversalRenderPipelineGlobalSettings +
    GasSourcePhase0Demo.unity + GasRoomScene.unity + the 4 character assets. Guid-pinning would collide with the URP package.
  - PuppetMaster feasibility: Assets/Plugins/RootMotion/ present ON DISK but .gitignored (lines 132-135: "paid Asset
    Store vendor asset, local-only, re-imported per machine, NEVER committed") → usable but a committed prefab carries a
    local-only dependency; hence the isolated-cosmetic-layer discipline.

  v20→v21 gate (OS repo): os/engineering/CONTRACT_VERSION current=21; the sole v21 delta is Plan-to-RED readiness
  (VALIDATION.md §Plan-to-RED, CONTOUR.md); v21 is "no parser/regex/schema/conformance", the product §Re-sync is
  contract-text only (mirror clause + bump synced_contract_version 20→21, no product code). Product repo AGENTS.md +
  validation.config stamped v20. GasCoopGame_core/p2a0_002 are worktrees of one repo (re-sync is repo-global). The
  v21-routing repair (history/2026-07-14-s-repair-daily-engineering-v21-routing-20260714-001.md) holds character "HELD
  pending its OWN current-contract full-packet check" — an independent line, not sequenced behind NearGas. Gating
  recommendation survived adversarial refutation (not refuted).

  Method note: an 8-agent understand/design/verify fan-out ran; U1(seam)/U3(magenta) returned schema-valid STUBS and
  U4(design-research) hit the StructuredOutput retry cap — all three recovered/redone first-hand by me (I already held
  the seam from direct reads); U2(gate) and the 3 adversarial verifiers did real first-hand work and produced F1/F2.

state_changes: |
  - ADD work/c-plan-characters-002-plan.md — the FROZEN В2 spec (both legs, F1/F2 baked in, v21 gating, cut list,
    riskiest assumption, lens sweep, downstream). END_OF_FILE trailer present.
  - ADD work/c-exec-char-v2-reaction-core-build-001-call.md — RUNNABLE Leg 1 BUILD CALL (self-contained, ABS spec
    path, reuse GasCoopGame_p2a0_002, opening idempotent v20→v21 re-sync, independent-RED headless reaction state
    machine + knockdown-aware source wrapper, seam types byte-identical, no rig/ragdoll/material/merge). END_OF_FILE.
  - UPDATE NOW.md (rebased over concurrent s-work-publish-near-gas-v21-main-and-open-binding-001, all its NearGas
    changes preserved): set updated session; register open_call c-exec-char-v2-reaction-core-build-001 (READY PARALLEL,
    character track — not the primary next) and c-exec-char-v2-body-rig-ragdoll-build-001 (Leg 2, HELD until Leg 1 G5);
    remove resolved decision d-char-v1-post-g5-001. NOW.next UNCHANGED (M1 route review stays PRIMARY).
  - APPEND LOG.md line; ADD this full RESULT to history/2026-07-14-s-plan-characters-v2-freeze-001.md.
  - UPDATE knowledge/g6d4e-char-v1-socket-delivered.md — «Дальше» now points to the frozen В2 plan + resolved decision.
  - REGENERATE owner panel work/board/dashboard.html — character sections reflect В2 frozen + Leg 1 open + Leg 2 HELD +
    d-char-v1-post-g5-001 resolved (Вариант 1); new 14 July journal entry.
  - Preserve TREE/CHARTER, all g-9c41/NearGas concurrent edits, the dirty marketing file, and product repos unchanged
    (not staged/committed by this RESULT).

captures:
  - Approach A (full custom rig + ragdoll) and Approach C (procedural-only tip-over) rejected at shape; kept as options if B fails.
  - Named fallback: Unity built-in ragdoll (Rigidbody + Character Joint) if PuppetMaster cosmetic blend proves inadequate under owner-eye — an ESCALATE decision, not a silent swap.

decisions_needed: []

play_check:
  - 1 Recite node goal/done_when + parent: done — g-6d4e В2 body через тот же сейм; parent = character presentation track (parallel, not a 2nd bet; g-9c41 spine stays #1).
  - 2 Appetite first: done — small parallel-track appetite; two focused BUILD legs (Leg 1 headless core tiny; Leg 2 engine/owner-eye), «legs not calendar».
  - 3 Approaches then minimal solution: done — 3 structurally different mechanisms (A build / B reuse+cosmetic / C procedural); chose B with why-over-others; A/C → captures.
  - 4 Scope hammer / cut list: done — cuts: full facial/hand rig (parked), gas-coupled reaction (В3), networked ragdoll (В3/FishNet), damage-driven knockdown (Sc-damage HELD), PuppetMaster fine-tuning.
  - 5 Lens sweep: done — core_gameplay_depth+technical_feasibility = tasks; coop_first/commercial/audience/scope_production = not_needed with reason.
  - 6 Riskiest assumption first: done — F1 knockdown↔authoritative contract; tested HEADLESS in Leg 1 before Leg 2 art.
  - 7 Tasks 3-7, riskiest first, kinds marked: done — Leg 1 (executor, headless) opened runnable; Leg 2 (executor, engine/owner-eye) HELD; binding G5 sessions named.
  - 8 Kill criteria / gating: done — v20→v21 gating decided in PLAN (idempotent re-sync at Leg-1 entry, not behind NearGas); leak-into-authoritative or seam-type change = STOP.
  - 9 Close — show bet, owner approval (owner): done — owner «1 да / 2 да / 3 как ты рекомендуешь» cited; spec frozen only after those words; Leg 1 CALL ready.

log: 2026-07-14 — plan/freeze (g-6d4e/В2, s-plan-characters-v2-freeze-001): В2 body spec frozen (owner «1 да / 2 да / 3 как рекомендуешь»); Leg 1 headless reaction SM + knockdown-aware source RUNNABLE, Leg 2 rig/ragdoll HELD until Leg 1 G5; v20→v21 = idempotent re-sync at Leg-1 entry not behind NearGas; magenta = URP-default (own material); d-char-v1-post-g5-001 resolved (Вариант 1). → history/2026-07-14-s-plan-characters-v2-freeze-001.md

next: |
  # CALL c-exec-char-v2-reaction-core-build-001 (Leg 1, RUNNABLE — parallel character track, NOT the direction's PRIMARY next)
  to: executor (GasCoopGame BUILD session; BUILD Opus/Claude Code, VALIDATE Codex cross-family read-only)
  for: g-6d4e / В2 Leg 1 — headless reaction core + knockdown-aware source
  spec: work/c-exec-char-v2-reaction-core-build-001-call.md (self-contained; authority = work/c-plan-characters-002-plan.md §4 Leg 1)
  note: |
    PRIMARY direction next stays NOW.next = c-review-poligon-m1-route-reset-001 (M1 bet review). This character
    Leg 1 is a READY PARALLEL executor leg. Leg 2 (c-exec-char-v2-body-rig-ragdoll-build-001) stays HELD until a
    fresh Direction binding G5 confirms Leg 1. The BUILD session runs in a fresh GasCoopGame session on worktree
    GasCoopGame_p2a0_002; on return, the binding fresh G5 runs as a separate Direction session.

END_OF_FILE: live/indie-game-development/history/2026-07-14-s-plan-characters-v2-freeze-001.md
