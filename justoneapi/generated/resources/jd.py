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

        Get JD.com product Details data, including pricing, images, and shop information, for catalog analysis, product monitoring, and ecommerce research.

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

        JD.com product Details v2 is available through the Just One API dashboard Task Management page. Direct API calls return an instruction message instead of fetching product data. Use the dashboard to submit product detail tasks, wait for completion, and download results.

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

        Get JD.com product Details data, including product metadata, current price, available coupon and promotion information, and the price after applying coupons, for catalog analysis, price monitoring, deal tracking, and ecommerce research.

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

        Get JD.com product Price data for price monitoring, catalog checks, repricing workflows, and ecommerce research.

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

        Get JD.com product Search data, including matched items and product metadata, for product discovery, catalog research, and market monitoring.

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

        Get JD.com product Search data sorted by sales volume, including matched items and product metadata, for product discovery, catalog research, and market monitoring.

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

        Get JD.com product Comments data, including ratings, timestamps, and reviewer signals, for customer feedback analysis and product research.

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
        is_sku: str | None = "1",
    ) -> ApiResponse[Any]:
        """
        Product Comments

        Get JD.com product Comments data, including comment text, ratings, timestamps, images, and SKU or SPU comment scope, for customer feedback analysis and product research.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
            page: Page number for paginated comments.
            is_sku: Comment scope. Use 1 for SKU-level comments and 0 for SPU-level comments.  Available Values: - `SKU_LEVEL`: Return SKU-level comments - `SPU_LEVEL`: Return SPU-level comments
        """
        return self._get(
            "/api/jd/get-item-comments/v2",
            {
                "itemId": item_id,
                "page": page,
                "isSku": is_sku,
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

        Get JD.com shop Product List data, including item titles, prices, and images, for catalog tracking and seller research.

        Args:
            shop_id: A unique shop identifier on JD.com (Shop ID).
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/jd/get-shop-item-list/v1",
            {
                "shopId": shop_id,
                "page": page,
            },
        )
