# NOW — health

active_bet: null

tasks: []

recurring: []

open_calls: []

decisions: []

next: |
  CALL c-health-map-001
  to: session
  direction: health
  play: map
  node: g-health-root
  goal: |
    Разложить shaped root g-health-root направления health на owner-approved child outcome nodes,
    grounded in the evidence pack from c-health-map-evidence-001.
  context: |
    Read live/health/CHARTER.md, live/health/TREE.md, live/health/NOW.md, and the stored history RESULT
    for s-health-map-evidence-001.

    Current state:
    - TREE root g-health-root is shaped and has no children.
    - active_bet is null; tasks are empty.
    - Charter success criteria: 90–95 kg held 12 months; first 5–10% loss in 6 months; strength/athletic look; maintenance system; Health AI System as working layer.
    - Owner baseline: 35-year-old male, 182 cm, 125 kg, BMI ≈37.7; no stated injuries, diagnoses, medications or restrictions.
    - Owner priorities: discipline, energy, health; quality bar: weight gone without rebound, strength up, athletic look.
    - Owner failure fears: weight regain and low activity.
    - Assets: VR, bicycle, 24 kg dumbbells, gym access, cooking equipment, scales, willingness to buy HR tracker/wearable if useful, prior sport and diet experience.
    - Architecture constraint: Health AI System belongs inside health as a working layer; Direction OS remains strategic and does not store daily raw weight/food/set data.

    Evidence implications to use:
    - Competent default path is staged chronic-care, not a short hard challenge:
      baseline/safety → first 5–10% loss by 6 months → scale toward 90–95 kg → 12-month maintenance.
    - The first proof milestone from 125 kg is about 112.5–118.75 kg.
    - Effective program components: reduced-calorie eating plan, physical activity, strength work, self-monitoring, feedback/support, relapse recovery and maintenance.
    - Activity lane should include both structured exercise and NEAT: CDC minimum is 150 min/week moderate activity plus 2 muscle-strengthening days; maintenance often needs 150–300+ min/week activity and weekly weighing.
    - Strength/body-composition lane is separate from weight loss: resistance training and adequate protein protect the "athletic" criterion.
    - Nutrition lane should be repeatable meal-prep/defaults/fallback foods, not a brittle diet.
    - Relapse/maintenance should be a child outcome from the beginning.
    - Health AI System should coordinate state, summaries, check-ins, food photos, recipes, Hevy/wearable imports and research prompts, while respecting privacy, AI fallibility and non-medical-authority boundaries.
    - A clinician-led medical escalation gate should exist for baseline findings, stalled first milestone, symptoms, comorbidities, medication discussion or bariatric eligibility questions.

  boundaries: |
    Do not create tasks or active_bet.
    Do not make a detailed diet or training plan.
    Do not store daily tracking data in Direction OS.
    Do not split Health AI System into a separate direction.
    Do not make medical prescriptions; map outcomes and safety/escalation gates only.
    Follow G9: TREE child outcome edits require explicit owner approval in-session.
  done_when: |
    TREE root has owner-approved child outcome nodes grounded in the evidence pack and charter lenses,
    with each child staying outcome-level and carrying a one-line why.
    No tasks, active bet, detailed plan, or daily tracking data are created.
  return: |
    RESULT with proposed/approved TREE child outcome edits, owner approval evidence for G9,
    any captures/decisions_needed, and next CALL for shape or awaiting_decision.

  budget: one map session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
