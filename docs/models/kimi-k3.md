# Kimi K3

> Canonical page on the main site: [chinaaihub.com/models/kimi-k3](https://chinaaihub.com/models/kimi-k3)

## Provider

[moonshot-ai](../companies/moonshot-ai.md)

## Model Family

Kimi K-series

## Release Date

2026-07-16

## Status

active

## Architecture

MoE: 2.8T total / 104B activated; 93 layers (1 dense); 896 experts (16 selected + 2 shared per token); 69 KDA + 24 Gated MLA layers; hidden dim 7168; SiTU-GLU; MoonViT-V2 vision encoder (401M); MXFP4 weights / MXFP8 activations

## Parameter Information

- **total_parameters:** 2.8T
- **active_parameters:** 104B

## Context Window

1048576

## Maximum Output

1048576

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **vision:** Yes
- **video:** Yes
- **tool_calling:** Yes
- **structured_output:** Yes
- **agent_capability:** Yes

## Open Weight

Yes

## License

Kimi K3 License (permissive MIT-style, but Model-as-a-Service operators with >$20M aggregate revenue over any 12 months must sign a separate agreement; products with >100M MAU or >$20M monthly revenue must display 'Kimi K3' in the UI)

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 3.0
- **output_price_per_1m:** 15.0
- **currency:** USD
- **pricing_ref:** moonshot-ai

## Official Api

Yes

## Cloud Providers

- Moonshot AI Platform

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| [GPQA Diamond](../benchmarks/gpqa-diamond.md) | 93.5 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| [HLE-Full](../benchmarks/hle.md) | 43.5 (56.0 with tools) | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| [DeepSWE](../benchmarks/deepswe.md) | 67.5 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| [Terminal-Bench 2.1](../benchmarks/terminal-bench.md) | 88.3 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| [MMMU-Pro](../benchmarks/mmmu-pro.md) | 81.6 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| [Video-MME (with subtitles)](../benchmarks/video-mme.md) | 90.0 | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |

## Known Limitations

- Temperature fixed at 1.0 and top_p at 0.95 - cannot be modified
- API access requires a minimum $1 top-up
- Modality documentation inconsistent: architecture table says Text+Image, while the README, launch blog and API guide also show video input
- Benchmarks vendor-reported; some comparison scores cited from Artificial Analysis

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence | published_date |
|---|---|---|---|---|---|
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high | — |
| Kimi API platform — model list | https://platform.kimi.ai/docs/models.md | official | 2026-09-20 | high | — |
| Kimi API — Chat Completions spec | https://platform.kimi.ai/docs/api/chat.md | official | 2026-09-20 | high | — |
| Kimi K3 launch blog | https://www.kimi.com/blog/kimi-k3 | official | 2026-09-20 | high | 2026-07-16 |
