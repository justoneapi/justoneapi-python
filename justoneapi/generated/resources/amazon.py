from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class AmazonResource(BaseResource):
    """Generated resource for Amazon."""

    def search_products_v1(
        self,
        *,
        keyword: str,
        country: str | None = "US",
        sort_by: str | None = "RELEVANCE",
        product_condition: str | None = "ALL",
        is_prime: bool | None = False,
        deals_and_discounts: str | None = "NONE",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls. Use it to discover products for catalog research, price comparison, or competitive assortment analysis.

        Args:
            keyword: Search keyword or ASIN to find Amazon products.
            country: Country code for the Amazon marketplace.  Available Values: - `US`: United States - `AU`: Australia - `BR`: Brazil - `CA`: Canada - `CN`: China - `FR`: France - `DE`: Germany - `IN`: India - `IT`: Italy - `MX`: Mexico - `NL`: Netherlands - `SG`: Singapore - `ES`: Spain - `TR`: Turkey - `AE`: United Arab Emirates - `GB`: United Kingdom - `JP`: Japan - `SA`: Saudi Arabia - `PL`: Poland - `SE`: Sweden - `BE`: Belgium - `EG`: Egypt - `ZA`: South Africa - `IE`: Ireland
            sort_by: Sort order for Amazon product search results.  Available Values: - `RELEVANCE`: Relevance - `LOWEST_PRICE`: Lowest Price - `HIGHEST_PRICE`: Highest Price - `REVIEWS`: Reviews - `NEWEST`: Newest - `BEST_SELLERS`: Best Sellers
            product_condition: Product condition filter for Amazon search results.  Available Values: - `ALL`: All product conditions - `NEW`: New products - `USED`: Used products - `RENEWED`: Renewed products - `COLLECTIBLE`: Collectible products
            is_prime: Whether to return only Prime-eligible products.
            deals_and_discounts: Deals and discounts filter for Amazon search results.  Available Values: - `NONE`: Do not filter by deals or discounts - `ALL_DISCOUNTS`: Return discounted products - `TODAYS_DEALS`: Return today's deals
            page: Page number for pagination.
        """
        return self._get(
            "/api/amazon/search-products/v1",
            {
                "keyword": keyword,
                "country": country,
                "sortBy": sort_by,
                "productCondition": product_condition,
                "isPrime": is_prime,
                "dealsAndDiscounts": deals_and_discounts,
                "page": page,
            },
        )

    def get_product_detail_v1(
        self,
        *,
        asin: str,
        country: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves details for an Amazon product identified by ASIN in a selected country marketplace. Use it to look up a known listing for catalog review, product comparison, or downstream commerce analysis.

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

        Retrieves the top reviews for an Amazon product identified by ASIN in a selected country marketplace. Use it to review prominent customer feedback for product research, sentiment analysis, or quality assessment.

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

        Retrieves paginated Amazon Best Sellers for a category path in a selected country marketplace. Use it to study category leaders, discover popular products, or compare bestseller pages across marketplaces.

        Args:
            category: Best Sellers category path taken from an Amazon Best Sellers URL. It may be a category slug or a nested category path.
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

        Retrieves paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting. Use it to browse a category, compare assortments, or collect category-specific product candidates.

        Args:
            category_id: Numeric Amazon category node ID taken from the node query parameter of a category URL.
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
