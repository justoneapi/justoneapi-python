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

        Retrieve details for a Zhihu column article identified by article ID. Use it to inspect a known article for reading, review, or archiving.

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

        Retrieve answers for a Zhihu question with sorting and pagination controls. Use it to browse responses to a known question and continue through additional answer pages.

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

        Search Zhihu by keyword with optional result-type, sort, time-interval, topic-display, and offset controls. Use it to find relevant answers, articles, or videos.

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

        Retrieve articles from a Zhihu column with offset pagination. Use it to browse a known column's publication history and select articles for detail lookup.

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

        Retrieve the public profile for a Zhihu user identified by URL token. Use it to inspect an account found through Zhihu content or relationship data.

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

        Retrieve accounts followed by a Zhihu user, with offset pagination. Use it to explore the outgoing connections of a known account.

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

        Retrieve accounts that follow a Zhihu user, with offset pagination. Use it to explore the audience connections of a known account.

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

        Retrieve articles published by a Zhihu user with offset pagination and publish-time or upvote sorting. Use it to browse a creator's articles in the selected order.

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

        Retrieve the included-article records exposed for a Zhihu user, with offset pagination. Use it to browse that account's included-article list.

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

        Retrieve Zhihu columns followed by a user, with offset pagination. Use it to browse the columns associated with a known account's follow activity.

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

        Retrieve Zhihu questions followed by a user, with offset pagination. Use it to browse the questions associated with a known account's follow activity.

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

        Retrieve Zhihu collections followed by a user, with offset pagination. Use it to browse the collections associated with a known account's follow activity.

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

        Retrieve Zhihu topics followed by a user, with offset pagination. Use it to browse the topics associated with a known account's follow activity.

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

    def get_answer_comments_v1(
        self,
        *,
        answer_id: str,
        order_by: str | None = "score",
        offset: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Answer Comments

        Retrieve comments for a Zhihu answer with hottest or latest sorting and offset pagination. Use it to review discussion around a known answer and continue through additional comment pages.

        Args:
            answer_id: Answer ID
            order_by: Sorting order for comments.  Available Values: - `score`: Sort by highest score. - `ts`: Sort by latest time.
            offset: Pagination offset from the previous result.
        """
        return self._get(
            "/api/zhihu/get-answer-comments/v1",
            {
                "answerId": answer_id,
                "orderBy": order_by,
                "offset": offset,
            },
        )

    def get_comment_replies_v1(
        self,
        *,
        comment_id: str,
        order_by: str | None = "score",
        offset: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Comment Replies

        Retrieve replies to a Zhihu comment with hottest or latest sorting and offset pagination. Use it to follow discussion under a known comment and continue through additional reply pages.

        Args:
            comment_id: Comment ID
            order_by: Sorting order for replies.  Available Values: - `score`: Sort by highest score. - `ts`: Sort by latest time.
            offset: Pagination offset from the previous result.
        """
        return self._get(
            "/api/zhihu/get-comment-replies/v1",
            {
                "commentId": comment_id,
                "orderBy": order_by,
                "offset": offset,
            },
        )
