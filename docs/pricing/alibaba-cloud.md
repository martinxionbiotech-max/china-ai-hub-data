# alibaba-cloud

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "OfferCatalog",
      "@id": "https://chinaaihub.com/pricing/alibaba-cloud",
      "name": "Alibaba Cloud (Qwen) pricing",
      "url": "https://chinaaihub.com/pricing/alibaba-cloud",
      "mainEntityOfPage": "https://data.chinaaihub.com/pricing/alibaba-cloud/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://chinaaihub.com/companies/alibaba-cloud",
        "url": "https://chinaaihub.com/companies/alibaba-cloud"
      },
      "itemListElement": [
        {
          "@type": "Offer",
          "name": "Qwen3.8-Max — input price per 1M tokens",
          "price": 2.0,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "Qwen3.8-Max",
            "@id": "https://chinaaihub.com/models/qwen3.8-max",
            "url": "https://chinaaihub.com/models/qwen3.8-max"
          },
          "url": "https://data.chinaaihub.com/pricing/alibaba-cloud/",
          "description": "Output price per 1M tokens: $6.0"
        },
        {
          "@type": "Offer",
          "name": "Qwen3.8-Flash — input price per 1M tokens",
          "price": 0.15,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "Qwen3.8-Flash",
            "@id": "https://chinaaihub.com/models/qwen3.8-flash",
            "url": "https://chinaaihub.com/models/qwen3.8-flash"
          },
          "url": "https://data.chinaaihub.com/pricing/alibaba-cloud/",
          "description": "Output price per 1M tokens: $0.47"
        },
        {
          "@type": "Offer",
          "name": "qwen3.7-plus — input price per 1M tokens",
          "price": 0.4,
          "priceCurrency": "USD",
          "itemOffered": {
            "@type": "SoftwareApplication",
            "name": "qwen3.7-plus"
          },
          "url": "https://data.chinaaihub.com/pricing/alibaba-cloud/",
          "description": "Output price per 1M tokens: $1.6"
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
          "name": "alibaba-cloud",
          "item": "https://data.chinaaihub.com/pricing/alibaba-cloud/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/pricing/alibaba-cloud](https://chinaaihub.com/pricing/alibaba-cloud)

## Currency

USD

## Region

Singapore (International)

## Billing Mode

pay_as_you_go

## Models

| model | input_price_per_1m | output_price_per_1m | cached_input_price_per_1m | note | official_source |
|---|---|---|---|---|---|
| [qwen3.8-max](../models/qwen3.8-max.md) | 2.0 | 6.0 | 0.25 | Beijing and Global regions (HK/Frankfurt/US/Tokyo): $1.65 input / $4.951 output. Beijing batch: 50% off. Explicit cache creation $2.5, explicit cache read $0.17 (Singapore). Free quota: 1M tokens, 90 days (Singapore). | https://www.alibabacloud.com/help/en/model-studio/model-pricing |
| [qwen3.8-flash](../models/qwen3.8-flash.md) | 0.15 | 0.47 | 0.016 | Beijing and Global regions: $0.113 / $0.382. Explicit cache creation $0.2, read $0.016 (Singapore). Batch inference not supported. | https://www.alibabacloud.com/help/en/model-studio/model-pricing |
| qwen3.7-plus | 0.4 | 1.6 | — | Up to 256K context tier. 256K-1M tier: $1.2 / $4.8. Beijing: $0.276/$1.101 and $0.826/$3.301. Limited-time 20% console discount. Thinking billed same as output. | https://www.alibabacloud.com/help/en/model-studio/model-pricing |

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Model Studio — model pricing | https://www.alibabacloud.com/help/en/model-studio/model-pricing | official | 2026-09-20 | high |
