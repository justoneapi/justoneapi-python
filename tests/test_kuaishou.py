import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestKuaishouAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_search_user_v2(self):
        result, data, message, has_next_page = self.client.kuaishou.search_user_v2(keyword="deepseek", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_video_list_v2(self):
        result, data, message, has_next_page = self.client.kuaishou.get_user_video_list_v2(user_id="1052294368")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_video_detail_v2(self):
        result, data, message = self.client.kuaishou.get_video_detail_v2(video_id="3x22wb9mi5km2zw")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_video_v2(self):
        result, data, message, has_next_page = self.client.kuaishou.search_video_v2(keyword="deepseek", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_detail_v2(self):
        result, data, message = self.client.kuaishou.get_user_detail_v2(user_id="1052294368")
        if result:
            print(json.dumps(data, ensure_ascii=False))
