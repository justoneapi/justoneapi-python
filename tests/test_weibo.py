import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestWeiboAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_search_all_v2(self):
        result, data, message, has_next_page = self.client.weibo.search_all_v2(q="deepseek", start_day="2025-07-01",
                                                                               start_hour=1, end_day="2025-07-02",
                                                                               end_hour="14", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_all_v3(self):
        result, data, message, has_next_page = self.client.weibo.search_all_v3(q="deepseek", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_weibo_detail_v1(self):
        result, data, message = self.client.weibo.get_weibo_detail_v1(id="5062665714010525")
        if result:
            print(json.dumps(data, ensure_ascii=False))
