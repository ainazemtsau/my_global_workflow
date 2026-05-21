from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin

import requests
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mealie")

REQUEST_TIMEOUT_SEC = 20
PITANIE_TAG = "chatgpt-pitanie"


@dataclass(frozen=True)
class Endpoints:
    recipe_list: str | None = None
    recipe_create: str | None = None
    recipe_detail_get: str | None = None
    recipe_update: str | None = None
    recipe_update_method: str = "PUT"
    tags_list: str | None = None
    tags_create: str | None = None
    categories_list: str | None = None
    categories_create: str | None = None


class MealieConfigError(RuntimeError):
    pass


def _base_url(required: bool = True) -> str | None:
    value = os.environ.get("MEALIE_BASE_URL", "").strip().rstrip("/")
    if not value and required:
        raise MealieConfigError("MEALIE_BASE_URL is not set.")
    return value or None


def _api_token(required: bool = True) -> str | None:
    value = os.environ.get("MEALIE_API_TOKEN", "").strip()
    if not value and required:
        raise MealieConfigError("MEALIE_API_TOKEN is not set.")
    return value or None


def _headers(required_token: bool = True) -> dict[str, str]:
    headers = {"Accept": "application/json"}
    token = _api_token(required=required_token)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _url(path: str) -> str:
    base = _base_url(required=True)
    if path.startswith("http://") or path.startswith("https://"):
        return path
    assert base is not None
    return urljoin(base + "/", path.lstrip("/"))


def _request(
    method: str,
    path: str,
    *,
    required_token: bool = True,
    **kwargs: Any,
) -> requests.Response:
    headers = _headers(required_token=required_token)
    extra_headers = kwargs.pop("headers", None)
    if extra_headers:
        headers.update(extra_headers)
    return requests.request(
        method,
        _url(path),
        headers=headers,
        timeout=REQUEST_TIMEOUT_SEC,
        **kwargs,
    )


def _json_response(response: requests.Response) -> Any:
    if not response.content:
        return None
    try:
        return response.json()
    except ValueError:
        return {"raw_text": response.text[:500]}


def _status_failure(response: requests.Response, endpoint: str) -> dict[str, Any]:
    return {
        "endpoint": endpoint,
        "status_code": response.status_code,
        "body": _json_response(response),
    }


def _load_openapi() -> tuple[dict[str, Any] | None, list[str]]:
    warnings: list[str] = []
    try:
        response = _request("GET", "/openapi.json", required_token=False)
    except Exception as exc:  # noqa: BLE001 - returned as structured MCP result
        return None, [f"Could not fetch /openapi.json: {exc}"]

    if response.status_code == 200:
        data = _json_response(response)
        if isinstance(data, dict):
            return data, warnings
        return None, ["Mealie /openapi.json did not return a JSON object."]

    warnings.append(f"/openapi.json returned HTTP {response.status_code}.")
    return None, warnings


def _paths_for_method(openapi: dict[str, Any] | None, method: str) -> list[str]:
    if not openapi:
        return []
    paths = openapi.get("paths")
    if not isinstance(paths, dict):
        return []
    method = method.lower()
    return [
        path
        for path, operations in paths.items()
        if isinstance(operations, dict) and method in operations
    ]


def _find_path(
    openapi: dict[str, Any] | None,
    method: str,
    *,
    includes: tuple[str, ...],
    excludes: tuple[str, ...] = (),
    prefer_exact: tuple[str, ...] = (),
    with_param: bool | None = None,
) -> str | None:
    candidates = []
    for path in _paths_for_method(openapi, method):
        lower = path.lower()
        if any(term not in lower for term in includes):
            continue
        if any(term in lower for term in excludes):
            continue
        has_param = "{" in path and "}" in path
        if with_param is not None and has_param != with_param:
            continue
        score = 0
        if path in prefer_exact:
            score += 100
        if lower.rstrip("/") in {item.lower().rstrip("/") for item in prefer_exact}:
            score += 80
        score -= lower.count("/")
        candidates.append((score, path))
    candidates.sort(reverse=True)
    return candidates[0][1] if candidates else None


def _resolve_endpoints(openapi: dict[str, Any] | None) -> Endpoints:
    if not openapi:
        return Endpoints(
            recipe_list="/api/recipes",
            recipe_create="/api/recipes",
            recipe_detail_get="/api/recipes/{slug}",
            recipe_update="/api/recipes/{slug}",
            tags_list="/api/organizers/tags",
            tags_create="/api/organizers/tags",
            categories_list="/api/organizers/categories",
            categories_create="/api/organizers/categories",
        )

    recipe_list = _find_path(
        openapi,
        "get",
        includes=("/api/recipes",),
        excludes=("/create", "/parse", "/image", "/assets", "/timeline", "/comments"),
        prefer_exact=("/api/recipes",),
        with_param=False,
    )
    recipe_create = _find_path(
        openapi,
        "post",
        includes=("/api/recipes",),
        excludes=("/url", "/zip", "/image", "/assets", "/comments", "/timeline"),
        prefer_exact=("/api/recipes", "/api/recipes/create"),
        with_param=False,
    )
    recipe_detail_get = _find_path(
        openapi,
        "get",
        includes=("/api/recipes",),
        excludes=("/assets", "/comments", "/timeline"),
        prefer_exact=("/api/recipes/{slug}",),
        with_param=True,
    )
    put_update = _find_path(
        openapi,
        "put",
        includes=("/api/recipes",),
        excludes=("/assets", "/comments", "/timeline"),
        prefer_exact=("/api/recipes/{slug}",),
        with_param=True,
    )
    patch_update = _find_path(
        openapi,
        "patch",
        includes=("/api/recipes",),
        excludes=("/assets", "/comments", "/timeline"),
        prefer_exact=("/api/recipes/{slug}",),
        with_param=True,
    )
    recipe_update = put_update or patch_update
    recipe_update_method = "PUT" if put_update else "PATCH"
    tags_list = _find_path(
        openapi,
        "get",
        includes=("/api/organizers/tags",),
        prefer_exact=("/api/organizers/tags",),
        with_param=False,
    )
    tags_create = _find_path(
        openapi,
        "post",
        includes=("/api/organizers/tags",),
        prefer_exact=("/api/organizers/tags",),
        with_param=False,
    )
    categories_list = _find_path(
        openapi,
        "get",
        includes=("/api/organizers/categories",),
        prefer_exact=("/api/organizers/categories",),
        with_param=False,
    )
    categories_create = _find_path(
        openapi,
        "post",
        includes=("/api/organizers/categories",),
        prefer_exact=("/api/organizers/categories",),
        with_param=False,
    )
    return Endpoints(
        recipe_list=recipe_list,
        recipe_create=recipe_create,
        recipe_detail_get=recipe_detail_get,
        recipe_update=recipe_update,
        recipe_update_method=recipe_update_method,
        tags_list=tags_list,
        tags_create=tags_create,
        categories_list=categories_list,
        categories_create=categories_create,
    )


def _missing_required_endpoints(endpoints: Endpoints) -> list[str]:
    missing = []
    if not endpoints.recipe_list:
        missing.append("GET recipe list endpoint, expected /api/recipes or equivalent")
    if not endpoints.recipe_create:
        missing.append("POST recipe create endpoint, expected /api/recipes or /api/recipes/create or equivalent")
    if not endpoints.recipe_update:
        missing.append("PUT/PATCH recipe update endpoint, expected /api/recipes/{slug} or equivalent")
    return missing


def _as_bundle(bundle: Any) -> dict[str, Any]:
    if isinstance(bundle, str):
        return json.loads(bundle)
    if isinstance(bundle, dict):
        return bundle
    raise TypeError("Bundle must be a JSON object or a JSON string.")


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _recipe_id(recipe: dict[str, Any]) -> str | None:
    extras = recipe.get("extras")
    if isinstance(extras, dict) and extras.get("pitanie_recipe_id"):
        return str(extras["pitanie_recipe_id"])
    if recipe.get("recipe_id"):
        return str(recipe["recipe_id"])
    return None


def _week_tag(week_id: Any) -> str | None:
    if not week_id:
        return None
    clean = re.sub(r"[^A-Za-z0-9_-]+", "-", str(week_id)).strip("-").lower()
    return f"week-{clean}" if clean else None


def _tag_names(value: Any) -> set[str]:
    names: set[str] = set()
    for item in _as_list(value):
        if isinstance(item, str):
            names.add(item)
        elif isinstance(item, dict):
            name = item.get("name") or item.get("slug") or item.get("label")
            if name:
                names.add(str(name))
    return names


def _taxonomy_name(item: Any) -> str | None:
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        for key in ("name", "label", "slug"):
            if item.get(key):
                return str(item[key])
    return None


def _items_from_response(data: Any) -> list[Any]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("items", "results", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return value
    return []


def _slug_or_id(recipe: dict[str, Any]) -> str | None:
    for key in ("slug", "id", "recipeSlug", "recipe_slug"):
        value = recipe.get(key)
        if value:
            return str(value)
    return None


def _fill_path(path: str, recipe: dict[str, Any]) -> str:
    value = _slug_or_id(recipe)
    if not value:
        raise ValueError("Existing recipe is missing slug/id needed for detail endpoint.")
    return re.sub(r"\{[^}]+\}", value, path)


def _recipe_url(recipe: dict[str, Any]) -> str | None:
    for key in ("url", "recipeUrl", "recipe_url"):
        value = recipe.get(key)
        if value:
            return str(value)
    slug = _slug_or_id(recipe)
    base = _base_url(required=False)
    if slug and base:
        return f"{base}/g/home/r/{slug}"
    return None


def _validate_bundle_payload(bundle: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if bundle.get("schema") != "mealie_recipe_bundle.v1":
        errors.append("schema must be mealie_recipe_bundle.v1")

    recipes = bundle.get("recipes")
    if not isinstance(recipes, list):
        errors.append("recipes must be a list")
        recipes = []

    for index, recipe in enumerate(recipes):
        prefix = f"recipes[{index}]"
        if not isinstance(recipe, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if not recipe.get("name"):
            errors.append(f"{prefix}.name is required")
        extras = recipe.get("extras")
        if not isinstance(extras, dict) or not extras.get("pitanie_recipe_id"):
            errors.append(f"{prefix}.extras.pitanie_recipe_id is required")
        if not recipe.get("categories"):
            errors.append(f"{prefix}.categories is required")
        if not recipe.get("tags"):
            errors.append(f"{prefix}.tags is required")
        if not recipe.get("servings"):
            errors.append(f"{prefix}.servings is required")
        if not (recipe.get("prep_time") or recipe.get("prepTime")):
            errors.append(f"{prefix}.prep_time is required")
        if not (recipe.get("cook_time") or recipe.get("cookTime")):
            errors.append(f"{prefix}.cook_time is required")
        if not (recipe.get("total_time") or recipe.get("totalTime")):
            errors.append(f"{prefix}.total_time is required")
        if not recipe.get("equipment"):
            errors.append(f"{prefix}.equipment is required")
        if not recipe.get("ingredients"):
            errors.append(f"{prefix}.ingredients is required")
        if not (recipe.get("steps") or recipe.get("instructions")):
            errors.append(f"{prefix}.steps is required")
        for optional_key in ("storage", "reheating", "substitutions", "meal_prep_notes", "why_it_fits"):
            if not recipe.get(optional_key):
                warnings.append(f"{prefix}.{optional_key} is recommended by Project Питание recipe quality bar")

    return {
        "valid": not errors,
        "recipe_count": len(recipes),
        "errors": errors,
        "warnings": warnings,
    }


def _recipe_payload(recipe: dict[str, Any], week_id: Any) -> dict[str, Any]:
    extras = dict(recipe.get("extras") or {})
    extras["pitanie_recipe_id"] = _recipe_id(recipe)
    if week_id:
        extras["pitanie_week_id"] = week_id

    tags = list(dict.fromkeys([str(item) for item in _as_list(recipe.get("tags"))]))
    if PITANIE_TAG not in tags:
        tags.append(PITANIE_TAG)
    week_tag = _week_tag(week_id)
    if week_tag and week_tag not in tags:
        tags.append(week_tag)

    categories = [str(item) for item in _as_list(recipe.get("categories"))]
    ingredients = _as_list(recipe.get("ingredients"))
    steps = _as_list(recipe.get("steps") or recipe.get("instructions"))

    description_parts = []
    for key in ("purpose", "slot", "storage", "reheating", "substitutions", "meal_prep_notes", "why_it_fits"):
        if recipe.get(key):
            description_parts.append(f"{key}: {recipe[key]}")
    if recipe.get("estimated_macros"):
        description_parts.append(f"estimated_macros: {recipe['estimated_macros']}")

    payload = {
        "name": recipe["name"],
        "description": "\n\n".join(description_parts),
        "recipeYield": str(recipe.get("servings", "")),
        "prepTime": str(recipe.get("prep_time") or recipe.get("prepTime") or ""),
        "cookTime": str(recipe.get("cook_time") or recipe.get("cookTime") or ""),
        "totalTime": str(recipe.get("total_time") or recipe.get("totalTime") or ""),
        "recipeIngredient": ingredients,
        "recipeInstructions": steps,
        "recipeCategory": categories,
        "tags": tags,
        "extras": extras,
    }

    notes = recipe.get("notes")
    if notes:
        payload["notes"] = notes
    return payload


def _taxonomy(endpoint: str | None) -> tuple[list[Any], dict[str, Any] | None]:
    if not endpoint:
        return [], {"endpoint": None, "status_code": None, "body": "Endpoint not resolved."}
    response = _request("GET", endpoint)
    if response.status_code == 200:
        return _items_from_response(_json_response(response)), None
    return [], _status_failure(response, endpoint)


def _ensure_taxonomy(
    names: list[str],
    *,
    list_endpoint: str | None,
    create_endpoint: str | None,
    label: str,
) -> list[str]:
    warnings: list[str] = []
    if not names:
        return warnings
    items, failure = _taxonomy(list_endpoint)
    if failure:
        warnings.append(f"Could not list Mealie {label}: {failure}")
        return warnings

    existing = {_taxonomy_name(item) for item in items}
    existing.discard(None)
    for name in names:
        if name in existing:
            continue
        if not create_endpoint:
            warnings.append(f"Could not create missing Mealie {label} '{name}': create endpoint not resolved.")
            continue
        response = _request("POST", create_endpoint, json={"name": name})
        if response.status_code in (200, 201, 204, 409):
            existing.add(name)
        else:
            warnings.append(
                f"Could not create Mealie {label} '{name}': "
                f"{_status_failure(response, create_endpoint)}"
            )
    return warnings


def _load_existing_recipes(endpoints: Endpoints) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    if not endpoints.recipe_list:
        return [], ["Recipe list endpoint is not resolved."]

    response = _request("GET", endpoints.recipe_list)
    if response.status_code != 200:
        return [], [f"Could not list recipes: {_status_failure(response, endpoints.recipe_list)}"]

    recipes = [item for item in _items_from_response(_json_response(response)) if isinstance(item, dict)]
    detailed: list[dict[str, Any]] = []
    for item in recipes:
        if not endpoints.recipe_detail_get or not _slug_or_id(item):
            detailed.append(item)
            continue
        try:
            detail_path = _fill_path(endpoints.recipe_detail_get, item)
            detail_response = _request("GET", detail_path)
        except Exception as exc:  # noqa: BLE001 - keep sync running with summary fallback
            warnings.append(f"Could not fetch recipe detail for {item.get('name')}: {exc}")
            detailed.append(item)
            continue
        if detail_response.status_code == 200:
            detail = _json_response(detail_response)
            detailed.append(detail if isinstance(detail, dict) else item)
        else:
            warnings.append(f"Could not fetch recipe detail for {item.get('name')}: HTTP {detail_response.status_code}")
            detailed.append(item)
    return detailed, warnings


def _existing_recipe_id(recipe: dict[str, Any]) -> str | None:
    extras = recipe.get("extras")
    if isinstance(extras, dict):
        value = extras.get("pitanie_recipe_id")
        if value:
            return str(value)
    return None


def _find_existing_recipe(
    recipe: dict[str, Any],
    existing: list[dict[str, Any]],
    week_id: Any,
) -> tuple[dict[str, Any] | None, str | None, list[str]]:
    warnings: list[str] = []
    wanted_id = _recipe_id(recipe)
    if wanted_id:
        matches = [item for item in existing if _existing_recipe_id(item) == wanted_id]
        if len(matches) == 1:
            return matches[0], "extras.pitanie_recipe_id", warnings
        if len(matches) > 1:
            return None, "DUPLICATE_CONFLICT", [f"Multiple Mealie recipes have extras.pitanie_recipe_id={wanted_id}."]

    week_tag = _week_tag(week_id)
    wanted_name = str(recipe.get("name", ""))
    fallback_matches = []
    for item in existing:
        names_match = str(item.get("name", "")) == wanted_name
        tags = _tag_names(item.get("tags") or item.get("recipeTags") or item.get("recipe_tags"))
        if names_match and PITANIE_TAG in tags and (not week_tag or week_tag in tags):
            fallback_matches.append(item)

    if len(fallback_matches) == 1:
        return fallback_matches[0], "name+chatgpt-pitanie+week tag", warnings
    if len(fallback_matches) > 1:
        return None, "DUPLICATE_CONFLICT", [
            f"Multiple Mealie recipes matched fallback identity for name={wanted_name!r}, week_tag={week_tag!r}."
        ]
    return None, None, warnings


def _created_recipe_from_response(data: Any, fallback_name: str) -> dict[str, Any]:
    if isinstance(data, dict):
        return data
    if isinstance(data, str):
        return {"slug": data, "name": fallback_name}
    return {"name": fallback_name}


def _send_recipe_create(
    endpoints: Endpoints,
    payload: dict[str, Any],
) -> tuple[bool, dict[str, Any] | None, list[str], Any]:
    warnings: list[str] = []
    assert endpoints.recipe_create is not None
    response = _request("POST", endpoints.recipe_create, json=payload)
    if response.status_code in (200, 201):
        data = _json_response(response)
        return True, _created_recipe_from_response(data, payload["name"]), warnings, data

    if response.status_code in (400, 422) and endpoints.recipe_create.rstrip("/").endswith("/create"):
        minimal_response = _request("POST", endpoints.recipe_create, json={"name": payload["name"]})
        if minimal_response.status_code in (200, 201):
            data = _json_response(minimal_response)
            created = _created_recipe_from_response(data, payload["name"])
            update_result, update_failure = _send_recipe_update(endpoints, created, payload)
            if update_result:
                return True, created, warnings, data
            warnings.append(f"Created recipe shell but could not update full payload: {update_failure}")
            return True, created, warnings, data

    if response.status_code in (400, 422) and payload.get("extras"):
        fallback_payload = dict(payload)
        fallback_payload.pop("extras", None)
        fallback_response = _request("POST", endpoints.recipe_create, json=fallback_payload)
        if fallback_response.status_code in (200, 201):
            warnings.append("Mealie rejected extras on create; recipe was created without extras metadata.")
            data = _json_response(fallback_response)
            return True, _created_recipe_from_response(data, payload["name"]), warnings, data

    return False, None, warnings, _status_failure(response, endpoints.recipe_create)


def _send_recipe_update(
    endpoints: Endpoints,
    existing_recipe: dict[str, Any],
    payload: dict[str, Any],
) -> tuple[bool, Any]:
    assert endpoints.recipe_update is not None
    try:
        update_path = _fill_path(endpoints.recipe_update, existing_recipe)
    except Exception as exc:  # noqa: BLE001 - structured MCP failure
        return False, str(exc)

    method = endpoints.recipe_update_method or "PUT"
    response = _request(method, update_path, json=payload)
    if response.status_code in (200, 204):
        return True, _json_response(response)

    fallback_method = "PATCH" if method == "PUT" else "PUT"
    if response.status_code in (404, 405, 501):
        fallback_response = _request(fallback_method, update_path, json=payload)
        if fallback_response.status_code in (200, 204):
            return True, _json_response(fallback_response)
        response = fallback_response
        method = fallback_method

    if response.status_code in (400, 422) and payload.get("extras"):
        fallback_payload = dict(payload)
        fallback_payload.pop("extras", None)
        fallback_response = _request(method, update_path, json=fallback_payload)
        if fallback_response.status_code in (200, 204):
            return True, {
                "warning": "Mealie rejected extras on update; recipe was updated without extras metadata.",
                "response": _json_response(fallback_response),
            }

    return False, _status_failure(response, update_path)


def _empty_summary(status: str = "DONE") -> dict[str, Any]:
    return {
        "status": status,
        "created": [],
        "updated": [],
        "skipped": [],
        "failed": [],
        "warnings": [],
        "mealie_urls": [],
    }


@mcp.tool()
def mealie_healthcheck() -> dict[str, Any]:
    """Check Mealie reachability without exposing the API token."""
    result = {
        "status": "UNKNOWN",
        "base_url_set": bool(_base_url(required=False)),
        "api_token_set": bool(_api_token(required=False)),
        "docs": None,
        "openapi": None,
        "warnings": [],
    }

    if not result["base_url_set"] or not result["api_token_set"]:
        result["status"] = "NEEDS_ENV"
        result["warnings"].append("MEALIE_BASE_URL and MEALIE_API_TOKEN must both be set outside the repo.")
        return result

    for path in ("/docs", "/openapi.json"):
        try:
            response = _request("GET", path, required_token=False)
            key = "docs" if path == "/docs" else "openapi"
            result[key] = {"status_code": response.status_code, "reachable": response.status_code < 500}
        except Exception as exc:  # noqa: BLE001 - structured health result
            result["warnings"].append(f"{path} check failed: {exc}")

    openapi, openapi_warnings = _load_openapi()
    result["warnings"].extend(openapi_warnings)
    endpoints = _resolve_endpoints(openapi)
    result["resolved_endpoints"] = endpoints.__dict__
    missing = _missing_required_endpoints(endpoints)
    if missing:
        result["status"] = "STUCK_API_SCHEMA"
        result["warnings"].extend(missing)
    elif result["docs"] or result["openapi"]:
        result["status"] = "DONE"
    else:
        result["status"] = "UNREACHABLE"
    return result


@mcp.tool()
def mealie_get_taxonomy() -> dict[str, Any]:
    """Return Mealie categories and tags if the local API exposes organizer endpoints."""
    summary = _empty_summary()
    try:
        openapi, warnings = _load_openapi()
        summary["warnings"].extend(warnings)
        endpoints = _resolve_endpoints(openapi)
        tags, tags_failure = _taxonomy(endpoints.tags_list)
        categories, categories_failure = _taxonomy(endpoints.categories_list)
    except MealieConfigError as exc:
        summary["status"] = "NEEDS_ENV"
        summary["failed"].append(str(exc))
        return summary
    except Exception as exc:  # noqa: BLE001 - MCP tool should return structured failure
        summary["status"] = "STUCK"
        summary["failed"].append(str(exc))
        return summary

    if tags_failure:
        summary["warnings"].append(f"Tags unavailable: {tags_failure}")
    if categories_failure:
        summary["warnings"].append(f"Categories unavailable: {categories_failure}")

    summary["tags"] = sorted(name for name in (_taxonomy_name(item) for item in tags) if name)
    summary["categories"] = sorted(name for name in (_taxonomy_name(item) for item in categories) if name)
    return summary


@mcp.tool()
def mealie_validate_recipe_bundle(bundle: Any) -> dict[str, Any]:
    """Validate a Project Питание Mealie recipe bundle without contacting Mealie."""
    try:
        parsed = _as_bundle(bundle)
        validation = _validate_bundle_payload(parsed)
    except Exception as exc:  # noqa: BLE001 - structured MCP result
        return {
            "status": "STUCK",
            "valid": False,
            "recipe_count": 0,
            "errors": [str(exc)],
            "warnings": [],
        }
    return {"status": "DONE" if validation["valid"] else "STUCK", **validation}


@mcp.tool()
def mealie_dry_run_recipe_bundle(bundle: Any) -> dict[str, Any]:
    """Classify bundle recipes as create/update without writing to Mealie."""
    try:
        parsed = _as_bundle(bundle)
        validation = _validate_bundle_payload(parsed)
    except Exception as exc:  # noqa: BLE001 - structured MCP result
        return {"status": "STUCK", "created": [], "updated": [], "skipped": [], "failed": [str(exc)], "warnings": []}

    summary = _empty_summary(status="DONE" if validation["valid"] else "STUCK")
    summary["warnings"].extend(validation["warnings"])
    if not validation["valid"]:
        summary["failed"].extend(validation["errors"])
        return summary

    if not _base_url(required=False) or not _api_token(required=False):
        summary["warnings"].append("MEALIE_BASE_URL or MEALIE_API_TOKEN is missing; dry run is validation-only.")
        summary["skipped"] = [_recipe_id(recipe) or recipe.get("name") for recipe in parsed.get("recipes", [])]
        return summary

    openapi, warnings = _load_openapi()
    summary["warnings"].extend(warnings)
    endpoints = _resolve_endpoints(openapi)
    missing = _missing_required_endpoints(endpoints)
    if missing:
        summary["status"] = "STUCK_API_SCHEMA"
        summary["failed"].extend(missing)
        return summary

    existing, existing_warnings = _load_existing_recipes(endpoints)
    summary["warnings"].extend(existing_warnings)
    week_id = parsed.get("week_id")
    for recipe in parsed.get("recipes", []):
        match, reason, match_warnings = _find_existing_recipe(recipe, existing, week_id)
        summary["warnings"].extend(match_warnings)
        identity = _recipe_id(recipe) or recipe.get("name")
        if reason == "DUPLICATE_CONFLICT":
            summary["status"] = "STUCK"
            summary["failed"].append({"recipe": identity, "reason": match_warnings})
        elif match:
            summary["updated"].append({"recipe": identity, "match": reason})
        else:
            summary["created"].append({"recipe": identity})
    return summary


@mcp.tool()
def mealie_upsert_recipe_bundle(bundle: Any) -> dict[str, Any]:
    """Create or update approved Project Питание recipes in Mealie."""
    try:
        parsed = _as_bundle(bundle)
        validation = _validate_bundle_payload(parsed)
    except Exception as exc:  # noqa: BLE001 - structured MCP result
        return {"status": "STUCK", "created": [], "updated": [], "skipped": [], "failed": [str(exc)], "warnings": []}

    summary = _empty_summary(status="DONE" if validation["valid"] else "STUCK")
    summary["warnings"].extend(validation["warnings"])
    if not validation["valid"]:
        summary["failed"].extend(validation["errors"])
        return summary

    try:
        _base_url(required=True)
        _api_token(required=True)
        openapi, warnings = _load_openapi()
        summary["warnings"].extend(warnings)
        endpoints = _resolve_endpoints(openapi)
    except MealieConfigError as exc:
        summary["status"] = "NEEDS_ENV"
        summary["failed"].append(str(exc))
        return summary
    except Exception as exc:  # noqa: BLE001
        summary["status"] = "UNREACHABLE"
        summary["failed"].append(str(exc))
        return summary

    missing = _missing_required_endpoints(endpoints)
    if missing:
        summary["status"] = "STUCK_API_SCHEMA"
        summary["failed"].extend(missing)
        summary["resolved_endpoints"] = endpoints.__dict__
        return summary

    recipes = [recipe for recipe in parsed.get("recipes", []) if isinstance(recipe, dict)]
    week_id = parsed.get("week_id")
    all_tags = sorted(
        {
            tag
            for recipe in recipes
            for tag in [*map(str, _as_list(recipe.get("tags"))), PITANIE_TAG]
            if tag
        }
    )
    week_tag = _week_tag(week_id)
    if week_tag:
        all_tags.append(week_tag)
    all_categories = sorted(
        {
            category
            for recipe in recipes
            for category in map(str, _as_list(recipe.get("categories")))
            if category
        }
    )
    summary["warnings"].extend(
        _ensure_taxonomy(
            all_tags,
            list_endpoint=endpoints.tags_list,
            create_endpoint=endpoints.tags_create,
            label="tag",
        )
    )
    summary["warnings"].extend(
        _ensure_taxonomy(
            all_categories,
            list_endpoint=endpoints.categories_list,
            create_endpoint=endpoints.categories_create,
            label="category",
        )
    )

    existing, existing_warnings = _load_existing_recipes(endpoints)
    summary["warnings"].extend(existing_warnings)

    for recipe in recipes:
        identity = _recipe_id(recipe) or recipe.get("name")
        match, reason, match_warnings = _find_existing_recipe(recipe, existing, week_id)
        summary["warnings"].extend(match_warnings)
        if reason == "DUPLICATE_CONFLICT":
            summary["status"] = "STUCK"
            summary["failed"].append({"recipe": identity, "reason": match_warnings})
            continue

        payload = _recipe_payload(recipe, week_id)
        if match:
            ok, response = _send_recipe_update(endpoints, match, payload)
            if ok:
                summary["updated"].append({"recipe": identity, "match": reason})
                url = _recipe_url(match)
                if url:
                    summary["mealie_urls"].append(url)
            else:
                summary["status"] = "PENDING_MEALIE_SYNC"
                summary["failed"].append({"recipe": identity, "operation": "update", "error": response})
            continue

        ok, created, create_warnings, response = _send_recipe_create(endpoints, payload)
        summary["warnings"].extend(create_warnings)
        if ok:
            created_recipe = created or {"name": recipe.get("name")}
            summary["created"].append({"recipe": identity})
            url = _recipe_url(created_recipe)
            if url:
                summary["mealie_urls"].append(url)
            existing.append(created_recipe)
        else:
            summary["status"] = "PENDING_MEALIE_SYNC"
            summary["failed"].append({"recipe": identity, "operation": "create", "error": response})

    return summary


if __name__ == "__main__":
    mcp.run(transport="stdio")
