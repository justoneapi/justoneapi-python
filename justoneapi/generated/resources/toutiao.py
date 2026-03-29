from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ToutiaoResource(BaseResource):
    """Generated resource for Toutiao APIs."""

    def get_article_detail_v1(
        self,
        *,
        id_: str,
    ) -> ApiResponse[Any]:
        """
        Article Details (V1)

        Retrieve detailed information for a specific Toutiao (Jinri Toutiao) article by its article ID.

        The API returns complete metadata including article ID, title, author information, publish time, content text or summary, engagement metrics (views, comments, likes, shares), and the article URL.

        Typical use cases:
        - Content performance analysis and media monitoring.
        - Verifying article authenticity and metadata retrieval.

        Args:
            id_: The unique identifier of the Toutiao article.
        """
        return self._get(
            "/api/toutiao/get-article-detail/v1",
            {
                "id": id_,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile (V1)

        Retrieve detailed information for a specific Toutiao (Jinri Toutiao) user by their user ID.

        The API returns comprehensive profile metadata including user ID, nickname, avatar, bio/description, verification status, follower and following counts, total likes, and total published articles or videos.

        Typical use cases:
        - Influencer profiling and audience analysis.
        - Monitoring creator performance and growth.

        Args:
            user_id: The unique identifier of the Toutiao user.
        """
        return self._get(
            "/api/toutiao/get-user-detail/v1",
            {
                "userId": user_id,
            },
        )

    def search_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        search_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Search (V1)

        Perform a keyword-based search on Toutiao (Jinri Toutiao) App to retrieve a list of matching articles, videos, and other content.

        The API returns detailed search results including title, summary, author, publish time, and engagement metrics such as likes, comments, and shares.

        Typical use cases:
        - Content aggregation and trend analysis.
        - Media monitoring and keyword intelligence.

        Args:
            keyword: Search keyword or query.
            page: Page number for pagination.
            search_id: Search session ID for consistent pagination (not required for the first page).
        """
        return self._get(
            "/api/toutiao/search/v1",
            {
                "keyword": keyword,
                "page": page,
                "searchId": search_id,
            },
        )

    def search_v2(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Search (V2)

        Perform a keyword-based search on Toutiao (Jinri Toutiao) PC version to retrieve a list of matching articles, videos, and other content.

        The API returns detailed search results including title, summary, author, publish time, and engagement metrics such as likes, comments, and shares.

        Typical use cases:
        - Content aggregation and trend analysis.
        - Media monitoring and keyword intelligence.

        Highlights
        - This is the PC version of the search API. Note that it currently only supports retrieving the first page of results.

        Args:
            keyword: Search keyword or query.
        """
        return self._get(
            "/api/toutiao/search/v2",
            {
                "keyword": keyword,
            },
        )
