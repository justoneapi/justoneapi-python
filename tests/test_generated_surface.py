from __future__ import annotations

from pathlib import Path

from justoneapi import JustOneAPIClient
from justoneapi.generated.models import Result
from justoneapi.generated.resources import RESOURCE_CLASSES
from tools.sdk_codegen import load_json

NORMALIZED_SPEC_PATH = Path("openapi/public-api.normalized.json")


def expected_resource_namespaces() -> set[str]:
    spec = load_json(NORMALIZED_SPEC_PATH)
    return {
        operation["x-sdk-resource"]
        for path_item in spec.get("paths", {}).values()
        for method, operation in path_item.items()
        if not method.startswith("x-")
    }


def test_generated_resource_registry_matches_public_api_surface():
    assert set(RESOURCE_CLASSES) == expected_resource_namespaces()
    assert {"douyin", "douyin_xingtu", "xiaohongshu_pgy", "twitter"}.issubset(
        RESOURCE_CLASSES
    )


def test_client_exposes_generated_resources():
    client = JustOneAPIClient(token="test-token")
    try:
        assert type(client.douyin).__name__ == "DouyinResource"
        assert type(client.douyin_xingtu).__name__ == "DouyinXingtuResource"
        assert type(client.xiaohongshu_pgy).__name__ == "XiaohongshuPgyResource"
        assert hasattr(client.search, "search_v1")
        assert hasattr(client.weixin, "get_article_comment_v1")
        assert hasattr(client.weixin, "get_article_feedback_v1")
        assert hasattr(client.weixin, "get_user_post_v1")
        assert hasattr(client.bilibili, "get_user_relation_stat_v1")
        assert hasattr(client.bilibili, "get_video_caption_v2")
        assert hasattr(client.douyin, "get_video_detail_v2")
        assert hasattr(client.twitter, "get_user_posts_v1")
    finally:
        client.close()


def test_generated_result_model_accepts_generic_payload():
    result = Result.model_validate({"code": "0", "message": "ok", "data": {"x": 1}})
    assert result.message == "ok"
    assert result.data == {"x": 1}
