#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdk_codegen import build_diff_summary, load_json


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Diff two OpenAPI specs and emit a markdown summary."
    )
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    summary = build_diff_summary(load_json(args.old), load_json(args.new))
    if args.output:
        args.output.write_text(summary + "\n")
        print(f"Wrote diff summary to {args.output}")
    else:
        print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
