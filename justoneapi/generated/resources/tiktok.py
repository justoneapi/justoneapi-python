from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TiktokResource(BaseResource):
    """Generated resource for TikTok."""

    def get_user_post_v1(
        self,
        *,
        sec_uid: str,
        cursor: str | None = "0",
        sort: str | None = "LATEST",
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Retrieves posts published by a TikTok user identified by secUid, with cursor pagination and latest or popular sorting. Use it to browse a creator's posting history or continue through their public post feed.

        Args:
            sec_uid: The opaque security ID returned for the TikTok user.
            cursor: Pagination cursor. Use '0' for the first page, then use the max_cursor value returned in the previous response.
            sort: Sorting criteria for the user's posts.  Available Values: - `LATEST`: Newest posts first (default) - `MOST_POPULAR`: Most popular posts first
        """
        return self._get(
            "/api/tiktok/get-user-post/v1",
            {
                "secUid": sec_uid,
                "cursor": cursor,
                "sort": sort,
            },
        )

    def get_post_detail_v1(
        self,
        *,
        post_id: str,
    ) -> ApiResponse[Any]:
        """
        Post Details

        Retrieves details for a TikTok post identified by its post ID. Use it to look up a known TikTok video before content review, reporting, or related engagement analysis.

        Args:
            post_id: The unique ID of the TikTok post.
        """
        return self._get(
            "/api/tiktok/get-post-detail/v1",
            {
                "postId": post_id,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        unique_id: str | None = "",
        sec_uid: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a TikTok user profile by public username or secUid. Use it to look up a known account for creator research, profile review, or subsequent user-post retrieval.

        Args:
            unique_id: The public TikTok handle or username of the user.
            sec_uid: The unique security ID of the user.
        """
        return self._get(
            "/api/tiktok/get-user-detail/v1",
            {
                "uniqueId": unique_id,
                "secUid": sec_uid,
            },
        )

    def get_post_comment_v1(
        self,
        *,
        aweme_id: str,
        cursor: str | None = "0",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Retrieves comments for a TikTok post with cursor pagination. Use it to review audience discussion, continue through comment pages, or support comment analysis for a known post.

        Args:
            aweme_id: The unique ID of the TikTok post (awemeId).
            cursor: Pagination cursor. Start with '0'.
        """
        return self._get(
            "/api/tiktok/get-post-comment/v1",
            {
                "awemeId": aweme_id,
                "cursor": cursor,
            },
        )

    def get_post_sub_comment_v1(
        self,
        *,
        aweme_id: str,
        comment_id: str,
        cursor: str | None = "0",
    ) -> ApiResponse[Any]:
        """
        Comment Replies

        Retrieves replies to a specific comment on a TikTok post with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for a known post comment.

        Args:
            aweme_id: The unique ID of the TikTok post.
            comment_id: The unique ID of the comment to retrieve replies for.
            cursor: Pagination cursor. Start with '0'.
        """
        return self._get(
            "/api/tiktok/get-post-sub-comment/v1",
            {
                "awemeId": aweme_id,
                "commentId": comment_id,
                "cursor": cursor,
            },
        )

    def search_user_v1(
        self,
        *,
        keyword: str,
        cursor: str | None = "0",
        search_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Search

        Searches TikTok users by keyword with cursor pagination and search-session continuity. Use it to discover accounts related to a creator name, topic, brand, or other search term.

        Args:
            keyword: Search keywords.
            cursor: Pagination cursor. Start with '0'.
            search_id: The 'logid' returned from the previous request for consistent search results.
        """
        return self._get(
            "/api/tiktok/search-user/v1",
            {
                "keyword": keyword,
                "cursor": cursor,
                "searchId": search_id,
            },
        )

    def search_post_v1(
        self,
        *,
        keyword: str,
        offset: int | None = 0,
        sort_type: str | None = "RELEVANCE",
        publish_time: str | None = "ALL",
        region: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Post Search

        Searches TikTok posts by keyword with offset pagination plus sorting, publish-time, and region controls. Use it to support regional content discovery, topic research, or monitoring keyword-related videos.

        Args:
            keyword: Search keywords.
            offset: Pagination offset, starting from 0 and stepping by 20.
            sort_type: Sorting criteria for search results.  Available Values: - `RELEVANCE`: Relevance (Default) - `MOST_LIKED`: Most Liked
            publish_time: Filter posts by publishing time.  Available Values: - `ALL`: All Time - `ONE_DAY`: Last 24 Hours - `ONE_WEEK`: Last 7 Days - `ONE_MONTH`: Last 30 Days - `THREE_MONTHS`: Last 90 Days - `HALF_YEAR`: Last 180 Days
            region: ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB').
        """
        return self._get(
            "/api/tiktok/search-post/v1",
            {
                "keyword": keyword,
                "offset": offset,
                "sortType": sort_type,
                "publishTime": publish_time,
                "region": region,
            },
        )
