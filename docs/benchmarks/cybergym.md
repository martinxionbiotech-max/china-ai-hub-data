# CyberGym

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Dataset",
      "@id": "https://sinoaihub.com/benchmarks/cybergym",
      "name": "CyberGym",
      "url": "https://sinoaihub.com/benchmarks/cybergym",
      "mainEntityOfPage": "https://data.sinoaihub.com/benchmarks/cybergym/",
      "description": "Cybersecurity agent benchmark focused on vulnerability discovery tasks."

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
          "name": "Benchmarks",
          "item": "https://data.sinoaihub.com/benchmarks/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "CyberGym",
          "item": "https://data.sinoaihub.com/benchmarks/cybergym/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/benchmarks/cybergym](https://sinoaihub.com/benchmarks/cybergym)

## Type

benchmark


## Key facts

- **Task type:** Cybersecurity vulnerability analysis (real-world vulnerability discovery)
- **Dataset size:** Large-scale task suite sourced from ARVO and OSS-Fuzz (~240GB data)
- **Evaluation method:** Docker-isolated environments; agents analyze vulnerabilities and generate proofs of concept; pre-/post-patch versions
- **Scoring:** Success rate on vulnerability analysis tasks (PoC generation)
- **Recorded evaluations:** 4

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

## Relevant Models

- [GLM-5.3](../models/glm-5.3.md) — 84.5

## Limitations

All scores are vendor-reported and not independently verified.

## Verification Status

verified

## Benchmark Changes

No documented benchmark changes on record as of 2026-09-29.

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-benchmarks-cybergym-1 | DeepSeek API Change Log | https://api-docs.deepseek.com/updates | Official documentation | — | 2026-09-20 | high | — |
| src-benchmarks-cybergym-2 | Z.ai docs — GLM-5.3 model page | https://docs.z.ai/guides/llm/glm-5.3 | Official documentation | — | 2026-09-20 | high | — |
