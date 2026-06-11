---
artifact_control:
  namespace: direction_proof
  direction_id: indie-game-development
  artifact_type: receipt
  status: accepted
  owner: proof_carrying_workflow_os
---

# Constraints Definition Receipt

```yaml
receipt_id: R-IDG-CONSTRAINTS-DEFINE-001
target_obligation: O-IDG-CONSTRAINTS-DEFINE
operator: ClarifyObjective
status: accepted
accepted_constraints:
  solo_capacity: >
    Solo developer by default, with AI/Codex/workflow assistance allowed.
    No human team is assumed by default.
  weekly_time_capacity: >
    User declares 50-80 hours/week available for the game direction.
  budget_boundary: >
    Low-spend by default. Current liquidity context is approximately $200,
    with about $100/month going to ChatGPT. Normal budget envelope is around
    $1000; extended ceiling is up to $3000 only for clearly worthwhile/high-leverage expenses.
  timeline_constraint: >
    Within 9 months from acceptance of this constraints receipt, the project
    should already generate some money/income/revenue flow. Exact amount,
    pricing, launch date, and monetization model remain unresolved.
  risk_tolerance: >
    High risk tolerance accepted, but no technology for technology's sake.
  gameplay_depth_constraint: >
    Gameplay depth is more important than technical complexity by itself.
    Technical systems, including gas simulation, must create interesting
    gameplay depth rather than pursue physical accuracy as an end in itself.
  platform_distribution_boundary: >
    Steam-only / PC-via-Steam target is accepted as the current platform/distribution boundary.
  business_marketing_capacity: >
    User is willing to execute marketing/business tasks as needed, but the
    workflow must provide a clear process/playbook for what to do, where to
    publish, when to publish, and how to evaluate results.
candidate_context_not_accepted:
  - user owns many Unity plugins
  - Unity may be economically relevant later
  - possible future marketing-team-like workflow design
not_accepted:
  - Unity engine commitment
  - exact revenue target
  - exact profit definition
  - exact pricing
  - exact launch date
  - exact monetization model
  - Steam launch strategy
  - Steam page timing
  - content calendar
  - paid ads
  - outsourcing/hiring
  - roadmap
  - Horizon
  - Active Frontier
  - Strategic Path Map
  - Codex/product execution
  - legacy import
  - old concept/archive details
scope_audit:
  target_obligation: O-IDG-CONSTRAINTS-DEFINE
  in_scope_used:
    - current human constraints input
    - accepted root objective
    - accepted success semantics
  necessary_dependencies:
    - strategy/projection remains blocked until constraints are committed
    - concept-specific details may still require optional LegacyImport later
  parked_residual_context:
    - existing Unity plugin inventory
    - possible marketing-team-like workflow design
    - detailed Steam tactics
    - exact monetization options
  blocked_or_forbidden:
    - roadmap
    - Horizon
    - Active Frontier
    - Strategic Path Map creation before commit
    - Codex/product execution
    - legacy import
  hidden_acceptance_check: pass
  one_obligation_scope: pass
invariant_checks:
  no_strategy_created: pass
  no_roadmap_created: pass
  no_execution_admitted: pass
  no_legacy_import_performed: pass
verification_result: pass
commit_scope: idg_root_scope
terminal_recommendation: commit
```

END_OF_FILE: directions/indie-game-development/workflow/receipts/R-IDG-CONSTRAINTS-DEFINE-001.md
