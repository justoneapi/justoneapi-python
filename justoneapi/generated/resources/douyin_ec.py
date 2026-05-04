from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinEcResource(BaseResource):
    """Generated resource for Douyin E-commerce."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Details

        Get Douyin E-commerce item details, including price, title, and stock, for product monitoring and competitive analysis.

        Args:
            item_id: The unique ID of the item on Douyin E-commerce.
        """
        return self._get(
            "/api/douyin-ec/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
        search_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Product Search

        Get Douyin E-commerce product Search data, including matched items and product metadata, for product discovery, catalog research, and market monitoring.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            search_id: Search ID; use the search_id value returned by the last response for subsequent pages.
        """
        return self._get(
            "/api/douyin-ec/search-item-list/v1",
            {
                "keyword": keyword,
                "page": page,
                "searchId": search_id,
            },
        )

    def get_item_comments_v1(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Item Comments

        Get Douyin E-commerce item comments, including ratings, review content, and reviewer signals, for customer feedback analysis and product research.

        Args:
            item_id: The unique ID of the item on Douyin E-commerce.
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/douyin-ec/get-item-comments/v1",
            {
                "itemId": item_id,
                "page": page,
            },
        )
