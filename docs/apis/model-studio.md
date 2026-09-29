# Model Studio API

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "APIReference",
      "@id": "https://sinoaihub.com/api/model-studio",
      "name": "Model Studio API",
      "url": "https://sinoaihub.com/api/model-studio",
      "mainEntityOfPage": "https://data.sinoaihub.com/apis/model-studio/",
      "provider": {
        "@type": "Organization",
        "name": "Alibaba Cloud (Qwen)",
        "@id": "https://sinoaihub.com/companies/alibaba-cloud",
        "url": "https://sinoaihub.com/companies/alibaba-cloud"
      },
      "documentation": "https://www.alibabacloud.com/help/en/model-studio/"
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
          "name": "APIs",
          "item": "https://data.sinoaihub.com/apis/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Model Studio API",
          "item": "https://data.sinoaihub.com/apis/model-studio/"
        }
      ]
    }
  ]
}
</script>
> Canonical page on the main site: [sinoaihub.com/api/model-studio](https://sinoaihub.com/api/model-studio)

## Definition

Model Studio API is Alibaba Cloud (Qwen)'s official API platform (endpoint https://dashscope-us.aliyuncs.com/compatible-mode/v1).

## Key facts

- **Endpoint:** https://dashscope-us.aliyuncs.com/compatible-mode/v1
- **Authentication:** API key (DASHSCOPE_API_KEY), created in the Model Studio console; keys are region-bound
- **Capabilities:** streaming, tool calling, structured output, vision
- **Rate limits:** Global regions (Frankfurt / US / Tokyo / Hong Kong): 30,000 RPM, 5,000,000 TPM for qwen3.8-max and qwen3.8-flash; Beijing and Singapore limits are dynamic, tiered by monthly spend

## Provider

[alibaba-cloud](../companies/alibaba-cloud.md)

## Api Type

official

## Endpoint

https://dashscope-us.aliyuncs.com/compatible-mode/v1

## Authentication

API key (DASHSCOPE_API_KEY), created in the Model Studio console; keys are region-bound

## Streaming

Yes

## Function Calling

Yes

## Tool Calling

Yes

## Structured Output

Yes

## Vision

Yes

## Context Limits

| model | input_limit | output_limit |
|---|---|---|
| [qwen3.8-max](../models/qwen3.8-max.md) | 991808 | 131072 |
| [qwen3.8-flash](../models/qwen3.8-flash.md) | 991808 | 131072 |

## Rate Limits

Global regions (Frankfurt / US / Tokyo / Hong Kong): 30,000 RPM, 5,000,000 TPM for qwen3.8-max and qwen3.8-flash; Beijing and Singapore limits are dynamic, tiered by monthly spend

## Regions

- china-beijing
- singapore
- hong-kong
- japan-tokyo
- us-virginia
- germany-frankfurt

## Cloud Providers

- Alibaba Cloud

## Pricing Ref

[alibaba-cloud](../pricing/alibaba-cloud.md)

## Documentation

https://www.alibabacloud.com/help/en/model-studio/

## Last Verified

2026-09-20

## Source history

No documented source-change events located as of 2026-09-20.

## Sources

| source_name | source_url | source_type | last_verified | confidence |
|---|---|---|---|---|
| Model Studio — OpenAI-compatible API | https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope | official | 2026-09-20 | high |
| Model Studio — qwen3.8-max model detail | https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max | official | 2026-09-20 | high |
| Model Studio — qwen3.8-flash model detail | https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash | official | 2026-09-20 | high |
