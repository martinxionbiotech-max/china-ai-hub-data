# MiniMax API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://sinoaihub.com/api/minimax",
      "name": "MiniMax API",
      "url": "https://sinoaihub.com/api/minimax",
      "mainEntityOfPage": "https://data.sinoaihub.com/apis/minimax/",
      "provider": {
        "@type": "Organization",
        "name": "MiniMax",
        "@id": "https://sinoaihub.com/companies/minimax",
        "url": "https://sinoaihub.com/companies/minimax"
      },
      "documentation": "https://platform.minimax.io/docs"
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
          "name": "MiniMax API",
          "item": "https://data.sinoaihub.com/apis/minimax/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/api/minimax](https://sinoaihub.com/api/minimax)

## Provider

[minimax](../companies/minimax.md)

## Api Type

official

## Endpoint

https://api.minimax.io/anthropic

## Authentication

API key (Bearer-style, passed via ANTHROPIC_API_KEY), managed in the platform console

## Streaming

Yes

## Function Calling

Yes

## Tool Calling

Yes

## Vision

Yes

## Context Limits

| model | input_limit |
|---|---|
| [minimax-m3](../models/minimax-m3.md) | 1048576 |
| [minimax-m2.7](../models/minimax-m2.7.md) | 204800 |
| [minimax-m2.7-highspeed](../models/minimax-m2.7-highspeed.md) | 204800 |

## Regions

- international
- china

## Cloud Providers

- MiniMax Platform

## Pricing Ref

[minimax](../pricing/minimax.md)

## Documentation

https://platform.minimax.io/docs

## Limitations

- Rate limits published on a JS-rendered docs page; structured_output not publicly documented as of 2026-09-27

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| MiniMax API — Anthropic-compatible API (intl) | https://platform.minimax.io/docs/api-reference/text-anthropic-api.md | official | 2026-09-20 | high |
| MiniMax API platform — pay-as-you-go pricing (intl) | https://platform.minimax.io/docs/guides/pricing-paygo.md | official | 2026-09-20 | high |
