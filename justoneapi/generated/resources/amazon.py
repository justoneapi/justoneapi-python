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
        Product Details (V1)

        Retrieves detailed product information from Amazon based on the provided ASIN.
        It returns core product data such as title, brand, price, availability, rating,
        review count, product images, category information, and other publicly available details.

        Typical use cases:
        - Building product catalogs and enriching item content (e.g., images)
        - Price monitoring and availability tracking
        - E-commerce analytics and competitor tracking

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
        Product Top Reviews (V1)

        Retrieves top (most relevant or most helpful) public reviews for an Amazon product based on the provided ASIN.
        It returns review details such as review ID, reviewer name, rating score,
        review title, review content, publish time, and helpful vote count (if available).

        Typical use cases:
        - Sentiment analysis and consumer feedback tracking
        - Product research and quality assessment
        - Monitoring competitor customer experience

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
        Best Sellers (V1)

        Retrieves top performing products for a given category on Amazon.
        Supports top level best sellers categories (e.g. software). In addition, subcategories / category path can be specified.

        Typical use cases:
        - Identifying trending products in specific categories
        - Market share analysis and category research
        - Tracking sales rank and popularity over time

        Args:
            category: Best sellers category to return products for (e.g. 'software' or 'software/229535').
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

    def get_products_by_category_v1(
        self,
        *,
        category_id: str,
        country: str | None = "US",
        sort_by: str | None = "RELEVANCE",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Products By Category (V1)

        Retrieves products under a specified Amazon category.
            Supports category-based product discovery and returns product information such as title, price, rating, review count, and other available marketplace fields.

            Typical use cases:
            - Discovering products within a specific category
            - Category research and competitor analysis
            - Monitoring product assortment, pricing, and popularity trends

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
