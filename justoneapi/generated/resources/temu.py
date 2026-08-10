from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TemuResource(BaseResource):
    """Generated resource for Temu."""

    def get_homepage_goods_v1(
        self,
        *,
        site: str,
        offset: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Homepage Product Feed

        Retrieves Temu homepage product feed cards for a selected site with offset pagination. Use it for product sourcing, catalog monitoring, and marketplace trend analysis.

        Args:
            site: Temu site used to select the regional homepage feed.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            offset: Zero-based offset for pagination.
        """
        return self._get(
            "/api/temu/get-homepage-goods/v1",
            {
                "site": site,
                "offset": offset,
            },
        )
