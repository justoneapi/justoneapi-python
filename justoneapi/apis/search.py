from justoneapi.apis import request_util
from justoneapi.log import logger


class SearchAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def search_v1(self, keyword: str = None, source: str = None, start: str = None, end: str = None, next_cursor: str = None):
        url = f"{self.base_url}/api/search/v1"
        params = {
            "token": self.token,
        }
        if keyword:
            params["keyword"] = keyword
        if source:
            params["source"] = source
        if start:
            params["start"] = start
        if end:
            params["end"] = end
        if next_cursor:
            params["nextCursor"] = next_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data.get("nextCursor"):
                has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page
