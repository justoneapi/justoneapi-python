from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TwitterResource(BaseResource):
    """Generated resource for X(Twitter) APIs."""

    def get_user_detail_v1(
        self,
        *,
        rest_id: str,
    ) -> ApiResponse[Any]:
        """
        User Details (V1)

        Retrieves basic public information for a specific X (Twitter) user using their Rest ID.

        Typical use cases:
        - Accessing user profile metadata (e.g., description, location, verification status).
        - Collecting follower and following counts.
        - Verifying account details for identity confirmation.

        Args:
            rest_id: The unique numeric identifier (Rest ID) for the X user.
        """
        return self._get(
            "/api/twitter/get-user-detail/v1",
            {
                "restId": rest_id,
            },
        )

    def get_user_posts_v1(
        self,
        *,
        rest_id: str,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Published Posts (V1)

        Retrieves the public tweet timeline (posts) for a specific X (Twitter) user.

        Typical use cases:
        - Monitoring recent activity of influential accounts.
        - Collecting tweets for archival or content analysis.
        - Tracking engagement on specific user-generated content.

        Highlights:
        - Supports pagination via cursor for large datasets.

        Args:
            rest_id: The unique numeric identifier (Rest ID) for the X user.
            cursor: Pagination cursor for navigating through long timelines.
        """
        return self._get(
            "/api/twitter/get-user-posts/v1",
            {
                "restId": rest_id,
                "cursor": cursor,
            },
        )
