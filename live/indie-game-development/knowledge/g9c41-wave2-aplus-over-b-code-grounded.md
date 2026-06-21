# Gas-model дорога A+ over B is CODE-GROUNDED, not just argued

read_by: shape of the next g-9c41 bet (when picking the road / sizing the appetite); the technical-feasibility lens (every future "rewrite the core" temptation); a converge session if the gas model is ever re-converged.

Accepted 2026-06-20 by review s-review-002 (independent adversarial check of work/gas-model-design-full-2026-06-20.md, 3 angles, code+math, NO dealbreaker).

**Fact.** The recommendation "дорога A+ (grow the proven integer graph core), NOT B (continuous-field rewrite)" is not a preference — it is proven by committed code+tests:

- The integer-graph determinism A+ REUSES is real and tested: `CoarseBandStep` is integer-native/`unchecked`, mass-exact, contractive; it ships a `FloatMutant` reduction whose only job is the CR3 negative control, and a test asserts the float arm's hash DIFFERS from canonical on ≥1 cell — i.e. "float silently breaks bit-exact" is *demonstrated*, not claimed. Followers reconstruct from the wire and never re-run the solver, so cross-machine divergence is structurally impossible by construction. Replication is proven host+2-followers bit-exact under fault (omitted-region divergence control passes), verdict HOLD under sustained load.
- B would knowingly THROW AWAY this proven Wave-1/2 work to re-open the most expensive solved problem: cheap **and** deterministic replication of an arbitrary-resolution continuous field over a no-dedicated-server (one-host) coop link. That is the unsolved-expensive problem; A+ already has the cheap deterministic answer.
- C (a 1–2-wk bounded continuous-field net-replication probe) is insurance only if the owner still doubts A+; the honest read is C will just rediscover that "a deterministic continuous field must be integer-discretized = A+ with extra steps."
- §K repo-overlay grounding: 9 of 11 "already built" claims hold EXACTLY against the code (the 2 imperfections are over-statements of fidelity/scale, not fabrications: "sillZ portals" today ≈ a 2-band height quantization; the real-DA geometry-derived-id path is proven only at 6 sectors while the ~3,300 scale lives on a SYNTHETIC graph). So A+ is honestly an EXTENSION on a proven base, NOT a disguised rewrite — the "purely new" set (geodesic front/Dijkstra, interest-grain, resident-gas damage, reactions, blast-as-transport, edge-destructibility) is genuinely absent from the Core and is where the real new work lives.

**How to apply.** Treat "rewrite the gas core into a continuous field" as carrying the burden of re-proving deterministic networked replication from scratch — a burden A+ does not have. Default to growing the LOCKed integer graph. Honest residual: throughput-at-scale is still a PROJECTION (proven scene-size-independently for the recovery mechanism + per-chunk cost, NOT at full-level scale) — "LOCKED + HOLD" ≠ "proven at full level scale"; that is exactly what the §G probes ([[g9c41-wave2-gload-probes-incomplete-plus4]]) must close before any A+ bet.

Relates to [[g9c41-wave2-gload-probes-incomplete-plus4]], [[g9c41-wave2-coarse-proof-not-resolution]], [[g9c41-wave1-hold-mechanism-lossy-projection]].

END_OF_FILE: live/indie-game-development/knowledge/g9c41-wave2-aplus-over-b-code-grounded.md
