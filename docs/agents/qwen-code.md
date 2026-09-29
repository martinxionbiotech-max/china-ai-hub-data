# Qwen Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/qwen-code",
      "name": "Qwen Code",
      "url": "https://sinoaihub.com/agents/qwen-code",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/qwen-code/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://sinoaihub.com/companies/alibaba-cloud",
        "url": "https://sinoaihub.com/companies/alibaba-cloud"
      },
      "description": "Alibaba Qwen team's open-source AI coding agent (Apache-2.0) for terminal, editor, desktop, browser and chat. Originally based on Google Gemini CLI v0.8.2, independent development since v0.1 as a multi-protocol, multi-platform agent framework. Ships as CLI (npm), Desktop app, VS Code 'Qwen Code Companion' (Beta), Web UI and IM channels (Telegram/DingTalk/WeChat/Feishu). Includes 5 permission modes, Seatbelt/Docker sandboxing, auto-memory, subagents, MCP, computer use and multi-protocol model support."
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
          "name": "Qwen Code",
          "item": "https://data.sinoaihub.com/agents/qwen-code/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/qwen-code](https://sinoaihub.com/agents/qwen-code)

## Type

agent


## Key facts

- **Company:** Alibaba Cloud (Qwen)
- **Type:** coding
- **Capabilities:** tool calling, browser use, computer use, MCP
- **Open source:** yes (Apache-2.0)
- **Pricing:** CLI free (Apache-2.0); user pays the model provider. Alibaba Cloud Coding Plan (intl) Pro $50/month; Token Plan (CN, Beijing only) Personal Lite ¥39 / Essential ¥79 / Standard ¥139 / Pro ¥499 per month, team seats ¥150-¥1398; or pay-as-you-go Model Studio API keys; BYO keys to other providers.

## Company

[alibaba-cloud](../companies/alibaba-cloud.md)

## API Platform

- [model-studio](../apis/model-studio.md)

## Description

Alibaba Qwen team's open-source AI coding agent (Apache-2.0) for terminal, editor, desktop, browser and chat. Originally based on Google Gemini CLI v0.8.2, independent development since v0.1 as a multi-protocol, multi-platform agent framework. Ships as CLI (npm), Desktop app, VS Code 'Qwen Code Companion' (Beta), Web UI and IM channels (Telegram/DingTalk/WeChat/Feishu). Includes 5 permission modes, Seatbelt/Docker sandboxing, auto-memory, subagents, MCP, computer use and multi-protocol model support.

## Agent Type

coding

## Framework

Multi-protocol agent framework (TypeScript); supports OpenAI, Anthropic, Gemini, Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models (Ollama/vLLM)

## Tool Calling

Yes

## Browser Use

Yes

## Computer Use

Yes

## Mcp

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

CLI free (Apache-2.0); user pays the model provider. Alibaba Cloud Coding Plan (intl) Pro $50/month; Token Plan (CN, Beijing only) Personal Lite ¥39 / Essential ¥79 / Standard ¥139 / Pro ¥499 per month, team seats ¥150-¥1398; or pay-as-you-go Model Studio API keys; BYO keys to other providers.

## Deployment

self_hosted

## Open Source

Yes

## License

Apache-2.0

## Github

https://github.com/QwenLM/qwen-code

## Documentation

https://qwenlm.github.io/qwen-code-docs/en/users/overview/

## Use Cases

- Building features from natural-language descriptions
- Debugging and fixing issues in existing codebases
- CI automation and pipe-friendly Unix workflows (qwen -p)
- Remote agent via chat channels (Telegram, DingTalk, WeChat, Feishu)
- Multi-model head-to-head comparisons via Agent Arena

## Limitations

- Web UI and daemon (qwen serve) marked experimental
- Qwen OAuth free tier discontinued 2026-04-15
- Sandboxing reduces but does not eliminate all risks; GUI apps may not work in sandboxes
- Default Docker sandbox image is intentionally minimal (Java not included by default)
- Auto Mode classifier biased toward blocking and fails closed on classifier outage
- Auto-memory is best-effort; QWEN.md is the guaranteed instruction file

## Verification Status

verified

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-qwen-code-1 | Qwen Code GitHub repository | https://github.com/QwenLM/qwen-code | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-2 | Qwen Code docs - overview | https://qwenlm.github.io/qwen-code-docs/en/users/overview/ | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-3 | Alibaba Cloud Model Studio Coding Plan | https://www.alibabacloud.com/help/en/model-studio/coding-plan | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-code-4 | Alibaba Cloud Token Plan overview | https://help.aliyun.com/en/model-studio/token-plan-overview | Official documentation | — | 2026-09-20 | high | — |
