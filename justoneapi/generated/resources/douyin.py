from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinResource(BaseResource):
    """Generated resource for Douyin (TikTok China)."""

    def get_user_detail_v3(
        self,
        *,
        sec_uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Douyin (TikTok China) user Profile data, including follower counts, verification status, and bio details, for creator research and account analysis.

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
        """
        return self._get(
            "/api/douyin/get-user-detail/v3",
            {
                "secUid": sec_uid,
            },
        )

    def get_user_video_list_v3(
        self,
        *,
        sec_uid: str,
        max_cursor: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Published Videos

        Get Douyin (TikTok China) user Published Videos data, including captions, covers, and publish times, for account monitoring.

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
        Video Details

        Get Douyin (TikTok China) video Details data, including author details, publish time, and engagement counts, for video research, archiving, and performance analysis.

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
        Video Search

        Get Douyin (TikTok China) video Search data, including metadata and engagement signals, for content discovery, trend research, and competitive monitoring.

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
        User Search

        Get Douyin (TikTok China) user Search data, including profile metadata and follower signals, for creator discovery and account research.

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
        Video Comments

        Get Douyin (TikTok China) video Comments data, including authors, text, and likes, for sentiment analysis and engagement review.

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
        Comment Replies

        Get Douyin (TikTok China) comment Replies data, including text, authors, and timestamps, for thread analysis and feedback research.

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
        Share Link Resolution

        Get Douyin (TikTok China) share Link Resolution data, including helping extract canonical IDs, for downstream video and comment workflows.

        Args:
            share_url: The Douyin short share URL.
        """
        return self._get(
            "/api/douyin/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
