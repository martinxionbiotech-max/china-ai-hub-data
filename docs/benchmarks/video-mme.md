# Video-MME

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/video-mme",
      "name": "Video-MME",
      "url": "https://sinoaihub.com/benchmarks/video-mme",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/video-mme/",
      "description": "Video understanding benchmark spanning various video durations and domains."

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
          "name": "Benchmarks",
          "item": "https://data.sinoaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Video-MME",
          "item": "https://data.sinoaihub.com/benchmarks/video-mme/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/video-mme](https://sinoaihub.com/benchmarks/video-mme)

## Key facts

- **Task type:** Video understanding (multimodal video analysis)
- **Dataset size:** 900 videos (254 hours total), 2,700 human-annotated question-answer pairs
- **Evaluation method:** Video QA with subtitles and audio modalities; duration-stratified evaluation
- **Scoring:** Accuracy (% correct); variants with/without subtitles
- **Recorded evaluations:** 3

## Description

Video understanding benchmark spanning various video durations and domains.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| Video-MME | [kimi-k3](../models/kimi-k3.md) | 90.0 | with subtitles | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| Video-MME | kimi-k2.5 | 87.4 | — | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |

## Methodology

**Task type:** Video understanding (multimodal video analysis)

**Dataset size:** 900 videos (254 hours total), 2,700 human-annotated question-answer pairs

**Evaluation method:** Video QA with subtitles and audio modalities; duration-stratified evaluation

**Scoring:** Accuracy (% correct); variants with/without subtitles

## Relevant Models

- [Kimi K3](../models/kimi-k3.md) — 90.0

## Limitations

All scores are vendor-reported and not independently verified. Subtitle usage differs between evaluations.

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
| Kimi K2.5 GitHub README | https://github.com/MoonshotAI/Kimi-K2.5 | official | 2026-09-20 | high |
