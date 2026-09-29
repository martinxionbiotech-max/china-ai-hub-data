# SWE-bench

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/swe-bench",
      "name": "SWE-bench",
      "url": "https://sinoaihub.com/benchmarks/swe-bench",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/swe-bench/",
      "description": "Software engineering benchmark family built from real GitHub issues, with Pro, Verified and Multilingual variants."

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
          "name": "SWE-bench",
          "item": "https://data.sinoaihub.com/benchmarks/swe-bench/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/swe-bench](https://sinoaihub.com/benchmarks/swe-bench)

## Type

benchmark


## Key facts

- **Task type:** Software engineering (resolve real GitHub issues by generating code patches)
- **Dataset size:** 2,294 task instances from 12 Python repositories (full set); SWE-bench Verified = 500 human-confirmed solvable problems
- **Evaluation method:** Docker-containerized harness; the model's patch is applied to the repository and the project's tests are run to verify resolution
- **Scoring:** Resolved rate (% of instances where all tests pass)
- **Recorded evaluations:** 6

## Description

Software engineering benchmark family built from real GitHub issues, with Pro, Verified and Multilingual variants.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| SWE-bench | [qwen3.8-max](../models/qwen3.8-max.md) | 67.7 | Pro | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| SWE-bench | [minimax-m3](../models/minimax-m3.md) | 59.0 | Pro | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/blog/minimax-m3 |
| SWE-bench | kimi-k2.5 | 76.8 | Verified | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |
| SWE-bench | minimax-m2 | 69.4 | Verified | accuracy | 2025-10 | vendor_reported | https://github.com/MiniMax-AI/MiniMax-M2 |
| SWE-bench | minimax-m2 | 56.5 | Multilingual | accuracy | 2025-10 | vendor_reported | https://github.com/MiniMax-AI/MiniMax-M2 |

## Methodology

**Task type:** Software engineering (resolve real GitHub issues by generating code patches)

**Dataset size:** 2,294 task instances from 12 Python repositories (full set); SWE-bench Verified = 500 human-confirmed solvable problems

**Evaluation method:** Docker-containerized harness; the model's patch is applied to the repository and the project's tests are run to verify resolution

**Scoring:** Resolved rate (% of instances where all tests pass)

## Relevant Models

- [Qwen3.8-Max](../models/qwen3.8-max.md) — 67.7
- [MiniMax-M3](../models/minimax-m3.md) — 59.0

## Limitations

Pro, Verified and Multilingual variants are different test sets and are not comparable to each other; the variant is recorded per evaluation. All scores are vendor-reported and not independently verified.

## Verification Status

verified

## Benchmark Changes

No documented benchmark changes on record as of 2026-09-29.

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-benchmarks-swe-bench-1 | Qwen3.8-2.4T-A95B model card | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | Model card | — | 2026-09-20 | high | — |
| src-benchmarks-swe-bench-2 | MiniMax M3 official blog post | https://www.minimax.cn/blog/minimax-m3 | Official | — | 2026-09-20 | high | — |
| src-benchmarks-swe-bench-3 | Kimi K2.5 GitHub README | https://github.com/MoonshotAI/Kimi-K2.5 | Official documentation | — | 2026-09-20 | high | — |
