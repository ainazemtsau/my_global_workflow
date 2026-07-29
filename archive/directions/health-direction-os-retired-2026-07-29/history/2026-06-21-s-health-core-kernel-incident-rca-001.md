# RESULT -- s-health-core-kernel-incident-rca-001 (incident RCA + workflow-loop repair)

direction: health - node: g-health-core - bet: b-health-core-kernel
trigger: owner pasted a problem transcript (HCI chat) -- first nutrition menu divergence + "the executor never returned a RESULT i could apply"
date: 2026-06-21

## outcome
Cross-repo root-cause analysis of the nutrition menu incident, adversarially verified (workflow wf_39392526-26c:
8 agents -- 4 readers, 3 skeptic verifiers, 1 synthesis; verdicts: contradiction=HOLDS [it is NOT a contradiction],
executor-defense=PARTIAL, state-drift=HOLDS). OS live/health re-synced to product reality (it had drifted a full
leg). Remediation routed to CALL c-health-core-kernel-incident-fix-001. Nutrition PAUSED.

## what actually happened (evidence-grade)
- The kernel spine (KC1-KC11 + KC14) was BUILT in health-ai; the binding journey-proof walked SEED->PROPOSED->ACTIVE
  with evidence (679dd8d) and SURVIVED a fresh-session refutation (9a0124a). The bet binding precondition is met.
- The executor returned its results ONLY inside the health-ai repo (in-product governance_handoff_packet files),
  NEVER as an OS RESULT with state_changes. So live/health never advanced: it still said t-3 todo / executor CALL
  ready / nutrition out-of-scope. This is the workflow-loop gap the owner hit ("nothing to apply").
- The first nutrition run then overran the thin-attach boundary (ran intake->program->cycle->menu) and an agent
  surfaced+persisted a CONCRETE owner-facing menu as PROPOSED without owner approval (8504d3f). Owner reverted to
  SEED + added an interim gate.md "confirm before authoring" patch (adebf3d).

## root causes (verified -- NOT a WA-K2/WA-K3 contradiction)
1. Under-specified FREEZE seam. The signed source is consistent (KV3 carries "(never directly ACTIVE)" = a status
   ceiling; KV20/KV21 = confirm-before-save). But the frozen WA-K3 done_when line DROPPED the ceiling clarifier and
   any cross-ref to WA-K2's first-save timing, so a code-only agent read "always lands PROPOSED" as a write-now
   license. The product file authoring-activation-separation.md repeats the gap. Two skeptics failed to prove a
   strict contradiction; the HCI chat overstated it as "mutually exclusive".
2. MISSING REQUIREMENT. "Abstract/numeric structure first; never pick concrete foods for the owner" was never in
   any contract until adebf3d -- it lived only in chat/history (WA-K11 violation). Even a perfect WA-K2/K3 only
   says "show before save", never "and the thing shown must be abstract".
3. STALE CONCRETE DATA + contradictory status flags. recipes/grocery/fallbacks/review still carry
   status=active_first_cycle + selected_workflow_state=WEEK_PLAN while their source menu=SEED; x_nutrition/index.md
   advertises them as "active artifacts", so agents grab them. recipes/first-cycle-base-recipes.md = 8 named dishes
   (the table ChatGPT reported grabbing).
4. Owner-facts (125 kg + clinical smoking-cessation block) duplicated into ~16 files instead of one source
   (core/profile/owner-facts.md).
5. No visible proof-of-load marker on chat replies (owner-requested mechanism).

## fault
- Largest share = the design/spec-freeze + converge-verify process (this direction's own sessions): the freeze
  dropped the clarifier; the blind oracle missed the seam; WA-K3 shipped a green control fixture matching exactly
  the bad act while WA-K2 shipped prose with no fixture, so a code-optimizing agent followed the testable rule.
- Executor (Codex): CLEARED of "fabricated report" (close-out ca71505 is byte-faithful and explicitly disclaims
  recipes/grocery/daily content) and of mechanical one-chat-one-job. Genuine sins: persisted owner-facing content
  unapproved (8504d3f), a 4-commit/~8-min run with no owner turn between (spirit of one-chat-one-job), and no OS
  RESULT.

## correction to the prior fix framing (owner was right)
The first owner-facing pass proposed "autotests/fixtures" as the fix. Owner correctly rejected it: this is an
LLM-instruction store, not a code repo -- a lint over markdown cannot guarantee what a chat will do. Real
guarantees for this system = (a) a visible proof-of-load marker on every reply, (b) ONE clean source of truth with
no stale duplicates, (c) short unambiguous instructions, (d) cross-model fresh-session refutation (the existing
G5). Markdown fixtures are at most a weak secondary aid, never the mechanism.

## state_changes applied (writer = this session, post-RESULT)
- NOW.md: tasks.t-3 todo -> done_with_incident (+done_note); open_calls
  c-health-core-kernel-spine-journey-executor-001 ready -> done (+incident_note, +closed); NOW.next replaced --
  the original build CALL marked SUPERSEDED/historical (frozen WA-K1-K12 verbatim retained as reference; permanent
  home health-ai acceptance/kernel/wa-k.md) and a new CALL c-health-core-kernel-incident-fix-001 set as the real
  next action.
- LOG.md: appended the 2026-06-21 incident + workflow-loop repair line.
- history/: this file.

## next
CALL c-health-core-kernel-incident-fix-001 -- (1) health-ai cleanup of stale concrete content + owner-facts
de-duplication + index fix [owner-confirm delete scope first], (2) seam reconciliation [os-maintenance], (3)
proof-of-load marker, (4) WA-K6/K8 live walk. Nutrition stays PAUSED. See NOW.next.

END_OF_FILE: live/health/history/2026-06-21-s-health-core-kernel-incident-rca-001.md
