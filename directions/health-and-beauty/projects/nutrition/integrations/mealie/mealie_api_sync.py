#!/usr/bin/env python3
"""Project-local Mealie API sync for ChatGPT Project "Pitanie".

This tool is intentionally HTTP-API based. The generic Mealie MCP server used
previously can collapse ingredients into display/note strings; this script writes
native Mealie ingredient rows with quantity, unit, food, and note fields.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback.
    tomllib = None  # type: ignore[assignment]


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BUNDLE = PROJECT_ROOT / "weeks" / "current" / "MEALIE_RECIPE_BUNDLE.json"
TOKEN_KEYS = ("MEALIE_API_TOKEN", "MEALIE_API_KEY")
BASE_URL_KEYS = ("MEALIE_BASE_URL", "MEALIE_URL")
MEAL_TYPE_ORDER = ("breakfast", "lunch", "dinner")
OLD_INVALID_TITLES = ("Shawarma Breakfast Omelet", "Шаурма-омлет")


class SyncError(RuntimeError):
    """Raised for user-actionable sync failures."""


@dataclass(frozen=True)
class MealieConfig:
    base_url: str
    token: str
    source: str


class MealieClient:
    def __init__(self, config: MealieConfig) -> None:
        self.base_url = config.base_url.rstrip("/")
        self.token = config.token

    def request(
        self,
        method: str,
        path: str,
        payload: Any | None = None,
        query: dict[str, Any] | None = None,
    ) -> Any:
        url = self.base_url + path
        if query:
            clean_query: dict[str, Any] = {}
            for key, value in query.items():
                if value is None:
                    continue
                clean_query[key] = value
            if clean_query:
                url += "?" + urllib.parse.urlencode(clean_query, doseq=True)

        data = None
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        if payload is not None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=data, method=method.upper(), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                if not body:
                    return None
                return json.loads(body.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise SyncError(f"{method.upper()} {path} failed: HTTP {exc.code}: {body}") from exc
        except urllib.error.URLError as exc:
            raise SyncError(f"{method.upper()} {path} failed: {exc.reason}") from exc

    def list_all(self, path: str, query: dict[str, Any] | None = None, per_page: int = 100) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page = 1
        while True:
            page_query = dict(query or {})
            page_query.update({"page": page, "perPage": per_page})
            result = self.request("GET", path, query=page_query)
            if isinstance(result, list):
                return result
            if not isinstance(result, dict):
                raise SyncError(f"Unexpected list response from {path}: {type(result).__name__}")
            batch = result.get("items") or []
            if not isinstance(batch, list):
                raise SyncError(f"Unexpected items response from {path}")
            items.extend(batch)
            total = result.get("total")
            total_pages = result.get("totalPages")
            if total_pages and page >= int(total_pages):
                break
            if total is not None and len(items) >= int(total):
                break
            if len(batch) < per_page:
                break
            page += 1
        return items


class EntityCache:
    def __init__(self, client: MealieClient, dry_run: bool = False) -> None:
        self.client = client
        self.dry_run = dry_run
        self.cache: dict[tuple[str, str], dict[str, Any]] = {}
        self.entity_lists: dict[str, list[dict[str, Any]]] = {}
        self.created: dict[str, list[str]] = {"foods": [], "units": [], "categories": [], "tags": []}

    def get_or_create(self, kind: str, name: str | None) -> dict[str, Any] | None:
        if not name:
            return None
        normalized = normalize_name(name)
        cache_key = (kind, normalized)
        if cache_key in self.cache:
            return self.cache[cache_key]

        path = {
            "foods": "/api/foods",
            "units": "/api/units",
            "categories": "/api/organizers/categories",
            "tags": "/api/organizers/tags",
        }[kind]
        found = self.find_exact(kind, path, normalized)
        if found is None:
            if self.dry_run:
                found = {"id": None, "name": name, "slug": None, "__dry_run": True}
            else:
                found = self.client.request("POST", path, {"name": name})
                self.entity_lists.setdefault(kind, []).append(found)
            self.created[kind].append(name)
        self.cache[cache_key] = found
        return found

    def find_exact(self, kind: str, path: str, normalized: str) -> dict[str, Any] | None:
        if kind not in self.entity_lists:
            self.entity_lists[kind] = self.client.list_all(path, per_page=500)
        for item in self.entity_lists[kind]:
            if normalize_name(item.get("name")) == normalized:
                return item
        return None


class RecipeIndex:
    def __init__(self, client: MealieClient) -> None:
        self.client = client
        self.by_recipe_id: dict[str, dict[str, Any]] = {}
        self.by_name: dict[str, dict[str, Any]] = {}
        self.by_slug: dict[str, dict[str, Any]] = {}

    def load(self) -> None:
        summaries = self.client.list_all("/api/recipes", query={"orderBy": "name", "orderDirection": "asc"}, per_page=100)
        for summary in summaries:
            slug = summary.get("slug")
            if not slug:
                continue
            try:
                detail = self.client.request("GET", f"/api/recipes/{urllib.parse.quote(str(slug))}")
            except SyncError:
                continue
            self._add(detail)

    def _add(self, recipe: dict[str, Any]) -> None:
        slug = recipe.get("slug")
        name = recipe.get("name")
        if slug:
            self.by_slug[str(slug)] = recipe
        if name:
            self.by_name[normalize_name(name)] = recipe
        recipe_id = extract_pitanie_recipe_id(recipe)
        if recipe_id:
            self.by_recipe_id[recipe_id] = recipe

    def resolve(self, bundle_recipe: dict[str, Any]) -> dict[str, Any] | None:
        recipe_id = bundle_recipe["recipe_id"]
        name = normalize_name(bundle_recipe.get("name"))
        intended_slug = bundle_recipe.get("mealie_slug")
        return self.by_recipe_id.get(recipe_id) or self.by_name.get(name) or self.by_slug.get(str(intended_slug))

    def create(self, bundle_recipe: dict[str, Any], dry_run: bool) -> dict[str, Any]:
        name = bundle_recipe["name"]
        if dry_run:
            return {"id": None, "name": name, "slug": bundle_recipe.get("mealie_slug"), "extras": {}, "__dry_run": True}
        created = self.client.request("POST", "/api/recipes", {"name": name})
        slug = created.get("slug") or created.get("recipe", {}).get("slug")
        if not slug:
            self.load()
            resolved = self.resolve(bundle_recipe)
            if resolved:
                return resolved
            raise SyncError(f"Created recipe {name!r}, but Mealie did not return a slug")
        detail = self.client.request("GET", f"/api/recipes/{urllib.parse.quote(str(slug))}")
        self._add(detail)
        return detail


class PlannerIndex:
    def __init__(self, client: MealieClient, start_date: str, end_date: str) -> None:
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.entries: list[dict[str, Any]] = []

    def load(self) -> None:
        self.entries = self.client.list_all(
            "/api/households/mealplans",
            query={"start_date": self.start_date, "end_date": self.end_date, "orderBy": "date", "orderDirection": "asc"},
            per_page=100,
        )

    def matching_slot(self, date: str, meal_type: str) -> list[dict[str, Any]]:
        return [entry for entry in self.entries if entry.get("date") == date and entry.get("entryType") == meal_type]


def main(argv: list[str] | None = None) -> int:
    ensure_utf8_stdout()
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        bundle = load_bundle(resolve_bundle_path(args.bundle))
        validate_bundle_shape(bundle)

        if args.command == "check-bundle":
            print_bundle_summary(bundle)
            return 0

        config = load_config()
        client = MealieClient(config)

        if args.command == "inspect-schema":
            inspect_schema(client)
            return 0

        if args.command == "validate":
            result = validate_mealie(client, bundle, examples=args.examples)
            print_validation_result(result)
            if result["errors"]:
                return 2
            return 0

        if args.command == "sync":
            sync_result = sync_mealie(client, bundle, dry_run=args.dry_run, sync_mealplans=args.sync_mealplans)
            print_sync_result(sync_result)
            if args.dry_run:
                return 0
            validation = validate_mealie(client, bundle, examples=args.examples)
            print_validation_result(validation)
            if validation["errors"]:
                return 2
            return 0

        raise SyncError(f"Unknown command: {args.command}")
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sync Project Pitanie recipe bundles to Mealie through the native HTTP API.")
    sub = parser.add_subparsers(dest="command", required=True)

    check_parser = sub.add_parser("check-bundle", help="Validate local bundle shape only; does not call Mealie")
    add_bundle_argument(check_parser)

    schema_parser = sub.add_parser("inspect-schema", help="Check that the target Mealie API exposes native ingredient fields")
    add_bundle_argument(schema_parser)

    validate_parser = sub.add_parser("validate", help="Read Mealie back and verify structured ingredients and meal planner entries")
    add_bundle_argument(validate_parser)
    validate_parser.add_argument("--examples", type=int, default=3, help="Ingredient examples per first three recipes")

    sync_parser = sub.add_parser("sync", help="Create/update recipes with native structured ingredients")
    add_bundle_argument(sync_parser)
    sync_parser.add_argument("--dry-run", action="store_true", help="Resolve and report intended writes without changing Mealie")
    sync_parser.add_argument("--sync-mealplans", action="store_true", help="Create/update meal planner entries from bundle")
    sync_parser.add_argument("--examples", type=int, default=3, help="Ingredient examples per first three recipes after sync")
    return parser


def add_bundle_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--bundle", default=str(DEFAULT_BUNDLE), help="Path to MEALIE_RECIPE_BUNDLE.json")


def ensure_utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def resolve_bundle_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path


def load_bundle(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SyncError(f"Bundle not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_bundle_shape(bundle: dict[str, Any]) -> None:
    recipes = bundle.get("recipes_to_upsert")
    if not isinstance(recipes, list) or not recipes:
        raise SyncError("Bundle must contain non-empty recipes_to_upsert")
    seen: set[str] = set()
    for recipe in recipes:
        recipe_id = recipe.get("recipe_id")
        if not recipe_id:
            raise SyncError("Each recipe must contain recipe_id")
        if recipe_id in seen:
            raise SyncError(f"Duplicate recipe_id in bundle: {recipe_id}")
        seen.add(recipe_id)
        structured = recipe.get("structured_ingredients_ru")
        if not isinstance(structured, list) or not structured:
            raise SyncError(f"Recipe {recipe_id} must contain structured_ingredients_ru")
        for index, row in enumerate(structured, start=1):
            if not row.get("food_ru"):
                raise SyncError(f"Recipe {recipe_id} ingredient {index} missing food_ru")
            if row.get("amount") is not None and not row.get("unit_ru"):
                raise SyncError(f"Recipe {recipe_id} ingredient {index} has amount but no unit_ru")
            if row.get("mealie_expected", {}).get("note_field_must_not_be_the_only_data") and not row.get("food_ru"):
                raise SyncError(f"Recipe {recipe_id} ingredient {index} would be note-only")


def print_bundle_summary(bundle: dict[str, Any]) -> None:
    recipes = bundle["recipes_to_upsert"]
    mealplans = bundle.get("meal_plan_entries") or []
    ingredient_rows = sum(len(recipe.get("structured_ingredients_ru") or []) for recipe in recipes)
    print("bundle_ok: true")
    print(f"week_id: {bundle.get('week_id')}")
    print(f"recipes_to_upsert: {len(recipes)}")
    print(f"structured_ingredient_rows: {ingredient_rows}")
    print(f"meal_plan_entries: {len(mealplans)}")


def load_config() -> MealieConfig:
    env_base = first_env(BASE_URL_KEYS)
    env_token = first_env(TOKEN_KEYS)
    if env_base and env_token:
        return MealieConfig(base_url=env_base, token=env_token, source="environment")

    config_values = read_codex_config_values()
    base = env_base or first_value(config_values, BASE_URL_KEYS)
    token = env_token or first_value(config_values, TOKEN_KEYS)
    if not base:
        raise SyncError("Missing MEALIE_BASE_URL or MEALIE_URL in env/config.toml")
    if not token:
        raise SyncError("Missing MEALIE_API_TOKEN or MEALIE_API_KEY in env/config.toml")
    return MealieConfig(base_url=base, token=token, source="config.toml")


def first_env(keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = os.environ.get(key)
        if value:
            return value
    return None


def read_codex_config_values() -> dict[str, str]:
    values: dict[str, str] = {}
    if tomllib is None:
        return values
    candidates = [PROJECT_ROOT / ".codex" / "config.toml"]
    candidates.extend(parent / ".codex" / "config.toml" for parent in PROJECT_ROOT.parents[:5])
    for path in candidates:
        if not path.exists():
            continue
        try:
            with path.open("rb") as handle:
                data = tomllib.load(handle)
        except Exception:
            continue
        flatten_toml(data, values)
    return values


def flatten_toml(value: Any, out: dict[str, str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(child, str):
                out.setdefault(key, child)
            else:
                flatten_toml(child, out)
    elif isinstance(value, list):
        for child in value:
            flatten_toml(child, out)


def first_value(values: dict[str, str], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        if values.get(key):
            return values[key]
    return None


def inspect_schema(client: MealieClient) -> None:
    schema = client.request("GET", "/openapi.json")
    ingredient = schema.get("components", {}).get("schemas", {}).get("RecipeIngredient-Input", {})
    props = set((ingredient.get("properties") or {}).keys())
    required = {"quantity", "unit", "food", "note", "display", "originalText"}
    missing = sorted(required - props)
    print("recipe_ingredient_input_fields:", ", ".join(sorted(props)))
    if missing:
        raise SyncError("Mealie API missing native ingredient fields: " + ", ".join(missing))
    print("native_structured_ingredients_supported: true")


def sync_mealie(client: MealieClient, bundle: dict[str, Any], dry_run: bool, sync_mealplans: bool) -> dict[str, Any]:
    entities = EntityCache(client, dry_run=dry_run)
    index = RecipeIndex(client)
    index.load()

    recipe_id_to_detail: dict[str, dict[str, Any]] = {}
    recipe_actions: list[dict[str, Any]] = []
    for recipe in bundle["recipes_to_upsert"]:
        current = index.resolve(recipe)
        action = "update"
        if current is None:
            action = "create"
            current = index.create(recipe, dry_run=dry_run)
        payload = build_recipe_payload(current, recipe, entities)
        if not dry_run:
            slug = current.get("slug")
            if not slug:
                raise SyncError(f"Cannot update recipe {recipe['recipe_id']}: missing Mealie slug")
            updated = client.request("PUT", f"/api/recipes/{urllib.parse.quote(str(slug))}", payload)
            recipe_id_to_detail[recipe["recipe_id"]] = updated
            index._add(updated)
        else:
            recipe_id_to_detail[recipe["recipe_id"]] = payload
        recipe_actions.append(
            {
                "recipe_id": recipe["recipe_id"],
                "name": recipe["name"],
                "action": action,
                "ingredient_rows": len(recipe.get("structured_ingredients_ru") or []),
                "mealie_slug": current.get("slug"),
            }
        )

    planner_actions: list[dict[str, Any]] = []
    if sync_mealplans:
        planner_actions = sync_mealplans_from_bundle(client, bundle, recipe_id_to_detail, dry_run=dry_run)

    return {
        "dry_run": dry_run,
        "recipe_actions": recipe_actions,
        "entity_creates": entities.created,
        "mealplan_actions": planner_actions,
    }


def build_recipe_payload(current: dict[str, Any], recipe: dict[str, Any], entities: EntityCache) -> dict[str, Any]:
    payload = dict(current)
    recipe_id = recipe["recipe_id"]
    payload["name"] = recipe["name"]
    payload["recipeServings"] = recipe.get("servings") or payload.get("recipeServings") or 1
    payload["recipeYieldQuantity"] = recipe.get("servings") or payload.get("recipeYieldQuantity") or 1
    payload["prepTime"] = minutes_to_iso(recipe.get("prep_time_minutes"))
    payload["cookTime"] = minutes_to_iso(recipe.get("cook_time_minutes"))
    payload["totalTime"] = minutes_to_iso(recipe.get("total_time_minutes"))
    payload["description"] = build_description(recipe)
    payload["recipeCategory"] = [entities.get_or_create("categories", name) for name in recipe.get("categories", [])]
    payload["tags"] = [entities.get_or_create("tags", name) for name in recipe.get("tags", [])]
    payload["recipeInstructions"] = [{"text": step} for step in recipe.get("instructions", [])]
    payload["recipeIngredient"] = build_ingredients(recipe, entities)
    payload["notes"] = build_notes(recipe)

    extras = dict(payload.get("extras") or {})
    extras.update(
        {
            "pitanie_recipe_id": recipe_id,
            "week_id": recipe.get("extras", {}).get("week_id"),
            "intended_mealie_slug": recipe.get("mealie_slug"),
            "sync_source": "directions/health-and-beauty/projects/nutrition/integrations/mealie/mealie_api_sync.py",
            "sync_policy": "native_structured_ingredients_ru",
        }
    )
    payload["extras"] = extras
    return payload


def build_ingredients(recipe: dict[str, Any], entities: EntityCache) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    recipe_id = recipe["recipe_id"]
    for index, row in enumerate(recipe["structured_ingredients_ru"], start=1):
        display = row.get("original_text_ru") or render_ingredient_display(row)
        food = entities.get_or_create("foods", row.get("food_ru"))
        unit = entities.get_or_create("units", row.get("unit_ru"))
        rows.append(
            {
                "quantity": row.get("amount"),
                "unit": unit,
                "food": food,
                "referencedRecipe": None,
                "note": row.get("prep_note_ru"),
                "display": display,
                "title": None,
                "originalText": display,
                "referenceId": str(uuid.uuid5(uuid.NAMESPACE_URL, f"{recipe_id}:{index}:{display}")),
            }
        )
    return rows


def build_description(recipe: dict[str, Any]) -> str:
    base = recipe.get("description") or recipe.get("purpose") or ""
    markers = [
        "",
        "Питание:",
        f"- recipe_id: {recipe['recipe_id']}",
        f"- week_id: {recipe.get('extras', {}).get('week_id')}",
        f"- intended_mealie_slug: {recipe.get('mealie_slug')}",
    ]
    return base.rstrip() + "\n" + "\n".join(markers)


def build_notes(recipe: dict[str, Any]) -> list[dict[str, str]]:
    sections = [
        ("Хранение", recipe.get("storage")),
        ("Разогрев", recipe.get("reheating")),
        ("Замены", recipe.get("substitutions")),
        ("Meal prep", recipe.get("meal_prep_notes")),
        ("Почему подходит плану", [recipe.get("why_it_fits_weekly_plan")] if recipe.get("why_it_fits_weekly_plan") else None),
        ("Оценка КБЖУ", [format_nutrition(recipe.get("nutrition_estimate_per_serving"))] if recipe.get("nutrition_estimate_per_serving") else None),
    ]
    notes: list[dict[str, str]] = []
    for title, lines in sections:
        clean_lines = [str(line) for line in (lines or []) if line]
        if clean_lines:
            notes.append({"title": title, "text": "\n".join(clean_lines)})
    return notes


def format_nutrition(nutrition: dict[str, Any]) -> str:
    return "\n".join(f"{key}: {value}" for key, value in nutrition.items())


def sync_mealplans_from_bundle(
    client: MealieClient,
    bundle: dict[str, Any],
    recipe_id_to_detail: dict[str, dict[str, Any]],
    dry_run: bool,
) -> list[dict[str, Any]]:
    entries = bundle.get("meal_plan_entries") or []
    if not entries:
        return []
    dates = sorted({entry["date"] for entry in entries})
    planner = PlannerIndex(client, dates[0], dates[-1])
    planner.load()
    actions: list[dict[str, Any]] = []

    for entry in entries:
        date = entry["date"]
        meal_type = entry["meal_type"]
        if meal_type not in MEAL_TYPE_ORDER:
            raise SyncError(f"Unsupported meal_type in bundle: {meal_type}")
        matches = planner.matching_slot(date, meal_type)
        if len(matches) > 1:
            titles = ", ".join(str(item.get("title")) for item in matches)
            raise SyncError(f"Duplicate meal planner slot {date} {meal_type}: {titles}")
        recipe_detail = recipe_id_to_detail.get(entry["recipe_id"])
        recipe_uuid = recipe_detail.get("id") if recipe_detail else None
        if not recipe_uuid and not dry_run:
            raise SyncError(f"Missing Mealie recipe id for meal plan recipe {entry['recipe_id']}")
        payload = {
            "date": date,
            "entryType": meal_type,
            "title": entry.get("title") or recipe_detail.get("name") if recipe_detail else entry.get("title"),
            "text": entry.get("notes") or "",
            "recipeId": recipe_uuid,
        }
        if matches:
            action = "update"
            target = dict(matches[0])
            target.update(payload)
            if not dry_run:
                client.request("PUT", f"/api/households/mealplans/{target['id']}", target)
        else:
            action = "create"
            if not dry_run:
                client.request("POST", "/api/households/mealplans", payload)
        actions.append({"date": date, "meal_type": meal_type, "title": payload["title"], "action": action})
    return actions


def validate_mealie(client: MealieClient, bundle: dict[str, Any], examples: int = 3) -> dict[str, Any]:
    errors: list[str] = []
    examples_out: list[dict[str, Any]] = []
    index = RecipeIndex(client)
    index.load()

    recipe_matches = 0
    ingredient_rows = 0
    note_only_rows = 0
    for recipe in bundle["recipes_to_upsert"]:
        detail = index.resolve(recipe)
        if detail is None:
            errors.append(f"Missing Mealie recipe for {recipe['recipe_id']} / {recipe['name']}")
            continue
        recipe_matches += 1
        if detail.get("name") != recipe.get("name"):
            errors.append(f"Recipe name mismatch for {recipe['recipe_id']}: {detail.get('name')} != {recipe.get('name')}")
        ingredients = detail.get("recipeIngredient") or []
        expected = recipe.get("structured_ingredients_ru") or []
        if len(ingredients) != len(expected):
            errors.append(f"Ingredient row count mismatch for {recipe['recipe_id']}: {len(ingredients)} != {len(expected)}")
        example_count_for_recipe = 0
        for index_row, readback in enumerate(ingredients, start=1):
            ingredient_rows += 1
            info = readback_ingredient_info(readback)
            if not info["food"]:
                errors.append(f"Ingredient {index_row} in {recipe['recipe_id']} missing food")
            if info["quantity"] is not None and not info["unit"]:
                errors.append(f"Ingredient {index_row} in {recipe['recipe_id']} has quantity but no unit")
            if not info["quantity"] and not info["unit"] and not info["food"] and info["note"]:
                note_only_rows += 1
            if recipe_matches <= 3 and example_count_for_recipe < examples:
                examples_out.append({"recipe": detail.get("name"), **info})
                example_count_for_recipe += 1
    if note_only_rows:
        errors.append(f"Note-only ingredient rows detected: {note_only_rows}")

    mealplan_summary = validate_mealplans(client, bundle, errors)
    return {
        "recipes_expected": len(bundle["recipes_to_upsert"]),
        "recipes_matched": recipe_matches,
        "ingredient_rows": ingredient_rows,
        "note_only_rows": note_only_rows,
        "mealplans": mealplan_summary,
        "examples": examples_out,
        "errors": errors,
    }


def validate_mealplans(client: MealieClient, bundle: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    entries = bundle.get("meal_plan_entries") or []
    if not entries:
        return {"expected": 0, "matched": 0, "old_invalid_entries": 0}
    dates = sorted({entry["date"] for entry in entries})
    planner = PlannerIndex(client, dates[0], dates[-1])
    planner.load()
    expected_slots = {(entry["date"], entry["meal_type"]) for entry in entries}
    matched = 0
    for date, meal_type in sorted(expected_slots):
        matches = planner.matching_slot(date, meal_type)
        if not matches:
            errors.append(f"Missing meal planner slot {date} {meal_type}")
        elif len(matches) > 1:
            errors.append(f"Duplicate meal planner slot {date} {meal_type}: {len(matches)} entries")
        else:
            matched += 1
    old_invalid = 0
    for entry in planner.entries:
        title = str(entry.get("title") or "")
        recipe_name = str((entry.get("recipe") or {}).get("name") or "")
        if any(old in title or old in recipe_name for old in OLD_INVALID_TITLES):
            old_invalid += 1
    if old_invalid:
        errors.append(f"Old invalid meal planner entries detected: {old_invalid}")
    return {"expected": len(entries), "matched": matched, "old_invalid_entries": old_invalid}


def print_sync_result(result: dict[str, Any]) -> None:
    print(f"dry_run: {str(result['dry_run']).lower()}")
    print(f"recipe_actions: {len(result['recipe_actions'])}")
    for action in result["recipe_actions"]:
        print(
            "recipe_action: "
            f"{action['action']} | {action['recipe_id']} | {action['name']} | "
            f"ingredients={action['ingredient_rows']} | slug={action.get('mealie_slug')}"
        )
    for kind, names in result["entity_creates"].items():
        if names:
            label = f"would_create_{kind}" if result["dry_run"] else f"created_{kind}"
            print(f"{label}: {len(names)}")
    if result["mealplan_actions"]:
        print(f"mealplan_actions: {len(result['mealplan_actions'])}")
        for action in result["mealplan_actions"]:
            print(f"mealplan_action: {action['action']} | {action['date']} | {action['meal_type']} | {action['title']}")


def print_validation_result(result: dict[str, Any]) -> None:
    print("validation:")
    print(f"  recipes_expected: {result['recipes_expected']}")
    print(f"  recipes_matched: {result['recipes_matched']}")
    print(f"  ingredient_rows: {result['ingredient_rows']}")
    print(f"  note_only_rows: {result['note_only_rows']}")
    print(f"  mealplans_expected: {result['mealplans']['expected']}")
    print(f"  mealplans_matched: {result['mealplans']['matched']}")
    print(f"  old_invalid_mealplans: {result['mealplans']['old_invalid_entries']}")
    if result["examples"]:
        print("  ingredient_examples:")
        for example in result["examples"]:
            print(
                "    - "
                f"recipe={example['recipe']} | amount={example['quantity']} | unit={example['unit']} | "
                f"food={example['food']} | note={example['note']}"
            )
    if result["errors"]:
        print("  errors:")
        for error in result["errors"]:
            print(f"    - {error}")
    else:
        print("  errors: none")


def readback_ingredient_info(row: dict[str, Any]) -> dict[str, Any]:
    unit = row.get("unit") or {}
    food = row.get("food") or {}
    return {
        "quantity": row.get("quantity"),
        "unit": unit.get("name") if isinstance(unit, dict) else None,
        "food": food.get("name") if isinstance(food, dict) else None,
        "note": row.get("note"),
        "display": row.get("display"),
    }


def extract_pitanie_recipe_id(recipe: dict[str, Any]) -> str | None:
    extras = recipe.get("extras") or {}
    if extras.get("pitanie_recipe_id"):
        return str(extras["pitanie_recipe_id"])
    description = recipe.get("description") or ""
    for line in description.splitlines():
        if "recipe_id:" in line:
            return line.split("recipe_id:", 1)[1].strip()
    return None


def render_ingredient_display(row: dict[str, Any]) -> str:
    amount = row.get("amount")
    unit = row.get("unit_ru")
    food = row.get("food_ru") or ""
    note = row.get("prep_note_ru")
    parts = []
    if amount is not None:
        parts.append(format_number(amount))
    if unit:
        parts.append(str(unit))
    parts.append(str(food))
    display = " ".join(part for part in parts if part)
    if note:
        display += f" ({note})"
    return display


def format_number(value: Any) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def minutes_to_iso(value: Any) -> str | None:
    if value is None:
        return None
    try:
        minutes = int(value)
    except (TypeError, ValueError):
        return None
    return f"PT{minutes}M"


def normalize_name(value: Any) -> str:
    return " ".join(str(value or "").strip().casefold().split())


if __name__ == "__main__":
    raise SystemExit(main())
