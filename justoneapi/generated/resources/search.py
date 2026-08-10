from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class SearchResource(BaseResource):
    """Generated resource for Social Media."""

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
        Cross-Platform Search

        Searches recent content across news, Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili, and Kuaishou with source and time filters. Use it to monitor a topic across multiple platforms.

        Args:
            keyword: Search query string. Supports these five syntax forms: - AND (&&): A && B matches content containing both A and B. - OR (||): A || B matches content containing A or B. - Exclusion (-): -A matches content that does not contain A. - Parentheses (): (A && B) || C matches content containing C, or both A and B. - English double quotes (""): "A" disables tokenization and requires an exact match for A.
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
