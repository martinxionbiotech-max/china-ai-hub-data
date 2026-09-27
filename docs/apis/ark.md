# Ark API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://china-ai-hub.pages.dev/api/ark",
      "name": "Ark API",
      "url": "https://china-ai-hub.pages.dev/api/ark",
      "mainEntityOfPage": "https://china-ai-hub-data.pages.dev/apis/ark/",
      "provider": {
        "@type": "Organization",
        "name": "ByteDance",
        "@id": "https://china-ai-hub.pages.dev/companies/bytedance",
        "url": "https://china-ai-hub.pages.dev/companies/bytedance"
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
          "item": "https://china-ai-hub-data.pages.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "APIs",
          "item": "https://china-ai-hub-data.pages.dev/apis/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Ark API",
          "item": "https://china-ai-hub-data.pages.dev/apis/ark/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [china-ai-hub.pages.dev/api/ark](https://china-ai-hub.pages.dev/api/ark)

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

## Limitations

- Function calling support for Ark-hosted models is documented per-model, not platform-wide; not extracted as of 2026-09-27

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Ark product overview (base URL, auth) | https://docs.volcengine.com/docs/ark/product-overview?lang=zh | official | 2026-09-20 | high |
| Ark Responses API reference | https://docs.volcengine.com/docs/ark/responses-api-text-generation?lang=zh | official | 2026-09-20 | high |
| Ark Chat API reference | https://docs.volcengine.com/docs/ark/chat-api?lang=zh | official | 2026-09-20 | high |
