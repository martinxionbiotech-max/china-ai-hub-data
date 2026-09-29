# Qwen-Agent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/qwen-agent",
      "name": "Qwen-Agent",
      "url": "https://sinoaihub.com/agents/qwen-agent",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/qwen-agent/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://sinoaihub.com/companies/alibaba-cloud",
        "url": "https://sinoaihub.com/companies/alibaba-cloud"
      },
      "description": "Alibaba Qwen team's open-source Python framework for developing LLM applications based on Qwen's instruction following, tool usage, planning and memory capabilities (Apache-2.0). Serves as the backend of Qwen Chat (chat.qwen.ai). Ships example applications including BrowserQwen browser assistant, Docker-isolated Code Interpreter, RAG over 1M-token documents, MCP integration and Gradio GUI."
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
          "name": "Agents",
          "item": "https://data.sinoaihub.com/agents/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Qwen-Agent",
          "item": "https://data.sinoaihub.com/agents/qwen-agent/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/qwen-agent](https://sinoaihub.com/agents/qwen-agent)

## Type

agent


## Key facts

- **Company:** Alibaba Cloud (Qwen)
- **Type:** framework
- **Capabilities:** tool calling, browser use, MCP
- **Open source:** yes (Apache-2.0)
- **Pricing:** Framework free and open source (Apache-2.0). Model usage billed via DashScope API pay-as-you-go per token, or free with self-hosted open models. No subscription of its own.

## Company

[alibaba-cloud](../companies/alibaba-cloud.md)

## API Platform

- [model-studio](../apis/model-studio.md)

## Description

Alibaba Qwen team's open-source Python framework for developing LLM applications based on Qwen's instruction following, tool usage, planning and memory capabilities (Apache-2.0). Serves as the backend of Qwen Chat (chat.qwen.ai). Ships example applications including BrowserQwen browser assistant, Docker-isolated Code Interpreter, RAG over 1M-token documents, MCP integration and Gradio GUI.

## Agent Type

framework

## Framework

Python framework (pip install qwen-agent); built-in Assistant / FnCallAgent / ReActChat agents with @register_tool; connects to DashScope API or self-hosted models via vLLM/Ollama

## Tool Calling

Yes

## Browser Use

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

Framework free and open source (Apache-2.0). Model usage billed via DashScope API pay-as-you-go per token, or free with self-hosted open models. No subscription of its own.

## Deployment

self_hosted

## Open Source

Yes

## License

Apache-2.0

## Github

https://github.com/QwenLM/Qwen-Agent

## Documentation

https://qwenlm.github.io/Qwen-Agent/en/guide/

## Use Cases

- Custom LLM applications with tool calling
- Browser automation assistant (BrowserQwen)
- RAG over 1M-token documents
- Code interpreter and PDF-reading assistants
- MCP tool integration and agent evaluation via DeepPlanning benchmark

## Limitations

- Docker-based code interpreter has only basic sandbox isolation - use with caution in production
- TIR math demo Python executor is not sandboxed (local testing only)
- GUI requires Python 3.10+
- Last GitHub release v0.0.26 on 2025-05-29; repo development cadence has slowed since

## Verification Status

verified

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-qwen-agent-1 | Qwen-Agent GitHub repository | https://github.com/QwenLM/Qwen-Agent | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-agent-2 | Qwen-Agent docs guide | https://qwenlm.github.io/Qwen-Agent/en/guide/ | Official documentation | — | 2026-09-20 | high | — |
