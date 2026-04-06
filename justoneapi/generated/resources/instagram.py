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

        Get Instagram user Profile data, including follower count, following count, and post count, for obtaining basic account metadata for influencer vetting, tracking follower growth and audience reach over time, and mapping user handles to specific profile stats.

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

        Get Instagram post Details data, including post caption, media content (images/videos), and publish time, for analyzing engagement metrics (likes/comments) for a specific post and archiving post content and media assets for content analysis.

        Args:
            code: The unique shortcode (slug) for the Instagram post (e.g., 'DRhvwVLAHAG').
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

        Get Instagram user Published Posts data, including post code, caption, and media type, for monitoring recent publishing activity of a specific user and building a historical record of content for auditing or analysis.

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

        Get Instagram reels Search data, including post ID, caption, and author profile, for tracking trends and viral content via specific keywords or hashtags and discovering high-engagement reels within a particular niche.

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

        Get Instagram hashtag Posts Search data, including caption, author profile, and publish time, for competitive analysis of trending topics and hashtags and monitoring community discussions and public opinion on specific tags.

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
