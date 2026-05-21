# Recipe Catalog Index

Status: active_metadata_index

Purpose: compact metadata-only recipe index for ChatGPT Project Files.

This file must not contain full recipe bodies, ingredient lists, cooking steps, storage instructions, or full macro notes.

Full recipe JSON files live under:

```text
recipes/catalog/*.json
```

## Fields

```yaml
recipe_id:
name:
categories:
tags:
primary_protein:
equipment:
total_time:
last_used_week:
mealie_status:
mealie_slug:
mealie_id_if_known:
```

## Index

```yaml
pitanie-2026-w21-calibration-chicken-shawarma-bowl-001:
  name: "Ninja Chicken Shawarma Rice Bowl"
  categories: ["Питание / Обед", "Питание / Ужин", "Питание / Meal Prep"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "low-friction", "air-fryer", "ninja", "batch-prep", "lunch", "dinner"]
  primary_protein: "chicken"
  equipment: ["Ninja dual-basket air fryer"]
  total_time: "65 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-chicken-shawarma-bowl"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-turkey-potato-chili-002:
  name: "Instant Pro Turkey Potato Chili"
  categories: ["Питание / Обед", "Питание / Ужин", "Питание / Meal Prep"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "low-friction", "instant-pot", "multicooker", "batch-prep", "lunch", "dinner"]
  primary_protein: "turkey"
  equipment: ["Instant Pro 8 multicooker"]
  total_time: "45 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-turkey-potato-chili"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-greek-turkey-feta-meatballs-003:
  name: "Ninja Greek Turkey Feta Meatballs"
  categories: ["Питание / Обед", "Питание / Ужин", "Питание / Meal Prep"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "air-fryer", "ninja", "batch-prep", "lunch", "dinner"]
  primary_protein: "turkey"
  equipment: ["Ninja dual-basket air fryer"]
  total_time: "30 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-greek-turkey-feta-meatballs"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-sesame-tuna-steak-004:
  name: "Ninja Sesame Tuna Steak"
  categories: ["Питание / Ужин"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "air-fryer", "ninja", "fast-20-min", "dinner"]
  primary_protein: "tuna"
  equipment: ["Ninja air fryer or grill"]
  total_time: "18 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-sesame-tuna-steak"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-tuna-egg-potato-salad-005:
  name: "Tuna Egg Potato Salad"
  categories: ["Питание / Обед", "Питание / Fallback"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "low-friction", "fast-10-min", "fallback", "lunch"]
  primary_protein: "tuna"
  equipment: ["mixing bowl"]
  total_time: "10 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-tuna-egg-potato-salad"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-tuna-feta-breakfast-omelet-006:
  name: "Tuna Feta Breakfast Omelet Roll"
  categories: ["Питание / Завтрак"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "fast-20-min", "breakfast", "pan"]
  primary_protein: "tuna, eggs"
  equipment: ["pan"]
  total_time: "13 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-tuna-feta-breakfast-omelet"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-shawarma-breakfast-omelet-007:
  name: "Shawarma Breakfast Omelet"
  categories: ["Питание / Завтрак"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "fast-20-min", "breakfast", "pan"]
  primary_protein: "chicken, eggs"
  equipment: ["pan"]
  total_time: "13 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-shawarma-breakfast-omelet"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-meatball-shakshuka-008:
  name: "Meatball Shakshuka"
  categories: ["Питание / Завтрак"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "fast-20-min", "breakfast", "pan"]
  primary_protein: "turkey, eggs"
  equipment: ["pan with lid"]
  total_time: "17 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-meatball-shakshuka"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-chicken-potato-frittata-009:
  name: "Chicken Potato Frittata"
  categories: ["Питание / Завтрак", "Питание / Fallback"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "fast-20-min", "breakfast", "fallback", "pan"]
  primary_protein: "chicken, eggs"
  equipment: ["pan with lid"]
  total_time: "17 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-chicken-potato-frittata"
  mealie_id_if_known: null

pitanie-2026-w21-calibration-chicken-shawarma-flatbread-010:
  name: "Chicken Shawarma Loaded Flatbread / Bowl"
  categories: ["Питание / Ужин", "Питание / Fallback"]
  tags: ["chatgpt-pitanie", "approved-menu", "high-protein", "fast-10-min", "dinner", "fallback"]
  primary_protein: "chicken"
  equipment: ["pan or Ninja reheat"]
  total_time: "10 min"
  last_used_week: "2026-W21-calibration-2026-05-21_to_2026-05-24"
  mealie_status: "sync_requested"
  mealie_slug: "pitanie-2026-w21-chicken-shawarma-flatbread"
  mealie_id_if_known: null
```

END_OF_FILE: directions/health-and-beauty/projects/nutrition/recipes/RECIPE_CATALOG_INDEX.md
