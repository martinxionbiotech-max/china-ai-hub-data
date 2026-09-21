# DeepSeek-V4.1-Flash

> Canonical page on the main site: [chinaaihub.com/models/deepseek-v4-1-flash](https://chinaaihub.com/models/deepseek-v4-1-flash)

## Provider

[deepseek](../companies/deepseek.md)

## Model Family

DeepSeek-V4.1

## Release Date

2026-09-10

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
