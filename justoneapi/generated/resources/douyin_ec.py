from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinEcResource(BaseResource):
    """Generated resource for Douyin E-commerce."""

    def get_item_detail_v2(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Details

        Retrieves Douyin E-commerce product details by item ID. Use it to inspect a known marketplace item for catalog or product research.

        Args:
            item_id: The unique ID of the item on Douyin E-commerce.
        """
        return self._get(
            "/api/douyin-ec/get-item-detail/v2",
            {
                "itemId": item_id,
            },
        )

    def get_item_sku_info_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product SKU Info

        Retrieves SKU information for a Douyin E-commerce product by item ID. Use it to inspect the purchasable variations of a known product during catalog review.

        Args:
            item_id: The unique ID of the item on Douyin E-commerce.
        """
        return self._get(
            "/api/douyin-ec/get-item-sku-info/v1",
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

        Searches Douyin E-commerce products by keyword with page and search-ID pagination. Use it to discover marketplace products and continue a multi-page search.

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

        Retrieves paginated customer comments for a Douyin E-commerce product by item ID. Use it to review product feedback for a known marketplace item.

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

    def get_shop_item_list_v1(
        self,
        *,
        shop_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Retrieves a paginated product list for a Douyin E-commerce shop by shop ID. Use it to browse a known seller's marketplace catalog page by page.

        Args:
            shop_id: The unique ID of the shop on Douyin E-commerce.
            page: Page number for pagination.
        """
        return self._get(
            "/api/douyin-ec/get-shop-item-list/v1",
            {
                "shopId": shop_id,
                "page": page,
            },
        )
