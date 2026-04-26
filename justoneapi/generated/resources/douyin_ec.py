from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinEcResource(BaseResource):
    """Generated resource for Douyin E-commerce."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Details

        Get Douyin E-commerce item details, including price, title, and stock, for product monitoring and competitive analysis.

        Args:
            item_id: The unique ID of the item on Douyin E-commerce.
        """
        return self._get(
            "/api/douyin-ec/get-item-detail/v1",
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
        Item Comments

        Get Douyin E-commerce item comments, including ratings, review content, and reviewer signals, for customer feedback analysis and product research.

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
