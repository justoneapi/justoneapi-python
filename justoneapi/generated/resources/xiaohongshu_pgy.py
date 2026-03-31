from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuPgyResource(BaseResource):
    """Generated resource for Xiaohongshu Pgy."""

    def api_solar_cooperator_user_blogger_user_id_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Blogger (V1)

        Retrieve blogger profile information.

        Args:
            user_id: Blogger's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/cooperator/user/blogger/userId/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_kol_data_v3_data_summary_v1(
        self,
        *,
        user_id: str,
        business: str | None = "DAILY_NOTE",
    ) -> ApiResponse[Any]:
        """
        Data Summary (V1)

        Get summary data for a specific KOL.

        Args:
            user_id: KOL's user ID.
            business: Business type.  Available Values: - `DAILY_NOTE`: Daily notes - `COOPERATE_NOTE`: Cooperative notes
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV3/dataSummary/v1",
            {
                "userId": user_id,
                "business": business,
            },
        )

    def api_solar_kol_data_user_id_fans_overall_new_history_v1(
        self,
        *,
        user_id: str,
        date_type: str | None = "DAY_30",
        increase_type: str | None = "FANS_TOTAL",
    ) -> ApiResponse[Any]:
        """
        Fans Overall New History (V1)

        Retrieve historical fans growth data.

        Args:
            user_id: KOL's user ID.
            date_type: Time range for data.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            increase_type: Type of growth data.  Available Values: - `FANS_TOTAL`: Total fans - `FANS_INCREASE`: New fans increase
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/data/userId/fans_overall_new_history/v1",
            {
                "userId": user_id,
                "dateType": date_type,
                "increaseType": increase_type,
            },
        )

    def api_solar_kol_data_v3_fans_summary_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        Fans Summary (V1)

        Get summary of fans demographics and stats.

        Args:
            user_id: KOL's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV3/fansSummary/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_kol_get_similar_kol_v1(
        self,
        *,
        user_id: str,
        page_num: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Similar KOL (V1)

        Find similar KOLs based on a given user ID.

        Args:
            user_id: KOL's user ID.
            page_num: Page number for results.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/get_similar_kol/v1",
            {
                "userId": user_id,
                "pageNum": page_num,
            },
        )

    def api_solar_kol_data_v2_kol_feature_tags_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        KOL Feature Tags (V1)

        Get feature tags assigned to a KOL.

        Args:
            user_id: KOL's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV2/kolFeatureTags/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_kol_data_v2_kol_content_tags_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        KOL Content Tags (V1)

        Get content-related tags for a KOL.

        Args:
            user_id: KOL's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV2/kolContentTags/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_kol_data_v3_notes_rate_v1(
        self,
        *,
        user_id: str,
        business: str | None = "DAILY_NOTE",
        note_type: str | None = "PHOTO_TEXT_AND_VIDEO",
        date_type: str | None = "DAY_30",
        advertise_switch: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Notes Rate (V1)

        Get performance rates for notes.

        Args:
            user_id: KOL's user ID.
            business: Business type.  Available Values: - `DAILY_NOTE`: Daily notes - `COOPERATE_NOTE`: Cooperative notes
            note_type: Type of note.  Available Values: - `PHOTO_TEXT_AND_VIDEO`: Photo and Video - `PHOTO_TEXT`: Photo and Text - `VIDEO`: Video only
            date_type: Time range for data.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            advertise_switch: Advertisement filter.  Available Values: - `ALL`: All notes - `ORGANIC_ONLY`: Organic notes only
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV3/notesRate/v1",
            {
                "userId": user_id,
                "business": business,
                "noteType": note_type,
                "dateType": date_type,
                "advertiseSwitch": advertise_switch,
            },
        )

    def api_solar_kol_data_v2_notes_detail_v1(
        self,
        *,
        user_id: str,
        advertise_switch: str | None = "ALL",
        order_type: str | None = "LATEST",
        note_type: str | None = "ALL",
        is_third_platform: str | None = "NO",
        page_number: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Published Notes List (V1)

        Retrieves the list of notes published by a specific Xiaohongshu user.
        It returns note items posted by the target account, typically including note IDs, titles/covers (if available), publish-related metadata, and paging information.

        Typical use cases:
        - Creator content monitoring: track a user's recently published notes.
        - Content collection: build datasets of notes under a specific account.
        - Account activity analysis: review posting frequency and content output.

        Highlights
        - Some users may not return note data through this endpoint. In general, users enrolled in Pugongying or users with relatively large follower bases are more likely to be supported.

        Args:
            user_id: KOL's user ID.
            advertise_switch: Advertisement filter.  Available Values: - `ALL`: All notes - `ORGANIC_ONLY`: Organic notes only
            order_type: Sorting order.  Available Values: - `LATEST`: Latest - `MOST_READ`: Most read - `MOST_INTERACT`: Most interactions
            note_type: Type of note.  Available Values: - `ALL`: All types - `COOPERATION`: Cooperation notes - `PHOTO_TEXT`: Photo and Text - `VIDEO`: Video only
            is_third_platform: Whether from third-party platform.  Available Values: - `NO`: No - `YES`: Yes
            page_number: Page number.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV2/notesDetail/v1",
            {
                "userId": user_id,
                "advertiseSwitch": advertise_switch,
                "orderType": order_type,
                "noteType": note_type,
                "isThirdPlatform": is_third_platform,
                "pageNumber": page_number,
            },
        )

    def api_solar_kol_data_user_id_fans_profile_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        Fans Profile (V1)

        Get detailed fans profile for a specific KOL.

        Args:
            user_id: KOL's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/data/userId/fans_profile/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_kol_data_v2_cost_effective_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        Cost Effective (V1)

        Analyze cost-effectiveness of a specific KOL.

        Args:
            user_id: KOL's user ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/kol/dataV2/costEffective/v1",
            {
                "userId": user_id,
            },
        )

    def api_solar_note_note_id_detail_v1(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details (V1)

        Retrieve details for a specific note.

        Args:
            note_id: Note's unique ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/note/noteId/detail/v1",
            {
                "noteId": note_id,
            },
        )

    def api_solar_cooperator_blogger_v2_v1(
        self,
        *,
        search_type: str | None = "NICKNAME",
        keyword: str | None = None,
        page: int | None = 1,
        fans_number_lower: int | None = None,
        fans_number_upper: int | None = None,
        fans_age: str | None = "ALL",
        fans_gender: str | None = "ALL",
        gender: str | None = "ALL",
        content_tag: str | None = None,
    ) -> ApiResponse[Any]:
        """
        KOL Search (V1)

        Search for KOLs using various filters.

        Args:
            search_type: Search criteria type.  Available Values: - `NICKNAME`: Search by nickname - `NOTE`: Search by note content
            keyword: Search keyword.
            page: Page number.
            fans_number_lower: Minimum number of fans.
            fans_number_upper: Maximum number of fans.
            fans_age: Target fans age group.  Available Values: - `ALL`: All ages - `LT_18`: Under 18 - `AGE_18_24`: 18 to 24 - `AGE_25_34`: 25 to 34 - `AGE_35_44`: 35 to 44 - `GT_44`: Above 44
            fans_gender: Target fans gender.  Available Values: - `ALL`: All genders - `MALE_HIGH`: Mainly Male - `FE_MALE_HIGH`: Mainly Female
            gender: KOL's gender.  Available Values: - `ALL`: All genders - `MALE`: Male - `FEMALE`: Female
            content_tag: Content categories, separated by commas.
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/cooperator/blogger/v2/v1",
            {
                "searchType": search_type,
                "keyword": keyword,
                "page": page,
                "fansNumberLower": fans_number_lower,
                "fansNumberUpper": fans_number_upper,
                "fansAge": fans_age,
                "fansGender": fans_gender,
                "gender": gender,
                "contentTag": content_tag,
            },
        )

    def api_pgy_kol_data_core_data_v1(
        self,
        *,
        user_id: str,
        business: str | None = "DAILY_NOTE",
        note_type: str | None = "PHOTO_TEXT_AND_VIDEO",
        date_type: str | None = "DAY_30",
        advertise_switch: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        KOL Data Core (V1)

        Retrieve core performance data for a KOL.

        Args:
            user_id: KOL's user ID.
            business: Business type.  Available Values: - `DAILY_NOTE`: Daily notes - `COOPERATE_NOTE`: Cooperative notes
            note_type: Type of note.  Available Values: - `PHOTO_TEXT_AND_VIDEO`: Photo and Video - `PHOTO_TEXT`: Photo and Text - `VIDEO`: Video only
            date_type: Time range for data.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            advertise_switch: Advertisement filter.  Available Values: - `ALL`: All notes - `ORGANIC_ONLY`: Organic notes only
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/pgy/kol/data/core_data/v1",
            {
                "userId": user_id,
                "business": business,
                "noteType": note_type,
                "dateType": date_type,
                "advertiseSwitch": advertise_switch,
            },
        )

    def get_kol_info_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Profile (V1) [Deprecated]

        Retrieve KOL profile information (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-info/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_note_rate_v1(
        self,
        *,
        kol_id: str,
        date_type: str | None = "_1",
        note_type: str | None = "_3",
        ad_switch: str | None = "_1",
        business: str | None = "_0",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Note Rate (V1) [Deprecated]

        Get note performance rate (Legacy).

        Args:
            kol_id: KOL ID.
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 90 days
            note_type: Note type.  Available Values: - `_1`: Photo and Text - `_2`: Video - `_3`: Photo and Video
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-note-rate/v1",
            {
                "kolId": kol_id,
                "dateType": date_type,
                "noteType": note_type,
                "adSwitch": ad_switch,
                "business": business,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_fans_portrait_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Follower Profile (V1) [Deprecated]

        Get fans portrait (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-portrait/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_fans_summary_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Follower Analysis (V1) [Deprecated]

        Get fans summary (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-summary/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_fans_trend_v1(
        self,
        *,
        kol_id: str,
        date_type: str,
        increase_type: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Follower Trend (V1) [Deprecated]

        Get fans growth trend (Legacy).

        Args:
            kol_id: KOL ID.
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 60 days
            increase_type: Increase type.  Available Values: - `_1`: Total fans - `_2`: New fans increase
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-trend/v1",
            {
                "kolId": kol_id,
                "dateType": date_type,
                "increaseType": increase_type,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_note_list_v1(
        self,
        *,
        kol_id: str,
        ad_switch: str,
        order_type: str,
        page: int | None = 1,
        note_type: str | None = "_4",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Note List (V1)

        Retrieve list of notes for a specific KOL.

        Args:
            kol_id: KOL ID.
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
            order_type: Sorting order.  Available Values: - `_1`: Latest - `_2`: Most read - `_3`: Most interactions
            page: Page number.
            note_type: Note type.  Available Values: - `_1`: Photo and Text notes - `_2`: Video notes - `_3`: Cooperation notes - `_4`: All types
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-note-list/v1",
            {
                "kolId": kol_id,
                "adSwitch": ad_switch,
                "orderType": order_type,
                "page": page,
                "noteType": note_type,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_data_summary_v1(
        self,
        *,
        kol_id: str,
        business: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Data Overview (V1) [Deprecated]

        Get data overview (Legacy).

        Args:
            kol_id: KOL ID.
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-data-summary/v1",
            {
                "kolId": kol_id,
                "business": business,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_data_summary_v2(
        self,
        *,
        kol_id: str,
        business: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Data Overview (V2) [Deprecated]

        Get data overview (Legacy V2).

        Args:
            kol_id: KOL ID.
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-data-summary/v2",
            {
                "kolId": kol_id,
                "business": business,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_cost_effective_v1(
        self,
        *,
        kol_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Cost-Effectiveness (V1) [Deprecated]

        Get cost-effectiveness data (Legacy).

        Args:
            kol_id: KOL ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-cost-effective/v1",
            {
                "kolId": kol_id,
                "acceptCache": accept_cache,
            },
        )

    def get_note_detail_v1(
        self,
        *,
        note_id: str,
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Note Details (V1) [Deprecated]

        Get note details (Legacy).

        Args:
            note_id: Note ID.
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-note-detail/v1",
            {
                "noteId": note_id,
                "acceptCache": accept_cache,
            },
        )

    def get_kol_data_core_v1(
        self,
        *,
        kol_id: str,
        business: str | None = "_0",
        note_type: str | None = "_3",
        date_type: str | None = "_1",
        ad_switch: str | None = "_1",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        KOL Data Core (V1) [Deprecated]

        Retrieve core performance data (Legacy).

        Args:
            kol_id: KOL ID.
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
            note_type: Note type.  Available Values: - `_1`: Photo and Text - `_2`: Video - `_3`: Photo and Video
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 90 days
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
            accept_cache: Enable cache.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-core-data/v1",
            {
                "kolId": kol_id,
                "business": business,
                "noteType": note_type,
                "dateType": date_type,
                "adSwitch": ad_switch,
                "acceptCache": accept_cache,
            },
        )
