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

## Type

model


## Definition

GLM-5.2 is a Zhipu AI model in the GLM-5 family: 744B total / 40B active (open weights, BF16/FP8); 1,048,576-token context window; 163,840 max output; open-weight; MIT (pure open, no regional limits per official model card) license; released 2026-06-16; status deprecated.

## Key facts

- **Architecture:** 744B total / 40B active (open weights, BF16/FP8)
- **Context window:** 1,048,576 tokens (max output 163,840)
- **Weights:** open; MIT (pure open, no regional limits per official model card) license
- **API pricing:** $1.4 input / $4.4 output per 1M tokens (USD)
- **Released:** 2026-06-16
- **Capabilities:** reasoning

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

## Verification Status

verified

## License Changes

No documented license changes on record as of 2026-09-29.

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-glm-5.2-1 | Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | Official documentation | — | 2026-09-20 | high | — |
| src-models-glm-5.2-2 | Z.ai pricing | https://docs.z.ai/guides/overview/pricing | Official documentation | — | 2026-09-20 | high | — |
| src-models-glm-5.2-3 | Z.ai release notes | https://docs.z.ai/release-notes/new-released | Official documentation | — | 2026-09-20 | high | — |
