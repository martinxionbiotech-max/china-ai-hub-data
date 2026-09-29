# Z.ai API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://sinoaihub.com/api/zai",
      "name": "Z.ai API",
      "url": "https://sinoaihub.com/api/zai",
      "mainEntityOfPage": "https://data.sinoaihub.com/apis/zai/",
      "provider": {
        "@type": "Organization",
        "name": "Zhipu AI",
        "@id": "https://sinoaihub.com/companies/zhipu-ai",
        "url": "https://sinoaihub.com/companies/zhipu-ai"
      },
      "documentation": "https://docs.z.ai/"
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
          "name": "APIs",
          "item": "https://data.sinoaihub.com/apis/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Z.ai API",
          "item": "https://data.sinoaihub.com/apis/zai/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/api/zai](https://sinoaihub.com/api/zai)

## Definition

Z.ai API is Zhipu AI's official API platform (endpoint https://api.z.ai/api/paas/v4/chat/completions).

## Key facts

- **Endpoint:** https://api.z.ai/api/paas/v4/chat/completions
- **Authentication:** Bearer API key
- **Capabilities:** streaming, tool calling, vision

## Provider

[zhipu-ai](../companies/zhipu-ai.md)

## Api Type

official

## Endpoint

https://api.z.ai/api/paas/v4/chat/completions

## Authentication

Bearer API key

## Streaming

Yes

## Function Calling

Yes

## Tool Calling

Yes

## Vision

Yes

## Context Limits

| model | input_limit | output_limit |
|---|---|---|
| [glm-5.3](../models/glm-5.3.md) | 1048576 | 131072 |
| [glm-5.3-flash](../models/glm-5.3-flash.md) | 1048576 | 131072 |

## Regions

- international
- china

## Cloud Providers

- Z.ai
- BigModel

## Pricing Ref

[zhipu-ai](../pricing/zhipu-ai.md)

## Documentation

https://docs.z.ai/

## Limitations

- Rate limit documentation page not located (docs.z.ai paths 404) as of 2026-09-27

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Z.ai docs — Quick Start | https://docs.z.ai/ | official | 2026-09-20 | high |
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
