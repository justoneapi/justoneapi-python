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

        Retrieves the public product detail for a 1688 wholesale listing by item ID. Use it to review a known offer during product sourcing or catalog research.

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

        Searches 1688 wholesale product listings by keyword. Use it to discover candidate products or suppliers during sourcing and market research.

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/1688/search-item-list/v1",
            {
                "keyword": keyword,
            },
        )
