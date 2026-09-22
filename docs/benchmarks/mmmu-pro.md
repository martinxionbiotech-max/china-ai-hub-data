# MMMU-Pro

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://chinaaihub.com/benchmarks/mmmu-pro",
      "name": "MMMU-Pro",
      "url": "https://chinaaihub.com/benchmarks/mmmu-pro",
      "mainEntityOfPage": "https://data.chinaaihub.com/benchmarks/mmmu-pro/",
      "description": "Multimodal, multi-discipline understanding benchmark with college-level questions requiring reasoning.",
      "dateModified": "2026-09-20"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://data.chinaaihub.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Benchmarks",
          "item": "https://data.chinaaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "MMMU-Pro",
          "item": "https://data.chinaaihub.com/benchmarks/mmmu-pro/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/benchmarks/mmmu-pro](https://chinaaihub.com/benchmarks/mmmu-pro)

## Description

Multimodal, multi-discipline understanding benchmark with college-level questions requiring reasoning.

## Evaluations

| benchmark | model | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|
| MMMU-Pro | [kimi-k3](../models/kimi-k3.md) | 81.6 (83.4 with tools) | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| MMMU-Pro | kimi-k2.5 | 78.5 | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |

## Methodology

**Task type:** Multimodal understanding and reasoning (college-level, multi-discipline)

**Dataset size:** 1,730 questions in standard format plus 1,730 vision-augmented variants (3,460 total); parent MMMU = 11.5K questions across 6 disciplines, 30 subjects

**Evaluation method:** Multiple-choice questions with interleaved images; vision-only input setting removes text leakage

**Scoring:** Accuracy (% correct answers)

## Limitations

All scores are vendor-reported and not independently verified. With-tools and without-tools results are not directly comparable.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
| Kimi K2.5 GitHub README | https://github.com/MoonshotAI/Kimi-K2.5 | official | 2026-09-20 | high |
