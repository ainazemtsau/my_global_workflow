# g-9c41 — the road slot after Sc-reactions is Sc-catalog (NOT env-typing) — drift-guard

**Who reads this / when:** any g-9c41 session touching the character road after Sc-reactions, and any writer applying a Sc-catalog / Sc-typing RESULT. Read it before assuming «Sc-typing / env-derived typing» is the next slice.

## The reframe (owner, 2026-07-08, s-shape-sc-catalog-001)
The g-9c41 character-road slot after Sc-reactions was RE-SCOPED **Sc-typing → Sc-catalog**. Sc-catalog = a solid, convenient, EXTENSIBLE kit to author **several genuinely-different gas TYPES as DATA** — each carrying its own laws via an extensible per-type param set (a new param = data, ZERO Core/** edit; inherit common→meta→type; folded into the handshake) — plus **reactions between them** on the Sc-reactions engine, plus the **handler-into-production-tick fix** (VoxelFaceFlow.Step hardcodes CreateDefault; a data-authored outcome must actually fire). ENGINE-ONLY. Ready CALL = `work/c-exec-034-sc-catalog-call.md`.

Owner scope boundary («делаем только что нужно игре»): BUILD only the above. Design-AWARE but build NOTHING of: env-conditioned params, mods/DLC/external-loader, procedural generation, look-lane/visual work, new gas physics. Types differ by their LAWS, drastically — but the visual (texture/noise/motion, not colour) is a SEPARATE slice (g-7e15), out of scope here.

## Env-derived dynamic typing is PARKED (not cancelled)
The former «Sc-typing» = env-derived identity (committed env-vector + per-cell exposure accumulator + hysteresis type-flip) is a LATER slice, socket-aware. Its design is PRESERVED in `work/c-exec-033-sc-typing-call.md` (bannered SUPERSEDED). Per SPEC §5 it is a «НОВОЕ ядро-требование» — the Sc-catalog PLAN's manual spec-check annotates the SPEC §5 «Динамическая типизация» block + §4 seam-5 exposure-accumulator note as **PARKED — socket-only** so the canon text does not resurface as drift. Precise canon: only TEMPERATURE-keyed typing waits on the deferred temp→gas feedback (d-tempfeedback-001); density/neighbour-driven typing could come earlier — do not preclude either path.

## Why the drift-guard exists (the collision)
A PARALLEL session `s-work-sc-typing-call-001` (accidental wrong chat, per owner) framed the env-typing version as **c-exec-033** and set it as the committed `next` while THIS session was shaping Sc-catalog. Owner: «случайно запустил не тот чат … остальные считаем за ошибку». Reconciliation: Sc-catalog wins (live owner instruction > committed state), c-exec-033 superseded, g-d3a8 design-lab track preserved. Lesson (recurring): g-9c41 has ≥2 writer sessions racing — reconcile against committed HEAD before writing, serialize writers. See [[workflow-stale-call-reverify-committed-state]], [[g9c41-drift-root-and-single-source-fix]].

END_OF_FILE: live/indie-game-development/knowledge/g9c41-sc-catalog-reframe.md
