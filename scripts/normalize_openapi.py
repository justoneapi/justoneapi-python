#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdk_codegen import (
    DEFAULT_NORMALIZED_SPEC_PATH,
    DEFAULT_OVERRIDES_PATH,
    DEFAULT_RAW_SPEC_PATH,
    dump_json,
    load_json,
    load_overrides,
    normalize_spec,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize the JustOneAPI OpenAPI spec for SDK generation."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_RAW_SPEC_PATH)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_NORMALIZED_SPEC_PATH)
    args = parser.parse_args()

    normalized = normalize_spec(load_json(args.input), load_overrides(args.overrides))
    dump_json(normalized, args.output)
    print(f"Normalized OpenAPI spec to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
