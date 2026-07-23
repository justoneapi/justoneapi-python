from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinXingtuResource(BaseResource):
    """Generated resource for Douyin Creator Marketplace (Xingtu)."""

    def gw_api_gsearch_search_for_author_square_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
        sort: str | None = "FANS",
        search_type: str | None = "NICKNAME",
        marketing_target: str | None = None,
        industry: str | None = "ALL",
        is_superstar: bool | None = False,
        follower_range: str | None = None,
        kol_price_type: str | None = None,
        kol_price_range: str | None = None,
        content_tag: str | None = None,
        content_theme: str | None = None,
        persona_tag: str | None = None,
        gender: str | None = None,
        location: str | None = None,
        tonality_tag: str | None = None,
        connected_user_range: str | None = None,
        audience_image: str | None = None,
        fans_image: str | None = None,
        expected_play_range: str | None = None,
        expected_cpm_range: str | None = None,
        expected_cpe_range: str | None = None,
        interaction_rate_range: str | None = None,
        completion_rate_range: str | None = None,
        viral_rate_range: str | None = None,
        progress_task_range: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Creator Search

        Searches Douyin Creator Marketplace (Xingtu) creators by keyword and structured filters for audience, pricing, content, performance, and campaign fit. Use it to build and compare campaign shortlists.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Creator search sorting. Values: FANS sorts by follower count descending, DEFAULT uses Xingtu score ranking.  Available Values: - `DEFAULT`: Platform default score ranking - `FANS`: Sort by follower count descending
            search_type: Search criteria type.  Available Values: - `NICKNAME`: By Nickname - `CONTENT`: By Content
            marketing_target: Marketing goal. Available values: BRAND_EXPOSURE/1/品牌曝光, CIRCLE_SEEDING/2/破圈种草, ACTION_CONVERSION/3/行动转化.  Available Values: - `BRAND_EXPOSURE`: Brand exposure - `CIRCLE_SEEDING`: Out-of-circle seeding - `ACTION_CONVERSION`: Action conversion
            industry: Recommended industry filter. Pass enum name, numeric industry ID, or Chinese industry label. Available values: - ALL/0/不限; - 1901: 3C及电器; - 1938: 购物; - 1903: 食品饮料; - 1904: 服装配饰; - 1905: 医药健康; - 1936: 医疗机构; - 1909: 家居建材; - 1907: 生活服务; - 1906: 商务服务; - 1921: 休闲娱乐; - 1937: 丽人; - 1908: 房地产; - 1910: 教育培训; - 1911: 出行旅游; - 1912: 社会公共; - 1913: 游戏; - 1914: 互联网电商服务; - 1915: 交通工具; - 1916: 汽车; - 1917: 农资园艺; - 1920: 机械设备; - 1939: 文化用品; - 1940: 运动户外; - 1922: 传媒资讯; - 1924: 通信; - 1925: 金融业; - 1927: 餐饮服务; - 1928: 工具类软件; - 1929: 招商加盟; - 1930: 美妆; - 1931: 母婴宠物; - 1933: 日化; - 1934: 实体书籍; - 1935: 社交通讯.  Available Values: - `ALL`: All - `ELECTRONICS_AND_APPLIANCES`: Electronics and Appliances - `SHOPPING`: Shopping - `FOOD_AND_BEVERAGE`: Food and Beverage - `CLOTHING_AND_ACCESSORIES`: Clothing and Accessories - `HEALTHCARE_AND_MEDICAL`: Healthcare and Medical - `MEDICAL_INSTITUTIONS`: Medical Institutions - `HOME_AND_BUILDING_MATERIALS`: Home and Building Materials - `LOCAL_SERVICES`: Local Services - `BUSINESS_SERVICES`: Business Services - `CULTURE_SPORTS_ENTERTAINMENT`: Leisure and Entertainment - `BEAUTY_SERVICES`: Beauty Services - `REAL_ESTATE`: Real Estate - `EDUCATION_AND_TRAINING`: Education and Training - `TRAVEL_AND_TOURISM`: Travel and Tourism - `PUBLIC_SERVICES`: Public Services - `GAMES`: Games - `RETAIL`: Internet E-commerce Services - `TRANSPORTATION_EQUIPMENT`: Transportation Equipment - `AUTOMOTIVE`: Automotive - `AGRICULTURE_FORESTRY_FISHERY`: Agriculture Forestry Fishery - `CHEMICAL_AND_ENERGY`: Chemical and Energy - `ELECTRONICS_AND_ELECTRICAL`: Electronics and Electrical - `MACHINERY_EQUIPMENT`: Machinery Equipment - `MEDIA_AND_INFORMATION`: Media and Information - `LOGISTICS`: Logistics - `TELECOMMUNICATIONS`: Telecommunications - `FINANCIAL_SERVICES`: Financial Services - `CATERING_SERVICES`: Catering Services - `SOFTWARE_TOOLS`: Software Tools - `FRANCHISING_AND_INVESTMENT`: Franchising and Investment - `BEAUTY_AND_COSMETICS`: Beauty and Cosmetics - `MOTHER_BABY_AND_PET`: Mother Baby and Pet - `DAILY_CHEMICALS`: Daily Chemicals - `PHYSICAL_BOOKS`: Physical Books - `SOCIAL_AND_COMMUNICATION`: Social and Communication - `CULTURAL_SUPPLIES`: Cultural Supplies - `SPORTS_OUTDOOR`: Sports and Outdoors
            is_superstar: Whether to filter celebrity creators.
            follower_range: Raw follower count range in min-max format. Example: 1000-2000 means 1,000 to 2,000 followers; 5000000-10000000 means 5 million to 10 million followers.
            kol_price_type: KOL price type.  Available Values: - `VIDEO_1_20S`: Video 1-20s - `VIDEO_21_60S`: Video 21-60s - `VIDEO_OVER_60S`: Video > 60s - `CUSTOM_SHORT_DRAMA_EPISODE`: Mini-drama episode - `NATURAL_PLAY_CPM`: CPM naturally - `SHORT_LIVE_SEEDING_VIDEO`: Short-live seeding video - `SHORT_LIVE_WARMUP_VIDEO`: Short-live warm-up video - `CELEBRITY_SHORT_LIVE_SEEDING`: Celebrity short-live seeding - `CELEBRITY_SHORT_LIVE_WARMUP`: Celebrity short-live warm-up - `CELEBRITY_VIDEO`: Celebrity video - `COLLECTION_VIDEO`: Collection video - `DOUYIN_SHORT_VIDEO_CO_CREATION_MAIN_CREATOR`: Douyin short video co-creation - main creator - `DOUYIN_SHORT_VIDEO_CO_CREATION_PARTICIPANT`: Douyin short video co-creation - participant
            kol_price_range: KOL price range (e.g., 10000-50000).
            content_tag: Creator category filter. Pass Xingtu first-level or second-level category labels separated by commas. Available values: - 美妆: 美妆教程, 妆容展示, 护肤保养, 美妆测评种草; - 时尚: 穿搭, 街拍, 造型, 时尚媒体; - 萌宠: 日常宠物, 特别宠物, 宠物周边; - 测评: 美妆测评, 3C数码测评, 汽车测评, 美食产品测评, 母婴产品测评, 综合测评, 酒店测评; - 游戏: 游戏剧情, 游戏解说, 游戏资讯, 游戏其他, 游戏录屏, 游戏集锦; - 二次元: 二次元真人, 动画漫画, 配音声优, 宅物手办; - 旅行: 旅行记录, 旅行攻略, 旅行推荐, 户外生活; - 汽车: 汽车测评, 汽车知识, 汽车周边; - 生活: 生活记录, 生活小窍门, 好物推荐, 健康养生, 婚恋; - 音乐: 歌曲演唱, 乐器演奏, 音乐教学, 音乐其他, 音乐剪辑; - 舞蹈; - 美食: 美食教程, 美食探店, 美食产品测评, 乡村野食, 美食其他, 酒类; - 母婴亲子: 育儿科普, 萌娃日常, 亲子互动, 测评种草; - 运动健身: 健身, 极限运动, 体育资讯, 冰雪, 垂钓, 格斗, 球类项目, 综合体育; - 科技数码: 3C数码, 家居电器, 科技; - 教育培训: 考学培训, 语言教学, 个人管理, 职业教育; - 颜值达人: 美女, 帅哥; - 生活家居: 硬装, 软装, 生活技巧, 家居氛围; - 才艺技能: 创意才能, 手工, 摄影, 绘画, 其他才艺; - 影视娱乐: 影视解说, 影视混剪, 明星资讯, 综艺解说, 综艺混剪; - 艺术文化: 传统文化, 人文科普, 自然科学; - 财经投资: 传统金融, 互联网金融, 财经知识; - 三农; - 剧情搞笑: 剧情, 搞笑; - 情感; - 园艺; - 房产: 其他房产, 房产知识, 房产及投资, 楼盘评测, 楼市资讯, 租房; - 随拍; - 媒体号. Example: 美妆,穿搭,剧情搞笑
            content_theme: Content theme filter. Pass Xingtu second-level content theme labels separated by commas. Available values include: - 妆容妆造: 淡妆教程, 变装造型, 韩系妆容, 甜美妆容, 清透妆容, 复古妆容, 男性妆容; - 穿搭指南: 日常穿搭, 简约气质穿搭, 国风穿搭, 运动穿搭, 通勤穿搭, 旅行穿搭, 职业穿搭, 约会穿搭; - 亲子育儿: 亲子活动, 亲子沟通, 学前训练, 新手爸妈指导, 儿童护理, 宝宝辅食, 奶粉测评, 孕产饮食; - 美食教程与测评: 地方美食, 家常菜谱, 美食探店, 零食测评, 酒水品鉴, 厨房用品, 海鲜烹饪, 减脂美食; - 精彩车生活: 汽车行业资讯, 用车知识, 车辆保养, 自驾旅行, 新能源汽车资讯, 汽车用品测评, SUV测评; - 手机/数码/家电分享: 科技科普, 电子产品测评, 家电推荐, 手机评测, 智能家居, AI应用, 数码开箱; - 剧情演绎: 搞笑剧情, 剧情反转, 情感演绎, 家庭幽默演绎, 职场趣闻, 古风剧情, 生存挑战; - 萌宠养护: 宠物狗故事, 动物萌态, 宠物养护, 猫咪萌态, 宠物健康, 宠物护理, 宠物救助; - 旅行攻略: 国内旅行, 海外旅行, 城市旅行攻略, 酒店体验, 露营体验, 亲子旅行, 网红景点种草; - 家居好物: 清洁技巧, 生活好物评测, 家居选购, 家居装修, 家居收纳, 家装避坑, 房间布置; - 运动户外: 户外运动, 健身塑形, 赛事回顾, 体重管理, 极限运动, 跑步健身, 户外露营. Example: 亲子活动,宝宝辅食
            persona_tag: Creator persona or background labels. Pass Xingtu labels or numeric tag IDs separated by commas. Available values: - 人群属性: Z世代, 新锐白领, 精致妈妈, 都市蓝领, 资深中产, 小镇青年, 小镇中老年, 都市银发; - 社会身份: 音乐人, 非遗传人, 画家; - 主要出镜人物: 海外华人, 外国友人, 情侣, 夫妻, 家庭, 朋友, 同事, 亲子, 个人; - 肤质肤色: 混油皮, 干皮, 油皮, 敏感肌, 痘痘肌, 黄皮, 白皮, 瑕疵皮; - 皮肤养护: 美白, 抗老, 祛皱, 抗炎, 修复, 控油, 眼部护理, 补水保湿, 祛斑, 祛痘祛闭口, 隔离防晒; - 母婴阶段: 孕期, 0-6月, 7-12月, 1-3岁, 3-6岁, 6-12岁, 12-15岁, 15-18岁; - 爱好: 摄影, 时尚穿搭, 美食制作, 科普, 星座, 绘画; - 职业: 法律从业者, 航空业从业者, 健身/舞蹈教练, 专业美食从业者, 室内设计师; - 学历: 大学生, 硕士生, 博士, 留学生; - 黄v认证: 美妆创作者, 体育创作者, 媒体人/主持人, 科技创作者, 运动员; - Other labels: 潮流运动, 球类, 非球类, 室内健身, 城市运动, 户外运动, 数码潮流玩家, 户外爱好者, 室内设计师, 品酒家/调酒师, 美食评论人, 母婴行业专家, 奶爸, 旧屋改造, 装修设计, 收纳, 新生儿妈妈, 孕妈, 时尚妈妈, 二三胎妈妈, 西餐, 火锅, 国风爱好者, 成分党. Example: 大学生,美妆创作者
            gender: Creator gender. Available values: MALE/1/男性, FEMALE/2/女性.  Available Values: - `MALE`: Male - `FEMALE`: Female
            location: Creator location filter. Pass Chinese province or city names separated by commas. Available province values include: 北京市, 天津市, 河北省, 山西省, 内蒙古自治区, 辽宁省, 吉林省, 黑龙江省, 上海市, 江苏省, 浙江省, 安徽省, 福建省, 江西省, 山东省, 河南省, 湖北省, 湖南省, 广东省, 广西壮族自治区, 海南省, 重庆市, 四川省, 贵州省, 云南省, 西藏自治区, 陕西省, 甘肃省, 青海省, 宁夏回族自治区, 新疆维吾尔自治区, 台湾省, 香港特别行政区, 澳门特别行政区. Example: 广东省,深圳市
            tonality_tag: Creator tonality labels. Pass Xingtu first-level or second-level tonality labels separated by commas. Available values: - 身份/爱好: 马术, 高尔夫, 橄榄球, 时尚爱好者, 企业高管, 汽车爱好者, 学者专家, 古玩收藏; - 精致达人: 设计师, 高阶潮玩, 职业模特, 造型顾问, 独立设计师, 美术/画廊/展览, 歌剧舞台剧, 流行, 潮流买手, 电影; - 潮流酷: 冲浪, 浮潜, 说唱, 滑雪, 普拉提, 网球. Example: 精致达人,设计师
            connected_user_range: Connected user count range. Pass raw user counts in min-max format. Example: 1000000-3000000
            audience_image: Audience profile filter from Xingtu Audience Image. Pass one or more shortcut values separated by commas. Available values: - Gender: GENDER_MALE_50, GENDER_MALE_60, GENDER_MALE_70, GENDER_MALE_80, GENDER_FEMALE_50, GENDER_FEMALE_60, GENDER_FEMALE_70, GENDER_FEMALE_80; - Age: AGE_18_23, AGE_24_30, AGE_31_40, AGE_41_50, AGE_GT_50; - Device: DEVICE_IPHONE, DEVICE_HUAWEI, DEVICE_XIAOMI, DEVICE_VIVO, DEVICE_OPPO; - City tier: CITY_TIER_1, CITY_TIER_2, CITY_TIER_3, CITY_TIER_4, CITY_TIER_5; - Average order amount: SPEND_0_50, SPEND_50_100, SPEND_100_200, SPEND_200_500, SPEND_GT_500; - Crowd profile: CROWD_REFINED_MOTHER(53 精致妈妈), CROWD_URBAN_SILVER(54 都市银发), CROWD_NEW_WHITE_COLLAR(55 新锐白领), CROWD_SENIOR_MIDDLE_CLASS(56 资深中产), CROWD_URBAN_BLUE_COLLAR(57 都市蓝领), CROWD_GEN_Z(58 Z世代), CROWD_TOWN_MIDDLE_AGED(59 小镇中老年), CROWD_TOWN_YOUTH(60 小镇青年). Example: GENDER_FEMALE_50,CROWD_REFINED_MOTHER
            fans_image: Fan profile filter from Xingtu Fan Image. Pass one or more shortcut values separated by commas. Available values: - Gender: GENDER_MALE_50, GENDER_MALE_60, GENDER_MALE_70, GENDER_MALE_80, GENDER_FEMALE_50, GENDER_FEMALE_60, GENDER_FEMALE_70, GENDER_FEMALE_80; - Age: AGE_18_23, AGE_24_30, AGE_31_40, AGE_41_50, AGE_GT_50; - Device: DEVICE_IPHONE, DEVICE_HUAWEI, DEVICE_XIAOMI, DEVICE_VIVO, DEVICE_OPPO; - City tier: CITY_TIER_1, CITY_TIER_2, CITY_TIER_3, CITY_TIER_4, CITY_TIER_5; - Average order amount: SPEND_0_50, SPEND_50_100, SPEND_100_200, SPEND_200_500, SPEND_GT_500; - Crowd profile: CROWD_REFINED_MOTHER(53 精致妈妈), CROWD_URBAN_SILVER(54 都市银发), CROWD_NEW_WHITE_COLLAR(55 新锐白领), CROWD_SENIOR_MIDDLE_CLASS(56 资深中产), CROWD_URBAN_BLUE_COLLAR(57 都市蓝领), CROWD_GEN_Z(58 Z世代), CROWD_TOWN_MIDDLE_AGED(59 小镇中老年), CROWD_TOWN_YOUTH(60 小镇青年). Example: GENDER_FEMALE_50,CROWD_REFINED_MOTHER
            expected_play_range: Expected play count range. Use raw counts in min-max format. Page presets include 10000000 or above, 5000000-10000000, 3000000-5000000, 1000000-3000000, 100000-1000000, and 0-100000. For open-ended presets, pass a high upper bound such as 10000000-1000000000. Example: 1000000-3000000.
            expected_cpm_range: Expected CPM range in min-max format. Example values matching Xingtu packs: 0-10, 0-20, 0-30, 0-50, 0-100, 100-1000000.
            expected_cpe_range: Expected CPE range in min-max format. Example values matching Xingtu packs: 0-1, 0-2, 0-3, 0-5, 0-10, 10-1000000.
            interaction_rate_range: Interaction rate range in decimal min-max format. Example values: 0.01-1 for 1% or above, 0.02-1 for 2% or above.
            completion_rate_range: Completion rate range in decimal min-max format. Example values: 0.1-1 for 10% or above, 0.2-1 for 20% or above.
            viral_rate_range: Viral content rate range in decimal min-max format. Page presets include 0-0.1, 0.1-0.25, 0.25-0.5, 0.5-0.99, and 0.99 or above. For open-ended presets, pass a high upper bound such as 0.99-1. Example: 0.1-0.25.
            progress_task_range: In-progress task count range. Place a colon between the day count and the min-max range; omit either bound for an open range. Example: 30:8-
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/gsearch/search_for_author_square/v1",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "searchType": search_type,
                "marketingTarget": marketing_target,
                "industry": industry,
                "isSuperstar": is_superstar,
                "followerRange": follower_range,
                "kolPriceType": kol_price_type,
                "kolPriceRange": kol_price_range,
                "contentTag": content_tag,
                "contentTheme": content_theme,
                "personaTag": persona_tag,
                "gender": gender,
                "location": location,
                "tonalityTag": tonality_tag,
                "connectedUserRange": connected_user_range,
                "audienceImage": audience_image,
                "fansImage": fans_image,
                "expectedPlayRange": expected_play_range,
                "expectedCpmRange": expected_cpm_range,
                "expectedCpeRange": expected_cpe_range,
                "interactionRateRange": interaction_rate_range,
                "completionRateRange": completion_rate_range,
                "viralRateRange": viral_rate_range,
                "progressTaskRange": progress_task_range,
            },
        )

    def gw_api_author_get_author_base_info_v1(
        self,
        *,
        o_author_id: str,
        platform: str | None = "SHORT_VIDEO",
    ) -> ApiResponse[Any]:
        """
        Creator Profile

        Returns the Douyin Creator Marketplace (Xingtu) profile for a specified creator and content channel. Use it to review creator information before shortlisting or campaign outreach.

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
        Creator Link Structure

        Returns Douyin Creator Marketplace (Xingtu) creator-link structure data for a specified creator and content channel. Use it to compare creator link structures during performance research.

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
        Creator Visibility Status

        Returns whether a specified creator can be displayed in Douyin Creator Marketplace (Xingtu) for the selected content channel. Use it to check creator availability before building a campaign shortlist.

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
        Creator Channel Metrics

        Returns Douyin Creator Marketplace (Xingtu) channel information for a specified creator and content format. Use it to compare a creator's short-video, live, image-text, or short-drama presence.

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
        Creator Order Experience

        Returns Douyin Creator Marketplace (Xingtu) creator order-experience information for the last 30 or 90 days. Use it to review marketplace order history during creator evaluation.

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
        Creator Link Metrics

        Returns Douyin Creator Marketplace (Xingtu) creator-link metrics for a specified creator, content channel, and industry category. Use it to review creator link information in an industry context.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            industry_tag: Industry tag.  Available Values: - `ALL`: All - `ELECTRONICS_AND_APPLIANCES`: Electronics and Appliances - `SHOPPING`: Shopping - `FOOD_AND_BEVERAGE`: Food and Beverage - `CLOTHING_AND_ACCESSORIES`: Clothing and Accessories - `HEALTHCARE_AND_MEDICAL`: Healthcare and Medical - `MEDICAL_INSTITUTIONS`: Medical Institutions - `HOME_AND_BUILDING_MATERIALS`: Home and Building Materials - `LOCAL_SERVICES`: Local Services - `BUSINESS_SERVICES`: Business Services - `CULTURE_SPORTS_ENTERTAINMENT`: Leisure and Entertainment - `BEAUTY_SERVICES`: Beauty Services - `REAL_ESTATE`: Real Estate - `EDUCATION_AND_TRAINING`: Education and Training - `TRAVEL_AND_TOURISM`: Travel and Tourism - `PUBLIC_SERVICES`: Public Services - `GAMES`: Games - `RETAIL`: Internet E-commerce Services - `TRANSPORTATION_EQUIPMENT`: Transportation Equipment - `AUTOMOTIVE`: Automotive - `AGRICULTURE_FORESTRY_FISHERY`: Agriculture Forestry Fishery - `CHEMICAL_AND_ENERGY`: Chemical and Energy - `ELECTRONICS_AND_ELECTRICAL`: Electronics and Electrical - `MACHINERY_EQUIPMENT`: Machinery Equipment - `MEDIA_AND_INFORMATION`: Media and Information - `LOGISTICS`: Logistics - `TELECOMMUNICATIONS`: Telecommunications - `FINANCIAL_SERVICES`: Financial Services - `CATERING_SERVICES`: Catering Services - `SOFTWARE_TOOLS`: Software Tools - `FRANCHISING_AND_INVESTMENT`: Franchising and Investment - `BEAUTY_AND_COSMETICS`: Beauty and Cosmetics - `MOTHER_BABY_AND_PET`: Mother Baby and Pet - `DAILY_CHEMICALS`: Daily Chemicals - `PHYSICAL_BOOKS`: Physical Books - `SOCIAL_AND_COMMUNICATION`: Social and Communication - `CULTURAL_SUPPLIES`: Cultural Supplies - `SPORTS_OUTDOOR`: Sports and Outdoors
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
        Video Distribution

        Returns Douyin Creator Marketplace (Xingtu) video-distribution data for a specified creator and content channel. Use it to analyze how the creator's videos are distributed during campaign research.

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
        Audience Distribution

        Returns Douyin Creator Marketplace (Xingtu) audience-distribution data for a creator, content channel, and selected relationship stage. Use it to assess audience fit for campaign targeting.

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
        Marketing Metrics

        Returns Douyin Creator Marketplace (Xingtu) marketing information for a specified creator and content channel. Use it to compare creator commercial offerings during campaign planning.

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
        Spread Metrics

        Returns Douyin Creator Marketplace (Xingtu) spread metrics for a creator, with channel, period, video-type, assignment, and flow filters. Use it to compare creator spread performance during campaign planning.

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
        Conversion Analysis

        Returns Douyin Creator Marketplace (Xingtu) conversion analysis for a creator, content channel, and 30- or 90-day period. Use it to compare creator conversion performance during commerce campaign planning.

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
        Showcase Items

        Returns Douyin Creator Marketplace (Xingtu) showcase items for a creator, with content-channel, assignment, and flow filters. Use it to review a creator's marketplace showcase during commerce campaign planning.

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
        Conversion Resources

        Lists Douyin Creator Marketplace (Xingtu) conversion-related videos or products for a creator, with industry, period, resource-type, and page filters. Use it to review commerce examples before creator selection.

        Args:
            o_author_id: Author's unique ID.
            platform: Platform type.  Available Values: - `SHORT_VIDEO`: Short video - `LIVE_STREAMING`: Live streaming - `PICTURE_TEXT`: Picture and text - `SHORT_DRAMA`: Short drama
            industry_id: Industry category.  Available Values: - `ALL`: All - `ELECTRONICS_AND_APPLIANCES`: Electronics and Appliances - `SHOPPING`: Shopping - `FOOD_AND_BEVERAGE`: Food and Beverage - `CLOTHING_AND_ACCESSORIES`: Clothing and Accessories - `HEALTHCARE_AND_MEDICAL`: Healthcare and Medical - `MEDICAL_INSTITUTIONS`: Medical Institutions - `HOME_AND_BUILDING_MATERIALS`: Home and Building Materials - `LOCAL_SERVICES`: Local Services - `BUSINESS_SERVICES`: Business Services - `CULTURE_SPORTS_ENTERTAINMENT`: Leisure and Entertainment - `BEAUTY_SERVICES`: Beauty Services - `REAL_ESTATE`: Real Estate - `EDUCATION_AND_TRAINING`: Education and Training - `TRAVEL_AND_TOURISM`: Travel and Tourism - `PUBLIC_SERVICES`: Public Services - `GAMES`: Games - `RETAIL`: Internet E-commerce Services - `TRANSPORTATION_EQUIPMENT`: Transportation Equipment - `AUTOMOTIVE`: Automotive - `AGRICULTURE_FORESTRY_FISHERY`: Agriculture Forestry Fishery - `CHEMICAL_AND_ENERGY`: Chemical and Energy - `ELECTRONICS_AND_ELECTRICAL`: Electronics and Electrical - `MACHINERY_EQUIPMENT`: Machinery Equipment - `MEDIA_AND_INFORMATION`: Media and Information - `LOGISTICS`: Logistics - `TELECOMMUNICATIONS`: Telecommunications - `FINANCIAL_SERVICES`: Financial Services - `CATERING_SERVICES`: Catering Services - `SOFTWARE_TOOLS`: Software Tools - `FRANCHISING_AND_INVESTMENT`: Franchising and Investment - `BEAUTY_AND_COSMETICS`: Beauty and Cosmetics - `MOTHER_BABY_AND_PET`: Mother Baby and Pet - `DAILY_CHEMICALS`: Daily Chemicals - `PHYSICAL_BOOKS`: Physical Books - `SOCIAL_AND_COMMUNICATION`: Social and Communication - `CULTURAL_SUPPLIES`: Cultural Supplies - `SPORTS_OUTDOOR`: Sports and Outdoors
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
        Cost Performance Analysis

        Returns Douyin Creator Marketplace (Xingtu) cost-performance information for a specified creator and content channel. Use it to compare creator efficiency during campaign budgeting.

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
        Audience Touchpoint Distribution

        Returns Douyin Creator Marketplace (Xingtu) audience-touchpoint distribution data for a specified creator and content channel. Use it to compare audience-contact patterns during campaign research.

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
        Recommended Videos

        Returns Douyin Creator Marketplace (Xingtu) recommended videos for a specified creator and content channel. Use it to inspect representative content during creator research.

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
        Follower Distribution

        Returns Douyin Creator Marketplace (Xingtu) follower or loyal-follower distribution data for a specified creator. Use it to compare audience-profile distributions during creator selection.

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

    def gw_api_data_sp_item_report_trend_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Item Report Trends

        Returns Douyin Creator Marketplace (Xingtu) report trend data for a specified video item. Use it to review how a video's reported performance changes over time.

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
        Video Details

        Returns Douyin Creator Marketplace (Xingtu) report details for a specified video item. Use it to inspect a video's marketplace report during content performance analysis.

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
        Item Report Analysis

        Returns Douyin Creator Marketplace (Xingtu) report analysis for a specified video item. Use it to evaluate a video's reported performance during campaign review.

        Args:
            item_id: Item's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/item_report_th_analysis/v1",
            {
                "itemId": item_id,
            },
        )

    def gw_api_data_get_author_hot_comment_tokens_v1(
        self,
        *,
        o_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Comment Keyword Analysis

        Returns Douyin Creator Marketplace (Xingtu) comment keyword analysis for a specified creator. Use it to identify recurring audience discussion themes during creator research.

        Args:
            o_author_id: Author's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data/get_author_hot_comment_tokens/v1",
            {
                "oAuthorId": o_author_id,
            },
        )

    def gw_api_data_sp_get_author_daily_fans_v1(
        self,
        *,
        o_author_id: str,
        start_date: str,
        end_date: str,
    ) -> ApiResponse[Any]:
        """
        Follower Growth Trend

        Returns Douyin Creator Marketplace (Xingtu) daily follower trend data for a specified creator and date range. Use it to review follower growth patterns during creator evaluation.

        Args:
            o_author_id: Author's unique ID.
            start_date: Start Date (yyyy-MM-dd).
            end_date: End Date (yyyy-MM-dd).
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/data_sp/get_author_daily_fans/v1",
            {
                "oAuthorId": o_author_id,
                "startDate": start_date,
                "endDate": end_date,
            },
        )

    def gw_api_gauthor_get_author_content_hot_keywords_v1(
        self,
        *,
        o_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Content Keyword Analysis

        Returns Douyin Creator Marketplace (Xingtu) content keyword analysis for a specified creator. Use it to identify recurring content themes during creator positioning research.

        Args:
            o_author_id: Author's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/gauthor/get_author_content_hot_keywords/v1",
            {
                "oAuthorId": o_author_id,
            },
        )

    def gw_api_gauthor_author_get_business_card_info_v1(
        self,
        *,
        o_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Business Card

        Returns the Douyin Creator Marketplace (Xingtu) business-card profile for a specified creator. Use it to review creator identity and business context before campaign outreach.

        Args:
            o_author_id: Author's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/gauthor/author_get_business_card_info/v1",
            {
                "oAuthorId": o_author_id,
            },
        )

    def gw_api_aggregator_get_author_commerce_spread_info_v1(
        self,
        *,
        o_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Commerce Spread Info

        Returns Douyin Creator Marketplace (Xingtu) commerce spread information for a specified creator. Use it to compare creators during commerce campaign planning.

        Args:
            o_author_id: Author's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_commerce_spread_info/v1",
            {
                "oAuthorId": o_author_id,
            },
        )

    def gw_api_aggregator_get_author_homepage_videos_v1(
        self,
        *,
        o_author_id: str,
        page: int | None = 1,
        keyword: str | None = None,
        video_type: str | None = "ALL",
        only_assign: bool | None = False,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Creator Homepage Videos

        Lists a Douyin Creator Marketplace (Xingtu) creator's homepage videos with keyword, video-type, assignment, date, and page filters. Use it to review relevant content before campaign selection.

        Args:
            o_author_id: Author's unique Xingtu ID.
            page: Page number, starting from 1.
            keyword: Keyword used to search creator homepage videos.
            video_type: Homepage video type filter.  Available Values: - `ALL`: All videos - `PERSONAL`: Personal videos - `XINGTU`: Xingtu videos
            only_assign: Whether to include only assigned videos. Xingtu usually shows this option when `videoType` is `XINGTU`.
            start_date: Start publish date in yyyyMMdd format. The filter starts at 00:00:00 in Asia/Shanghai.
            end_date: End publish date in yyyyMMdd format. The filter ends at 23:59:59 in Asia/Shanghai.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_homepage_videos/v1",
            {
                "oAuthorId": o_author_id,
                "page": page,
                "keyword": keyword,
                "videoType": video_type,
                "onlyAssign": only_assign,
                "startDate": start_date,
                "endDate": end_date,
            },
        )

    def gw_api_aggregator_get_author_tags_v1(
        self,
        *,
        star_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Tags

        Returns Douyin Creator Marketplace (Xingtu) tags for a specified creator. Use it to classify creators and compare their fit for campaign briefs.

        Args:
            star_author_id: Creator's unique Xingtu ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_tags/v1",
            {
                "starAuthorId": star_author_id,
            },
        )

    def gw_api_aggregator_get_author_side_base_info_v1(
        self,
        *,
        o_author_id: str,
    ) -> ApiResponse[Any]:
        """
        Creator Side Base Info

        Returns the Douyin Creator Marketplace (Xingtu) side-card baseline information for a specified creator. Use it to review a creator's marketplace overview during shortlisting.

        Args:
            o_author_id: Author's unique ID.
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_side_base_info/v1",
            {
                "oAuthorId": o_author_id,
            },
        )

    def gw_api_aggregator_get_author_live_statistics_v1(
        self,
        *,
        o_author_id: str,
        live_type: str | None = "1",
        period: str | None = "30",
        only_star_order: bool | None = False,
        flow_type: str | None = "0",
    ) -> ApiResponse[Any]:
        """
        Live Statistics

        Returns Douyin Creator Marketplace (Xingtu) live-stream statistics for a creator, with live-room, period, marketplace-order, and flow filters. Use it to compare live-streaming creators for campaign planning.

        Args:
            o_author_id: Author's unique ID.
            live_type: Live room type filter.  Available Values: - `ALL`: All live rooms - `GAME`: Game live rooms - `ECOMMERCE`: E-commerce live rooms - `OTHER`: Other live rooms
            period: Live data time period.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
            only_star_order: Whether to include only Xingtu marketplace orders.
            flow_type: Flow type filter.  Available Values: - `EXCLUDE`: Exclude - `INCLUDE`: Include
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_live_statistics/v1",
            {
                "oAuthorId": o_author_id,
                "liveType": live_type,
                "period": period,
                "onlyStarOrder": only_star_order,
                "flowType": flow_type,
            },
        )

    def gw_api_aggregator_get_author_live_watch_distribution_v1(
        self,
        *,
        o_author_id: str,
        live_crowd_type: str | None = "2",
        live_type: str | None = "1",
    ) -> ApiResponse[Any]:
        """
        Live Watch Distribution

        Returns Douyin Creator Marketplace (Xingtu) live audience or follower watch-distribution data for a creator and selected live-room type. Use it to assess live audience fit for a campaign.

        Args:
            o_author_id: Author's unique ID.
            live_crowd_type: Live audience profile type.  Available Values: - `AUDIENCE`: Viewer profile - `FANS`: Follower profile
            live_type: Live room type filter.  Available Values: - `ALL`: All live rooms - `GAME`: Game live rooms - `ECOMMERCE`: E-commerce live rooms - `OTHER`: Other live rooms
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_live_watch_distribution/v1",
            {
                "oAuthorId": o_author_id,
                "liveCrowdType": live_crowd_type,
                "liveType": live_type,
            },
        )

    def gw_api_aggregator_get_author_commerce_seed_base_info_v1(
        self,
        *,
        o_author_id: str,
        range: str | None = "DAY_90",
    ) -> ApiResponse[Any]:
        """
        Commerce Seeding Base Info

        Returns Douyin Creator Marketplace (Xingtu) commerce-seeding baseline information for a creator over a selectable 30- or 90-day period. Use it to research creators for product-seeding campaigns.

        Args:
            o_author_id: Author's unique ID.
            range: Time range.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_commerce_seed_base_info/v1",
            {
                "oAuthorId": o_author_id,
                "range": range,
            },
        )

    def gw_api_aggregator_get_author_contract_base_info(
        self,
        *,
        o_author_id: str,
        range: str | None = "90",
    ) -> ApiResponse[Any]:
        """
        Creator Contract Base Info

        Returns Douyin Creator Marketplace (Xingtu) contract-related baseline information for a creator over a selectable 30- or 90-day period. Use it to review creator contract context during campaign planning.

        Args:
            o_author_id: Author's unique ID.
            range: Time range.  Available Values: - `DAY_30`: Last 30 days - `DAY_90`: Last 90 days
        """
        return self._get(
            "/api/douyin-xingtu/gw/api/aggregator/get_author_contract_base_info",
            {
                "oAuthorId": o_author_id,
                "range": range,
            },
        )
