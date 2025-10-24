from justoneapi.apis import request_util


class JdAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url

    def get_item_detail_v1(self, item_id: str):
        url = f"{self.base_url}/api/jd/get-item-detail/v1"
        params = {
            "token": self.token,
            "itemId": item_id,
        }
        return request_util.get_request(url, params)

