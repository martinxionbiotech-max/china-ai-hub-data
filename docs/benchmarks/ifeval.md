# IFEval

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/ifeval",
      "name": "IFEval",
      "url": "https://sinoaihub.com/benchmarks/ifeval",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/ifeval/",
      "description": "Instruction-Following Eval: a benchmark of verifiable instructions ('write over 400 words', 'mention a keyword at least 3 times') that checks whether a model actually obeys precise natural-language constraints, scored by rule-checking rather than an LLM judge."
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
          "name": "IFEval",
          "item": "https://data.sinoaihub.com/benchmarks/ifeval/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/ifeval](https://sinoaihub.com/benchmarks/ifeval)

## Type

benchmark

## Key facts

- **Task type:** Instruction following on verifiable natural-language constraints (length, format, keyword counts, etc.)
- **Dataset size:** 25 types of verifiable instructions; approximately 500 prompts, each containing one or more verifiable instructions
- **Evaluation method:** Prompts carry rule-checkable instructions; a program verifies whether each constraint was satisfied
- **Scoring:** Strict accuracy and prompt-level / instruction-level accuracy (fraction of instructions followed)
- **Recorded evaluations:** 0

## Description

Instruction-Following Eval: a benchmark of verifiable instructions ("write over 400 words", "mention a keyword at least 3 times") that checks whether a model actually obeys precise natural-language constraints, scored by rule-checking rather than an LLM judge.

## Evaluations

No evaluations recorded — no tracked Chinese model publishes an IFEval score as of 2026-09-29.

## Methodology

**Task type:** Instruction following on verifiable natural-language constraints (length, format, keyword counts, etc.)

**Dataset size:** 25 types of verifiable instructions; approximately 500 prompts, each containing one or more verifiable instructions

**Evaluation method:** Prompts carry rule-checkable instructions; a program verifies whether each constraint was satisfied

**Scoring:** Strict accuracy and prompt-level / instruction-level accuracy (fraction of instructions followed)

**Contamination notes:** Rule-checked verification (not an LLM judge) reduces evaluator bias; the verifiable-instruction format is not tied to a single knowledge cutoff.

## Relevant Models

No tracked model currently publishes an IFEval score. Natural candidates in the database include [Qwen3.8-Max](../models/qwen3.8-max.md), [GLM-5.3](../models/glm-5.3.md) and [DeepSeek-V4-Pro](../models/deepseek-v4-pro.md).

## Limitations

IFEval measures only mechanical, rule-checkable instruction following — it does not capture semantic quality, helpfulness or correctness of the response content. No Chinese model in the China AI Hub database currently publishes an IFEval score, so this page records no evaluations.

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
| src-benchmarks-ifeval-1 | Zhou et al. — Instruction-Following Evaluation for Large Language Models (IFEval) | https://arxiv.org/abs/2311.07911 | Literature | 2023-11 | 2026-09-29 | high | — |
| src-benchmarks-ifeval-2 | IFEval — Google Research (instruction_following_eval) | https://github.com/google-research/google-research/tree/master/instruction_following_eval | Official documentation | — | 2026-09-29 | high | — |
