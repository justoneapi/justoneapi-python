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

        Searches X (Twitter) by keyword across top, latest, media, people, or list result modes with cursor pagination. Use it to find public conversations, accounts, media, or lists related to a topic.

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

        Retrieves an X (Twitter) user profile identified by its numeric Rest ID. Use it to review a known account before monitoring its posts or conducting creator and account research.

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

        Retrieves posts published by an X (Twitter) user identified by Rest ID, with cursor pagination. Use it to browse a known account's timeline or continue through its public post history.

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

    def get_post_comments_v1(
        self,
        *,
        tweet_id: str,
        cursor: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Retrieves the latest comments for an X (Twitter) post identified by tweet ID, with cursor pagination. Use it to review recent discussion on a known post and continue through additional comment pages.

        Args:
            tweet_id: The unique identifier of the X (Twitter) post.
            cursor: Pagination cursor returned by the previous response.
        """
        return self._get(
            "/api/twitter/get-post-comments/v1",
            {
                "tweetId": tweet_id,
                "cursor": cursor,
            },
        )
