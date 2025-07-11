from justoneapi import config
from justoneapi.apis import request_util


class UserAPI:
    def __init__(self, token):
        self.token = token

    def get_balance(self):
        url = f"{config.BASE_URL}/user/get-balance"
        params = {
            "token": self.token,
        }
        return request_util.get_request(url, params)

    def get_record(self, order_year: int, order_month: int):
        url = f"{config.BASE_URL}/user/get-record"
        params = {
            "token": self.token,
            "orderYear": order_year,
            "orderMonth": order_month,
        }
        return request_util.get_request(url, params)
