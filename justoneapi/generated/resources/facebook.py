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

        Searches public Facebook posts by keyword with optional inclusive date-range filters and cursor pagination. Use it to find topic-related posts or continue a time-bounded public-content search.

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

        Resolves the Facebook profile ID associated with a submitted profile-path value. Use it to obtain the identifier required before retrieving posts for a known public profile.

        Args:
            url: The path portion of the Facebook profile URL, such as /<profile-path>. Do not include the scheme or host.
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

        Retrieves public posts for a Facebook profile ID with cursor pagination. Use it to browse a known profile's public posting history or continue through subsequent post pages.

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

    def get_post_comments_v1(
        self,
        *,
        post_id: str,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Retrieves comments for a Facebook post ID with cursor pagination. Use it to review discussion associated with a known public post or continue through subsequent comment pages.

        Args:
            post_id: The unique identifier of the Facebook post.
            cursor: Pagination cursor for fetching the next set of comments.
        """
        return self._get(
            "/api/facebook/get-post-comments/v1",
            {
                "postId": post_id,
                "cursor": cursor,
            },
        )
