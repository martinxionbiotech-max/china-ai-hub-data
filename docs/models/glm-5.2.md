# GLM-5.2

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/glm-52",
      "name": "GLM-5.2",
      "url": "https://sinoaihub.com/models/glm-52",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/glm-52/",
      "provider": {
        "@type": "Organization",
        "name": "Zhipu AI",
        "@id": "https://sinoaihub.com/companies/zhipu-ai",
        "url": "https://sinoaihub.com/companies/zhipu-ai"
      },
      "datePublished": "2026-06-16"
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
          "name": "GLM-5.2",
          "item": "https://data.sinoaihub.com/models/glm-52/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/glm-52](https://sinoaihub.com/models/glm-52)

## Provider

[zhipu-ai](../companies/zhipu-ai.md)

## Model Family

GLM-5

## Release Date

2026-06-16

## Status

deprecated

## Architecture

744B total / 40B active (open weights, BF16/FP8)

## Parameter Information

- **total_parameters:** 744B
- **active_parameters:** 40B

## Context Window

1048576

## Capabilities

- **reasoning:** Yes
- **vision:** No

## Open Weight

Yes

## License

MIT (pure open, no regional limits per official model card)

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

## Maximum Output

163840

## Benchmark Results

- **HLE:** 40.5 (text-only) (vendor_reported)
- **HLE:** 54.7 (w/ tools) (vendor_reported)
- **SWE-bench Pro:** 62.1 (vendor_reported)

## Known Limitations

- Superseded by GLM-5.3 (same base model, improved post-training) but still listed on the API pricing page at the same price
- Text-only input; reasoning supports high/max only

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
| Z.ai pricing | https://docs.z.ai/guides/overview/pricing | official | 2026-09-20 | high |
| Z.ai release notes | https://docs.z.ai/release-notes/new-released | official | 2026-09-20 | high |
