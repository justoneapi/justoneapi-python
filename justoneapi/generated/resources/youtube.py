from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class YoutubeResource(BaseResource):
    """Generated resource for YouTube."""

    def search_v1(
        self,
        *,
        keyword: str | None = "",
        lang: str | None = None,
        upload_date: str | None = "all",
        duration: str | None = "all",
        sort_by: str | None = "relevance",
        next_token: str | None = None,
    ) -> ApiResponse[Any]:
        """
        General Search

        Search YouTube videos by keyword with optional language, upload-date, duration, and sort filters, or continue with a pagination token. Use it to discover public videos or browse additional result pages.

        Args:
            keyword: Search term. Required for the first page; leave empty when using nextToken.
            lang: Optional IETF language tag for localized results, such as en-US. Leave empty to use the default language.
            upload_date: Upload-date filter.  Available Values: - `all`: No upload-date limit - `lastHour`: Uploaded within the last hour - `today`: Uploaded today - `thisWeek`: Uploaded this week - `thisMonth`: Uploaded this month - `thisYear`: Uploaded this year
            duration: Video-duration filter.  Available Values: - `all`: No duration limit - `short`: Short videos under 4 minutes - `medium`: Medium videos from 4 to 20 minutes - `long`: Long videos over 20 minutes
            sort_by: Sort order for search results.  Available Values: - `relevance`: Sort by relevance - `uploadDate`: Sort by upload date - `viewCount`: Sort by view count - `rating`: Sort by rating
            next_token: Pagination token returned by the previous response. When provided, the keyword and filter parameters are ignored; very long tokens may exceed GET URL limits.
        """
        return self._get(
            "/api/youtube/search/v1",
            {
                "keyword": keyword,
                "lang": lang,
                "uploadDate": upload_date,
                "duration": duration,
                "sortBy": sort_by,
                "nextToken": next_token,
            },
        )

    def get_video_detail_v1(
        self,
        *,
        video_id: str,
        lang: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Retrieve public details for a YouTube video identified by video ID. Use it to inspect a known video before further content or comment analysis.

        Args:
            video_id: The unique identifier for a YouTube video.
            lang: Optional IETF language tag for localized video details, such as en-US. Leave empty to use the default language.
        """
        return self._get(
            "/api/youtube/get-video-detail/v1",
            {
                "videoId": video_id,
                "lang": lang,
            },
        )

    def get_channel_videos_v1(
        self,
        *,
        channel_id: str,
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Channel Videos

        Retrieve public videos from a YouTube channel, with optional cursor-based pagination. Use it to browse a channel's uploads and continue through additional result pages.

        Args:
            channel_id: The unique identifier for a YouTube channel.
            cursor: The cursor for pagination.
        """
        return self._get(
            "/api/youtube/get-channel-videos/v1",
            {
                "channelId": channel_id,
                "cursor": cursor,
            },
        )

    def get_video_captions_v1(
        self,
        *,
        video_id: str,
        language_code: str | None = "",
        format: str | None = "srt",
    ) -> ApiResponse[Any]:
        """
        Video Captions

        Retrieve available caption tracks for a YouTube video or request captions in SRT, XML, JSON3, or plain-text format. Use it to support transcription, accessibility, localization, or text analysis.

        Args:
            video_id: The unique identifier for a YouTube video.
            language_code: Caption language code, such as en, zh-Hans, or a.en. Leave it empty to retrieve available caption tracks.
            format: Caption output format.  Available Values: - `srt`: SubRip caption format with timeline cues - `xml`: Original XML caption format - `json3`: YouTube original JSON caption structure - `txt`: Plain text without timeline cues
        """
        return self._get(
            "/api/youtube/get-video-captions/v1",
            {
                "videoId": video_id,
                "languageCode": language_code,
                "format": format,
            },
        )

    def get_channel_shorts_v1(
        self,
        *,
        channel_id: str,
        continuation_token: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Channel Shorts

        Retrieve public Shorts from a YouTube channel ID with optional continuation-token pagination. Use it to browse a channel's short-form videos and continue through additional result pages.

        Args:
            channel_id: The UC-prefixed unique identifier for a YouTube channel. @username handles are not supported.
            continuation_token: Pagination token returned by the previous response.
        """
        return self._get(
            "/api/youtube/get-channel-shorts/v1",
            {
                "channelId": channel_id,
                "continuationToken": continuation_token,
            },
        )

    def get_video_comment_v1(
        self,
        *,
        video_id: str,
        cursor: str | None = "",
        language_code: str | None = "zh-CN",
        country_code: str | None = "US",
        sort_by: str | None = "newest",
    ) -> ApiResponse[Any]:
        """
        Video Comment List

        Retrieve first-level comments for a YouTube video with sorting, locale options, and cursor pagination. Use it to review audience discussion or continue through additional comment pages.

        Args:
            video_id: The unique identifier for a YouTube video.
            cursor: Pagination cursor returned by the previous response.
            language_code: Language preference for response data.
            country_code: Region code for response data.
            sort_by: Sort order for the comment list.  Available Values: - `top`: Top comments - `newest`: Newest comments
        """
        return self._get(
            "/api/youtube/get-video-comment/v1",
            {
                "videoId": video_id,
                "cursor": cursor,
                "languageCode": language_code,
                "countryCode": country_code,
                "sortBy": sort_by,
            },
        )

    def get_video_sub_comment_v1(
        self,
        *,
        cursor: str,
        language_code: str | None = "zh-CN",
        country_code: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Video Sub Comment List

        Retrieve replies associated with a YouTube comment continuation cursor, with optional locale settings. Use it to follow threaded discussion beyond first-level comments.

        Args:
            cursor: Reply cursor from a first-level comment response.
            language_code: Language preference for response data.
            country_code: Region code for response data.
        """
        return self._get(
            "/api/youtube/get-video-sub-comment/v1",
            {
                "cursor": cursor,
                "languageCode": language_code,
                "countryCode": country_code,
            },
        )
