# Video-MME

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://chinaaihub.com/benchmarks/video-mme",
      "name": "Video-MME",
      "url": "https://chinaaihub.com/benchmarks/video-mme",
      "mainEntityOfPage": "https://data.chinaaihub.com/benchmarks/video-mme/",
      "description": "Video understanding benchmark spanning various video durations and domains.",
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
          "name": "Benchmarks",
          "item": "https://data.chinaaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Video-MME",
          "item": "https://data.chinaaihub.com/benchmarks/video-mme/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/benchmarks/video-mme](https://chinaaihub.com/benchmarks/video-mme)

## Description

Video understanding benchmark spanning various video durations and domains.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| Video-MME | [kimi-k3](../models/kimi-k3.md) | 90.0 | with subtitles | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| Video-MME | kimi-k2.5 | 87.4 | — | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |

## Limitations

All scores are vendor-reported and not independently verified. Subtitle usage differs between evaluations.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
| Kimi K2.5 GitHub README | https://github.com/MoonshotAI/Kimi-K2.5 | official | 2026-09-20 | high |
