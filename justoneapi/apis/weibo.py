from justoneapi import config
from justoneapi.apis import request_util
from justoneapi.log import logger


class WeiboAPI:
    def __init__(self, token):
        self.token = token

    def search_all_v2(self, q: str, start_day: str, start_hour: int, end_day: str, end_hour: int, page: int):
        url = f"{config.BASE_URL}/api/weibo/search-all/v2"
        params = {
            "token": self.token,
            "q": q,
            "startDay": start_day,
            "startHour": start_hour,
            "endDay": end_day,
            "endHour": end_hour,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("has_next_page", False) is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_all_v3(self, q: str, page: int):
        url = f"{config.BASE_URL}/api/weibo/search-all/v3"
        params = {
            "token": self.token,
            "q": q,
            "page": page,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("cards"):
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_weibo_detail_v1(self, id: str):
        url = f"{config.BASE_URL}/api/weibo/get-weibo-detail/v1"
        params = {
            "token": self.token,
            "id": id,
        }
        return request_util.get_request(url, params)

