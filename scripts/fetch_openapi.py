#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.sdk_codegen import (
    DEFAULT_RAW_SPEC_PATH,
    DEFAULT_SPEC_URL,
    dump_json,
    fetch_openapi,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch the JustOneAPI OpenAPI spec with HTTP Basic auth."
    )
    parser.add_argument("--url", default=DEFAULT_SPEC_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_RAW_SPEC_PATH)
    parser.add_argument("--username", default=os.getenv("OPENAPI_BASIC_AUTH_USERNAME"))
    parser.add_argument("--password", default=os.getenv("OPENAPI_BASIC_AUTH_PASSWORD"))
    args = parser.parse_args()

    if not args.username or not args.password:
        raise SystemExit(
            "Both username and password are required. Set OPENAPI_BASIC_AUTH_USERNAME / OPENAPI_BASIC_AUTH_PASSWORD or pass flags."
        )

    spec = fetch_openapi(args.url, args.username, args.password)
    dump_json(spec, args.output)
    print(f"Fetched OpenAPI spec to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
