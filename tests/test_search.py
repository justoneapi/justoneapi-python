import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestSearchAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_search_v1(self):
        result, data, message, has_next_page = self.client.search.search_v1(keyword="deepseek", source="XIAOHONGSHU", start="2025-07-10 00:00:00", end="2025-08-10 00:00:00")
        if result:
            print(json.dumps(data, ensure_ascii=False))
