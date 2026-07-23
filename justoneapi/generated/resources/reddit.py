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

        Retrieves details for a Reddit post identified by its full post ID. Use it to look up a known post before discussion review, content analysis, or subsequent comment retrieval.

        Args:
            post_id: The Reddit post identifier in t3_<post-id> format.
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

        Retrieves comments for a Reddit post with pagination-token support. Use it to review a thread's discussion or continue through additional comment results for a known post.

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

        Searches Reddit posts by keyword with an optional continuation token. Use it to discover topic-related discussions or continue through additional search-result pages.

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
