# AIME

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/aime",
      "name": "AIME",
      "url": "https://sinoaihub.com/benchmarks/aime",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/aime/",
      "description": "The American Invitational Mathematics Examination, repurposed as a benchmark: 15 integer-answer math problems used to test a model's advanced mathematical reasoning, with scores typically reported for AIME 2024 or AIME 2025."
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
          "name": "AIME",
          "item": "https://data.sinoaihub.com/benchmarks/aime/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/aime](https://sinoaihub.com/benchmarks/aime)

## Type

benchmark

## Key facts

- **Task type:** Advanced competition mathematics — 15 integer-answer problems
- **Dataset size:** 15 problems per exam (integer answers from 000 to 999); benchmark scores typically report AIME 2024 or AIME 2025
- **Evaluation method:** Models answer each problem; graded by exact match against the integer answer
- **Scoring:** Accuracy (% of 15 problems answered correctly); the raw exam score is 0–15
- **Recorded evaluations:** 0

## Description

The American Invitational Mathematics Examination, repurposed as a benchmark: 15 integer-answer math problems used to test a model's advanced mathematical reasoning, with scores typically reported for AIME 2024 or AIME 2025.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes an AIME score as of 2026-09-29.

## Methodology

**Task type:** Advanced competition mathematics — 15 integer-answer problems

**Dataset size:** 15 problems per exam (integer answers from 000 to 999); benchmark scores typically report AIME 2024 or AIME 2025

**Evaluation method:** Models answer each problem; graded by exact match against the integer answer

**Scoring:** Accuracy (% of 15 problems answered correctly); the raw exam score is 0–15

**Contamination notes:** AIME is a fixed public exam, so models trained after a given year may have seen its problems; vendors differ in which year(s) they report.

## Relevant Models

No tracked model currently publishes an AIME score. Natural candidates in the database include [DeepSeek-V4-Pro](../models/deepseek-v4-pro.md), [Kimi K3](../models/kimi-k3.md) and [Qwen3.8-Max](../models/qwen3.8-max.md).

## Limitations

AIME is an exam, not a versioned benchmark, so scores are only comparable when the same year is reported. Exact-match integer grading gives no partial credit for correct reasoning with a wrong final answer. No Chinese model in the China AI Hub database currently publishes an AIME score, so this page records no evaluations.

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
| src-benchmarks-aime-1 | Mathematical Association of America — American Invitational Mathematics Examination (AIME) | https://maa.org/math-competitions/american-invitational-mathematics-examination-aime | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-aime-2 | Mathematical Association of America — Competitions | https://maa.org/math-competitions | Official documentation | — | 2026-09-29 | high | — |
