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

### Data schemas

- [Entity Template](entity-template.md) — unified field structure for every collection
- [Evidence Layer](evidence-layer.md) — unified `sources` schema (`evidence_id`, `source_type`, `published`, `verified`, `confidence`, `conflict`)
- [History Data](history-data.md) — structured historical dimensions (`model_versions`, `license_changes`, `api_changes`, `company_milestones`, `benchmark_changes`)

### Historical dimensions

Beyond current-value fields, each collection carries sourced history where documented: models expose a `release_history` timeline; pricing exposes `price_history` change events; companies expose a `timeline` of founding, release and pricing milestones. Every history entry includes a `source` and `verification_date`. `benchmark_history` is intentionally not built — no sourced before/after benchmark values exist for any model+benchmark pair.

## Relationship to the main site

- **Main site (sinoaihub.com)** = editorial authority: what it means, how to choose, original research
- **Data hub (data.sinoaihub.com)** = reference layer: what is known, with sources

Every entity here links back to its canonical page on the main site. All data follows the same source policy as the main site: no fabricated data, official sources first, `FACT` / `VENDOR CLAIM` / `ANALYSIS` classification, and `unknown` where information is not publicly disclosed.

## Status

The data hub is **fully migrated** from the main site's structured collections and is maintained as the canonical structured-fact + evidence + history layer. Every entity page carries the complete eight-element block (definition, key facts, relationships, evidence, source history, update date, related entities, and a canonical main-site link), with sources and `last_verified` dates on every record.

- Models: 21 tracked
- Companies: 12 tracked
- Agents: 18 tracked
- APIs: 6 tracked
- Pricing: 6 providers tracked
- Benchmarks: 18 tracked

### Completeness self-check

Entity counts are verified across four surfaces by `scripts/check-entity-counts.py` in the main-site repo: main-site content files, data-hub records, the main-site sitemap, and the data hub's declared entities (nav + index tables) must all agree. Any drift fails the check. See the main repo's `docs/data-integrity-check.md` for the current comparison table and the mechanics of the check.

- **Eight-element coverage** — all 81 entity pages (21 models + 12 companies + 18 agents + 6 APIs + 6 pricing + 18 benchmarks) carry Definition/Description, Key facts, Sources, and a canonical main-site link; source-history notes are present where applicable.
- **Canonical links** — every record links to its main-site page; dangling canonicals are fixed as part of migration.
- **Cross-surface parity** — models, companies, agents, APIs, pricing and benchmarks each show 0 discrepancy between the four surfaces.
