# Directions Legacy Evidence Boundary

Status: legacy_evidence_only

## Purpose

This directory contains Workflow v2 Direction evidence.

For Workflow v3 development, `directions/**` is read-only by default. It is not accepted Workflow v3 state.

Legacy Direction evidence may be inspected for migration/adoption evidence when an explicit bounded package authorizes that review.

## Boundary Rules

- No automatic import.
- No automatic discard.
- Do not delete, rename, move, archive, compact, or decommission legacy Direction folders without an explicit bounded package.
- Any carried-forward fact requires legacy evidence review plus an acceptance/update path.
- Future accepted v3 runtime state belongs under `directions_v3/<direction-id>/runtime/**` only after an explicit adoption/runtime-root package.

## Status

This file does not import, accept, bridge, migrate, persist, or create Workflow v3 runtime state.

END_OF_FILE: directions/README_LEGACY_EVIDENCE_ONLY.md
