from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class InstagramResource(BaseResource):
    """Generated resource for Instagram."""

    def get_user_detail_v1(
        self,
        *,
        username: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves an Instagram user profile by username. Use it to review a known account before creator research, brand monitoring, or related post analysis.

        Args:
            username: The Instagram username whose profile details are to be retrieved.
        """
        return self._get(
            "/api/instagram/get-user-detail/v1",
            {
                "username": username,
            },
        )

    def get_post_detail_v1(
        self,
        *,
        code: str,
    ) -> ApiResponse[Any]:
        """
        Post Details

        Retrieves an Instagram post by its shortcode. Use it to look up a known post before content review, archiving, comment analysis, or related workflows.

        Args:
            code: The unique shortcode from the Instagram post URL.
        """
        return self._get(
            "/api/instagram/get-post-detail/v1",
            {
                "code": code,
            },
        )

    def get_user_posts_v1(
        self,
        *,
        username: str,
        pagination_token: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Retrieves posts published by an Instagram user with token-based pagination. Use it to browse a known account's post history or continue through subsequent result pages.

        Args:
            username: The Instagram username whose published posts are to be retrieved.
            pagination_token: Token used for retrieving the next page of results.
        """
        return self._get(
            "/api/instagram/get-user-posts/v1",
            {
                "username": username,
                "paginationToken": pagination_token,
            },
        )

    def search_reels_v1(
        self,
        *,
        keyword: str,
        pagination_token: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Reels Search

        Searches Instagram Reels by keyword or hashtag with token-based pagination. Use it to discover short-form videos, monitor topics, and continue through matching results.

        Args:
            keyword: The search keyword or hashtag to filter Reels.
            pagination_token: Token used for retrieving the next page of results.
        """
        return self._get(
            "/api/instagram/search-reels/v1",
            {
                "keyword": keyword,
                "paginationToken": pagination_token,
            },
        )

    def search_hashtag_posts_v1(
        self,
        *,
        hashtag: str,
        end_cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Hashtag Posts Search

        Searches Instagram posts by hashtag with cursor pagination. Use it to explore tagged content, monitor topics, and continue through subsequent result pages.

        Args:
            hashtag: The hashtag or keyword to search for.
            end_cursor: Cursor used for retrieving the next page of results.
        """
        return self._get(
            "/api/instagram/search-hashtag-posts/v1",
            {
                "hashtag": hashtag,
                "endCursor": end_cursor,
            },
        )

    def get_post_comments_v1(
        self,
        *,
        code: str,
        min_id: str | None = "",
        sort_order: str | None = "newest",
    ) -> ApiResponse[Any]:
        """
        Post Comment List

        Retrieves top-level comments for an Instagram post by shortcode, with cursor pagination and popular or newest sorting. Use it to review audience feedback or analyze discussion around a known post.

        Args:
            code: The unique shortcode for the Instagram post.
            min_id: Pagination cursor returned as next_min_id from the previous response.
            sort_order: Sort order for the comments.  Available Values: - `popular`: Popular - `newest`: Newest
        """
        return self._get(
            "/api/instagram/get-post-comments/v1",
            {
                "code": code,
                "minId": min_id,
                "sortOrder": sort_order,
            },
        )

    def get_comment_replies_v1(
        self,
        *,
        media_id: str,
        comment_id: str,
        min_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Comment Reply List

        Retrieves replies to a specific Instagram post comment by media and comment IDs, with cursor pagination. Use it to inspect threaded discussion and continue through reply pages.

        Args:
            media_id: The numeric media ID of the Instagram post.
            comment_id: The parent comment ID whose replies are to be retrieved.
            min_id: Pagination cursor returned as next_min_child_cursor from the previous response.
        """
        return self._get(
            "/api/instagram/get-comment-replies/v1",
            {
                "mediaId": media_id,
                "commentId": comment_id,
                "minId": min_id,
            },
        )
