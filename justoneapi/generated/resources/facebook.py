from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class FacebookResource(BaseResource):
    """Generated resource for Facebook."""

    def search_v1(
        self,
        *,
        keyword: str,
        start_date: str | None = None,
        end_date: str | None = None,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Search Posts (V1)

        Search for public posts on Facebook based on keywords.

        The results include post metadata, content, author information, publication time,
        engagement metrics (reactions, comments, shares), and media URLs.

        Typical use cases:
        - Discovering relevant public posts for specific keywords.
        - Analyzing engagement and reach of public content on Facebook.

        Args:
            keyword: Keyword to search for in public posts. Supports basic text matching.
            start_date: Start date for the search range (inclusive), formatted as yyyy-MM-dd.
            end_date: End date for the search range (inclusive), formatted as yyyy-MM-dd.
            cursor: Pagination cursor for fetching the next set of results.
        """
        return self._get(
            "/api/facebook/search-post/v1",
            {
                "keyword": keyword,
                "startDate": start_date,
                "endDate": end_date,
                "cursor": cursor,
            },
        )
