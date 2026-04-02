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
        Video Details (V1)

        Retrieves detailed metadata for a specific YouTube video, including its title, description,
        view counts, channel information, and media assets.

        Typical use cases
        - Tracking video engagement and statistics
        - Extracting video metadata for content analysis
        - Verifying video availability and status

        Args:
            video_id: The unique identifier for a YouTube video.
        """
        return self._get(
            "/api/youtube/get-video-detail/v1",
            {
                "videoId": video_id,
            },
        )
