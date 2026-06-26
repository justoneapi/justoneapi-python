#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_VERSION_PATH = Path("justoneapi/_version.py")
VERSION_RE = re.compile(r'^__version__ = "(\d+)\.(\d+)\.(\d+)"\s*$')


def bump_patch_version(path: Path) -> str:
    content = path.read_text()
    match = VERSION_RE.fullmatch(content.strip())
    if not match:
        raise ValueError(
            f"{path} must contain a single __version__ = \"X.Y.Z\" assignment"
        )

    major, minor, patch = (int(part) for part in match.groups())
    next_version = f"{major}.{minor}.{patch + 1}"
    path.write_text(f'__version__ = "{next_version}"\n')
    return next_version


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump the package patch version.")
    parser.add_argument("--path", type=Path, default=DEFAULT_VERSION_PATH)
    args = parser.parse_args()

    print(bump_patch_version(args.path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
