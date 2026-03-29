![PyPI version](https://img.shields.io/pypi/v/justoneapi.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

[English](README.md) | [简体中文](README.zh-CN.md)

# Just One API - Python SDK

Official Python SDK for accessing [Just One API](https://justoneapi.com).

Version 2 is generated from the public OpenAPI document and covers the full `public-api` surface. The SDK now returns typed response objects instead of tuples.

## Installation

```bash
pip install justoneapi
```

## Quick Start

```python
from justoneapi import JustOneAPIClient

client = JustOneAPIClient(token="your_token")
response = client.douyin.get_video_detail_v2(video_id="7428906452091145483")

print(response.success)
print(response.code)
print(response.message)
print(response.data)
```

## Response Shape

Every API method returns an `ApiResponse` instance with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `success` | `bool` | `True` only when `code == 0`. |
| `code` | `Any` | Raw business code returned by the API. |
| `message` | `str` | Server message. |
| `data` | `Any` | Response payload from the API. |
| `raw_json` | `dict` | Full response payload before SDK normalization. |

## Authentication

All API requests require a valid API token.

## OpenAPI Sync

The repository ships scripts for the generation pipeline:

```bash
python3.11 scripts/fetch_openapi.py
python3.11 scripts/normalize_openapi.py
python3.11 scripts/generate_sdk.py
```

`fetch_openapi.py` reads credentials from `OPENAPI_BASIC_AUTH_USERNAME` and `OPENAPI_BASIC_AUTH_PASSWORD` by default.
