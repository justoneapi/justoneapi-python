from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class RedditResource(BaseResource):
    """Generated resource for Reddit APIs."""

    def get_post_detail_v1(
        self,
        *,
        post_id: str,
    ) -> ApiResponse[Any]:
        """
        Post Details (V1)

        Retrieves comprehensive information of a specific Reddit post by its unique ID.
        Includes the post content (text or link), author details, subreddit information,
        and engagement statistics like upvotes, downvotes, and comment counts.

        Typical use cases
        - Sentiment analysis for brands, products, or topics
        - Tracking public engagement with specific pieces of content
        - Content archiving and metadata analysis

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
        Post Comments (V1)

        Fetches the discussion thread (comments) for a specific Reddit post by its ID.
        The results are returned as a paginated list of comment objects, including the text,
        author, and other metadata for each response.

        Typical use cases
        - Mining customer feedback and reviews
        - Understanding community sentiment through detailed discussions
        - Tracking the evolution of topics within a thread

        Highlights
        - Pagination is supported via the 'cursor' parameter.

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
        Search (V1)

        Performs a search for posts on Reddit based on specified keywords.
        Retrieves matching posts along with their metadata and basic engagement metrics.

        Typical use cases
        - Discovering new discussions or trends on specific topics
        - Competitive intelligence and brand monitoring
        - Researching community activity across the platform

        Highlights
        - Results can be paginated using the 'after' parameter.

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
