# NearGas L1B — owner preflight A checkpoint

date: 2026-07-16
direction_task: g-9c41 / L1B-PLAN
status: owner-selected preflight input; NOT a product PLAN; NOT final PLAN approval; NOT product-task dispatch authority
source: current Codex Direction session, exact owner reply `A`

## Authority boundary

The frozen Direction acceptance remains `work/neargas-l1b-acceptance.md`. The product planner must re-read fresh
GasCoopGame root authority and own the architecture. This checkpoint records the owner's selected direction; it does
not override the product repo, authorize implementation, or satisfy the CALL's final owner-approval gate.

## Selected direction A

1. Use one operation-local internal observation context on the real `NearGasSimulation.ReplaceGeneration/Step` path;
   ordinary/public execution supplies no observer. No global mutable switch and no public API expansion.
2. Define retry snapshot as a deep immutable record of every retry-relevant committed field. Candidate scratch may be
   excluded only where the PLAN proves its epoch reset/abandon semantics; absence of that proof is a STOP.
3. Freeze exactly two semantic fault points: replacement candidate built before publish, and Step fully prepared after
   staging but before commit. Preserve the existing exception, generation/tick and atomic rollback behavior.
4. Handler classification records the actual concrete handler object invoked at the real call site. Kernel rows record
   actual canonical sparse-kernel row identity and order, not a reconstructed or parallel surrogate.
5. Loopback is a test-side correlation of the four upstream raw record families. It is not runtime telemetry, replay,
   networking, gameplay/co-op proof, C1 digest authority or a comparison of peer `GenerationId` values.
6. The dependency chain is Capture → Classify → Trace with separate ownership, product-registry admission and serial
   integration. Parallel tracks may prepare disjoint work, but the Editor/integration path remains serialized.
7. Truncation, observer effect, any failed family, or a 4/5 result is RED / L1B NOT MET. Rollback removes only the L1B
   observation delta and leaves delivered L1a authority and behavior intact.

## Fresh-admission stop

Read-only preflight of published product `5cd18250` found the previous protocol-repair registry row still labelled
`HANDBACK-PENDING` despite its later verified close. Before any PLAN artifact write, the product session must re-read
the current canonical registry and use only a registry-authorized serialized lifecycle/admission transaction. If the
current protocol cannot legally close/release that row and admit L1B, STOP and return the exact lifecycle blocker.

## Approval distinction

`A` approves this preflight direction only. The owner has not yet approved a completed product planning package and
has not yet explicitly asked Codex to create the required separate product task. A future product session must present
the actual committed PLAN package for an explicit owner verdict; no approval may be inferred from this checkpoint.

END_OF_FILE: live/indie-game-development/work/neargas-l1b-plan-owner-a-checkpoint.md
