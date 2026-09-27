# HLE

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://china-ai-hub.pages.dev/benchmarks/hle",
      "name": "HLE",
      "url": "https://china-ai-hub.pages.dev/benchmarks/hle",
      "mainEntityOfPage": "https://china-ai-hub-data.pages.dev/benchmarks/hle/",
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
          "item": "https://china-ai-hub-data.pages.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Benchmarks",
          "item": "https://china-ai-hub-data.pages.dev/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "HLE",
          "item": "https://china-ai-hub-data.pages.dev/benchmarks/hle/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [china-ai-hub.pages.dev/benchmarks/hle](https://china-ai-hub.pages.dev/benchmarks/hle)

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

## Methodology

**Task type:** Expert-level academic Q&A across mathematics, humanities and natural sciences

**Dataset size:** 2,500 questions across dozens of subjects

**Evaluation method:** Multiple-choice and short-answer questions developed by subject-matter experts; multimodal; suitable for automated grading

**Scoring:** Accuracy (% correct); frequently reported with and without tool access

**Contamination notes:** Dataset includes a canary string (hle:3r2s:26b5c67b-...) to aid model builders in filtering the dataset from future training.

## Relevant Models

- [Qwen3.8-Max
provider: alibaba-cloud
model_family: Qwen3.8
version: ](../models/qwen38-max
provider:-alibaba-cloud
model_family:-qwen38
version:-.md) — 43.6 (56.2 with tools)
- [DeepSeek-V4.1-Flash
provider: deepseek
model_family: DeepSeek-V4.1
release_date: ](../models/deepseek-v41-flash
provider:-deepseek
model_family:-deepseek-v41
release_date:-.md) — 36.8
- [Kimi K3
provider: moonshot-ai
model_family: Kimi K-series
release_date: ](../models/kimi-k3
provider:-moonshot-ai
model_family:-kimi-k-series
release_date:-.md) — 43.5 (56.0 with tools)
- [DeepSeek-V4-Pro
provider: deepseek
model_family: DeepSeek-V4
version: ](../models/deepseek-v4-pro
provider:-deepseek
model_family:-deepseek-v4
version:-.md) — 42.7 (60.0 with tools)

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
