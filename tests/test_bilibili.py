import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestBilibiliAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_video_detail_v2(self):
        result, data, message = self.client.bilibili.get_video_detail_v2(bvid="BV1vk4y1S7dV")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_video_list_v2(self):
        result, data, message, has_next_page = self.client.bilibili.get_user_video_list_v2(uid="559186307")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_detail_v2(self):
        result, data, message = self.client.bilibili.get_user_detail_v2(uid="559186307")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_video_comment_v2(self):
        result, data, message, has_next_page = self.client.bilibili.get_video_comment_v2(aid="1401344783", cursor="3")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_video_v2(self):
        result, data, message, has_next_page = self.client.bilibili.search_video_v2(keyword="deepseek", page=50)
        if result:
            print(json.dumps(data, ensure_ascii=False))
