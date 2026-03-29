![PyPI version](https://img.shields.io/pypi/v/justoneapi.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

[English](README.md) | [简体中文](README.zh-CN.md)

# Just One API - Python SDK

官方 Python SDK，用于访问 [Just One API](https://justoneapi.com/zh/)。

2.x 版本改为基于公开 OpenAPI 文档自动生成，覆盖完整 `public-api` 接口面，返回值也改为 `ApiResponse` 对象，不再返回 tuple。

## 安装

```bash
pip install justoneapi
```

## 快速开始

```python
from justoneapi import JustOneAPIClient

client = JustOneAPIClient(token="your_token")
response = client.douyin.get_video_detail_v2(video_id="7428906452091145483")

print(response.success)
print(response.code)
print(response.message)
print(response.data)
```

## 返回结构

每个 API 方法都会返回一个 `ApiResponse` 对象，包含以下字段：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `success` | `bool` | 仅当 `code == 0` 时为 `True`。 |
| `code` | `Any` | 服务端返回的业务码。 |
| `message` | `str` | 服务端消息。 |
| `data` | `Any` | API 返回的业务数据。 |
| `raw_json` | `dict` | SDK 处理前的完整 JSON 响应。 |

## OpenAPI 同步

仓库内置了生成链路脚本：

```bash
python3.11 scripts/fetch_openapi.py
python3.11 scripts/normalize_openapi.py
python3.11 scripts/generate_sdk.py
```

默认会从环境变量 `OPENAPI_BASIC_AUTH_USERNAME` 和 `OPENAPI_BASIC_AUTH_PASSWORD` 读取 swagger 的 Basic Auth 凭据。
