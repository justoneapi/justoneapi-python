from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuResource(BaseResource):
    """Generated resource for Xiaohongshu (RedNote)."""

    def hot_search_v1(
        self,
        *,
        search_word: str | None = "",
        page_num: int | None = 1,
        order_by: str | None = "premium_imp_num",
        nd: str | None = "DAY_7",
    ) -> ApiResponse[Any]:
        """
        Hot Search

        Searches Xiaohongshu (RedNote) hot-content entries with optional keyword, pagination, ranking metric, and time-range controls. Use it to support trend discovery, topic monitoring, and content planning.

        Args:
            search_word: Search keyword.
            page_num: Page number for pagination.
            order_by: Sort metric for the result set.  Available Values: - `premium_imp_num`: Exposure - `premium_good_read_rate`: Read rate - `premium_read_num`: Read count - `premium_engage_num`: Engagement count - `premium_engage_rate`: Engagement rate - `premium_like_num`: Like count - `premium_fav_num`: Favorite count - `premium_cmt_num`: Comment count
            nd: Time range in days.  Available Values: - `DAY_3`: Last 3 days - `DAY_7`: Last 7 days - `DAY_14`: Last 14 days - `DAY_30`: Last 30 days
        """
        return self._get(
            "/api/xiaohongshu/hot-search/v1",
            {
                "searchWord": search_word,
                "pageNum": page_num,
                "orderBy": order_by,
                "nd": nd,
            },
        )

    def hot_list_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Hot List

        Retrieves the current Xiaohongshu (RedNote) hot list for platform trend monitoring and content research. Use it to review current hot-list entries before deeper analysis.
        """
        return self._get(
            "/api/xiaohongshu/hot-list/v1",
            {},
        )

    def search_note_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
        note_time: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Note Search

        Searches Xiaohongshu (RedNote) notes by keyword with pagination plus sort, note-type, and publish-time filters. Use it to support topic research, content discovery, and monitoring keyword-related posts.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter. Results may include notes published outside the selected time range.  Available Values: - `ONE_DAY`: Within one day - `ONE_WEEK`: Within a week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v2",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "noteType": note_type,
                "noteTime": note_time,
            },
        )

    def search_note_v4(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        search_id: str | None = "",
        session_id: str | None = "",
        sort_type: str | None = "general",
        note_type: str | None = "ALL",
        time_filter: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Note Search

        Searches Xiaohongshu (RedNote) notes through the mobile-app search flow with pagination, session continuity, sorting, note-type, and time filters. Use it to support iterative topic research and filtered content discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            search_id: Search session ID from the previous response data.api_info.search_id.
            session_id: Session ID from the previous response data.api_info.session_id.
            sort_type: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `ALL`: No Limit - `VIDEO_NOTE`: Video Note - `NORMAL_NOTE`: Normal Note
            time_filter: Publish time filter.  Available Values: - `ALL`: No Limit - `ONE_DAY`: Within one day - `ONE_WEEK`: Within one week - `HALF_YEAR`: Within half a year
        """
        return self._get(
            "/api/xiaohongshu/search-note/v4",
            {
                "keyword": keyword,
                "page": page,
                "searchId": search_id,
                "sessionId": session_id,
                "sortType": sort_type,
                "noteType": note_type,
                "timeFilter": time_filter,
            },
        )

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Search

        Searches Xiaohongshu (RedNote) users by keyword with page-based pagination. Use it to support creator discovery, account research, and finding profiles related to a topic, name, or brand term.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/xiaohongshu/search-user/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def get_user_note_list_v4(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Retrieves notes published by a Xiaohongshu (RedNote) user, accepting a user ID or supported profile URL and a cursor for pagination. Use it to support creator content browsing, account monitoring, and reviewing a user's note history.

        Args:
            user_id: A Xiaohongshu user ID or a profile URL containing /user/profile/.
            last_cursor: Pagination cursor from the previous page (the last note's cursor value).
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v4",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
            },
        )

    def get_note_detail_v1(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Retrieves Xiaohongshu (RedNote) details for a note identified by a note ID or supported explore URL. Use it to perform direct note lookup and content review from stored identifiers or shared explore links.

        Args:
            note_id: A Xiaohongshu note ID or an explore URL containing /explore/.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v1",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v6(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Retrieves Xiaohongshu (RedNote) video-note details by note ID. Use it to look up and process a known video note.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v6",
            {
                "noteId": note_id,
            },
        )

    def get_note_comment_v2(
        self,
        *,
        note_id: str,
        last_cursor: str | None = None,
        sort: str | None = "latest",
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Retrieves comments for a Xiaohongshu (RedNote) note with cursor pagination and normal, latest, or like-count sorting. Use it to support feedback review, discussion analysis, and comment moderation workflows.

        Args:
            note_id: A Xiaohongshu note ID or an explore URL containing /explore/.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
            sort: Sort strategy for the result set.  Available Values: - `normal`: Normal - `latest`: Latest - `like_count`: Like Count
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v2",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_sub_comment_v2(
        self,
        *,
        note_id: str,
        comment_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Comment Replies

        Retrieves replies to a specific Xiaohongshu (RedNote) note comment with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for feedback review or moderation.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            comment_id: Unique comment identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
        """
        return self._get(
            "/api/xiaohongshu/get-note-sub-comment/v2",
            {
                "noteId": note_id,
                "commentId": comment_id,
                "lastCursor": last_cursor,
            },
        )

    def get_user_v3(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a Xiaohongshu (RedNote) user profile from a user ID or supported profile URL. Use it to support creator discovery, account research, and reviewing a known profile before related content analysis.

        Args:
            user_id: A Xiaohongshu user ID or a profile URL containing /user/profile/.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v3",
            {
                "userId": user_id,
            },
        )

    def search_recommend_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Keyword Suggestions

        Returns Xiaohongshu (RedNote) search keyword suggestions for a submitted seed term. Use it to expand query sets, refine content-research searches, and plan SEO or programmatic SEO keyword coverage.

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/xiaohongshu/search-recommend/v1",
            {
                "keyword": keyword,
            },
        )

    def get_topic_note_list_v1(
        self,
        *,
        topic_id: str,
        sort: str | None = "hot",
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Topic Note List

        Retrieves Xiaohongshu (RedNote) notes associated with a topic ID, with hot or latest sorting and cursor pagination. Use it to support topic content discovery, trend review, and continuing through topic result pages.

        Args:
            topic_id: Unique topic identifier on Xiaohongshu.
            sort: Sort order for the result set.  Available Values: - `time`: Latest - `hot`: Hot
            cursor: Pagination cursor from the previous page.
        """
        return self._get(
            "/api/xiaohongshu/get-topic-note-list/v1",
            {
                "topicId": topic_id,
                "sort": sort,
                "cursor": cursor,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution

        Resolve a supported Xiaohongshu (RedNote) short share link and return its public redirect URL. Use it to expand shared links before subsequent Xiaohongshu content lookup or processing.

        Args:
            share_url: A Xiaohongshu (RedNote) short share URL beginning with http://xhslink.com/ or https://xhslink.com/.
        """
        return self._get(
            "/api/xiaohongshu/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
