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

        Get Xianyu (GooFish) product Search data by keyword, including matched second-hand marketplace listings, seller signals, prices, images, filters, and pagination metadata, for resale-market discovery, catalog research, pricing analysis, and item monitoring.

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

        Get Xianyu (GooFish) product Details data by item ID, including listing metadata, seller information, images, item status, pricing, and marketplace flow data, for second-hand item inspection, resale tracking, and ecommerce research.

        Args:
            item_id: A unique product identifier on Xianyu.
        """
        return self._get(
            "/api/xianyu/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )
