# MiniMax-M3

> Canonical page on the main site: [chinaaihub.com/models/minimax-m3](https://chinaaihub.com/models/minimax-m3)

## Provider

minimax

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

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| BrowseComp | 83.5 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/models/text/m3 |
| PostTrainBench | 37.1 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/models/text/m3 |
| SWE-bench Pro | 59.0 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/blog/minimax-m3 |
| Terminal-Bench 2.1 | 66.0 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/blog/minimax-m3 |
| MCP Atlas | 74.2 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/blog/minimax-m3 |

## Known Limitations

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
