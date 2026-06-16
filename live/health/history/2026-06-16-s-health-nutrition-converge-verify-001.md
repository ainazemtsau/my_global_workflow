RESULT s-health-nutrition-converge-verify-001 (call: c-health-nutrition-converge-verify-001)
direction: health   play: converge-verify   node/task: g-health-nutrition-system

outcome: |
  Verdict: FAIL / bounced to converge-arch correction.

  The contract/architecture surface for g-health-nutrition-system is not clean enough for shape.
  Independent refutation found three blocker gaps:
  - B1: NCA1/NCA4 do not explicitly bind nutrition review to the core-owned review policy/cadence/procedure.
  - B2: TREE regular nutrition process extension points are not contract-covered as core procedure-template invocations.
  - B3: NCA8 overstates a current planned day_type producer; core evidence proves a CA5 provenance contract only.

  No §SIGNOFF was written. Shape is blocked until converge-arch correction closes B1-B3 and fresh
  converge-verify passes.

evidence: |
  Freshness / G5 posture:
  - This c-health-nutrition-converge-verify-001 session is separate from the converge and converge-arch sessions that authored the nutrition WHAT/NCA rows, so this is the binding fresh refutation for the spec.
  - No in-session subagent pre-pass was used; the verdict is the parent session's direct refutation.

  Product/core evidence:
  - Cloned ainazemtsau/health-ai at 8bc980ad21d3f54cbd27b28dcb363e0198c46751.
  - Ran `python tools/check_acceptance_matrix.py`: PASS; 17 acceptance rows, 9 contract rows, 27 PLAN rows, 9 architecture inputs, blocker gaps 0.
  - Ran `python tools/check_core_slice.py`: PASS; 32 core files, schema/frontmatter OK, matrix target files OK, PLAN/LOG separation OK, forbidden module/runtime directories absent.
  - Ran `python tools/check_core_evidence.py`: PASS; 11 dry-run scenarios, 26 acceptance/contract rows pass, blocker gaps 0.
  - Read core/review.md: review is core-owned reconciliation reading PLAN, LOG, metrics, derived anchors, safety guardrails, and cadence policy.
  - Read core/procedures/template-contract.md: procedures are declarative, have trigger/inputs/stop/touch boundaries, and never self-schedule.
  - Read core/provenance/day-type.md: CA5 is a provenance contract only; no nutrition target is implemented there.

  Independent oracle authored before attack:
  - DCN1 source-of-truth and authority boundary.
  - DCN2 additive core attach and no duplication of core-owned concepts.
  - DCN3 owner-fact vs expert-variable boundary and non-blocking intake.
  - DCN4 personalized cycle derivation.
  - DCN5 practical outputs and recipe executability.
  - DCN6 base-prep/reuse and grocery/prep correctness.
  - DCN7 low-friction nutrition tracking LOG and materiality.
  - DCN8 tracking-to-review mutation, autonomy, and brakes.
  - DCN9 bad-week/fallback/adherence preservation.
  - DCN10 safety/crash-diet/medical boundary.
  - DCN11 external app/future mirror seam without current app authority.
  - DCN12 training/activity interaction and build-order/dangling producer checks.
  - DCN13 Direction OS visibility and raw-data ownership boundary.
  - DCN14 regular nutrition procedure extension points with no runtime scheduler.
  - DCN15 HOW firewall: contract vs PLAN/implementation.

  Completeness attack:
  - TREE source-of-truth clauses map to W1/W2 plus NCA1; PASS.
  - TREE practical outputs map to W5/W6/W7 plus NCA2/NCA5/NCA6; PASS.
  - TREE nutrition review maps to W8/W9 plus NCA3/NCA4; semantic loop present, but core-review ownership is not explicit; B1.
  - TREE regular process extension points only map weakly to W1 bounded process specs, NCA1 procedure surface, and W13 future seam. No NCA row says nutrition recurring/process specs are declarative core procedures, invoked only by operator/review and never by scheduler; B2.
  - TREE specialized-app and Direction OS boundary maps to W12/W13 plus NCA7/NCA9; PASS.
  - TREE body outcome / no crash diet / bad weeks maps to W9/W10/W11 plus NCA2/NCA4/NCA6; PASS.
  - Core attach maps to NCA1/NCA3/NCA4/NCA8, but core-owned review policy/cadence is absent from NCA1 and only implicit in NCA4; B1.
  - Training day_type is named as future-nonblocking, but NCA8 says current planned source exists in core while product evidence only proves a provenance contract; B3.

  Smuggling / firewall attack:
  - NCA0 starter seed traces to done g-health-starter-kit and signed WHAT; PASS.
  - NCA1 profile/phase/metrics/parser/procedure/schema/attach traces to core CA4/CA7/CA8/CA9 and health-ai files; PASS except review omission B1.
  - NCA2 personalized cycle traces to W3/W4/W5/W8/W9 and core profile/phase/metrics; PASS.
  - NCA3 tracking LOG traces to W8 and core parser/materiality/non-blocking policy; PASS.
  - NCA4 mutation semantics trace to W9/W10/W11, but the producer is named as "nutrition review" rather than a nutrition invocation of core-owned review; B1.
  - NCA5 base-prep/grocery traces to W6/W7; PASS.
  - NCA6 bad-week/safety traces to W10/W11 and core safety/minimum tracked signals; PASS.
  - NCA7 future mirror traces to W12/W13; PASS.
  - NCA8 day_type traces to core CA5, but the "current planned source exists" claim is not proven by the read core evidence; B3.
  - NCA9 Direction OS boundary traces to core CA1/WA11 and W1/W8/W12; PASS.
  - HOW leakage sweep: no current UI/app/Mealie/runtime/DB/server/cron/scheduler requirement found in NCA rows; concrete schemas/tokens/magnitudes route to PLAN. PASS.

state_changes: |
  1) Update live/health/NOW.md:
     - active_bet.note now records failed converge-verify and B1-B3 class blockers.
     - next is replaced with CALL c-health-nutrition-converge-arch-correction-001.

  2) Append to live/health/LOG.md:
     - 2026-06-16 — health/g-health-nutrition-system converge-verify: FAIL; bounced core-review, regular-process, and day_type producer blockers to converge-arch correction. → history/2026-06-16-s-health-nutrition-converge-verify-001.md

  3) Create live/health/history/2026-06-16-s-health-nutrition-converge-verify-001.md with this RESULT packet exactly.

captures:
  - Proposed knowledge canon for later review/pulse: nutrition-module-on-core decision-class checklist DCN1-DCN15 from this verify.

decisions_needed: []

play_check:
  - 1 Recite the claim: done. Attacked both propositions: complete question set and no answer depending on unresolved/smuggled questions.
  - 2 Attack completeness with independent oracle: done. Authored DCN1-DCN15 before attacking; found B1, B2, B3.
  - 3 Attack smuggling: done. Traceability mostly passed, HOW firewall passed, but B1 and B3 remain untraced/overstated contract claims.
  - 4 Close: done. Verdict FAIL; no §SIGNOFF; next routes to converge-arch correction carrying exact blockers.

log: |
  health/g-health-nutrition-system converge-verify: FAIL; bounced core-review, regular-process, and day_type producer blockers to converge-arch correction.

next: |
  CALL c-health-nutrition-converge-arch-correction-001
  to: session
  direction: health
  play: converge-arch
  node: g-health-nutrition-system
  goal: |
    g-health-nutrition-system contract/architecture closure is corrected so verifier blockers
    are closed and the node is ready for fresh verification.
  context: |
    Read:
    - live/health/CHARTER.md
    - live/health/TREE.md
    - live/health/NOW.md
    - live/health/work/converge-g-health-nutrition-system.md
    - live/health/work/converge-g-health-nutrition-system-arch.md
    - live/health/work/converge-g-health-core.md
    - live/health/knowledge/health-core-corrected-g5-review.md
    - health-ai acceptance/core/evidence-summary.md
    - health-ai acceptance/core/matrix.json
    - health-ai core/extensions/attach-contract.md
    - health-ai core/metrics.md
    - health-ai core/review.md
    - health-ai core/progression/cadence.md
    - health-ai core/procedures/template-contract.md
    - health-ai core/provenance/day-type.md
    - health-ai core/profile/owner-facts.md
    - health-ai core/profile/derived-anchors.md
    - health-ai core/intake/non-blocking-questions.md
    - health-ai core/parser/materiality.md
    - health-ai core/principles/minimum-tracked-signals.md
    - health-ai core/phases.md

    Correct these converge-verify blockers exactly:
    - B1: NCA1/NCA4 do not explicitly bind nutrition review to core-owned review policy/cadence/procedure.
      Core evidence says review is a core-owned reconciliation step; current NCA4 can read as a duplicated
      nutrition review engine.
    - B2: TREE's regular nutrition process extension points are not contract-covered as core procedure-template
      invocations. Current coverage maps them only weakly via W1/W13/NCA1; examples include new dish search,
      fallback refresh, pantry-based recipes, and low-time-week adaptation.
    - B3: NCA8 overstates the current planned day_type producer. Core evidence proves CA5 as a provenance
      contract only; either cite an actual current core planned day_type source or make the nutrition dependency
      explicitly non-blocking/fallback-safe without requiring a core rewrite.
  boundaries: |
    Do not shape the node or create executor CALLs.
    Do not add UI/app/Mealie/runtime/DB/server/cron/scheduler requirements.
    Do not rewrite g-health-core.
    Do not reopen owner-signed nutrition WHAT unless a blocker proves a true WHAT-level gap.
    Do not store raw daily food/weight/photo/check-in logs in Direction OS.
  done_when: |
    B1-B3 are closed in the nutrition contract/architecture artifact or explicitly routed as unresolved.
    No new current app/runtime/UI requirement is introduced.
    No g-health-core rewrite requirement is introduced.
    Open/deferred high-risk architecture rows are zero, or exact remaining blockers are returned.
    Next route is a fresh converge-verify CALL.
  return: |
    RESULT with corrected contract/architecture rows, evidence against B1-B3, state_changes, play_check,
    and next CALL.
  budget: one focused correction movement
  surface: any capable session

END_OF_FILE: live/health/history/2026-06-16-s-health-nutrition-converge-verify-001.md
