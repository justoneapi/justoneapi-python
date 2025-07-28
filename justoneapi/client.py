from justoneapi import config
from justoneapi.apis.bilibili import BilibiliAPI
from justoneapi.apis.douyin import DouyinAPI
from justoneapi.apis.kuaishou import KuaishouAPI
from justoneapi.apis.taobao import TaobaoAPI
from justoneapi.apis.user import UserAPI
from justoneapi.apis.weibo import WeiboAPI
from justoneapi.apis.xiaohongshu import XiaohongshuAPI


class JustOneAPIClient:
    def __init__(self, token: str, env: str = "cn"):
        if not token:
            raise ValueError("Token is required. Please contact us to obtain one.")
        self.token = token
        if env == "cn":
            self.base_url = config.BASE_URL_CN
        elif env == "global":
            self.base_url = config.BASE_URL_GLOBAL
        else:
            raise ValueError("env must be 'cn' or 'global'.")
        self.user = UserAPI(self.token, self.base_url)
        self.taobao = TaobaoAPI(self.token, self.base_url)
        self.xiaohongshu = XiaohongshuAPI(self.token, self.base_url)
        self.douyin = DouyinAPI(self.token, self.base_url)
        self.kuaishou = KuaishouAPI(self.token, self.base_url)
        self.weibo = WeiboAPI(self.token, self.base_url)
        self.bilibili = BilibiliAPI(self.token, self.base_url)
