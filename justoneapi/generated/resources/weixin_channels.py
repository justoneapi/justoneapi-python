from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinChannelsResource(BaseResource):
    """Generated resource for WeChat Channels."""

    def search_video_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Searches WeChat Channels videos through the real-time WeChat web search flow. Version 1 supports publish time filtering, sort order, offset, and cookies_buffer pagination for finding recent or high-engagement Channel videos.
        """
        return self._get(
            "/api/weixin-channels/search-video/v1",
            {},
        )

    def search_video_v2(
        self,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Searches WeChat Channels videos through the categorized WeChat web search flow. Version 2 focuses on the Channels video category and keeps offset plus cookies_buffer state for continuous result collection.
        """
        return self._get(
            "/api/weixin-channels/search-video/v2",
            {},
        )

    def search_account_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Channels accounts through the categorized WeChat web search flow. Version 1 returns account-oriented search cards and pagination metadata, which helps discover Channel creators by keyword.
        """
        return self._get(
            "/api/weixin-channels/search-account/v1",
            {},
        )

    def search_account_v2(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Channels accounts and related encrypted video objects through the wxvideo keyword endpoint. Version 2 is useful when a broader account and video object result set is needed from one keyword.

        Args:
            keyword: Search keyword used to find WeChat Channels accounts and related video objects.
        """
        return self._get(
            "/api/weixin-channels/search-account/v2",
            {
                "keyword": keyword,
            },
        )

    def search_account_v3(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches for a specific WeChat Channels account id by keyword through the wxvideo account lookup endpoint. Version 3 is optimized for resolving a creator name into a v2Name identifier and account profile fields.

        Args:
            keyword: Search keyword used to resolve a WeChat Channels account id.
        """
        return self._get(
            "/api/weixin-channels/search-account/v3",
            {
                "keyword": keyword,
            },
        )

    def get_account_videos_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Account Videos

        Returns a paginated real-time list of videos, images, and live entries from a WeChat Channels account by v2Name. The response keeps last_buffer and continue_flag fields for paging through the account feed.
        """
        return self._get(
            "/api/weixin-channels/get-account-videos/v1",
            {},
        )

    def get_bound_channel_v1(
        self,
        *,
        ghid: str | None = "",
        url: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Get Bound Channel

        Returns the WeChat Channels account bound to a WeChat Official Account by ghid or article URL. It is useful for connecting Official Account publishing data with its related Channels creator identity.

        Args:
            ghid: WeChat Official Account original id used to find the bound WeChat Channels account. Use either ghid or url.
            url: WeChat Official Account article URL used to find the bound WeChat Channels account. Use either ghid or url.
        """
        return self._get(
            "/api/weixin-channels/get-bound-channel/v1",
            {
                "ghid": ghid,
                "url": url,
            },
        )

    def get_video_basic_info_v1(
        self,
        *,
        feed_info: str,
    ) -> ApiResponse[Any]:
        """
        Video Basic Info

        Resolves a copied WeChat Channels video link or short feed id into basic video and account fields. The response includes object id, object nonce id, title, cover, account v2Name, and interaction counts when available.

        Args:
            feed_info: WeChat Channels copied video link, finder-preview URL, or short feed id.
        """
        return self._get(
            "/api/weixin-channels/get-video-basic-info/v1",
            {
                "feedInfo": feed_info,
            },
        )

    def get_video_title_v1(
        self,
        *,
        object_id: str,
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Title

        Returns lightweight WeChat Channels video title and account fields by object id. It is suitable when only the title, media type, and account identity are needed without requesting downloadable media links.

        Args:
            object_id: WeChat Channels video object id.
            object_nonce_id: Optional WeChat Channels object nonce id. Supplying it can improve lookup accuracy.
        """
        return self._get(
            "/api/weixin-channels/get-video-title/v1",
            {
                "objectId": object_id,
                "objectNonceId": object_nonce_id,
            },
        )

    def convert_export_id_v1(
        self,
        *,
        export_id: str,
    ) -> ApiResponse[Any]:
        """
        Export Id Conversion

        Converts an encrypted WeChat Channels exportId from search results into the video object id and account identity fields. Use it before calling video detail, metrics, or comment endpoints that require objectId.

        Args:
            export_id: Encrypted WeChat Channels exportId returned by video search results.
        """
        return self._get(
            "/api/weixin-channels/convert-export-id/v1",
            {
                "exportId": export_id,
            },
        )

    def get_video_download_url_v1(
        self,
        *,
        object_id: str,
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Download URL

        Returns downloadable and playable media links for a WeChat Channels video by object id. The endpoint also keeps video metadata such as counts, cover image, publish time, media type, and account fields when available.

        Args:
            object_id: WeChat Channels video object id used to fetch downloadable media links.
            object_nonce_id: Optional WeChat Channels object nonce id. Supplying it can improve media lookup accuracy.
        """
        return self._get(
            "/api/weixin-channels/get-video-download-url/v1",
            {
                "objectId": object_id,
                "objectNonceId": object_nonce_id,
            },
        )

    def get_video_metrics_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Video Metrics

        Returns WeChat Channels video interaction metrics by object id, including comment, forward, like, and favorite counts. It also preserves last_buffer and continuation flags returned by the upstream metrics flow.
        """
        return self._get(
            "/api/weixin-channels/get-video-metrics/v1",
            {},
        )

    def get_video_comment_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Video Comments

        Returns first-level comments for a WeChat Channels video by object id. The response includes comment ids, author fields, like counts, reply signals, last_buffer, and continuation status for comment pagination.
        """
        return self._get(
            "/api/weixin-channels/get-video-comment/v1",
            {},
        )

    def get_video_sub_comment_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Video Sub Comments

        Returns second-level replies under a WeChat Channels video comment. Provide the video object id and root comment id from the first-level comments endpoint, and keep last_buffer for reply pagination.
        """
        return self._get(
            "/api/weixin-channels/get-video-sub-comment/v1",
            {},
        )
