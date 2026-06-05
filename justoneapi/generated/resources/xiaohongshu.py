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

        Get Xiaohongshu (RedNote) hot Search data, including popular notes and engagement metrics, for content trend discovery.

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

        Get Xiaohongshu (RedNote) note Search data, including snippets, authors, and media, for topic discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter. This parameter is for reference only and does not have much effect.  Available Values: - `一天内`: Within one day - `一周内`: Within a week - `半年内`: Within half a year
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

    def search_note_v3(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
    ) -> ApiResponse[Any]:
        """
        Note Search

        Get Xiaohongshu (RedNote) note Search data, including snippets, authors, and media, for topic discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Hot - `time_descending`: New
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
        """
        return self._get(
            "/api/xiaohongshu/search-note/v3",
            {
                "keyword": keyword,
                "page": page,
                "sort": sort,
                "noteType": note_type,
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
        note_type: str | None = "不限",
        time_filter: str | None = "不限",
    ) -> ApiResponse[Any]:
        """
        Note Search

        Get Xiaohongshu (RedNote) note Search data, including snippets, authors, and media, for topic discovery.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            search_id: Search session ID from the previous response data.api_info.search_id.
            session_id: Session ID from the previous response data.api_info.session_id.
            sort_type: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `不限`: No Limit - `视频笔记`: Video Note - `普通笔记`: Normal Note
            time_filter: Publish time filter.  Available Values: - `不限`: No Limit - `一天内`: Within one day - `一周内`: Within one week - `半年内`: Within half a year
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

        Get Xiaohongshu (RedNote) user Search data, including profile metadata and public signals, for creator discovery and account research.

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

    def get_user_note_list_v2(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes

        Get Xiaohongshu (RedNote) user Published Notes data, including note metadata, covers, and publish times, for account monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (the last note's cursor value).
        """
        return self._get(
            "/api/xiaohongshu/get-user-note-list/v2",
            {
                "userId": user_id,
                "lastCursor": last_cursor,
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

        Get Xiaohongshu (RedNote) user Published Notes data, including note metadata, covers, and publish times, for account monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
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
        format: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            format: Do not use unless confirmed by admin.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v1",
            {
                "noteId": note_id,
                "format": format,
            },
        )

    def get_note_detail_v2(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v2",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v3(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v3",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v4(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v4",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v5(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v5",
            {
                "noteId": note_id,
            },
        )

    def get_note_detail_v7(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Details

        Get Xiaohongshu (RedNote) note Details data, including media and engagement metrics, for content analysis, archiving, and campaign research.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v7",
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

        Get Xiaohongshu (RedNote) note Comments data, including text, authors, and timestamps, for feedback analysis.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page (use the cursor value returned by the last response).
            sort: Sort order for the result set.  Available Values: - `normal`: Normal - `latest`: Latest
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v2",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_comment_v3(
        self,
        *,
        note_id: str,
        last_cursor: str | None = None,
        sort: str | None = "latest",
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Get Xiaohongshu (RedNote) note Comments data, including text, authors, and timestamps, for feedback analysis.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
            last_cursor: Pagination cursor from the previous page.
            sort: Sort strategy for the result set.  Available Values: - `normal`: Normal - `latest`: Latest - `like_count`: Like Count
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v3",
            {
                "noteId": note_id,
                "lastCursor": last_cursor,
                "sort": sort,
            },
        )

    def get_note_comment_v4(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Comments

        Get Xiaohongshu (RedNote) note Comments data, including comment text, author profiles, and interaction data, for sentiment analysis and community monitoring.

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-comment/v4",
            {
                "noteId": note_id,
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

        Get Xiaohongshu (RedNote) comment Replies data, including text, authors, and timestamps, for thread analysis and feedback research.

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

        Get Xiaohongshu (RedNote) user Profile data, including follower counts and bio details, for creator research, account analysis, and competitor monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v3",
            {
                "userId": user_id,
            },
        )

    def get_user_v4(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Get Xiaohongshu (RedNote) user Profile data, including follower counts and bio details, for creator research, account analysis, and competitor monitoring.

        Args:
            user_id: Unique user identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v4",
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

        Get Xiaohongshu (RedNote) keyword Suggestions data, including suggested queries, keyword variants, and query metadata, for expanding keyword sets for content research and seo/pseo workflows and improving search coverage by using platform-recommended terms.

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

        Get Xiaohongshu (RedNote) topic Note List data, including notes under a topic, for topic monitoring and content discovery.

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

        Get Xiaohongshu (RedNote) share Link Resolution data, including helping extract note IDs, for downstream note and comment workflows.

        Args:
            share_url: RedNote share link URL to be resolved (short link or shared URL).
        """
        return self._get(
            "/api/xiaohongshu/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
