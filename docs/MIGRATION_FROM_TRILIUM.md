# Migration From Trilium

Status: migration_admin

This file is migration/admin documentation only.

It is not a runtime workflow file and must not be loaded by default in Direction Projects after the migration.

During migration, Trilium is used only as the temporary source for transferring existing workflow and Direction notes into GitHub.

After Step 10 acceptance:
- GitHub repository files are the canonical AI workflow source.
- Trilium may remain useful for personal notes, research notes, whiteboard work, and non-runtime material.
- Runtime workflow files must not require Trilium as an operating layer.

Migration safety rules:
- Do not invent Direction data.
- Do not migrate private research notes into runtime Direction files.
- Do not mix Direction folders.
- Missing source material must be reported as `NEEDS_INPUT`, `source_missing`, or `migration_incomplete`.
