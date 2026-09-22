# DeepSeek API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "OfferCatalog",
      "@id": "https://chinaaihub.com/pricing/deepseek",
      "name": "DeepSeek pricing",
      "url": "https://chinaaihub.com/pricing/deepseek",
      "mainEntityOfPage": "https://data.chinaaihub.com/pricing/deepseek/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://chinaaihub.com/companies/deepseek",
        "url": "https://chinaaihub.com/companies/deepseek"
      },
      "itemListElement": [
        {
          "@type": "Offer",
          "name": "DeepSeek-V4.1-Flash — input price per 1M tokens",
          "price": 0.15,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "DeepSeek-V4.1-Flash",
            "@id": "https://chinaaihub.com/models/deepseek-v4-1-flash",
            "url": "https://chinaaihub.com/models/deepseek-v4-1-flash"
          },
          "url": "https://data.chinaaihub.com/pricing/deepseek/",
          "description": "Output price per 1M tokens: $0.6"
        },
        {
          "@type": "Offer",
          "name": "DeepSeek-V4-Pro — input price per 1M tokens",
          "price": 0.66,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "DeepSeek-V4-Pro",
            "@id": "https://chinaaihub.com/models/deepseek-v4-pro",
            "url": "https://chinaaihub.com/models/deepseek-v4-pro"
          },
          "url": "https://data.chinaaihub.com/pricing/deepseek/",
          "description": "Output price per 1M tokens: $1.98"
        }
      ],
      "dateModified": "2026-09-20"
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
          "name": "Pricing",
          "item": "https://data.chinaaihub.com/pricing/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "DeepSeek API",
          "item": "https://data.chinaaihub.com/pricing/deepseek/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/pricing/deepseek](https://chinaaihub.com/pricing/deepseek)

## Currency

USD

## Billing Mode

pay_as_you_go

## Models

| model | input_price_per_1m | output_price_per_1m | cached_input_price_per_1m | note | official_source |
|---|---|---|---|---|---|
| [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 0.15 | 0.6 | 0.003 | Off-peak rates (all times except 01:00-04:00 and 06:00-10:00 UTC Mon-Fri). Peak = 2x: $0.30 input / $1.20 output / $0.006 cache hit. Concurrency limit 2500. No batch pricing listed. | https://api-docs.deepseek.com/quick_start/pricing |
| [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 0.66 | 1.98 | 0.022 | Off-peak rates; peak = 2x: $1.32 input / $3.96 output / $0.044 cache hit. Concurrency limit 500. Deprecation announced 2026-09-10 (service continuation per change log). | https://api-docs.deepseek.com/quick_start/pricing |

## Price History

| model | field | old | new | effective | source |
|---|---|---|---|---|---|
| deepseek-v4-pro | billing_structure | Flat pricing | Peak/off-peak pricing; off-peak = 50% of peak | 2026-08-16 | https://api-docs.deepseek.com/updates |
| deepseek-v4-1-flash | api_pricing | V4-Flash list pricing (model retired) | Reduced V4.1-Flash pricing | 2026-09-10 | https://api-docs.deepseek.com/updates |

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence | published_date |
|---|---|---|---|---|---|
| DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | official | 2026-09-20 | high | — |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high | — |
| DeepSeek-V4.1-Flash release announcement | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ | official | 2026-09-20 | high | 2026-09-10 |
