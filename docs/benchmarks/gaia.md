# GAIA

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/gaia",
      "name": "GAIA",
      "url": "https://sinoaihub.com/benchmarks/gaia",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/gaia/",
      "description": "A benchmark for general AI assistants: 466 real-world questions requiring reasoning, multi-modality handling, web browsing and tool use, where humans score 92% and early frontier assistants far lower."
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
          "name": "GAIA",
          "item": "https://data.sinoaihub.com/benchmarks/gaia/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/gaia](https://sinoaihub.com/benchmarks/gaia)

## Type

benchmark

## Key facts

- **Task type:** Real-world question answering requiring reasoning, web browsing, multi-modality and tool use
- **Dataset size:** 466 questions across three difficulty levels; answers to 300 of them are held out for the leaderboard
- **Evaluation method:** Questions are conceptually simple for humans but require tool use; graded by exact-match against a single ground-truth answer
- **Scoring:** Exact-match accuracy (% correct); a question is passed only if the final answer matches exactly
- **Recorded evaluations:** 0

## Description

A benchmark for general AI assistants: 466 real-world questions requiring reasoning, multi-modality handling, web browsing and tool use, where humans score 92% and early frontier assistants far lower.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes a GAIA score as of 2026-09-29.

## Methodology

**Task type:** Real-world question answering requiring reasoning, web browsing, multi-modality and tool use

**Dataset size:** 466 questions across three difficulty levels; answers to 300 of them are held out for the leaderboard

**Evaluation method:** Questions are conceptually simple for humans but require tool use; graded by exact-match against a single ground-truth answer

**Scoring:** Exact-match accuracy (% correct); a question is passed only if the final answer matches exactly

**Contamination notes:** 300 of the 466 questions are retained privately for leaderboard evaluation, reducing training-set leakage.

## Relevant Models

No tracked model currently publishes a GAIA score. Natural candidates in the database include [DeepSeek-V4-Pro](../models/deepseek-v4-pro.md) and [Qwen3.8-Max](../models/qwen3.8-max.md).

## Limitations

Exact-match scoring is strict and can understate near-correct answers. Results depend on the tool/search scaffolding a model is given, so scores are not comparable across different setups. No Chinese model in the China AI Hub database currently publishes a GAIA score, so this page records no evaluations.

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
| src-benchmarks-gaia-1 | Mialon et al. — GAIA: a benchmark for General AI Assistants | https://arxiv.org/abs/2311.12983 | Literature | 2023-11 | 2026-09-29 | high | — |
| src-benchmarks-gaia-2 | GAIA benchmark (Hugging Face) | https://huggingface.co/gaia-benchmark | Official documentation | — | 2026-09-29 | high | — |
