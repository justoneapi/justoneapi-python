from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuResource(BaseResource):
    """Generated resource for Xiaohongshu (RedNote)."""

    def ask_dots(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Ask Dots AI

        Queries Xiaohongshu (RedNote) Ask Dots AI with a keyword question. Use it to retrieve an AI answer for topic research and question exploration.

        Args:
            keyword: Question or keyword to submit to Ask Dots AI.
        """
        return self._get(
            "/api/xiaohongshu/ask-dots",
            {
                "keyword": keyword,
            },
        )

    def hot_search_v1(
        self,
        *,
        search_word: str | None = "",
        page_num: int | None = 1,
        order_by: str | None = "premium_imp_num",
        nd: str | None = "DAY_7",
        note_content_category: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Hot Search

        Searches Xiaohongshu (RedNote) hot-content entries with optional keyword, content-category path, pagination, ranking metric, and time-range controls. Use it to support trend discovery, topic monitoring, and content planning.

        Args:
            search_word: Search keyword.
            page_num: Page number for pagination.
            order_by: Sort metric for the result set.  Available Values: - `premium_imp_num`: Exposure - `premium_good_read_rate`: Read rate - `premium_read_num`: Read count - `premium_engage_num`: Engagement count - `premium_engage_rate`: Engagement rate - `premium_like_num`: Like count - `premium_fav_num`: Favorite count - `premium_cmt_num`: Comment count
            nd: Time range in days.  Available Values: - `DAY_3`: Last 3 days - `DAY_7`: Last 7 days - `DAY_14`: Last 14 days - `DAY_30`: Last 30 days
            note_content_category: Content category filter. Pass one complete Pugongying category path joined with # separators. You may pass a parent path or append one listed child with another #. Only one path is accepted.  Available values:  Content categories: - 内容类目#美妆: 整体妆容, 唇妆, 眼妆, 美甲, 底妆, 美妆合集, 香水, 美妆其他 - 内容类目#护肤: 面部保养, 面部清洁, 护肤合集, 护肤其他 - 内容类目#个人护理: 头发产品, 身体护理, 口腔护理, 护理其他 - 内容类目#母婴: 母婴日常, 早教, 婴童用品, 婴童洗护, 婴童食品, 婴童时尚, 孕期穿搭, 孕产经验, 产后恢复, 育儿经验, 宝宝才艺, 宝宝写真, 母婴其他 - 内容类目#时尚: 穿搭, 配饰, 发型, 箱包, 鞋靴, 时尚其他 - 内容类目#美食: 美食教程, 美食探店, 美食展示, 美食测评, 吃播, 美食其他 - 内容类目#家居家装: 装修, 家居用品, 花艺园艺, 家居装饰, 家具, 家电, 室内设计, 居家经验, 家居家装其他 - 内容类目#影视综资讯: 动漫, 娱乐资讯, 影视, 民生资讯, 综艺, 影视综其他 - 内容类目#运动健身: 减脂塑形, 滑雪, 滑板, 水上活动, 运动其他, 足球, 篮球, 跑步, 游泳 - 内容类目#宠物: 猫, 狗, 动物其他 - 内容类目#文化艺术: 社科, 文化, 艺术, 文化艺术其他 - 内容类目#兴趣爱好: 绘画, 手工, 阅读, 文具手账, 舞蹈, 兴趣爱好其他, 玩具周边 - 内容类目#生活记录: 接地气生活, 日常片段, 中外生活, 品质生活, 校园生活 - 内容类目#教育: 大学教育, k12教育, 家庭教育, 学习日常, 留学教育, 教育其他, 语言教育 - 内容类目#职场: 职场干货, 职场行业, 职业考试, 职场其他 - 内容类目#情感: 情感知识, 情感日常, 情感其他 - 内容类目#摄影: 人文风光摄影, 摄影技巧, 胶片摄影, 人像摄影, 摄影其他 - 内容类目#游戏: 手机游戏, 主机游戏, 游戏其他, 线下游戏 - 内容类目#科技数码: 移动数码, 玩机攻略, 数码科技其他 - 内容类目#出行旅游: 城市出行, 户外, 旅行 - 内容类目#音乐 - 内容类目#搞笑 - 内容类目#健康养生 - 内容类目#汽车: 用车攻略, 汽车评测, 汽车其他 - 内容类目#婚嫁: 婚礼造型, 婚礼记录, 婚礼经验, 婚礼用品 - 内容类目#商业财经 - 内容类目#素材 - 内容类目#其他  Industry categories: - 所属行业#母婴: 母婴出行, 哺乳喂养工具, 婴童个护清洁, 母婴家居, 母婴奶粉, 母婴辅零食, 婴童服饰鞋靴, 玩具相关, 母婴纸品, 孕产妇相关, 母婴营养品, 婴童面部护肤, 母婴小家电 - 所属行业#家用电器: 大家电, 厨卫电器, 生活电器, 家电套系 - 所属行业#3C数码: 手机, 数码设备, 电脑, 办公设备, 操作系统 - 所属行业#食品饮料: 休闲零食, 方便速食, 粮油调味, 预制菜, 饮料冲调, 乳制品, 水果/水产, 肉禽蛋品, 功能性食品, 酒类（新） - 所属行业#美妆个护: 彩妆, 美容护肤, 香水香薰, 身体洗护, 口腔护理, 头发护理, 美容仪器 - 所属行业#汽车出行: 乘用车, 摩托车, 电动自行车, 自行车, 卡车, 汽车用品, 维修保养, 汽车服务 - 所属行业#本地生活: 奶茶果汁(新), 咖啡(新), 甜品烘焙(新), 熟食卤味(新), 特色小吃/特产(新), 酒吧(新), 西式快餐(新), 中式快餐(新), 中式正餐(新), 西式正餐(新), 线下零售 - 所属行业#日化家清: 家务工具, 家用清洁, 纸品, 护理用品 - 所属行业#医疗健康: OTC, 保健食品, 保健用品, 非OTC药品, 健康机械, 视力保健, 家用医疗器械, 成人计生（械） - 所属行业#宠物（新）: 宠物服务, 宠物食品, 宠物用品, 养宠经验, 宠物药保 - 所属行业#家居家装: 灯饰光源, 家居百货, 家居建材零售, 家具, 家装辅材, 家装主材, 五金电具, 装修设计与工程服务, 智能家居, 家居卖场, 家居展会, 家纺, 餐厨杯 - 所属行业#出行旅游: 交通出行, 酒店住宿, 国内游(新), 出境游(新), 景点景区(新), 旅游攻略(新), 旅游主题(新) - 所属行业#教育培训: K12教育, 素质教育, 图书, 成人兴趣培训, 学历教育, 语言及留学, 早教, 职业教育 - 所属行业#金融行业: 保险, 贷款, 银行, 证券 - 所属行业#医疗医美: 口腔医疗, 眼科医疗, 皮肤美容, 植发养发, 体检机构(新), 月子妇产(新), 面部塑形, 医美身体塑形, 中医医疗 - 所属行业#免税平台: 美妆个护, 奢侈品 - 所属行业#服饰鞋包: 女装, 男装, 女鞋, 男鞋, 女士内衣, 男士内衣, 服饰配件, 童装/亲子装, 箱包, 旅行箱, 童鞋/亲子鞋 - 所属行业#珠宝配饰: 腕表, 首饰, 眼镜, 配饰, 珠宝摆件, 金条、金币 - 所属行业#运动户外: 运动鞋, 户外鞋, 运动服装, 户外服装, 运动户外装备, 运动服配, 健身器械, 运动现场 - 所属行业#文玩娱乐: 玩具, 游戏, 文玩收藏, 文体, 文具 - 所属行业#到店综合: 商务服务, 生活服务 - 所属行业#奢侈品: 箱包, 服饰, 鞋履, 珠宝配饰, 腕表, 运动户外, 品质生活, 婴童, 内衣, 高端酒店, 书写工具 - 所属行业#互联网: 平台电商, 网服, 游戏, 内容消费, 生活服务, 软件工具, 会员服务 - 所属行业#影像婚美: 婚纱摄影, 写真摄影, 婚礼服务, 婚恋交友 - 所属行业#房地产: 房产中介, 房产开发, 商业地产  Examples: - 内容类目#美妆 - 内容类目#美妆#整体妆容 - 所属行业#母婴#母婴出行
        """
        return self._get(
            "/api/xiaohongshu/hot-search/v1",
            {
                "searchWord": search_word,
                "pageNum": page_num,
                "orderBy": order_by,
                "nd": nd,
                "noteContentCategory": note_content_category,
            },
        )

    def hot_list_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Hot List

        Retrieves the current Xiaohongshu (RedNote) hot list for platform trend monitoring and content research. Use it to review current hot-list entries before deeper analysis.
        """
        return self._get(
            "/api/xiaohongshu/hot-list/v1",
            {},
        )

    def search_note_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
        note_time: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Note Search

        Get Xiaohongshu (RedNote) note Search data, including note snippets, authors, media, publish time, engagement signals, and pagination data, for topic discovery, trend monitoring, creator research, and content analysis.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter.  Available Values: - `ONE_DAY`: Within one day - `ONE_WEEK`: Within a week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v1",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "noteType": note_type,
                "noteTime": note_time,
            },
        )

    def search_note_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
        note_time: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Note Search

        Searches Xiaohongshu (RedNote) notes by keyword with pagination plus sort, note-type, and publish-time filters. Use it to support topic research, content discovery, and monitoring keyword-related posts.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter. Results may include notes published outside the selected time range.  Available Values: - `ONE_DAY`: Within one day - `ONE_WEEK`: Within a week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v2",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "noteType": note_type,
                "noteTime": note_time,
            },
        )

    def search_note_v3(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
        note_time: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Note Search

        Get Xiaohongshu (RedNote) note Search data, including snippets, authors, and media, for topic discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter. This parameter is for reference only and does not have much effect.  Available Values: - `ONE_DAY`: Within one day - `ONE_WEEK`: Within a week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v3",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "noteType": note_type,
                "noteTime": note_time,
            },
        )

    def search_note_v4(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort_type: str | None = "general",
        note_type: str | None = "ALL",
        time_filter: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Note Search

        Searches Xiaohongshu (RedNote) notes through the mobile-app search flow with pagination, sorting, note-type, and time filters. Use it to support iterative topic research and filtered content discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort_type: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `ALL`: No Limit - `VIDEO_NOTE`: Video Note - `NORMAL_NOTE`: Normal Note
            time_filter: Publish time filter.  Available Values: - `ALL`: No Limit - `ONE_DAY`: Within one day - `ONE_WEEK`: Within one week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v4",
            {
                "keyword": keyword,
                "page": page,
                "sortType": sort_type,
                "noteType": note_type,
                "timeFilter": time_filter,
            },
        )

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Search

        Searches Xiaohongshu (RedNote) users by keyword with page-based pagination. Use it to support creator discovery, account research, and finding profiles related to a topic, name, or brand term.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/xiaohongshu/search-user/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_user_note_list_v1(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Get Xiaohongshu (RedNote) user Published Notes data, including note metadata, covers, publish times, pagination cursors, and engagement signals, for account monitoring, creator research, and content analysis.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page.
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v1",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
            },
        )

    def get_user_note_list_v2(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Get Xiaohongshu (RedNote) user Published Notes data, including note metadata, covers, and publish times, for account monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (the last note's cursor value).
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v2",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
            },
        )

    def get_user_note_list_v3(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Get Xiaohongshu (RedNote) user Published Notes data, including note metadata, covers, and publish times, for account monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (the last note's cursor value).
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v3",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
            },
        )

    def get_user_note_list_v4(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Retrieves notes published by a Xiaohongshu (RedNote) user, accepting a user ID or supported profile URL and a cursor for pagination. Use it to support creator content browsing, account monitoring, and reviewing a user's note history.

        Args:
            user_id: A Xiaohongshu user ID or a profile URL containing /user/profile/.
            last_cursor: Pagination cursor from the previous page (the last note's cursor value).
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v4",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
            },
        )

    def get_note_detail_v1(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Retrieves Xiaohongshu (RedNote) details for a note identified by a note ID or supported explore URL. Use it to perform direct note lookup and content review from stored identifiers or shared explore links.

        Args:
            note_id: A Xiaohongshu note ID or an explore URL containing /explore/.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v1",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v2(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v2",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v3(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v3",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v4(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v4",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v5(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v5",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v6(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Retrieves Xiaohongshu (RedNote) video-note details by note ID. Use it to look up and process a known video note.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v6",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v7(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v7",
            {
                "noteId": note_id,
            },
        )

    def get_note_comment_v2(
        self,
        *,
        note_id: str,
        last_cursor: str | None = None,
        sort: str | None = "latest",
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Retrieves comments for a Xiaohongshu (RedNote) note with cursor pagination and normal, latest, or like-count sorting. Use it to support feedback review, discussion analysis, and comment moderation workflows.

        Args:
            note_id: A Xiaohongshu note ID or an explore URL containing /explore/.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
            sort: Sort strategy for the result set.  Available Values: - `normal`: Normal - `latest`: Latest - `like_count`: Like Count
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v2",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_comment_v3(
        self,
        *,
        note_id: str,
        last_cursor: str | None = None,
        sort: str | None = "latest",
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Get Xiaohongshu (RedNote) note Comments data, including text, authors, and timestamps, for feedback analysis.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page.
            sort: Sort strategy for the result set.  Available Values: - `normal`: Normal - `latest`: Latest - `like_count`: Like Count
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v3",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_comment_v4(
        self,
        *,
        note_id: str,
        last_cursor: str | None = None,
        sort: str | None = "latest",
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Get Xiaohongshu (RedNote) note Comments data, including text, authors, and timestamps, for feedback analysis.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
            sort: Sort strategy for the result set.  Available Values: - `normal`: Normal - `latest`: Latest - `like_count`: Like Count
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v4",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_sub_comment_v2(
        self,
        *,
        note_id: str,
        comment_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Comment Replies

        Retrieves replies to a specific Xiaohongshu (RedNote) note comment with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for feedback review or moderation.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            comment_id: Unique comment identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
        """
        return self._get(
            "/api/xiaohongshu/get-note-sub-comment/v2",
            {
                "noteId": note_id,
                "commentId": comment_id,
                "lastCursor": last_cursor,
            },
        )

    def get_user_v3(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a Xiaohongshu (RedNote) user profile from a user ID or supported profile URL. Use it to support creator discovery, account research, and reviewing a known profile before related content analysis.

        Args:
            user_id: A Xiaohongshu user ID or a profile URL containing /user/profile/.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v3",
            {
                "userId": user_id,
            },
        )

    def get_user_v4(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Xiaohongshu (RedNote) user Profile data, including follower counts and bio details, for creator research, account analysis, and competitor monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v4",
            {
                "userId": user_id,
            },
        )

    def search_recommend_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Keyword Suggestions

        Returns Xiaohongshu (RedNote) search keyword suggestions for a submitted seed term. Use it to expand query sets, refine content-research searches, and plan SEO or programmatic SEO keyword coverage.

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/xiaohongshu/search-recommend/v1",
            {
                "keyword": keyword,
            },
        )

    def get_topic_note_list_v1(
        self,
        *,
        topic_id: str,
        sort: str | None = "hot",
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Topic Note List

        Retrieves Xiaohongshu (RedNote) notes associated with a topic ID, with hot or latest sorting and cursor pagination. Use it to support topic content discovery, trend review, and continuing through topic result pages.

        Args:
            topic_id: Unique topic identifier on Xiaohongshu.
            sort: Sort order for the result set.  Available Values: - `time`: Latest - `hot`: Hot
            cursor: Pagination cursor from the previous page.
        """
        return self._get(
            "/api/xiaohongshu/get-topic-note-list/v1",
            {
                "topicId": topic_id,
                "sort": sort,
                "cursor": cursor,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution

        Resolve a supported Xiaohongshu (RedNote) short share link and return its public redirect URL. Use it to expand shared links before subsequent Xiaohongshu content lookup or processing.

        Args:
            share_url: A Xiaohongshu (RedNote) short share URL beginning with http://xhslink.com/ or https://xhslink.com/.
        """
        return self._get(
            "/api/xiaohongshu/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
