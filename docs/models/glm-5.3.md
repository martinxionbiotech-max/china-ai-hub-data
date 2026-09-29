# GLM-5.3

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/glm-53",
      "name": "GLM-5.3",
      "url": "https://sinoaihub.com/models/glm-53",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/glm-53/",
      "provider": {
        "@type": "Organization",
        "name": "Zhipu AI",
        "@id": "https://sinoaihub.com/companies/zhipu-ai",
        "url": "https://sinoaihub.com/companies/zhipu-ai"
      },
      "datePublished": "2026-08-18"
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
          "name": "Models",
          "item": "https://data.sinoaihub.com/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "GLM-5.3",
          "item": "https://data.sinoaihub.com/models/glm-53/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/glm-53](https://sinoaihub.com/models/glm-53)

## Definition

GLM-5.3 is a Zhipu AI model in the GLM-5 family: 744B total / 40B active (open-weight FP8); same base model as GLM-5.2 with post-training gains; 1,048,576-token context window; 131,072 max output; open-weight; Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse) license; released 2026-08-18.

## Key facts

- **Architecture:** 744B total / 40B active (open-weight FP8); same base model as GLM-5.2 with post-training gains
- **Context window:** 1,048,576 tokens (max output 131,072)
- **Weights:** open; Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse) license
- **API pricing:** $1.4 input / $4.4 output per 1M tokens (USD)
- **Released:** 2026-08-18
- **Capabilities:** reasoning, coding

## Provider

[zhipu-ai](../companies/zhipu-ai.md)

## Model Family

GLM-5

## Release Date

2026-08-18

## Status

active

## Architecture

744B total / 40B active (open-weight FP8); same base model as GLM-5.2 with post-training gains

## Parameter Information

- **total_parameters:** 744B
- **active_parameters:** 40B
- **parameter_precision:** FP8 (BF16 variant also released)

## Context Window

1048576

## Maximum Output

131072

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** No

## Open Weight

Yes

## License

Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse)

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 1.4
- **output_price_per_1m:** 4.4
- **currency:** USD
- **pricing_ref:** zhipu-ai

## Official Api

Yes

## Cloud Providers

- Z.ai
- BigModel

## Regions

- international
- china

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| [Terminal-Bench 3.0](../benchmarks/terminal-bench.md) | 28.3 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| [DeepSWE v1.1](../benchmarks/deepswe.md) | 66.9 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| Agents' Last Exam (CLI) | 28.5 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| [CyberGym](../benchmarks/cybergym.md) | 84.5 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |

## Known Limitations

- Text-only input
- Reasoning always enabled (low/high/max, default max); cannot be disabled
- Z.ai Code Bench is a private in-house benchmark
- Benchmarks vendor-reported; not independently verified

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
| Z.ai pricing | https://docs.z.ai/guides/overview/pricing | official | 2026-09-20 | high |
| GLM-5 GitHub repository | https://github.com/zai-org/GLM-5 | official | 2026-09-20 | high |
