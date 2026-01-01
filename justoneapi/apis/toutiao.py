from justoneapi.apis import request_util
from justoneapi.log import logger


class ToutiaoAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def search_v1(self, keyword: str, page: int, search_id: str = None):
        url = f"{self.base_url}/api/toutiao/search/v1"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
        }
        if search_id:
            params["searchId"] = search_id

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("search_id"):
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page
