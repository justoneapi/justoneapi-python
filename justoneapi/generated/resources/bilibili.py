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

        Retrieves details for a Bilibili video identified by its BVID. Use it to look up a known video for content review, cataloging, or subsequent engagement analysis.

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

        Retrieves videos published by a Bilibili user identified by UID, with an optional continuation parameter from a prior response. Use it to browse a creator's uploads or continue through their video list.

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

        Retrieves a Bilibili user profile identified by UID. Use it to look up a known account for creator research, profile review, or subsequent retrieval of that user's videos.

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

        Retrieves one page of danmaku comments for a Bilibili video segment identified by AID and CID. Use it to review time-synchronized audience reactions or page through danmaku for a known video.

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

        Retrieves comments for a Bilibili video identified by AID, with optional cursor pagination. Use it to review audience discussion, continue through comment pages, or support comment moderation and analysis.

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

        Searches Bilibili videos by keyword with page-based pagination and sorting by general ranking, play count, publish time, danmaku count, or favorites. Use it to support content discovery, topic research, or ranking-focused searches.

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

        Resolve a supported Bilibili short share link that targets a video and return its public redirect URL. Use it to expand video links before subsequent Bilibili content lookup or processing.

        Args:
            share_url: A Bilibili short share URL beginning with https://b23.tv/.
        """
        return self._get(
            "/api/bilibili/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )

    def get_user_relation_stat_v1(
        self,
        *,
        wmid: str,
    ) -> ApiResponse[Any]:
        """
        User Relation Stats

        Retrieves relation statistics for a Bilibili user identified by WMID. Use it to compare audience relationships across creator accounts or track relation-count changes for a known user.

        Args:
            wmid: Bilibili User ID (WMID).
        """
        return self._get(
            "/api/bilibili/get-user-relation-stat/v1",
            {
                "wmid": wmid,
            },
        )

    def get_video_caption_v2(
        self,
        *,
        bvid: str,
        aid: str,
        cid: str,
    ) -> ApiResponse[Any]:
        """
        Video Captions

        Retrieves caption data for a Bilibili video segment identified by BVID, AID, and CID. Use it to obtain subtitles for transcript extraction, accessibility review, or language-focused content analysis.

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
