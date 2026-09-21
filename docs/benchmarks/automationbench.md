# AutomationBench

> Canonical page on the main site: [chinaaihub.com/benchmarks/automationbench](https://chinaaihub.com/benchmarks/automationbench)

## Description

Benchmark of computer-use automation tasks.

## Evaluations

| benchmark | model | score | metric | date | source_type | source_url | model_version |
|---|---|---|---|---|---|---|---|
| AutomationBench | [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 54.8 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates | — |
| AutomationBench | [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 31.8 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates | Public |
| AutomationBench | [qwen3.8-max](../models/qwen3.8-max.md) | 27.3 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B | Pass@1 |
| AutomationBench | [glm-5.3-flash](../models/glm-5.3-flash.md) | 48.8 | accuracy | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash | GLM-5.2: 26.2 |

## Limitations

All scores are vendor-reported and not independently verified. Pass@1 vs other sampling settings differ between vendors.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high |
| Z.ai docs — GLM-5.3-Flash model page | https://docs.z.ai/guides/vlm/glm-5.3-flash | official | 2026-09-20 | high |
