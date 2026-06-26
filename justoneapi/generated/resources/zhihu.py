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
        show_all_topics: str | None = "FALSE",
        vertical: str | None = None,
        sort: str | None = None,
        time_interval: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Keyword Search

        Get Zhihu keyword Search data, including matched results, metadata, and ranking signals, for topic discovery and content research.

        Args:
            keyword: Search keywords.
            offset: Start offset, begins with 0.
            show_all_topics: Whether to show all topics.  Available Values: - `FALSE`: Do not show topics. - `TRUE`: Show all topics.
            vertical: Result type filter.  Available Values: - `answer`: Answers only. - `article`: Articles only. - `zvideo`: Videos only.
            sort: Sorting criteria.  Available Values: - `upvoted_count`: Most upvoted. - `created_time`: Latest published.
            time_interval: Publish time interval filter.  Available Values: - `a_day`: Within one day. - `a_week`: Within one week. - `a_month`: Within one month. - `three_months`: Within three months. - `half_a_year`: Within half a year. - `a_year`: Within one year.
        """
        return self._get(
            "/api/zhihu/search/v1",
            {
                "keyword": keyword,
                "offset": offset,
                "showAllTopics": show_all_topics,
                "vertical": vertical,
                "sort": sort,
                "timeInterval": time_interval,
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

    def get_user_info_v1(
        self,
        *,
        user_url_token: str,
    ) -> ApiResponse[Any]:
        """
        User Info

        Get Zhihu user Info data, including profile identifiers, names, avatar information, headline details, follower signals, and account metadata for creator profiling, audience research, and account verification workflows.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
        """
        return self._get(
            "/api/zhihu/get-user-info/v1",
            {
                "userUrlToken": user_url_token,
            },
        )

    def get_user_followees_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Followees

        Get Zhihu user Followees data, including followed account profiles, identifiers, headlines, avatar fields, and pagination metadata for network mapping, creator discovery, and relationship analysis.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-followees/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_followers_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Followers

        Get Zhihu user Followers data, including follower account profiles, identifiers, headlines, avatar fields, and pagination metadata for audience analysis, creator evaluation, and relationship mapping.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-followers/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_articles_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
        sort_type: str | None = "created",
    ) -> ApiResponse[Any]:
        """
        User Articles

        Get Zhihu user Articles data, including article identifiers, titles, author context, engagement signals, publish metadata, and pagination fields for creator research and content monitoring.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
            sort_type: Sorting criteria for user articles.  Available Values: - `created`: Sort by publish time. - `voteups`: Sort by upvote count.
        """
        return self._get(
            "/api/zhihu/get-user-articles/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
                "sortType": sort_type,
            },
        )

    def get_user_included_articles_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Included Articles

        Get Zhihu user Included Articles data, including collected article identifiers, titles, author context, engagement signals, publish metadata, and pagination fields for content research and archive tracking.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-included-articles/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_follow_columns_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Follow Columns

        Get Zhihu user Follow Columns data, including subscribed column identifiers, names, descriptions, creator context, follower signals, and pagination fields for creator research and topic monitoring.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-follow-columns/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_follow_questions_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Follow Questions

        Get Zhihu user Follow Questions data, including followed question identifiers, titles, answer counts, follower signals, update metadata, and pagination fields for topic tracking and research workflows.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-follow-questions/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_follow_collections_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Follow Collections

        Get Zhihu user Follow Collections data, including followed collection identifiers, titles, creator context, item counts, follower signals, and pagination fields for collection tracking and content research.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-follow-collections/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )

    def get_user_follow_topics_v1(
        self,
        *,
        user_url_token: str,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Follow Topics

        Get Zhihu user Follow Topics data, including followed topic identifiers, names, descriptions, follower signals, content counts, and pagination fields for topic monitoring and audience research.

        Args:
            user_url_token: Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.
            offset: Start offset, begins with 0.
        """
        return self._get(
            "/api/zhihu/get-user-follow-topics/v1",
            {
                "userUrlToken": user_url_token,
                "offset": offset,
            },
        )
