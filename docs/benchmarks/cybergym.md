# CyberGym

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://china-ai-hub.pages.dev/benchmarks/cybergym",
      "name": "CyberGym",
      "url": "https://china-ai-hub.pages.dev/benchmarks/cybergym",
      "mainEntityOfPage": "https://china-ai-hub-data.pages.dev/benchmarks/cybergym/",
      "description": "Cybersecurity agent benchmark focused on vulnerability discovery tasks.",
      "dateModified": "2026-09-20"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://china-ai-hub-data.pages.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Benchmarks",
          "item": "https://china-ai-hub-data.pages.dev/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "CyberGym",
          "item": "https://china-ai-hub-data.pages.dev/benchmarks/cybergym/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [china-ai-hub.pages.dev/benchmarks/cybergym](https://china-ai-hub.pages.dev/benchmarks/cybergym)

## Description

Cybersecurity agent benchmark focused on vulnerability discovery tasks.

## Evaluations

| benchmark | model | score | metric | date | source_type | source_url | model_version |
|---|---|---|---|---|---|---|---|
| CyberGym | [deepseek-v4-1-flash](../models/deepseek-v4-1-flash.md) | 88.1 | accuracy | 2026-09-10 | vendor_reported | https://api-docs.deepseek.com/updates | — |
| CyberGym | [deepseek-v4-pro](../models/deepseek-v4-pro.md) | 83.3 | accuracy | 2026-08-13 | vendor_reported | https://api-docs.deepseek.com/updates | — |
| CyberGym | [glm-5.3](../models/glm-5.3.md) | 84.5 | accuracy | 2026-08-18 | vendor_reported | https://docs.z.ai/guides/llm/glm-5.3 | vuln discovery (GLM-5.2: 77.2) |

## Methodology

**Task type:** Cybersecurity vulnerability analysis (real-world vulnerability discovery)

**Dataset size:** Large-scale task suite sourced from ARVO and OSS-Fuzz (~240GB data)

**Evaluation method:** Docker-isolated environments; agents analyze vulnerabilities and generate proofs of concept; pre-/post-patch versions

**Scoring:** Success rate on vulnerability analysis tasks (PoC generation)

## Limitations

All scores are vendor-reported and not independently verified.

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | official | 2026-09-20 | high |
| Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | official | 2026-09-20 | high |
