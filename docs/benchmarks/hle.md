# HLE

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://chinaaihub.com/benchmarks/hle",
      "name": "HLE",
      "url": "https://chinaaihub.com/benchmarks/hle",
      "mainEntityOfPage": "https://data.chinaaihub.com/benchmarks/hle/",
      "description": "Humanity's Last Exam - a frontier benchmark of expert-level questions across disciplines, often reported with and without tool access.",
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
          "name": "HLE",
          "item": "https://data.chinaaihub.com/benchmarks/hle/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/benchmarks/hle](https://chinaaihub.com/benchmarks/hle)

## Description

Humanity's Last Exam - a frontier benchmark of expert-level questions across disciplines, often reported with and without tool access.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| HLE | [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 36.8 | 39.1 on pure-text subset | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| HLE | [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 42.7 (60.0 with tools) | — | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| HLE | [qwen3.8-max](../models/qwen3.8-max.md) | 43.6 (56.2 with tools) | — | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| HLE | [kimi-k3](../models/kimi-k3.md) | 43.5 (56.0 with tools) | HLE-Full | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| HLE | kimi-k2.5 | 30.1 (50.2 with tools) | HLE-Full | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |
| HLE | minimax-m2 | 12.5 without tools / 31.8 with tools | — | accuracy | 2025-10 | vendor_reported | https://github.com/MiniMax-AI/MiniMax-M2 |

## Limitations

All scores are vendor-reported and not independently verified. With-tools and without-tools results are not directly comparable; the setting is recorded per score.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high |
| Qwen3.8-2.4T-A95B model card | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | official | 2026-09-20 | high |
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
