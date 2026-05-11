# Migration State

Status: M0_M1_APPLIED_PENDING_VALIDATION
Updated at: 2026-05-11 10:33:28 +03:00

## Current Step

- Step: M0/M1
- Name: Migration Control + Full Legacy Inventory
- Runtime canonical source: GitHub repository
- Legacy source role: migration source only

## Direction Roots

| Direction | Legacy root id | GitHub path | Inventory |
|---|---|---|---|
| Solo Max Productive | TokWnxJOqNse | directions/solo-max-productive | migration/legacy_inventory/solo-max-productive_inventory.md |
| Indie Game Development | km9QhwfF2zoO | directions/indie-game-development | migration/legacy_inventory/indie-game-development_inventory.md |
| Health and Beauty | YqlUxoXMVTUr | directions/health-and-beauty | migration/legacy_inventory/health-and-beauty_inventory.md |

## Inventory Summary

- solo-max-productive: 166 visible entries, 0 inaccessible
- indie-game-development: 160 visible entries, 0 inaccessible
- health-and-beauty: 92 visible entries, 0 inaccessible

## Validation State

- migration folder exists: pending validation
- runtime files changed in M0/M1: no
- content migrated in M0/M1: no
- classification manifests complete: no, M2 required
- next allowed step after validation: M2 Classification Manifests

## M2 Classification Summary

- Updated at: 2026-05-11 10:35:47 +03:00
- Total classified inventory entries: 418
- migrate_to_github: 86
- needs_user_decision: 14
- needs_user_export: 0
- next allowed step after validation: M3 Canonical Repo Structure Cleanup


## M3 Structure Cleanup Summary

- Updated at: 2026-05-11 10:38:04 +03:00
- Added Direction README, knowledge, and domain_docs folders.
- Expanded direction.meta.yml to GitHub-only schema.
- Cleaned project file metadata to use GitHub repository file source wording.
- next allowed step after validation: M4 Workflow Core Verification

