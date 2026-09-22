# MiniMax-M2.7

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://chinaaihub.com/models/minimax-m27",
      "name": "MiniMax-M2.7",
      "url": "https://chinaaihub.com/models/minimax-m27",
      "mainEntityOfPage": "https://data.chinaaihub.com/models/minimax-m27/",
      "provider": {
        "@type": "Organization",
        "name": "MiniMax",
        "@id": "https://chinaaihub.com/companies/minimax",
        "url": "https://chinaaihub.com/companies/minimax"
      },
      "datePublished": "2026-03-18"
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
          "name": "Models",
          "item": "https://data.chinaaihub.com/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "MiniMax-M2.7",
          "item": "https://data.chinaaihub.com/models/minimax-m27/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/models/minimax-m27](https://chinaaihub.com/models/minimax-m27)

## Provider

[minimax](../companies/minimax.md)

## Model Family

MiniMax M2.7

## Release Date

2026-03-18

## Status

active

## Context Window

204800

## Capabilities

- **reasoning:** Yes
- **tool_calling:** Yes
- **vision:** No

## Open Weight

Yes

## License

Custom NON-COMMERCIAL license (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution 'Built with MiniMax M2.7' required)

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 0.3
- **output_price_per_1m:** 1.2
- **currency:** USD
- **pricing_ref:** minimax

## Official Api

Yes

## Cloud Providers

- MiniMax Platform

## Regions

- china
- international

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| GDPval-AA ELO | 1495 | ELO | 2026-03-18 | vendor_reported | https://huggingface.co/MiniMaxAI/MiniMax-M2.7 |
| MM Claw end-to-end benchmark | 62.7 | accuracy | 2026-03-18 | vendor_reported | https://huggingface.co/MiniMaxAI/MiniMax-M2.7 |

## Known Limitations

- Text-only input; interleaved thinking always on (cannot be disabled via API)
- Parameter count and max output tokens not publicly disclosed
- Must echo full assistant content (thinking blocks) back in multi-turn history
- Benchmarks vendor-reported; not independently verified

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| MiniMax API platform — model overview (CN) | https://platform.minimaxi.com/docs/guides/models-intro | official | 2026-09-20 | high |
| MiniMax official release notes | https://platform.minimaxi.com/docs/release-notes/models.md | official | 2026-09-20 | high |
| Hugging Face model card — MiniMax-M2.7 | https://huggingface.co/MiniMaxAI/MiniMax-M2.7 | official | 2026-09-20 | high |
