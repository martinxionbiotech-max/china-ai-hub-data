# MetaGPT

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/metagpt",
      "name": "MetaGPT",
      "url": "https://sinoaihub.com/agents/metagpt",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/metagpt/",
      "provider": {
        "@type": "Organization",
        "name": "DeepWisdom (FoundationAgents)",
        "@id": "https://sinoaihub.com/companies/deepwisdom",
        "url": "https://sinoaihub.com/companies/deepwisdom"
      },
      "description": "MetaGPT is an open-source multi-agent framework by DeepWisdom (now FoundationAgents). It assigns distinct roles — product managers, architects, project managers and engineers — to LLMs to form a collaborative 'software company' that turns a one-line requirement into user stories, requirements, data structures, APIs and code, under the philosophy 'Code = SOP(Team)'. MIT-licensed."
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/metagpt](https://sinoaihub.com/agents/metagpt)

## Type

agent


## Key facts

- **Company:** DeepWisdom (FoundationAgents)
- **Type:** framework
- **Capabilities:** tool calling, memory, planning, multi-agent
- **Open source:** yes (MIT)
- **Pricing:** Free and open source (MIT); MGX offered separately.

## Company

[deepwisdom](../companies/deepwisdom.md)

## Description

MetaGPT is an open-source multi-agent framework by DeepWisdom (now FoundationAgents). It assigns distinct roles — product managers, architects, project managers and engineers — to LLMs to form a collaborative 'software company' that turns a one-line requirement into user stories, requirements, data structures, APIs and code, under the philosophy 'Code = SOP(Team)'. Ships as a pip-installable Python framework and CLI; the natural-language-programming product MGX (MetaGPT X) is built on it. MIT-licensed.

## Agent Type

framework

## Framework

Python framework (pip install metagpt) with a role-based multi-agent architecture; SOP (standard operating procedure) orchestration of a software-company team; configurable LLM backend (OpenAI, Azure, Ollama, Groq and other API-compatible providers).

## Tool Calling

Yes

## Memory

Yes

## Planning

Yes

## Multi Agent

Yes

## Api

Yes

## Pricing

Free and open source (MIT). The commercial product MGX (MetaGPT X) at mgx.dev is separately offered; framework usage is free with self-supplied model API keys.

## Deployment

self_hosted

## Open Source

Yes

## License

MIT

## Github

https://github.com/FoundationAgents/MetaGPT

## Documentation

https://docs.deepwisdom.ai/

## Use Cases

- Multi-agent software development from a single requirement
- Role-based orchestration (PM / architect / engineer) of LLM teams
- Data analysis via the Data Interpreter
- Research prototyping of agentic workflows (SPO, AOT, AFlow)
- Natural-language programming via MGX

## Limitations

- Requires Python 3.9–3.11 (3.12 not yet supported per the README)
- Model-agnostic means the user must configure and pay for their own LLM API keys
- The framework is a research-grade SDK, not a turnkey hosted product (MGX is the productized layer)
- Repository recently moved from geekan/MetaGPT to FoundationAgents/MetaGPT

## Verification Status

verified

## Last Verified

2026-09-29

## Source history

No documented source-change events located as of 2026-09-29.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-metagpt-1 | MetaGPT GitHub repository (FoundationAgents) | https://github.com/FoundationAgents/MetaGPT | Official documentation | — | 2026-09-29 | high | — |
| src-agents-metagpt-2 | MetaGPT documentation (DeepWisdom) | https://docs.deepwisdom.ai/ | Official documentation | — | 2026-09-29 | high | — |
| src-agents-metagpt-3 | MGX (MetaGPT X) product site | https://mgx.dev/ | Official | — | 2026-09-29 | high | — |
