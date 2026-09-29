# MiniMax API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "OfferCatalog",
      "@id": "https://sinoaihub.com/pricing/minimax",
      "name": "MiniMax pricing",
      "url": "https://sinoaihub.com/pricing/minimax",
      "mainEntityOfPage": "https://data.sinoaihub.com/pricing/minimax/",
      "provider": {
        "@type": "Organization",
        "name": "MiniMax",
        "@id": "https://sinoaihub.com/companies/minimax",
        "url": "https://sinoaihub.com/companies/minimax"
      },
      "itemListElement": [
        {
          "@type": "Offer",
          "name": "MiniMax-M3 — input price per 1M tokens",
          "price": 0.3,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "MiniMax-M3",
            "@id": "https://sinoaihub.com/models/minimax-m3",
            "url": "https://sinoaihub.com/models/minimax-m3"
          },
          "url": "https://data.sinoaihub.com/pricing/minimax/",
          "description": "Output price per 1M tokens: $1.2"
        },
        {
          "@type": "Offer",
          "name": "MiniMax-M2.7 — input price per 1M tokens",
          "price": 0.3,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "MiniMax-M2.7",
            "@id": "https://sinoaihub.com/models/minimax-m27",
            "url": "https://sinoaihub.com/models/minimax-m27"
          },
          "url": "https://data.sinoaihub.com/pricing/minimax/",
          "description": "Output price per 1M tokens: $1.2"
        },
        {
          "@type": "Offer",
          "name": "MiniMax-M2.7-Highspeed — input price per 1M tokens",
          "price": 0.6,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "MiniMax-M2.7-Highspeed",
            "@id": "https://sinoaihub.com/models/minimax-m27-highspeed",
            "url": "https://sinoaihub.com/models/minimax-m27-highspeed"
          },
          "url": "https://data.sinoaihub.com/pricing/minimax/",
          "description": "Output price per 1M tokens: $2.4"
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
          "name": "MiniMax API",
          "item": "https://data.sinoaihub.com/pricing/minimax/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/pricing/minimax](https://sinoaihub.com/pricing/minimax)

## Definition

MiniMax API pricing in USD, pay as you go.

## Key facts

- **Currency:** USD
- **Region:** International
- **Billing:** pay as you go
- **Models priced:** 3
- **Price history:** documented

## Currency

USD

## Region

International

## Billing Mode

pay_as_you_go

## Models

| model | input_price_per_1m | output_price_per_1m | cached_input_price_per_1m | note | official_source |
|---|---|---|---|---|---|
| [minimax-m3](../models/minimax-m3.md) | 0.3 | 1.2 | 0.06 | Standard tier, <=512K input (permanent 50% off vs list $0.60/$2.40). >512K input: $0.60/$2.40, cache $0.12. Priority tier (service_tier=priority) = 1.5x. China platform: ¥2.1 / ¥8.4 (<=512K), ¥4.2 / ¥16.8 (>512K). | https://platform.minimax.io/docs/guides/pricing-paygo.md |
| [minimax-m2.7](../models/minimax-m2.7.md) | 0.3 | 1.2 | 0.06 | Cache write $0.375 per 1M tokens. China platform: ¥2.1 / ¥8.4. | https://platform.minimax.io/docs/guides/pricing-paygo.md |
| [minimax-m2.7-highspeed](../models/minimax-m2.7-highspeed.md) | 0.6 | 2.4 | 0.06 | Cache write $0.375 per 1M tokens. China platform: ¥4.2 / ¥16.8. | https://platform.minimax.io/docs/guides/pricing-paygo.md |

## Price History

| model | field | old | new | effective | source | verification_date |
|---|---|---|---|---|---|---|
| minimax-m3 | input_price_per_1m | 0.6 | 0.3 | — | https://platform.minimax.io/docs/guides/pricing-paygo | 2026-09-20 |
| minimax-m3 | output_price_per_1m | 2.4 | 1.2 | — | https://platform.minimax.io/docs/guides/pricing-paygo | 2026-09-20 |
| minimax-m3 | cached_input_price_per_1m | 0.12 | 0.06 | — | https://platform.minimax.io/docs/guides/pricing-paygo | 2026-09-20 |

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| MiniMax API platform — pay-as-you-go pricing (intl) | https://platform.minimax.io/docs/guides/pricing-paygo.md | official | 2026-09-20 | high |
| MiniMax API platform — pay-as-you-go pricing (CN) | https://platform.minimaxi.com/docs/guides/pricing-paygo.md | official | 2026-09-20 | high |
