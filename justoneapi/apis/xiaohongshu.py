from justoneapi import config
from justoneapi.apis import request_util
from justoneapi.log import logger


class XiaohongshuAPI:
    def __init__(self, token):
        self.token = token

    def get_user_v3(self, user_id: str):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-user/v3"
        params = {
            "token": self.token,
            "userId": user_id,
        }
        return request_util.get_request(url, params)

    def get_user_note_list_v4(self, user_id: str, last_cursor: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-user-note-list/v4"
        params = {
            "token": self.token,
            "userId": user_id,
        }
        if last_cursor:
            params["lastCursor"] = last_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                has_more = data.get("has_more")
                if has_more is not None and isinstance(has_more, bool) and has_more is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_note_detail_v7(self, note_id: str):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-detail/v7"
        params = {
            "token": self.token,
            "noteId": note_id,
        }
        return request_util.get_request(url, params)

    def get_note_detail_v8(self, note_id: str):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-detail/v8"
        params = {
            "token": self.token,
            "noteId": note_id,
        }
        return request_util.get_request(url, params)

    def get_note_comment_v2(self, note_id: str, last_cursor: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-comment/v2"
        params = {
            "token": self.token,
            "noteId": note_id,
        }
        if last_cursor:
            params["lastCursor"] = last_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                has_more = data.get("has_more")
                if has_more is not None and isinstance(has_more, bool) and has_more is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_note_comment_v3(self, note_id: str, last_cursor: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-comment/v3"
        params = {
            "token": self.token,
            "noteId": note_id,
        }
        if last_cursor:
            params["lastCursor"] = last_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                has_more = data.get("has_more")
                if has_more is not None and isinstance(has_more, bool) and has_more is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_note_sub_comment_v2(self, note_id: str, comment_id: str, last_cursor: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-sub-comment/v2"
        params = {
            "token": self.token,
            "noteId": note_id,
            "commentId": comment_id,
        }
        if last_cursor:
            params["lastCursor"] = last_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                has_more = data.get("has_more")
                if has_more is not None and isinstance(has_more, bool) and has_more is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_note_sub_comment_v3(self, note_id: str, comment_id: str, last_cursor: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-sub-comment/v3"
        params = {
            "token": self.token,
            "noteId": note_id,
            "commentId": comment_id,
        }
        if last_cursor:
            params["lastCursor"] = last_cursor

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                has_more = data.get("has_more")
                if has_more is not None and isinstance(has_more, bool) and has_more is True:
                    has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_note_v2(self, keyword: str, page: int, sort: str, note_type: str, note_time: str = None):
        url = f"{config.BASE_URL}/api/xiaohongshu/search-note/v2"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
            "sort": sort,
            "noteType": note_type,
        }
        if note_time:
            params["noteTime"] = note_time

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("items"):
                    has_more = data.get("has_more")
                    if has_more is None or (isinstance(has_more, bool) and has_more is True):
                        has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_note_v3(self, keyword: str, page: int, sort: str, note_type: str):
        url = f"{config.BASE_URL}/api/xiaohongshu/search-note/v3"
        params = {
            "token": self.token,
            "keyword": keyword,
            "page": page,
            "sort": sort,
            "noteType": note_type,
        }

        has_next_page = False
        result, data, message = request_util.get_request_page(url, params)
        try:
            if data:
                if data.get("items"):
                    has_more = data.get("has_more")
                    if has_more is None or (isinstance(has_more, bool) and has_more is True):
                        has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def search_user_v2(self, keyword: str, page: int):
        url = f"{config.BASE_URL}/api/xiaohongshu/search-user/v2"
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
                    has_more = data.get("has_more")
                    if has_more is None or (isinstance(has_more, bool) and has_more is True):
                        has_next_page = True
        except Exception as e:
            logger.warning(f"Pagination parse error at {url}. Contact us to fix it.")
        return result, data, message, has_next_page

    def get_note_feed_v1(self, oid: str, page: int):
        url = f"{config.BASE_URL}/api/xiaohongshu/get-note-feed/v1"
        params = {
            "token": self.token,
            "oid": oid,
            "page": page,
        }
        return request_util.get_request(url, params)

