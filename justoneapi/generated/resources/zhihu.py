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
        Column Article Details

        Get Zhihu column Article Details data, including title, author, and content, for article archiving and content research.

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
        Answer List

        Get Zhihu answer List data, including answer content, author profiles, and interaction metrics, for question analysis and answer research.

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
        Keyword Search

        Get Zhihu keyword Search data, including matched results, metadata, and ranking signals, for topic discovery and content research.

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
        Column Article List

        Get Zhihu column Article List data, including article metadata and list ordering, for column monitoring and content collection.

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
