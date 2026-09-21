# Qwen3.8-2.4T-A95B

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://chinaaihub.com/models/qwen3.8-2.4t-a95b",
      "name": "Qwen3.8-2.4T-A95B",
      "url": "https://chinaaihub.com/models/qwen3.8-2.4t-a95b",
      "mainEntityOfPage": "https://data.chinaaihub.com/models/qwen3.8-2.4t-a95b/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://chinaaihub.com/companies/alibaba-cloud",
        "url": "https://chinaaihub.com/companies/alibaba-cloud"
      },
      "datePublished": "2026-08-12"
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
          "name": "Qwen3.8-2.4T-A95B",
          "item": "https://data.chinaaihub.com/models/qwen3.8-2.4t-a95b/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/models/qwen3.8-2.4t-a95b](https://chinaaihub.com/models/qwen3.8-2.4t-a95b)

## Provider

[alibaba-cloud](../companies/alibaba-cloud.md)

## Model Family

Qwen3.8

## Release Date

2026-08-12

## Status

active

## Architecture

2.4T-parameter MoE, 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, Gated DeltaNet + Gated Attention hybrid

## Parameter Information

- **total_parameters:** 2.4T
- **active_parameters:** 95B

## Context Window

262144

## Capabilities

- **reasoning:** Yes
- **vision:** No

## Open Weight

Yes

## License

Qwen3.8-Max License (custom MIT-style: unrestricted use/copy/modify/sell, but products with >100M MAU or >US$20M/month revenue must display the model name; Model-as-a-Service or AI Work Assistant businesses with >US$50M/12-month revenue need a separate license from Qwen)

## Self Hosting

Yes

## Api Available

No

## Official Api

No

## Known Limitations

- Text-only input; thinking cannot be disabled; reasoning_effort xhigh/medium/low
- Native context 262,144 tokens, extensible to 1,010,000
- Not the same product as the qwen3.8-max API model (which adds vision/video input, non-thinking mode and 1M default context)

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Hugging Face model card — Qwen3.8-2.4T-A95B | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | official | 2026-09-20 | high |
| Qwen3.8 repository README | https://github.com/QwenLM/Qwen3.8 | official | 2026-09-20 | high |
| Qwen3.8-2.4T-A95B license file | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE | official | 2026-09-20 | high |
