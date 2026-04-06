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
