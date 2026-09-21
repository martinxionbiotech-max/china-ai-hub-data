# Qwen3.8-Max

> Canonical page on the main site: [chinaaihub.com/models/qwen3.8-max](https://chinaaihub.com/models/qwen3.8-max)

## Provider

alibaba-cloud

## Model Family

Qwen3.8

## Version

0902

## Aliases

- qwen3.8-max-0902
- qwen3.8-max-2026-09-02

## Release Date

2026-08

## Status

active

## Architecture

2.4T-parameter MoE, 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, Gated DeltaNet + Gated Attention hybrid

## Parameter Information

- **total_parameters:** 2.4T
- **active_parameters:** 95B

## Context Window

1048576

## Maximum Output

131072

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** Yes
- **video:** Yes
- **tool_calling:** Yes
- **structured_output:** Yes

## Open Weight

No

## License

proprietary

## Self Hosting

No

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 2.0
- **output_price_per_1m:** 6.0
- **currency:** USD
- **pricing_ref:** alibaba-cloud

## Official Api

Yes

## Cloud Providers

- Alibaba Cloud

## Regions

- china-beijing
- singapore
- hong-kong
- germany-frankfurt
- us-virginia
- japan-tokyo

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| Terminal-Bench 2.1 | 86.6 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| SWE-bench Pro | 67.7 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| GPQA Diamond | 92.6 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| HLE | 43.6 (56.2 with tools) | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| MRCR v2 256K | 92.9 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |

## Known Limitations

- Closed API model (the open Qwen3.8-2.4T-A95B weights are text-only and thinking-only - not the same product)
- Exact API release date not stated; the 0902 snapshot is dated 2026-09-02
- Prices differ by region: Singapore $2/$6; Beijing and Global regions $1.65/$4.951 per 1M tokens
- Benchmarks are from the vendor model card (Qwen3.8-Max column); not independently verified

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Model Studio — qwen3.8-max model detail | https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max | official | 2026-09-20 | high |
| Model Studio — model pricing | https://www.alibabacloud.com/help/en/model-studio/model-pricing | official | 2026-09-20 | high |
| Hugging Face model card — Qwen3.8-2.4T-A95B | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | official | 2026-09-20 | high |
