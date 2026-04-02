from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ZhihuResource(BaseResource):
    """Generated resource for Zhihu."""

    def get_column_article_detail_v1(
        self,
        *,
        id_: str,
    ) -> ApiResponse[Any]:
        """
        Column Article Details (V1)

        Retrieve detailed information for a specific Zhihu Column article by its article ID.

        Typical use cases:
        - In-depth content analysis of professional articles.
        - Creator performance evaluation and topic trend monitoring.

        Args:
            id_: Article ID
        """
        return self._get(
            "/api/zhihu/get-column-article-detail/v1",
            {
                "id": id_,
            },
        )

    def get_answer_list_v1(
        self,
        *,
        question_id: str,
        cursor: str | None = "",
        offset: int | None = 0,
        order: str | None = "_updated",
        session_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Answer List (V1)

        Retrieve the list of answers under a specific Zhihu question by its question ID.

        Typical use cases:
        - Analyzing user opinions and extracting high-quality responses.
        - Studying community engagement and topic discussions.

        Args:
            question_id: Question ID
            cursor: Pagination cursor from previous result.
            offset: Start offset, begins with 0.
            order: Sorting criteria for answers.  Available Values: - `_default`: Default sorting. - `_updated`: Sorted by updated time.
            session_id: Session ID from previous result.
        """
        return self._get(
            "/api/zhihu/get-answer-list/v1",
            {
                "questionId": question_id,
                "cursor": cursor,
                "offset": offset,
                "order": order,
                "sessionId": session_id,
            },
        )

    def search_v1(
        self,
        *,
        keyword: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Search (V1)

        Search for Zhihu content (including questions, answers, and articles) by keyword.

        Typical use cases:
        - Topic discovery and competitive brand monitoring.
        - Identifying trending discussions and high-value creators.

        Args:
            keyword: Search keywords.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/search/v1",
            {
                "keyword": keyword,
                "offset": offset,
            },
        )

    def get_column_article_list_v1(
        self,
        *,
        column_id: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Column Article List (V1)

        Retrieve the list of articles published under a specific Zhihu Column by its column ID.

        Typical use cases:
        - Tracking creator output and analyzing column performance.
        - Knowledge aggregation based on specific topics.

        Args:
            column_id: Column ID
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-column-article-list/v1",
            {
                "columnId": column_id,
                "offset": offset,
            },
        )
