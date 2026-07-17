# Health Reclamation Reforging v2 — M2 lifecycle decision

decision_at: 2026-07-17
direction: solmax
decision: ADMIT
admitted_definition: 4ed9cd1542ce8d6bf327b7aba443db759b77f92b
closing_evidence: d4c22f4903eb5b2ea7ccecb4b577084be522d66f
activation_scope_id: solmax/hr-m2-first-live-v1
status: ADMITTED_NOT_AUTHORIZED_NOT_ACTIVATED_NOT_LIVE_PROVEN

## Decision

`4ed9cd1542ce8d6bf327b7aba443db759b77f92b` is semantically admitted only
as eligible for the bounded activation configuration below. The admission is
for the exact fifteen-file Health Reclamation pack definition at that commit.

`d4c22f4903eb5b2ea7ccecb4b577084be522d66f` is closing evidence and
materialized authority; it is not the effective process definition. Neither
commit is activated by this decision. Owner acceptance closed BUILD but is not
activation authorization, an activation result, first-live proof, usefulness
proof, recurring-reliability proof, or reuse proof.

## Admission basis

- The formerly pending bounded repair is present as exact direct child
  `7ed7903 -> 00a23b0`: the three allowed paths only, OP-HR01/KH-HR01 repaired,
  sibling sweep closed, protected surfaces preserved, and repository gates
  recorded green.
- The admitted successor is the linear descendant
  `00a23b0 -> c1c1236 -> 49c77d7 -> ae9e7e9 -> 4ed9cd1`.
- Fresh round-3 G5 at exact `4ed9cd1` is PASS: A-01..A-50 50/50,
  M2-A01..A07b 8/8, P-01..P-12 12/12, C01..C16 16/16 removed,
  OD/AM 8/8, original F-01..F-07 7/7, REVIEW items 11/11, and G5-R2-01
  fixed with sibling sweep closed and no refuted finding.
- Closing commit `d4c22f4` is the direct child of `4ed9cd1`, changes exactly
  RESULT.md plus seven evidence/authority files, and leaves every
  `packs/health-reclamation/**` blob unchanged.
- All six frozen authority SHA-256 values and the review SHA-256 match the
  closing report. Current inner-loop, negative selfcheck and deliver gates are
  green; both required exact-diff whitespace checks are green; the product
  worktree is clean.
- The candidate declares the mandatory semantic capabilities and an explicit
  legitimate degraded route when the private durable writer is absent.

## Allowed bootstrap carrier and adapter binding

For `solmax/hr-m2-first-live-v1` only:

1. **Definition carrier:** the exact Markdown pack tree at `4ed9cd1`, verified
   by the blob manifest in the closing evidence. Markdown carries the
   definition but owns no process meaning or lifecycle authority.
2. **Owner-facing carrier:** one private ChatGPT Project conversation used for
   read-only reasoning and routing. The project must receive the exact admitted
   definition and the configuration below; project/file presence is not
   activation evidence.
3. **Lifecycle verifier/adapter:** Codex with read access to
   `C:/projects/solmax-operating-substrate` may verify identity, binding and
   activation evidence and return the lifecycle handback. Codex supplies
   capability only; it cannot self-authorize activation or become Health
   policy/clinical authority.
4. **Private writer adapter:** disabled for the first activation. No durable
   personal capture, correction, revocation or deletion may be claimed.

The carrier and adapters are bounded implementation choices, not substrate
architecture and not permission to substitute another commit, provider,
storage target or effect surface without revalidation.

## Apply and activation authority

- **Admission authority:** this Solmax Direction session, based on exact fresh
  G5 and closing evidence.
- **Activation authorization:** the owner, in a later session, by explicit
  words bound to `solmax/hr-m2-first-live-v1`. The earlier M2 acceptance is not
  reused as this authorization.
- **Activation apply authority:** a fresh t-5 executor handback is validated by
  a Solmax Direction session; only that session's valid RESULT, applied by the
  Direction writer, may establish `4ed9cd1` as effective for the bounded scope.
  The authoritative non-personal lifecycle receipt lives in Direction history
  and points to the exact definition, carrier/config identity, owner words and
  apply disposition.
- **Personal-state apply authority:** none in this first configuration. The
  private writer is absent, so any write request must return no apply/no save
  plus a portable continuation.

An activation attempt returning `rejected`, `conflict`,
`failed-known-not-done`, `partial`, or `outcome-unknown` does not activate the
candidate. Presence in ChatGPT, a commit, a tool call, an artifact or owner
authorization alone is not an applied activation.

## Mandatory first-activation configuration

- exact definition: `4ed9cd1542ce8d6bf327b7aba443db759b77f92b`;
- evidence basis: `d4c22f4903eb5b2ea7ccecb4b577084be522d66f`;
- scope: one owner, one new-work first-live campaign scope, no predecessor
  migration and no concurrent v1 authority;
- state mode: `private-portable-continuation-no-durable-write`;
- current personal basis: only current free-form owner input plus an explicitly
  supplied compatible private continuation; no legacy import or model-memory
  reconstruction;
- public repo and Direction OS: non-personal lifecycle pointers/evidence only;
  no health facts, reports, menus, programmes, metrics or raw continuation;
- durable capture/private mutation: disabled; private writer absent;
- external effects: disabled, including booking, buying, messaging, scheduling,
  publishing, device control and background monitoring;
- ordinary current-source check: disabled unless separately authorized for one
  bounded question; stale model knowledge is not a fallback;
- Deep Research: disabled for the first pass; a material gap may return a
  launch-ready request but may not launch or simulate the child;
- starter authority: the exact `m1-m2-design.md` SHA-256 binding recorded by
  the admitted candidate; mismatch disables only dependent A5-01/A5-02 support;
- safety: possible urgent/emergency signals preempt ordinary coaching; a
  nonurgent professional-judgment gap holds only the affected route;
- honest closures: useful action/proposal, one material question, clear
  affected-route block, no-change/stop/rollback decision, or portable
  continuation only.

## First live boundary and required evidence

First live begins only after an authoritative `applied` activation result. It
is one ordinary, owner-originated, low-consequence Health Reclamation
obligation handled in t-6. It may perform a first council, current-day/session
support or a bounded programme proposal. It may not perform external effects,
durable private writes, legacy migration, Deep Research, medically dependent
intervention, M3 work or a reliability/reuse test.

Before that live obligation, t-5 must execute the abstract adverse branch
`explicit capture request + private writer absent`: useful reasoning continues,
zero apply call occurs, no save is claimed, the unsatisfied obligation is
named, and a private portable continuation is returned without personal data
in repository or Direction evidence.

The first-live evidence packet must record, without exposing personal health
content:

- exact effective definition and carrier/config identity;
- the owner's exact activation-authorization words and authoritative apply
  disposition/receipt;
- compatibility/current-basis disposition and confirmation that v1 is not
  concurrent authority;
- a private or owner-redacted identity of the real owner-originated obligation;
- procedures actually invoked and the exact owner-facing closure class;
- assumptions, unknowns, safety/authority holds and external-effect status;
- capture/private-writer outcome and whether portable continuation was returned;
- the owner's actual usefulness judgment in his words;
- unresolved obligations, their current owners and the next legitimate action;
- explicit limits: recurring reliability and demonstrated substrate reuse
  remain NOT_YET_PROVEN.

M3 is not opened by this decision. It still requires a separate PLAN, the full
A3/A4/A5 research/design packet, and the required owner decisions.

END_OF_FILE: live/solmax/work/health-reclamation-reforging-v2-m2-lifecycle-decision.md
