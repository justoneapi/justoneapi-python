from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class KuaishouResource(BaseResource):
    """Generated resource for Kuaishou."""

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Search (V2)

        Enhanced user search for Kuaishou, returning detailed user profiles with nickname,
        avatar, follower count, and bio.

        Typical use cases:
        - Creator discovery and influencer analytics
        - Market research on specific content domains

        Args:
            keyword: The search keyword to find users.
            page: Page number for results, starting from 1.
        """
        return self._get(
            "/api/kuaishou/search-user/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_user_video_list_v2(
        self,
        *,
        user_id: str,
        pcursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Videos (V2)

        Retrieves a list of videos posted by a specific Kuaishou user, including video ID,
        cover image, publish time, and engagement metrics.

        Typical use cases:
        - Content analysis for specific creators
        - Monitoring video performance and engagement trends

        Args:
            user_id: The unique user ID on Kuaishou.
            pcursor: Pagination cursor for subsequent pages.
        """
        return self._get(
            "/api/kuaishou/get-user-video-list/v2",
            {
                "userId": user_id,
                "pcursor": pcursor,
            },
        )

    def get_video_details_v2(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details (V2)

        Provides detailed information about a specific Kuaishou video, including video URL,
        caption, author info, publish time, and engagement metrics (likes, comments, shares).

        Typical use cases:
        - In-depth content performance analysis
        - Building databases of viral videos

        Args:
            video_id: The unique ID of the Kuaishou video.
        """
        return self._get(
            "/api/kuaishou/get-video-detail/v2",
            {
                "videoId": video_id,
            },
        )

    def search_video_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Search (V2)

        Enables searching for Kuaishou videos by keyword, returning matched results with video ID,
        cover image, description, author info, publish time, and engagement metrics.

        Typical use cases:
        - Competitive analysis and market trends
        - Keywords monitoring and brand tracking

        Args:
            keyword: The search keyword to find videos.
            page: Page number for results, starting from 1.
        """
        return self._get(
            "/api/kuaishou/search-video/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_user_profile_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile (V1)

        Retrieves detailed profile information of a Kuaishou user, including nickname,
        avatar, follower count, verification status, and bio.

        Typical use cases:
        - Creator research and building creator profiles
        - Monitoring audience growth and account status

        Args:
            user_id: The unique user ID on Kuaishou.
        """
        return self._get(
            "/api/kuaishou/get-user-detail/v1",
            {
                "userId": user_id,
            },
        )

    def share_link_resolution_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution (V1)

        Converts Kuaishou short share URLs to structured data.

        Typical use cases:
        - Resolving shared links for automated content processing

        Args:
            share_url: Kuaishou share URL (must start with 'https://v.kuaishou.com/').
        """
        return self._get(
            "/api/kuaishou/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )

    def get_video_comments_v1(
        self,
        *,
        photo_id: str,
        pcursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Comments (V1)

        Retrieves public comments of a Kuaishou video, including comment content,
        author info, like count, and reply count.

        Typical use cases:
        - Sentiment analysis and community feedback monitoring
        - Gathering engagement data for specific videos

        Args:
            photo_id: The unique numeric photo ID of the video.
            pcursor: Pagination cursor for subsequent pages.
        """
        return self._get(
            "/api/kuaishou/get-video-comment/v1",
            {
                "photoId": photo_id,
                "pcursor": pcursor,
            },
        )
