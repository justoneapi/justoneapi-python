from justoneapi import config
from justoneapi.apis import request_util
from justoneapi.log import logger


class DouyinAPI:
    def __init__(self, token):
        self.token = token

    def get_user_detail_v3(self, sec_uid: str):
        url = f"{config.BASE_URL}/api/douyin/get-user-detail/v3"
        params = {
            "token": self.token,
            "secUid": sec_uid,
        }
        return request_util.get_request(url, params)

    def get_user_video_list_v3(self, sec_uid: str, max_cursor: int):
        url = f"{config.BASE_URL}/api/douyin/get-user-video-list/v3"
        params = {
            "token": self.token,
            "secUid": sec_uid,
            "maxCursor": max_cursor,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("has_more") == 1:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_video_detail_v2(self, video_id: str):
        url = f"{config.BASE_URL}/api/douyin/get-video-detail/v2"
        params = {
            "token": self.token,
            "videoId": video_id,
        }
        return request_util.get_request(url, params)

    def search_video_v4(self, keyword: str, sort_type: str, publish_time: str, duration: str, page: int, search_id: str = None):
        url = f"{config.BASE_URL}/api/douyin/search-video/v4"
        params = {
            "token": self.token,
            "keyword": keyword,
            "sortType": sort_type,
            "publishTime": publish_time,
            "duration": duration,
            "page": page,
        }
        if search_id:
            params["searchId"] = search_id

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("business_config", {}).get("has_more", 0) == 1:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_user_v2(self, keyword: str, page: int, user_type: str = None):
        url = f"{config.BASE_URL}/api/douyin/search-user/v2"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
        }
        if user_type:
            params["userType"] = user_type

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("business_config", {}).get("has_more", 0) == 1:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_video_comment_v1(self, aweme_id: str, page: int):
        url = f"{config.BASE_URL}/api/douyin/get-video-comment/v1"
        params = {
            "token": self.token,
            "awemeId": aweme_id,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("has_more") == 1:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_video_sub_comment_v1(self, comment_id: str, page: int):
        url = f"{config.BASE_URL}/api/douyin/get-video-sub-comment/v1"
        params = {
            "token": self.token,
            "commentId": comment_id,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("has_more") == 1:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page
