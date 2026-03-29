from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class InstagramResource(BaseResource):
    """Generated resource for Instagram APIs."""

    def get_user_detail_v1(
        self,
        *,
        username: str,
    ) -> ApiResponse[Any]:
        """
        User Details (V1)

        Retrieves public profile information of an Instagram user, including follower count, following count, post count, and basic profile details.

        Typical use cases:
        - Obtaining basic account metadata for influencer vetting
        - Tracking follower growth and audience reach over time
        - Mapping user handles to specific profile stats

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
        Post Details (V1)

        Retrieves detailed information of a public Instagram post by post code, including post caption, media content (images/videos), publish time, and engagement metrics such as likes and comments.

        Typical use cases:
        - Analyzing engagement metrics (likes/comments) for a specific post
        - Archiving post content and media assets for content analysis
        - Verifying post details via the unique shortcode

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
        User Published Posts (V1)

        Retrieves a list of public posts published by an Instagram user, including post code, caption, media type, publish time, and basic engagement metrics.

        Typical use cases:
        - Monitoring recent publishing activity of a specific user
        - Building a historical record of content for auditing or analysis
        - Collecting post identifiers for deeper engagement analysis

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
        Reels Search (V1)

        Allows you to search public Instagram Reels by keyword or hashtag. It returns detailed information for each matched post, including post ID, caption, author profile, publish time, and engagement metrics.

        Typical use cases:
        - Tracking trends and viral content via specific keywords or hashtags
        - Discovering high-engagement Reels within a particular niche
        - Monitoring brand mentions and campaign hashtags

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
        Hashtag Posts Search (V1)

        Searches public Instagram posts by keyword or hashtag. It returns a list of matched posts with metadata including caption, author profile, publish time, and media links.

        Typical use cases:
        - Competitive analysis of trending topics and hashtags
        - Monitoring community discussions and public opinion on specific tags
        - Aggregating user-generated content for specific campaigns

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
