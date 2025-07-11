from justoneapi import config
from justoneapi.apis import request_util
from justoneapi.log import logger


class KuaishouAPI:
    def __init__(self, token):
        self.token = token

    def search_user_v2(self, keyword: str, page: int):
        url = f"{config.BASE_URL}/api/kuaishou/search-user/v2"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("users"):
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_user_video_list_v2(self, user_id: str, pcursor: str = None):
        url = f"{config.BASE_URL}/api/kuaishou/get-user-video-list/v2"
        params = {
            "token": self.token,
            "userId": user_id,
        }
        if pcursor:
            params["pcursor"] = pcursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("feeds"):
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_video_detail_v2(self, video_id: str):
        url = f"{config.BASE_URL}/api/kuaishou/get-video-detail/v2"
        params = {
            "token": self.token,
            "videoId": video_id,
        }
        return request_util.get_request(url, params)

    def search_video_v2(self, keyword: str, page: int):
        url = f"{config.BASE_URL}/api/kuaishou/search-video/v2"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("feeds"):
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_user_detail_v2(self, user_id: str):
        url = f"{config.BASE_URL}/api/kuaishou/get-user-detail/v1"
        params = {
            "token": self.token,
            "userId": user_id,
        }
        return request_util.get_request(url, params)

