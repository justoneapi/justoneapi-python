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
        Video Details (V2)

        Retrieve comprehensive details about a specific Bilibili video, including metadata (title, tags, publishing time), statistics (views, likes, danmaku count), and uploader profile information.

        Typical use cases:
        - Tracking video performance and engagement metrics.
        - Analyzing content metadata and uploader information.

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
        User Published Videos (V2)

        Retrieve a list of videos published by a specific Bilibili user, including video metadata, cover images, and engagement metrics.

        Typical use cases:
        - Monitoring creator's content updates and publishing patterns.
        - Building user-specific video catalogs for analysis.

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
        User Profile (V2)

        Retrieve detailed profile information of a specific Bilibili user, including username, avatar, level, and verification status.

        Typical use cases:
        - Analyzing creator's profile, level, and verification status.
        - Verifying user identity and social presence on Bilibili.

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
        Video Danmaku (V2)

        Retrieve danmaku (rolling comments) for a specific Bilibili video.

        Typical use cases:
        - Analyzing real-time viewer reactions and community trends.
        - Sentiment analysis based on rolling comments.

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
        Video Comments (V2)

        Retrieve top-level comments for a specific Bilibili video, including commenter info, text, likes, and timestamps.

        Typical use cases:
        - Gathering detailed viewer feedback and community discussions.
        - Sentiment analysis and public opinion monitoring.

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
        Video Search (V2)

        Search for Bilibili videos based on keywords, returning matched videos with metadata, author information, and engagement stats.

        Typical use cases:
        - Discovering trending videos or creators by specific keywords.
        - Competitive analysis and market research on Bilibili.

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
        Share Link Resolution (V1)

        Resolve Bilibili share URLs (e.g., https://b23.tv/...) to get the original content metadata.

        Typical use cases:
        - Converting shortened mobile share links to standard BVID/metadata.
        - Automating content extraction from shared social media links.

        Highlights
        - Only supports share URLs starting with 'https://b23.tv/'.

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
        User Relation Stats (V1)

        Retrieve follower count and following count for a specific Bilibili user.

        Typical use cases:
        - Tracking creator's follower growth and audience reach.
        - Analyzing social influence and account popularity.

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
        Video Captions (V2)

        Retrieve subtitle/caption information for a specific Bilibili video.

        Typical use cases:
        - Extracting textual content from video subtitles for indexing or analysis.
        - Multi-language content processing and accessibility analysis.

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
