#!/usr/bin/env python3
"""Phase 2B P1-4 — Entity template unification (backfill).

Adds the two genuinely-missing common-core fields to every entity record:

  ## Type                -> model | company | agent | api | benchmark | pricing
  ## Verification Status -> verified | partially_verified

`Type` is derivable from the collection. `Verification Status` is derived
from the existing `last_verified` date + source confidence + whether the
entity's Known Limitations documents core fields as "not publicly disclosed".

Zero fabrication: verification_status is `verified` (core facts checked
against official sources on last_verified) or `partially_verified` (verified,
but one or more core fields — context / architecture / parameters /
capabilities / benchmark results / exact release date — are documented as not
publicly disclosed). The partially-verified set is enumerated explicitly.
"""
import re
from pathlib import Path

COLLECTIONS = ["models", "companies", "agents", "apis", "benchmarks", "pricing"]

TYPE_VALUES = {
    "models": "model",
    "companies": "company",
    "agents": "agent",
    "apis": "api",
    "benchmarks": "benchmark",
    "pricing": "pricing",
}

# Entities whose Known Limitations documents a core field as not publicly
# disclosed / published / stated. Everything else is `verified`.
PARTIALLY_VERIFIED = {
    # models — context / architecture / parameters / capabilities / benchmarks
    ("models", "deepseek-v3-2"),          # context window not stated
    ("models", "doubao-seed-2-1-pro"),    # architecture/params not disclosed
    ("models", "doubao-seed-2-1-turbo"),
    ("models", "doubao-seed-evolving"),
    ("models", "glm-5.3-flashx"),         # context/capabilities/benchmarks not published
    ("models", "kimi-k2.7-code"),         # architecture/params not disclosed
    ("models", "kimi-k2.7-code-highspeed"),
    ("models", "minimax-m2.7"),           # param count + max output not disclosed
    ("models", "minimax-m2.7-highspeed"), # parameter counts not published
    ("models", "minimax-m3"),             # max output not disclosed
    ("models", "qwen3.7-plus"),           # context/capabilities/benchmarks not published
    ("models", "qwen3.8-flash"),          # architecture/params not disclosed
    ("models", "qwen3.8-max"),            # exact API release date not stated
    # apis — capability field not publicly documented
    ("apis", "minimax"),                  # structured_output not documented
}

CANONICAL_LINE = re.compile(r"(^> Canonical page on the main site:.*$)", re.M)


def main():
    updated = 0
    verified = 0
    partial = 0
    for coll in COLLECTIONS:
        for f in sorted(Path(f"docs/{coll}").glob("*.md")):
            if f.name == "index.md":
                continue
            text = f.read_text()
            if "## Type" in text:
                print(f"  SKIP (already has Type): {f}")
                continue
            type_val = TYPE_VALUES[coll]
            status = "partially_verified" if (coll, f.stem) in PARTIALLY_VERIFIED else "verified"
            if status == "verified":
                verified += 1
            else:
                partial += 1

            # Insert ## Type right after the canonical-page blockquote.
            m = CANONICAL_LINE.search(text)
            assert m, f"no canonical line in {f}"
            end = m.end()
            # also consume the following blank line(s) so we don't double-space
            tail = text[end:]
            type_block = f"{text[:end]}\n\n## Type\n\n{type_val}\n"
            new_text = type_block + tail

            # Insert ## Verification Status right before ## Last Verified.
            anchor = "\n## Last Verified\n"
            assert anchor in new_text, f"no Last Verified in {f}"
            new_text = new_text.replace(anchor, f"\n## Verification Status\n\n{status}\n{anchor}", 1)

            f.write_text(new_text)
            updated += 1
            print(f"  {coll}/{f.name}: type={type_val}, status={status}")
    print(f"\n== entity-template summary ==")
    print(f"entities updated: {updated}")
    print(f"verified: {verified}, partially_verified: {partial}")


if __name__ == "__main__":
    main()
