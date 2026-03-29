from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinResource(BaseResource):
    """Generated resource for Douyin APIs."""

    def get_user_detail_v3(
        self,
        *,
        sec_uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile (V3)

        Retrieves detailed profile information of a Douyin user, including nickname, avatar,
        follower count, verification status, bio, and other user statistics.

        Typical use cases:
        - Identifying creators and building creator lists
        - Enriching user records for analytics and reporting
        - Monitoring profile changes and audience growth

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
        """
        return self._get(
            "/api/douyin/get-user-detail/v3",
            {
                "secUid": sec_uid,
            },
        )

    def get_user_video_list_v1(
        self,
        *,
        sec_uid: str,
        max_cursor: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Published Videos (V1)

        Retrieves a list of videos published by a specific Douyin user, including video ID,
        cover image, title/caption, publish time, and engagement metrics.

        Highlights:
        - Capable of retrieving the latest published videos.

        Typical use cases:
        - Creator monitoring and content tracking
        - Building content timelines for specific accounts

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
            max_cursor: Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages.
        """
        return self._get(
            "/api/douyin/get-user-video-list/v1",
            {
                "secUid": sec_uid,
                "maxCursor": max_cursor,
            },
        )

    def get_user_video_list_v3(
        self,
        *,
        sec_uid: str,
        max_cursor: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Published Videos (V3)

        Retrieves a list of videos published by a specific Douyin user. This version may offer
        different data structure or coverage compared to V1.

        Highlights:
        - Not capable of retrieving the latest published videos.

        Typical use cases:
        - Creator monitoring and content tracking
        - Building content timelines for specific accounts

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
            max_cursor: Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages.
        """
        return self._get(
            "/api/douyin/get-user-video-list/v3",
            {
                "secUid": sec_uid,
                "maxCursor": max_cursor,
            },
        )

    def get_video_detail_v2(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details (V2)

        Provides detailed information about a specific Douyin video, including video URL,
        description, author info, publish time, and engagement metrics (likes, comments, shares).

        Typical use cases:
        - Content analysis and performance tracking
        - Retrieving high-quality video assets and metadata

        Args:
            video_id: The unique video identifier (aweme_id or model_id).
        """
        return self._get(
            "/api/douyin/get-video-detail/v2",
            {
                "videoId": video_id,
            },
        )

    def search_video_v4(
        self,
        *,
        keyword: str,
        sort_type: str | None = "_0",
        publish_time: str | None = "_0",
        duration: str | None = "_0",
        page: int | None = 1,
        search_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Search (V4)

        Allows searching for Douyin videos based on keywords, returning matched results with
        video metadata and engagement metrics. Supports filtering by sort type, publish time, and duration.

        Typical use cases:
        - Trend analysis and keyword monitoring
        - Discovery of relevant content for specific topics

        Args:
            keyword: The search keyword.
            sort_type: Sorting criteria for search results.  Available Values: - `_0`: General - `_1`: More likes - `_2`: Newest
            publish_time: Filter by video publish time range.  Available Values: - `_0`: No Limit - `_1`: Last 24 Hours - `_7`: Last 7 Days - `_180`: Last 6 Months
            duration: Filter by video duration.  Available Values: - `_0`: No Limit - `_1`: Under 1 Minute - `_2`: 1-5 Minutes - `_3`: Over 5 Minutes
            page: Page number (starting from 1).
            search_id: Search ID; required for pages > 1 (use the search_id value returned by the last response).
        """
        return self._get(
            "/api/douyin/search-video/v4",
            {
                "keyword": keyword,
                "sortType": sort_type,
                "publishTime": publish_time,
                "duration": duration,
                "page": page,
                "searchId": search_id,
            },
        )

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        user_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Search (V2)

        Enables searching for Douyin users by keyword, returning profiles with nickname,
        avatar, follower count, and other metadata.

        Typical use cases:
        - Identifying creators and influencers
        - Competitive analysis and creator discovery

        Args:
            keyword: The search keyword.
            page: Page number (starting from 1).
            user_type: Filter by user type.  Available Values: - `common_user`: Common User - `enterprise_user`: Enterprise User - `personal_user`: Verified Individual User
        """
        return self._get(
            "/api/douyin/search-user/v2",
            {
                "keyword": keyword,
                "page": page,
                "userType": user_type,
            },
        )

    def get_video_comment_v1(
        self,
        *,
        aweme_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Comments (V1)

        Retrieves the comment list of a Douyin video by awemeId.
        Returns comment content, author info, like count, reply count, and publish time.

        Typical use cases:
        - Sentiment analysis and community feedback monitoring
        - Gathering user engagement data for specific videos

        Args:
            aweme_id: The unique video identifier (aweme_id).
            page: Page number (starting from 1).
        """
        return self._get(
            "/api/douyin/get-video-comment/v1",
            {
                "awemeId": aweme_id,
                "page": page,
            },
        )

    def get_video_sub_comment_v1(
        self,
        *,
        comment_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Comment Replies (V1)

        Retrieves replies to a specific top-level comment under a Douyin video,
        including reply content, user information, timestamp, and like count.

        Typical use cases:
        - Deep-dive into specific discussion threads
        - Detailed community feedback analysis

        Args:
            comment_id: The unique identifier of the top-level comment.
            page: Page number (starting from 1).
        """
        return self._get(
            "/api/douyin/get-video-sub-comment/v1",
            {
                "commentId": comment_id,
                "page": page,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution (V1)

        Converts a Douyin short share URL (e.g., https://v.douyin.com/...) into structured video data.

        Typical use cases:
        - Resolving shared links from users or social media posts
        - Automating content ingestion from shared URLs

        Args:
            share_url: The Douyin short share URL.
        """
        return self._get(
            "/api/douyin/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
