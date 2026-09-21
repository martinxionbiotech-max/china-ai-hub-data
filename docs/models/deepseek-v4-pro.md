# DeepSeek-V4-Pro

> Canonical page on the main site: [chinaaihub.com/models/deepseek-v4-pro](https://chinaaihub.com/models/deepseek-v4-pro)

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

## Known Limitations

- Deprecation announced 2026-09-10: news page says V4-Pro requests will route to V4.1-Flash after 2026-09-14 until V4.1-Pro launches, but the same-day change log says V4-Pro API service continues with unchanged billing - the official pages conflict
- Vision not supported
- Open-weight HF checkpoint last modified 2026-06-22; unclear whether it matches the 0813 GA checkpoint
- Pricing is peak/off-peak: listed prices are off-peak; peak is 2x

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence | published_date |
|---|---|---|---|---|---|
| DeepSeek API docs — Models & Pricing | https://api-docs.deepseek.com/quick_start/pricing | official | 2026-09-20 | high | — |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high | — |
| DeepSeek-V4 Preview release | https://www.deepseek.com/en/news/v4-preview/ | official | 2026-09-20 | high | 2026-04-24 |
| Hugging Face model card — DeepSeek-V4-Pro | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | official | 2026-09-20 | high | — |
