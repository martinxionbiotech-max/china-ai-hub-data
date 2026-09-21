# GLM-5.3-Flash

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://chinaaihub.com/models/glm-5.3-flash",
      "name": "GLM-5.3-Flash",
      "url": "https://chinaaihub.com/models/glm-5.3-flash",
      "mainEntityOfPage": "https://data.chinaaihub.com/models/glm-5.3-flash/",
      "provider": {
        "@type": "Organization",
        "name": "Zhipu AI",
        "@id": "https://chinaaihub.com/companies/zhipu-ai",
        "url": "https://chinaaihub.com/companies/zhipu-ai"
      },
      "datePublished": "2026-08-26"
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
          "name": "Models",
          "item": "https://data.chinaaihub.com/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "GLM-5.3-Flash",
          "item": "https://data.chinaaihub.com/models/glm-5.3-flash/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/models/glm-5.3-flash](https://chinaaihub.com/models/glm-5.3-flash)

## Provider

[zhipu-ai](../companies/zhipu-ai.md)

## Model Family

GLM-5.3-Flash

## Version

FlashX

## Aliases

- glm-5.3-flashx
- GLM-5.3-FlashX

## Release Date

2026-08-26

## Status

active

## Architecture

320B total / 18B active; first open-source frontier model combining sparse + linear attention; mHC hyper-connections; 30T-token multimodal pre-training corpus

## Parameter Information

- **total_parameters:** 320B
- **active_parameters:** 18B

## Context Window

1048576

## Maximum Output

131072

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** Yes
- **video:** Yes
- **computer_use:** Yes
- **agent_capability:** Yes

## Open Weight

Yes

## License

Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse)

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 0.15
- **output_price_per_1m:** 0.5
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
| Artificial Analysis Intelligence Index v4.1.1 | 57 | index score | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash |
| [DeepSWE v1.1](../benchmarks/deepswe.md) | 63.4 | accuracy | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash |
| [AutomationBench](../benchmarks/automationbench.md) | 48.8 | accuracy | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash |

## Known Limitations

- FlashX tier not yet available on the GLM Coding Plan (pay-as-you-go only)
- Reasoning always enabled; cannot be disabled
- Z.ai Code Bench is a private in-house benchmark
- Benchmarks vendor-reported; not independently verified

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Z.ai docs — GLM-5.3-Flash model page | https://docs.z.ai/guides/vlm/glm-5.3-flash | official | 2026-09-20 | high |
| Z.ai pricing | https://docs.z.ai/guides/overview/pricing | official | 2026-09-20 | high |
| GLM-5 GitHub repository | https://github.com/zai-org/GLM-5 | official | 2026-09-20 | high |
