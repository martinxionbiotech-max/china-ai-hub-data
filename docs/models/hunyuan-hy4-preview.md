# Hunyuan Hy4 preview

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/models/hunyuan-hy4-preview",
      "name": "Hunyuan Hy4 preview",
      "url": "https://sinoaihub.com/models/hunyuan-hy4-preview",
      "mainEntityOfPage": "https://data.sinoaihub.com/models/hunyuan-hy4-preview/",
      "provider": {
        "@type": "Organization",
        "name": "Tencent",
        "@id": "https://sinoaihub.com/companies/tencent",
        "url": "https://sinoaihub.com/companies/tencent"
      },
      "datePublished": "2026-08-28"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://data.sinoaihub.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Models",
          "item": "https://data.sinoaihub.com/models/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Hunyuan Hy4 preview",
          "item": "https://data.sinoaihub.com/models/hunyuan-hy4-preview/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/models/hunyuan-hy4-preview](https://sinoaihub.com/models/hunyuan-hy4-preview)

## Type

model


## Definition

Hunyuan Hy4 preview is a Tencent model in the Hunyuan Hy family: Mixture-of-Experts: 770B total / 49B active (6.4%), 78 layers (1 dense FFN + 77 MoE), 256 routed + 1 shared expert per layer, top-8 routing, Gated DeepSeek Sparse Attention with IndexCache, plus one native MTP layer (10B total / 0.7B active) for speculative decoding; 1,000,000-token context window; open-weight; Apache-2.0 license; released 2026-08-28.

## Key facts

- **Architecture:** Mixture-of-Experts: 770B total / 49B active (6.4%), 78 layers (1 dense FFN + 77 MoE), 256 routed + 1 shared expert per layer, top-8 routing, Gated DeepSeek Sparse Attention with IndexCache, plus one native MTP layer (10B total / 0.7B active) for speculative decoding
- **Context window:** 1,000,000 tokens (max output not published)
- **Weights:** open; Apache-2.0 license
- **API pricing:** $0.834 input / $2.501 output per 1M tokens (USD); $0.042 per 1M cached input
- **Released:** 2026-08-28
- **Capabilities:** reasoning, coding, math, chinese, english, multilingual, tool_calling, function_calling, agent_capability

## Provider

[tencent](../companies/tencent.md)

## Model Family

Hunyuan Hy

## Release Date

2026-08-28

## Status

preview

## Architecture

Mixture-of-Experts: 770B total / 49B active (6.4%), 78 layers (1 dense FFN + 77 MoE), 256 routed + 1 shared expert per layer, top-8 routing, Gated DeepSeek Sparse Attention with IndexCache, plus one native MTP layer (10B total / 0.7B active) for speculative decoding

## Parameter Information

- **total_parameters:** 770B
- **active_parameters:** 49B
- **parameter_precision:** BF16 open weights; separate FP8 quantized release

## Context Window

1000000

## Maximum Output

Not published

## Capabilities

- **reasoning:** Yes
- **coding:** Yes
- **math:** Yes
- **chinese:** Yes
- **english:** Yes
- **multilingual:** Yes
- **vision:** No
- **audio:** No
- **video:** No
- **tool_calling:** Yes
- **function_calling:** Yes
- **agent_capability:** Yes

## Open Weight

Yes

## License

Apache-2.0

## Self Hosting

Yes

## Api Available

Yes

## Pricing

- **input_price_per_1m:** 0.834
- **output_price_per_1m:** 2.501
- **currency:** USD
- **effective_date:** 2026-08-28
- **pricing_ref:** tencent

## Official Api

Yes

## Cloud Providers

- Tencent Cloud TokenHub
- OpenRouter

## Regions

- china
- international

## Benchmark Results

| benchmark | score | metric | date | source_type | source_url |
|---|---|---|---|---|---|
| Tencent internal blind evaluation (163 experts, 203 engineering tasks) | 2.99 | mean rating out of 4.00 | 2026-08-28 | vendor_reported | https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/ |

## Known Limitations

- Tencent states the preview over-reasons on complex tasks and tends to over-verify its own work
- Early preview — Tencent says both pre-training and post-training have headroom left
- Maximum output length is not published
- Text-only in the preview; visual understanding was announced for the next Hy4 generation, not this one
- No independent suite is recorded here — the only published comparative result is Tencent's own internal blind evaluation

## Verification Status

verified

## License Changes

No documented license changes on record as of 2026-10-31.

## Last Verified

2026-10-31

## Source history

No documented source-change events located as of 2026-10-31.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-hy4-1 | Tencent — Hy4 preview release announcement | https://www.tencent.com/zh-cn/tencent-releases-and-open-sources-tencent-hy4-preview/ | Official | 2026-08-28 | 2026-10-31 | high | — |
| src-models-hy4-2 | Hy4 preview model card (Hugging Face) | https://huggingface.co/tencent/Hy4-preview | Official | — | 2026-10-31 | high | — |
| src-models-hy4-3 | Hy4 preview model card — Chinese (README_CN) | https://huggingface.co/tencent/Hy4-preview/blob/main/README_CN.md | Official | — | 2026-10-31 | high | — |
| src-models-hy4-4 | Tencent Hy research site — Hy4 | https://hy.tencent.com/research/hy4-preview | Official | — | 2026-10-31 | medium | Page did not render for extraction; cited for existence only |
| src-models-hy4-5 | 智东西 — 汤道生预告混元Hy4，首次加入视觉理解 | https://news.qq.com/rain/a/20261030A0000M00 | Industry media | 2026-10-30 | 2026-10-31 | medium | Vision and flash variant described as forthcoming, not shipped |
| src-models-hy4-6 | 财联社 — Hy4 preview 开源，下一版模型近期上线 | https://cls.cn/detail/2467904 | Industry media | 2026-08-28 | 2026-10-31 | medium | — |
