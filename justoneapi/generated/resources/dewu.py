from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DewuResource(BaseResource):
    """Generated resource for Dewu (Poizon)."""

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches Dewu (Poizon) products by keyword with page-based pagination. Use it to discover marketplace products matching a title or product term.

        Args:
            keyword: Search keyword.
            page: Page number for pagination. The first page is 1.
        """
        return self._get(
            "/api/dewu/search-item-list/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )
