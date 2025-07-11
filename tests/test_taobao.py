import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestTaobaoAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_item_detail_v1(self):
        result, data, message = self.client.taobao.get_item_detail_v1(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_detail_v2(self):
        result, data, message = self.client.taobao.get_item_detail_v2(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_detail_v3(self):
        result, data, message = self.client.taobao.get_item_detail_v3(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_detail_v4(self):
        result, data, message = self.client.taobao.get_item_detail_v4(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_detail_v5(self):
        result, data, message = self.client.taobao.get_item_detail_v5(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_comment_v6(self):
        result, data, message, has_next_page = self.client.taobao.get_item_comment_v6(item_id="765880060015", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_comment_v7(self):
        result, data, message, has_next_page = self.client.taobao.get_item_comment_v7(item_id="765880060015", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_social_feed_v1(self):
        result, data, message, has_next_page = self.client.taobao.get_social_feed_v1(item_id="765880060015", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_shop_item_list_v9(self):
        result, data, message, has_next_page = self.client.taobao.get_shop_item_list_v9(user_id="880734502",
                                                                                        shop_id="71720200",
                                                                                        sort="_sale", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_get_item_sale_v5(self):
        result, data, message = self.client.taobao.get_item_sale_v5(item_id="765880060015")
        if result:
            print(json.dumps(data, ensure_ascii=False))

    def test_search_item_list_v6(self):
        result, data, message, has_next_page = self.client.taobao.search_item_list_v6(keyword="deepseek", sort="_sale", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))
