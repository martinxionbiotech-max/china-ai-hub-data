# Evidence Layer

Unified `sources` schema and the 2B-P1 backfill that applied it to every entity
record in the data hub.

## Unified source record

Every entry in a record's `## Sources` table now carries the same seven fields:

| Field | Meaning | Rules |
|---|---|---|
| `evidence_id` | Stable, globally-unique identifier | `src-<collection>-<entity>-<n>`, e.g. `src-models-deepseek-v4-pro-1` |
| `source_name` | 出处 (provenance label) | human-readable name of the source |
| `source_url` | URL | canonical locator |
| `source_type` | Type of source | enumerated below |
| `published` | Source publication date | filled only where documented; `—` otherwise (never guessed) |
| `verified` | Verification date | was `last_verified` |
| `confidence` | `high` \| `medium` \| `low` | |
| `conflict` | Contradiction flag | `—` unless the record documents a conflict between sources |

## `source_type` enumeration

| Value | Applies to |
|---|---|
| `Official` | Vendor blog posts, release announcements, official site pages |
| `Official documentation` | API docs, model/pricing pages, release notes, GitHub repos/READMEs, license files |
| `Model card` | Hugging Face / provider model cards |
| `Vendor-reported` | Benchmark scores published by the model vendor |
| `Independent benchmark` | Third-party benchmark evaluation |
| `China AI Hub analysis` | Original China AI Hub research/interpretation |
| `Literature` | Academic or industry literature |

The legacy `official` tag was split into `Official` / `Official documentation` /
`Model card` by source name and URL (e.g. a Hugging Face URL → `Model card`, a
`docs.*` / GitHub URL → `Official documentation`).

## Backfill results (2B-P1)

- **Records touched:** 59 (all entity + pricing files)
- **Evidence rows:** 168
- **`source_type` distribution:**
  - `Official documentation` — 130
  - `Official` — 26
  - `Model card` — 12
- **`confidence` distribution:** `high` — 168 (no medium/low rows exist today)
- **`conflict` annotations:** 1 — DeepSeek-V4-Pro's "API Change Log" source is
  flagged as conflicting with the same-day deprecation announcement
  (V4-Pro → V4.1-Flash routing vs. unchanged billing). This is the only
  documented source conflict in the dataset.

## Zero-fabrication rules

- `published` is `—` wherever the legacy table had no `published_date`. No
  publication dates were inferred.
- `verified` is copied from the existing `last_verified`.
- `conflict` is written only where the record itself documents a contradiction
  (see DeepSeek-V4-Pro known-limitations). No conflicts were invented.
- `evidence_id` is deterministic and stable: re-running the backfill on the same
  source order reproduces the same IDs.
