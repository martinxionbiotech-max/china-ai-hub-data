# Kimi K2.6

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/kimi-k26",
      "name": "Kimi K2.6",
      "url": "https://sinoaihub.com/models/kimi-k26",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/kimi-k26/",
      "provider": {
        "@type": "Organization",
        "name": "Moonshot AI",
        "@id": "https://sinoaihub.com/companies/moonshot-ai",
        "url": "https://sinoaihub.com/companies/moonshot-ai"
      },
      "datePublished": "2026-04-20"
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
          "name": "Kimi K2.6",
          "item": "https://data.sinoaihub.com/models/kimi-k26/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/kimi-k26](https://sinoaihub.com/models/kimi-k26)

## Definition

Kimi K2.6 is a Moonshot AI model in the Kimi K2.6 family: Mixture-of-Experts (MoE): 1T total / 32B activated; 384 routed experts (8 selected + 1 shared); MLA attention, SwiGLU activation; 61 layers (1 dense); MoonViT vision encoder (400M); 262,144-token context window; 98,304 max output; open-weight; Modified MIT license; released 2026-04-20.

## Key facts

- **Architecture:** Mixture-of-Experts (MoE): 1T total / 32B activated; 384 routed experts (8 selected + 1 shared); MLA attention, SwiGLU activation; 61 layers (1 dense); MoonViT vision encoder (400M)
- **Context window:** 262,144 tokens (max output 98,304)
- **Weights:** open; Modified MIT license
- **API pricing:** $0.95 input / $4.0 output per 1M tokens (USD)
- **Released:** 2026-04-20
- **Capabilities:** reasoning, vision

## Provider

[moonshot-ai](../companies/moonshot-ai.md)

## Model Family

Kimi K2.6

## Release Date

2026-04-20

## Status

active

## Context Window

262144

## Capabilities

- **reasoning:** Yes
- **vision:** Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 0.95
- **output_price_per_1m:** 4.0
- **currency:** USD
- **pricing_ref:** moonshot-ai

## Official Api

Yes

## Cloud Providers

- Moonshot AI Platform

## Architecture

Mixture-of-Experts (MoE): 1T total / 32B activated; 384 routed experts (8 selected + 1 shared); MLA attention, SwiGLU activation; 61 layers (1 dense); MoonViT vision encoder (400M)

## Parameter Information

- **total_parameters:** 1T
- **active_parameters:** 32B

## Maximum Output

98304

## License

Modified MIT

## Open Weight

Yes

## Benchmark Results

- **HLE:** 36.4 (text-only, no tools) (vendor_reported)
- **HLE:** 55.5 (with tools) (vendor_reported)

## Known Limitations

- Maximum output of 98,304 tokens is the documented max generation length in the official model card's evaluation configuration

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi API platform — model list | https://platform.kimi.ai/docs/models.md | official | 2026-09-20 | high |
| Kimi API — pricing (chat) | https://platform.kimi.ai/docs/pricing/chat | official | 2026-09-20 | high |
