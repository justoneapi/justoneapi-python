from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class JdResource(BaseResource):
    """Generated resource for JD."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details (V1)

        Retrieves product detail data for JD.com items, including basic metadata (title, item ID),
        media assets (images), shop information, item status, and pricing.

        Typical use cases:
        - Building product catalogs and enriching item content
        - E-commerce analytics and competitor tracking
        - General product lookup and verification

        Highlights
        - Price accuracy: The after-coupon (coupon-discounted) price is not accurate(Non-login version).

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_comments_v1(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Comments (V1)

        Retrieves customer reviews (comments) for a specific JD.com (China) product by item ID.
        It returns review content, rating/score, review time, user/display info (if available), and paging data.

        Typical use cases:
        - Review & sentiment monitoring: track comment volume and rating shifts.
        - Public opinion analysis: analyze negative/positive feedback signals.

        Highlights
        - Page limit: The maximum page number supported is 8.

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

    def get_shop_item_list_v1(
        self,
        *,
        shop_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Product List (V1)

        Retrieves the product list for a specific JD.com (China) shop.
            It returns items available in the shop, typically including basic product information such as item ID, title, price, sales-related data, image, and paging data.

            Typical use cases:
            - Shop catalog monitoring: track product assortments and newly listed items for a target shop.
            - Competitive analysis: analyze a shop’s product lineup, pricing, and listing changes over time.

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
