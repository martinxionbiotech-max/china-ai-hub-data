# DeepSeek API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://sinoaihub.com/api/deepseek",
      "name": "DeepSeek API",
      "url": "https://sinoaihub.com/api/deepseek",
      "mainEntityOfPage": "https://data.sinoaihub.com/apis/deepseek/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://sinoaihub.com/companies/deepseek",
        "url": "https://sinoaihub.com/companies/deepseek"
      },
      "documentation": "https://api-docs.deepseek.com/"
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
          "name": "DeepSeek API",
          "item": "https://data.sinoaihub.com/apis/deepseek/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/api/deepseek](https://sinoaihub.com/api/deepseek)

## Type

api


## Definition

DeepSeek API is DeepSeek's official API platform (endpoint https://api.deepseek.com).

## Key facts

- **Endpoint:** https://api.deepseek.com
- **Authentication:** Bearer API key (created at platform.deepseek.com/api_keys)
- **Capabilities:** streaming, tool calling, structured output, vision
- **Rate limits:** Concurrency: deepseek-flash 2500; deepseek-v4-pro 500 (per official pricing page)

## Provider

[deepseek](../companies/deepseek.md)

## Api Type

official

## Endpoint

https://api.deepseek.com

## Authentication

Bearer API key (created at platform.deepseek.com/api_keys)

## Streaming

Yes

## Function Calling

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
| [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 1048576 | 393216 |
| [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 1048576 | 393216 |

## Rate Limits

Concurrency: deepseek-flash 2500; deepseek-v4-pro 500 (per official pricing page)

## Cloud Providers

- DeepSeek Platform

## Pricing Ref

[deepseek](../pricing/deepseek.md)

## Documentation

https://api-docs.deepseek.com/

## Limitations

- Official docs publish concurrency limits only; no regional deployment breakdown as of 2026-09-27

## Verification Status

verified

## API Changes

| date | change | source | verification_date |
|---|---|---|---|
| 2026-08-13 | DeepSeek-V4-Pro GA (0813) shipped on the API | https://api-docs.deepseek.com/updates | 2026-09-29 |
| 2026-08-16 | Peak/off-peak pricing introduced (peak = 2x off-peak) | https://api-docs.deepseek.com/updates | 2026-09-29 |
| 2026-09-10 | V4-Pro deprecation announced then reversed the same day; V4.1-Flash released | https://api-docs.deepseek.com/updates | 2026-09-29 |

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-apis-deepseek-1 | DeepSeek API docs | https://api-docs.deepseek.com/ | Official documentation | — | 2026-09-20 | high | — |
| src-apis-deepseek-2 | DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | Official documentation | — | 2026-09-20 | high | — |
