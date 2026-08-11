from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ShopeeResource(BaseResource):
    """Generated resource for Shopee."""

    def get_item_detail_v1(
        self,
        *,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Details

        Retrieves Shopee item details by marketplace site and item ID.

        Args:
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-detail/v1",
            {
                "itemId": item_id,
                "site": site,
            },
        )

    def get_shop_seo_v1(
        self,
        *,
        shop_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Shop Profile and Rating Summary

        Retrieves a Shopee shop profile and rating summary by marketplace site and shop ID.

        Args:
            shop_id: Shopee shop ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-shop-seo/v1",
            {
                "shopId": shop_id,
                "site": site,
            },
        )

    def get_item_detail_v2(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Details

        Retrieves Shopee item details by marketplace site, shop ID, and item ID using the version 2 data source.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-detail/v2",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
            },
        )

    def get_shop_item_list_v1(
        self,
        *,
        username: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Shop Item List

        Retrieves Shopee item cards for a shop username in the selected marketplace site.

        Args:
            username: Shopee shop username.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-shop-item-list/v1",
            {
                "username": username,
                "site": site,
            },
        )

    def get_item_sku_matrix_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item SKU Matrix

        Retrieves the SKU option matrix for a Shopee item in the selected marketplace site.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-sku-matrix/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
            },
        )

    def get_shop_base_v1(
        self,
        *,
        username: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Shop Basic Profile

        Retrieves the basic Shopee shop profile by username and marketplace site.

        Args:
            username: Shopee shop username.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-shop-base/v1",
            {
                "username": username,
                "site": site,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Search

        Searches Shopee items by keyword in the selected marketplace site.

        Args:
            keyword: Product search keyword.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/search-item-list/v1",
            {
                "keyword": keyword,
                "site": site,
            },
        )

    def get_item_sku_models_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
        offset: str | None = None,
        rating_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Item SKU Models

        Retrieves observed SKU models for a Shopee item with offset and rating filters.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            offset: Zero-based result offset.
            rating_type: Rating filter from 0 to 5, where 0 includes all ratings.
        """
        return self._get(
            "/api/shopee/get-item-sku-models/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
                "offset": offset,
                "ratingType": rating_type,
            },
        )

    def get_shop_detail_v1(
        self,
        *,
        username: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Shop Details

        Retrieves detailed Shopee shop information by username and marketplace site.

        Args:
            username: Shopee shop username.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-shop-detail/v1",
            {
                "username": username,
                "site": site,
            },
        )

    def get_shop_reviews_rich_v1(
        self,
        *,
        shop_id: int,
        site: str | None = "TW",
        offset: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Rich Shop Reviews

        Retrieves enriched Shopee shop reviews using a zero-based result offset.

        Args:
            shop_id: Shopee shop ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            offset: Zero-based result offset.
        """
        return self._get(
            "/api/shopee/get-shop-reviews-rich/v1",
            {
                "shopId": shop_id,
                "site": site,
                "offset": offset,
            },
        )

    def get_item_snapshot_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Display Snapshot

        Retrieves a display snapshot for a Shopee item in the selected marketplace site.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-snapshot/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
            },
        )

    def get_shop_reviews_v1(
        self,
        *,
        shop_id: int,
        site: str | None = "TW",
        offset: str | None = None,
        rating_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Reviews

        Retrieves Shopee shop reviews with offset pagination and a rating filter.

        Args:
            shop_id: Shopee shop ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            offset: Zero-based result offset.
            rating_type: Rating filter from 0 to 5, where 0 includes all ratings.
        """
        return self._get(
            "/api/shopee/get-shop-reviews/v1",
            {
                "shopId": shop_id,
                "site": site,
                "offset": offset,
                "ratingType": rating_type,
            },
        )

    def get_item_reviews_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
        offset: str | None = None,
        rating_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Item Reviews

        Retrieves reviews for a specified Shopee item with offset pagination and a rating filter.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            offset: Zero-based result offset.
            rating_type: Rating filter from 0 to 5, where 0 includes all ratings.
        """
        return self._get(
            "/api/shopee/get-item-reviews/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
                "offset": offset,
                "ratingType": rating_type,
            },
        )

    def get_search_prefills_v1(
        self,
        *,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Search Prefills

        Retrieves Shopee search prefill suggestions for the selected marketplace site.

        Args:
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-search-prefills/v1",
            {
                "site": site,
            },
        )

    def get_search_filters_v1(
        self,
        *,
        keyword: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Search Filter Configuration

        Retrieves available Shopee search filters for a keyword in the selected marketplace site.

        Args:
            keyword: Product search keyword.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-search-filters/v1",
            {
                "keyword": keyword,
                "site": site,
            },
        )

    def get_shop_categories_v1(
        self,
        *,
        shop_id: int,
        site: str | None = "TW",
        offset: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Categories

        Retrieves Shopee shop categories using a zero-based result offset.

        Args:
            shop_id: Shopee shop ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            offset: Zero-based result offset.
        """
        return self._get(
            "/api/shopee/get-shop-categories/v1",
            {
                "shopId": shop_id,
                "site": site,
                "offset": offset,
            },
        )

    def get_item_review_models_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Review Model Distribution

        Retrieves the review distribution across SKU models for a Shopee item.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-review-models/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
            },
        )

    def get_item_review_tags_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Item Review Tags

        Retrieves review tags for a Shopee item in the selected marketplace site.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-item-review-tags/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
            },
        )

    def get_search_facets_v1(
        self,
        *,
        keyword: str,
        site: str | None = "TW",
    ) -> ApiResponse[Any]:
        """
        Search Category Facets

        Retrieves category facets for a Shopee product search keyword.

        Args:
            keyword: Product search keyword.
            site: Shopee marketplace site.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
        """
        return self._get(
            "/api/shopee/get-search-facets/v1",
            {
                "keyword": keyword,
                "site": site,
            },
        )

    def get_item_installments_v1(
        self,
        *,
        shop_id: int,
        item_id: int,
        site: str | None = "TW",
        detail_level: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Item Installments and Amounts

        Retrieves installment and amount information for a Shopee item. This operation supports Taiwan and Indonesia but not Thailand.

        Args:
            shop_id: Shopee shop ID.
            item_id: Shopee item ID.
            site: Shopee marketplace site. Taiwan and Indonesia are supported for this operation.  Available Values: - `TW`: Taiwan - `ID`: Indonesia - `TH`: Thailand
            detail_level: Detail level for the installment response.
        """
        return self._get(
            "/api/shopee/get-item-installments/v1",
            {
                "shopId": shop_id,
                "itemId": item_id,
                "site": site,
                "detailLevel": detail_level,
            },
        )
