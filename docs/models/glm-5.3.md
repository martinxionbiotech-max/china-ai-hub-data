# GLM-5.3

> Canonical page on the main site: [chinaaihub.com/models/glm-5.3](https://chinaaihub.com/models/glm-5.3)

## Provider

[zhipu-ai](../companies/zhipu-ai.md)

## Model Family

GLM-5

## Release Date

2026-08-18

## Status

active

## Architecture

744B total / 40B active (open-weight FP8); same base model as GLM-5.2 with post-training gains

## Parameter Information

- **total_parameters:** 744B
- **active_parameters:** 40B
- **parameter_precision:** FP8 (BF16 variant also released)

## Context Window

1048576

## Maximum Output

131072

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** No

## Open Weight

Yes

## License

Apache-2.0 (per GitHub repo metadata; README has no separate weights-license section - verify per-model HF cards before reuse)

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 1.4
- **output_price_per_1m:** 4.4
- **currency:** USD
- **pricing_ref:** zhipu-ai

## Official Api

Yes

## Cloud Providers

- Z.ai
- BigModel

## Regions

- international
- china

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| [Terminal-Bench 3.0](../benchmarks/terminal-bench.md) | 28.3 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| [DeepSWE v1.1](../benchmarks/deepswe.md) | 66.9 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| Agents' Last Exam (CLI) | 28.5 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| [CyberGym](../benchmarks/cybergym.md) | 84.5 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |

## Known Limitations

- Text-only input
- Reasoning always enabled (low/high/max, default max); cannot be disabled
- Z.ai Code Bench is a private in-house benchmark
- Benchmarks vendor-reported; not independently verified

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
| Z.ai pricing | https://docs.z.ai/guides/overview/pricing | official | 2026-09-20 | high |
| GLM-5 GitHub repository | https://github.com/zai-org/GLM-5 | official | 2026-09-20 | high |
