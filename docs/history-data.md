# History Data

Structured historical dimensions on top of the current-value fields. Every entry
is sourced (each row carries a `source` and `verification_date`); dimensions with
no documented evidence carry the explicit annotation **"No documented changes on
record"** rather than an empty table or a fabricated one.

## Dimensions

### Pre-existing (2B-P2)

| Dimension | Collection | Structure | Coverage |
|---|---|---|---|
| `release_history` | models | date / event / source / verification_date | 4 models (DeepSeek-V4-Pro, DeepSeek-V4.1-Flash, Qwen3.8-Max, Doubao Seed 2.1 Pro) |
| `price_history` | pricing | model / field / old / new / effective / source / verification_date | 2 providers (DeepSeek, MiniMax); 4 providers state "no documented events" |
| `timeline` | companies | date / event / type / source / verification_date | 6 companies (all) |

### New (2B-P1)

| Dimension | Collection | Structure | Coverage |
|---|---|---|---|
| `model_versions` | models | version / date / source / verification_date | 5 models (see below); 16 models — no documented version sequence |
| `license_changes` | models | change events | 0 — **No documented license changes on record** for all 21 models |
| `api_changes` | apis | date / change / source / verification_date | 1 API (DeepSeek); 5 APIs — no documented changes |
| `company_milestones` | companies | merged into existing `timeline` | 6 companies (already covered; no separate field added) |
| `benchmark_changes` | benchmarks | before/after values (both must be sourced) | 0 — **No documented benchmark changes on record** for all 10 benchmarks |

## `model_versions` — documented version sequences

Version snapshots are recorded only where the entity itself documents them
(Version / Aliases / Release History). A `date` of `—` means the snapshot is
documented but carries no sourced date.

| Model | Versions |
|---|---|
| DeepSeek-V4-Pro | V4 Preview (2026-04-24) → 0813 GA (2026-08-13) |
| Qwen3.8-Max | initial (2026-08) → 0902 snapshot (2026-09-02) |
| Doubao Seed 2.1 Pro | 260628 (—) → 260915 (2026-09) |
| Doubao Seed 2.1 Turbo | 260628 (—) |
| Doubao Seed Evolving | rolling (—) |

**16 models with no documented version sequence:** DeepSeek-V3.2,
DeepSeek-V4.1-Flash, GLM-5.2, GLM-5.3, GLM-5.3-Flash, GLM-5.3-FlashX, Kimi K2.6,
Kimi K2.7 Code, Kimi K2.7 Code Highspeed, Kimi K3, MiniMax-M2.7,
MiniMax-M2.7-Highspeed, MiniMax-M3, Qwen3.7-Plus, Qwen3.8-2.4T-A95B, Qwen3.8-Flash.

## `api_changes` — documented API-platform changes

Only DeepSeek's official Change Log documents API-platform changes:

| Date | Change |
|---|---|
| 2026-08-13 | DeepSeek-V4-Pro GA (0813) shipped on the API |
| 2026-08-16 | Peak/off-peak pricing introduced (peak = 2x off-peak) |
| 2026-09-10 | V4-Pro deprecation announced then reversed the same day; V4.1-Flash released |

**5 APIs with no documented changes:** ark, minimax, model-studio, moonshot, zai.

## Why three dimensions are empty

- **`license_changes`** — no model has a documented license change on record.
  (GLM-5.2 → GLM-5.3 changed MIT → Apache-2.0, but that is a *successor model*,
  not a license change within one entity.)
- **`benchmark_changes`** — a change record requires *both* a before and an after
  value with sources. The main site documents benchmark *version* divergence
  (e.g. Terminal-Bench 2.1 vs 3.0 vs 4.0) but no sourced before/after pair for
  the same model+benchmark, so the dimension is intentionally left empty.
- **`company_milestones`** — company milestones are already structured in the
  `timeline` field (founding, releases, pricing changes), so no separate field
  was introduced.

## Zero-fabrication rules

- A dimension is populated only where both the event and its source already
  exist in the record. No dates, versions, scores or prices are inferred.
- Empty dimensions are written out as "No documented changes on record as of
  2026-09-29" — stating the absence of evidence rather than implying none was
  looked for.
