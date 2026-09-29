# Ark API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://sinoaihub.com/api/ark",
      "name": "Ark API",
      "url": "https://sinoaihub.com/api/ark",
      "mainEntityOfPage": "https://data.sinoaihub.com/apis/ark/",
      "provider": {
        "@type": "Organization",
        "name": "ByteDance",
        "@id": "https://sinoaihub.com/companies/bytedance",
        "url": "https://sinoaihub.com/companies/bytedance"
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
          "name": "Ark API",
          "item": "https://data.sinoaihub.com/apis/ark/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/api/ark](https://sinoaihub.com/api/ark)

## Type

api


## Definition

Ark API is ByteDance's official API platform (endpoint https://ark.cn-beijing.volces.com/api/v3).

## Key facts

- **Endpoint:** https://ark.cn-beijing.volces.com/api/v3
- **Authentication:** API key (Bearer token); AK/SK also documented for the chat API
- **Capabilities:** streaming, tool calling, structured output, vision
- **Rate limits:** Flagship Doubao models: 500 RPM / 1,000,000 TPM (as of 2026-09-20)

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

## Verification Status

verified

## API Changes

No documented API changes on record as of 2026-09-29.

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-apis-ark-1 | Ark product overview (base URL, auth) | https://docs.volcengine.com/docs/ark/product-overview?lang=zh | Official documentation | — | 2026-09-20 | high | — |
| src-apis-ark-2 | Ark Responses API reference | https://docs.volcengine.com/docs/ark/responses-api-text-generation?lang=zh | Official documentation | — | 2026-09-20 | high | — |
| src-apis-ark-3 | Ark Chat API reference | https://docs.volcengine.com/docs/ark/chat-api?lang=zh | Official documentation | — | 2026-09-20 | high | — |
