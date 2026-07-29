RESULT s-health-repair-starter-kit-state-002 (call: c-health-repair-starter-kit-state-002)
direction: health   play: repair   node/task: g-health-starter-kit/t-1

outcome: |
  Missing shaped state for g-health-starter-kit is reconstructed in one repair packet,
  with writer validation blockers fixed.

  Fixes vs s-health-repair-starter-kit-state-001:
  - NOW.md task t-2 status is open, not ready.
  - TREE.md edit carries explicit owner_approved: true and approval_evidence for the TREE change.

  The corrected state:
  - TREE.md: g-health-starter-kit becomes active and carries appetite/kill_by.
  - NOW.md: active_bet is reconstructed with valid shape fields, t-1 is done, t-2 is open.
  - work/: work/health-starter-kit-v0.md is created with owner-calibrated A+ training and A-food nutrition.
  - LOG/history/FRICTION updates are included.

  This RESULT does not depend on a missing shape RESULT. It is the repair RESULT that reconstructs that missing state.

evidence: |
  Contradiction evidence:
  - Current NOW.md has active_bet: null and tasks: [].
  - Current TREE.md has g-health-starter-kit status: parked.
  - Current LOG.md has frame/map/research only; no applied shape/work RESULT for starter-kit.
  - Writer reported work/ does not exist and refused partial apply.
  - Writer rejected s-health-repair-starter-kit-state-001 because:
    1. t-2.status was ready, but allowed task statuses are only open | active | blocked | done.
    2. TREE.md change lacked explicit owner_approved mark.

  Reconstruction evidence from owner/current conversation:
  - Owner rejected the generic starter kit as ungrounded: "я в нём вообще не участвовал".
  - Owner specified training minimum: "минимум это три в неделю, это 100% минимум".
  - Owner specified rhythm: "утром VR, Beat Saber, днём перед обедом силовая".
  - Owner specified equipment/constraints:
    - home dumbbells;
    - no bench;
    - long resistance bands 4–5 difficulty levels;
    - short fabric leg bands;
    - no squats for now;
    - no single-leg lower-body work for now;
    - prior Achilles irritation;
    - recent break was only roughly a couple of weeks after training about 4x/week.
  - Owner approved training frame: "A+".
  - Owner specified food:
    - Greek salad only as salad;
    - rice or pasta + chicken;
    - cottage cheese / творог + strawberries;
    - omelet with meat/tuna/possibly beans;
    - simple first week;
    - equipment: multicooker, air fryer, oven, gas stove, pans; no microwave.
  - Owner approved nutrition frame: "A-food".
  - Owner/writer requested repair reissue with t-2.status: open and explicit owner_approved mark for TREE.md edit.

  Required starter artifact coverage:
  - nutrition starter: work/health-starter-kit-v0.md section 1.
  - training/activity starter: section 2.
  - safety stop/escalation gates: section 3.
  - bad-week minimum: section 4.
  - what not to track in Direction OS: section 5.
  - exact owner feedback prompt for t-2: section 6.

state_changes: |
  TREE.md:
  - owner_approved: true
  - approval_evidence: >
      Owner approved the reconstructed starter-kit content in-session through explicit choices:
      training frame "A+" and nutrition frame "A-food"; writer then requested this repair RESULT
      be reissued with an explicit owner_approved mark for the TREE.md edit.
  - Replace only the existing root.children node with id: g-health-starter-kit with the exact block below.
  - Leave all other TREE.md content unchanged.

      - id: g-health-starter-kit
        goal: >
          Стартовый комплект питания и тренировок выдан и пригоден к немедленному началу:
          owner может начать есть и тренироваться по первому рабочему варианту до завершения
          Health AI System.
        why: >
          Быстрый старт нужен, чтобы тело начало меняться сейчас, а питание и тренировки
          не ждали завершения AI/tracking-инфраструктуры.
        done_when:
          - Создан один стартовый артефакт, который можно выполнить без полной AI/tracking-системы:
            первый nutrition starter и первый training/activity starter.
          - Артефакт остаётся практическим, но не превращается в долгий "идеальный план":
            он покрывает ближайший стартовый период и даёт понятный способ сообщить, что не подошло.
          - В комплекте есть safety boundaries: боль, симптомы, перегруз, резкое падение сна/энергии
            или другие красные флаги не игнорируются.
          - В Direction OS не заносятся daily raw data: только итоговый summary, проблемы, решения
            и следующий CALL.
          - Starter kit спроектирован так, чтобы позже стать первым seed для nutrition system
            и training/activity system, а не одноразовой случайной выдачей.
        status: active
        appetite: 7 calendar days
        kill_by: >
          2026-06-19: if corrected starter kit v0 and compressed feedback path are not usable by then,
          stop and review instead of extending the bet.
        children: []

  NOW.md:
  - Replace the entire file with:

    # NOW — health

    active_bet:
      id: g-health-starter-kit
      status: active
      appetite: 7 calendar days
      kill_by: >
        2026-06-19: if corrected starter kit v0 and compressed feedback path are not usable by then,
        stop and review instead of extending the bet.
      goal: >
        Стартовый комплект питания и тренировок выдан и пригоден к немедленному началу:
        owner может начать есть и тренироваться по первому рабочему варианту до завершения
        Health AI System.
      done_when:
        - work/health-starter-kit-v0.md exists.
        - Artifact covers first nutrition starter and first training/activity starter.
        - Artifact includes safety stop/escalation gates.
        - Artifact includes bad-week minimum.
        - Artifact states what not to track in Direction OS.
        - Artifact includes exact compressed feedback prompt for t-2.
        - No daily raw health data is stored in Direction OS.
        - No long-term detailed diet, full progressive training program, Health AI System core, or app integration choice is created.
      reconstructed_by: s-health-repair-starter-kit-state-002
      reconstruction_reason: >
        Previous work/repair RESULT could not apply because NOW.md still had active_bet: null and tasks: [].
        This repair reconstructs the missing shaped state and records the owner-approved A+ / A-food starter.
      cut_list:
        - Do not create a detailed long-term diet.
        - Do not create a full progressive training program.
        - Do not build Health AI System core or data architecture.
        - Do not choose Hevy/Strava-like/wearable/VR integrations.
        - Do not store daily raw weight/food/set/activity data in Direction OS.
        - Do not make medical prescriptions.
        - Do not include squats, single-leg lower-body work, running, jumps, or calf work in v0.
      lens_sweep:
        - weight-nutrition: >
            Covered by A-food: omelet, chicken + rice/pasta + Greek salad, творог + strawberries,
            simple first-week prep and no raw food logs in Direction OS.
        - strength-body-composition: >
            Covered by A+: 3 home strength sessions using dumbbells and bands, with protein anchors
            and no full progressive program.
        - activity-conditioning: >
            Covered by morning VR/Beat Saber and bicycle as easy/moderate low-impact activity.
        - adherence-relapse: >
            Covered by bad-week minimum and exact compressed feedback prompt for t-2.
        - medical-safety: >
            Covered by Achilles-specific exclusions, pain/recovery red flags, urgent stop signs,
            and clinician-baseline gate before intensification.
        - ai-system-data-architecture: >
            Covered by explicit Direction OS exclusions; Health AI System and integrations are deferred.

    tasks:
      - id: t-1
        node: g-health-starter-kit
        status: done
        goal: >
          Produce work/health-starter-kit-v0.md: one practical starter artifact with
          initial nutrition starter, initial training/activity starter, safety boundaries,
          bad-week minimum, and compressed feedback path.
        done_when:
          - work/health-starter-kit-v0.md exists.
          - It covers nutrition starter.
          - It covers training/activity starter.
          - It covers safety stop/escalation gates.
          - It covers bad-week minimum.
          - It states what not to track in Direction OS.
          - It includes exact owner feedback prompt for t-2.
        evidence:
          - work/health-starter-kit-v0.md
          - live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md
        note: >
          Corrected A+ / A-food version supersedes earlier generic/unapplyable drafts.

      - id: t-2
        node: g-health-starter-kit
        status: open
        goal: >
          Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
          and turn that feedback into a concise next-step adjustment without storing daily raw health data
          in Direction OS.
        done_when:
          - Owner feedback is compressed into what worked, what failed, safety/Achilles flags,
            nutrition adjustment, training/activity adjustment, and next recommended action.
          - Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
        evidence: []

    recurring: []

    open_calls: []

    decisions: []

    next: |
      CALL c-health-starter-kit-t-2-guide-001
      to: session
      direction: health
      play: guide
      node: g-health-starter-kit
      task: t-2
      goal: |
        Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
        and turn that feedback into a concise next-step adjustment without storing
        daily raw health data in Direction OS.
      context: |
        Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
        work/health-starter-kit-v0.md, and
        live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md.

        Corrected starter kit:
        - training frame A+:
          - 3 strength sessions/week is the normal minimum;
          - strength is at home with dumbbells + long bands + short fabric bands;
          - no bench;
          - morning VR/Beat Saber; pre-lunch strength;
          - bicycle as low-impact cardio;
          - no squats, no single-leg lower body, no running, no jumps, no calf work;
          - prior Achilles irritation is a safety constraint;
          - optional 4th upper/back/arms pump only if safety markers are green.
        - nutrition frame A-food:
          - breakfast: omelet with meat/tuna/beans;
          - main meals: chicken + rice/pasta + Greek salad;
          - dessert/snack: творог + strawberries;
          - tools: multicooker, air fryer, oven, gas stove, pans;
          - no microwave;
          - simple first-week restoration, not interesting cooking yet.

        Owner should paste the exact feedback prompt from section "6. Exact feedback prompt for t-2".
      boundaries: |
        Do not store daily raw weight/food/set/activity data in Direction OS.
        Do not ask for raw logs.
        Do not build Health AI System core or data architecture.
        Do not choose Hevy/Strava-like/wearable/VR integrations.
        Do not make medical prescriptions.
        Do not create a long-term detailed diet or full progressive training program.
        If owner reports safety red flags or Achilles worsening, prioritize safety escalation/regression over optimization.
      done_when: |
        Owner feedback on corrected starter kit v0 is compressed into:
        - what worked;
        - what failed;
        - safety/Achilles flags;
        - nutrition adjustment needed;
        - training/activity adjustment needed;
        - whether to keep A+ / A-food, add 4th upper pump, lighten, add simple recipe variety, or redesign;
        - next recommended action.
        Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
      return: |
        RESULT with compressed feedback summary, safety assessment, suggested v1 adjustment
        or escalation, any decisions_needed, NOW task status update, and next CALL.
      budget: one guide session
      surface: chatgpt

    END_OF_FILE: live/health/NOW.md

  work/:
  - Create directory work/ if missing.
  - Add file: work/health-starter-kit-v0.md
  - Exact file content:

    # Health Starter Kit v0

    Status: owner-calibrated starter artifact, not a medical prescription.
    Direction: health
    Node: g-health-starter-kit
    Timebox: first 7 calendar days.
    Goal: start immediately without waiting for Health AI System.

    ## Owner calibration used

    Baseline from state:
    - 35-year-old male.
    - 182 cm.
    - 125 kg.
    - BMI approx 37.7.
    - No stated diagnoses, medications, injuries, or formal restrictions.

    Owner-specific training inputs:
    - This is not a beginner return from zero.
    - Recent break was roughly a couple of weeks after a period of training about 4x/week.
    - Normal minimum is 3 strength sessions per week.
    - Future possibility: 4–5 training days, but not forced in v0.
    - Preferred rhythm: VR/Beat Saber in the morning; strength before lunch.
    - Home equipment: 24 kg dumbbells, long resistance bands with 4–5 difficulty levels, short fabric bands for legs.
    - No bench; bench is broken.
    - VR and bicycle are available.
    - Because of current high bodyweight and prior Achilles irritation, v0 excludes:
      - squats;
      - single-leg lower-body exercises;
      - jumps;
      - running;
      - calf raises;
      - aggressive foot/ankle loading.

    Owner-specific nutrition inputs:
    - First week should be simple restoration, not interesting healthy cooking yet.
    - Salad preference: Greek salad only.
    - Main food base: chicken + rice or pasta.
    - Seasonal protein/sweet option: cottage cheese / творог + strawberries.
    - Breakfast preference: omelet with something meaty, tuna, or possibly beans.
    - Cooking equipment:
      - multicooker;
      - air fryer;
      - oven;
      - gas stove;
      - pans;
      - small kitchen tools.
    - No microwave.
    - Later nutrition-system work may build interesting healthy dishes using available cooking equipment.

    ## 0. Scope

    This artifact is a 7-day starter, not:
    - a long-term diet;
    - a full progressive training program;
    - medical treatment;
    - Health AI System architecture;
    - an app/integration decision.

    The purpose of v0:
    - restore rhythm quickly;
    - make nutrition simple enough to execute;
    - run 3 strength sessions safely;
    - keep morning VR/gameful activity;
    - protect Achilles and joints;
    - collect compressed feedback for t-2 without raw daily logs.

    ## 1. Nutrition starter: A-food

    ### 1.1 Nutrition strategy

    First week nutrition is simple, repetitive, and owner-compatible.

    Rules:
    1. Use the same small set of foods instead of inventing a diet.
    2. Build most meals around a protein anchor.
    3. Use Greek salad as the default vegetable/salad format.
    4. Use rice or pasta as the simple carb base.
    5. Use chicken as the main prepared protein.
    6. Use творог + strawberries as dessert/snack.
    7. Do not crash diet.
    8. Do not compensate for overeating by starving the next day.
    9. Do not store daily calories/macros/food logs in Direction OS.

    Practical control points:
    - Portion of rice/pasta matters.
    - Oil, feta, and olives in Greek salad matter.
    - Meat/cheese/oil in omelet matter.
    - Sweet additions to творог matter.
    - None of these are banned; they just need to be repeatable rather than chaotic.

    ### 1.2 Breakfast: omelet

    Default breakfast:
    - omelet;
    - plus one protein/flavour component:
      - meat/chicken/turkey/lean ham;
      - tuna;
      - beans;
    - optional simple vegetables:
      - tomato;
      - cucumber on the side;
      - onion;
      - pepper;
      - herbs.

    First-week omelet rule:
    - Keep it easy.
    - Do not turn breakfast into complex cooking.
    - If calories creep up, first reduce oil/cheese/fatty meat, not the whole meal.

    Example omelets:
    - eggs + tuna + onion/herbs;
    - eggs + chicken/meat + tomato;
    - eggs + beans + a little meat;
    - eggs + tuna + cucumber/tomato on the side.

    ### 1.3 Main meal: chicken + rice/pasta + Greek salad

    Default lunch/dinner template:
    - chicken;
    - rice or pasta;
    - Greek salad.

    Greek salad:
    - cucumber;
    - tomato;
    - red onion;
    - bell pepper if desired;
    - feta;
    - olives;
    - olive oil;
    - lemon/vinegar;
    - salt/pepper/oregano.

    Greek salad execution:
    - Do not premix a huge salad for 3 days; tomato/cucumber will leak.
    - Keep vegetables, feta/olives, and dressing separate if prepping ahead.
    - Add oil/feta/olives at serving.
    - The salad is Greek salad, not a random green salad.

    Chicken:
    - cook for 2–3 days at a time;
    - use air fryer, oven, pan, or multicooker;
    - use spices/marinade, not lots of oil;
    - keep it simple.

    Rice/pasta:
    - rice: multicooker is preferred;
    - pasta: stove, fresh or 1–2 day prep;
    - no microwave: reheat rice/pasta/chicken on pan with a splash of water, in oven, or in air fryer where appropriate.

    ### 1.4 Cottage cheese / творог + strawberries

    Use as:
    - dessert;
    - snack;
    - light evening meal if the day already had enough real food;
    - post-training protein addition if convenient.

    Template:
    - творог;
    - strawberries;
    - optional: cinnamon, low-calorie sweetener, small amount of yogurt if texture needs it.

    Avoid turning it into:
    - творог + large honey load;
    - творог + chocolate spread;
    - творог + uncontrolled nuts;
    - dessert that silently becomes the biggest calorie source of the day.

    ### 1.5 First-week simple menu

    This is a structure, not a daily log.

    Day type A:
    - Breakfast: omelet with tuna/meat/beans.
    - Main meal 1: chicken + rice + Greek salad.
    - Main meal 2: chicken + pasta + Greek salad.
    - Dessert/snack: творог + strawberries.

    Day type B:
    - Breakfast: omelet with meat + cucumber/tomato.
    - Main meal 1: chicken + pasta + Greek salad.
    - Main meal 2: chicken + rice + Greek salad.
    - Dessert/snack: творог + strawberries.

    Low-time day:
    - Omelet.
    - Chicken + rice/pasta.
    - Greek salad assembled fresh.
    - Творог + strawberries.
    - Do not solve variety on low-time days.

    ### 1.6 Meal prep with current equipment

    Cook 2–3 days of chicken:
    - air fryer: fastest, useful for pieces;
    - oven: useful for larger batch;
    - pan: useful but control oil;
    - multicooker: useful if doing simple shredded/stewed chicken.

    Cook rice:
    - multicooker;
    - make enough for 1–3 days;
    - reheat on pan with splash of water because no microwave.

    Pasta:
    - cook fresh or for 1–2 days;
    - reheat on pan with small splash of water/sauce.

    Greek salad:
    - buy enough vegetables for several days;
    - assemble daily or semi-daily;
    - keep dressing/feta/olives separate until serving.

    Творог + strawberries:
    - keep ready as a no-cook protein/sweet option.

    ### 1.7 What is intentionally delayed

    Not in v0:
    - interesting healthy recipe system;
    - weekly menu research;
    - large recipe database;
    - complex sauces;
    - calorie/macro optimization;
    - full grocery automation.

    Capture for later:
    - owner wants interesting healthy dishes using cooking equipment after first-week restoration.

    ## 2. Training/activity starter: A+

    ### 2.1 Weekly frame

    Owner-approved frame:
    - 3 main strength sessions at home using dumbbells + bands.
    - Morning VR/Beat Saber 4–6x/week if Achilles/joints/recovery are green.
    - Bicycle 1–3x/week easy/moderate as low-impact cardio.
    - Optional 4th upper/back/arms pump only if recovery markers are green.
    - No squats.
    - No single-leg lower-body exercises.
    - No jumps/running/calf raises.
    - No full progressive program yet.

    Intensity:
    - Strength: RPE 7–8 ceiling in week 1, about 1–3 reps in reserve.
    - Do not train to failure in v0.
    - VR/Beat Saber: activation/cardio, not punishment.
    - Bicycle: easy/moderate, not a hard endurance block.
    - VR boxing: optional only easy/moderate; avoid hard footwork and twisting in v0.

    Preferred daily rhythm:
    - Morning: VR/Beat Saber.
    - Before lunch: strength.

    ### 2.2 First week layout

    Day 1:
    - Morning: Beat Saber / VR 15–30 min.
    - Before lunch: Strength A.

    Day 2:
    - Morning: Beat Saber easy or bicycle 20–40 min.
    - No strength.

    Day 3:
    - Morning: Beat Saber / VR 15–30 min.
    - Before lunch: Strength B.

    Day 4:
    - Morning: bicycle 20–40 min or VR easy.
    - No strength.

    Day 5:
    - Morning: Beat Saber / VR 15–30 min.
    - Before lunch: Strength C.

    Day 6:
    - Optional VR or bicycle easy.
    - Optional upper/back/arms pump only if all safety markers are green.

    Day 7:
    - Rest, light bike, or easy walk if Achilles is quiet.
    - Fill t-2 feedback prompt.

    Safety markers that must be green before optional Day 6 pump:
    - no Achilles pain/stiffness increase;
    - no joint pain changing movement;
    - sleep not worse;
    - energy not collapsing;
    - no unusual fatigue accumulation;
    - no chest/breathing red flags.

    ### 2.3 Strength session rules

    Warm-up:
    - 5–8 min easy VR, bike, or joint prep.
    - 1–2 light ramp-up sets for first movement.
    - No jumping warm-up.
    - No calf bouncing.

    Tempo:
    - controlled lowering;
    - no ballistic reps;
    - stop if technique changes.

    Load:
    - choose dumbbell/band level that leaves 1–3 reps in reserve;
    - if dumbbells are too light, slow the tempo or add reps within the range;
    - if dumbbells are too heavy, use bands or reduce sets/reps.

    Band safety:
    - only use door/anchor setups that are genuinely secure;
    - do not improvise anchors that can snap into the face or pull you off balance;
    - inspect bands for damage before use.

    ### 2.4 Strength A — hinge / push / pull

    1. Dumbbell Romanian Deadlift
       - 3–4 sets x 8–12 reps.
       - Two legs only.
       - Hips back; no bounce.
       - Stop if Achilles, low back, or hamstring feels wrong.

    2. Dumbbell Floor Press
       - 3–4 x 8–12.
       - Replaces bench press because no bench.

    3. One-arm Dumbbell Row or Band Row
       - 3–4 x 8–12 each side.
       - Support hand on stable chair/table/thigh if needed.

    4. Band Face Pull or Band Pull-Apart
       - 2–3 x 12–20.

    5. Dead bug or plank
       - 2–3 easy sets.

    Optional:
    - band curl + band triceps extension: 2 x 10–15.

    ### 2.5 Strength B — glutes / shoulders / back

    1. Two-leg Dumbbell Glute Bridge on floor
       - 3–4 x 10–15.
       - Optional short fabric band around knees.
       - Both feet planted; no single-leg version.

    2. Seated Hip Abduction with fabric band
       - 2–3 x 15–25.
       - Seated only in v0.
       - Do not use lateral walks or monster walks yet.

    3. Dumbbell Overhead Press
       - 3 x 6–10.
       - Standing, seated on a stable chair, or seated on floor if comfortable.
       - No pain in shoulders/back.

    4. One-arm Dumbbell Row
       - 3–4 x 8–12 each side.

    5. Band Pulldown or Straight-arm Pulldown
       - 2–3 x 10–15.
       - Only if anchor is safe.
       - If no safe anchor, replace with band row or pull-apart.

    6. Core
       - 2–3 sets.

    ### 2.6 Strength C — posterior chain / upper volume

    1. Dumbbell Romanian Deadlift, lighter than Strength A
       - 3 x 8–10.

    2. Elevated Push-up or Dumbbell Floor Press
       - 3–4 x 8–12.
       - Choose the version that feels stable and pain-free.

    3. Band Row or Dumbbell Row
       - 3–4 x 10–12.

    4. Band Pull-Apart
       - 2–3 x 15–25.

    5. Dumbbell or Band Lateral Raise
       - 2–3 x 12–20.

    6. Arms
       - curls/extensions: 2–3 x 10–15.

    7. Core
       - 2 sets.

    ### 2.7 Optional Day 6 upper/back/arms pump

    Only if safety markers are green.

    No legs.
    No hinge.
    No squat.
    No calf.
    No single-leg.
    No hard VR boxing after.

    20–35 minutes:
    - band row;
    - pull-apart or face pull;
    - floor press or push-up;
    - lateral raise;
    - curls;
    - triceps;
    - core.

    This is not a fourth heavy session.
    It is an optional pump/volume session.

    ### 2.8 Activity options

    Beat Saber:
    - 15–30 min.
    - Comfortable to moderate.
    - Reduce foot movement if Achilles/ankle reacts.
    - Stop for Achilles, calf, knee, hip, back, shoulder, wrist, or neck pain.

    VR boxing/fitness:
    - Not a hard default in v0.
    - If used, keep it controlled and short.
    - Avoid aggressive pivots, bouncing, and all-out rounds.

    Bicycle:
    - 20–40 min easy/moderate.
    - Good low-impact cardio option.
    - Do not turn it into hard intervals in week 1.

    Walking:
    - allowed if Achilles is quiet;
    - not required as main cardio in v0.

    ## 3. Safety boundaries: stop, regress, escalate

    ### 3.1 Stop immediately and seek urgent help

    Stop exercise and seek urgent medical help if:
    - chest pain, pressure, tightness, or pain spreading to arm/jaw/back;
    - fainting or near-fainting;
    - severe breathlessness out of proportion to effort;
    - irregular heartbeat with dizziness, chest symptoms, or weakness;
    - sudden neurological symptoms;
    - severe acute injury;
    - sudden pop in calf/heel with sharp pain or loss of function.

    ### 3.2 Achilles-specific gates

    Stop or regress if:
    - Achilles pain appears during training;
    - morning Achilles stiffness increases after activity;
    - pain worsens with activity;
    - swelling appears;
    - pain changes gait or movement.

    Excluded in v0:
    - running;
    - jumping;
    - calf raises;
    - squats;
    - single-leg lower body;
    - lateral/monster walks;
    - hard VR boxing footwork;
    - sudden volume jumps.

    If Achilles symptoms persist or affect walking/stairs/sleep:
    - do not intensify;
    - use easy bike only if pain-free;
    - seek clinician/physio input.

    ### 3.3 Joint/movement gates

    Stop a movement if:
    - pain is sharp;
    - pain changes technique;
    - pain increases set to set;
    - joint pain appears and does not settle with a lighter variation.

    Do not push through knee, hip, back, shoulder, elbow, wrist, or Achilles pain in v0.

    ### 3.4 Recovery gates

    Hold or reduce load/volume if for 2–3 days:
    - sleep drops sharply;
    - resting fatigue is high;
    - mood/energy/work function worsens;
    - soreness changes normal movement;
    - motivation drops together with irritability;
    - morning VR feels unusually heavy.

    Adjustment:
    - keep 3 sessions if possible, but make them micro-sessions;
    - remove optional Day 6;
    - keep bike/VR easy;
    - no load increases.

    ### 3.5 Medical baseline gate

    This starter is not medical treatment.

    Because starting BMI is approx 37.7 and the goal is large, do not escalate into:
    - maximal lifting;
    - hard intervals;
    - aggressive volume;
    - extreme deficits;
    - stimulant-driven training;
    - pain-based discipline.

    Non-urgent clinician baseline to consider when practical:
    - blood pressure;
    - resting heart rate;
    - relevant labs;
    - medication/supplement review;
    - sleep apnea symptoms;
    - any chest/breathing/pain symptoms;
    - personal restrictions for intensity, nutrition, or protein.

    ## 4. Bad-week minimum

    Bad week does not mean zero.
    But safety overrides discipline.

    Normal bad-week minimum:
    - 3 micro strength sessions, 15–25 minutes each.
    - 2 easy activity exposures, 10–25 minutes each: Beat Saber easy or bike easy.
    - Nutrition:
      - omelet or other protein breakfast;
      - chicken + rice/pasta or equivalent protein meal once per day;
      - Greek salad or basic vegetables once per day;
      - творог + strawberries if it helps avoid chaotic snacking;
      - water/zero-calorie drinks as default.

    Micro strength template:
    - two-leg hinge or glute bridge: 1–2 easy sets;
    - floor press or elevated push-up: 1–2 easy sets;
    - row or band pull-apart: 1–2 easy sets;
    - core: 1 easy set.

    If sick/injured/red-flagged:
    - minimum becomes sleep, hydration, safe movement only, and feedback;
    - do not force 3 strength sessions through symptoms.

    Comeback rule:
    - next meal is normal;
    - next session is easy;
    - no heroic make-up day.

    ## 5. What Direction OS must not track

    Do not store in Direction OS:
    - daily raw weight values;
    - daily food logs;
    - food photos;
    - calories/macros by day;
    - set/rep/load logs;
    - workout-by-workout exports;
    - HR/GPS/route files;
    - VR raw session logs;
    - daily sleep scores;
    - daily mood diaries;
    - body photos;
    - raw medical measurements or lab details.

    Direction OS may store:
    - this artifact;
    - compressed weekly summary;
    - what worked/failed;
    - safety incidents as summaries;
    - decisions;
    - accepted constraints;
    - next CALLs;
    - review outcomes.

    ## 6. Exact feedback prompt for t-2

    Use this after 7 days, or earlier if the kit breaks.
    Do not include raw daily logs.

    PROMPT START

    Я использовал `work/health-starter-kit-v0.md` A+ / A-food version.

    Период:
    - дней пробовал: [число]
    - неделя была: [обычная / плохая / стресс / болезнь / поездка / другое]

    Training summary, без set logs:
    - цвет: [green / yellow / red]
    - силовые: [0 / 1 / 2 / 3 / 4 сессии]
    - A/B/C сделал? [какие]
    - optional pump делал? [нет / да]
    - утром VR/Beat Saber: [0 / 1–2 / 3–4 / 5+ раз]
    - велосипед: [0 / 1 / 2 / 3+ раз]
    - что ощущалось лучше всего: [1–3 строки]
    - что было слишком легко/тяжело/скучно: [1–3 строки]
    - хватает ли 3 силовых как минимума? [да / нет, хочу 4 / нет, тяжело]

    Achilles / safety:
    - ахилл: [тихо / лёгкое напоминание / боль / хуже утром]
    - другие боли: [нет / где / что провоцирует]
    - красные флаги: [нет / да: какие]
    - сон/энергия/настроение: [лучше / норм / хуже + 1 строка]

    Nutrition summary, без raw food log:
    - цвет: [green / yellow / red]
    - омлет: [зашёл / не зашёл / не делал]
    - курица + рис/макароны: [зашло / не зашло / не делал]
    - греческий салат: [зашёл / надоел / не делал]
    - творог + клубника: [зашло / не зашло / не делал]
    - готовка партиями: [удобно / неудобно / не пробовал]
    - что мешало: [голод / скука / готовка / цена / время / социальная еда / срывы / другое]
    - хочется ли уже перейти к интересным здоровым блюдам? [да / нет / частично]

    Weight trend, если известно, без daily values:
    - [down / flat / up / unknown]

    Главное:
    - оставить в v1: [1–3 пункта]
    - изменить в v1: [1–3 пункта]
    - главный friction: [одна строка]
    - мой выбор на следующую неделю:
      [A сохранить A+ / A-food ещё неделю /
       B добавить 4-й upper pump как обычный /
       C облегчить тренировки /
       D добавить 1–2 интересных здоровых блюда /
       E пересобрать питание /
       F пересобрать тренировки из-за боли/friction]
    - рекомендация от меня самому себе: [одна строка]

    Запусти t-2 guide: сожми это в summary/risks/next adjustment, не заноси daily raw data в Direction OS, не строй долгосрочную диету или полную программу.

    PROMPT END

    ## 7. Seed notes for later systems

    Nutrition-system seed:
    - first accepted food frame is A-food;
    - breakfast: omelet with meat/tuna/beans;
    - main meal: chicken + rice/pasta + Greek salad;
    - dessert/snack: творог + strawberries;
    - prep tools: multicooker, air fryer, oven, gas stove, pans;
    - no microwave;
    - later: owner wants interesting healthy dishes using cooking equipment;
    - feedback categories: hunger, boredom, cooking time, cost, social eating, loss-of-control risk.

    Training/activity-system seed:
    - first accepted training frame is A+;
    - owner prefers morning VR and pre-lunch strength;
    - 3 strength sessions is normal minimum;
    - 4th day can become upper/back/arms pump if recovery is green;
    - current home setup: dumbbells + long bands + fabric bands, no bench;
    - excluded for now: squats, single-leg lower body, running, jumps, calf work;
    - Achilles sensitivity is a standing safety constraint until proven quiet across several weeks.

    Integration seed:
    - no Hevy/Strava/wearable/VR integration chosen in v0;
    - future system may summarize from tools, but Direction OS receives only compressed summaries.

    END_OF_FILE: work/health-starter-kit-v0.md

  LOG.md:
  - Append exactly:
    - 2026-06-13 — repair s-health-repair-starter-kit-state-002: reconstructed missing g-health-starter-kit shaped state, created starter kit v0, marked t-1 done; next t-2 guide. → history/2026-06-13-s-health-repair-starter-kit-state-002.md

  history/:
  - Add this RESULT as:
    live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md

  os/FRICTION.md:
  - Append exactly:
    - 2026-06-13 — health starter kit: a personalized work RESULT was emitted before owner calibration and before shaped NOW state existed; future personal health work must run repair/shape first and present rationale + owner choice frame before final artifact.

captures:
  - Later nutrition-system work: owner wants interesting healthy dishes using cooking equipment after first-week simple restoration.
  - Later equipment decision: bench is broken; consider whether replacing it would materially improve home training after v0 feedback.
  - Later training-system work: if A+ week is green, evaluate adding 4th upper/back/arms pump as normal, not another lower-body day.
  - Safety watch: prior Achilles irritation means squats/single-leg/running/jumps/calf work remain excluded until explicit review changes the constraint.

decisions_needed: []

play_check:
  - 1 Name the contradiction: done — current NOW.md has active_bet null/tasks [], TREE.md has g-health-starter-kit parked, while previous RESULTs tried to mark non-existent t-1 done and then used invalid t-2.status: ready plus missing owner_approved marker.
  - 2 Reconstruct: done — map state exists; shape/work state was missing; reconstructed only from current state, owner-approved A+ / A-food inputs, and writer’s explicit rejection reports.
  - 3 Propose corrected state: done — this RESULT includes exact TREE edit with owner_approved mark, full NOW.md replacement with t-2.status: open, work artifact content, LOG/history/FRICTION updates.
  - 4 Confirm: done — owner/writer requested reissue with "t-2.status: open and an explicit owner_approved mark for the TREE.md edit."
  - 5 Friction: done — state_changes includes one os/FRICTION.md line naming the process failure.

log: |
  2026-06-13 — repair s-health-repair-starter-kit-state-002: reconstructed missing g-health-starter-kit shaped state, created starter kit v0, marked t-1 done; next t-2 guide.

next: |
  CALL c-health-starter-kit-t-2-guide-001
  to: session
  direction: health
  play: guide
  node: g-health-starter-kit
  task: t-2
  goal: |
    Guide the owner through compressed feedback on corrected work/health-starter-kit-v0.md
    and turn that feedback into a concise next-step adjustment without storing
    daily raw health data in Direction OS.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md,
    work/health-starter-kit-v0.md, and
    live/health/history/2026-06-13-s-health-repair-starter-kit-state-002.md.

    Corrected starter kit:
    - training frame A+:
      - 3 strength sessions/week is the normal minimum;
      - strength is at home with dumbbells + long bands + short fabric bands;
      - no bench;
      - morning VR/Beat Saber; pre-lunch strength;
      - bicycle as low-impact cardio;
      - no squats, no single-leg lower body, no running, no jumps, no calf work;
      - prior Achilles irritation is a safety constraint;
      - optional 4th upper/back/arms pump only if safety markers are green.
    - nutrition frame A-food:
      - breakfast: omelet with meat/tuna/beans;
      - main meals: chicken + rice/pasta + Greek salad;
      - dessert/snack: творог + strawberries;
      - tools: multicooker, air fryer, oven, gas stove, pans;
      - no microwave;
      - simple first-week restoration, not interesting cooking yet.

    Owner should paste the exact feedback prompt from section "6. Exact feedback prompt for t-2".
  boundaries: |
    Do not store daily raw weight/food/set/activity data in Direction OS.
    Do not ask for raw logs.
    Do not build Health AI System core or data architecture.
    Do not choose Hevy/Strava-like/wearable/VR integrations.
    Do not make medical prescriptions.
    Do not create a long-term detailed diet or full progressive training program.
    If owner reports safety red flags or Achilles worsening, prioritize safety escalation/regression over optimization.
  done_when: |
    Owner feedback on corrected starter kit v0 is compressed into:
    - what worked;
    - what failed;
    - safety/Achilles flags;
    - nutrition adjustment needed;
    - training/activity adjustment needed;
    - whether to keep A+ / A-food, add 4th upper pump, lighten, add simple recipe variety, or redesign;
    - next recommended action.
    Direction OS receives only summary/problems/decisions/next CALL, not daily raw logs.
  return: |
    RESULT with compressed feedback summary, safety assessment, suggested v1 adjustment
    or escalation, any decisions_needed, NOW task status update, and next CALL.
  budget: one guide session
  surface: chatgpt