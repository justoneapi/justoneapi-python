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

        Retrieves details for a Toutiao article identified by its article ID. Use it to look up a known article for content review, archiving, or related media analysis.

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

        Retrieves a Toutiao user profile identified by user ID. Use it to look up a known account for creator research, profile review, or related article analysis.

        Args:
            user_id: The unique identifier of the Toutiao user.
        """
        return self._get(
            "/api/toutiao/get-user-detail/v1",
            {
                "userId": user_id,
            },
        )

    def get_user_id_v1(
        self,
        *,
        user_profile_url: str,
    ) -> ApiResponse[Any]:
        """
        User ID

        Resolves the user ID associated with a Toutiao profile URL. Use it to convert a known profile link into the identifier required for subsequent user-profile lookups.

        Args:
            user_profile_url: The Toutiao user profile URL used to resolve the user ID.
        """
        return self._get(
            "/api/toutiao/get-user-id/v1",
            {
                "userProfileUrl": user_profile_url,
            },
        )

    def search_v2(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Web Keyword Search

        Searches Toutiao web articles by keyword. Use it to discover relevant articles for topic research, media monitoring, or source collection.

        Args:
            keyword: Search keyword or query.
        """
        return self._get(
            "/api/toutiao/search/v2",
            {
                "keyword": keyword,
            },
        )
