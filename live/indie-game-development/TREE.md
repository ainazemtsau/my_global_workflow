# TREE — indie-game-development

root:
  id: g-a7f2
  goal: |
    A solo-developed co-op Steam game built around gas + grid + expedition systems exists as a released commercial product: technically strong enough for owner pride, legible enough for players, and commercially successful enough to generate real revenue.

  why: |
    This is the direction’s top-level outcome: ship the game as both a craft achievement and a business seed, without separating technical pride from commercial validation.

  done_when: |
    All are true:

    1. The game is publicly available on Steam as either paid Early Access or 1.0 release.

    2. The game has generated real external revenue or funding attributable to the project.

    3. The project has reached the charter’s target commercial success threshold:
       - target: at least $100,000 gross lifetime revenue or funding;
       - unless the charter is later explicitly revised through a review session.

    4. The released product demonstrates the core fantasy:
       - co-op-first play;
       - gas + grid simulation;
       - destruction or spatial change;
       - distinct gas types with meaningful gameplay differences;
       - expedition pressure or equivalent mission structure.

    5. The owner explicitly accepts the released product as something he is proud to have made, based on playable evidence rather than intent.

    6. External evidence exists that players can understand and value the game:
       - Steam reviews, revenue, wishlists/conversion history, playtest reports, crowdfunding/publisher response, or other concrete market/player signal.

  status: active

  map_order: |
    g-9c41 is the spine and the priority. Parallel tracks run alongside it at an OWNER-SET cadence
    (the owner correlates load; the engine bet always comes first). The dropped "spectacular clip"
    trigger is RESOLVED (c-map-003, 2026-06-16): storefront/audience EXECUTION (g-5b07 page, g-e6f2
    cadence) starts when the marketing process g-2f8c PUBLISHES its first artifact — NOT a pre-fixed
    clip. The artifact is g-2f8c's call (canon hook + c-map-003 market research), and the build-side
    guarantee that showable material WILL exist needs NO separate node — it already lives in the
    Wave-2 player-facing terminus mandate (g-9c41 active bet) + the fixed 2026-08-31 page date
    (g-2f8c's first emission is timed to 08-31 — the teeth vs pre-mortem #2). The contested
    fixed-artifact node "(a) first player-legible artifact" was REJECTED as a crutch (artifact =
    g-2f8c's output; legibility floor already owned by Wave 2). Parallel tracks: the creative/CANON
    track (g-d3a8 design + lore) runs now via the canon track (repo gas_coop_game_canon +
    local/canon-forge); the marketing process g-2f8c is parked + ready to be shaped into its own
    local play (canon-forge-style) in a parallel low-ceremony session when the owner chooses; gas
    visibility (g-7e15), the Steam-page slice of g-5b07, and the posting cadence of g-e6f2 stay
    parked, started when the owner chooses. The g-d3a8 EXECUTABLE-CONFIG validation sub-part still
    needs g-9c41 alive (its lore/design-on-paper does not). Calendar that still holds: Fest go/no-go
    checkpoint ~late September 2026; pre-committed decision gate 2026-10-05 (see g-5b07). PROPOSED,
    decision DEFERRED at owner's request: a "co-op interdependence proof" node (b) — pre-mortem #5
    (the gas world must FORCE cooperation, currently unowned before a parked Steam Playtest); routed
    to follow-up c-map-004.

    Parallel track ADDED 2026-07-13 (s-map-characters-track-p2a0-close-001): g-6d4e «Игровые персонажи» =
    the character presentation/embodiment layer (reusable drop-in player prefab + stable adapter-API + control
    + procedural reactions + cosmetic PuppetMaster ragdoll), sibling of g-7e15, NOT a 2nd bet (adds no
    active_tasks; g-9c41 stays the spine). Born from the P2a0 verdict (Candidate A — the core owns the
    authoritative body position, ragdoll cosmetic). The deterministic "grid-ballistics" physical-interaction
    layer stays a g-9c41 CORE slice, named for later, NOT part of this track's build scope.

  children:

  - id: g-9c41
    goal: |
      A representative networked co-op scene runs and holds, on a core architected for
      huge procedural levels: 2–4 players on a player-hosted session (one player hosts; no
      dedicated server), host-authoritative multi-gas simulation on sector-band grid/room
      topology with doors/vents and at least one destruction-driven topology change,
      levels fed from procedural generators (Dungeon Architect at minimum, ideally also
      Procedural Generation Grid) through a replaceable ingestion adapter — solo-maintainable.
      The core is a REAL EXTENSIBLE LAYERED architecture (RE-SHAPED 2026-06-14, s-shape-004): independent
      system-layers ride one seam (gas + a thin DYNAMIC temperature layer + the topology/grid), communicate
      via grid events, and a REAL controlled destruction (a destructible wall breached → hole → topology
      change → gas flows; no scripted, no structural collapse) drives a topology change — a new layer/driver
      plugs in without core edits. Delivered in WAVES.
    why: every root criterion stands on this core; the direction's riskiest assumption dies first here, the moat — first commercial co-op expedition on a fine-grained multi-gas sim with destruction-driven topology (SS13/SS14 = 2D legacy and seed audience, not refutation) — lives here, and the tech stays reusable even if the game fails.
    done_when: |
      All hold in the validation harness:
      1. Performance targets met on the min-spec profile (8GB-VRAM 60-class GPU, 16GB RAM),
         not on the dev 4090; cheap validation allowed (capped profiling / used 3060).
      2. (⚠ networking clause SUPERSEDED by #12 / ADR-0010 — input-lockstep) Replication model locked: host/server-authoritative sim + chunked-delta gas
         stream; entity ghosts only for players/objects; rollback/lockstep at most one
         1–2-week timeboxed spike; GPU compute never authoritative for networked state
         (default vendor FishNet — Steam-only, free, GameObject-native; model locked,
         vendor swappable).
      3. 2+ networked clients see consistent gas behavior across a topology change; debug
         surfaces expose mass/flows/tick/topology revision; reproducible build + video.
      4. Gas types are declarative and two-level: meta-gas = behavior archetype (own
         handler behind an extension seam), gas inside a meta-gas = pure config;
         acceptance test — a third gas type lands by data alone and passes the harness.
      5. The harness is a reusable, agent-drivable asset: fixed scene set (room chain /
         ventilation / vertical shaft pattern), headless runs, deterministic seeds,
         machine-readable telemetry; no scene sprawl.
      6. A timeboxed (<=2 weeks) "gas render proof slice" locks the stylization hypothesis
         (default: quantized volumetrics) and the render-pipeline decision behind a seam,
         with a ms-budget check on the min-spec class.
      7. The core runs a clean 1-player session; player count is a first-class config
         input (no bots).
      8. (DEFERRED 2026-06-14, s-shape-004 — owner «клип не паримся») First spectacular clip
         is DROPPED from the core bet; a genuinely spectacular clip is g-7e15's later job once
         real visuals exist. The parallel-track gate that hung on this clip (root map_order)
         needs a map-level re-check (follow-up).
      9. (⚠ bandwidth-budget basis SUPERSEDED by #12 — binding limit = weakest-peer CPU under D1) Scale architecture (R1): the coarse simulation tier is designed and
         arithmetic-validated to hold a huge procedurally generated level profile
         (≈200×200×40 m class, ≥1000 volumes) within measured memory/tick/bandwidth
         budgets on the min-spec profile. (REFINED 2026-06-16, review c-review-001 —
         owner-approved «го») The bandwidth budget MUST be computed from the ON-WIRE
         rate INCLUSIVE of the periodic resync-keyframe flush (a full-state snapshot
         whose byte cost scales with cell count), NOT from offered-demand deltas alone:
         the Wave-1 t-3 lossy projection (~59k cells @275 KB/s) was offered-demand-based
         and ~5.3× optimistic; the honest on-wire lossy basis is ~11k cells (lossless
         ~4.9k is conservative). Size the coarse-tier grid against the on-wire
         keyframe-inclusive number. Building that scale (sector subdivision, 1000-object
         ingest gate) may be a later bet; this node requires the architecture and the
         numbers, not the full content.
      10. (ADDED 2026-06-14, s-shape-004; REWORDED 2026-06-16, s-shape-wave2 — G9,
          per d-tempfeedback-001 + converge-verify CAPTURE V2-4) Layered architecture
          PROVEN: ≥2 independent system-layers (gas + a thin dynamic temperature layer)
          ride ONE seam and are networked-consistent together AT COARSE SCALE (each layer
          held to the dual-guarantee per CR1/CR2/CR3). The cross-layer interaction
          observable THIS wave is the gas→temperature SINK (a reaction/heat event drives
          the temperature layer's response) — this proves the SEAM (transport +
          extensibility), NOT gameplay depth. The REVERSE temperature→gas FEEDBACK is
          DEFERRED to a later wave (post-g-d3a8, where the per-gas-type heat rule is game
          design), NAMED here, not silently dropped. A new layer/driver plugs in without
          core edits (extensible seams, R13 — EXERCISED by a 3rd demonstrative layer, not
          only argued). The destruction-driven topology change of criteria 2/3 is a REAL
          controlled wall-breach, not a scripted stub.
      11. (ADDED 2026-06-20, review s-review-002 → A+ breakdown — owner-approved «да», G9) дорога A+
          RE-FRAME: after Wave 2 PROVED the coarse model + the owner SAW it, the core is re-formed as
          the MULTI-WAVE дорога-A+ core = the proven integer graph "water" base + bit-exact networked
          replication (KEPT, criteria 2/3) GROWN with the missing layers — an integer geodesic FRONT
          ("where exactly is the gas"), interest-grain detail near the player/event, a resident-gas
          DAMAGE law (consequence), confirmed-colocation reactions, and edge-based destructibility.
          The model is graph-based (NOT a continuous-field rewrite — B was rejected: it reopens the
          solved network-determinism problem). KEEP-OPEN invariants the redesign must NOT weld shut:
          per-SPECIES temperature stays an independent readable layer; the coarse layer carries the
          TRANSIENT (not settled-only); ROOM capacity + back-pressure is KEPT (only the 2-band split
          is replaced); a sparse+tunable gas encoding (unlimited TYPE catalog; bounded concurrent-per-
          node). HOST-RESILIENCE is now a named core obligation: a host can leave/crash without ending
          the 4–8 co-op session (§H — spiked in Wave A). Every A+ bet is preceded by the §G(+4)
          load-probe DE-RISK WALL (no core blind spot found late). The wave breakdown lives in NOW.md
          wave_plan + work/aplus-breakdown-v1.md + work/aplus-wave-map-v1.md (the design source =
          work/gas-model-design-full-2026-06-20.md). Criteria 1–10 still hold; A+ deepens what "the
          core" resolves and consequences, it does not drop them.
      12. (ADDED 2026-06-22, owner-approved «да» (G9) — дорога A+ ARCHITECTURE LOCKED + SLICE METHODOLOGY;
          ADR-0010 supersedes the host-broadcast authority of ADR-0004/0005) NETCODE = input-lockstep (only
          inputs on wire; every peer deterministically recomputes; binding limit = WEAKEST-PEER CPU, not
          bandwidth — supersedes #2's host-broadcast/chunked-delta + "lockstep=spike" and #9's on-wire
          bandwidth basis). MODEL = ONE integer cell model at cell-SIZE LOD: near = full-3D grid + flow
          through OPEN FACES (area/height/no-through-walls emergent); far = room-graph ROLLUP; ROOM = a LABEL
          at every tier (pipe dropped near). DETAIL = a LOCAL non-authoritative refinement of the
          COARSE-authoritative truth (coarse computed everywhere + in checksum; detail only where a peer's
          own player is — ~1 bubble/peer not N; hard shared consequences = coarse EVENTS). sparse
          dominant-gas (D9), integer chemistry table (D10), real-height-3D near (D11). NO late-join
          (lobby→raid boundary). ZERO-legacy at completion. reusable-engine DROPPED (D12, game-first).
          DELIVERED as INCREMENTAL VISIBLE SLICES (each: PLAN-ingests-all-research → RED-first → build
          deterministic/clean/extensible → owner-VISIBLE result → integrate; per-mechanic depth classified
          ведро-1/2/3 at its slice PLAN, default room-granular). Full spec + slice graph + decision index:
          work/dev-plan-graph-2026-06-22.md. Criteria 1–11 hold where not superseded here.
    status: active
    detail: history/s-map-002.md   # + s-review-002 (A+ re-frame); wave breakdown → NOW.md wave_plan + work/aplus-breakdown-v1.md
    # ⚠ 2026-07-02 (s-repair-review-reconcile-001): read this node THROUGH the SPEC (knowledge/g9c41-gas-engine-SPEC.md).
    # Any «ADR-0010» lock citation in the goal/done_when = citation ERROR (lock = ADR-0002; SPEC §1 поправка 2026-06-28).
    # The goal-text «host-authoritative … sector-band» wording is superseded by #12 (input-lockstep) + the SPEC leading
    # frame. Node CONSOLIDATION (rewrite of the #2/#8/#9/#11/#12 banner palimpsest) is QUEUED for an owner-present
    # session — additive banners only until then. Answered scale watchmen: see knowledge/g9c41-scale-watchmen.md
    # (d-biglevels-tree9-001 for #9); NOW.decisions remains pending-only.

  - id: g-d3a8
    goal: |
      The game's design truth is coherent and current across an explicit
      authority ladder rather than treated as one finished document:

      1. Minimum Game Frame v2 is the owner-approved whole-game design
         basis and is not canon.
      2. An unresolved design question becomes an OWNER-SELECTED PAPER
         ANSWER only through an owner-present paper verdict.
      3. A paper answer becomes canon only through a separate
         owner-present canon-admission decision.

      At whole-game altitude the game is designed first for changing
      4–8-player groups, with support for the full group of eight as a
      hard design and support requirement. The exact supported lower
      bound below four remains OPEN, and solo is not a current design
      target.

      The branch preserves the Frame-v2 player promise and anchors:
      gas is the shared physical medium and regular expedition value;
      safe return converts extraction into lasting power for the current
      run; predictable tools differ from exceptional artifacts; a run is
      short, difficult and finite, with full wipe and a fast meaningful
      restart; and the Ball/Bubble remains the principal visible
      extraction DESIGN ANCHOR while its exact behavior stays OPEN.

      The branch progressively resolves gas grammar and roster,
      temporary co-op composition, expedition economy and progression,
      artifacts, depth and end-state, failure and recovery, and lore
      without promoting hypotheses, examples or untested mechanics to
      frame or canon authority.

    why: |
      This branch turns the root's pride, gameplay-depth and co-op-first
      criteria into design truth that the engine, canon and storefront can
      consume without authority drift. The explicit
      FRAME → OWNER-SELECTED PAPER ANSWER → CANON ladder lets the
      owner/AI workflow resolve bounded questions without pretending that
      paper proves fun, while the owner's available eight-person group
      provides a direct route to later real co-op evidence.

    done_when: |
      All are true:

      1. A current design document and source/status map identify
         Minimum Game Frame v2 as FRAME READY and not canon, and
         unambiguously distinguish:
         - statements accepted at FRAME altitude;
         - OWNER-SELECTED PAPER ANSWERS;
         - answers separately admitted to CANON;
         - still-OPEN questions;
         - claims requiring playable or external evidence.
         No hypothesis, example or paper answer gains canon authority
         by implication.

      2. The whole-game design states explicitly that:
         - changing 4–8-player groups are the primary current design range;
         - support for the full group of eight is mandatory;
         - the exact supported lower bound below four remains OPEN;
         - solo is outside the current design target.

      3. The Frame-v2 anchors remain intact without silently fixing their
         open implementation:
         - gas is the shared physical environment and regular expedition
           value;
         - only safely returned gas becomes durable power for the current
           run;
         - predictable tools and exceptional artifacts have different jobs;
         - one run is short, difficult and finite;
         - full wipe ends the run and the next start reaches meaningful
           decisions quickly;
         - Ball/Bubble is the principal extraction DESIGN ANCHOR, while
           filling, control, capacity, durability, rupture, required hands
           and rare alternatives remain OPEN;
         - c-001 remains limited to the conscious
           investigation → operation transition.

      4. Each remaining Frame-v2 macro fork is either resolved through
         the authority ladder or remains explicitly OPEN:
         - economy or access that makes meaningful gas return produce
           progression without making near-empty systematic returns optimal;
         - artifact origin, frequency and run-shaping role;
         - depth, staging-zone structure and final objective;
         - wipe/reset state, persistence, metaprogression and permitted
           exceptions;
         - temporary subgroup and role composition, additional value from
           4–8 players, attendance continuity, scaling and the supported
           lower bound.

      5. Current canon is indexed against the frame. Any contradiction is
         handled through an explicit amendment or supersession chain,
         never by silently expanding or rewriting a canon card.
         c-001 remains bounded to its declared question and does not
         acquire extraction, Bubble, co-op-composition, damage, economy
         or progression authority.

      6. Gas grammar is designed rather than accumulated as decorative
         content:
         - every base gas has a gameplay job involving a decision, risk,
           tool, route, consequence or co-op pressure;
         - the design catalogue may be effectively unlimited, while
           g-9c41 owns the bounded, tunable concurrent-per-node
           engineering budget;
         - reactions, mixing and anomalous gases remain consistent with
           honest physical behavior: no creature intelligence, scripted
           gas scares or hidden cheating;
         - exact roster, states, reactions and tuning remain separate
           design questions.

      7. Selected design answers are checked against g-9c41 for
         simulability and pass a structured paper red-team for internal
         consistency, dominant strategies, loopholes, degenerate
         combinations and balance hypotheses. Executable-config
         self-play may be added once the relevant g-9c41 surface exists,
         but it does not replace human play.

      8. Evidence limits remain explicit. Paper work does not certify fun,
         meaningful co-op, pacing, onboarding, runtime legibility,
         production cost, market response or the actual play value of
         eight players. Those require playable and external evidence.

      9. The owner gives an explicit verdict that he is proud of the
         resulting design, based on the current evidence level rather
         than claims beyond it.

    status: parked

    detail: |
      Current reconciliation and lineage:
      - history/2026-07-15-s-map-g-d3a8-frame-v2-reconciliation-001.md
      - history/s-map-002.md

      Current authority:
      - FRAME: work/minimum-game-frame-v2.md — FRAME READY 2026-07-14;
        whole-game design basis, not canon.
      - OWNER REQUIREMENT:
        knowledge/g9c41-players-8-owner-requirement.md — eight-player
        support is mandatory; solo is outside the current design target.
      - CANON: gas_coop_game_canon/CONSTITUTION.md, CORE.md, INDEX.md
        and canon cards.
      - CURRENT CARD: c-001 resolves only the conscious
        investigation → operation transition.

      Authority route:
      FRAME READY
      → OWNER-SELECTED PAPER ANSWER
      → separate owner-present CANON ADMISSION.

      Dependency map:
      - consistency lane:
        c-map-g-d3a8-frame-v2-reconciliation-001 [CLOSED]
        → c-repair-canon-frame-v2-eight-player-001 [READY FIRST]
        → c-repair-eight-player-live-consistency-sweep-001
          [HELD until canon repair closes];

      - design lane:
        c-map-g-d3a8-frame-v2-reconciliation-001 [CLOSED]
        → c-research-q-coop-interdependence-002
          [READY PARALLEL / PAPER-ONLY]
        → possible OWNER-SELECTED PAPER ANSWER
        → separate owner-present canon-admission CALL;

      - c-shape-sc-damage-001 remains HELD until a ready canon
        specification explicitly changes that disposition.

      The canon reconciliation changes no mechanics. The live
      consistency sweep scans only current authoritative/live surfaces
      and does not rewrite historical evidence.

      Work continues as a parallel creative/canon track through
      owner-present sessions and adds no second active bet or active
      tasks. Existing procedures remain local/canon-forge and
      local/canon-status, subject to the authority route above.

      Superseded g-d3a8 wording remains recoverable through
      history/s-map-002.md and git history. TREE.md carries only the
      current readable card; no duplicate legacy copy is created in
      archive.

  - id: g-7e15
    goal: |
      Gases are readable and spectacular without debug overlays: procedural visual
      identity derived from simulation parameters (meta-gas = visual language, config =
      variation; flagship anomalous gases may carry custom visuals), driven by simulation
      data — not hand-staged VFX.
    why: the concept sells on spectacular, readable chain reactions (pre-mortem #6); clips of real gameplay are the storefront's bait, and the "networked gas sim footage" clip category is verified empty.
    done_when: |
      1. In harness scenes with product visuals on, 2–3 gas types are distinguishable at a
         glance — no labels, no debug overlay — at min-spec-class performance.
      2. Blind check without humans: a vision-agent pass over a captured clip (how many
         gases, where is danger, where does it flow) matches simulation state; plus the
         owner's gamer-eye verdict.
      3. 2–3 flagship anomalous gases pass the menace test: silhouette/motion/sound read
         as threat in a 10–30s out-of-context clip (flagships only, not the full roster).
      4. The visual pipeline is a derivation of simulation state (density-mask-style),
         behind the pipeline seam locked by the g-9c41 render proof slice.
      5. Clip material flows directly from harness scenes to g-5b07/g-e6f2.
    status: active   # owner-directed 2026-06-21 (s-visual-001): elevated parked→active as a PARALLEL TRACK (NOT a 2nd bet). Engine g-9c41 stays the PRIMARY active bet (G1 — visual adds NO active_tasks; work via CALLs). Full track state → NOW.parallel_tracks.
    detail: |
      history/s-map-002.md + history/s-visual-001.md. VISUAL (GASG) TRACK stood up 2026-06-21 — the owner wants the
      gas's LOOK worked NOW, in parallel to the engine, visible in planning with its own budget («участвовало в дереве
      … со своим аппетитом … не на задворках … начать сейчас»; SECONDARY to g-9c41, with no fixed hour quota). Approach
      (research-backed, work/gas-visual-research-2026-06-21.md): a READ-ONLY visual view over the authoritative gas
      grid, decoupled by the R13/R14 seam (fake data now → swap to the real Wave-B front later, zero visualizer
      change); layered = grid → URP raymarch body and/or GraphicsBuffer-fed VFX-Graph accents → gas-as-light
      distinctiveness (INSIDE low-complexity lever); off-the-shelf (Zibra/URP-Fog-Volumes) mostly mismatches. Work =
      executor CALLs in GasCoopGame's render layer (owner-EYE gated), tracked in NOW.parallel_tracks (g-7e15), not
      active_tasks; first = c-visual-001 (P1 = grid→GPU pipe + show where/how-much, reads existing RN1). Node
      goal/done_when (criteria 1-5) UNCHANGED.

  - id: g-6d4e
    goal: |
      The player-character embodiment layer exists as a reusable DROP-IN asset: a controllable player
      prefab that any scene or level — including test scenes built by OTHER threads — can drop in and get
      a working character, driven through a STABLE adapter-API (spawn; drive the body's authoritative
      position FROM the core; trigger a procedural reaction / knockdown / get-up), with procedural animation
      and a cosmetic PuppetMaster ragdoll view. Solo-maintainable. Under the P2a0 verdict (Candidate A):
      the ragdoll is a COSMETIC local view, never authoritative; the deterministic core owns the
      authoritative body position.
    why: the game needs actual characters players inhabit, and every other thread (levels, gas scenes, test scenes) needs a droppable player without rebuilding one — P2a0 proved the network-ownership route, this turns that verdict into a reusable embodiment layer while the deterministic core catches up.
    done_when: |
      1. A reusable player prefab + a STABLE, documented adapter-API exist; a scene built by another thread
         drops the prefab in and gets a controllable player with no character-code duplication.
      2. The adapter-API works against a PLACEHOLDER authoritative-position source now and swaps to the real
         g-9c41 core position later with ZERO character-track change (the R13/R14 seam pattern, mirroring
         g-7e15's read-only view over fake→real data).
      3. Procedural reactions + a cosmetic PuppetMaster ragdoll blend onto the authoritative position
         (Candidate A — ragdoll cosmetic, never on the networked authoritative path).
      4. Owner-eye gate: the owner plays a scene with the drop-in character and accepts the control + reaction
         feel (the owner's verdict is the acceptance, as with the other presentation track g-7e15).
      5. BOUNDARY: the deterministic "grid-ballistics" physical-interaction layer is NOT built here — it is a
         g-9c41 CORE slice (input-lockstep, integer, needs delivered grid+Step+lockstep). This track only
         defines/consumes the adapter seam where that core authoritative position plugs in.
    status: active   # owner-approved 2026-07-13 («трек ... ок», «поехали»): PARALLEL TRACK like g-7e15, NOT a 2nd bet — adds NO active_tasks to the g-9c41 bet (G1); work via CALLs at owner-set cadence; g-9c41 engine stays the PRIMARY bet. First step = PLAN c-plan-characters-001.
    detail: |
      Born 2026-07-13 from the P2a0 verdict (M1-P2a0 done). Canonical verdict + grid-ballistics design =
      GasCoopGame product repo origin/main@0e9eed02 docs/results/c-exec-player-puppetmaster-p2a0-lean-spike-build-001.md
      (single source — NOT duplicated into OS state). Spike stand: branch codex/c-exec-player-puppetmaster-p2a0-002-build@a6d9271f
      (Assets/_PuppetSpike + OWNER-INSTRUCTION.md); RootMotion vendor asset local-only/gitignored@f2f860b7, disposable (no merge).
      Ordering (owner-approved): PLAN-first, but the FIRST build target is the drop-in prefab + adapter-API;
      then control / procedural reactions / cosmetic ragdoll; grid-ballistics (Phase 1 first) lands later as a
      g-9c41 core slice once the core route (NearGas L1→…→I2) delivers grid+Step+lockstep. Mandatory downstream
      network leg (captured): a 2-machine FishNet proof that authoritative grid-ballistics + local cosmetic
      ragdoll stay consistent across machines. Secondary to g-9c41 (no fixed hour quota); BUILD runs in a fresh
      GasCoopGame_dev session.

  - id: g-5b07
    goal: |
      The game has a public commercial face and first external validation: Steam page
      live, free solo-startable co-op demo public, money channels tested — the
      October-2026 window as the preferred plan, a pre-committed decision gate, the
      December check per the charter's letter (income OR credible potential), and a hard
      outer wall: EA launched and earning no later than ~Q2 2027.
    why: the standard playbook pays unknowns in 12–24 months against this direction's 6–12-month clock — the storefront must run parallel to the core; at zero audience the product-as-bait inbound path (Balatro seed) beats outbound marketing.
    done_when: |
      1. Steam page live + October Next Fest registration by 2026-08-31 (registration is a
         free reversible option until fest start; page ships only with 5 pro assets —
         human-commissioned capsule ~$300–600 budgeted, real-gameplay trailer by ~Sep 7; the page's
         first gameplay material = g-2f8c's first published artifact off the Wave-2 player-facing
         terminus, fronted by the illustrated capsule as the highest-ROI asset).
      2. Free demo: solo-startable, end-of-session wishlist prompt, submitted by Oct 5
         (press-preview cut Sep 21 target), kept live through Dec–Jan; quality gate — a
         janky demo skips the fest rather than burning the one-per-game slot. Steam
         Playtest demoted to feedback/netcode tool.
      3. Pre-committed decision gate 2026-10-05 on PRE-fest wishlists + velocity:
         >=~7–10k (or clear Popular Upcoming trajectory) → EA Oct 27–31 (payout ~Nov 30;
         attempt Scream V placement — Valve-curated); below → run the fest anyway, EA
         slips to Q1–Q2 2027; the decision is not re-litigated mid-fest.
      4. December 2026 check (charter letter): small external income OR credible potential
         (wishlist base/velocity, fest results, scout contact). Optional instant-payout
         side channels (paid itch "expedition pass" / Ko-fi) may be stood up before
         Oct 19 — optional morale/signal, not a forced valve.
      5. Hard wall: EA launched and earning for real no later than ~Q2 2027 (owner's
         one-year line; charter amendment queued as c-frame-002).
      6. Inbound path live: page discoverable from day one (scout-scanned); publisher
         pitching deferred to post-gate 2027 upside; June chores done — Steamworks
         paperwork started, owner residency/entity checked for crowdfunding eligibility.
    status: parked
    detail: history/s-map-002.md

  - id: g-e6f2
    goal: |
      An audience machine runs as a byproduct of development: AI prepares, the owner
      publishes; a steady cadence of REAL captured sim footage accumulates an own
      audience — wishlists, followers, Steam Playtest participants (the future external
      co-op testers the charter's pride bar needs).
    why: no audience and no manual SMM means marketing is either a system or nonexistent (pre-mortem #7); this machine feeds the storefront and recruits external co-op playtesters without "find four friends".
    done_when: |
      1. Cadence starts the day g-2f8c publishes its first artifact (the dropped "first clip"
         trigger RESOLVED here — c-map-003); g-e6f2 EXECUTES g-2f8c's plan (logistics delegable to
         the owner's wife/brother; authentic owner voice, AI-assisted) and holds a steady deliberate
         cadence (target set in shape; NOT a filler treadmill).
      2. Channel mix explicit and metricated: sim-footage-first short form (X primary,
         Bluesky cross-post, player subreddits, TikTok/Shorts/Reels), async micro-creator
         seeding once a distributable build exists, monthly FFF-style tech post, mailing
         list from day one; any channel failing 4–6 weeks is dropped without tree changes.
      3. AI lanes enforced: ALLOWED — AI text/captions/cut-lists/editing/scheduling on
         real captured footage (platform-native TTS captions fine); FORBIDDEN (standing
         policy, revisable only with extraordinary evidence) — AI-generated
         imagery/video/voice in public marketing.
      4. Metrics feed the Oct-5 gate: demo plays / CCU / Discord weighed alongside
         wishlists (wishlists under-measure co-op).
      5. Playtest lobbies recruit from this audience (gated on page/demo existing).
    status: parked
    detail: history/s-map-002.md

  - id: g-2f8c
    goal: |
      A working, authentic social-marketing system exists: a warm ("ламповое") community around the
      game in the solo-dev's own voice (NOT corporate), driven by a concrete go-to-market plan
      (positioning/hook, honest channel roles, publisher/crowdfunding path, timing) — run as a
      GENERATIVE PROCESS (its own local play, modeled on canon-forge) that EMITS the marketing
      artifacts the project should make (what to show, where, when) instead of the tree pre-fixing
      them. Logistics delegable to non-technical operators (the owner's wife + brother); the VOICE
      stays the owner's (AI amplifies, never replaces).
    why: closes pre-mortem #7 (audience never became a workflow) + #6 (illegible positioning), is the path not only to wishlists but to publishers/crowdfunding (charter money-gate 2026-12-11), and it OWNS the artifact decision that re-installs the dropped player-facing trigger — so it is commercially load-bearing.
    done_when: |
      1. One go-to-market plan exists: positioning/hook (matures with the canon track), a channel map
         with HONEST roles (Reddit/streamers/Steam-page = cold acquisition; Discord/X/mailing =
         capture/retention), the publisher/crowdfunding path + prerequisites (residency/entity),
         timing against 2026-08-31 / 10-05 / 12-11.
      2. It runs as its own local play (canon-forge-style) that EMITS artifact cards ("make X to show
         on channel Y by date Z") into its own work ledger, fed by the canon hook + the c-map-003
         market research; the FIRST emission is timed to the 2026-08-31 page date (teeth vs pre-mortem #2).
      3. Delegable operating split defined: logistics (scheduling, cross-post, mailing/Discord admin,
         feedback collection) → wife/brother; authentic voice + Reddit hero-posts + streamer outreach
         + approval → owner; analysis + drafts-in-the-owner's-voice → AI.
      4. "Human test": sample posts read as a real person, not detectable-AI generic (explicit anti-criterion).
      5. Cadence = a steady rhythm of deliberate posts (each genuinely needed, analyzed), gated on
         "there is something real to say" — NOT a filler treadmill; not dependent on a volunteer's weekly slot.
      6. Light metrics only (learn channel fit, not corporate analytics); markdown-first, no special
         MCP/tooling now (API metrics optional later).
    status: parked
    detail: |
      history/s-map-003.md. Born at map c-map-003 (2026-06-16) from owner discussion + 2 deep-research
      passes (market wf_c85f223d-c09; structure design-panel wf_9d9c7ccf-cd5). The contested fixed-artifact
      node (a) was REJECTED as a crutch — the artifact is this node's OUTPUT (canon hook + research), while
      the build-side legibility guarantee already lives in the Wave-2 player-facing terminus + the fixed
      2026-08-31 page date (no separate guard node). NOT a second active bet (G1 — g-9c41 stays the spine);
      worked in a parallel low-ceremony session when the owner chooses (shape via c-shape-marketing).
      Helper resource: the owner's wife + brother run logistics IF the system is clear/rule-based with an
      AI analysis layer (delegate ADMIN not the VOICE).
      SET UP 2026-06-16 (shape c-shape-marketing, owner-approved G9) as a parallel LOW-CEREMONY PROCESS — NOT a
      second active bet (G1; g-9c41 stays the spine). Local plays plays/marketing-forge.md (forge ONE card:
      Frame → Research+owner-inputs → Cross-track → Choose(owner) → Draft → Voice-gate(owner) → Freeze;
      canon-forge-style) + plays/marketing-status.md (render-only graph) + the work/marketing/ question-graph
      (seed: q-foundation / q-studio-identity / q-positioning-hook). Design: work/marketing-track-design-2026-06-16.md.
      The go-to-market plan/goals/channels/stages/numbers are DERIVED INSIDE the process (one chat = one card),
      NOT baked here. Node stays parked; advanced via marketing-forge sessions in separate chats. → history/s-shape-marketing.md

END_OF_FILE: live/indie-game-development/TREE.md
