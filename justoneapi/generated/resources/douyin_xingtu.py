from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinXingtuResource(BaseResource):
    """Generated resource for Douyin Xingtu APIs."""

    def gw_api_author_get_author_base_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Base Info (V1)

        Retrieve basic information for a specific author.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/author/get_author_base_info/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_author_link_struct_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Link Struct (V1)

        Get structure of author links.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_link_struct/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_check_author_display_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Check Author Display (V1)

        Check visibility status of an author.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/check_author_display/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_author_get_author_platform_channel_info_v2_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Platform Channel Info (V1)

        Retrieve author's platform channel data.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/author/get_author_platform_channel_info_v2/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_aggregator_get_author_order_experience_v1(
        self,
        *,
        o_author_id: str,
        period: str | None = "DAY_30",
    ) -> ApiResponse[Any]:
        """
        Author Order Experience (V1)

        Get author's transaction experience summary.

        Args:
            o_author_id: Author's unique ID.
            period: Time period.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_order_experience/v1",
            {
                "oAuthorId": o_author_id,
                "period": period,
            },
        )

    def gw_api_data_sp_get_author_link_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        industry_tag: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Author Link Info (V1)

        Get author's link index and stats.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            industry_tag: Industry tag.  Available Values: - `ALL`: All - `ELECTRONICS_AND_APPLIANCES`: Electronics and Appliances - `FOOD_AND_BEVERAGE`: Food and Beverage - `CLOTHING_AND_ACCESSORIES`: Clothing and Accessories - `HEALTHCARE_AND_MEDICAL`: Healthcare and Medical - `BUSINESS_SERVICES`: Business Services - `LOCAL_SERVICES`: Local Services - `REAL_ESTATE`: Real Estate - `HOME_AND_BUILDING_MATERIALS`: Home and Building Materials - `EDUCATION_AND_TRAINING`: Education and Training - `TRAVEL_AND_TOURISM`: Travel and Tourism - `PUBLIC_SERVICES`: Public Services - `GAMES`: Games - `RETAIL`: Retail - `TRANSPORTATION_EQUIPMENT`: Transportation Equipment - `AUTOMOTIVE`: Automotive - `AGRICULTURE_FORESTRY_FISHERY`: Agriculture Forestry Fishery - `CHEMICAL_AND_ENERGY`: Chemical and Energy - `ELECTRONICS_AND_ELECTRICAL`: Electronics and Electrical - `MACHINERY_EQUIPMENT`: Machinery Equipment - `CULTURE_SPORTS_ENTERTAINMENT`: Culture Sports Entertainment - `MEDIA_AND_INFORMATION`: Media and Information - `LOGISTICS`: Logistics - `TELECOMMUNICATIONS`: Telecommunications - `FINANCIAL_SERVICES`: Financial Services - `CATERING_SERVICES`: Catering Services - `SOFTWARE_TOOLS`: Software Tools - `FRANCHISING_AND_INVESTMENT`: Franchising and Investment - `BEAUTY_AND_COSMETICS`: Beauty and Cosmetics - `MOTHER_BABY_AND_PET`: Mother Baby and Pet - `DAILY_CHEMICALS`: Daily Chemicals - `PHYSICAL_BOOKS`: Physical Books - `SOCIAL_AND_COMMUNICATION`: Social and Communication - `MEDICAL_INSTITUTIONS`: Medical Institutions
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_link_info/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "industryTag": industry_tag,
            },
        )

    def gw_api_data_sp_author_video_distribution_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Video Distribution (V1)

        Get author's video performance distribution.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_video_distribution/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_author_audience_distribution_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        link_type: str | None = "CONNECTED",
    ) -> ApiResponse[Any]:
        """
        Author Audience Distribution (V1)

        Get author's audience demographics.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            link_type: Link type filter.  Available Values: - `CONNECTED`: Connected - `AWARE`: Aware - `INTERESTED`: Interested - `LIKE`: Like - `FOLLOW`: Follow
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_audience_distribution/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "linkType": link_type,
            },
        )

    def gw_api_author_get_author_marketing_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Marketing Info (V1)

        Get author's marketing pricing and stats.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/author/get_author_marketing_info/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_get_author_spread_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        range: str | None = "DAY_30",
        type: str | None = "PERSONAL_VIDEO",
        only_assign: bool | None = False,
        flow_type: str | None = "EXCLUDE",
    ) -> ApiResponse[Any]:
        """
        Author Spread Info (V1)

        Get author's spread performance metrics.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            range: Time range.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            type: Video type.  Available Values: - `PERSONAL_VIDEO`: Personal video - `XINTU_VIDEO`: Xingtu video
            only_assign: Whether to only include assigned videos.
            flow_type: Flow type filter.  Available Values: - `EXCLUDE`: Exclude - `INCLUDE`: Include
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_spread_info/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "range": range,
                "type": type,
                "onlyAssign": only_assign,
                "flowType": flow_type,
            },
        )

    def gw_api_data_sp_get_author_convert_ability_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        range: str | None = "DAY_30",
    ) -> ApiResponse[Any]:
        """
        Author Convert Ability (V1)

        Get author's conversion capability analysis.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            range: Time range.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_convert_ability/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "range": range,
            },
        )

    def gw_api_author_get_author_show_items_v2_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        only_assign: bool | None = False,
        flow_type: str | None = "EXCLUDE",
    ) -> ApiResponse[Any]:
        """
        Author Show Items (V1)

        Get author's showcased items or videos.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            only_assign: Whether to only include assigned items.
            flow_type: Flow type filter.  Available Values: - `EXCLUDE`: Exclude - `INCLUDE`: Include
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/author/get_author_show_items_v2/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "onlyAssign": only_assign,
                "flowType": flow_type,
            },
        )

    def gw_api_data_sp_get_author_convert_videos_or_products_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
        industry_id: str | None = "ALL",
        range: str | None = "DAY_30",
        detail_type: str | None = "VIDEO",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Author Convert Videos or Products (V1)

        Get detailed conversion data for videos or products.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            industry_id: Industry category.  Available Values: - `ALL`: All - `ELECTRONICS_AND_APPLIANCES`: Electronics and Appliances - `FOOD_AND_BEVERAGE`: Food and Beverage - `CLOTHING_AND_ACCESSORIES`: Clothing and Accessories - `HEALTHCARE_AND_MEDICAL`: Healthcare and Medical - `BUSINESS_SERVICES`: Business Services - `LOCAL_SERVICES`: Local Services - `REAL_ESTATE`: Real Estate - `HOME_AND_BUILDING_MATERIALS`: Home and Building Materials - `EDUCATION_AND_TRAINING`: Education and Training - `TRAVEL_AND_TOURISM`: Travel and Tourism - `PUBLIC_SERVICES`: Public Services - `GAMES`: Games - `RETAIL`: Retail - `TRANSPORTATION_EQUIPMENT`: Transportation Equipment - `AUTOMOTIVE`: Automotive - `AGRICULTURE_FORESTRY_FISHERY`: Agriculture Forestry Fishery - `CHEMICAL_AND_ENERGY`: Chemical and Energy - `ELECTRONICS_AND_ELECTRICAL`: Electronics and Electrical - `MACHINERY_EQUIPMENT`: Machinery Equipment - `CULTURE_SPORTS_ENTERTAINMENT`: Culture Sports Entertainment - `MEDIA_AND_INFORMATION`: Media and Information - `LOGISTICS`: Logistics - `TELECOMMUNICATIONS`: Telecommunications - `FINANCIAL_SERVICES`: Financial Services - `CATERING_SERVICES`: Catering Services - `SOFTWARE_TOOLS`: Software Tools - `FRANCHISING_AND_INVESTMENT`: Franchising and Investment - `BEAUTY_AND_COSMETICS`: Beauty and Cosmetics - `MOTHER_BABY_AND_PET`: Mother Baby and Pet - `DAILY_CHEMICALS`: Daily Chemicals - `PHYSICAL_BOOKS`: Physical Books - `SOCIAL_AND_COMMUNICATION`: Social and Communication - `MEDICAL_INSTITUTIONS`: Medical Institutions
            range: Time range.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            detail_type: Resource type.  Available Values: - `VIDEO`: Video - `PRODUCT`: Product
            page: Page number.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_convert_videos_or_products/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
                "industryId": industry_id,
                "range": range,
                "detailType": detail_type,
                "page": page,
            },
        )

    def gw_api_data_sp_author_cp_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author CP Info (V1)

        Get author's cost-performance analysis.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_cp_info/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_author_touch_distribution_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Touch Distribution (V1)

        Get author's user touchpoints and distribution.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_touch_distribution/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_author_rec_videos_v2_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Author Recommended Videos (V1)

        Get author's high-performance recommended videos.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/author_rec_videos_v2/v1",
            {
                "oAuthorId": o_author_id,
                "platform": platform,
            },
        )

    def gw_api_data_sp_get_author_fans_distribution_v1(
        self,
        *,
        o_author_id: str,
        author_type: str | None = "FAN",
    ) -> ApiResponse[Any]:
        """
        Author Fans Distribution (V1)

        Get author's fans demographics and distribution.

        Args:
            o_author_id: Author's unique ID.
            author_type: Author type filter.  Available Values: - `FAN`: Fan - `DIE_HARD_FAN`: Die Hard Fan
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_fans_distribution/v1",
            {
                "oAuthorId": o_author_id,
                "authorType": author_type,
            },
        )

    def gw_api_gsearch_search_for_author_square_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
        search_type: str | None = "NICKNAME",
        follower_range: str | None = None,
        kol_price_type: str | None = None,
        kol_price_range: str | None = None,
        content_tag: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Author Search (V1)

        Search for authors using filters.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            search_type: Search criteria type.  Available Values: - `NICKNAME`: By Nickname - `CONTENT`: By Content
            follower_range: Follower range (e.g., 10-100).
            kol_price_type: KOL price type.  Available Values: - `视频1_20s`: Video 1-20s - `视频21_60s`: Video 21-60s - `视频60s以上`: Video > 60s - `定制短剧单集`: Mini-drama episode - `千次自然播放量`: CPM naturally - `短直种草视频`: Short-live seeding video - `短直预热视频`: Short-live warm-up video - `短直明星种草`: Celebrity short-live seeding - `短直明星预热`: Celebrity short-live warm-up - `明星视频`: Celebrity video - `合集视频`: Collection video - `抖音短视频共创_主投稿达人`: Douyin short video co-creation - main creator - `抖音短视频共创_参与达人`: Douyin short video co-creation - participant
            kol_price_range: KOL price range (e.g., 10000-50000).
            content_tag: Content tag filter.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/gsearch/search_for_author_square/v1",
            {
                "keyword": keyword,
                "page": page,
                "searchType": search_type,
                "followerRange": follower_range,
                "kolPriceType": kol_price_type,
                "kolPriceRange": kol_price_range,
                "contentTag": content_tag,
            },
        )

    def gw_api_data_sp_item_report_trend_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Report Trend (V1)

        Get trend analysis for an item report.

        Args:
            item_id: Item's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/item_report_trend/v1",
            {
                "itemId": item_id,
            },
        )

    def gw_api_data_sp_item_report_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Report Details (V1)

        Get detailed item report data.

        Args:
            item_id: Item's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/item_report_detail/v1",
            {
                "itemId": item_id,
            },
        )

    def gw_api_data_sp_item_report_th_analysis_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Report Analysis (V1)

        Get analytical insights for an item report.

        Args:
            item_id: Item's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/item_report_th_analysis/v1",
            {
                "itemId": item_id,
            },
        )

    def get_kol_info_v1(
        self,
        *,
        kol_id: str,
        platform_channel: str | None = "_1",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Profile (V1) [Deprecated]

        Retrieve KOL profile information (Legacy).

        Args:
            kol_id: KOL ID.
            platform_channel: Platform channel.  Available Values: - `_1`: Short Video - `_10`: Live Streaming
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-info/v1",
            {
                "kolId": kol_id,
                "platformChannel": platform_channel,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_audience_distribution_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Audience Profile (V1) [Deprecated]

        Get fans audience distribution (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-audience-distribution/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_fans_distribution_v1(
        self,
        *,
        kol_id: str,
        fans_type: str | None = "_1",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Follower Profile (V1) [Deprecated]

        Get fans portrait (Legacy).

        Args:
            kol_id: KOL ID.
            fans_type: Fans type.  Available Values: - `_1`: Fans Portrait - `_2`: Fans Group Portrait - `_5`: Iron Fans Portrait
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-fans-distribution/v1",
            {
                "kolId": kol_id,
                "fansType": fans_type,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_marketing_info_v1(
        self,
        *,
        kol_id: str,
        platform_channel: str | None = "_1",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Service Pricing (V1) [Deprecated]

        Get marketing pricing info (Legacy).

        Args:
            kol_id: KOL ID.
            platform_channel: Platform channel.  Available Values: - `_1`: Short Video - `_10`: Live Streaming
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-marketing-info/v1",
            {
                "kolId": kol_id,
                "platformChannel": platform_channel,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_spread_info_v1(
        self,
        *,
        kol_id: str,
        type: str | None = "_1",
        range: str | None = "_2",
        flow_type: str | None = "1",
        only_assign: bool | None = False,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Data Overview (V1) [Deprecated]

        Get spread performance metrics (Legacy).

        Args:
            kol_id: KOL ID.
            type: Spread info type.  Available Values: - `_1`: Personal Video - `_2`: Xingtu Video
            range: Time range.  Available Values: - `_2`: Last 30 days - `_3`: Last 90 days
            flow_type: Flow type.
            only_assign: Only assigned notes.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-spread-info/v1",
            {
                "kolId": kol_id,
                "type": type,
                "range": range,
                "flowType": flow_type,
                "onlyAssign": only_assign,
                "acceptCache": accept_cache,
            },
        )

    def search_douyin_kol_v1(
        self,
        *,
        body: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Douyin KOL Search (V1) [Deprecated]

        Search for Douyin KOLs (Legacy JSON body).

        Args:
            body: JSON request body.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/search-douyin-kol/v1",
            {
                "body": body,
                "acceptCache": accept_cache,
            },
        )

    def search_kol_simple_v1(
        self,
        *,
        keyword: str,
        platform_source: str,
        page: int,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Keyword Search (V1)

        Simple keyword-based KOL search.

        Args:
            keyword: Search keywords.
            platform_source: Platform source.  Available Values: - `_1`: Douyin - `_2`: Toutiao - `_3`: Xigua
            page: Page number.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/search-kol-simple/v1",
            {
                "keyword": keyword,
                "platformSource": platform_source,
                "page": page,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_convert_ability_v1(
        self,
        *,
        kol_id: str,
        range: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Conversion Analysis (V1) [Deprecated]

        Get conversion capability analysis (Legacy).

        Args:
            kol_id: KOL ID.
            range: Time range.  Available Values: - `_1`: Last 7 days - `_2`: Last 30 days - `_3`: Last 90 days
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-convert-ability/v1",
            {
                "kolId": kol_id,
                "range": range,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_show_items_v2_v1(
        self,
        *,
        kol_id: str,
        only_assign: bool | None = False,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Video Performance (V1) [Deprecated]

        Get showcased items or videos performance (Legacy).

        Args:
            kol_id: KOL ID.
            only_assign: Whether true is Xingtu video, false is personal video.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-show-items-v2/v1",
            {
                "kolId": kol_id,
                "onlyAssign": only_assign,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_link_info_v1(
        self,
        *,
        kol_id: str,
        industry_tag: str | None = "",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Xingtu Index (V1) [Deprecated]

        Get author link index (Legacy).

        Args:
            kol_id: KOL ID.
            industry_tag: Industry Tag.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-link-info/v1",
            {
                "kolId": kol_id,
                "industryTag": industry_tag,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_convert_videos_or_products_v1(
        self,
        *,
        kol_id: str,
        detail_type: str,
        page: int,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Conversion Video Display (V1) [Deprecated]

        Get detailed conversion resource list (Legacy).

        Args:
            kol_id: KOL ID.
            detail_type: Resource type.  Available Values: - `_1`: Video Data - `_2`: Product Data
            page: Page number.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-convert-videos-or-products/v1",
            {
                "kolId": kol_id,
                "detailType": detail_type,
                "page": page,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_link_struct_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Link Struct (V1) [Deprecated]

        Get author link structure (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-link-struct/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_touch_distribution_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Connected User Sources (V1) [Deprecated]

        Get connected user source distribution (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-touch-distribution/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_cp_info_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Cost-Effectiveness Analysis (V1) [Deprecated]

        Get cost-effectiveness analysis data (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-cp-info/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_rec_videos_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Content Performance (V1) [Deprecated]

        Get author content and video performance (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-rec-videos/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def search_for_author_square_v3(
        self,
        *,
        page: int,
        fans_low: int,
        fans_high: int,
    ) -> ApiResponse[Any]:
        """
        Creator List Search (V3) [Deprecated]

        Search for creators by fans range (Legacy).

        Args:
            page: Page number.
            fans_low: Minimum fans count.
            fans_high: Maximum fans count.
        """
        return self._get(
            "/api/douyin-xingtu/search-for-author-square/v3",
            {
                "page": page,
                "fansLow": fans_low,
                "fansHigh": fans_high,
            },
        )

    def get_kol_daily_fans_v1(
        self,
        *,
        kol_id: str,
        start_date: str,
        end_date: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Follower Trend (V1)

        Get author's historical daily fans growth trend.

        Args:
            kol_id: KOL ID.
            start_date: Start Date (yyyy-MM-dd).
            end_date: End Date (yyyy-MM-dd).
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-kol-daily-fans/v1",
            {
                "kolId": kol_id,
                "startDate": start_date,
                "endDate": end_date,
                "acceptCache": accept_cache,
            },
        )

    def get_author_hot_comment_tokens_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Comment Keyword Analysis (V1)

        Get analytical tokens from author's top comments.

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-author-hot-comment-tokens/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_author_content_hot_keywords_v1(
        self,
        *,
        kol_id: str,
        keyword_type: str | None = "0",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Content Keyword Analysis (V1)

        Get analytical keywords from author's content.

        Args:
            kol_id: KOL ID.
            keyword_type: Type of keywords.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-author-content-hot-keywords/v1",
            {
                "kolId": kol_id,
                "keywordType": keyword_type,
                "acceptCache": accept_cache,
            },
        )

    def get_author_commerce_spread_info_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Author Commerce Spread Info (V1)

        Get author's commercial spread metrics.

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-author-commerce-spread-info/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_author_commerce_seeding_base_info_v1(
        self,
        *,
        kol_id: str,
        range: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Author Commerce Seeding Base Info (V1)

        Get author's commercial seeding data.

        Args:
            kol_id: KOL ID.
            range: Time range.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-author-commerce-seed-base-info/v1",
            {
                "kolId": kol_id,
                "range": range,
                "acceptCache": accept_cache,
            },
        )

    def get_video_detail_v1(
        self,
        *,
        detail_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Video Details (V1) [Deprecated]

        Get detailed video data (Legacy).

        Args:
            detail_id: Video detail ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/douyin-xingtu/get-video-detail/v1",
            {
                "detailId": detail_id,
                "acceptCache": accept_cache,
            },
        )
