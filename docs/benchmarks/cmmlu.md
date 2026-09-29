# CMMLU

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/cmmlu",
      "name": "CMMLU",
      "url": "https://sinoaihub.com/benchmarks/cmmlu",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/cmmlu/",
      "description": "A comprehensive Chinese benchmark measuring massive multitask language understanding across 67 subjects, from STEM and humanities to China-specific knowledge such as driving rules."
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
          "name": "CMMLU",
          "item": "https://data.sinoaihub.com/benchmarks/cmmlu/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/cmmlu](https://sinoaihub.com/benchmarks/cmmlu)

## Type

benchmark

## Key facts

- **Task type:** Chinese multiple-choice knowledge and reasoning questions across 67 subjects
- **Dataset size:** 67 subjects from elementary to advanced professional level; multiple-choice with 4 options and a single correct answer; a 5-question development set and a 100+ question test set per subject
- **Evaluation method:** Multiple-choice; evaluated in zero-shot and five-shot settings, with and without chain-of-thought
- **Scoring:** Accuracy (% correct); the random baseline is 25%
- **Recorded evaluations:** 0

## Description

A comprehensive Chinese benchmark measuring massive multitask language understanding across 67 subjects, from STEM and humanities to China-specific knowledge such as driving rules.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes a CMMLU score as of 2026-09-29.

## Methodology

**Task type:** Chinese multiple-choice knowledge and reasoning questions across 67 subjects

**Dataset size:** 67 subjects from elementary to advanced professional level; multiple-choice with 4 options and a single correct answer; a 5-question development set and a 100+ question test set per subject

**Evaluation method:** Multiple-choice; evaluated in zero-shot and five-shot settings, with and without chain-of-thought

**Scoring:** Accuracy (% correct); the random baseline is 25%

**Contamination notes:** CMMLU maintainers verify API-only models for data contamination before listing them on the leaderboard; questions include China-specific answers less common in English training data.

## Relevant Models

No tracked model currently publishes a CMMLU score. Natural candidates in the database include [Qwen3.8-Max](../models/qwen3.8-max.md), [DeepSeek-V4-Pro](../models/deepseek-v4-pro.md) and [GLM-5.3](../models/glm-5.3.md).

## Limitations

Multiple-choice format measures recognition and reasoning within fixed options, not free-form generation or grounding. Zero-shot and five-shot scores are not directly comparable. No Chinese model in the China AI Hub database currently publishes a CMMLU score, so this page records no evaluations.

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
| src-benchmarks-cmmlu-1 | Li et al. — CMMLU: Measuring massive multitask language understanding in Chinese | https://arxiv.org/abs/2306.09212 | Literature | 2023-06 | 2026-09-29 | high | — |
| src-benchmarks-cmmlu-2 | CMMLU official repository | https://github.com/haonan-li/CMMLU | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-cmmlu-3 | CMMLU dataset card (Hugging Face) | https://huggingface.co/datasets/haonan-li/cmmlu | Official documentation | — | 2026-09-29 | high | — |
