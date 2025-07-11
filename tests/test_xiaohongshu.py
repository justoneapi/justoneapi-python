import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestXiaohongshuAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_user_v3(self):
        result, data, message = self.client.xiaohongshu.get_user_v3(user_id="5da13fc8000000000100b68a")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_note_list_v4(self):
        result, data, message, has_next_page = self.client.xiaohongshu.get_user_note_list_v4(
            user_id="5da13fc8000000000100b68a")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_note_detail_v7(self):
        result, data, message = self.client.xiaohongshu.get_note_detail_v7(note_id="685e7cdf000000000d0253a5")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_note_comment_v2(self):
        result, data, message, has_next_page = self.client.xiaohongshu.get_note_comment_v2(
            note_id="6868f8530000000020018dea")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_note_sub_comment_v2(self):
        result, data, message, has_next_page = self.client.xiaohongshu.get_note_sub_comment_v2(
            note_id="6868f8530000000020018dea", comment_id="686b315e000000002002d1b9")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_note_v2(self):
        result, data, message, has_next_page = self.client.xiaohongshu.search_note_v2(keyword="deepseek", page=1,
                                                                                      sort="general", note_type="_0")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_user_v2(self):
        result, data, message, has_next_page = self.client.xiaohongshu.search_user_v2(keyword="cat", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_note_feed_v1(self):
        result, data, message = self.client.xiaohongshu.get_note_feed_v1(oid="homefeed_recommend", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))
