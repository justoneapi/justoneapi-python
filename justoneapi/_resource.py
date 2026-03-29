from __future__ import annotations

from typing import Any

from justoneapi._response import ApiResponse
from justoneapi._transport import Transport


class BaseResource:
    def __init__(self, transport: Transport):
        self._transport = transport

    def _get(self, path: str, params: dict[str, Any]) -> ApiResponse[Any]:
        return self._transport.get(path, params)
