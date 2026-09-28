# China AI Hub Data

This is the **data layer** for [China AI Hub](https://sinoaihub.com) — the English-language structured information layer for China's AI ecosystem.

While the main site hosts editorial content, comparisons and original research, this data hub is dedicated to the **structured reference data** behind it: what is known, verified, and sourceable about Chinese AI models, companies, agents, APIs, pricing and benchmarks.

## What this hub covers

| Section | Scope |
|---------|-------|
| [Models](models/index.md) | Chinese foundation and coding models: capabilities, context windows, training knowledge, release dates |
| [Companies](companies/index.md) | The organizations building China's AI stack: ownership, funding, products |
| [Agents](agents/index.md) | Consumer and developer agent products: features, platforms, defaults |
| [APIs](apis/index.md) | API platforms and endpoints: access, modalities, token limits |
| [Pricing](pricing/index.md) | Time-stamped pricing snapshots with effective dates, plus documented `price_history` |
| [Benchmarks](benchmarks/index.md) | Benchmark methodologies and vendor-reported results |

### Historical dimensions

Beyond current-value fields, each collection carries sourced history where documented: models expose a `release_history` timeline; pricing exposes `price_history` change events; companies expose a `timeline` of founding, release and pricing milestones. Every history entry includes a `source` and `verification_date`. `benchmark_history` is intentionally not built — no sourced before/after benchmark values exist for any model+benchmark pair.

## Relationship to the main site

- **Main site (sinoaihub.com)** = editorial authority: what it means, how to choose, original research
- **Data hub (data.sinoaihub.com)** = reference layer: what is known, with sources

Every entity here links back to its canonical page on the main site. All data follows the same source policy as the main site: no fabricated data, official sources first, `FACT` / `VENDOR CLAIM` / `ANALYSIS` classification, and `unknown` where information is not publicly disclosed.

## Status

**Skeleton (2026-09-21).** Section structures are in place; full entity pages are being migrated from the main site's structured collections.

- Models: 19 tracked
- Companies: 6 tracked
- Agents: 10 tracked
- APIs: 6 tracked
- Pricing: 6 providers tracked
- Benchmarks: 10 tracked
