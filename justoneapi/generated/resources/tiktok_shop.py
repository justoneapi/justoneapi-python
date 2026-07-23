from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TiktokShopResource(BaseResource):
    """Generated resource for TikTok Shop."""

    def search_products_v1(
        self,
        *,
        keyword: str,
        region: str | None = "US",
        offset: int | None = 0,
        page_token: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches TikTok Shop products by keyword within a selected region, with offset and page-token pagination. Use it to discover regional products and continue through search results.

        Args:
            keyword: Search keyword.
            region: Target region for product search.  Available Values: - `US`: United States - `GB`: United Kingdom - `FR`: France - `SG`: Singapore - `MY`: Malaysia - `PH`: Philippines - `TH`: Thailand - `VN`: Vietnam - `ID`: Indonesia
            offset: Search result offset.
            page_token: Pagination token for the next page.
        """
        return self._get(
            "/api/tiktok-shop/search-products/v1",
            {
                "keyword": keyword,
                "region": region,
                "offset": offset,
                "pageToken": page_token,
            },
        )

    def get_product_detail_v1(
        self,
        *,
        product_id: str,
        region: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves the public TikTok Shop product detail for a product ID in a selected region. Use it to inspect a known regional product after search or catalog discovery.

        Args:
            product_id: TikTok Shop Product ID.
            region: Target region for product detail.  Available Values: - `US`: United States - `GB`: United Kingdom - `FR`: France - `SG`: Singapore - `MY`: Malaysia - `PH`: Philippines - `TH`: Thailand - `VN`: Vietnam - `ID`: Indonesia
        """
        return self._get(
            "/api/tiktok-shop/get-product-detail/v1",
            {
                "productId": product_id,
                "region": region,
            },
        )
