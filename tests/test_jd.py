import json
import os
from unittest import TestCase

from justoneapi.client import JustOneAPIClient


class TestJdAPI(TestCase):
    client = JustOneAPIClient(token=os.environ.get("JUSTONEAPI_TOKEN"))

    def test_get_item_detail_v1(self):
        result, data, message = self.client.jd.get_item_detail_v1(item_id="10151656101707")
        if result:
            print(json.dumps(data, ensure_ascii=False))
