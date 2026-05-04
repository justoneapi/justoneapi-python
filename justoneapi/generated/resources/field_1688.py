from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class Field1688Resource(BaseResource):
    """Generated resource for 1688."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Get 1688 product details, including product metadata and offer information, for sourcing research and catalog analysis.

        Args:
            item_id: A unique product identifier on 1688.
        """
        return self._get(
            "/api/1688/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Get 1688 product search results by keyword for sourcing discovery, supplier research, and market monitoring.

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/1688/search-item-list/v1",
            {
                "keyword": keyword,
            },
        )
