# Terminal-Bench

> Canonical page on the main site: [chinaaihub.com/benchmarks/terminal-bench](https://chinaaihub.com/benchmarks/terminal-bench)

## Description

Terminal-based agent benchmark (shell commands, file operations, package management and other command-line tasks).

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| Terminal-Bench | deepseek-v4-1-flash | 90.6 | 2.1 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| Terminal-Bench | deepseek-v4-pro | 87.9 | 2.1 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| Terminal-Bench | qwen3.8-max | 86.6 | 2.1 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| Terminal-Bench | kimi-k3 | 88.3 | 2.1 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| Terminal-Bench | minimax-m3 | 66.0 | 2.1 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/blog/minimax-m3 |
| Terminal-Bench | glm-5.3 | 28.3 | 3.0 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| Terminal-Bench | glm-5.2 | 4.6 | 3.0 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| Terminal-Bench | kimi-k2.5 | 50.8 | 2.0 | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |
| Terminal-Bench | minimax-m2 | 46.3 | version not stated in source | accuracy | 2025-10 | vendor_reported | https://github.com/MiniMax-AI/MiniMax-M2 |

## Limitations

Benchmark versions (2.0 / 2.1 / 3.0) are not comparable to each other; the version is recorded per evaluation. All scores are vendor-reported and not independently verified.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high |
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
