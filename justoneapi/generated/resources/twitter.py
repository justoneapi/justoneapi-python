from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TwitterResource(BaseResource):
    """Generated resource for Twitter."""

    def search_v1(
        self,
        *,
        keyword: str,
        search_type: str | None = "Top",
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Search Timeline

        Search Twitter timeline data through TIKHUB, including top, latest, media, people, and list results with cursor pagination for social listening, topic tracking, and account discovery.

        Args:
            keyword: Search keyword.
            search_type: Search result type.  Available Values: - `TOP`: Top search results - `LATEST`: Latest search results - `MEDIA`: Media search results - `PEOPLE`: People search results - `LISTS`: List search results
            cursor: Pagination cursor returned by the previous response.
        """
        return self._get(
            "/api/twitter/search/v1",
            {
                "keyword": keyword,
                "searchType": search_type,
                "cursor": cursor,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        rest_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Twitter user Profile data, including account metadata, audience metrics, and verification-related fields, for accessing user profile metadata (e.g., description, location, verification status) and collecting follower and following counts.

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
        User Published Posts

        Get Twitter user Published Posts data, including post content, timestamps, and engagement data, for account monitoring and content analysis.

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
