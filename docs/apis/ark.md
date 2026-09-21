# Ark API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://chinaaihub.com/api/ark",
      "name": "Ark API",
      "url": "https://chinaaihub.com/api/ark",
      "mainEntityOfPage": "https://data.chinaaihub.com/apis/ark/",
      "provider": {
        "@type": "Organization",
        "name": "ByteDance",
        "@id": "https://chinaaihub.com/companies/bytedance",
        "url": "https://chinaaihub.com/companies/bytedance"
      },
      "documentation": "https://docs.volcengine.com/docs/ark"
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
          "name": "APIs",
          "item": "https://data.chinaaihub.com/apis/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Ark API",
          "item": "https://data.chinaaihub.com/apis/ark/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/api/ark](https://chinaaihub.com/api/ark)

## Provider

[bytedance](../companies/bytedance.md)

## Api Type

official

## Endpoint

https://ark.cn-beijing.volces.com/api/v3

## Authentication

API key (Bearer token); AK/SK also documented for the chat API

## Streaming

Yes

## Tool Calling

Yes

## Structured Output

Yes

## Vision

Yes

## Context Limits

| model | input_limit | output_limit |
|---|---|---|
| [doubao-seed-2-1-pro](../models/doubao-seed-2-1-pro.md) | 1048576 | 262144 |
| [doubao-seed-evolving](../models/doubao-seed-evolving.md) | 1048576 | 262144 |
| [doubao-seed-2-1-turbo](../models/doubao-seed-2-1-turbo.md) | 262144 | 262144 |

## Rate Limits

Flagship Doubao models: 500 RPM / 1,000,000 TPM (as of 2026-09-20)

## Regions

- china

## Cloud Providers

- Volcengine

## Pricing Ref

[bytedance](../pricing/bytedance.md)

## Documentation

https://docs.volcengine.com/docs/ark

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Ark product overview (base URL, auth) | https://docs.volcengine.com/docs/ark/product-overview?lang=zh | official | 2026-09-20 | high |
| Ark Responses API reference | https://docs.volcengine.com/docs/ark/responses-api-text-generation?lang=zh | official | 2026-09-20 | high |
| Ark Chat API reference | https://docs.volcengine.com/docs/ark/chat-api?lang=zh | official | 2026-09-20 | high |
