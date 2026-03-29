from __future__ import annotations

import os

import pytest

from justoneapi import JustOneAPIClient

pytestmark = pytest.mark.skipif(
    not os.getenv("JUSTONEAPI_TOKEN"), reason="JUSTONEAPI_TOKEN not set"
)


@pytest.fixture(scope="module")
def client() -> JustOneAPIClient:
    sdk = JustOneAPIClient(token=os.environ["JUSTONEAPI_TOKEN"])
    try:
        yield sdk
    finally:
        sdk.close()


def test_douyin_video_detail_smoke(client: JustOneAPIClient):
    response = client.douyin.get_video_detail_v2(video_id="7428906452091145483")
    assert response.code is not None
    assert isinstance(response.raw_json, dict)


def test_taobao_item_detail_smoke(client: JustOneAPIClient):
    response = client.taobao.get_item_detail_v1(item_id="765880060015")
    assert response.code is not None
    assert isinstance(response.raw_json, dict)


def test_bilibili_video_detail_smoke(client: JustOneAPIClient):
    response = client.bilibili.get_video_detail_v2(bvid="BV1vk4y1S7dV")
    assert response.code is not None
    assert isinstance(response.raw_json, dict)
