from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TaobaoResource(BaseResource):
    """Generated resource for Taobao & Tmall."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details (V1)

        Retrieves product detail data for Taobao/Tmall items, including basic metadata (title, item ID, category),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Building product catalogs and enriching item content (e.g., images)
        - E-commerce analytics and competitor tracking
        - General product lookup and verification

        Highlights
        - Some items are not supported; in that case the response business code is 202 and retrying will not help.
        - After-coupon (coupon-discounted) price is not guaranteed: some items may miss it or return an imprecise value.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v1",
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
        Product Details (V3)

        Retrieves product detail data for Taobao/Tmall items, including basic metadata (title, item ID, category),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Price monitoring and promotion tracking
        - Building product catalogs and enriching item content (e.g., images)
        - E-commerce analytics and competitor tracking

        Highlights
        - App-based data source.
        - Accurate after-coupon (coupon-discounted) price.
        - Works across all items supported by this endpoint.

        Args:
            item_id: AUnique product identifier on Taobao/Tmall (item ID).
        """
        return self._get(
            "/api/taobao/get-item-detail/v3",
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
        Product Details (V4)

        Retrieves product detail data for Taobao/Tmall items, including basic metadata (title, item ID, category),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Building product catalogs and enriching item content (e.g., images)
        - E-commerce analytics and competitor tracking
        - General product lookup and verification

        Highlights
        - Accurate after-coupon price is available, but detailed coupon information is not included.

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
        Product Details (V5)

        Retrieves product detail data for Taobao/Tmall items, including basic metadata (title, item ID, category),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Building product catalogs and enriching item content (e.g., images)
        - E-commerce analytics and competitor tracking
        - General product lookup and verification

        Highlights
        - Some items are not supported. Unsupported items and transient collection failures may both return business code = 301.
        - Retry is not meant to be unlimited. A small number of retries (e.g., up to 5 attempts) is recommended.
          If it still returns code = 301, treat the item as unsupported and switch to another item or endpoint.

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
        Product Details (V9)

        Retrieves product detail data for Taobao/Tmall items, including basic metadata (title, item ID, category),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Building product catalogs and enriching item content (e.g., images)
        - E-commerce analytics and competitor tracking
        - General product lookup and verification

        Highlights
        - Some items are not supported; in that case the response business code is 202 and retrying will not help.
        - After-coupon (coupon-discounted) price is not guaranteed: some items may miss it or return an imprecise value.

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
        Product Reviews (V3)

        Retrieves user reviews for a Taobao/Tmall item, including review text, publish time,
        author info (when available), rating/likes (if present), and other review metadata. Supports pagination.

        Typical use cases:
        - Review and sentiment monitoring
        - Tracking rating/review volume changes over time
        - Collecting feedback for product/competitor analysis
        - Building datasets for NLP or customer-insight workflows

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
        Shop Product List (V1)

        Retrieves a paginated list of products under a Taobao/Tmall shop, including basic product metadata
        (e.g., item ID, title, price, images when available) and listing status.

        Typical use cases:
        - Monitoring a shop's assortment and new/removed products
        - Building shop-level catalogs and scheduled collection pipelines
        - Competitor shop tracking and e-commerce analytics

        Highlights
        - An empty product list may mean either: the shop has no products, or the shop is not supported by this endpoint.
          If the list is empty, verify with another shop or use an alternative endpoint if available.

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
        Shop Product List (V2)

        Retrieves a paginated list of products under a Taobao/Tmall shop, including basic product metadata
        (e.g., item ID, title, price, images when available) and listing status.

        Typical use cases:
        - Monitoring a shop's assortment and new/removed products
        - Building shop-level catalogs and scheduled collection pipelines
        - Competitor shop tracking and e-commerce analytics

        Highlights
        - An empty product list may mean either: the shop has no products, or the shop is not supported by this endpoint.
          If the list is empty, verify with another shop or use an alternative endpoint if available.

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
        Shop Product List (V3)

        Retrieves a paginated list of products under a Taobao/Tmall shop, including basic product metadata
        (e.g., item ID, title, price, images when available) and listing status.

        Typical use cases:
        - Monitoring a shop's assortment and new/removed products
        - Building shop-level catalogs and scheduled collection pipelines
        - Competitor shop tracking and e-commerce analytics

        Highlights
        - Works across all shops supported by this endpoint.

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
        Product Search (V1)

        Searches Taobao/Tmall products by keyword and optional filters, returning a paginated result set
        with basic product metadata (e.g., item ID, title, price, images when available) and listing status.

        Typical use cases:
        - Discovering products for analysis or monitoring
        - Building watchlists by keyword/category
        - Market and competitor research
        - Feeding downstream pipelines (detail collection, price tracking)

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
