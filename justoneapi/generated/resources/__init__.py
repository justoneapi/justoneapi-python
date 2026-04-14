from __future__ import annotations

from justoneapi.generated.resources.amazon import AmazonResource
from justoneapi.generated.resources.beike import BeikeResource
from justoneapi.generated.resources.bilibili import BilibiliResource
from justoneapi.generated.resources.douban import DoubanResource
from justoneapi.generated.resources.douyin import DouyinResource
from justoneapi.generated.resources.douyin_ec import DouyinEcResource
from justoneapi.generated.resources.douyin_xingtu import DouyinXingtuResource
from justoneapi.generated.resources.facebook import FacebookResource
from justoneapi.generated.resources.imdb import ImdbResource
from justoneapi.generated.resources.instagram import InstagramResource
from justoneapi.generated.resources.jd import JdResource
from justoneapi.generated.resources.kuaishou import KuaishouResource
from justoneapi.generated.resources.reddit import RedditResource
from justoneapi.generated.resources.search import SearchResource
from justoneapi.generated.resources.taobao import TaobaoResource
from justoneapi.generated.resources.tiktok import TiktokResource
from justoneapi.generated.resources.tiktok_shop import TiktokShopResource
from justoneapi.generated.resources.toutiao import ToutiaoResource
from justoneapi.generated.resources.twitter import TwitterResource
from justoneapi.generated.resources.web import WebResource
from justoneapi.generated.resources.weibo import WeiboResource
from justoneapi.generated.resources.weixin import WeixinResource
from justoneapi.generated.resources.xiaohongshu import XiaohongshuResource
from justoneapi.generated.resources.xiaohongshu_pgy import XiaohongshuPgyResource
from justoneapi.generated.resources.youku import YoukuResource
from justoneapi.generated.resources.youtube import YoutubeResource
from justoneapi.generated.resources.zhihu import ZhihuResource

RESOURCE_CLASSES = {
    "amazon": AmazonResource,
    "beike": BeikeResource,
    "bilibili": BilibiliResource,
    "douban": DoubanResource,
    "douyin": DouyinResource,
    "douyin_ec": DouyinEcResource,
    "douyin_xingtu": DouyinXingtuResource,
    "facebook": FacebookResource,
    "imdb": ImdbResource,
    "instagram": InstagramResource,
    "jd": JdResource,
    "kuaishou": KuaishouResource,
    "reddit": RedditResource,
    "search": SearchResource,
    "taobao": TaobaoResource,
    "tiktok": TiktokResource,
    "tiktok_shop": TiktokShopResource,
    "toutiao": ToutiaoResource,
    "twitter": TwitterResource,
    "web": WebResource,
    "weibo": WeiboResource,
    "weixin": WeixinResource,
    "xiaohongshu": XiaohongshuResource,
    "xiaohongshu_pgy": XiaohongshuPgyResource,
    "youku": YoukuResource,
    "youtube": YoutubeResource,
    "zhihu": ZhihuResource,
}

__all__ = [
    "AmazonResource",
    "BeikeResource",
    "BilibiliResource",
    "DoubanResource",
    "DouyinResource",
    "DouyinEcResource",
    "DouyinXingtuResource",
    "FacebookResource",
    "ImdbResource",
    "InstagramResource",
    "JdResource",
    "KuaishouResource",
    "RedditResource",
    "SearchResource",
    "TaobaoResource",
    "TiktokResource",
    "TiktokShopResource",
    "ToutiaoResource",
    "TwitterResource",
    "WebResource",
    "WeiboResource",
    "WeixinResource",
    "XiaohongshuResource",
    "XiaohongshuPgyResource",
    "YoukuResource",
    "YoutubeResource",
    "ZhihuResource",
    "RESOURCE_CLASSES",
]
