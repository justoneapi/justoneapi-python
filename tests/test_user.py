import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestUserAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_balance(self):
        result, data, message = self.client.user.get_balance()
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_record(self):
        result, data, message = self.client.user.get_record(order_year=2025, order_month=7)
        if result:
            print(json.dumps(data, ensure_ascii=False))
