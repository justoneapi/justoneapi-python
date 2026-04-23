from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class AmazonResource(BaseResource):
    """Generated resource for Amazon."""

    def get_product_detail_v1(
        self,
        *,
        asin: str,
        country: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Details

        Get Amazon product Details data, including title, brand, and price, for building product catalogs and enriching item content (e.g., images), price monitoring and availability tracking, and e-commerce analytics and competitor tracking.

        Args:
            asin: ASIN (Amazon Standard Identification Number).
            country: Country code for the Amazon product.  Available Values: - `US`: United States - `AU`: Australia - `BR`: Brazil - `CA`: Canada - `CN`: China - `FR`: France - `DE`: Germany - `IN`: India - `IT`: Italy - `MX`: Mexico - `NL`: Netherlands - `SG`: Singapore - `ES`: Spain - `TR`: Turkey - `AE`: United Arab Emirates - `GB`: United Kingdom - `JP`: Japan - `SA`: Saudi Arabia - `PL`: Poland - `SE`: Sweden - `BE`: Belgium - `EG`: Egypt - `ZA`: South Africa - `IE`: Ireland
        """
        return self._get(
            "/api/amazon/get-product-detail/v1",
            {
                "asin": asin,
                "country": country,
            },
        )

    def get_product_top_reviews_v1(
        self,
        *,
        asin: str,
        country: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Top Reviews

        Get Amazon product Top Reviews data, including most helpful) public reviews, for sentiment analysis and consumer feedback tracking, product research and quality assessment, and monitoring competitor customer experience.

        Args:
            asin: ASIN (Amazon Standard Identification Number).
            country: Country code for the Amazon product.  Available Values: - `US`: United States - `AU`: Australia - `BR`: Brazil - `CA`: Canada - `CN`: China - `FR`: France - `DE`: Germany - `IN`: India - `IT`: Italy - `MX`: Mexico - `NL`: Netherlands - `SG`: Singapore - `ES`: Spain - `TR`: Turkey - `AE`: United Arab Emirates - `GB`: United Kingdom - `JP`: Japan - `SA`: Saudi Arabia - `PL`: Poland - `SE`: Sweden - `BE`: Belgium - `EG`: Egypt - `ZA`: South Africa - `IE`: Ireland
        """
        return self._get(
            "/api/amazon/get-product-top-reviews/v1",
            {
                "asin": asin,
                "country": country,
            },
        )

    def get_best_sellers_v1(
        self,
        *,
        category: str,
        country: str | None = "US",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Best Sellers

        Get Amazon best Sellers data, including rank positions, product metadata, and pricing, for identifying trending products in specific categories, market share analysis and category research, and tracking sales rank and popularity over time.

        Args:
            category: Best sellers category to return products for (e.g. 'baby-products' or 'baby-products/166777011'). The value is derived from the URL path of the Amazon Best Sellers page, such as: https://www.amazon.com/Best-Sellers-Baby-Baby-Toddler-Feeding-Supplies/zgbs/baby-products/166777011
            country: Country code for the Amazon product.  Available Values: - `US`: United States - `AU`: Australia - `BR`: Brazil - `CA`: Canada - `CN`: China - `FR`: France - `DE`: Germany - `IN`: India - `IT`: Italy - `MX`: Mexico - `NL`: Netherlands - `SG`: Singapore - `ES`: Spain - `TR`: Turkey - `AE`: United Arab Emirates - `GB`: United Kingdom - `JP`: Japan - `SA`: Saudi Arabia - `PL`: Poland - `SE`: Sweden - `BE`: Belgium - `EG`: Egypt - `ZA`: South Africa - `IE`: Ireland
            page: Page number for pagination.
        """
        return self._get(
            "/api/amazon/get-best-sellers/v1",
            {
                "category": category,
                "country": country,
                "page": page,
            },
        )

    def get_category_products_v1(
        self,
        *,
        category_id: str,
        country: str | None = "US",
        sort_by: str | None = "RELEVANCE",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Products By Category

        Get Amazon products By Category data, including title, price, and rating, for category-based product discovery and returns product information such as title, price, and rating.

        Args:
            category_id: For example: https://amazon.com/s?node=172282 - the Amazon Category ID is 172282
            country: Country code for the Amazon product.  Available Values: - `US`: United States - `AU`: Australia - `BR`: Brazil - `CA`: Canada - `CN`: China - `FR`: France - `DE`: Germany - `IN`: India - `IT`: Italy - `MX`: Mexico - `NL`: Netherlands - `SG`: Singapore - `ES`: Spain - `TR`: Turkey - `AE`: United Arab Emirates - `GB`: United Kingdom - `JP`: Japan - `SA`: Saudi Arabia - `PL`: Poland - `SE`: Sweden - `BE`: Belgium - `EG`: Egypt - `ZA`: South Africa - `IE`: Ireland
            sort_by: Sort by.  Available Values: - `RELEVANCE`: Relevance - `LOWEST_PRICE`: Lowest Price - `HIGHEST_PRICE`: Highest Price - `REVIEWS`: Reviews - `NEWEST`: Newest - `BEST_SELLERS`: Best Sellers
            page: Page number for pagination.
        """
        return self._get(
            "/api/amazon/get-category-products/v1",
            {
                "categoryId": category_id,
                "country": country,
                "sortBy": sort_by,
                "page": page,
            },
        )
