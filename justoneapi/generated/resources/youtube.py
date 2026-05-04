from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class YoutubeResource(BaseResource):
    """Generated resource for YouTube."""

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
