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

        Searches Youku videos by keyword with page-based pagination. Use it to discover videos related to a topic, title, creator, or other search term.

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

        Retrieves details for a Youku video identified by video ID. Use it to look up a known video for content review, cataloging, or subsequent video analysis.

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

        Retrieves a Youku user profile identified by UID. Use it to look up a known account for creator research, profile review, or related video discovery.

        Args:
            uid: The unique identifier for the user.
        """
        return self._get(
            "/api/youku/get-user-detail/v1",
            {
                "uid": uid,
            },
        )
