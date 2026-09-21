# BrowseComp

> Canonical page on the main site: [chinaaihub.com/benchmarks/browsecomp](https://chinaaihub.com/benchmarks/browsecomp)

## Description

Benchmark of browsing and retrieval ability: locating obscure information using web search and browsing.

## Evaluations

| benchmark | model | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|
| BrowseComp | kimi-k3 | 91.2 (90.4 with full 1M context, no compaction) | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| BrowseComp | kimi-k2.5 | 60.6 (74.9 with context management; 78.4 Agent Swarm) | accuracy | — | vendor_reported | https://github.com/MoonshotAI/Kimi-K2.5 |
| BrowseComp | minimax-m3 | 83.5 | accuracy | 2026-06-01 | vendor_reported | https://www.minimax.cn/models/text/m3 |

## Limitations

All scores are vendor-reported and not independently verified. Evaluation setups (context management, agent scaffolding) differ between vendors.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | official | 2026-09-20 | high |
| MiniMax official M3 model page | https://www.minimax.cn/models/text/m3 | official | 2026-09-20 | high |
