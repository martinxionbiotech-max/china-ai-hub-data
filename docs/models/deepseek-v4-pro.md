# DeepSeek-V4-Pro

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/deepseek-v4-pro",
      "name": "DeepSeek-V4-Pro",
      "url": "https://sinoaihub.com/models/deepseek-v4-pro",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/deepseek-v4-pro/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://sinoaihub.com/companies/deepseek",
        "url": "https://sinoaihub.com/companies/deepseek"
      }
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
          "name": "Models",
          "item": "https://data.sinoaihub.com/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "DeepSeek-V4-Pro",
          "item": "https://data.sinoaihub.com/models/deepseek-v4-pro/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/deepseek-v4-pro](https://sinoaihub.com/models/deepseek-v4-pro)

## Type

model


## Definition

DeepSeek-V4-Pro is a DeepSeek model in the DeepSeek-V4 family: MoE: 1.6T total / 49B active parameters; 1,048,576-token context window; 393,216 max output; open-weight; MIT license; released 2026-04-24 (V4 Preview) / 2026-08-13 (GA); status deprecated.

## Key facts

- **Architecture:** MoE: 1.6T total / 49B active parameters
- **Context window:** 1,048,576 tokens (max output 393,216)
- **Weights:** open; MIT license
- **API pricing:** $0.66 input / $1.98 output per 1M tokens (USD)
- **Released:** 2026-04-24 (V4 Preview) / 2026-08-13 (GA)
- **Capabilities:** reasoning, coding, tool calling

## Provider

[deepseek](../companies/deepseek.md)

## Model Family

DeepSeek-V4

## Version

0813

## Aliases

- deepseek-v4-pro-0813

## Release Date

2026-04-24 (V4 Preview) / 2026-08-13 (GA)

## Release History

| date | event | source | verification_date |
|---|---|---|---|
| 2026-04-24 | V4 Preview released — open weights, 1.6T/49B MoE, MIT license | https://www.deepseek.com/en/news/v4-preview/ | 2026-09-20 |
| 2026-08-13 | V4-Pro GA (0813 checkpoint) shipped on the API | https://api-docs.deepseek.com/updates | 2026-09-20 |
| 2026-09-10 | Deprecation announced, then reversed the same day — service continues with unchanged billing | https://api-docs.deepseek.com/updates | 2026-09-20 |

## Status

deprecated

## Architecture

MoE: 1.6T total / 49B active parameters

## Parameter Information

- **total_parameters:** 1.6T
- **active_parameters:** 49B

## Context Window

1048576

## Maximum Output

393216

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **math:** Yes
- **vision:** No
- **tool_calling:** Yes
- **function_calling:** Yes
- **structured_output:** Yes

## Open Weight

Yes

## License

MIT

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 0.66
- **output_price_per_1m:** 1.98
- **currency:** USD
- **pricing_ref:** deepseek

## Official Api

Yes

## Cloud Providers

- DeepSeek Platform

## Regions

- unknown

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| [HLE](../benchmarks/hle.md) | 42.7 (60.0 with tools) | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| [Terminal-Bench 2.1](../benchmarks/terminal-bench.md) | 87.9 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| [DeepSWE](../benchmarks/deepswe.md) | 62.7 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| Agents' Last Exam | 25.7 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |

## Related Agents

- [deepseek-harness](../agents/deepseek-harness.md)
- [qoder](../agents/qoder.md)

## Related Technologies

- [function-calling](https://sinoaihub.com/technology/function-calling/)
- [inference](https://sinoaihub.com/technology/inference/)
- [long-context](https://sinoaihub.com/technology/long-context/)
- [reasoning-models](https://sinoaihub.com/technology/reasoning-models/)
- [tool-calling](https://sinoaihub.com/technology/tool-calling/)

## Known Limitations

- Deprecation announced 2026-09-10: news page says V4-Pro requests will route to V4.1-Flash after 2026-09-14 until V4.1-Pro launches, but the same-day change log says V4-Pro API service continues with unchanged billing - the official pages conflict
- Vision not supported
- Open-weight HF checkpoint last modified 2026-06-22; unclear whether it matches the 0813 GA checkpoint
- Pricing is peak/off-peak: listed prices are off-peak; peak is 2x

## Verification Status

verified

## Model Versions

| version | date | source | verification_date |
|---|---|---|---|
| V4 Preview | 2026-04-24 | https://www.deepseek.com/en/news/v4-preview/ | 2026-09-29 |
| 0813 (GA) | 2026-08-13 | https://api-docs.deepseek.com/updates | 2026-09-29 |

## License Changes

No documented license changes on record as of 2026-09-29.

## Last Verified

2026-09-20

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-deepseek-v4-pro-1 | DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | Official documentation | — | 2026-09-20 | high | — |
| src-models-deepseek-v4-pro-2 | DeepSeek API Change Log | https://api-docs.deepseek.com/updates | Official documentation | — | 2026-09-20 | high | Conflicts with the same-day deprecation announcement (V4-Pro → V4.1-Flash routing) |
| src-models-deepseek-v4-pro-3 | DeepSeek-V4 Preview release | https://www.deepseek.com/en/news/v4-preview/ | Official | 2026-04-24 | 2026-09-20 | high | — |
| src-models-deepseek-v4-pro-4 | Hugging Face model card — DeepSeek-V4-Pro | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | Model card | — | 2026-09-20 | high | — |
