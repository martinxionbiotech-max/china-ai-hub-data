# DeepSeek API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://chinaaihub.com/api/deepseek",
      "name": "DeepSeek API",
      "url": "https://chinaaihub.com/api/deepseek",
      "mainEntityOfPage": "https://data.chinaaihub.com/apis/deepseek/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://chinaaihub.com/companies/deepseek",
        "url": "https://chinaaihub.com/companies/deepseek"
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
          "name": "DeepSeek API",
          "item": "https://data.chinaaihub.com/apis/deepseek/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/api/deepseek](https://chinaaihub.com/api/deepseek)

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

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API docs | https://api-docs.deepseek.com/ | official | 2026-09-20 | high |
| DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | official | 2026-09-20 | high |
