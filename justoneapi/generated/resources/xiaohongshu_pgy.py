from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuPgyResource(BaseResource):
    """Generated resource for Xiaohongshu Creator Marketplace (Pugongying)."""

    def api_solar_cooperator_user_blogger_user_id_v1(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Profile

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Profile data, including audience and pricing data, for influencer vetting, benchmark analysis, and campaign planning.

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
        Data Summary

        Get Xiaohongshu Creator Marketplace (Pugongying) Summary data, including activity, engagement, and audience growth, for creator evaluation, campaign planning, and creator benchmarking.

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
        Follower Growth History

        Get Xiaohongshu Creator Marketplace (Pugongying) follower Growth History data, including historical points, trend signals, and growth metrics, for trend tracking, audience analysis, and creator performance monitoring.

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
        Follower Summary

        Get Xiaohongshu Creator Marketplace (Pugongying) follower Summary data, including growth and engagement metrics, for audience analysis and creator benchmarking.

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
        Similar Creators

        Get Xiaohongshu Creator Marketplace (Pugongying) similar Creators data, including audience signals, for creator discovery, benchmarking, and shortlist building.

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
        Creator Feature Tags

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Feature Tags data, including platform tags, category labels, and classification signals, for segmentation, discovery, and creator classification.

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
        Creator Content Tags

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Content Tags data, including topic labels that describe publishing themes and content focus, for creator evaluation, campaign planning, and creator benchmarking.

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
        Note Performance Metrics

        Get Xiaohongshu Creator Marketplace (Pugongying) note performance metrics data, including core metrics, trend signals, and performance indicators, for content efficiency analysis, creator benchmarking, and campaign planning.

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
        User Published Notes

        Get Xiaohongshu Creator Marketplace (Pugongying) user Published Notes data, including note metadata and engagement signals, for creator monitoring and campaign research.

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
        Follower Distribution

        Get Xiaohongshu Creator Marketplace (Pugongying) follower distribution data, including audience demographics, interests, and distribution metrics, for creator evaluation, campaign planning, and creator benchmarking.

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
        Cost Effectiveness Analysis

        Get Xiaohongshu Creator Marketplace (Pugongying) cost Effectiveness Analysis data, including pricing, reach, and engagement efficiency indicators, for campaign evaluation.

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
        Note Details

        Get Xiaohongshu Creator Marketplace (Pugongying) note Details data, including media and engagement signals, for content analysis, archiving, and campaign review.

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
        personal_tags: str | None = None,
        top20_crowds_label: str | None = None,
        industry_specific_crowds_motor_dom: str | None = None,
        feature_tags: str | None = None,
        content_theme_label: str | None = None,
        exclude_low_active: bool | None = None,
        fans_num_up: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Creator Search

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Search data, including filters, returning profile, and audience, for discovery, comparison, and shortlist building.

        Args:
            search_type: Search criteria type.  Available Values: - `NICKNAME`: Search by nickname - `NOTE`: Search by note content
            keyword: Search keyword.
            page: Page number.
            fans_number_lower: Minimum number of fans.
            fans_number_upper: Maximum number of fans.
            fans_age: Target fans age group.  Available Values: - `ALL`: All ages - `LT_18`: Under 18 - `AGE_18_24`: 18 to 24 - `AGE_25_34`: 25 to 34 - `AGE_35_44`: 35 to 44 - `GT_44`: Above 44
            fans_gender: Target fans gender.  Available Values: - `ALL`: All genders - `MALE_HIGH`: Mainly Male - `FE_MALE_HIGH`: Mainly Female
            gender: KOL's gender.  Available Values: - `ALL`: All genders - `MALE`: Male - `FEMALE`: Female
            content_tag: Content category filter. Pass first-level or second-level category labels from Pugongying, separated by commas.
            personal_tags: Blogger persona tag filter covering family identity, profession identity, and special background labels. Pass label values separated by commas.
            top20_crowds_label: Top-20 audience filter. Pass top-level or child audience labels separated by commas; child labels are converted to Pugongying request values.
            industry_specific_crowds_motor_dom: Industry-specific portrait filter. Pass Pugongying portrait value IDs or label values separated by commas.
            feature_tags: Good-at content tag filter. Pass label values separated by commas.
            content_theme_label: Content theme filter. Pass Pugongying value IDs or label values separated by commas; labels are converted to value IDs.
            exclude_low_active: Whether to exclude low-activity bloggers.
            fans_num_up: Whether to exclude bloggers whose fan count is dropping.
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
                "personalTags": personal_tags,
                "top20CrowdsLabel": top20_crowds_label,
                "industrySpecificCrowdsMotorDom": industry_specific_crowds_motor_dom,
                "featureTags": feature_tags,
                "contentThemeLabel": content_theme_label,
                "excludeLowActive": exclude_low_active,
                "fansNumUp": fans_num_up,
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
        Creator Core Metrics

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Core Metrics data, including engagement and content metrics, for benchmarking, vetting, and campaign planning.

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

    def api_pgy_content_square_search_note_v2_v1(
        self,
        *,
        search_word: str | None = "",
        page_num: int | None = 1,
        biz_type: str | None = "XIAOHONGSHU_HOT",
        order_by: str | None = "premium_imp_num",
        nd: str | None = "DAY_7",
    ) -> ApiResponse[Any]:
        """
        Content Square Notes

        Search Xiaohongshu Creator Marketplace (Pugongying) content square notes by business type, ranking metric, time range, and keyword.

        Args:
            search_word: Keyword for note search. Empty string searches all notes.
            page_num: Page number for results.
            biz_type: Business category.  Available Values: - `XIAOHONGSHU_HOT`: Xiaohongshu hot - `PRODUCT_SEEDING`: Product seeding - `ECOMMERCE_PROMOTION`: E-commerce promotion - `PUGONGYING_COOPERATION`: Pugongying cooperation - `LEAD_COLLECTION`: Lead collection - `ECOMMERCE_HOT`: E-commerce hot - `SEEDING_DIRECT`: Seeding direct - `APP_PROMOTION`: App promotion
            order_by: Ranking metric.  Available Values: - `premium_imp_num`: Exposure - `premium_good_read_rate`: Read rate - `premium_read_num`: Read count - `premium_engage_num`: Engagement count - `premium_engage_rate`: Engagement rate - `premium_like_num`: Like count - `premium_fav_num`: Favorite count - `premium_cmt_num`: Comment count
            nd: Time range in days.  Available Values: - `DAY_3`: Last 3 days - `DAY_7`: Last 7 days - `DAY_14`: Last 14 days - `DAY_30`: Last 30 days
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/pgy/content_square/search_note_v2/v1",
            {
                "searchWord": search_word,
                "pageNum": page_num,
                "bizType": biz_type,
                "orderBy": order_by,
                "nd": nd,
            },
        )

    def get_kol_info_v1(
        self,
        *,
        kol_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Profile

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Profile data, including audience and pricing data, for influencer vetting, benchmark analysis, and campaign planning.

        Args:
            kol_id: KOL ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-info/v1",
            {
                "kolId": kol_id,
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
    ) -> ApiResponse[Any]:
        """
        Note Performance Metrics

        Get Xiaohongshu Creator Marketplace (Pugongying) note performance metrics data, including core metrics, trend signals, and performance indicators, for content efficiency analysis, creator benchmarking, and campaign planning.

        Args:
            kol_id: KOL ID.
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 90 days
            note_type: Note type.  Available Values: - `_1`: Photo and Text - `_2`: Video - `_3`: Photo and Video
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-note-rate/v1",
            {
                "kolId": kol_id,
                "dateType": date_type,
                "noteType": note_type,
                "adSwitch": ad_switch,
                "business": business,
            },
        )

    def get_kol_fans_portrait_v1(
        self,
        *,
        kol_id: str,
    ) -> ApiResponse[Any]:
        """
        Follower Distribution

        Get Xiaohongshu Creator Marketplace (Pugongying) follower distribution data, including audience demographics, interests, and distribution metrics, for creator evaluation, campaign planning, and creator benchmarking.

        Args:
            kol_id: KOL ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-portrait/v1",
            {
                "kolId": kol_id,
            },
        )

    def get_kol_fans_summary_v1(
        self,
        *,
        kol_id: str,
    ) -> ApiResponse[Any]:
        """
        Follower Summary

        Get Xiaohongshu Creator Marketplace (Pugongying) follower summary data, including core metrics, trend signals, and performance indicators, for creator evaluation, campaign planning, and creator benchmarking.

        Args:
            kol_id: KOL ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-summary/v1",
            {
                "kolId": kol_id,
            },
        )

    def get_kol_fans_trend_v1(
        self,
        *,
        kol_id: str,
        date_type: str,
        increase_type: str,
    ) -> ApiResponse[Any]:
        """
        Follower Growth History

        Get Xiaohongshu Creator Marketplace (Pugongying) follower growth history data, including historical audience changes over time, for creator evaluation, campaign planning, and creator benchmarking.

        Args:
            kol_id: KOL ID.
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 60 days
            increase_type: Increase type.  Available Values: - `_1`: Total fans - `_2`: New fans increase
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-fans-trend/v1",
            {
                "kolId": kol_id,
                "dateType": date_type,
                "increaseType": increase_type,
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
    ) -> ApiResponse[Any]:
        """
        Creator Note List

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Note List data, including content metadata, publish time, and engagement indicators, for content analysis.

        Args:
            kol_id: KOL ID.
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
            order_type: Sorting order.  Available Values: - `_1`: Latest - `_2`: Most read - `_3`: Most interactions
            page: Page number.
            note_type: Note type.  Available Values: - `_1`: Photo and Text notes - `_2`: Video notes - `_3`: Cooperation notes - `_4`: All types
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-note-list/v1",
            {
                "kolId": kol_id,
                "adSwitch": ad_switch,
                "orderType": order_type,
                "page": page,
                "noteType": note_type,
            },
        )

    def get_kol_data_summary_v2(
        self,
        *,
        kol_id: str,
        business: str,
    ) -> ApiResponse[Any]:
        """
        Data Summary

        Get Xiaohongshu Creator Marketplace (Pugongying) summary data, including activity, engagement, and audience growth, for creator evaluation, campaign planning, and creator benchmarking.

        Args:
            kol_id: KOL ID.
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-data-summary/v2",
            {
                "kolId": kol_id,
                "business": business,
            },
        )

    def get_kol_cost_effective_v1(
        self,
        *,
        kol_id: str,
    ) -> ApiResponse[Any]:
        """
        Cost Effectiveness Analysis

        Get Xiaohongshu Creator Marketplace (Pugongying) cost Effectiveness Analysis data, including pricing, reach, and engagement efficiency indicators, for campaign evaluation.

        Args:
            kol_id: KOL ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-cost-effective/v1",
            {
                "kolId": kol_id,
            },
        )

    def get_note_detail_v1(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu Creator Marketplace (Pugongying) note Details data, including media and engagement signals, for content analysis, archiving, and campaign review.

        Args:
            note_id: Note ID.
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-note-detail/v1",
            {
                "noteId": note_id,
            },
        )

    def get_kol_core_data_v1(
        self,
        *,
        kol_id: str,
        business: str | None = "_0",
        note_type: str | None = "_3",
        date_type: str | None = "_1",
        ad_switch: str | None = "_1",
    ) -> ApiResponse[Any]:
        """
        Creator Core Metrics

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Core Metrics data, including engagement and content metrics, for benchmarking, vetting, and campaign planning.

        Args:
            kol_id: KOL ID.
            business: Business type.  Available Values: - `_0`: Normal notes - `_1`: Cooperation notes
            note_type: Note type.  Available Values: - `_1`: Photo and Text - `_2`: Video - `_3`: Photo and Video
            date_type: Date type.  Available Values: - `_1`: Last 30 days - `_2`: Last 90 days
            ad_switch: Ad filter.  Available Values: - `_1`: Full traffic (All notes) - `_0`: Natural traffic (Organic notes)
        """
        return self._get(
            "/api/xiaohongshu-pgy/get-kol-core-data/v1",
            {
                "kolId": kol_id,
                "business": business,
                "noteType": note_type,
                "dateType": date_type,
                "adSwitch": ad_switch,
            },
        )
