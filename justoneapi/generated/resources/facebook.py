from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class FacebookResource(BaseResource):
    """Generated resource for Facebook."""

    def search_post_v1(
        self,
        *,
        keyword: str,
        start_date: str | None = None,
        end_date: str | None = None,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Search

        Get Facebook post Search data, including matched results, metadata, and ranking signals, for discovering relevant public posts for specific keywords and analyzing engagement and reach of public content on facebook.

        Args:
            keyword: Keyword to search for in public posts. Supports basic text matching.
            start_date: Start date for the search range (inclusive), formatted as yyyy-MM-dd.
            end_date: End date for the search range (inclusive), formatted as yyyy-MM-dd.
            cursor: Pagination cursor for fetching the next set of results.
        """
        return self._get(
            "/api/facebook/search-post/v1",
            {
                "keyword": keyword,
                "startDate": start_date,
                "endDate": end_date,
                "cursor": cursor,
            },
        )

    def get_profile_id_v1(
        self,
        *,
        url: str,
    ) -> ApiResponse[Any]:
        """
        Get Profile ID

        Retrieve the unique Facebook profile ID from a given profile URL.

        Args:
            url: The path part of the Facebook profile URL. Do not include `https://www.facebook.com`. Example: `/people/To-Bite/pfbid021XLeDjjZjsoWse1H43VEgb3i1uCLTpBvXSvrnL2n118YPtMF5AZkBrZobhWWdHTHl/`
        """
        return self._get(
            "/api/facebook/get-profile-id/v1",
            {
                "url": url,
            },
        )

    def get_profile_posts_v1(
        self,
        *,
        profile_id: str,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Get Profile Posts

        Get public posts from a specific Facebook profile using its profile ID.

        Args:
            profile_id: The unique Facebook profile ID.
            cursor: Pagination cursor for fetching the next set of results.
        """
        return self._get(
            "/api/facebook/get-profile-posts/v1",
            {
                "profileId": profile_id,
                "cursor": cursor,
            },
        )
