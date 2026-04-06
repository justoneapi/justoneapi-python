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
