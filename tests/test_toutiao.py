import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestToutiaoAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_search_v1(self):
        result, data, message, has_next_page = self.client.toutiao.search_v1(keyword="个人公积金", page=1)
        if result:
            print(json.dumps(data, ensure_ascii=False))
