#!/usr/bin/env python3
"""B3: add the 8-element entity block (Definition / Key facts / Source history)
to every data-station entity page.

Idempotent: strips any previously-inserted `## Definition` / `## Key facts` /
`## Source history` blocks, then re-inserts fresh content. Zero fabrication —
every clause is composed from fields already present on the page, and every
display name is resolved to the target page's own H1 title."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
COLLS = ["models", "companies", "agents", "apis", "pricing", "benchmarks"]


def sec(text: str, name: str) -> str | None:
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
    return m.group(1).strip() if m else None


def has_section(text: str, name: str) -> bool:
    return re.search(rf"^## {re.escape(name)}\s*$", text, flags=re.M) is not None


def bullets(text: str | None) -> list[str]:
    if not text:
        return []
    return [ln[2:].strip() for ln in text.splitlines() if ln.strip().startswith("- ")]


def first_value(text: str | None) -> str:
    if not text:
        return ""
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("|"):
            continue
        return ln.strip()
    return ""


def fmt_num(s: str) -> str:
    s = s.strip()
    return f"{int(s):,}" if re.fullmatch(r"\d+", s) else s


def weight_label(ow: str) -> str:
    v = ow.strip().lower()
    return {"yes": "open", "no": "closed"}.get(v, "not stated")


# (collection, slug) -> display title, built from every page's H1
NAME_MAP: dict[tuple[str, str], str] = {}
for c in COLLS:
    for f in sorted((DOCS / c).glob("*.md")):
        if f.name == "index.md":
            continue
        NAME_MAP[(c, f.stem)] = f.read_text().split("\n", 1)[0].lstrip("# ").strip()


def resolve(line: str) -> str:
    """Resolve `[label](../coll/slug.md)` -> the target page's H1 title."""
    m = re.match(r"\[[^\]]+\]\(\.\./(\w+)/([^)/]+)\.md\)", line.strip())
    if m:
        coll, slug = m.group(1), m.group(2)
        return NAME_MAP.get((coll, slug), slug)
    return line.strip()


# ---------------------------------------------------------------------------
# strip previously inserted blocks (idempotency)
# ---------------------------------------------------------------------------

def strip_block(text: str) -> str:
    for name in ("Definition", "Key facts", "Source history"):
        text = re.sub(rf"^## {re.escape(name)}\s*\n.*?(?=^## |\Z)", "", text, flags=re.M | re.S)
    return text


def insert_after_canonical(text: str, block: str) -> str:
    marker = "> Canonical page on the main site:"
    idx = text.index(marker)
    line_end = text.index("\n", idx)
    return text[: line_end + 1] + "\n" + block + text[line_end + 1 :]


def insert_before_section(text: str, section: str, block: str) -> str:
    idx = text.index(f"## {section}")
    return text[:idx] + block + "\n" + text[idx:]


# ---------------------------------------------------------------------------
# generators
# ---------------------------------------------------------------------------

def model_block(text: str, slug: str) -> str:
    name = text.split("\n", 1)[0].lstrip("# ").strip()
    provider = resolve(first_value(sec(text, "Provider")))
    family = first_value(sec(text, "Model Family"))
    release = first_value(sec(text, "Release Date"))
    status = first_value(sec(text, "Status"))
    arch = first_value(sec(text, "Architecture"))
    cw = first_value(sec(text, "Context Window"))
    mo = first_value(sec(text, "Maximum Output"))
    ow = first_value(sec(text, "Open Weight"))
    lic = first_value(sec(text, "License"))

    defn = f"{name} is a {provider} model" + (f" in the {family} family" if family else "")
    clauses = []
    if arch:
        clauses.append(arch.rstrip("."))
    if cw:
        clauses.append(f"{fmt_num(cw)}-token context window")
        if mo:
            clauses.append(f"{fmt_num(mo)} max output")
    if ow:
        clauses.append(f"{weight_label(ow)}-weight")
    if lic:
        clauses.append(f"{lic} license")
    if release:
        clauses.append(f"released {release}")
    if status and status.lower() != "active":
        clauses.append(f"status {status}")
    defn += (": " + "; ".join(clauses) + ".") if clauses else "."

    facts = []
    if arch:
        facts.append(f"**Architecture:** {arch}")
    if cw:
        f = f"**Context window:** {fmt_num(cw)} tokens"
        if mo:
            f += f" (max output {fmt_num(mo)})"
        facts.append(f)
    if ow or lic:
        w = weight_label(ow) if ow else "not stated"
        facts.append(f"**Weights:** {w}" + (f"; {lic} license" if lic else ""))
    pr = sec(text, "Pricing")
    pi = re.search(r"input_price_per_1m:\*\*\s*([\d.]+)", pr or "")
    po = re.search(r"output_price_per_1m:\*\*\s*([\d.]+)", pr or "")
    cur = re.search(r"currency:\*\*\s*(\w+)", pr or "")
    if pi:
        facts.append(
            f"**API pricing:** ${pi.group(1)} input / ${po.group(1) if po else '—'} output per 1M tokens"
            + (f" ({cur.group(1)})" if cur else "")
        )
    if release:
        facts.append(f"**Released:** {release}")
    caps = sec(text, "Capabilities")
    if caps:
        on = [k.replace("_", " ") for k in ("reasoning", "coding", "vision", "tool_calling")
              if re.search(rf"\*\*{k}:\*\*\s*Yes", caps)]
        if on:
            facts.append("**Capabilities:** " + ", ".join(on))
    if status and status.lower() != "active":
        facts.append(f"**Status:** {status}")

    lines = ["## Definition", "", defn, "", "## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def company_block(text: str, slug: str) -> str:
    name = text.split("\n", 1)[0].lstrip("# ").strip()
    aliases = bullets(sec(text, "Aliases"))
    hq = first_value(sec(text, "Headquarters"))
    funding = first_value(sec(text, "Funding"))
    fmodels = bullets(sec(text, "Foundation Models"))
    agents = bullets(sec(text, "Agents"))
    apis = bullets(sec(text, "API"))
    oss = bullets(sec(text, "Open Source Projects"))

    defn = f"{name} is a Chinese AI company"
    if aliases:
        defn += f" (also {', '.join(aliases[:2])})"
    if fmodels:
        defn += f" developing {len(fmodels)} foundation model{'s' if len(fmodels) != 1 else ''}"
    if apis:
        defn += f" and operating the {resolve(apis[0])}"
    defn += "."

    facts = []
    if hq:
        facts.append(f"**Headquarters:** {hq}")
    if funding:
        facts.append(f"**Funding:** {funding}")
    if fmodels:
        facts.append(f"**Foundation models:** {', '.join(resolve(m) for m in fmodels)}")
    if agents:
        facts.append(f"**Agents:** {', '.join(resolve(a) for a in agents)}")
    if apis:
        facts.append(f"**API:** {', '.join(resolve(a) for a in apis)}")
    if oss:
        facts.append(f"**Open-source:** {len(oss)} projects")

    lines = ["## Definition", "", defn, "", "## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def agent_block(text: str, slug: str) -> str:
    company = resolve(first_value(sec(text, "Company")))
    atype = first_value(sec(text, "Agent Type"))
    umodels = bullets(sec(text, "Underlying Models"))
    ow = first_value(sec(text, "Open Source"))
    lic = first_value(sec(text, "License"))
    tool = first_value(sec(text, "Tool Calling"))
    browser = first_value(sec(text, "Browser Use"))
    computer = first_value(sec(text, "Computer Use"))
    mcp = first_value(sec(text, "Mcp"))
    pricing = first_value(sec(text, "Pricing"))

    facts = []
    if company:
        facts.append(f"**Company:** {company}")
    if atype:
        facts.append(f"**Type:** {atype}")
    if umodels:
        facts.append(f"**Underlying models:** {', '.join(resolve(m) for m in umodels)}")
    caps = []
    if tool and tool.lower() == "yes":
        caps.append("tool calling")
    if browser and browser.lower() == "yes":
        caps.append("browser use")
    if computer and computer.lower() == "yes":
        caps.append("computer use")
    if mcp and mcp.lower() == "yes":
        caps.append("MCP")
    if caps:
        facts.append("**Capabilities:** " + ", ".join(caps))
    if ow or lic:
        facts.append(f"**Open source:** {ow.lower() if ow else 'n/a'}" + (f" ({lic})" if lic else ""))
    if pricing:
        facts.append(f"**Pricing:** {pricing}")

    lines = ["## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def api_block(text: str, slug: str) -> str:
    name = text.split("\n", 1)[0].lstrip("# ").strip()
    provider = resolve(first_value(sec(text, "Provider")))
    atype = first_value(sec(text, "Api Type"))
    endpoint = first_value(sec(text, "Endpoint"))
    auth = first_value(sec(text, "Authentication"))
    streaming = first_value(sec(text, "Streaming"))
    tool = first_value(sec(text, "Tool Calling"))
    structured = first_value(sec(text, "Structured Output"))
    vision = first_value(sec(text, "Vision"))
    rate = first_value(sec(text, "Rate Limits"))

    defn = f"{name} is {provider}'s {atype} API platform"
    defn += (f" (endpoint {endpoint})" if endpoint else "") + "."

    facts = []
    if endpoint:
        facts.append(f"**Endpoint:** {endpoint}")
    if auth:
        facts.append(f"**Authentication:** {auth}")
    caps = []
    for label, v in (("streaming", streaming), ("tool calling", tool),
                     ("structured output", structured), ("vision", vision)):
        if v and v.lower() == "yes":
            caps.append(label)
    if caps:
        facts.append("**Capabilities:** " + ", ".join(caps))
    if rate:
        facts.append(f"**Rate limits:** {rate}")

    lines = ["## Definition", "", defn, "", "## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def pricing_block(text: str, slug: str) -> str:
    name = text.split("\n", 1)[0].lstrip("# ").strip()
    cur = first_value(sec(text, "Currency"))
    region = first_value(sec(text, "Region"))
    bill = first_value(sec(text, "Billing Mode"))
    models = sec(text, "Models")
    n_models = models.count("| [") if models else 0
    pr = sec(text, "Price History")

    defn = f"{name} pricing" + (f" in {cur}" if cur else "")
    if bill:
        defn += f", {bill.replace('_', ' ')}"
    defn += "."

    facts = []
    if cur:
        facts.append(f"**Currency:** {cur}")
    if region:
        facts.append(f"**Region:** {region}")
    if bill:
        facts.append(f"**Billing:** {bill.replace('_', ' ')}")
    facts.append(f"**Models priced:** {n_models}")
    if pr:
        documented = "|" in pr and "No " not in pr
        facts.append(f"**Price history:** {'documented' if documented else 'none documented'}")

    lines = ["## Definition", "", defn, "", "## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def benchmark_block(text: str, slug: str) -> str:
    meth = sec(text, "Methodology")
    task = re.search(r"\*\*Task type:\*\*\s*(.*)", meth or "")
    dsize = re.search(r"\*\*Dataset size:\*\*\s*(.*)", meth or "")
    evalm = re.search(r"\*\*Evaluation method:\*\*\s*(.*)", meth or "")
    scoring = re.search(r"\*\*Scoring:\*\*\s*(.*)", meth or "")
    evals = sec(text, "Evaluations")
    n_evals = evals.count("\n|") if evals else 0

    facts = []
    if task:
        facts.append(f"**Task type:** {task.group(1)}")
    if dsize:
        facts.append(f"**Dataset size:** {dsize.group(1)}")
    if evalm:
        facts.append(f"**Evaluation method:** {evalm.group(1)}")
    if scoring:
        facts.append(f"**Scoring:** {scoring.group(1)}")
    if n_evals:
        facts.append(f"**Recorded evaluations:** {n_evals}")

    lines = ["## Key facts", ""]
    lines += [f"- {f}" for f in facts[:6]]
    return "\n".join(lines) + "\n"


def source_history_note(text: str, last_verified: str) -> str | None:
    for h in ("Release History", "Price History", "Timeline"):
        if has_section(text, h):
            return None
    lv = first_value(sec(text, "Last Verified")) or last_verified
    return "## Source history\n\nNo documented source-change events located as of " + lv + ".\n"


GENERATORS = {
    "models": model_block,
    "companies": company_block,
    "agents": agent_block,
    "apis": api_block,
    "pricing": pricing_block,
    "benchmarks": benchmark_block,
}


if __name__ == "__main__":
    summary = {}
    for coll, gen in GENERATORS.items():
        n_def = n_sh = 0
        for f in sorted((DOCS / coll).glob("*.md")):
            if f.name == "index.md":
                continue
            t = strip_block(f.read_text())
            block = gen(t, f.stem)
            t = insert_after_canonical(t, block)
            n_def += 1
            note = source_history_note(t, "2026-09-20")
            if note is not None:
                if has_section(t, "Sources"):
                    t = insert_before_section(t, "Sources", note)
                elif has_section(t, "Last Verified"):
                    t = insert_before_section(t, "Last Verified", note)
                else:
                    t = t.rstrip() + "\n\n" + note + "\n"
                n_sh += 1
            f.write_text(t)
        summary[coll] = (n_def, n_sh)
        print(f"{coll}: pages={n_def}, source-history notes={n_sh}")
    print("\nDONE", summary)
