# china-ai-hub-data

Data layer for **China AI Hub** — future subdomain `data.chinaaihub.com`.

- **Main site repo:** [martinxionbiotech-max/china-ai-hub](https://github.com/martinxionbiotech-max/china-ai-hub) (chinaaihub.com)
- **This repo:** structured data layer for China AI Hub
- **Created:** 2026-09-21
- **Status:** live — structured fact + evidence + history layer

## Schema & historical dimensions

Each entity record carries a `last_verified` date and a `sources` table (source_type + confidence). On top of that, the following historical dimensions are structured (all values sourced, no fabrication):

- **`release_history`** (models) — chronological release timeline. Each entry: `date`, `event`, `source`, `verification_date`. Populated only where a multi-event timeline is documented (e.g. DeepSeek-V4-Pro Preview → GA → deprecation reversal; Qwen3.8-Max → 0902 snapshot).
- **`price_history`** (pricing) — documented price-change events. Each entry: `model`, `field`, `old`, `new`, `effective`, `source`, `verification_date`. Providers with no documented price change state "no documented events" explicitly rather than inventing history.
- **`benchmark_history`** — not built: the main site documents benchmark *version* divergence (e.g. Terminal-Bench 2.1 vs 3.0 vs 4.0) but no sourced before/after benchmark values for the same model+benchmark. Skipped to avoid fabrication.
- **`timeline`** (companies) — company-level milestones (founding, model releases, pricing changes). Each entry: `date`, `event`, `type`, `source`, `verification_date`.

## Relationship to main site

The main site hosts the three information layers (structured data, knowledge, original research). This repo is the planned data layer at `data.chinaaihub.com`, to be introduced after the main site's information architecture and authority are established (see main repo `docs/MASTER_PROMPT.md`, section 4).
