# DeepSeek Harness

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://chinaaihub.com/agents/deepseek-harness",
      "name": "DeepSeek Harness",
      "url": "https://chinaaihub.com/agents/deepseek-harness",
      "mainEntityOfPage": "https://data.chinaaihub.com/agents/deepseek-harness/",
      "provider": {
        "@type": "Organization",
        "name": "DeepSeek",
        "@id": "https://chinaaihub.com/companies/deepseek",
        "url": "https://chinaaihub.com/companies/deepseek"
      },
      "description": "Open-source agent harness from DeepSeek ('Everything is a Plugin') that powers its coding agent. All capabilities - models, tools, skills, sessions, sandbox, storage, loops, scheduling and UI - are composed from replaceable plugins. Developer preview; ships as CLI (dsh), Web UI, Electron Desktop app, Python SDK and ACP server."
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
          "name": "DeepSeek Harness",
          "item": "https://data.chinaaihub.com/agents/deepseek-harness/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [chinaaihub.com/agents/deepseek-harness](https://chinaaihub.com/agents/deepseek-harness)

## Company

[deepseek](../companies/deepseek.md)

## Description

Open-source agent harness from DeepSeek ('Everything is a Plugin') that powers its coding agent. All capabilities - models, tools, skills, sessions, sandbox, storage, loops, scheduling and UI - are composed from replaceable plugins. Developer preview; ships as CLI (dsh), Web UI, Electron Desktop app, Python SDK and ACP server.

## Agent Type

framework

## Underlying Models

- deepseek-v4-1-flash
- deepseek-v4-pro

## Framework

Cordis

## Tool Calling

Yes

## Browser Use

Yes

## Computer Use

Yes

## Mcp

Yes

## Memory

No

## Planning

Yes

## Multi Agent

Yes

## Api

Yes

## Pricing

Software itself free and open source. Model usage billed by the configured provider (DeepSeek API pay-as-you-go: flash $0.15-$0.30/M input cache-miss, $0.60-$1.20/M output, off-peak = half of peak; v4-pro $0.66-$1.32/M input, $1.98-$3.96/M output).

## Deployment

self_hosted

## Open Source

Yes

## License

MIT

## Github

https://github.com/deepseek-ai/deepseek-harness

## Documentation

https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart

## Use Cases

- Interactive coding-agent chat via Web UI
- Headless one-shot tasks via dsh --profile headless with a task prompt
- Embedding agents in Python programs (Python SDK)
- Programmatic multi-session automation over ACP (Agent Client Protocol)
- GitHub PR review via webhook overlay
- Custom profiles/plugins/presets for different agent compositions

## Limitations

- Developer preview - compatibility-breaking changes expected; not security-audited, not production-ready (SAFETY.md)
- Sandboxing/approvals do not guarantee isolation - run untrusted work in a disposable VM or container
- Web server binds loopback only; trusted-host list required for LAN access
- No VS Code/editor extension found in repo; ACP is automation-only
- Image input only via deepseek-flash; deepseek-v4-pro is text-only
- OAuth providers (e.g. Codex) not yet supported; API-key providers only
- No built-in memory; third-party memory MCP servers are interoperability examples only
- sdk-minimal profile pins danger-full-access permissions by default

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| DeepSeek Harness GitHub repository | https://github.com/deepseek-ai/deepseek-harness | official | 2026-09-20 | high |
| DeepSeek Harness product page | https://deepseek.com/harness | official | 2026-09-20 | high |
| DeepSeek Harness documentation | https://deepseek-harness.github.io/deepseek-harness/en/guide/quickstart | official | 2026-09-20 | high |
| DeepSeek API pricing | https://api-docs.deepseek.com/quick_start/pricing | official | 2026-09-20 | high |
