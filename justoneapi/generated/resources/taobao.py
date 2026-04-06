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

        Get Taobao and Tmall product Details data, including pricing, images, and shop details, for product research, catalog monitoring, and ecommerce analysis.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v1",
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

        Get Taobao and Tmall product Details data, including pricing, images, and shop details, for product research, catalog monitoring, and ecommerce analysis.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
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

        Get Taobao and Tmall product Details data, including pricing, images, and shop details, for product research, catalog monitoring, and ecommerce analysis.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
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

        Get Taobao and Tmall product Details data, including pricing, images, and shop details, for product research, catalog monitoring, and ecommerce analysis.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
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
    ) -> ApiResponse[Any]:
        """
        Product Reviews

        Get Taobao and Tmall product Reviews data, including ratings, timestamps, and reviewer signals, for feedback analysis and product research.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
            order_type: Sort order for the result set.  Available Values: - `feedbackdate`: Sort by feedback date - `general`: General sorting
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-item-comment/v3",
            {
                "itemId": item_id,
                "orderType": order_type,
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

        Get Taobao and Tmall shop Product List data, including item titles, prices, and images, for seller research and catalog tracking.

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

        Get Taobao and Tmall shop Product List data, including item titles, prices, and images, for seller research and catalog tracking.

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

    def get_shop_item_list_v3(
        self,
        *,
        user_id: str,
        shop_id: str,
        sort: str | None = "coefp",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Get Taobao and Tmall shop Product List data, including item titles, prices, and images, for seller research and catalog tracking.

        Args:
            user_id: Shop identifier. Also known as Seller ID or User ID (they refer to the same value).
            shop_id: Unique shop identifier on Taobao/Tmall (shop ID).
            sort: Sort order for the result set.  Available Values: - `coefp`: Comprehensive sorting - `hotsell`: Hot selling / Sales volume - `oldstarts`: New arrivals / Old starts - `bid`: Price: Low to High - `_bid`: Price: High to Low
            page: Page number for pagination.
        """
        return self._get(
            "/api/taobao/get-shop-item-list/v3",
            {
                "userId": user_id,
                "shopId": shop_id,
                "sort": sort,
                "page": page,
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

        Get Taobao and Tmall product Search data, including titles, prices, and images, for product discovery.

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
