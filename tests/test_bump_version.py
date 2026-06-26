from __future__ import annotations

import pytest

from scripts.bump_version import bump_patch_version


def test_bump_patch_version_updates_version_file(tmp_path):
    version_path = tmp_path / "_version.py"
    version_path.write_text('__version__ = "3.0.5"\n')

    assert bump_patch_version(version_path) == "3.0.6"
    assert version_path.read_text() == '__version__ = "3.0.6"\n'


def test_bump_patch_version_rejects_unsupported_format(tmp_path):
    version_path = tmp_path / "_version.py"
    version_path.write_text('__version__ = "3.0.5.dev0"\n')

    with pytest.raises(ValueError):
        bump_patch_version(version_path)
