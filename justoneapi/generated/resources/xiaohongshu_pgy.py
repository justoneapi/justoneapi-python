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
        note_type: str | None = "ALL",
        industry: str | None = None,
        accum_common_imp_medin_num30d: str | None = None,
        read_mid_nor30: str | None = None,
        inter_mid_nor30: str | None = None,
        thousand_like_percent30: str | None = None,
        note_price: str | None = None,
        video_price: str | None = None,
        invite_reply48h_num_ratio: str | None = None,
        progress_order_cnt: str | None = None,
        trade_type: str | None = None,
        trade_report_brand_ids: str | None = None,
        exclude_trade_report_brand_ids: bool | None = None,
        accum_coop_imp_medin_num30d: str | None = None,
        read_mid_coop30: str | None = None,
        inter_mid_coop30: str | None = None,
        m_cpuv_num30d: str | None = None,
        estimate_picture_cpm: str | None = None,
        estimate_video_cpm: str | None = None,
        estimate_pic_read_price: str | None = None,
        estimate_video_read_price: str | None = None,
        estimate_picture_engage_cost: str | None = None,
        estimate_video_engage_cost: str | None = None,
        estimate_cpuv30d: str | None = None,
        klive_cnt30d: str | None = None,
        avg_live_viewer_num: str | None = None,
        avg_agmv90d: str | None = None,
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
            personal_tags: Blogger persona tag filter covering family identity, profession identity, and special background labels. Pass Chinese label values separated by English or Chinese commas. Family identity values: 妈妈, 萌娃, 爸爸, 奶奶, 情侣, 夫妻, 家庭, 闺蜜, 兄弟, 备孕中, 孕期中, 0-6个月, 6-12个月, 1-3岁, 3-6岁, 6-12岁, 12岁以上. Profession identity values: 传统行业, 互联网, 教育科研, 金融法律, 企业创业, 时尚美妆, 食品饮料, 文化传媒, 医疗健康, 艺术设计, 影视娱乐, 运动健身, 专业服务, 工程师, 销售, HR, 教练, 运动员, 舞蹈老师. Special background values: 生活背景, 备考经验, 兴趣爱好, 留学背景, 海外华人, 铲屎官, 孕妈, 独居人群, 外国人, 混血儿.
            top20_crowds_label: Top-20 audience filter. Pass top-level or child audience labels separated by commas; child labels are converted to Pugongying request values.
            industry_specific_crowds_motor_dom: Industry-specific portrait filter. Pass Pugongying portrait value IDs or label values separated by commas.
            feature_tags: Good-at content tag filter. Pass label values separated by commas.
            content_theme_label: Content theme filter. Pass Pugongying value IDs or label values separated by commas; labels are converted to value IDs.
            exclude_low_active: Whether to exclude low-activity bloggers.
            fans_num_up: Whether to exclude bloggers whose fan count is dropping.
            note_type: Note type filter. Values: ALL=all note types, PHOTO_TEXT=mainly photo-text notes, VIDEO=mainly video notes.  Available Values: - `ALL`: All note types - `PHOTO_TEXT`: Mainly photo-text notes - `VIDEO`: Mainly video notes
            industry: Pugongying industry preset for industry assistant style creator recommendations.  Available Values: - `BEAUTY_PERSONAL_CARE_BEAUTY`: Beauty and personal care - beauty - `BEAUTY_PERSONAL_CARE_SKINCARE`: Beauty and personal care - skincare - `BEAUTY_PERSONAL_CARE_PERSONAL_CARE`: Beauty and personal care - personal care - `BEAUTY_PERSONAL_CARE_FRAGRANCE`: Beauty and personal care - fragrance - `FOOD_BEVERAGE_SNACKS`: Food and beverage - snacks - `FOOD_BEVERAGE_DRINKS`: Food and beverage - drinks - `FOOD_BEVERAGE_HEALTH_FOOD`: Food and beverage - health food - `FOOD_BEVERAGE_DAIRY`: Food and beverage - dairy - `FOOD_BEVERAGE_ALCOHOL`: Food and beverage - alcohol - `FOOD_BEVERAGE_GRAINS_OIL`: Food and beverage - grains and oil - `FOOD_BEVERAGE_CROSS_BORDER_FOOD`: Food and beverage - cross-border food - `FOOD_BEVERAGE_FRESH_FOOD`: Food and beverage - fresh food - `FOOD_BEVERAGE_MEAL_REPLACEMENT`: Food and beverage - meal replacement - `FOOD_BEVERAGE_TRADITIONAL_NOURISHMENT`: Food and beverage - traditional nourishment - `MOTHER_BABY_SUPPLIES`: Mother and baby - baby supplies - `MOTHER_BABY_FORMULA_FOOD`: Mother and baby - formula and baby food - `DIGITAL_APPLIANCES_HOME_APPLIANCES`: Digital and appliances - home appliances - `DIGITAL_APPLIANCES_DIGITAL_PRODUCTS`: Digital and appliances - digital products - `DAILY_GOODS_HOUSEHOLD_DAILY_USE`: Daily goods - household daily use - `DAILY_GOODS_PET_SUPPLIES_FOOD`: Daily goods - pet supplies and food - `DAILY_GOODS_OFFICE_SUPPLIES`: Daily goods - office supplies - `APPAREL_ACCESSORIES_CLOTHING_SHOES_HATS`: Apparel and accessories - clothing, shoes, and hats - `APPAREL_ACCESSORIES_JEWELRY`: Apparel and accessories - jewelry - `APPAREL_ACCESSORIES_BAGS_GLASSES`: Apparel and accessories - bags and glasses - `APPAREL_ACCESSORIES_SPORTS_OUTDOOR`: Apparel and accessories - sports and outdoor - `APPAREL_ACCESSORIES_WATCHES`: Apparel and accessories - watches - `APPAREL_ACCESSORIES_SECOND_HAND_LUXURY`: Apparel and accessories - second-hand luxury - `HOME_BUILDING_MATERIALS_HOME_DECOR`: Home and building materials - home decor - `HOME_BUILDING_MATERIALS_FURNITURE`: Home and building materials - furniture - `HOME_BUILDING_MATERIALS_MAIN_MATERIALS`: Home and building materials - main building materials - `AUTOMOTIVE`: Automotive - `INTERNET_ECOMMERCE`: Internet - e-commerce - `INTERNET_SOFTWARE_TOOLS`: Internet - software tools - `HEALTHCARE_MEDICAL_DEVICES`: Healthcare - medical devices - `HEALTHCARE_MEDICAL_BEAUTY`: Healthcare - medical beauty - `CULTURE_SPORTS_ENTERTAINMENT_SPORTS_GOODS`: Culture, sports, and entertainment - sports goods - `CULTURE_SPORTS_ENTERTAINMENT_STATIONERY_TOYS_GIFTS`: Culture, sports, and entertainment - stationery, toys, and gifts - `CULTURE_SPORTS_ENTERTAINMENT_OUTDOOR_PRODUCTS`: Culture, sports, and entertainment - outdoor products - `CULTURE_SPORTS_ENTERTAINMENT_ART_COLLECTIBLES`: Culture, sports, and entertainment - art collectibles - `LIFE_SERVICES_OFFLINE_RETAIL`: Life services - offline retail - `LIFE_SERVICES_BEAUTY_HAIR`: Life services - beauty and hair - `CATERING_RESTAURANTS`: Catering - restaurants - `CATERING_DRINKS_DESSERTS`: Catering - drinks and desserts - `BUSINESS_SERVICES`: Business services - `EDUCATION_TRAINING_LANGUAGE_STUDY_ABROAD`: Education and training - language and study abroad - `EDUCATION_TRAINING_VOCATIONAL_EDUCATION`: Education and training - vocational education - `EDUCATION_TRAINING_INTEREST_TRAINING`: Education and training - interest training - `EDUCATION_TRAINING_K12_EDUCATION`: Education and training - K-12 education - `EDUCATION_TRAINING_DEGREE_EDUCATION`: Education and training - degree education - `EDUCATION_TRAINING_CORPORATE_DEVELOPMENT`: Education and training - corporate and team development - `EDUCATION_TRAINING_OTHER`: Education and training - other - `GAMES`: Games - `TRAVEL_TOURISM`: Travel and tourism
            accum_common_imp_medin_num30d: Daily note exposure median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.
            read_mid_nor30: Daily note read median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.
            inter_mid_nor30: Daily note interaction median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.
            thousand_like_percent30: Thousand-like note ratio range. Pass fractional ratios such as 0.4,null or percentage values such as 40,null.
            note_price: Photo-text cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.
            video_price: Video cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.
            invite_reply48h_num_ratio: 48-hour invite reply ratio range. Pass fractional ratios such as 0.9,0.95 or percentage values such as 90,95.
            progress_order_cnt: Current cooperation order count range. Pass two comma-separated numeric bounds.
            trade_type: Recent cooperation industry filter from Pugongying.
            trade_report_brand_ids: Recent cooperation brand IDs, separated by English or Chinese commas.
            exclude_trade_report_brand_ids: Whether to exclude creators who cooperated with the selected recent cooperation brands.
            accum_coop_imp_medin_num30d: Cooperation note exposure median range. Pass two comma-separated numeric bounds.
            read_mid_coop30: Cooperation note read median range. Pass two comma-separated numeric bounds.
            inter_mid_coop30: Cooperation note interaction median range. Pass two comma-separated numeric bounds.
            m_cpuv_num30d: Cooperation note outer-store median range. Pass two comma-separated numeric bounds.
            estimate_picture_cpm: Estimated photo-text CPM range. Pass two comma-separated numeric bounds.
            estimate_video_cpm: Estimated video CPM range. Pass two comma-separated numeric bounds.
            estimate_pic_read_price: Estimated photo-text read unit price range. Pass two comma-separated numeric bounds.
            estimate_video_read_price: Estimated video read unit price range. Pass two comma-separated numeric bounds.
            estimate_picture_engage_cost: Estimated photo-text engagement unit price range. Pass two comma-separated numeric bounds.
            estimate_video_engage_cost: Estimated video engagement unit price range. Pass two comma-separated numeric bounds.
            estimate_cpuv30d: Estimated outer-store visit unit price range. Pass two comma-separated numeric bounds.
            klive_cnt30d: Live count in the last 30 days range. Pass two comma-separated numeric bounds.
            avg_live_viewer_num: Average live viewer count range. Pass two comma-separated numeric bounds.
            avg_agmv90d: Average live sales amount range. Pass two comma-separated numeric bounds.
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
                "noteType": note_type,
                "industry": industry,
                "accumCommonImpMedinNum30d": accum_common_imp_medin_num30d,
                "readMidNor30": read_mid_nor30,
                "interMidNor30": inter_mid_nor30,
                "thousandLikePercent30": thousand_like_percent30,
                "notePrice": note_price,
                "videoPrice": video_price,
                "inviteReply48hNumRatio": invite_reply48h_num_ratio,
                "progressOrderCnt": progress_order_cnt,
                "tradeType": trade_type,
                "tradeReportBrandIds": trade_report_brand_ids,
                "excludeTradeReportBrandIds": exclude_trade_report_brand_ids,
                "accumCoopImpMedinNum30d": accum_coop_imp_medin_num30d,
                "readMidCoop30": read_mid_coop30,
                "interMidCoop30": inter_mid_coop30,
                "mCpuvNum30d": m_cpuv_num30d,
                "estimatePictureCpm": estimate_picture_cpm,
                "estimateVideoCpm": estimate_video_cpm,
                "estimatePicReadPrice": estimate_pic_read_price,
                "estimateVideoReadPrice": estimate_video_read_price,
                "estimatePictureEngageCost": estimate_picture_engage_cost,
                "estimateVideoEngageCost": estimate_video_engage_cost,
                "estimateCpuv30d": estimate_cpuv30d,
                "kliveCnt30d": klive_cnt30d,
                "avgLiveViewerNum": avg_live_viewer_num,
                "avgAgmv90d": avg_agmv90d,
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
        Creator Note List

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
        Creator Note List Pro

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
