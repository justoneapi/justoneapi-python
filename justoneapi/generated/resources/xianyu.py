from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XianyuResource(BaseResource):
    """Generated resource for Xianyu (GooFish)."""

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
        sort: str | None = "active",
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches Xianyu (GooFish) second-hand listings by keyword with page and sort controls. Use it to discover resale items by activity, recency, seller credit, price, or listing time.

        Args:
            keyword: Search keyword.
            page: Page number for pagination. The first page is 1.
            sort: Sort order for Xianyu search results.  Available Values: - `active`: Active listings first. - `recent`: Recent nearby or position-based results first. - `credit`: Seller credit first. - `price_asc`: Lowest price first. - `price_desc`: Highest price first. - `price_drop`: Reduced-price listings first. - `newest`: Newly listed items first.
        """
        return self._get(
            "/api/xianyu/search-item-list/v1",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
            },
        )

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves the public detail for a Xianyu (GooFish) second-hand listing by item ID. Use it to inspect a known resale item after search or link discovery.

        Args:
            item_id: A unique product identifier on Xianyu.
        """
        return self._get(
            "/api/xianyu/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )
