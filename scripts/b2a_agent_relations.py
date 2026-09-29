#!/usr/bin/env python3
"""B2-a data-station sync: link Underlying Models to model pages and add
Agent -> API relationship field to each data-station agent page."""
import re
from pathlib import Path

AGENTS_DIR = Path("docs/agents")

# agent -> company api entity (from company frontmatter `api` field)
AGENT_TO_API = {
    "autoglm": "zai",
    "deepseek-harness": "deepseek",
    "doubao-app": "ark",
    "glm-coding-plan": "zai",
    "kimi-code": "moonshot",
    "minimax-agent": "minimax",
    "minimax-code": "minimax",
    "qoder": "model-studio",
    "qwen-agent": "model-studio",
    "qwen-code": "model-studio",
}

# model display names for link text
MODEL_NAMES = {
    "deepseek-v3-2": "DeepSeek-V3.2",
    "deepseek-v4-1-flash": "DeepSeek-V4.1-Flash",
    "deepseek-v4-pro": "DeepSeek-V4-Pro",
    "doubao-seed-2-1-pro": "Doubao Seed 2.1 Pro",
    "doubao-seed-2-1-turbo": "Doubao Seed 2.1 Turbo",
    "doubao-seed-evolving": "Doubao Seed Evolving",
    "glm-5.2": "GLM-5.2",
    "glm-5.3-flash": "GLM-5.3-Flash",
    "glm-5.3-flashx": "GLM-5.3-FlashX",
    "glm-5.3": "GLM-5.3",
    "kimi-k2.6": "Kimi K2.6",
    "kimi-k2.7-code-highspeed": "Kimi K2.7 Code Highspeed",
    "kimi-k2.7-code": "Kimi K2.7 Code",
    "kimi-k3": "Kimi K3",
    "minimax-m2.7-highspeed": "MiniMax-M2.7-Highspeed",
    "minimax-m2.7": "MiniMax-M2.7",
    "minimax-m3": "MiniMax-M3",
    "qwen3.7-plus": "Qwen3.7-Plus",
    "qwen3.8-2.4t-a95b": "Qwen3.8-2.4T-A95B",
    "qwen3.8-flash": "Qwen3.8-Flash",
    "qwen3.8-max": "Qwen3.8-Max",
}


def link_models(text: str) -> str:
    """Convert plain model-id bullets under ## Underlying Models to links."""
    def repl(m):
        mid = m.group(1).strip()
        name = MODEL_NAMES.get(mid, mid)
        return f"- [{name}](../models/{mid}.md)"
    # only inside the Underlying Models section
    lines = text.split("\n")
    out = []
    in_section = False
    for line in lines:
        if line.startswith("## Underlying Models"):
            in_section = True
            out.append(line)
            continue
        if in_section:
            if line.startswith("## "):
                in_section = False
                out.append(line)
                continue
            if line.startswith("- "):
                mid = line[2:].strip()
                name = MODEL_NAMES.get(mid, mid)
                out.append(f"- [{name}](../models/{mid}.md)")
                continue
            # blank or other -> keep
        out.append(line)
    return "\n".join(out)


def add_api(text: str, api_id: str) -> str:
    """Insert an `## API Platform` relationship section after `## Company`."""
    if "## API Platform" in text:
        return text
    # find the Company link block: "## Company\n\n[xxx](../companies/xxx.md)\n\n"
    m = re.search(r"(## Company\n\n\[[^\]]+\]\(\.\./companies/[^)]+\.md\)\n)", text)
    if not m:
        raise SystemExit(f"no Company block found for api_id={api_id}")
    insert = m.group(1) + f"\n## API Platform\n\n- [{api_id}](../apis/{api_id}.md)\n"
    return text[:m.start()] + insert + text[m.end():]


for f in sorted(AGENTS_DIR.glob("*.md")):
    if f.name == "index.md":
        continue
    slug = f.stem
    text = f.read_text()
    text = link_models(text)
    text = add_api(text, AGENT_TO_API[slug])
    f.write_text(text)
    print(f"updated {f.name} -> api {AGENT_TO_API[slug]}")
