from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuResource(BaseResource):
    """Generated resource for Xiaohongshu."""

    def get_user_v3(
        self,
        *,
        user_id: str,
    ) -> ApiResponse[Any]:
        """
        User Profile (V3)

        Retrieves Xiaohongshu user profile data, including user identifiers and profile metadata
        (e.g., nickname, avatar, bio), as well as public counters such as follower count and like count (when available).

        Typical use cases:
        - Identifying creators/KOLs and building creator lists
        - Enriching user records for analytics and reporting
        - Creator monitoring (profile and counter changes over time)

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
        User Profile (V4)

        Retrieves Xiaohongshu user profile data, including user identifiers and profile metadata
        (e.g., nickname, avatar, bio), as well as public counters such as follower count and like count (when available).

        Typical use cases:
        - Identifying creators/KOLs and building creator lists
        - Enriching user records for analytics and reporting
        - Creator monitoring (profile and counter changes over time)

        Args:
            user_id: Unique user identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-user/v4",
            {
                "userId": user_id,
            },
        )

    def get_user_note_list_v2(
        self,
        *,
        user_id: str,
        last_cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Notes (V2)

        Retrieves a paginated list of notes published by a specific Xiaohongshu user.
        Each page returns basic note data (e.g., note ID, title/text snippet, publish time, cover/media info when available)
        and may include engagement counters depending on availability.

        Typical use cases:
        - Building a creator's content timeline and monitoring new posts
        - Batch collection for analytics, reporting, and dataset building
        - Creator/KOL and competitor monitoring

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
        User Published Notes (V4)

        Retrieves a paginated list of notes published by a specific Xiaohongshu user.
        Each page returns basic note data (e.g., note ID, title/text snippet, publish time, cover/media info when available)
        and may include engagement counters depending on availability.

        Typical use cases:
        - Building a creator's content timeline and monitoring new posts
        - Batch collection for analytics, reporting, and dataset building
        - Creator/KOL and competitor monitoring

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
    ) -> ApiResponse[Any]:
        """
        Note Details (V1)

        Retrieves detailed note data from Xiaohongshu, including the full note description,
        engagement metrics (likes, comments, collects, shares), and media information.

        The response includes media download URLs for images and videos.

        Typical use cases:
        - Content analysis and review using full note text
        - Engagement tracking for creators, campaigns, and competitors
        - Collecting media assets (images/videos) for downstream processing or archiving
        - Building datasets for analytics, reporting, and automation

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v1",
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
        Note Details (V3)

        Retrieves detailed note data from Xiaohongshu, including the full note description,
        engagement metrics (likes, comments, collects, shares), and media information.

        The response includes media download URLs for images and videos.

        Typical use cases:
        - Content analysis and review using full note text
        - Engagement tracking for creators, campaigns, and competitors
        - Collecting media assets (images/videos) for downstream processing or archiving
        - Building datasets for analytics, reporting, and automation

        Args:
            note_id: Unique note identifier on Xiaohongshu.
        """
        return self._get(
            "/api/xiaohongshu/get-note-detail/v3",
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
        Note Details (V7)

        Retrieves detailed note data from Xiaohongshu, including the full note description,
        engagement metrics (likes, comments, collects, shares), and media information.

        The response includes media download URLs for images and videos.

        Typical use cases:
        - Content analysis and review using full note text
        - Engagement tracking for creators, campaigns, and competitors
        - Collecting media assets (images/videos) for downstream processing or archiving
        - Building datasets for analytics, reporting, and automation

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
        Note Comments (V2)

        Retrieves comments for a Xiaohongshu note with pagination.
        The response includes comment text, publish time, commenter information (when available),
        and other comment metadata.

        Typical use cases:
        - Sentiment and public-opinion monitoring based on comment content
        - Tracking comment volume and feedback trends over time
        - Collecting discussions for analytics, reporting, and dataset building

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

    def get_note_comment_v4(
        self,
        *,
        note_id: str,
    ) -> ApiResponse[Any]:
        """
        Note Comments (V4)

        Retrieves comments for a Xiaohongshu note.

        Typical use cases:
        - Quick lookup of the latest/top comments for a note
        - Comment snapshot for lightweight monitoring

        Highlights
        - This version only returns the first page of comments; subsequent pages are not available.
        - If you need to fetch more pages, use the Note Comments (V2) endpoint.

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
        Comment Replies (V2)

        Retrieves replies under a specific Xiaohongshu comment (also known as second-level comments),
        with pagination when supported. The response includes reply text, publish time, replier information
        (when available), and other metadata.

        Typical use cases:
        - Deep sentiment analysis by including comment threads
        - Monitoring discussions under key comments
        - Collecting reply threads for analytics, reporting, and dataset building

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

    def get_search_note_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
        note_time: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Note Search (V2)

        Searches Xiaohongshu notes by keyword and optional filters, returning a paginated result set.
        Each result typically includes basic note information (e.g., note ID, title/text snippet, cover/media info),
        author signals (when available), and engagement counters (when available).

        Typical use cases:
        - Topic/keyword research and trend analysis
        - Discovering notes for monitoring, analytics, and dataset building
        - Campaign and competitor content discovery

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
            sort: Sort order for the result set.  Available Values: - `general`: General - `popularity_descending`: Popularity Descending - `time_descending`: Time Descending - `comment_descending`: Comment Descending - `collect_descending`: Collect Descending
            note_type: Note type filter.  Available Values: - `_0`: General - `_1`: Video - `_2`: Normal
            note_time: Note publish time filter.  Available Values: - `一天内`: Within one day - `一周内`: Within a week - `半年内`: Within half a year
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

    def get_search_note_v3(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        sort: str | None = "general",
        note_type: str | None = "_0",
    ) -> ApiResponse[Any]:
        """
        Note Search (V3)

        Searches Xiaohongshu notes by keyword and optional filters, returning a paginated result set.
        Each result typically includes basic note information (e.g., note ID, title/text snippet, cover/media info),
        author signals (when available), and engagement counters (when available).

        Typical use cases:
        - Topic/keyword research and trend analysis
        - Discovering notes for monitoring, analytics, and dataset building
        - Campaign and competitor content discovery

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

    def get_search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Search (V2)

        Searches Xiaohongshu users by keyword, returning a paginated result set with basic profile
        information (e.g., user ID, nickname, avatar, bio when available) and public counters/signals
        (when available).

        Typical use cases:
        - Finding creators/KOLs by niche, brand, or topic keywords
        - Building creator lists for monitoring and analytics
        - Discovering competitor accounts and related profiles

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

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Convert (V3)

        Converts a shared RedNote note short link into a normal (resolved) note URL.
        This is typically used to extract the note ID from a share link for downstream APIs
        (e.g., Note Details or Note Comments).

        Typical use cases:
        - Turning user-provided share links into structured identifiers (note ID)
        - Normalizing links before fetching note details, media, or comments
        - Automating workflows that start from share links

        Args:
            share_url: RedNote share link URL to be resolved (short link or shared URL).
        """
        return self._get(
            "/api/xiaohongshu/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )

    def search_recommend_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Search Keyword Suggestions (V1)

        Retrieves keyword suggestions for Xiaohongshu search.
        Given an input keyword prefix, this endpoint returns a list of recommended/related search terms
        that can be used to refine queries.

        Typical use cases:
        - Expanding keyword sets for content research and SEO/pSEO workflows
        - Improving search coverage by using platform-recommended terms
        - Building autocomplete experiences and discovery tools

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/xiaohongshu/search-recommend/v1",
            {
                "keyword": keyword,
            },
        )
