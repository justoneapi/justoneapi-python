from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class SearchResource(BaseResource):
    """Generated resource for Search APIs."""

    def search_v1(
        self,
        *,
        keyword: str | None = None,
        source: str | None = "ALL",
        start: str | None = None,
        end: str | None = None,
        next_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Unified Search (V1)

        Retrieves social media data across all supported platforms (Weibo, Weixin, Douyin, Xiaohongshu, etc.)
        based on the provided keyword and time range. This non-real-time search provides a
        comprehensive view of cross-platform social sentiment and trends.

        Typical use cases:
        - Analyzing brand mentions across different social ecosystems
        - Comparative sentiment monitoring between platforms
        - Historical keyword tracking within an 84-day window

        Highlights
        - Time range limit: Data is restricted to the last 84 days from the current date.
        - Non-real-time: Results are not indexed in real-time and may have a delay.

        Args:
            keyword: Search query string. Supports: - Multiple keywords (AND): keyword1 keyword2 - Multiple keywords (OR): keyword1~keyword2 - Excluded keywords (NOT): required_keyword -excluded_keyword
            source: Target social media platform for search filtering.  Available Values: - `ALL`: All platforms - `NEWS`: News - `WEIBO`: Sina Weibo - `WEIXIN`: Weixin (WeChat) - `ZHIHU`: Zhihu - `DOUYIN`: Douyin (TikTok China) - `XIAOHONGSHU`: Xiaohongshu (Little Red Book) - `BILIBILI`: Bilibili - `KUAISHOU`: Kuaishou
            start: Start time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.
            end: End time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.
            next_cursor: Pagination cursor provided by the 'nextCursor' field in the previous response.
        """
        return self._get(
            "/api/search/v1",
            {
                "keyword": keyword,
                "source": source,
                "start": start,
                "end": end,
                "nextCursor": next_cursor,
            },
        )
