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
      2. Replication model locked: host/server-authoritative sim + chunked-delta gas
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
      9. Scale architecture (R1): the coarse simulation tier is designed and
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
    status: active
    detail: history/s-map-002.md   # + s-review-002 (A+ re-frame); wave breakdown → NOW.md wave_plan + work/aplus-breakdown-v1.md

  - id: g-d3a8
    goal: |
      The game's design truth exists and is fixed on paper: gas grammar (meta-gas behavior
      archetypes with config gradations; reactions; mixing into new gases; special and
      anomalous gases designed as the game's ANTAGONIST ROSTER of a horror-tinged
      expedition), co-op roles, lore premise (pharma corp → descending underground city →
      the unknown below), expedition loop v2 — solo-startable, co-op-optimal (1–4 players
      via parametric scaling; no AI companions/bots).
    why: the pride bar (root criteria 3–4) is designed, not hoped for; gives the core its capability list beyond the nucleus and the storefront its fantasy language — with honest limits on what AI validation can certify.
    done_when: |
      1. Design doc exists; every base gas carries a gameplay job (decision / risk / tool /
         co-op role) — no decorative gases. (EXPANDED 2026-06-20, s-review-002, owner-approved:
         the gas TYPE catalog is effectively UNLIMITED — meta-gas archetypes × config gradations,
         «должно быть очень много типов»; the engineering constraint lives in g-9c41 A+ = a bounded,
         TUNABLE number of gases CONCURRENT per node + a hard wire cap, NOT a cap on the catalog;
         per-room overflow → a reaction QUEUE. Catalog size is free design; concurrency is the
         engineered budget.)
      2. The loop produces designed, repeatable co-op fear-spike moments; horror stays
         sim-derived (no scripted jump-scare drift); candidate systems (sanity/exposure)
         remain candidates until they pass the depth test on merit.
      3. Grammar checked against g-9c41 for simulability (nothing impossible promised).
      4. AI red-team passed under a structured protocol (fixed adversarial roles,
         anonymized authorship, simultaneous presentation, verdicts never revised under
         owner pushback) for: internal consistency, loopholes/dominant strategies,
         degenerate combos, balance hypotheses. Explicitly NOT certified here: fun,
         pacing, onboarding, "co-op feels meaningful" — re-homed to the first Steam
         Playtest as the pre-EA fun-gate.
      5. Agent self-play over executable gas configs added as a second validation lane
         once g-9c41 exists (timeboxed layer over the harness, not a separate project).
      6. Owner's explicit verdict recorded: proud of this design.
    status: parked
    detail: |
      history/s-map-002.md. CANON TRACK (wired 2026-06-15): this node is worked in PARALLEL as the
      creative/canon track. Content repo github.com/ainazemtsau/gas_coop_game_canon (clone
      C:\projects\gas_coop_game_canon). Procedures: local/canon-forge (forge ONE question — 3 options →
      owner picks → draft → craft gates → optional consistent images → freeze a canon card) and
      local/canon-status (render-only — what is actionable / parallel / blocked / cluster-ready).
      Full design + form-plan: work/canon-track-design-2026-06-15.md. Advanced via canon-forge sessions
      in separate chats; NOT a second active bet — stays parked, the g-9c41 bet is untouched (G1).

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
    status: parked
    detail: history/s-map-002.md

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
