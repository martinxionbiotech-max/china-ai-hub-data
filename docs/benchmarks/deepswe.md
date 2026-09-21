# DeepSWE

> Canonical page on the main site: [chinaaihub.com/benchmarks/deepswe](https://chinaaihub.com/benchmarks/deepswe)

## Description

Software engineering benchmark built from real-world issues and pull requests.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| DeepSWE | deepseek-v4-1-flash | 74.2 | v1.1 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| DeepSWE | deepseek-v4-pro | 62.7 | version not stated in source | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| DeepSWE | qwen3.8-max | 56.6 | v1.1 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| DeepSWE | kimi-k3 | 67.5 | 67.3 with mini-SWE-agent harness | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| DeepSWE | glm-5.3 | 66.9 | v1.1 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| DeepSWE | glm-5.3-flash | 63.4 | v1.1 | accuracy | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash |

## Limitations

All scores are vendor-reported and not independently verified. Some vendors do not state the benchmark version; unversioned scores should not be compared with versioned ones.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high |
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
