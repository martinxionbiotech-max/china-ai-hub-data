# DeepSeek API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "OfferCatalog",
      "@id": "https://sinoaihub.com/pricing/deepseek",
      "name": "DeepSeek pricing",
      "url": "https://sinoaihub.com/pricing/deepseek",
      "mainEntityOfPage": "https://data.sinoaihub.com/pricing/deepseek/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://sinoaihub.com/companies/deepseek",
        "url": "https://sinoaihub.com/companies/deepseek"
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
            "@id": "https://sinoaihub.com/models/deepseek-v4-1-flash",
            "url": "https://sinoaihub.com/models/deepseek-v4-1-flash"
          },
          "url": "https://data.sinoaihub.com/pricing/deepseek/",
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
            "@id": "https://sinoaihub.com/models/deepseek-v4-pro",
            "url": "https://sinoaihub.com/models/deepseek-v4-pro"
          },
          "url": "https://data.sinoaihub.com/pricing/deepseek/",
          "description": "Output price per 1M tokens: $1.98"
        }
      ]

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
          "name": "Pricing",
          "item": "https://data.sinoaihub.com/pricing/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "DeepSeek API",
          "item": "https://data.sinoaihub.com/pricing/deepseek/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/pricing/deepseek](https://sinoaihub.com/pricing/deepseek)

## Type

pricing


## Definition

DeepSeek API pricing in USD, pay as you go.

## Key facts

- **Currency:** USD
- **Billing:** pay as you go
- **Models priced:** 2
- **Price history:** documented

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

| model | field | old | new | effective | source | verification_date |
|---|---|---|---|---|---|---|
| deepseek-v4-pro | billing_structure | Flat pricing | Peak/off-peak pricing; off-peak = 50% of peak | 2026-08-16 | https://api-docs.deepseek.com/updates | 2026-09-20 |
| deepseek-v4-1-flash | api_pricing | V4-Flash list pricing (model retired) | Reduced V4.1-Flash pricing | 2026-09-10 | https://api-docs.deepseek.com/updates | 2026-09-20 |

## Verification Status

verified

## Last Verified

2026-09-20

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-pricing-deepseek-1 | DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | Official documentation | — | 2026-09-20 | high | — |
| src-pricing-deepseek-2 | DeepSeek API Change Log | https://api-docs.deepseek.com/updates | Official documentation | — | 2026-09-20 | high | — |
| src-pricing-deepseek-3 | DeepSeek-V4.1-Flash release announcement | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ | Official | 2026-09-10 | 2026-09-20 | high | — |
