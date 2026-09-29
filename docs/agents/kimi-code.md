# Kimi Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/kimi-code",
      "name": "Kimi Code",
      "url": "https://sinoaihub.com/agents/kimi-code",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/kimi-code/",
      "provider": {
        "@type": "Organization",
        "name": "Moonshot AI",
        "@id": "https://sinoaihub.com/companies/moonshot-ai",
        "url": "https://sinoaihub.com/companies/moonshot-ai"
      },
      "description": "Moonshot AI's terminal AI coding agent ('The Starting Point for Next-Gen Agents'), successor to the deprecated kimi-cli. CLI (TypeScript, MIT), VS Code extension and Desktop app; reads/edits code, runs shell commands, searches files, fetches web pages, plans and adjusts actions autonomously. Includes subagents, MCP, Kimi Computer Use, browser control (WebBridge/Browser Extension) and multimodal input (text, images, video). Billed under Kimi membership."
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
          "name": "Kimi Code",
          "item": "https://data.sinoaihub.com/agents/kimi-code/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/kimi-code](https://sinoaihub.com/agents/kimi-code)

## Key facts

- **Company:** Moonshot AI
- **Type:** coding
- **Underlying models:** Kimi K3, Kimi K2.7 Code, Kimi K2.7 Code Highspeed
- **Capabilities:** tool calling, browser use, computer use, MCP
- **Open source:** yes (MIT)
- **Pricing:** Included with Kimi membership, Plus and above (Adagio free tier has no coding quota; Plus $15/mo, Pro $31/mo, Max $79/mo, Ultra $159/mo). All clients share one quota with rolling 5-hour window and monthly total. Open Platform API pay-as-you-go: kimi-k3 $3.00/M input / $15.00/M output; kimi-k2.7-code $0.95/$4.00; kimi-k2.7-code-highspeed $1.90/$8.00.

## Company

[moonshot-ai](../companies/moonshot-ai.md)

## API Platform

- [moonshot](../apis/moonshot.md)

## Description

Moonshot AI's terminal AI coding agent ('The Starting Point for Next-Gen Agents'), successor to the deprecated kimi-cli. CLI (TypeScript, MIT), VS Code extension and Desktop app; reads/edits code, runs shell commands, searches files, fetches web pages, plans and adjusts actions autonomously. Includes subagents, MCP, Kimi Computer Use, browser control (WebBridge/Browser Extension) and multimodal input (text, images, video). Billed under Kimi membership.

## Agent Type

coding

## Underlying Models

- [Kimi K3](../models/kimi-k3.md)
- [Kimi K2.7 Code](../models/kimi-k2.7-code.md)
- [Kimi K2.7 Code Highspeed](../models/kimi-k2.7-code-highspeed.md)

## Tool Calling

Yes

## Browser Use

Yes

## Computer Use

Yes

## Mcp

Yes

## Framework

TypeScript terminal agent (pi-tui); succeeds the deprecated Python kimi-cli

## Planning

Yes

## Multi Agent

Yes

## Api

Yes

## Pricing

Included with Kimi membership, Plus and above (Adagio free tier has no coding quota; Plus $15/mo, Pro $31/mo, Max $79/mo, Ultra $159/mo). All clients share one quota with rolling 5-hour window and monthly total. Open Platform API pay-as-you-go: kimi-k3 $3.00/M input / $15.00/M output; kimi-k2.7-code $0.95/$4.00; kimi-k2.7-code-highspeed $1.90/$8.00.

## Deployment

both

## Open Source

Yes

## License

MIT

## Github

https://github.com/MoonshotAI/kimi-code

## Documentation

https://moonshotai.github.io/kimi-code/en/

## Use Cases

- Understanding unfamiliar codebases and implementing features
- Bug fixing, writing tests, refactoring
- Batch file processing
- Long-horizon whole-repo work via 1M-token context (K3)
- Video-input tasks (screen recording to code)
- Scheduled and background tasks
- IDE-driven sessions via VS Code extension or ACP (Zed, JetBrains)

## Limitations

- Runs on the local machine with approval gates; no dedicated OS-level sandbox engine
- kimi-cli predecessor deprecated and being wound down (auto-migrated on install)
- Computer Use (macOS) needs Accessibility + Screen Recording permissions; Windows version may briefly take over mouse/keyboard
- Third-party tools must keep the real client identifier (User-Agent tampering restricted)
- Cloud inference only (managed endpoints api.kimi.com/coding/v1 and api.kimi.ai/coding/v1); not self-hostable as a model service
- Windows install requires Git for Windows
- API keys shown only once (max 5); quota shared across devices; devices inactive >30 days unbound

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Kimi Code GitHub repository | https://github.com/MoonshotAI/kimi-code | official | 2026-09-20 | high |
| Kimi Code CLI documentation | https://moonshotai.github.io/kimi-code/en/ | official | 2026-09-20 | high |
| Kimi Code product docs | https://www.kimi.com/code/docs/en/ | official | 2026-09-20 | high |
| Kimi membership pricing | https://www.kimi.ai/membership/pricing | official | 2026-09-20 | high |
