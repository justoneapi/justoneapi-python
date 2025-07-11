import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestDouyinAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_user_detail_v3(self):
        result, data, message = self.client.douyin.get_user_detail_v3(
            sec_uid="MS4wLjABAAAAwxn90DEjJIMYK1Em-vB2mgijIsVhnYrIgKlQdZU0bE4g-HrLIab8PZ7fqo8R0hvw")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_user_video_list_v3(self):
        result, data, message, has_next_page = self.client.douyin.get_user_video_list_v3(
            sec_uid="MS4wLjABAAAAwxn90DEjJIMYK1Em-vB2mgijIsVhnYrIgKlQdZU0bE4g-HrLIab8PZ7fqo8R0hvw", max_cursor=0)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_video_detail_v2(self):
        result, data, message = self.client.douyin.get_video_detail_v2(video_id="7428906452091145483")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_video_v4(self):
        result, data, message, has_next_page = self.client.douyin.search_video_v4(keyword="deepseek", sort_type="_0",
                                                                                  publish_time="_0", duration="_0",
                                                                                  page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_user_v2(self):
        result, data, message, has_next_page = self.client.douyin.search_user_v2(keyword="deepseek", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_video_comment_v1(self):
        result, data, message, has_next_page = self.client.douyin.get_video_comment_v1(aweme_id="7428906452091145483",
                                                                                       page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_video_sub_comment_v1(self):
        result, data, message, has_next_page = self.client.douyin.get_video_sub_comment_v1(comment_id="7428923938056471355",
                                                                                       page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))
