# ARC-AGI

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/arc-agi",
      "name": "ARC-AGI",
      "url": "https://sinoaihub.com/benchmarks/arc-agi",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/arc-agi/",
      "description": "The Abstraction and Reasoning Corpus for AGI: grid-based visual reasoning tasks that are trivial for humans but have historically defeated frontier language models, used to measure general fluid intelligence."
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
          "name": "ARC-AGI",
          "item": "https://data.sinoaihub.com/benchmarks/arc-agi/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/arc-agi](https://sinoaihub.com/benchmarks/arc-agi)

## Type

benchmark

## Key facts

- **Task type:** Grid-based abstract visual reasoning — infer an input→output transformation and apply it to new grids
- **Dataset size:** ARC-AGI-1: 400 training + 400 public evaluation tasks; newer families (ARC-AGI-2, ARC-AGI-3) add fresh task sets
- **Evaluation method:** A task is solved if the model produces the correct output grid for every test input (up to 3 trials per input)
- **Scoring:** Accuracy (% of tasks solved); a task counts only if all test inputs are correct
- **Recorded evaluations:** 0

## Description

The Abstraction and Reasoning Corpus for AGI: grid-based visual reasoning tasks that are trivial for humans but have historically defeated frontier language models, used to measure general fluid intelligence.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes an ARC-AGI score as of 2026-09-29.

## Methodology

**Task type:** Grid-based abstract visual reasoning — infer an input→output transformation and apply it to new grids

**Dataset size:** ARC-AGI-1: 400 training + 400 public evaluation tasks; newer families (ARC-AGI-2, ARC-AGI-3) add fresh task sets

**Evaluation method:** A task is solved if the model produces the correct output grid for every test input (up to 3 trials per input)

**Scoring:** Accuracy (% of tasks solved); a task counts only if all test inputs are correct

**Contamination notes:** Evaluation tasks are held out; ARC-AGI-2 and ARC-AGI-3 introduce new task families to counter overfitting to ARC-AGI-1.

## Relevant Models

No tracked model currently publishes an ARC-AGI score. Natural candidates in the database include [DeepSeek-V4-Pro](../models/deepseek-v4-pro.md), [Qwen3.8-Max](../models/qwen3.8-max.md) and [Kimi K3](../models/kimi-k3.md).

## Limitations

ARC-AGI measures a specific form of abstraction, not general model quality; visual-grid reasoning is only weakly correlated with useful real-world task performance. No Chinese model in the China AI Hub database currently publishes an ARC-AGI score, so this page records no evaluations.

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
| src-benchmarks-arc-agi-1 | Chollet — On the Measure of Intelligence (introducing ARC) | https://arxiv.org/abs/1911.01547 | Literature | 2019-11 | 2026-09-29 | high | — |
| src-benchmarks-arc-agi-2 | ARC-AGI repository (fchollet) | https://github.com/fchollet/ARC-AGI | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-arc-agi-3 | ARC Prize / ARC-AGI | https://arcprize.org | Official documentation | — | 2026-09-29 | high | — |
