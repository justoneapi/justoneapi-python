from __future__ import annotations

from pathlib import Path

from tools.sdk_codegen import (
    build_diff_summary,
    collect_resources,
    load_json,
    load_overrides,
    normalize_spec,
)

RAW_SPEC_PATH = Path("openapi/public-api.json")
OVERRIDES_PATH = Path("openapi/sdk_overrides.yaml")


def test_normalize_spec_removes_token_and_adds_security_scheme():
    normalized = normalize_spec(
        load_json(RAW_SPEC_PATH), load_overrides(OVERRIDES_PATH)
    )
    search_operation = normalized["paths"]["/api/search/v1"]["get"]

    assert search_operation["x-sdk-resource"] == "search"
    assert search_operation["x-sdk-method-name"] == "search_v1"
    assert all(
        parameter["name"] != "token" for parameter in search_operation["parameters"]
    )
    assert normalized["components"]["securitySchemes"]["tokenAuth"]["name"] == "token"


def test_collect_resources_matches_expected_counts():
    normalized = normalize_spec(
        load_json(RAW_SPEC_PATH), load_overrides(OVERRIDES_PATH)
    )
    resources = collect_resources(normalized)

    assert len(resources) == 25
    assert sum(len(resource.operations) for resource in resources) == 201
    namespace_set = {resource.namespace for resource in resources}
    assert {"douyin", "douyin_xingtu", "tiktok_shop", "xiaohongshu_pgy"}.issubset(
        namespace_set
    )


def test_diff_summary_reports_operation_changes():
    old_spec = {
        "paths": {
            "/api/demo/v1": {
                "get": {"operationId": "demoV1", "summary": "old"},
            }
        },
        "tags": [],
    }
    new_spec = {
        "paths": {
            "/api/demo/v1": {
                "get": {"operationId": "demoV1", "summary": "new"},
            },
            "/api/demo/v2": {
                "get": {"operationId": "demoV2", "summary": "added"},
            },
        },
        "tags": [],
    }

    summary = build_diff_summary(old_spec, new_spec)

    assert "demoV2 [GET /api/demo/v2]" in summary
    assert "demoV1 [GET /api/demo/v1]" in summary
    assert "Changed operationId count: 1" in summary
