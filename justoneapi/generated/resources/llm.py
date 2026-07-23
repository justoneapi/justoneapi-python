from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class LlmResource(BaseResource):
    """Generated resource for LLM."""

    def doubao_answer_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Doubao Answer

        Requests a Doubao web answer for a submitted keyword or question. Use it to collect a generated answer for research and information-gathering workflows.

        Args:
            keyword: Keyword or question to ask Doubao.
        """
        return self._get(
            "/api/llm/doubao-answer/v1",
            {
                "keyword": keyword,
            },
        )
