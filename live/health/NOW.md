# NOW — health

active_bet: null

tasks: []

recurring: []

open_calls:
  - id: c-health-map-evidence-001
    to: research
    direction: health
    play: research
    node: g-health-root
    goal: |
      Собрать evidence pack для будущей map-сессии направления health:
      какие дочерние outcome-узлы нужны под root, чтобы карта была grounded
      в доказательствах по крупному снижению веса, удержанию, силовым на дефиците,
      активности, relapse prevention и AI-assisted health system.
    context: |
      Read live/health/CHARTER.md and live/health/TREE.md after they are created.
      Owner baseline: 35 лет, мужчина, 182 см, 125 кг; цель — около 90 кг,
      без заявленных травм, диагнозов, лекарств и ограничений.
      Owner priorities: дисциплина, энергия, здоровье; качество — вес ушёл без
      отката, силовые выросли, внешний вид атлетичный.
      Owner failure fears: снова набрал вес, мало активности.
      Assets: VR, велосипед, гантели 24 кг, доступ к залу, техника для еды,
      весы, готовность купить пульсометр/трекер, опыт спорта и диет.
      Important architecture decision: Health AI System belongs inside health
      as a working layer, while Direction OS remains strategic and must not
      store daily raw weight/food/set data.
      Candidate outcomes captured by frame:
      - быстрый вводный план тренировок и питания, чтобы начать движение до полной архитектуры;
      - baseline здоровья, веса, силовых, активности и питания;
      - система снижения веса на первые 5–10% за 6 месяцев;
      - силовая система для сохранения/роста мышц и атлетичного вида;
      - система активности/кардио с использованием велосипеда, VR, ходьбы и зала;
      - repeatable meal-prep система и набор простых рецептов;
      - Health AI System architecture: state, data model, session protocol, фото еды, рецепты, апдейты, research;
      - Hevy или аналог как специализированный слой для силовых тренировок;
      - maintenance system на 12 месяцев после выхода в 90–95 кг;
      - medical safety / baseline checks / review gates.
    boundaries: |
      Не создавать TREE children и не выбирать первую ставку.
      Не делать детальный тренировочный или диетический план.
      Не записывать daily tracking data в Direction OS.
      Не отделять Health AI System в новое направление.
      Не заменять будущую map-сессию: результат research должен только подготовить evidence.
    done_when: |
      Evidence pack готов и покрывает:
      1. evidence-based sequencing for losing ~30–35 kg and maintaining it;
      2. strength training and muscle retention during caloric deficit;
      3. activity/cardio/NEAT requirements and relapse prevention;
      4. nutrition/meal-prep adherence patterns;
      5. safety checks for obese beginner/intermediate training escalation;
      6. practical AI-assisted tracking architecture patterns and tool-boundary principles;
      7. implications for child outcome nodes under g-health-root.
    return: |
      RESULT with concise evidence pack, source citations, recommended map implications,
      captures, and next = ready CALL c-health-map-001 for play: map carrying the evidence
      and candidate outcomes.
    budget: one deep-research-capable session
    surface: chatgpt

decisions: []

next: |
  CALL c-health-map-evidence-001
  to: research
  direction: health
  play: research
  node: g-health-root
  goal: |
    Собрать evidence pack для будущей map-сессии направления health.
  context: |
    live/health/CHARTER.md; live/health/TREE.md; candidate outcomes from frame
    are in open_calls.c-health-map-evidence-001.
  boundaries: |
    No TREE children, no tasks, no detailed plan, no daily tracking data in Direction OS.
  done_when: |
    Evidence pack ready for map and its RESULT chains to c-health-map-001.
  return: |
    RESULT with evidence pack and next CALL for map.
  budget: one deep-research-capable session
  surface: chatgpt

END_OF_FILE: live/health/NOW.md
