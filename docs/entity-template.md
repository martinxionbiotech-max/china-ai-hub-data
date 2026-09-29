# Entity Template

Unified field structure for the five entity collections — **Models, Companies,
Agents, APIs, Benchmarks** (plus the `pricing` time-series, which is a per-provider
price snapshot rather than an entity). This document is the single source of truth
for how a record in `data.sinoaihub.com` is shaped, and it is what the backfill
scripts enforce.

Every entity record carries a **common core** of identity + provenance fields, then
a **collection-specific** set. Unknown or non-applicable values use `null` /
`unknown` / `not publicly disclosed` — never invented.

## Common core (every entity)

| Field | Meaning | Notes |
|---|---|---|
| `id` | Stable lowercase-hyphen identifier | Equals the filename stem; immutable |
| `name` | Display name | H1 title on the page |
| `type` | `model` \| `company` \| `agent` \| `api` \| `benchmark` \| `pricing` | New in 2B-P1; added to all 59 records |
| `provider` | Owning organization (→ companies id) | Models / agents / APIs / pricing link to a company; companies link to themselves implicitly |
| `status` | `active` \| `preview` \| `deprecated` \| `discontinued` | Models carry it explicitly; other collections infer `active` from `last_verified` freshness |
| `release_date` | ISO 8601 (or `~YYYY-MM`) | Models have it; companies use `founded`; agents / APIs / benchmarks usually lack a public date |
| `official_url` | Canonical main-site page | The "Canonical page" link at the top of every record |
| `sources` | Evidence list | Unified schema — see [evidence-layer.md](evidence-layer.md) |
| `last_verified` | Verification date | Present on every record |
| `verification_status` | `verified` \| `partially_verified` | New in 2B-P1; derived from source confidence + documented disclosure gaps |

## Collection-specific fields

### Models

| Field | Example | Required |
|---|---|---|
| `model_family` | DeepSeek-V4 | yes |
| `version` | `0813` | when documented |
| `aliases` | `deepseek-v4-pro-0813` | when documented |
| `architecture` | MoE: 1.6T total / 49B active | when disclosed |
| `parameter_information` | `total_parameters`, `active_parameters` | when disclosed |
| `context_window` | 1048576 | when disclosed |
| `maximum_output` | 393216 | when disclosed |
| `capabilities` | reasoning / coding / math / vision / tool_calling / function_calling / structured_output | yes (each tri-state) |
| `open_weight` | true / false | yes |
| `license` | MIT \| Apache-2.0 \| proprietary \| custom | yes |
| `self_hosting` | true / false | yes |
| `api_available` | true / false | yes |
| `pricing` | input/output per 1M + currency + pricing_ref | yes (if api_available) |
| `official_api` | true / false | yes |
| `cloud_providers` | `[DeepSeek Platform]` | when documented |
| `regions` | `[china, global]` \| `unknown` | when documented |
| `benchmark_results` | benchmark / score / metric / date / source | when documented |
| `release_history` | date / event / source / verification_date | when multi-event |
| `model_versions` | version / date / source | when documented (2B-P1) |
| `license_changes` | change events | none documented (2B-P1) |
| `known_limitations` | list | yes |

### Companies

| Field | Example | Notes |
|---|---|---|
| `aliases` | 深度求索 | |
| `founded` | 2023 | replaces `release_date` |
| `headquarters` | Hangzhou, Zhejiang, China | |
| `funding` | "No external funding disclosed…" | |
| `ai_products` | list | |
| `foundation_models` | → models ids | |
| `open_models` | → models ids | |
| `agents` | → agents ids | |
| `api` | → apis ids | |
| `major_releases` | name / date / type | |
| `timeline` | date / event / type / source / verification_date | company milestones (2B-P1) |
| `open_source_projects` | list | |
| `official_documentation` | URL | |
| `official_website` | URL | |

### Agents

| Field | Example | Notes |
|---|---|---|
| `company` | → companies id | |
| `description` | 1–3 factual sentences | |
| `agent_type` | `coding` \| `browser` \| `computer_use` \| … | defensible |
| `underlying_models` | → models ids | |
| `framework` | TypeScript terminal agent | |
| `tool_calling` / `browser_use` / `computer_use` / `mcp` / `memory` / `planning` / `multi_agent` / `api` | true / false | tri-state |
| `pricing` | description | |
| `deployment` | `cloud` \| `self_hosted` \| `both` | |
| `open_source` | true / false | |
| `license` | MIT | |
| `github` / `documentation` | URL | |
| `use_cases` / `limitations` | list | |

### APIs

| Field | Example | Notes |
|---|---|---|
| `provider` | → companies id | |
| `api_type` | `official` \| `cloud_hosted` \| … | |
| `endpoint` | https://api.deepseek.com | |
| `authentication` | Bearer API key | |
| `streaming` / `function_calling` / `tool_calling` / `structured_output` / `vision` | true / false | |
| `context_limits` | model / input_limit / output_limit | |
| `rate_limits` | text | |
| `regions` / `cloud_providers` | | |
| `pricing_ref` | → pricing id | |
| `documentation` | URL | |
| `api_changes` | date / change / source | DeepSeek only (2B-P1) |

### Benchmarks

| Field | Example | Notes |
|---|---|---|
| `description` | what it measures | |
| `task_type` / `dataset_size` / `evaluation_method` / `scoring` | methodology | |
| `evaluations` | benchmark / model / score / model_version / metric / date / source_type / source_url | per-result source_type mandatory |
| `relevant_models` | → models ids + scores | |
| `limitations` | | |
| `benchmark_changes` | before/after values | none sourced (2B-P1) |

## Field presence matrix (2B-P1)

Counts of the 59 entity records (21 models + 6 companies + 10 agents + 6 APIs +
6 pricing + 10 benchmarks) after backfill.

| Collection | Records | Common-core `type` added | `verification_status` added | Sparse (missing ≥1 optional field) |
|---|---|---|---|---|
| Models | 21 | 21 | 21 | 13 `partially_verified` (context / architecture / parameters / capabilities / benchmarks not disclosed) |
| Companies | 6 | 6 | 6 | 0 |
| Agents | 10 | 10 | 10 | 0 |
| APIs | 6 | 6 | 6 | 1 `partially_verified` (minimax structured_output) |
| Pricing | 6 | 6 | 6 | 0 |
| Benchmarks | 10 | 10 | 10 | 0 |

## Backfill rules

- Values are copied only from the main-site frontmatter or existing data-hub
  content. Nothing is sourced from memory.
- A field absent from both is left out or marked `unknown` / `not publicly
  disclosed` — it is never guessed.
- `verification_status` = `verified` when core facts rest on high-confidence
  official sources and no core field is documented as undisclosed;
  `partially_verified` when a core field is documented as not publicly
  disclosed (the gap is stated, not hidden).
