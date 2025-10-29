from justoneapi.apis import request_util


class TikTokAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def get_user_post_v1(self, sec_uid: str, cursor: str, sort: str = None):
        url = f"{self.base_url}/api/tiktok/get-user-post/v1"
        params = {
            "token": self.token,
            "secUid": sec_uid,
            "cursor": cursor,
        }
        if sort:
            params["sort"] = sort
        return request_util.get_request(url, params)

    def get_post_detail_v1(self, post_id: str):
        url = f"{self.base_url}/api/tiktok/get-post-detail/v1"
        params = {
            "token": self.token,
            "postId": post_id,
        }
        return request_util.get_request(url, params)

    def get_user_detail_v1(self, unique_id: str = None, sec_uid: str = None):
        url = f"{self.base_url}/api/tiktok/get-user-detail/v1"
        params = {
            "token": self.token,
        }
        if unique_id:
            params["uniqueId"] = unique_id
        if sec_uid:
            params["secUid"] = sec_uid
        return request_util.get_request(url, params)

    def get_post_comment_v1(self, aweme_id, cursor: str = None):
        url = f"{self.base_url}/api/tiktok/get-post-comment/v1"
        params = {
            "token": self.token,
            "awemeId": aweme_id,
        }
        if cursor:
            params["cursor"] = cursor
        return request_util.get_request(url, params)

    def get_post_sub_comment_v1(self, aweme_id, comment_id: str, cursor: str = None):
        url = f"{self.base_url}/api/tiktok/get-post-sub-comment/v1"
        params = {
            "token": self.token,
            "awemeId": aweme_id,
            "commentId": comment_id,
        }
        if cursor:
            params["cursor"] = cursor
        return request_util.get_request(url, params)

    def search_user_v1(self, keyword, cursor: str = None, search_id: str = None):
        url = f"{self.base_url}/api/tiktok/search-user/v1"
        params = {
            "token": self.token,
            "keyword": keyword,
        }
        if cursor:
            params["cursor"] = cursor
        if search_id:
            params["searchId"] = search_id
        return request_util.get_request(url, params)

    def search_post_v1(self, keyword, cursor: str = None, search_id: str = None):
        url = f"{self.base_url}/api/tiktok/search-post/v1"
        params = {
            "token": self.token,
            "keyword": keyword,
        }
        if cursor:
            params["cursor"] = cursor
        if search_id:
            params["searchId"] = search_id
        return request_util.get_request(url, params)

