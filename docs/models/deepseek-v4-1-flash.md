# DeepSeek-V4.1-Flash

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/deepseek-v4-1-flash",
      "name": "DeepSeek-V4.1-Flash",
      "url": "https://sinoaihub.com/models/deepseek-v4-1-flash",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/deepseek-v4-1-flash/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://sinoaihub.com/companies/deepseek",
        "url": "https://sinoaihub.com/companies/deepseek"
      },
      "datePublished": "2026-09-10"
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
          "name": "DeepSeek-V4.1-Flash",
          "item": "https://data.sinoaihub.com/models/deepseek-v4-1-flash/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/deepseek-v4-1-flash](https://sinoaihub.com/models/deepseek-v4-1-flash)

## Definition

DeepSeek-V4.1-Flash is a DeepSeek model in the DeepSeek-V4.1 family: 552B-parameter MoE; Causal Encoder-Decoder; 8B active parameters on input, 16B on output; 1,048,576-token context window; 393,216 max output; open-weight; MIT license; released 2026-09-10.

## Key facts

- **Architecture:** 552B-parameter MoE; Causal Encoder-Decoder; 8B active parameters on input, 16B on output
- **Context window:** 1,048,576 tokens (max output 393,216)
- **Weights:** open; MIT license
- **API pricing:** $0.15 input / $0.6 output per 1M tokens (USD)
- **Released:** 2026-09-10
- **Capabilities:** reasoning, coding, vision, tool calling

## Provider

[deepseek](../companies/deepseek.md)

## Model Family

DeepSeek-V4.1

## Release Date

2026-09-10

## Release History

| date | event | source | verification_date |
|---|---|---|---|
| 2026-09-10 | V4.1-Flash released — 552B MoE (8B/16B active), multimodal, MIT weights; V4-Flash and V4-Flash-Vision-Exp retired | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ | 2026-09-20 |

## Status

active

## Architecture

552B-parameter MoE; Causal Encoder-Decoder; 8B active parameters on input, 16B on output

## Parameter Information

- **total_parameters:** 552B
- **active_parameters:** 8B (input) / 16B (output)

## Context Window

1048576

## Maximum Output

393216

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** Yes
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

- **input_price_per_1m:** 0.15
- **output_price_per_1m:** 0.6
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
| [GPQA Diamond](../benchmarks/gpqa-diamond.md) | 90.9 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| [HLE](../benchmarks/hle.md) | 36.8 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| Codeforces | 3471 | rating | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| [Terminal-Bench 2.1](../benchmarks/terminal-bench.md) | 90.6 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| [DeepSWE v1.1](../benchmarks/deepswe.md) | 74.2 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |

## Related Agents

- [deepseek-harness](../agents/deepseek-harness.md)
- [qoder](../agents/qoder.md)

## Related Technologies

- [function-calling](https://sinoaihub.com/technology/function-calling/)
- [inference](https://sinoaihub.com/technology/inference/)
- [rag](https://sinoaihub.com/technology/rag/)
- [reasoning-models](https://sinoaihub.com/technology/reasoning-models/)
- [tool-calling](https://sinoaihub.com/technology/tool-calling/)

## Known Limitations

- Pricing is peak/off-peak: listed prices are off-peak; peak (01:00-04:00 and 06:00-10:00 UTC, Mon-Fri) is 2x
- Benchmarks are vendor-reported using DeepSeek Harness (minimal mode, max effort); not independently verified
- HLE score is on the pure-text subset (39.1 on that subset; 36.8 full)
- Legacy API names deepseek-v4-flash and deepseek-v4-flash-vision-exp route to V4.1-Flash

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence | published_date |
|---|---|---|---|---|---|
| DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | official | 2026-09-20 | high | — |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high | — |
| DeepSeek-V4.1-Flash release announcement | https://www.deepseek.com/en/news/deepseek-v4-1-flash/ | official | 2026-09-20 | high | 2026-09-10 |
| Hugging Face model card — DeepSeek-V4.1-Flash | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | official | 2026-09-20 | high | — |
