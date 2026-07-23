from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class BeikeResource(BaseResource):
    """Generated resource for Beike."""

    def ershoufang_detail_v1(
        self,
        *,
        city_id: str,
        house_code: str,
    ) -> ApiResponse[Any]:
        """
        Resale Housing Details

        Retrieves a Beike resale-housing listing by city ID and house code. Use it to inspect a known second-hand property listing in a specific city.

        Args:
            city_id: The numeric Beike city identifier.
            house_code: The unique identifier for the property listing.
        """
        return self._get(
            "/api/beike/ershoufang/detail/v1",
            {
                "cityId": city_id,
                "houseCode": house_code,
            },
        )

    def get_ershoufang_list_v1(
        self,
        *,
        city_id: str,
        condition: str | None = "",
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Resale Housing List

        Retrieves Beike resale-housing listings for a city with optional condition filters and offset pagination. Use it to browse second-hand properties in a selected market.

        Args:
            city_id: The numeric Beike city identifier.
            condition: Filter conditions (e.g., region, price range, layout).
            offset: Pagination offset, starting from 0 (e.g., 0, 20, 40...).
        """
        return self._get(
            "/api/beike/get-ershoufang-list/v1",
            {
                "cityId": city_id,
                "condition": condition,
                "offset": offset,
            },
        )

    def community_list_v1(
        self,
        *,
        city_id: str,
        condition: str | None = "",
        limit_offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Community List

        Retrieves Beike residential communities for a city with optional condition filters and offset pagination. Use it to browse housing communities in a selected city.

        Args:
            city_id: The numeric Beike city identifier.
            condition: Filter conditions for communities.
            limit_offset: Pagination offset, starting from 0 (e.g., 0, 20, 40...).
        """
        return self._get(
            "/api/beike/community/list/v1",
            {
                "cityId": city_id,
                "condition": condition,
                "limitOffset": limit_offset,
            },
        )
