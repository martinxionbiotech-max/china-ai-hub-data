# LiveCodeBench

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/livecodebench",
      "name": "LiveCodeBench",
      "url": "https://sinoaihub.com/benchmarks/livecodebench",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/livecodebench/",
      "description": "A contamination-controlled coding benchmark that continuously collects fresh problems from LeetCode, AtCoder and Codeforces contests, plus self-repair, code-execution and test-output-prediction tasks."
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
          "name": "LiveCodeBench",
          "item": "https://data.sinoaihub.com/benchmarks/livecodebench/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/livecodebench](https://sinoaihub.com/benchmarks/livecodebench)

## Type

benchmark

## Key facts

- **Task type:** Competitive-programming code generation plus self-repair, code execution and test-output prediction
- **Dataset size:** Continuously growing; initially 300+ problems from LeetCode, AtCoder and Codeforces contests (from May 2023 onward, updated over time)
- **Evaluation method:** Models solve fresh contest problems released after a cutoff date; graded by executing code against hidden test cases
- **Scoring:** Pass@1 accuracy (% of problems solved correctly on the first submission)
- **Recorded evaluations:** 0

## Description

A contamination-controlled coding benchmark that continuously collects fresh problems from LeetCode, AtCoder and Codeforces contests, plus self-repair, code-execution and test-output-prediction tasks.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes a LiveCodeBench score as of 2026-09-29.

## Methodology

**Task type:** Competitive-programming code generation plus self-repair, code execution and test-output prediction

**Dataset size:** Continuously growing; initially 300+ problems from LeetCode, AtCoder and Codeforces contests (from May 2023 onward, updated over time)

**Evaluation method:** Models solve fresh contest problems released after a cutoff date; graded by executing code against hidden test cases

**Scoring:** Pass@1 accuracy (% of problems solved correctly on the first submission)

**Contamination notes:** Problems are drawn from contests after a fixed cutoff date specifically to avoid contamination; the benchmark keeps adding new problems to stay ahead of training leakage.

## Relevant Models

No tracked model currently publishes a LiveCodeBench score. Natural candidates in the database include [DeepSeek-V4.1-Flash](../models/deepseek-v4-1-flash.md), [Kimi K2.7 Code](../models/kimi-k2.7-code.md) and [GLM-5.3-Flash](../models/glm-5.3-flash.md).

## Limitations

Pass@1 depends on sampling temperature and prompting, and on the execution sandbox. Newer problems are added continuously, so a score is always tied to a specific snapshot. No Chinese model in the China AI Hub database currently publishes a LiveCodeBench score, so this page records no evaluations.

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
| src-benchmarks-livecodebench-1 | Jain et al. — LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code | https://arxiv.org/abs/2403.07974 | Literature | 2024-03 | 2026-09-29 | high | — |
| src-benchmarks-livecodebench-2 | LiveCodeBench website | https://livecodebench.github.io/ | Official documentation | — | 2026-09-29 | high | — |
| src-benchmarks-livecodebench-3 | LiveCodeBench repository | https://github.com/LiveCodeBench/LiveCodeBench | Official documentation | — | 2026-09-29 | high | — |
