# Qwen-Agent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://chinaaihub.com/agents/qwen-agent",
      "name": "Qwen-Agent",
      "url": "https://chinaaihub.com/agents/qwen-agent",
      "mainEntityOfPage": "https://data.chinaaihub.com/agents/qwen-agent/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://chinaaihub.com/companies/alibaba-cloud",
        "url": "https://chinaaihub.com/companies/alibaba-cloud"
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
          "item": "https://data.chinaaihub.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Agents",
          "item": "https://data.chinaaihub.com/agents/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Qwen-Agent",
          "item": "https://data.chinaaihub.com/agents/qwen-agent/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/agents/qwen-agent](https://chinaaihub.com/agents/qwen-agent)

## Company

[alibaba-cloud](../companies/alibaba-cloud.md)

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

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Qwen-Agent GitHub repository | https://github.com/QwenLM/Qwen-Agent | official | 2026-09-20 | high |
| Qwen-Agent docs guide | https://qwenlm.github.io/Qwen-Agent/en/guide/ | official | 2026-09-20 | high |
