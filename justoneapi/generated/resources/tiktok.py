from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TiktokResource(BaseResource):
    """Generated resource for TikTok."""

    def get_user_post_v1(
        self,
        *,
        sec_uid: str,
        cursor: str | None = "0",
        sort: str | None = "_0",
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Get TikTok user Published Posts data, including video ID, description, and publish time, for user activity analysis and posting frequency tracking, influencer performance evaluation, and content trend monitoring for specific creators.

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
        Post Details

        Get TikTok post Details data, including video ID, author information, and description text, for content performance analysis and metadata extraction and influencer evaluation via specific post metrics.

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
        User Profile

        Get TikTok user Profile data, including nickname, unique ID, and avatar, for influencer profiling and audience analysis, account performance tracking and growth monitoring, and identifying verified status and official accounts.

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
        Post Comments

        Get TikTok post Comments data, including comment ID, user information, and text content, for sentiment analysis of the audience's reaction to specific content and engagement measurement via comment volume and quality.

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
        Comment Replies

        Get TikTok comment Replies data, including reply ID, user information, and text content, for understanding detailed user interactions and threaded discussions and identifying influencers or active participants within a comment section.

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
        User Search

        Get TikTok user Search data, including basic profile information such as user ID, nickname, and unique handle, for discovering influencers in specific niches via keywords and identifying target audiences and conducting competitor research.

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
        Post Search

        Get TikTok post Search data, including key details such as video ID, description, and author information, for trend monitoring and content discovery and keyword-based market analysis and sentiment tracking.

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
