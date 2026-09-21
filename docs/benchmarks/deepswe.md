# DeepSWE

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://chinaaihub.com/benchmarks/deepswe",
      "name": "DeepSWE",
      "url": "https://chinaaihub.com/benchmarks/deepswe",
      "mainEntityOfPage": "https://data.chinaaihub.com/benchmarks/deepswe/",
      "description": "Software engineering benchmark built from real-world issues and pull requests.",
      "dateModified": "2026-09-20"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://data.chinaaihub.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Benchmarks",
          "item": "https://data.chinaaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "DeepSWE",
          "item": "https://data.chinaaihub.com/benchmarks/deepswe/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/benchmarks/deepswe](https://chinaaihub.com/benchmarks/deepswe)

## Description

Software engineering benchmark built from real-world issues and pull requests.

## Evaluations

| benchmark | model | score | model_version | metric | date | source_type | source_url |
|---|---|---|---|---|---|---|---|
| DeepSWE | [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 74.2 | v1.1 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates |
| DeepSWE | [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 62.7 | version not stated in source | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates |
| DeepSWE | [qwen3.8-max](../models/qwen3.8-max.md) | 56.6 | v1.1 | accuracy | 2026-08 | vendor_reported | https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B |
| DeepSWE | [kimi-k3](../models/kimi-k3.md) | 67.5 | 67.3 with mini-SWE-agent harness | accuracy | 2026-07 | vendor_reported | https://github.com/MoonshotAI/Kimi-K3 |
| DeepSWE | [glm-5.3](../models/glm-5.3.md) | 66.9 | v1.1 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 |
| DeepSWE | [glm-5.3-flash](../models/glm-5.3-flash.md) | 63.4 | v1.1 | accuracy | 2026-08-26 | vendor_reported | https://docs.z.ai/guides/vlm/glm-5.3-flash |

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
