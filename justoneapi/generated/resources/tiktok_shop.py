from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TiktokShopResource(BaseResource):
    """Generated resource for TikTok Shop APIs."""

    def search_products_v1(
        self,
        *,
        keyword: str,
        region: str | None = "US",
        offset: int | None = 0,
        page_token: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Search Products (V1)

        Searches for products on TikTok Shop based on the provided keyword and region.
        It returns a list of products including title, price, sales, and other metadata.

        Typical use cases:
        - Market research and trend analysis
        - Competitor product discovery
        - Monitoring product popularity in specific regions

        Args:
            keyword: Search keyword.
            region: Target region for product search.  Available Values: - `US`: United States - `GB`: United Kingdom - `SG`: Singapore - `MY`: Malaysia - `PH`: Philippines - `TH`: Thailand - `VN`: Vietnam - `ID`: Indonesia
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
        Product Detail (V1)

        Retrieves detailed information for a specific product on TikTok Shop based on the provided product ID and region.
        It returns comprehensive product data including title, description, price, stock, and media.

        Typical use cases:
        - Building product catalogs
        - Price and stock monitoring
        - In-depth product analysis

        Args:
            product_id: TikTok Shop Product ID.
            region: Target region for product detail.  Available Values: - `US`: United States - `GB`: United Kingdom - `SG`: Singapore - `MY`: Malaysia - `PH`: Philippines - `TH`: Thailand - `VN`: Vietnam - `ID`: Indonesia
        """
        return self._get(
            "/api/tiktok-shop/get-product-detail/v1",
            {
                "productId": product_id,
                "region": region,
            },
        )
