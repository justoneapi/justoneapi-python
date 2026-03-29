from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TiktokResource(BaseResource):
    """Generated resource for TikTok APIs."""

    def get_user_post_v1(
        self,
        *,
        sec_uid: str,
        cursor: str | None = "0",
        sort: str | None = "_0",
    ) -> ApiResponse[Any]:
        """
        User Published Posts (V1)

        Retrieve a list of posts published by a specific TikTok user.
        The API returns detailed information about each post, including video ID, description, publish time,
        statistics (likes, comments, shares, views), and video download URL if available.

        Typical use cases:
        - User activity analysis and posting frequency tracking.
        - Influencer performance evaluation.
        - Content trend monitoring for specific creators.

        Args:
            sec_uid: The unique security ID of the TikTok user (e.g., MS4wLjABAAAAonP2...).
            cursor: Pagination cursor. Use '0' for the first page, then use the 'cursor' value returned in the previous response.
            sort: Sorting criteria for the user's posts.  Available Values: - `_0`: Default (Mixed) - `_1`: Highest Liked - `_2`: Latest Published
        """
        return self._get(
            "/api/tiktok/get-user-post/v1",
            {
                "secUid": sec_uid,
                "cursor": cursor,
                "sort": sort,
            },
        )

    def get_post_detail_v1(
        self,
        *,
        post_id: str,
    ) -> ApiResponse[Any]:
        """
        Post Details (V1)

        Retrieve detailed information for a specific TikTok post by its post ID.
        The API returns complete metadata including video ID, author information, description text, publish time,
        engagement metrics (likes, comments, shares, views), and available download URLs for both the video and cover image.

        Typical use cases:
        - Content performance analysis and metadata extraction.
        - Influencer evaluation via specific post metrics.
        - Verifying post authenticity and downloading media for offline analysis.

        Args:
            post_id: The unique ID of the TikTok post.
        """
        return self._get(
            "/api/tiktok/get-post-detail/v1",
            {
                "postId": post_id,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        unique_id: str | None = "",
        sec_uid: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Profile (V1)

        Retrieve detailed profile information for a specific TikTok user by user ID.
        The API returns comprehensive data including nickname, unique ID, avatar, bio, follower/following counts,
        total likes, and other engagement indicators.

        Typical use cases:
        - Influencer profiling and audience analysis.
        - Account performance tracking and growth monitoring.
        - Identifying verified status and official accounts.

        Notes:
        - You must provide either 'uniqueId' or 'secUid'.

        Args:
            unique_id: The unique handle/username of the user (e.g., 'tiktok').
            sec_uid: The unique security ID of the user.
        """
        return self._get(
            "/api/tiktok/get-user-detail/v1",
            {
                "uniqueId": unique_id,
                "secUid": sec_uid,
            },
        )

    def get_post_comment_v1(
        self,
        *,
        aweme_id: str,
        cursor: str | None = "0",
    ) -> ApiResponse[Any]:
        """
        Post Comments (V1)

        Retrieve a list of comments under a specific TikTok post by post ID.
        The API returns detailed information for each comment, including comment ID, user information,
        text content, like count, reply count, and publish time.

        Typical use cases:
        - Sentiment analysis of the audience's reaction to specific content.
        - Engagement measurement via comment volume and quality.
        - Community interaction research and feedback collection.

        Args:
            aweme_id: The unique ID of the TikTok post (awemeId).
            cursor: Pagination cursor. Start with '0'.
        """
        return self._get(
            "/api/tiktok/get-post-comment/v1",
            {
                "awemeId": aweme_id,
                "cursor": cursor,
            },
        )

    def get_post_sub_comment_v1(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: str | None = "0",
    ) -> ApiResponse[Any]:
        """
        Comment Replies (V1)

        Retrieve a list of replies under a specific TikTok comment by comment ID.
        The API returns detailed information for each reply, including reply ID, user information,
        text content, like count, and publish time.

        Typical use cases:
        - Understanding detailed user interactions and threaded discussions.
        - Identifying influencers or active participants within a comment section.
        - Tracking sentiment propagation within comment threads.

        Args:
            aweme_id: The unique ID of the TikTok post.
            comment_id: The unique ID of the comment to retrieve replies for.
            cursor: Pagination cursor. Start with '0'.
        """
        return self._get(
            "/api/tiktok/get-post-sub-comment/v1",
            {
                "awemeId": aweme_id,
                "commentId": comment_id,
                "cursor": cursor,
            },
        )

    def search_user_v1(
        self,
        *,
        keyword: str,
        cursor: str | None = "0",
        search_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Search (V1)

        Search for TikTok users by keyword.
        The API returns a list of matching users along with basic profile information such as user ID,
        nickname, unique handle, avatar, bio, follower count, and verification status.

        Typical use cases:
        - Discovering influencers in specific niches via keywords.
        - Identifying target audiences and conducting competitor research.
        - Finding official brand accounts.

        Args:
            keyword: Search keywords (e.g., 'deepseek').
            cursor: Pagination cursor. Start with '0'.
            search_id: The 'logid' returned from the previous request for consistent search results.
        """
        return self._get(
            "/api/tiktok/search-user/v1",
            {
                "keyword": keyword,
                "cursor": cursor,
                "searchId": search_id,
            },
        )

    def search_post_v1(
        self,
        *,
        keyword: str,
        offset: int | None = 0,
        sort_type: str | None = "RELEVANCE",
        publish_time: str | None = "ALL",
        region: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Post Search (V1)

        Search for TikTok posts by keyword.
        The API returns a list of matching posts with key details such as video ID, description,
        author information, publish time, and engagement metrics (likes, comments, shares, views).

        Typical use cases:
        - Trend monitoring and content discovery.
        - Keyword-based market analysis and sentiment tracking.
        - Identifying viral content related to specific topics.

        Args:
            keyword: Search keywords (e.g., 'deepseek').
            offset: Pagination offset, starting from 0 and stepping by 20.
            sort_type: Sorting criteria for search results.  Available Values: - `RELEVANCE`: Relevance (Default) - `MOST_LIKED`: Most Liked
            publish_time: Filter posts by publishing time.  Available Values: - `ALL`: All Time - `ONE_DAY`: Last 24 Hours - `ONE_WEEK`: Last 7 Days - `ONE_MONTH`: Last 30 Days - `THREE_MONTHS`: Last 90 Days - `HALF_YEAR`: Last 180 Days
            region: ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB').
        """
        return self._get(
            "/api/tiktok/search-post/v1",
            {
                "keyword": keyword,
                "offset": offset,
                "sortType": sort_type,
                "publishTime": publish_time,
                "region": region,
            },
        )
