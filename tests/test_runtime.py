from __future__ import annotations

import httpx
import pytest

from justoneapi import JustOneAPIClient
from justoneapi._exceptions import BusinessError, ProtocolError


@pytest.fixture()
def make_client():
    clients: list[JustOneAPIClient] = []

    def _make(handler, *, raise_on_business_error: bool = False) -> JustOneAPIClient:
        client = JustOneAPIClient(
            token="test-token", raise_on_business_error=raise_on_business_error
        )
        client._transport.close()
        client._transport._client = httpx.Client(
            transport=httpx.MockTransport(handler),
            base_url="https://api.justoneapi.com",
            follow_redirects=True,
        )
        clients.append(client)
        return client

    yield _make

    for client in clients:
        client.close()


def test_code_zero_is_success(make_client):
    captured: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["query"] = str(request.url)
        return httpx.Response(
            200, json={"code": 0, "message": "ok", "data": {"value": 1}}
        )

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is True
    assert response.code == 0
    assert response.data == {"value": 1}
    assert "token=test-token" in captured["query"]
    assert "keyword=deepseek" in captured["query"]


def test_non_zero_code_is_failure(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"code": 200, "message": "not ok", "data": {}})

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == 200
    assert response.message == "not ok"


def test_http_error_with_json_payload_returns_api_response(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={"code": 100, "message": "invalid token", "data": None},
        )

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == 100
    assert response.message == "invalid token"


def test_raise_on_business_error(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, json={"code": "300", "message": "quota exceeded", "data": None}
        )

    client = make_client(handler, raise_on_business_error=True)

    with pytest.raises(BusinessError) as excinfo:
        client.search.search_v1(keyword="deepseek")

    assert excinfo.value.response.code == "300"


def test_non_json_response_raises_protocol_error(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, text="not json", headers={"content-type": "text/plain"}
        )

    client = make_client(handler)

    with pytest.raises(ProtocolError):
        client.search.search_v1(keyword="deepseek")


def test_string_zero_is_not_treated_as_success(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"code": "0", "message": "ok", "data": {}})

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == "0"


def test_optional_none_is_omitted_and_bool_is_lowercase(make_client):
    captured: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["query"] = str(request.url)
        return httpx.Response(200, json={"code": 0, "message": "ok", "data": []})

    client = make_client(handler)
    response = client.taobao.search_item_list_v1(
        keyword="bag", sort="_sale", tmall=True, end_price=None
    )

    assert response.success is True
    assert "tmall=true" in captured["query"]
    assert "endPrice" not in captured["query"]
