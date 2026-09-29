#!/usr/bin/env python3
"""Phase 2B P1-6 — History-data extension (zero fabrication).

Extends the existing history dimensions (release_history / price_history /
timeline) with five new structured dimensions where evidence exists, and an
explicit "No documented changes on record" annotation where it does not:

  model_versions     — documented version sequence (date-coded / checkpoint snapshots)
  license_changes    — license change events (none documented anywhere)
  api_changes        — API change records (DeepSeek only)
  company_milestones — covered by the existing timeline (no new field)
  benchmark_changes  — before/after benchmark values (none sourced)

Every row added here is traceable to content already in the entity record
(Version / Aliases / Release History / the API Change Log). No dates, versions
or scores are invented; absent evidence is stated explicitly.
"""
import re
from pathlib import Path

# model_versions: documented version snapshots, sourced from the entity's
# existing Version/Aliases/Release History. date "—" = no sourced date.
MODEL_VERSIONS = {
    "deepseek-v4-pro": [
        ("V4 Preview", "2026-04-24", "https://www.deepseek.com/en/news/v4-preview/"),
        ("0813 (GA)", "2026-08-13", "https://api-docs.deepseek.com/updates"),
    ],
    "qwen3.8-max": [
        ("initial", "2026-08", "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"),
        ("0902", "2026-09-02", "https://www.qwencloud.com/models/qwen3.8-max-0902"),
    ],
    "doubao-seed-2-1-pro": [
        ("260628", "—", "https://docs.volcengine.com/docs/ark/model-list?lang=zh"),
        ("260915", "2026-09", "https://docs.volcengine.com/docs/ark/model-release-announcement"),
    ],
    "doubao-seed-2-1-turbo": [
        ("260628", "—", "https://docs.volcengine.com/docs/ark/model-list?lang=zh"),
    ],
    "doubao-seed-evolving": [
        ("rolling", "—", "https://docs.volcengine.com/docs/ark/model-release-announcement"),
    ],
}

# api_changes: documented API-platform changes (DeepSeek Change Log).
API_CHANGES = {
    "deepseek": [
        ("2026-08-13", "DeepSeek-V4-Pro GA (0813) shipped on the API",
         "https://api-docs.deepseek.com/updates"),
        ("2026-08-16", "Peak/off-peak pricing introduced (peak = 2x off-peak)",
         "https://api-docs.deepseek.com/updates"),
        ("2026-09-10", "V4-Pro deprecation announced then reversed the same day; V4.1-Flash released",
         "https://api-docs.deepseek.com/updates"),
    ],
}

AS_OF = "2026-09-29"


def insert_before_last_verified(text, block):
    anchor = "\n## Last Verified\n"
    assert anchor in text, "no Last Verified anchor"
    return text.replace(anchor, block + anchor, 1)


def main():
    counts = {"model_versions": 0, "license_changes": 0, "api_changes": 0,
              "benchmark_changes": 0}
    skipped = {"model_versions": [], "license_changes": [], "api_changes": [],
               "benchmark_changes": []}

    # models: model_versions + license_changes
    for f in sorted(Path("docs/models").glob("*.md")):
        if f.name == "index.md":
            continue
        text = f.read_text()
        block = ""
        stem = f.stem
        # model_versions
        if stem in MODEL_VERSIONS:
            rows = MODEL_VERSIONS[stem]
            lines = ["\n## Model Versions\n",
                     "| version | date | source | verification_date |",
                     "|---|---|---|---|"]
            for version, date, src in rows:
                lines.append(f"| {version} | {date} | {src} | {AS_OF} |")
            block += "\n".join(lines) + "\n"
            counts["model_versions"] += 1
        else:
            skipped["model_versions"].append(stem)
        # license_changes — none documented anywhere
        block += (f"\n## License Changes\n\nNo documented license changes on record as of {AS_OF}.\n")
        counts["license_changes"] += 1
        f.write_text(insert_before_last_verified(text, block))
        print(f"  models/{f.name}: model_versions={'Y' if stem in MODEL_VERSIONS else 'n'}, license_changes=n")

    # apis: api_changes
    for f in sorted(Path("docs/apis").glob("*.md")):
        if f.name == "index.md":
            continue
        text = f.read_text()
        stem = f.stem
        block = ""
        if stem in API_CHANGES:
            lines = ["\n## API Changes\n",
                     "| date | change | source | verification_date |",
                     "|---|---|---|---|"]
            for date, change, src in API_CHANGES[stem]:
                lines.append(f"| {date} | {change} | {src} | {AS_OF} |")
            block += "\n".join(lines) + "\n"
            counts["api_changes"] += 1
        else:
            block = f"\n## API Changes\n\nNo documented API changes on record as of {AS_OF}.\n"
            skipped["api_changes"].append(stem)
        f.write_text(insert_before_last_verified(text, block))
        print(f"  apis/{f.name}: api_changes={'Y' if stem in API_CHANGES else 'n'}")

    # benchmarks: benchmark_changes
    for f in sorted(Path("docs/benchmarks").glob("*.md")):
        if f.name == "index.md":
            continue
        text = f.read_text()
        block = f"\n## Benchmark Changes\n\nNo documented benchmark changes on record as of {AS_OF}.\n"
        f.write_text(insert_before_last_verified(text, block))
        counts["benchmark_changes"] += 1
        skipped["benchmark_changes"].append(f.stem)
        print(f"  benchmarks/{f.name}: benchmark_changes=n")

    print("\n== history-data summary ==")
    print("counts:", counts)
    print("skipped (no evidence):")
    for k, v in skipped.items():
        print(f"  {k}: {len(v)} -> {v}")


if __name__ == "__main__":
    main()
