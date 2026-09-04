from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class AliexpressResource(BaseResource):
    """Generated resource for AliExpress."""

    def search_products_v1(
        self,
        *,
        q: str | None = None,
        page: str | None = None,
        sort: str | None = "default",
        cat_id: str | None = None,
        brand_id: str | None = None,
        loc: str | None = None,
        switches: str | None = None,
        attr: str | None = None,
        start_price: float | None = None,
        end_price: float | None = None,
        locale: str | None = None,
        region: str | None = None,
        currency: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches AliExpress products with optional query, page, sort, category, brand, location, attribute, price, locale, region, and currency controls. Use it for product discovery, catalog research, and marketplace assortment analysis.

        Args:
            q: Product search query.
            page: One-based page number for pagination.
            sort: Sort order for product search results.  Available Values: - `DEFAULT`: Default result order - `SALES_DESC`: Sales volume, highest first - `PRICE_ASC`: Price, lowest first - `PRICE_DESC`: Price, highest first
            cat_id: Category ID used to filter product search results.
            brand_id: Brand ID used to filter product search results.
            loc: Location filter for product search results.
            switches: Search switches used to select optional result features.
            attr: Product attribute filter for search results.
            start_price: Minimum product price filter, inclusive.
            end_price: Maximum product price filter, inclusive.
            locale: Locale used for the AliExpress response.
            region: AliExpress marketplace region.
            currency: Currency code used for product prices.
        """
        return self._get(
            "/api/aliexpress/search-products/v1",
            {
                "q": q,
                "page": page,
                "sort": sort,
                "catId": cat_id,
                "brandId": brand_id,
                "loc": loc,
                "switches": switches,
                "attr": attr,
                "startPrice": start_price,
                "endPrice": end_price,
                "locale": locale,
                "region": region,
                "currency": currency,
            },
        )

    def get_product_detail_v1(
        self,
        *,
        item_id: str,
        currency: str | None = None,
        region: str | None = None,
        locale: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves an AliExpress product by item ID with optional currency, region, and locale controls. Use it to inspect a known listing for catalog review, product comparison, or downstream commerce analysis.

        Args:
            item_id: Numeric AliExpress item ID.
            currency: Currency code used for product prices.
            region: AliExpress marketplace region.
            locale: Locale used for the AliExpress response.
        """
        return self._get(
            "/api/aliexpress/get-product-detail/v1",
            {
                "itemId": item_id,
                "currency": currency,
                "region": region,
                "locale": locale,
            },
        )
