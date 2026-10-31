# WorkBuddy

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://sinoaihub.com/agents/workbuddy",
      "name": "WorkBuddy",
      "url": "https://sinoaihub.com/agents/workbuddy",
      "mainEntityOfPage": "https://data.sinoaihub.com/agents/workbuddy/",
      "provider": {
        "@type": "Organization",
        "name": "Tencent",
        "@id": "https://sinoaihub.com/companies/tencent",
        "url": "https://sinoaihub.com/companies/tencent"
      },
      "description": "WorkBuddy is Tencent's all-scenario AI office agent — a desktop workbench launched 9 March 2026 on the CodeBuddy architecture. It plans and executes multi-step tasks, operates local files with permission, and delivers finished documents, spreadsheets and slides. It is model-neutral by design (Hunyuan, GLM, Kimi, MiniMax and DeepSeek are all built in), compatible with the OpenClaw skill format, and connected to WeChat, WeCom, QQ, Feishu and DingTalk for remote control."
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/agents/workbuddy](https://sinoaihub.com/agents/workbuddy)

## Type

agent


## Key facts

- **Company:** Tencent
- **Type:** enterprise
- **Capabilities:** tool calling, MCP, memory, planning, multi-agent, API
- **Open source:** no (proprietary)
- **Pricing:** Free tier 500 credits/month; Standard ¥99/month; Advanced ¥199/month; Flagship ¥999/month; Buddy One VIP ¥999–1,399/month.

## Company

[tencent](../companies/tencent.md)

## Description

WorkBuddy is Tencent's all-scenario AI office agent — a desktop workbench launched 9 March 2026 on the CodeBuddy architecture. It plans and executes multi-step tasks, operates local files with permission, and delivers finished documents, spreadsheets and slides. It is model-neutral by design (Hunyuan, GLM, Kimi, MiniMax and DeepSeek are all built in), compatible with the OpenClaw skill format, and connected to WeChat, WeCom, QQ, Feishu and DingTalk for remote control.

## Agent Type

enterprise

## Underlying Models

- [glm-5.3](../models/glm-5.3.md)
- [glm-5.3-flash](../models/glm-5.3-flash.md)
- [glm-5.2](../models/glm-5.2.md)
- [minimax-m3](../models/minimax-m3.md)
- [minimax-m2.7](../models/minimax-m2.7.md)
- [kimi-k3](../models/kimi-k3.md)
- [kimi-k2.7-code](../models/kimi-k2.7-code.md)
- [kimi-k2.6](../models/kimi-k2.6.md)
- [deepseek-v4-pro](../models/deepseek-v4-pro.md)

## Tool Calling

Yes

## Browser Use

Via skill only — browser work is provided by the Agent Browser skill, not a core capability

## Computer Use

No

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

## Framework

Desktop agent client for Windows, macOS, HarmonyOS PC and Linux (UOS/Kylin), built on Tencent's CodeBuddy architecture. Task execution runs locally in a sandbox; models are routed either to built-in cloud models or to a user-configured OpenAI-compatible endpoint. Extensible through Buddy apps, experts, skills (OpenClaw-compatible), connectors and MCP.

## Pricing

Free tier: 500 credits/month. Standard ¥99/month (2,000 base + 2,000 bonus credits). Advanced ¥199/month (4,000 + 5,000). Flagship ¥999/month (20,000 + 30,000). Buddy One VIP ¥999–1,399/month with a 50,000-credit pool shared across WorkBuddy, Tencent Docs, ima and Tencent Drive. Enterprise pricing quoted separately.

## Deployment

cloud

## Open Source

No

## License

proprietary

## Documentation

https://www.workbuddy.cn/docs/workbuddy/Overview

## Use Cases

- Multi-step office work that ends in a finished file — documents, spreadsheets, slide decks, formatted data
- Batch reading and processing of local files after folder authorisation
- Deep research with cross-source checking and structured report output
- Scheduled and recurring tasks (daily briefs, report generation)
- Remote task dispatch from WeChat, WeCom, QQ, Feishu or DingTalk
- Enterprise agent deployment through the WorkBuddy Managed Agents API, with versioned agents and A/B routing
- Reuse of OpenClaw-format skills and community skill packages

## Limitations

- No built-in GUI or browser control — browser work depends on the Agent Browser skill, not a core operator
- Desktop-first; the mobile app can dispatch tasks but cannot operate desktop files
- Cloud-delivered service — no open-source or self-hosted edition, though a VPC edition is offered to enterprises
- With the built-in models, inputs and outputs are processed in the cloud; only a custom-model configuration keeps content off Tencent's side
- Hunyuan Hy4 preview and Hy3 ship as built-in models but are not yet tracked in this database's model index
- No independent evaluation of task-completion quality is recorded
- Skill quality is uneven at the platform's 200,000-listing scale; skill-scanner reduces but does not eliminate the risk of a malicious package

## Verification Status

verified

## Last Verified

2026-10-31

## Source history

No documented source-change events located as of 2026-10-31.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-workbuddy-1 | WorkBuddy official site (China) | https://www.workbuddy.cn/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-2 | WorkBuddy product documentation | https://www.workbuddy.cn/docs/workbuddy/Overview | Official documentation | — | 2026-10-31 | high | — |
| src-agents-workbuddy-3 | WorkBuddy model configuration documentation | https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model | Official documentation | — | 2026-10-31 | high | — |
| src-agents-workbuddy-4 | WorkBuddy pricing | https://www.workbuddy.cn/pricing/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-5 | WorkBuddy Enterprise Managed Agents API | https://cloud.tencent.com/document/product/1831/138581 | Cloud documentation | 2026-09-23 | 2026-10-31 | high | — |
| src-agents-workbuddy-6 | WorkBuddy open platform | https://open.workbuddy.cn/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-7 | 央广网 — Tencent Digital Ecosystem Summit report | https://tech.cnr.cn/techgd/20261029/t20261029_527856346.shtml | Industry media | 2026-10-29 | 2026-10-31 | high | — |
| src-agents-workbuddy-8 | 极目新闻 — WorkBuddy launch report | https://www.ctdsb.net/c1476_202603/2681903.html | Industry media | 2026-03-10 | 2026-10-31 | medium | Launch-day details (2,000 internal users, 5,000 sign-up credits) differ from later official figures |
