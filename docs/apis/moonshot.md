# Moonshot AI API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://chinaaihub.com/api/moonshot",
      "name": "Moonshot AI API",
      "url": "https://chinaaihub.com/api/moonshot",
      "mainEntityOfPage": "https://data.chinaaihub.com/apis/moonshot/",
      "provider": {
        "@type": "Organization",
        "name": "Moonshot AI",
        "@id": "https://chinaaihub.com/companies/moonshot-ai",
        "url": "https://chinaaihub.com/companies/moonshot-ai"
      },
      "documentation": "https://platform.kimi.ai/docs"
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
          "name": "Moonshot AI API",
          "item": "https://data.chinaaihub.com/apis/moonshot/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/api/moonshot](https://chinaaihub.com/api/moonshot)

## Provider

[moonshot-ai](../companies/moonshot-ai.md)

## Api Type

official

## Endpoint

https://api.moonshot.ai/v1

## Authentication

Bearer API key (MOONSHOT_API_KEY), managed in the platform console

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
| [kimi-k3](../models/kimi-k3.md) | 1048576 | 1048576 |
| [kimi-k2.7-code](../models/kimi-k2.7-code.md) | 262144 | — |
| [kimi-k2.7-code-highspeed](../models/kimi-k2.7-code-highspeed.md) | 262144 | — |
| [kimi-k2.6](../models/kimi-k2.6.md) | 262144 | — |

## Cloud Providers

- Moonshot AI Platform

## Pricing Ref

[moonshot-ai](../pricing/moonshot-ai.md)

## Documentation

https://platform.kimi.ai/docs

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi API overview | https://platform.kimi.ai/docs/api/overview.md | official | 2026-09-20 | high |
| Kimi API — Chat Completions spec | https://platform.kimi.ai/docs/api/chat.md | official | 2026-09-20 | high |
