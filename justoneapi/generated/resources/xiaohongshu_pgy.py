from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuPgyResource(BaseResource):
    """Generated resource for Xiaohongshu Creator Marketplace (Pugongying)."""

    def api_solar_cooperator_blogger_v2_v1(
        self,
        *,
        search_type: str | None = "NICKNAME",
        keyword: str | None = None,
        page: int | None = 1,
        sort: str | None = "FANS",
        fans_number_lower: int | None = None,
        fans_number_upper: int | None = None,
        fans_age: str | None = "ALL",
        fans_gender: str | None = "ALL",
        fans_child_age_info: str | None = None,
        gender: str | None = "ALL",
        location: str | None = None,
        content_tag: str | None = None,
        content_scene_label: str | None = None,
        personal_tags: str | None = None,
        market_target: str | None = None,
        audience_group: str | None = None,
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
        similar_user_id: str | None = None,
        similar_word: str | None = None,
        fans_location: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Creator Search

        Get Xiaohongshu Creator Marketplace (Pugongying) creator Search data, including filters, returning profile, and audience, for discovery, comparison, and shortlist building.

        Args:
            search_type: Search criteria type.  Available Values: - `NICKNAME`: Search by nickname - `NOTE`: Search by note content
            keyword: Search keyword.
            page: Page number.
            sort: Creator search sorting. Values: FANS sorts by follower count descending, DEFAULT uses Pugongying intelligent ranking.  Available Values: - `DEFAULT`: Platform default intelligent ranking - `FANS`: Sort by follower count descending
            fans_number_lower: Minimum number of fans.
            fans_number_upper: Maximum number of fans.
            fans_age: Target fans age group.  Available Values: - `ALL`: All ages - `LT_18`: Under 18 - `AGE_18_24`: 18 to 24 - `AGE_25_34`: 25 to 34 - `AGE_35_44`: 35 to 44 - `GT_44`: Above 44
            fans_gender: Target fans gender.  Available Values: - `ALL`: All genders - `MALE_HIGH`: Mainly Male - `FE_MALE_HIGH`: Mainly Female
            fans_child_age_info: Mother-and-baby audience stage filter. Pass Pugongying labels or numeric codes separated by English or Chinese commas.  Available values: - 1: 备孕 - 2: 0-6月 - 3: 7-12月 - 4: 1-3岁 - 5: 4-6岁 - 6: 7-12岁 - 7: 孕早期 - 8: 孕晚期
            gender: KOL's gender.  Available Values: - `ALL`: All genders - `MALE`: Male - `FEMALE`: Female
            location: Creator profile location filter. Pass Pugongying location labels separated by English or Chinese commas. Country, China province or region, city-level paths, and district/county-level paths are supported. China province or region short labels are normalized to the full Pugongying value. Only paths present in the Pugongying location tree are accepted. Paths such as `河北 秦皇岛`, `山西 长治 潞州区`, or `中国 山西 长治 潞州区` are normalized to values like `中国 山西 长治 潞州区`.  Available country/province base values: - 中国 - 美国 - 日本 - 澳大利亚 - 英国 - 加拿大 - 韩国 - 法国 - 德国 - 新加坡 - 其他 - 中国 北京 - 中国 天津 - 中国 河北 - 中国 山西 - 中国 内蒙古 - 中国 辽宁 - 中国 吉林 - 中国 黑龙江 - 中国 上海 - 中国 江苏 - 中国 浙江 - 中国 安徽 - 中国 福建 - 中国 江西 - 中国 山东 - 中国 河南 - 中国 湖北 - 中国 湖南 - 中国 广东 - 中国 广西 - 中国 海南 - 中国 重庆 - 中国 四川 - 中国 贵州 - 中国 云南 - 中国 西藏 - 中国 陕西 - 中国 甘肃 - 中国 青海 - 中国 宁夏 - 中国 新疆 - 中国 澳门 - 中国 台湾 - 中国 香港  Example: - 广东,中国 上海,河北 秦皇岛,山西 长治 潞州区
            content_tag: Content category filter. Pass first-level or second-level category labels from Pugongying, separated by commas.  Available values: - 美妆: 整体妆容, 唇妆, 眼妆, 美甲, 底妆, 美妆合集, 香水, 美妆其他 - 护肤: 面部保养, 面部清洁, 护肤合集, 护肤其他 - 个人护理: 头发产品, 身体护理, 口腔护理, 护理其他 - 母婴: 母婴日常, 早教, 婴童用品, 婴童洗护, 婴童食品, 婴童时尚, 孕期穿搭, 孕产经验, 产后恢复, 育儿经验, 宝宝才艺, 宝宝写真, 母婴其他 - 时尚: 穿搭, 配饰, 发型, 箱包, 鞋靴, 时尚其他 - 美食: 美食教程, 美食探店, 美食展示, 美食测评, 吃播, 美食其他 - 家居家装: 装修, 家居用品, 家居装饰, 家具, 家电, 室内设计, 居家经验, 家居家装其他 - 影视综资讯: 动漫, 电影, 电视, 娱乐资讯, 影视, 民生资讯, 综艺, 影视综其他 - 运动健身: 健身减肥, 健身塑形, 滑雪, 滑板, 水上活动, 运动其他, 足球, 篮球, 跑步, 游泳 - 宠物: 猫, 狗, 动物其他 - 文化艺术: 社科, 文化, 艺术, 文化艺术其他 - 兴趣爱好: 绘画, 手工, 阅读, 文具手账, 舞蹈, 益智玩具, 潮流玩具, 兴趣爱好其他 - 生活记录: 接地气生活, 日常片段, 中外生活, 品质生活, 校园生活 - 教育: 大学教育, k12教育, 家庭教育, 学习日常, 职场教育, 教育其他 - 情感: 情感知识, 情感日常, 情感其他 - 摄影: 人文风光摄影, 摄影技巧, 胶片摄影, 人像摄影, 摄影其他 - 游戏: 手机游戏, 主机游戏, 游戏其他, 线下游戏 - 科技数码: 数码, 玩机攻略, 数码科技其他 - 出行: 城市出行, 户外, 旅行 - 音乐 - 搞笑 - 健康养生 - 汽车 - 婚嫁: 婚礼造型, 婚礼记录, 婚礼经验, 婚礼用品 - 商业财经 - 素材 - 其他
            content_scene_label: Content scene label filter. Pass full Pugongying note category scene label paths separated by English or Chinese commas.  Available values: - 汽车 理性决策 选车攻略 政策 - 汽车 理性决策 选车攻略 购车顾虑 - 汽车 理性决策 选车攻略 配置 - 汽车 理性决策 选车攻略 能源类型优势对比 - 汽车 理性决策 选车攻略 攻略 - 汽车 理性决策 新车测评 - 汽车 理性决策 探店试驾 - 汽车 理性决策 车主心得 - 汽车 用车场景 远行近游 近郊探索 - 汽车 用车场景 远行近游 长途自驾 - 汽车 用车场景 远行近游 硬核越野 - 汽车 用车场景 提车/交付场景 场地布置与礼遇 - 汽车 用车场景 提车/交付场景 仪式感记录 - 汽车 用车场景 商务用车 移动头等舱 - 汽车 用车场景 商务用车 商务接待 - 汽车 用车场景 亲子家庭 家庭采购日 - 汽车 用车场景 亲子家庭 接送孩子 - 汽车 用车场景 亲子家庭 三代同堂 - 汽车 用车场景 亲子家庭 周末溜娃 - 汽车 用车场景 亲子家庭 车内学习室 - 汽车 用车场景 亲子家庭 车内育婴室 - 汽车 用车场景 朋友社交 后备箱经济 - 汽车 用车场景 朋友社交 移动娱乐屋 - 汽车 用车场景 礼赠场景 毕业礼物 - 汽车 用车场景 礼赠场景 送给父母 - 汽车 用车场景 礼赠场景 适合送男友 - 汽车 用车场景 礼赠场景 适合送女友 - 汽车 用车场景 户外兴趣 钓鱼/野营 - 汽车 用车场景 户外兴趣 骑行 - 汽车 用车场景 户外兴趣 徒步 - 汽车 用车场景 户外兴趣 硬核竞速 - 汽车 用车场景 宠物出行 大型宠物 - 汽车 用车场景 宠物出行 短途出行 - 汽车 用车场景 宠物出行 小型宠物 - 汽车 用车场景 宠物出行 长途出行 - 汽车 用车场景 城市通勤 车内小憩 - 汽车 用车场景 城市通勤 健身储物 - 汽车 用车场景 城市通勤 日常通勤 - 汽车 用车场景 城市通勤 生活圈代步 - 汽车 用车场景 城市通勤 移动美容舱 - 汽车 个性化美化 个性改装 - 汽车 个性化美化 储物收纳 - 汽车 个性化美化 车内装饰 - 汽车 个性化美化 车外装饰 - 汽车 个性化美化 车衣保护 - 汽车 个性化美化 汽车用品 - 汽车 车型品类 轿车 - 汽车 车型品类 SUV - 汽车 车型品类 MPV - 汽车 车型品类 跑车 - 汽车 车型品类 微型车 - 汽车 车型品类 微面 - 汽车 车型品类 房车 - 汽车 车型品类 越野车 - 汽车 车型品类 旅行车 - 汽车 圈层属性 改装圈层 - 汽车 圈层属性 痛车圈层 - 汽车 圈层属性 跑山圈层 - 汽车 品牌倾向 自主 - 汽车 品牌倾向 豪华 - 汽车 品牌倾向 集团 - 汽车 品牌倾向 新势力 - 汽车 能源类型 纯电车 - 汽车 能源类型 新能源 - 汽车 能源类型 油车 - 汽车 人生阶段 单身 - 汽车 人生阶段 多娃&大家庭阶段 - 汽车 人生阶段 银发退休阶段 - 游戏 游戏品类 网页游戏 - 游戏 游戏品类 电脑游戏 - 游戏 游戏品类 手机游戏 - 游戏 游戏类型 动作格斗游戏 永劫无间 - 游戏 游戏类型 即时制二次元游戏 境界刀鸣 - 游戏 游戏类型 即时制二次元游戏 黑色信标 - 游戏 游戏类型 即时制二次元游戏 物华弥新 - 游戏 游戏类型 即时制二次元游戏 无期迷途 - 游戏 游戏类型 即时制二次元游戏 新月同行 - 游戏 游戏类型 即时制二次元游戏 绝区零 - 游戏 游戏类型 即时制角色扮演 诛仙2 - 游戏 游戏类型 即时制角色扮演 诛仙 - 游戏 游戏类型 即时制角色扮演 明日之后 - 游戏 游戏类型 即时制角色扮演 超自然行动组 - 游戏 游戏类型 即时制角色扮演 永恒之塔2 - 游戏 游戏类型 回合制二次元游戏 未定事件簿 - 游戏 游戏类型 回合制二次元游戏 雷索纳斯 - 游戏 游戏类型 回合制二次元游戏 浮生忆玲珑 - 游戏 游戏类型 回合制二次元游戏 重返未来1999 - 游戏 游戏类型 回合制角色扮演 梦幻西游手游 - 游戏 游戏类型 回合制角色扮演 龙魂旅人 - 游戏 游戏类型 回合制角色扮演 最终幻想14 - 游戏 游戏类型 塔防游戏 保卫向日葵 - 游戏 游戏类型 塔防游戏 全境守卫 - 游戏 游戏类型 塔防游戏 向僵尸开炮 - 游戏 游戏类型 开放世界角色扮演 燕云十六声 - 游戏 游戏类型 开放世界角色扮演 王者荣耀世界 - 游戏 游戏类型 恋爱游戏 如鸢 - 游戏 游戏类型 恋爱游戏 银与绯 - 游戏 游戏类型 恋爱游戏 时空中的绘旅人 - 游戏 游戏类型 恋爱游戏 光与夜之恋 - 游戏 游戏类型 恋爱游戏 恋与深空 - 游戏 游戏类型 恋爱游戏 恋与制作人 - 游戏 游戏类型 战略游戏 率土之滨 - 游戏 游戏类型 战略游戏 群星纪元 - 游戏 游戏类型 战略游戏 阿瓦隆之王 - 游戏 游戏类型 战略游戏 快来当领主 - 游戏 游戏类型 战略游戏 冒险之星 - 游戏 游戏类型 战略游戏 无尽的拉格朗日 - 游戏 游戏类型 放置类二次元游戏 花花与幕间剧 - 游戏 游戏类型 放置类角色扮演 发条总动员 - 游戏 游戏类型 放置类角色扮演 遮天凡尘一叶 - 游戏 游戏类型 模拟养成 美人传 - 游戏 游戏类型 模拟养成 盲盒派对 - 游戏 游戏类型 模拟养成 闪耀暖暖 - 游戏 游戏类型 模拟养成 以闪亮之名 - 游戏 游戏类型 模拟养成 无限暖暖 - 游戏 游戏类型 模拟家园建造 江南百景图 - 游戏 游戏类型 模拟家园建造 动物森友会 - 游戏 游戏类型 模拟家园建造 星露谷物语 - 游戏 游戏类型 模拟经营 暴吵萌厨 - 游戏 游戏类型 模拟经营 肥鹅健身房 - 游戏 游戏类型 模拟职业 杜拉拉升职记 - 游戏 游戏类型 消除游戏 四季合合 - 游戏 游戏类型 生存沙盒游戏 无尽冬日 - 游戏 游戏类型 聚会游戏 蛋仔派对 - 游戏 游戏类型 聚会游戏 代号砰砰 - 游戏 游戏类型 解谜游戏 晴空之下 - 游戏 游戏类型 抓宠类游戏 洛克王国手游 - 游戏 游戏类型 射击游戏 三角洲行动 - 游戏 游戏类型 射击游戏 codm（使命召唤） - 母婴 婴童洗护 安全防晒 - 母婴 婴童洗护 浴后护理 - 母婴 婴童洗护 敏感修护 - 母婴 婴童洗护 屏障树立 - 母婴 婴童洗护 泳后护理 - 母婴 婴童洗护 口周干裂 - 母婴 婴童洗护 分区清洁 - 母婴 婴童洗护 头皮问题 - 母婴 婴童洗护 驱虫驱蚊 - 母婴 婴童洗护 洁面清洁 - 母婴 婴童洗护 红屁股 - 母婴 婴童洗护 湿疹皮炎 - 母婴 婴童洗护 痱子热疹 - 母婴 婴童洗护 抚触链接 - 母婴 婴童洗护 趣味洗护 - 母婴 母婴纸品 精算育儿 - 母婴 母婴纸品 颜值派 - 母婴 母婴纸品 汗宝宝 - 母婴 母婴纸品 囤货党 - 母婴 母婴纸品 敏感肌 - 母婴 母婴纸品 肉腿娃 - 母婴 母婴纸品 功课党 - 母婴 母婴纸品 好动宝 - 母婴 母婴纸品 安睡整夜 - 母婴 母婴纸品 出行便携 - 母婴 母婴纸品 贵妇体验 - 母婴 母婴纸品 红屁屁 - 母婴 母婴小家电 空间收纳 - 母婴 母婴小家电 滋补养生 - 母婴 母婴小家电 温度把控 - 母婴 母婴小家电 夜奶操作 - 母婴 母婴小家电 新手喂养 - 母婴 母婴小家电 材质挑选 - 母婴 母婴小家电 三代同育 - 母婴 母婴小家电 户外喂养 - 母婴 母婴小家电 通乳攻略 - 母婴 母婴小家电 洁癖爸妈 - 母婴 母婴小家电 精准喂养 - 母婴 母婴小家电 职场妈妈 - 母婴 婴童辅食 吞咽能力 - 母婴 婴童辅食 多元辅食 - 母婴 婴童辅食 零食分享 - 母婴 婴童辅食 健康零食 - 母婴 婴童辅食 放学加餐 - 母婴 婴童辅食 出牙磨牙 - 母婴 婴童辅食 居家囤货 - 母婴 婴童辅食 节日礼包 - 母婴 婴童辅食 零食训练 - 母婴 婴童辅食 宝宝挑食 - 母婴 婴童辅食 户外零食 - 母婴 婴童辅食 低敏辅食 - 母婴 婴童辅食 入园社交 - 母婴 婴童辅食 居家辅食 - 母婴 婴童辅食 入园准备 - 母婴 婴童辅食 敏敏零食 - 母婴 婴童辅食 抓握训练 - 母婴 婴童辅食 外出口粮 - 母婴 婴童辅食 营养均衡 - 母婴 婴童辅食 自主进食 - 母婴 婴童辅食 第一口辅食 - 母婴 母婴营养品 开胃因子 - 母婴 母婴营养品 视力保护 - 母婴 母婴营养品 营养补充 - 母婴 母婴营养品 防护因子 - 母婴 母婴营养品 高钙因子 - 母婴 母婴营养品 自护构建 - 母婴 母婴营养品 发育表现 - 母婴 母婴营养品 助眠安睡 - 母婴 婴童奶粉 丝滑转奶 - 母婴 婴童奶粉 益生组合 - 母婴 婴童奶粉 眼脑体发育 - 母婴 婴童奶粉 选奶功课 - 母婴 婴童奶粉 防敏脱敏 - 母婴 婴童奶粉 助力聪明脑 - 母婴 婴童奶粉 乳铁自护 - 母婴 婴童奶粉 黄金长高 - 母婴 婴童奶粉 内修外护 - 母婴 婴童奶粉 肚肚吸收 - 母婴 婴童奶粉 断奶攻略 - 母婴 婴童奶粉 混合喂养 - 母婴 婴童奶粉 母源黄金HMO - 母婴 婴童奶粉 长肉多肉 - 母婴 哺乳喂养工具 萌娃穿搭 - 母婴 哺乳喂养工具 安全材质 - 母婴 哺乳喂养工具 奶瓶喂养 - 母婴 哺乳喂养工具 颜值发育 - 母婴 哺乳喂养工具 哄娃安抚 - 母婴 哺乳喂养工具 餐具选购 - 母婴 哺乳喂养工具 学饮指南 - 母婴 哺乳喂养工具 换季保温 - 母婴 母婴孕产 职场孕妇 - 母婴 母婴孕产 产后复工 - 母婴 母婴孕产 顺产 - 母婴 母婴孕产 孕期变化 - 母婴 母婴孕产 孕期学习 - 母婴 母婴孕产 剖腹产 - 母婴 母婴家居 护脊深睡 - 母婴 母婴家居 安全翻滚 - 母婴 母婴家居 进食习惯 - 母婴 母婴家居 早教启蒙 - 母婴 母婴家居 学习角落 - 母婴 母婴家居 自主入睡 - 母婴 母婴家居 爬行探索 - 母婴 母婴家居 防惊跳 - 母婴 母婴出行&用品 长线旅途 - 母婴 母婴出行&用品 户外探索 - 母婴 母婴出行&用品 二胎/双胎 - 母婴 母婴出行&用品 新贵消费 - 母婴 母婴出行&用品 备产研究 - 母婴 母婴出行&用品 短途旅行 - 母婴 母婴出行&用品 高频出行 - 母婴 母婴出行&用品 新生出行 - 母婴 母婴出行&用品 务实精算 - 母婴 母婴出行&用品 遛娃必备
            personal_tags: Blogger persona tag filter. Pass one or more Pugongying persona labels separated by English or Chinese commas.  Available values: - 妈妈 - 萌娃 - 爸爸 - 奶奶 - 情侣 - 夫妻 - 家庭 - 闺蜜 - 兄弟 - 备孕中 - 孕期中 - 12岁以上 - 传统行业 - 互联网 - 教育科研 - 金融法律 - 企业创业 - 时尚美妆 - 食品饮料 - 文化传媒 - 医疗健康 - 艺术设计 - 影视娱乐 - 运动健身 - 专业服务 - 工程师 - 销售 - HR - 教练 - 运动员 - 舞蹈老师 - 生活背景 - 备考经验 - 兴趣爱好 - 留学背景 - 海外华人 - 铲屎官 - 孕妈 - 独居人群 - 外国人 - 混血儿  Example: - 妈妈,教练,运动员,舞蹈老师,留学背景
            market_target: Marketing target filter. Pass one Pugongying marketing target value.  Available values: - estimateAllCpm: Exposure - exposure performance - cost - mAccumImpNum: Exposure - exposure performance - scale - readCost: Exposure - read performance - cost - mValidRawReadFeedNum: Exposure - read performance - scale - estimateEngageCost: Seeding - engagement performance - cost - mEngagementNum90d: Seeding - engagement performance - scale - estimateCpuv: Conversion - outer-store visit performance - cost - mCpuvNum: Conversion - outer-store visit performance - scale  Example: - estimateAllCpm
            audience_group: Audience target filter. Pass Pugongying audience group IDs (`dmpGroupId`) separated by English or Chinese commas. These IDs are dynamic and account-specific, so there is no fixed global value list. Use the audience group name shown in Pugongying Audience Management to identify what each ID means.  Example: - 123456,789012
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
            similar_user_id: Similar creator user ID. `similarUserId` and `similarWord` must be provided together.
            similar_word: Similar creator keyword shown by Pugongying. `similarUserId` and `similarWord` must be provided together.
            fans_location: Follower audience location filter. Pass Pugongying follower-region labels separated by English or Chinese commas. Country, China province, and city-level paths are supported; district/county-level paths are not accepted. Only paths present in the Pugongying follower-region tree are accepted. Use city paths such as `福建 南平`, `福建-南平`, or `中国 福建 南平`; they are normalized to values like `中国 福建 南平`.  Examples: - 福建 南平 - 中国 福建 南平,广东
        """
        return self._get(
            "/api/xiaohongshu-pgy/api/solar/cooperator/blogger/v2/v1",
            {
                "searchType": search_type,
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "fansNumberLower": fans_number_lower,
                "fansNumberUpper": fans_number_upper,
                "fansAge": fans_age,
                "fansGender": fans_gender,
                "fansChildAgeInfo": fans_child_age_info,
                "gender": gender,
                "location": location,
                "contentTag": content_tag,
                "contentSceneLabel": content_scene_label,
                "personalTags": personal_tags,
                "marketTarget": market_target,
                "audienceGroup": audience_group,
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
                "similarUserId": similar_user_id,
                "similarWord": similar_word,
                "fansLocation": fans_location,
            },
        )

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
