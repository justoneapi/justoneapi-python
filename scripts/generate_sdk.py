#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdk_codegen import DEFAULT_NORMALIZED_SPEC_PATH, generate_sdk


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate the JustOneAPI SDK surface from a normalized OpenAPI spec."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_NORMALIZED_SPEC_PATH)
    args = parser.parse_args()

    resources = generate_sdk(args.input)
    print(
        f"Generated {sum(len(resource.operations) for resource in resources)} operations across {len(resources)} resources."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
