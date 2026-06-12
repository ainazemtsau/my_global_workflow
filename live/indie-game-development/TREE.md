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
    g-9c41 is the spine. Three calendar-anchored parallel tracks start DURING g-9c41 work,
    gated by the named milestone "first spectacular harness clip": gas visibility (g-7e15),
    the Steam-page slice of g-5b07, and the posting cadence of g-e6f2. Before the first
    clip, parallel tracks take <=10% of weekly hours. Fest go/no-go checkpoint ~late
    September 2026; pre-committed decision gate 2026-10-05 (see g-5b07). g-d3a8 deepens
    after the core exists (executable-config validation needs g-9c41 alive).

  children:

  - id: g-9c41
    goal: |
      A small representative networked co-op scene runs and holds: 2–4 players on a
      player-hosted listen-server, host-authoritative multi-gas simulation on grid/room
      topology with doors/vents and at least one destruction-driven topology change,
      levels fed from procedural generators (Dungeon Architect at minimum, ideally also
      Procedural Generation Grid) through a replaceable ingestion adapter — solo-maintainable.
    why: every root criterion stands on this core; the direction's riskiest assumption dies first here, the moat — first commercial co-op expedition on a fine-grained multi-gas sim with destruction-driven topology (SS13/SS14 = 2D legacy and seed audience, not refutation) — lives here, and the tech stays reusable even if the game fails.
    done_when: |
      All hold in the validation harness:
      1. Performance targets met on the min-spec profile (8GB-VRAM 60-class GPU, 16GB RAM),
         not on the dev 4090; cheap validation allowed (capped profiling / used 3060).
      2. Replication model locked: host/server-authoritative sim + chunked-delta gas
         stream; entity ghosts only for players/objects; rollback/lockstep at most one
         1–2-week timeboxed spike; GPU compute never authoritative for networked state
         (Netcode for Entities = default vendor; model locked, vendor swappable).
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
      8. Named milestone reached: first spectacular clip captured from a harness scene —
         it opens the parallel tracks (see root map_order).
    status: parked
    detail: history/s-map-002.md

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
         co-op role) — no decorative gases.
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
    detail: history/s-map-002.md

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
         human-commissioned capsule ~$300–600 budgeted, real-gameplay trailer by ~Sep 7).
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
      1. Cadence starts the day the first harness clip exists and holds for weeks without
         heroics (target set in shape; before the first clip this track is <=10% of
         weekly hours).
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

END_OF_FILE: live/indie-game-development/TREE.md
