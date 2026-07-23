from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TaobaoResource(BaseResource):
    """Generated resource for Taobao and Tmall."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Taobao or Tmall product details by item ID through the V1 endpoint. Use it to perform direct product lookup for catalog research, product monitoring, or ecommerce analysis.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v1",
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

        Access the asynchronous Taobao and Tmall product detail workflow from the Just One API dashboard Task Management page. Use it to submit and download product detail research tasks.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v2",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v4(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Taobao or Tmall product details by item ID through the V4 endpoint. Use it to perform direct product lookup for catalog research, product monitoring, or ecommerce analysis.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v4",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v5(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Taobao or Tmall product details by item ID through the V5 endpoint. Use it to perform direct product lookup for catalog research, product monitoring, or ecommerce analysis.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v5",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v9(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Taobao or Tmall product details by item ID through the V9 endpoint. Use it to perform direct product lookup for catalog research, product monitoring, or ecommerce analysis.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v9",
            {
                "itemId": item_id,
            },
        )

    def get_item_comment_v3(
        self,
        *,
        item_id: str,
        order_type: str | None = "feedbackdate",
        page: int | None = 1,
        content: str | None = "SHOW_DEFAULT_POSITIVE_REVIEWS",
    ) -> ApiResponse[Any]:
        """
        Product Reviews

        Retrieves Taobao and Tmall product reviews by item ID with page-based pagination, configurable sorting, and optional exclusion of default positive reviews. Use it to analyze customer feedback.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
            order_type: Sort order for the result set.  Available Values: - `feedbackdate`: Sort by feedback date - `general`: General sorting
            page: Page number for pagination.
            content: Controls default positive reviews. Use `1` to hide them; omit this parameter to include them (default).  Available Values: - `SHOW_DEFAULT_POSITIVE_REVIEWS`: Include default positive reviews (default) - `HIDE_DEFAULT_POSITIVE_REVIEWS`: Hide default positive reviews
        """
        return self._get(
            "/api/taobao/get-item-comment/v3",
            {
                "itemId": item_id,
                "orderType": order_type,
                "page": page,
                "content": content,
            },
        )

    def get_social_feed_v1(
        self,
        *,
        item_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Product Questions

        Retrieves the Taobao or Tmall product social feed by item ID with page-based pagination. Use it to review product questions and related discussion during customer-concern or product research.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-social-feed/v1",
            {
                "itemId": item_id,
                "page": page,
            },
        )

    def get_shop_item_list_v1(
        self,
        *,
        user_id: str,
        sort: str | None = "_sale",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Retrieves products from a Taobao or Tmall shop by seller or user ID, with page-based pagination and default or sales sorting. Use it to browse or monitor a seller catalog.

        Args:
            user_id: Shop identifier. Also known as Seller ID or User ID (they refer to the same value).
            sort: Sort order for the result set.  Available Values: - `_sale`: Sales - `_default`: Default
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-shop-item-list/v1",
            {
                "userId": user_id,
                "sort": sort,
                "page": page,
            },
        )

    def get_shop_item_list_v2(
        self,
        *,
        user_id: str,
        shop_id: str,
        sort: str | None = "coefp",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Retrieves products from a Taobao or Tmall shop using both seller or user ID and shop ID, with page-based pagination and configurable sorting. Use it to browse a known shop catalog.

        Args:
            user_id: Shop identifier. Also known as Seller ID or User ID (they refer to the same value).
            shop_id: Unique shop identifier on Taobao/Tmall (shop ID).
            sort: Sort order for the result set.  Available Values: - `coefp`: Comprehensive sorting - `hotsell`: Hot selling / Sales volume - `oldstarts`: New arrivals / Old starts - `bid`: Price: Low to High - `_bid`: Price: High to Low
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-shop-item-list/v2",
            {
                "userId": user_id,
                "shopId": shop_id,
                "sort": sort,
                "page": page,
            },
        )

    def get_shop_item_list_v4(
        self,
        *,
        seller_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Retrieves products from a Taobao or Tmall shop by seller ID with page-based pagination. Use it to browse or monitor a known seller's catalog across result pages.

        Args:
            seller_id: Taobao/Tmall seller user ID used to identify the shop.
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-shop-item-list/v4",
            {
                "sellerId": seller_id,
                "page": page,
            },
        )

    def get_item_sale_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Sales

        Retrieves the 30-day sales count for a Taobao or Tmall product by item ID. Use it to compare recent product sales or support ecommerce monitoring and product research.

        Args:
            item_id: Unique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-sale/v1",
            {
                "itemId": item_id,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        sort: str | None = "_sale",
        tmall: bool | None = False,
        start_price: str | None = None,
        end_price: str | None = None,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches Taobao and Tmall products by keyword with page, sort, optional Tmall-only, and inclusive price-range filters. Use it to discover products and narrow ecommerce research.

        Args:
            keyword: Search keyword.
            sort: Sort order for the result set.  Available Values: - `_sale`: Sales - `_bid`: Price: High to Low - `bid`: Price: Low to High - `_coefp`: General
            tmall: Whether to filter results to Tmall only.
            start_price: Minimum price filter (inclusive).
            end_price: Maximum price filter (inclusive).
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/search-item-list/v1",
            {
                "keyword": keyword,
                "sort": sort,
                "tmall": tmall,
                "startPrice": start_price,
                "endPrice": end_price,
                "page": page,
            },
        )
