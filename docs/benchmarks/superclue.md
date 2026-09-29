# SuperCLUE

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/superclue",
      "name": "SuperCLUE",
      "url": "https://sinoaihub.com/benchmarks/superclue",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/superclue/",
      "description": "A Chinese comprehensive evaluation system for large models, organised around four ability quadrants — language understanding and generation, professional knowledge, agent capability and safety — refined into 12 base capabilities."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://data.sinoaihub.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Benchmarks",
          "item": "https://data.sinoaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "SuperCLUE",
          "item": "https://data.sinoaihub.com/benchmarks/superclue/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/superclue](https://sinoaihub.com/benchmarks/superclue)

## Type

benchmark

## Key facts

- **Task type:** Chinese multi-part evaluation spanning language understanding/generation, professional knowledge, agent capability and safety
- **Dataset size:** Multi-part rolling evaluation across four ability quadrants and 12 base capabilities; no fixed single question count (periodic leaderboard releases)
- **Evaluation method:** Combines objective multiple-choice questions with multi-turn open-ended questions and agent/tool-use tasks; scored by the CLUE team rather than self-reported
- **Scoring:** Composite total score (总分) with sub-scores per quadrant (e.g. OPEN multi-turn, open questions, objective questions)
- **Recorded evaluations:** 0

## Description

A Chinese comprehensive evaluation system for large models, organised around four ability quadrants — language understanding and generation, professional knowledge, agent capability and safety — refined into 12 base capabilities.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes a SuperCLUE score as of 2026-09-29.

## Methodology

**Task type:** Chinese multi-part evaluation spanning language understanding/generation, professional knowledge, agent capability and safety

**Dataset size:** Multi-part rolling evaluation across four ability quadrants and 12 base capabilities; no fixed single question count (periodic leaderboard releases)

**Evaluation method:** Combines objective multiple-choice questions with multi-turn open-ended questions and agent/tool-use tasks; scored by the CLUE team rather than self-reported

**Scoring:** Composite total score (总分) with sub-scores per quadrant (e.g. OPEN multi-turn, open questions, objective questions)

**Contamination notes:** SuperCLUE maintains public and hidden test sets and runs its own evaluation, reducing reliance on vendor self-reported scores.

## Relevant Models

No tracked model currently publishes a SuperCLUE score. Natural candidates in the database include [Doubao Seed 2.1 Pro](../models/doubao-seed-2-1-pro.md), [GLM-5.3](../models/glm-5.3.md) and [Qwen3.8-Max](../models/qwen3.8-max.md).

## Limitations

The composite score aggregates heterogeneous sub-tasks, so a single total hides capability-specific strengths. Leaderboard snapshots are time-stamped and not comparable across dates. No Chinese model in the China AI Hub database currently publishes a SuperCLUE score, so this page records no evaluations.

## Verification Status

verified

## Benchmark Changes

No documented benchmark changes on record as of 2026-09-29.

## Last Verified

2026-09-29

## Source history

No documented source-change events located as of 2026-09-29.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-benchmarks-superclue-1 | SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark | https://arxiv.org/abs/2307.15020 | Literature | 2023-07 | 2026-09-29 | high | — |
| src-benchmarks-superclue-2 | SuperCLUE official repository (CLUEbenchmark) | https://github.com/CLUEbenchmark/SuperCLUE | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-superclue-3 | SuperCLUE official website | https://www.superclueai.com/ | Official documentation | — | 2026-09-29 | high | — |
