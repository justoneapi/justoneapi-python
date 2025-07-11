# Just One API - Python SDK

Official Python SDK for accessing [Just One API](https://justoneapi.com) — a unified data service platform offering structured data from Social, E-commerce platforms such as Xiaohongshu, Taobao, Douyin, Kuaishou, Bilibili, and Weibo.

This SDK simplifies API integration and request signing, allowing developers to easily retrieve platform-specific data with minimal setup.

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

client = JustOneAPIClient(token="your_token")

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
You can obtain your token by contact us:  
👉 [Contact](https://justoneapi.com/contact)

---

## 📚 Documentation

👉 Full API docs: [https://justoneapi.com/docs](https://doc.justoneapi.com)

Includes:
- Request parameters
- Response fields
- Error codes

---

## 🏠 Official Website

👉 [https://justoneapi.com](https://justoneapi.com)

Learn more about the project, data sources, and commercial integration opportunities.

---

## 📬 Contact Us

If you have any questions, feedback, or partnership inquiries:

- Email: **justoneapi@gmail.com**
- Telegram: [@justoneapi](https://t.me/justoneapi)

---

## 🪪 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.