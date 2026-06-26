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
        continuation_token: str | None = "",
        upload_date: str | None = None,
        type: str | None = None,
        duration: str | None = None,
        features: str | None = None,
        sort_by: str | None = None,
    ) -> ApiResponse[Any]:
        """
        General Search

        Search YouTube through TIKHUB general search, returning mixed video, channel, playlist, and movie results with continuation tokens plus filters for upload date, type, duration, features, and sort order for discovery and monitoring.

        Args:
            keyword: Search keyword. Required on the first request; leave empty when using a continuation token.
            continuation_token: Pagination token returned by the previous response.
            upload_date: Filter results by upload date.  Available Values: - `last_hour`: Uploaded within the last hour - `today`: Uploaded today - `this_week`: Uploaded this week - `this_month`: Uploaded this month - `this_year`: Uploaded this year
            type: Filter results by result type.  Available Values: - `video`: Video results - `channel`: Channel results - `playlist`: Playlist results - `movie`: Movie results
            duration: Filter video results by duration. Supported request values: short, medium, long.  Available Values: - `SHORT`: Short videos under 4 minutes - `MEDIUM`: Medium videos from 4 to 20 minutes - `LONG`: Long videos over 20 minutes
            features: Feature filters separated by commas. Supported values: live, 4k, hd, subtitles, creative_commons, 360, vr180, 3d, hdr.
            sort_by: Sort order for search results.  Available Values: - `relevance`: Sort by relevance - `upload_date`: Sort by upload date - `view_count`: Sort by view count - `rating`: Sort by rating
        """
        return self._get(
            "/api/youtube/search/v1",
            {
                "keyword": keyword,
                "continuationToken": continuation_token,
                "uploadDate": upload_date,
                "type": type,
                "duration": duration,
                "features": features,
                "sortBy": sort_by,
            },
        )

    def get_video_detail_v1(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Get YouTube video Details data, including its title, description, and view counts, for tracking video engagement and statistics, extracting video metadata for content analysis, and verifying video availability and status.

        Args:
            video_id: The unique identifier for a YouTube video.
        """
        return self._get(
            "/api/youtube/get-video-detail/v1",
            {
                "videoId": video_id,
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

        Retrieve a list of videos from a specific YouTube channel, providing detailed insights into content performance and upload history.

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

        Get YouTube video Captions data through TIKHUB, including available caption tracks or formatted content in SRT, XML, JSON3, or plain text for transcription, localization, accessibility review, and content analysis.

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

        Get first-level video comments, author profiles, like counts, reply counts, and reply cursors for audience feedback and engagement analysis.

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

        Get second-level video comment replies, reply authors, like counts, and pagination cursors for threaded discussion analysis.

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
