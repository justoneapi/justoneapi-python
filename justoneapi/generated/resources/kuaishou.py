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
        User Search

        Get Kuaishou user Search data, including profile names, avatars, and follower counts, for creator discovery and account research.

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
        User Published Videos

        Get Kuaishou user Published Videos data, including covers, publish times, and engagement metrics, for creator monitoring and content performance analysis.

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

    def get_video_detail_v2(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Get Kuaishou video Details data, including video URL, caption, and author info, for in-depth content performance analysis and building databases of viral videos.

        Args:
            video_id: The unique ID of the Kuaishou video, e.g. `3xg9avuebhtfcku`
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
        Video Search

        Get Kuaishou video Search data, including video ID, cover image, and description, for competitive analysis and market trends and keywords monitoring and brand tracking.

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

    def get_user_detail_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Kuaishou user Profile data, including account metadata, audience metrics, and verification-related fields, for creator research and building creator profiles and monitoring audience growth and account status.

        Args:
            user_id: The unique user ID on Kuaishou.
        """
        return self._get(
            "/api/kuaishou/get-user-detail/v1",
            {
                "userId": user_id,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution

        Get Kuaishou share Link Resolution data, including resolved content identifier and target object data, for resolving shared links for automated content processing.

        Args:
            share_url: Kuaishou share URL (must start with 'https://v.kuaishou.com/').
        """
        return self._get(
            "/api/kuaishou/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )

    def get_video_comment_v1(
        self,
        *,
        video_id: str,
        pcursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Comments

        Retrieves public comments of a Kuaishou video, including comment content,
        author info, like count, and reply count.

        Typical use cases:
        - Sentiment analysis and community feedback monitoring
        - Gathering engagement data for specific videos

        Args:
            video_id: The unique ID of the Kuaishou video, e.g. `3xbknvct79h46h9` or refer_photo_id `177012131237`
            pcursor: Pagination cursor for subsequent pages.
        """
        return self._get(
            "/api/kuaishou/get-video-comment/v1",
            {
                "videoId": video_id,
                "pcursor": pcursor,
            },
        )
