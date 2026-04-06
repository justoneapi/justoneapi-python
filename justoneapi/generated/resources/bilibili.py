from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class BilibiliResource(BaseResource):
    """Generated resource for Bilibili."""

    def get_video_detail_v2(
        self,
        *,
        bvid: str,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Get Bilibili video Details data, including metadata (title, tags, and publishing time), for tracking video performance and engagement metrics and analyzing content metadata and uploader information.

        Args:
            bvid: Bilibili Video ID (BVID).
        """
        return self._get(
            "/api/bilibili/get-video-detail/v2",
            {
                "bvid": bvid,
            },
        )

    def get_user_video_list_v2(
        self,
        *,
        uid: str,
        param: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Videos

        Get Bilibili user Published Videos data, including titles, covers, and publish times, for creator monitoring and content performance analysis.

        Args:
            uid: Bilibili User ID (UID).
            param: Pagination parameter from previous response.
        """
        return self._get(
            "/api/bilibili/get-user-video-list/v2",
            {
                "uid": uid,
                "param": param,
            },
        )

    def get_user_detail_v2(
        self,
        *,
        uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Bilibili user Profile data, including account metadata, audience metrics, and verification-related fields, for analyzing creator's profile, level, and verification status and verifying user identity and social presence on bilibili.

        Args:
            uid: Bilibili User ID (UID).
        """
        return self._get(
            "/api/bilibili/get-user-detail/v2",
            {
                "uid": uid,
            },
        )

    def get_video_danmu_v2(
        self,
        *,
        aid: str,
        cid: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Danmaku

        Get Bilibili video Danmaku data, including timeline positions and comment text, for audience reaction analysis and subtitle-style comment review.

        Args:
            aid: Bilibili Archive ID (AID).
            cid: Bilibili Chat ID (CID).
            page: Page number for pagination.
        """
        return self._get(
            "/api/bilibili/get-video-danmu/v2",
            {
                "aid": aid,
                "cid": cid,
                "page": page,
            },
        )

    def get_video_comment_v2(
        self,
        *,
        aid: str,
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Comments

        Get Bilibili video Comments data, including commenter profiles, text, and likes, for sentiment analysis and comment moderation workflows.

        Args:
            aid: Bilibili Archive ID (AID).
            cursor: Pagination cursor.
        """
        return self._get(
            "/api/bilibili/get-video-comment/v2",
            {
                "aid": aid,
                "cursor": cursor,
            },
        )

    def search_video_v2(
        self,
        *,
        keyword: str,
        page: str | None = None,
        order: str | None = "general",
    ) -> ApiResponse[Any]:
        """
        Video Search

        Get Bilibili video Search data, including matched videos, creators, and engagement metrics, for topic research and content discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            order: Sorting criteria for search results.  Available Values: - `general`: General - `click`: Most Played - `pubdate`: Latest - `dm`: Most Danmaku - `stow`: Most Favorite
        """
        return self._get(
            "/api/bilibili/search-video/v2",
            {
                "keyword": keyword,
                "page": page,
                "order": order,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution

        Get Bilibili share Link Resolution data, including resolved video and page identifier, for converting shortened mobile share links to standard bvid/metadata and automating content extraction from shared social media links.

        Args:
            share_url: Bilibili share URL (must start with https://b23.tv/).
        """
        return self._get(
            "/api/bilibili/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )

    def get_user_relation_stat(
        self,
        *,
        wmid: str,
    ) -> ApiResponse[Any]:
        """
        User Relation Stats

        Get Bilibili user Relation Stats data, including following counts, for creator benchmarking and audience growth tracking.

        Args:
            wmid: Bilibili User ID (WMID).
        """
        return self._get(
            "/api/bilibili/get-user-relation-stat/v1",
            {
                "wmid": wmid,
            },
        )

    def get_video_caption_v1(
        self,
        *,
        bvid: str,
        aid: str,
        cid: str,
    ) -> ApiResponse[Any]:
        """
        Video Captions

        Get Bilibili video Captions data, including caption data, for transcript extraction and multilingual content analysis.

        Args:
            bvid: Bilibili Video ID (BVID).
            aid: Bilibili AID.
            cid: Bilibili CID.
        """
        return self._get(
            "/api/bilibili/get-video-caption/v2",
            {
                "bvid": bvid,
                "aid": aid,
                "cid": cid,
            },
        )
