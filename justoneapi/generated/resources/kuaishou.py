from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class KuaishouResource(BaseResource):
    """Generated resource for Kuaishou."""

    def search_video_v1(
        self,
        *,
        keyword: str,
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Search public Kuaishou videos by keyword with cursor-based pagination. Use it to discover relevant videos and continue through additional result pages.

        Args:
            keyword: The search keyword to find videos.
            cursor: Pagination cursor returned by the previous response. Omit or leave blank for the first page; maximum 256 characters.
        """
        return self._get(
            "/api/kuaishou/search-video/v1",
            {
                "keyword": keyword,
                "cursor": cursor,
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

        Search public Kuaishou videos by keyword with page-number pagination. Use it to discover relevant videos and browse results by page.

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

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Search

        Search public Kuaishou user accounts by keyword with page-number pagination. Use it to discover relevant creators or accounts before requesting profile and published-video data.

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

        Retrieve public videos published by a Kuaishou user, with optional cursor-based pagination. Use it to review a creator's content history or select videos for detail and comment requests.

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

        Retrieve public details for a Kuaishou video identified by its video ID. Use it to inspect a selected video after search or user-published-video discovery.

        Args:
            video_id: The unique video identifier returned by Kuaishou.
        """
        return self._get(
            "/api/kuaishou/get-video-detail/v2",
            {
                "videoId": video_id,
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

        Retrieve public comments for a Kuaishou video, with optional cursor-based pagination. Use it to review audience discussion and continue through additional comment pages.

        Args:
            video_id: The Kuaishou video identifier or numeric refer_photo_id returned by a related response.
            pcursor: Pagination cursor for subsequent pages.
        """
        return self._get(
            "/api/kuaishou/get-video-comment/v1",
            {
                "videoId": video_id,
                "pcursor": pcursor,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieve the public profile for a Kuaishou user identified by user ID. Use it to inspect an account found through user or video results.

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

        Resolve a supported Kuaishou short share link and return its public redirect URL. Use it to expand shared links before subsequent Kuaishou content lookup or processing.

        Args:
            share_url: A Kuaishou short share URL beginning with https://v.kuaishou.com/.
        """
        return self._get(
            "/api/kuaishou/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
