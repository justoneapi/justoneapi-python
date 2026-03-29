from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class YoukuResource(BaseResource):
    """Generated resource for Youku APIs."""

    def search_video_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Search (V1)

        This API performs a keyword-based search on Youku, returning a list of videos that match the search term.
        Returned fields include video ID, title, cover image, duration, play count, publish time, and the video's detail page URL.

        Typical use cases:
        - Keyword-based video discovery.
        - Monitoring specific topics or trends on Youku.
        - Analyzing search results for market research.

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
        Video Details (V1)

        This API retrieves detailed information of a specific Youku video, including video ID, title, description, cover image, duration, tags, play count, like count, publish time, and the video's detail page URL.

        Typical use cases:
        - Fetching comprehensive metadata for a single video.
        - Tracking engagement metrics like play counts and likes.
        - Integrating detailed video info into third-party dashboards.

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
        User Profile (V1)

        This API retrieves detailed profile information of a specific Youku creator/user, including user ID, username, avatar, signature/description, follower count, following count, total videos, and verification status.

        Typical use cases:
        - Analyzing creator influence and audience size.
        - Monitoring account growth and verification status.
        - Fetching basic user info for social CRM.

        Args:
            uid: The unique identifier for the user.
        """
        return self._get(
            "/api/youku/get-user-detail/v1",
            {
                "uid": uid,
            },
        )
