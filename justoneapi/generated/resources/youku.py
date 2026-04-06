from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class YoukuResource(BaseResource):
    """Generated resource for YOUKU."""

    def search_video_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Get YOUKU video Search data, including video ID, title, and cover image, for keyword-based video discovery, monitoring specific topics or trends on youku, and analyzing search results for market research.

        Args:
            keyword: Keyword to search for.
            page: Page number for pagination, starting from 1.
        """
        return self._get(
            "/api/youku/search-video/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_video_detail_v1(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Get YOUKU video Details data, including video ID, title, and description, for fetching comprehensive metadata for a single video, tracking engagement metrics like play counts and likes, and integrating detailed video info into third-party dashboards.

        Args:
            video_id: The unique identifier for the video.
        """
        return self._get(
            "/api/youku/get-video-detail/v1",
            {
                "videoId": video_id,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get YOUKU user Profile data, including user ID, username, and avatar, for analyzing creator influence and audience size, monitoring account growth and verification status, and fetching basic user info for social crm.

        Args:
            uid: The unique identifier for the user.
        """
        return self._get(
            "/api/youku/get-user-detail/v1",
            {
                "uid": uid,
            },
        )
