# MiniMax-M3

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://china-ai-hub.pages.dev/models/minimax-m3",
      "name": "MiniMax-M3",
      "url": "https://china-ai-hub.pages.dev/models/minimax-m3",
      "mainEntityOfPage": "https://china-ai-hub-data.pages.dev/models/minimax-m3/",
      "provider": {
        "@type": "Organization",
        "name": "MiniMax",
        "@id": "https://china-ai-hub.pages.dev/companies/minimax",
        "url": "https://china-ai-hub.pages.dev/companies/minimax"
      },
      "datePublished": "2026-06-01"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://china-ai-hub-data.pages.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Models",
          "item": "https://china-ai-hub-data.pages.dev/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "MiniMax-M3",
          "item": "https://china-ai-hub-data.pages.dev/models/minimax-m3/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [china-ai-hub.pages.dev/models/minimax-m3](https://china-ai-hub.pages.dev/models/minimax-m3)

## Provider

[minimax](../companies/minimax.md)

## Model Family

MiniMax M-series

## Release Date

2026-06-01

## Status

active

## Architecture

Mixture-of-Experts: ~428B total / ~23B activated; MiniMax Sparse Attention (MSA) with claimed 9x prefill and 15x decode speedup vs M2 at 1M context

## Parameter Information

- **total_parameters:** ~428B
- **active_parameters:** ~23B

## Context Window

1048576

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** Yes
- **video:** Yes
- **tool_calling:** Yes
- **agent_capability:** Yes

## Open Weight

Yes

## License

MiniMax Community License (custom): free for non-commercial use; commercial use requires prominent attribution 'Built with MiniMax M3' plus written authorization from MiniMax if yearly revenue exceeds US$20M (otherwise a one-time notice to api@minimax.io)

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

- **BrowseComp:** 83.5 (vendor_reported)
- **PostTrainBench:** 37.1 (vendor_reported)
- **SWE-bench Pro:** 59.0 (vendor_reported)
- **Terminal-Bench 2.1:** 66.0 (vendor_reported)
- **MCP Atlas:** 74.2 (vendor_reported)

## Related Agents

- [minimax-agent](../agents/minimax-agent.md)
- [minimax-code](../agents/minimax-code.md)
- [qoder](../agents/qoder.md)

## Related Technologies

- [ai-agents](https://china-ai-hub.pages.dev/technology/ai-agents/)
- [long-context](https://china-ai-hub.pages.dev/technology/long-context/)
- [multimodal-ai](https://china-ai-hub.pages.dev/technology/multimodal-ai/)
- [reasoning-models](https://china-ai-hub.pages.dev/technology/reasoning-models/)
- [tool-calling](https://china-ai-hub.pages.dev/technology/tool-calling/)

## Maximum Output

131072

## Known Limitations

- Maximum output of 131,072 tokens derived from official card evaluation config (128K max output tokens); the standalone API max-output ceiling is not separately published
- Max output tokens not publicly disclosed in official docs
- 1M context with at least 512K guaranteed usable; pricing splits at the 512K input boundary
- Thinking is disabled by default (thinking=adaptive enables it)
- Benchmarks vendor-reported; not independently verified

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence | published_date |
|---|---|---|---|---|---|
| MiniMax API platform — model overview (CN) | https://platform.minimaxi.com/docs/guides/models-intro | official | 2026-09-20 | high | — |
| MiniMax official M3 model page | https://www.minimax.cn/models/text/m3 | official | 2026-09-20 | high | — |
| MiniMax M3 official blog post | https://www.minimax.cn/blog/minimax-m3 | official | 2026-09-20 | high | 2026-06-01 |
| Hugging Face model card — MiniMax-M3 | https://huggingface.co/MiniMaxAI/MiniMax-M3 | official | 2026-09-20 | high | — |
