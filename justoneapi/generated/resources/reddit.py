from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class RedditResource(BaseResource):
    """Generated resource for Reddit."""

    def get_post_detail_v1(
        self,
        *,
        post_id: str,
    ) -> ApiResponse[Any]:
        """
        Post Details

        Get Reddit post Details data, including author details, subreddit info, and engagement counts, for content analysis, moderation research, and monitoring.

        Args:
            post_id: The unique identifier of the Reddit post (e.g., 't3_1q4aqti').
        """
        return self._get(
            "/api/reddit/get-post-detail/v1",
            {
                "postId": post_id,
            },
        )

    def get_post_comments_v1(
        self,
        *,
        post_id: str,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Get Reddit post Comments data, including text, authors, and timestamps, for discussion analysis and moderation research.

        Args:
            post_id: The unique identifier of the Reddit post.
            cursor: Pagination token for the next page of results.
        """
        return self._get(
            "/api/reddit/get-post-comments/v1",
            {
                "postId": post_id,
                "cursor": cursor,
            },
        )

    def search_v1(
        self,
        *,
        keyword: str,
        after: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Keyword Search

        Get Reddit keyword Search data, including titles, authors, and subreddit context, for topic discovery and monitoring.

        Args:
            keyword: Search query keywords.
            after: Pagination token to retrieve the next set of results.
        """
        return self._get(
            "/api/reddit/search/v1",
            {
                "keyword": keyword,
                "after": after,
            },
        )
