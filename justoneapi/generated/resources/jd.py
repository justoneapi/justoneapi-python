from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class JdResource(BaseResource):
    """Generated resource for JD.com."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieve JD.com product details for a known item ID. Use it to inspect an individual product after finding its identifier.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v2(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Access the asynchronous JD.com product detail workflow from the Just One API dashboard Task Management page. Use it to submit and download product detail research tasks.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v2",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v3(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves JD.com product details for a known item ID. Use it to review a known listing during product research or offer comparison.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v3",
            {
                "itemId": item_id,
            },
        )

    def get_item_price_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Price

        Retrieve the current JD.com product price for a known item ID. Use it to check a product's price before catalog comparison or purchase analysis.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-price/v1",
            {
                "itemId": item_id,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Search JD.com products by keyword with page-based pagination. Use it to discover products and collect item IDs for follow-up lookups.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/jd/search-item-list/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def search_item_list_v2(
        self,
        *,
        keyword: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Search JD.com products by keyword with page-based pagination and sales-volume ordering. Use it to discover popular products and collect item IDs for follow-up lookups.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/jd/search-item-list/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_item_comments_v1(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Comments

        Retrieve paginated customer comments for a JD.com product identified by item ID. Use it to review buyer feedback for a known product.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/jd/get-item-comments/v1",
            {
                "itemId": item_id,
                "page": page,
            },
        )

    def get_item_comments_v2(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Comments

        Retrieve paginated JD.com product comments for a specific SKU. Use it to review buyer feedback for that product.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/jd/get-item-comments/v2",
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

        Retrieve a page of products from a JD.com shop identified by shop ID. Use it to browse a seller's catalog and collect item IDs for follow-up lookups.

        Args:
            shop_id: A unique shop identifier on JD.com (Shop ID).
            page: Page number for the paginated shop product list.
        """
        return self._get(
            "/api/jd/get-shop-item-list/v1",
            {
                "shopId": shop_id,
                "page": page,
            },
        )
