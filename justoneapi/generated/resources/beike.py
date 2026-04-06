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

        Get Beike resale Housing Details data, including - Pricing (total and unit price), Physical attributes (area, and layout, for displaying a full property profile to users and detailed price comparison between specific listings.

        Args:
            city_id: The ID of the city (e.g., '110000' for Beijing).
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

        Get Beike resale Housing List data, including - Supports filtering by city/region, price range, and layout, for building search result pages for property portals and aggregating market data for regional housing trends.

        Args:
            city_id: The ID of the city (e.g., '110000' for Beijing).
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

        Get Beike community List data, including - Community name and unique ID and Average listing price and historical price trends, for identifying popular residential areas in a city and comparing average housing prices across different communities.

        Args:
            city_id: The ID of the city (e.g., '110000' for Beijing).
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
