"""mkdocs on_post_build hook: publish clean Markdown per page (Plan A).

Zero-cost alternative to Cloudflare's paid Markdown for Agents:
docs/*.md sources are already clean content (no site chrome), so they
are copied verbatim to site/llms/** and indexed from llms.txt.
"""
import shutil
import pathlib


def on_post_build(config, **kwargs):
    docs_dir = pathlib.Path(config["docs_dir"])
    site_dir = pathlib.Path(config["site_dir"])
    base = config.get("site_url", "").rstrip("/") or "https://data.sinoaihub.com"

    out_root = site_dir / "llms"
    if out_root.exists():
        shutil.rmtree(out_root)

    pages = []
    for f in sorted(docs_dir.rglob("*.md")):
        rel = f.relative_to(docs_dir)
        dst = out_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        content = f.read_text(encoding="utf-8")
        dst.write_text(content, encoding="utf-8")
        slug = str(rel).replace("\\", "/")
        if slug == "index.md":
            url = base + "/"
            md_path = "llms/index.md"
        elif slug.endswith("/index.md"):
            url = base + "/" + slug[: -len("index.md")]
            md_path = "llms/" + slug
        else:
            url = base + "/" + slug[: -3] + "/"
            md_path = "llms/" + slug
        title = "Untitled"
        for line in content.split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                break
        pages.append((title, url, md_path))

    pages.sort(key=lambda x: x[2])

    section = (
        "## Per-page Markdown\n\n"
        + "\n".join(f"- [{t}]({base}/{p})" for t, _, p in pages)
        + "\n\n## Full content\n\n"
        + f"- [All pages in one file]({base}/llms-full.txt)\n"
    )

    llms_txt = site_dir / "llms.txt"
    if llms_txt.exists():
        existing = llms_txt.read_text(encoding="utf-8")
        if "## Per-page Markdown" not in existing:
            llms_txt.write_text(existing.rstrip() + "\n\n" + section, encoding="utf-8")
    else:
        llms_txt.write_text("# China AI Hub Data Hub\n\n" + section, encoding="utf-8")

    full = "\n\n".join(
        f"<!-- {base}/{p} -->\n\n{(docs_dir / p[len('llms/'):]).read_text(encoding='utf-8')}"
        for _, _, p in pages
    )
    (site_dir / "llms-full.txt").write_text(
        "# China AI Hub Data Hub — full content\n" + full + "\n", encoding="utf-8"
    )
