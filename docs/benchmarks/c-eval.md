# C-Eval

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/c-eval",
      "name": "C-Eval",
      "url": "https://sinoaihub.com/benchmarks/c-eval",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/c-eval/",
      "description": "A Chinese evaluation suite of 13,948 multiple-choice questions across 52 disciplines and four difficulty levels, for measuring advanced knowledge and reasoning of foundation models in a Chinese context."
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
          "name": "C-Eval",
          "item": "https://data.sinoaihub.com/benchmarks/c-eval/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/c-eval](https://sinoaihub.com/benchmarks/c-eval)

## Type

benchmark

## Key facts

- **Task type:** Multiple-choice knowledge and reasoning questions across 52 disciplines (humanities, science, engineering)
- **Dataset size:** 13,948 multiple-choice questions across 52 disciplines; four difficulty levels (middle school, high school, college, professional); plus the C-Eval Hard subset
- **Evaluation method:** Closed-book multiple-choice; models answer exam-style questions spanning 52 disciplines at four difficulty levels
- **Scoring:** Accuracy (% correct); reported as an overall average and per-discipline / per-level breakdowns
- **Recorded evaluations:** 0

## Description

A Chinese evaluation suite of 13,948 multiple-choice questions across 52 disciplines and four difficulty levels, for measuring advanced knowledge and reasoning of foundation models in a Chinese context.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes a C-Eval score as of 2026-09-29.

## Methodology

**Task type:** Multiple-choice knowledge and reasoning questions across 52 disciplines (humanities, science, engineering)

**Dataset size:** 13,948 multiple-choice questions across 52 disciplines; four difficulty levels (middle school, high school, college, professional); plus the C-Eval Hard subset

**Evaluation method:** Closed-book multiple-choice; models answer exam-style questions spanning 52 disciplines at four difficulty levels

**Scoring:** Accuracy (% correct); reported as an overall average and per-discipline / per-level breakdowns

**Contamination notes:** The complete C-Eval test set was released to the community in July 2025, so models trained after that date may have seen the answers.

## Relevant Models

No tracked model currently publishes a C-Eval score. Natural candidates in the database include [Qwen3.8-Max](../models/qwen3.8-max.md), [GLM-5.3](../models/glm-5.3.md) and [Kimi K3](../models/kimi-k3.md).

## Limitations

Multiple-choice format cannot assess free-form generation, open-ended reasoning or factual grounding. Scores on C-Eval Hard and the full set are not interchangeable. No Chinese model in the China AI Hub database currently publishes a C-Eval score, so this page records no evaluations.

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
| src-benchmarks-c-eval-1 | Huang et al. — C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models | https://arxiv.org/abs/2305.08322 | Literature | 2023-05 | 2026-09-29 | high | — |
| src-benchmarks-c-eval-2 | C-Eval official repository (HKUST-NLP) | https://github.com/hkust-nlp/ceval | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-c-eval-3 | C-Eval benchmark website | https://cevalbenchmark.com/ | Official documentation | — | 2026-09-29 | high | — |
