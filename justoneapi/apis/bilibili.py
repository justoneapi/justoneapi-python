from justoneapi import config
from justoneapi.apis import request_util
from justoneapi.log import logger


class BilibiliAPI:
    def __init__(self, token):
        self.token = token

    def get_video_detail_v2(self, bvid: str):
        url = f"{config.BASE_URL}/api/bilibili/get-video-detail/v2"
        params = {
            "token": self.token,
            "bvid": bvid,
        }
        return request_util.get_request(url, params)

    def get_user_video_list_v2(self, uid: str, aid: str = None):
        url = f"{config.BASE_URL}/api/bilibili/get-user-video-list/v2"
        params = {
            "token": self.token,
            "uid": uid,
        }
        if aid:
            params["aid"] = aid

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("data", {}).get("has_next", False) is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_user_detail_v2(self, uid: str):
        url = f"{config.BASE_URL}/api/bilibili/get-user-detail/v2"
        params = {
            "token": self.token,
            "uid": uid,
        }
        return request_util.get_request(url, params)

    def get_video_comment_v2(self, aid: str, cursor: str = None):
        url = f"{config.BASE_URL}/api/bilibili/get-video-comment/v2"
        params = {
            "token": self.token,
            "aid": aid,
        }
        if cursor:
            params["cursor"] = cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("data", {}).get("has_next", False) is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_video_v2(self, keyword: str, page: int):
        url = f"{config.BASE_URL}/api/bilibili/search-video/v2"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("data", {}).get("result"):
                    if page < data.get("data", {}).get("numPages", 0):
                        has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

