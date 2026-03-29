from __future__ import annotations

from justoneapi import JustOneAPIClient
from justoneapi.generated.models import Result
from justoneapi.generated.resources import RESOURCE_CLASSES


def test_generated_resource_registry_matches_public_api_surface():
    assert len(RESOURCE_CLASSES) == 25
    assert "douyin" in RESOURCE_CLASSES
    assert "douyin_xingtu" in RESOURCE_CLASSES
    assert "xiaohongshu_pgy" in RESOURCE_CLASSES
    assert "twitter" in RESOURCE_CLASSES


def test_client_exposes_generated_resources():
    client = JustOneAPIClient(token="test-token")
    try:
        assert type(client.douyin).__name__ == "DouyinResource"
        assert type(client.douyin_xingtu).__name__ == "DouyinXingtuResource"
        assert type(client.xiaohongshu_pgy).__name__ == "XiaohongshuPgyResource"
        assert hasattr(client.search, "search_v1")
        assert hasattr(client.douyin, "get_video_detail_v2")
        assert hasattr(client.twitter, "get_user_posts_v1")
    finally:
        client.close()


def test_generated_result_model_accepts_generic_payload():
    result = Result.model_validate({"code": "0", "message": "ok", "data": {"x": 1}})
    assert result.message == "ok"
    assert result.data == {"x": 1}
