# Dify

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/dify",
      "name": "Dify",
      "url": "https://sinoaihub.com/agents/dify",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/dify/",
      "provider": {
        "@type": "Organization",
        "name": "LangGenius (Dify)",
        "@id": "https://sinoaihub.com/companies/langgenius",
        "url": "https://sinoaihub.com/companies/langgenius"
      },
      "description": "Dify is an open-source LLM application development platform by LangGenius. Its interface combines AI workflow, RAG pipeline, agent capabilities, model management and observability (Opik, Langfuse, Arize Phoenix) to move teams from prototype to production. Model-agnostic: integrates hundreds of proprietary and open-source LLMs, including any OpenAI API-compatible model. Deployable on Dify Cloud, VPC, or self-hosted via Docker Compose."
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/dify](https://sinoaihub.com/agents/dify)

## Type

agent


## Key facts

- **Company:** LangGenius (Dify)
- **Type:** platform
- **Capabilities:** tool calling, MCP, memory, planning
- **Open source:** yes (Dify Open Source License)
- **Pricing:** Open source (free self-hosted); Dify Cloud paid SaaS tiers.

## Company

[langgenius](../companies/langgenius.md)

## Description

Dify is an open-source LLM application development platform by LangGenius. Its interface combines AI workflow, RAG pipeline, agent capabilities, model management and observability (Opik, Langfuse, Arize Phoenix) to move teams from prototype to production. Model-agnostic: integrates hundreds of proprietary and open-source LLMs, including any OpenAI API-compatible model. Deployable on Dify Cloud, VPC, or self-hosted via Docker Compose.

## Agent Type

platform

## Tool Calling

Yes

## Mcp

Yes

## Memory

Yes

## Planning

Yes

## Api

Yes

## Pricing

Open source (free self-hosted); Dify Cloud is a paid SaaS with free and paid tiers (dify.ai/pricing); commercial licensing required for multi-tenant SaaS redistribution under the Dify Open Source License.

## Deployment

both

## Open Source

Yes

## License

Dify Open Source License (Apache-2.0 based with additional conditions)

## Github

https://github.com/langgenius/dify

## Documentation

https://docs.dify.ai/

## Use Cases

- Building agentic workflows and RAG pipelines
- Prototyping and shipping LLM applications
- Model management across multiple providers
- Observability and evaluation of LLM apps
- Self-hosted or VPC deployment for data control

## Limitations

- License is not pure Apache-2.0: a commercial license is required for multi-tenant SaaS-style redistribution
- Minimum system requirements (2-core CPU, 4 GiB RAM) mean heavier self-hosting than a CLI tool
- Model neutrality means the operator must configure and pay for their own model providers
- MCP is exposed via a published MCP Server URL that carries authentication credentials

## Verification Status

verified

## Last Verified

2026-09-29

## Source history

No documented source-change events located as of 2026-09-29.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-dify-1 | Dify GitHub repository | https://github.com/langgenius/dify | Official documentation | — | 2026-09-29 | high | — |
| src-agents-dify-2 | Dify official website | https://dify.ai/ | Official | — | 2026-09-29 | high | — |
| src-agents-dify-3 | Dify documentation | https://docs.dify.ai/ | Official documentation | — | 2026-09-29 | high | — |
| src-agents-dify-4 | Dify LICENSE | https://github.com/langgenius/dify/blob/main/LICENSE | Official documentation | — | 2026-09-29 | high | — |
| src-agents-dify-5 | Dify MCP Server documentation | https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp | Official documentation | — | 2026-09-29 | high | — |
