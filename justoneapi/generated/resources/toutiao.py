from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ToutiaoResource(BaseResource):
    """Generated resource for Toutiao."""

    def get_article_detail_v1(
        self,
        *,
        id_: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Get Toutiao article Details data, including article ID, title, and author information, for content performance analysis and media monitoring and verifying article authenticity and metadata retrieval.

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
        User Profile

        Get Toutiao user Profile data, including user ID, nickname, and avatar, for influencer profiling and audience analysis and monitoring creator performance and growth.

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
        App Keyword Search

        Get Toutiao app Keyword Search data, including matching articles, videos, and authors, for topic discovery and monitoring.

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
        Web Keyword Search

        Get Toutiao web Keyword Search data, including this is the PC version of the search API. Note that it currently only supports retrieving the first page of results, for first-page discovery of articles, videos, and authors for trend research and monitoring.

        Args:
            keyword: Search keyword or query.
        """
        return self._get(
            "/api/toutiao/search/v2",
            {
                "keyword": keyword,
            },
        )
