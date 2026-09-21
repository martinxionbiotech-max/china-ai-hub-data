# AutoGLM

> Canonical page on the main site: [chinaaihub.com/agents/autoglm](https://chinaaihub.com/agents/autoglm)

## Company

[zhipu-ai](../companies/zhipu-ai.md)

## Description

Zhipu AI's open-source phone-use autonomous agent (repo Open-AutoGLM). The VLM sees the phone screen, plans a chain-of-thought action sequence, and executes it via ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). First phone agent with true Phone Use capabilities (2024-10-25); AutoGLM 2.0 commercial product runs agents in cloud virtual phones. Research/learning use.

## Agent Type

autonomous

## Framework

Python framework (PhoneAgent API + CLI); model AutoGLM-Phone-9B built on the GLM-4.1V-9B family

## Tool Calling

Yes

## Computer Use

Yes

## Memory

No

## Planning

Yes

## Api

Yes

## Pricing

Open-source framework free. AutoGLM-Phone API (BigModel model id autoglm-phone) limited-time free as of 2026-09-20; paid price after promotion not publicly disclosed.

## Deployment

both

## Open Source

Yes

## License

Apache-2.0 (code); MIT (models)

## Github

https://github.com/zai-org/Open-AutoGLM

## Documentation

https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md

## Use Cases

- Food delivery ordering and reordering
- Product purchase and cross-platform price comparison
- Travel planning (routes, flights/trains, hotels)
- News, music, video playback and social interactions
- Cloud-phone batch operations - notifications, likes, customer-service and attendance workflows
- AI-native phone research and GUI agent development

## Limitations

- Research/learning use only; prohibited for illegal information gathering
- Sensitive pages (payment, password, banking) cannot be screenshotted - agent auto-detects and requests human takeover
- Android 7.0+ with developer mode + USB debugging required; ADB Keyboard needed for Android text input
- iOS support requires separate WebDriverAgent setup
- Local deployment needs ~24GB+ VRAM GPU
- No persistent-memory feature documented in the README

## Last Verified

2026-09-20

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Open-AutoGLM GitHub repository | https://github.com/zai-org/Open-AutoGLM | official | 2026-09-20 | high |
| AutoGLM Goes Open Source blog | https://autoglm.z.ai/blog | official | 2026-09-20 | high |
| AutoGLM-Phone model card (Hugging Face) | https://huggingface.co/zai-org/AutoGLM-Phone-9B | official | 2026-09-20 | high |
| BigModel AutoGLM-Phone API docs | https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md | official | 2026-09-20 | high |
