from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class BeikeResource(BaseResource):
    """Generated resource for Beike APIs."""

    def ershoufang_detail_v1(
        self,
        *,
        city_id: str,
        house_code: str,
    ) -> ApiResponse[Any]:
        """
        Resale Housing Details (V1)

        Retrieves comprehensive information for a specific second-hand property listing on Beike (Lianjia).

        The data includes:
        - Pricing (total and unit price).
        - Physical attributes (area, layout, floor, orientation).
        - Listing metadata (tags, listing date).
        - Agent contact information.

        Typical use cases:
        - Displaying a full property profile to users.
        - Detailed price comparison between specific listings.

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
        Resale Housing List (V1)

        Fetches a list of second-hand property listings from Beike (Lianjia) based on specified filters.

        Key features:
        - Supports filtering by city/region, price range, layout, and area.
        - Returns core listing details such as title, total price, unit price, and community info.
        - Provides house codes for fetching full details via the detail API.

        Typical use cases:
        - Building search result pages for property portals.
        - Aggregating market data for regional housing trends.

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
        Community List (V1)

        Retrieves a list of residential communities (Xiaoqu) from Beike (Lianjia) within a specified city.

        The data includes:
        - Community name and unique ID.
        - Average listing price and historical price trends.
        - Build year and architectural details.
        - Geographical coordinates and location information.

        Typical use cases:
        - Identifying popular residential areas in a city.
        - Comparing average housing prices across different communities.
        - Spatial analysis of property development patterns.

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
