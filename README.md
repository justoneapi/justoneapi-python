![PyPI version](https://img.shields.io/pypi/v/justoneapi.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

[English](README.md) | [简体中文](README.zh-CN.md)

# Just One API - Python SDK

Official Python SDK for accessing [Just One API](https://justoneapi.com) — a unified data service platform offering structured data from Social, E-commerce platforms such as Xiaohongshu, Taobao, Douyin, Kuaishou, Bilibili, and Weibo.

This SDK simplifies API integration and request signing, allowing developers to easily retrieve platform-specific data with minimal setup.

---

## 🧧 Featured Project (Separate Service)

### [Just Serp API](https://justserpapi.com/)
> **Note:** This is an independent project and not part of the Just One API Python SDK.

Need search engine data? Check out Just Serp API — a high-performance SERP API providing structured data from Google, Bing, and other search engines.

---

## 🚀 Installation

Install via PyPI:

```bash
pip install justoneapi
```

---

## 🛠 Quick Start

```python
from justoneapi.client import JustOneAPIClient

# By default, the client uses the "cn" (Mainland China) environment.
client = JustOneAPIClient(token="your_token")
# If you are located outside Mainland China and experience slow responses,
# you can switch to the "global" environment for better performance:
# client = JustOneAPIClient(token="your_token", env="global")

# Example: Get Douyin Video detail
result, data, message = client.douyin.get_video_detail_v2(video_id="7428906452091145483")
print(result)
print(data)
print(message)

# Example: Douyin Video Search
result, data, message, has_next_page = client.douyin.search_video_v4(keyword="deepseek", sort_type="_0", publish_time="_0", duration="_0", page=1)
print(result)
print(data)
print(message)
print(has_next_page)
```

### 📦 Return Value Description

Each API method returns one or more of the following values:

| Variable         | Type     | Description |
|------------------|----------|-------------|
| `result`         | `bool`   | Whether the request was successful. `True` means success, `False` means failure. |
| `data`           | `dict` / `list` | The actual data returned from the API. Structure varies by endpoint. |
| `message`        | `str`    | Message from the server. Contains error info when request fails. |
| `has_next_page`  | `bool`   | Present in paginated APIs. Indicates whether more data is available. |

---

## 🔐 Authentication

All API requests require a valid API token.  
👉 [Register](https://user.justoneapi.com/sign-up)

---

## 📚 Documentation

👉 Full API docs: [API Document](https://docs.justoneapi.com/en)

Includes:
- Request parameters
- Response fields
- Error codes

---

## 🏠 Official Website

👉 [Home Page](https://justoneapi.com)

Learn more about the project, data sources, and commercial integration opportunities.

---

## 📬 Contact Us

If you have any questions, feedback, or partnership inquiries:

👉 [Contact](https://justoneapi.com/contact)

---

## 🪪 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
