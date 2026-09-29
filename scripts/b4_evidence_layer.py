#!/usr/bin/env python3
"""Phase 2B P1-5 — Evidence layer unification.

Rewrite every `## Sources` table to a single unified schema:

  evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict

- evidence_id  = src-<collection>-<entity_id>-<n>  (globally unique, stable)
- source_name  = 出处 (provenance label)
- source_url   = URL
- source_type  = mapped from the legacy "official" tag to the new enum:
                 Official | Official documentation | Model card | Vendor-reported |
                 Independent benchmark | China AI Hub analysis | Literature
- published    = source publication date (only where documented; "—" otherwise)
- verified     = verification date (was last_verified)
- confidence   = high | medium | low
- conflict     = "—" unless the entity documents a conflict between sources
                 (only DeepSeek-V4-Pro today)

Zero fabrication: no dates are invented; `published` is "—" when the legacy
table carried no `published_date`.
"""
import re
import sys
from pathlib import Path

COLLECTIONS = ["models", "companies", "agents", "apis", "benchmarks", "pricing"]

# source_type classification. Order matters.
def classify_source_type(name, url):
    n = (name or "").lower()
    u = (url or "").lower()
    if "license" in n:
        return "Official documentation"
    if "model card" in n or "huggingface.co" in u:
        return "Model card"
    # technical / documentation surfaces (including GitHub repos & READMEs)
    if re.search(r"docs|documentation|reference|spec|model page|model list|model detail|"
                 r"pricing|release notes|overview|guide|llms\.txt|readme|repository|"
                 r"github|license file|integration guide|quick ?start|api", n) \
       or re.search(r"docs\.|/docs/|api-docs|\.md|github\.com|help/en|help\.aliyun", u):
        return "Official documentation"
    # announcements / official presence
    if re.search(r"blog|announcement|release|news|official site|official website|homepage|"
                 r"transparency|about|profile|app store|legal|agreement|download|landing|"
                 r"product page|product|launch", n):
        return "Official"
    return "Official"


def parse_sources_table(section_text):
    """Return (header_cells, rows) for a markdown table, or (None, None)."""
    lines = section_text.strip().split("\n")
    if not lines:
        return None, None
    # find header + separator
    header = None
    sep_idx = None
    rows = []
    for i, ln in enumerate(lines):
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("|") and "---" in ln:
            sep_idx = i
            break
        if ln.startswith("|") and header is None:
            header = ln
    if header is None or sep_idx is None:
        return None, None
    header_cells = [c.strip() for c in header.strip().strip("|").split("|")]
    for ln in lines[sep_idx + 1:]:
        ln = ln.strip()
        if ln.startswith("|"):
            rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
    return header_cells, rows


def extract_sources_block(text):
    """Return (prefix, table_text, suffix) where table_text is the Sources table."""
    m = re.search(r"(^## Sources\s*\n\n)(.*?)(\Z)", text, re.S | re.M)
    if not m:
        return None, None, None
    prefix = m.group(1)
    body = m.group(2)
    # the Sources table is the last thing; but guard against trailing H2 (shouldn't happen)
    return prefix, body, ""


def main(dry_run=False):
    total_files = 0
    total_rows = 0
    type_dist = {}
    conf_dist = {}
    conflict_count = 0
    for coll in COLLECTIONS:
        for f in sorted(Path(f"docs/{coll}").glob("*.md")):
            if f.name == "index.md":
                continue
            text = f.read_text()
            i = text.find("## Sources")
            if i == -1:
                print(f"  WARN: no Sources in {f}")
                continue
            section = text[i:]
            header, rows = parse_sources_table(section)
            if header is None:
                print(f"  WARN: no parseable table in {f}")
                continue
            # map legacy columns
            idx = {h: k for k, h in enumerate(header)}
            entity_id = f.stem
            new_header = ["evidence_id", "source_name", "source_url", "source_type",
                          "published", "verified", "confidence", "conflict"]
            new_rows = []
            for n, row in enumerate(rows, 1):
                def get(*names):
                    for nm in names:
                        if nm in idx and idx[nm] < len(row):
                            return row[idx[nm]]
                    return ""
                source_name = get("source_name")
                source_url = get("source_url")
                published = get("published_date")
                verified = get("last_verified")
                confidence = get("confidence") or "high"
                conflict = "—"
                if entity_id == "deepseek-v4-pro" and "Change Log" in source_name:
                    conflict = "Conflicts with the same-day deprecation announcement (V4-Pro → V4.1-Flash routing)"
                    conflict_count += 1
                if published in ("", "—", "-"):
                    published = "—"
                if verified in ("", "—", "-"):
                    verified = ""
                st = classify_source_type(source_name, source_url)
                type_dist[st] = type_dist.get(st, 0) + 1
                conf_dist[confidence] = conf_dist.get(confidence, 0) + 1
                new_rows.append([f"src-{coll}-{entity_id}-{n}", source_name, source_url,
                                 st, published, verified, confidence, conflict])
            total_files += 1
            total_rows += len(new_rows)
            # render
            out = []
            out.append("| " + " | ".join(new_header) + " |")
            out.append("|" + "|".join(["---"] * len(new_header)) + "|")
            for row in new_rows:
                out.append("| " + " | ".join(row) + " |")
            new_table = "\n".join(out)
            # replace: keep everything before "## Sources" + new Sources block
            new_text = text[:i] + "## Sources\n\n" + new_table + "\n"
            if dry_run:
                pass
            else:
                f.write_text(new_text)
            print(f"  {coll}/{f.name}: {len(new_rows)} sources")
    print(f"\n== evidence-layer summary ==")
    print(f"files updated: {total_files}")
    print(f"evidence rows: {total_rows}")
    print(f"source_type distribution: {type_dist}")
    print(f"confidence distribution: {conf_dist}")
    print(f"conflict annotations: {conflict_count}")


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    if dry:
        print("DRY RUN — no files written\n")
    main(dry_run=dry)
