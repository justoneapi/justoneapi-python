from justoneapi.apis.bilibili import BilibiliAPI
from justoneapi.apis.douyin import DouyinAPI
from justoneapi.apis.kuaishou import KuaishouAPI
from justoneapi.apis.taobao import TaobaoAPI
from justoneapi.apis.user import UserAPI
from justoneapi.apis.weibo import WeiboAPI
from justoneapi.apis.xiaohongshu import XiaohongshuAPI


class JustOneAPIClient:
    def __init__(self, token: str):
        if not token:
            raise ValueError("Token is required. Please contact us to obtain one.")
        self.token = token
        self.user = UserAPI(self.token)
        self.taobao = TaobaoAPI(self.token)
        self.xiaohongshu = XiaohongshuAPI(self.token)
        self.douyin = DouyinAPI(self.token)
        self.kuaishou = KuaishouAPI(self.token)
        self.weibo = WeiboAPI(self.token)
        self.bilibili = BilibiliAPI(self.token)
