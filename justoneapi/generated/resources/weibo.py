from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeiboResource(BaseResource):
    """Generated resource for Weibo."""

    def search_all_v2(
        self,
        *,
        q: str,
        start_day: str,
        start_hour: int,
        end_day: str,
        end_hour: int,
        hot_sort: bool | None = False,
        contains: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Keyword Search

        Searches Weibo posts by keyword within a required day-and-hour time range, with page-based pagination, hot or time sorting, and filters for pictures, video, music, or links. Use it to find time-bounded posts for topic research or monitoring.

        Args:
            q: Search Keywords.
            start_day: Start Day (yyyy-MM-dd).
            start_hour: Start Hour (0-23).
            end_day: End Day (yyyy-MM-dd).
            end_hour: End Hour (0-23).
            hot_sort: Hot sort, true for hot sort, false for time sort. Default is false.
            contains: Contains filter for the result set.  Available Values: - `ALL`: All - `PICTURE`: Has Picture - `VIDEO`: Has Video - `MUSIC`: Has Music - `LINK`: Has Link
            page: Page number, starting with 1.
        """
        return self._get(
            "/api/weibo/search-all/v2",
            {
                "q": q,
                "startDay": start_day,
                "startHour": start_hour,
                "endDay": end_day,
                "endHour": end_hour,
                "hotSort": hot_sort,
                "contains": contains,
                "page": page,
            },
        )

    def get_weibo_detail_v1(
        self,
        *,
        id_: str,
    ) -> ApiResponse[Any]:
        """
        Post Details

        Retrieves details for a Weibo post identified by its post ID. Use it to look up a known post for content review, archiving, or related engagement analysis.

        Args:
            id_: Weibo post ID.
        """
        return self._get(
            "/api/weibo/get-weibo-detail/v1",
            {
                "id": id_,
            },
        )

    def get_user_detail_v3(
        self,
        *,
        uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a Weibo user profile identified by UID. Use it to look up a known account for creator research, profile review, or subsequent retrieval of that user's posts and videos.

        Args:
            uid: Weibo User ID (UID).
        """
        return self._get(
            "/api/weibo/get-user-detail/v3",
            {
                "uid": uid,
            },
        )

    def get_fans_v1(
        self,
        *,
        uid: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Fans

        Retrieves a page of fan accounts that follow a Weibo user identified by UID. Use it to browse the account's follower audience or continue through its fan list.

        Args:
            uid: Weibo User ID (UID).
            page: Page number, starting with 1.
        """
        return self._get(
            "/api/weibo/get-fans/v1",
            {
                "uid": uid,
                "page": page,
            },
        )

    def get_followers_v1(
        self,
        *,
        uid: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        User Followers

        Retrieves a page of accounts followed by a Weibo user identified by UID. Use it to examine the account's outgoing follow network or continue through its following list.

        Args:
            uid: Weibo User ID (UID).
            page: Page number, starting with 1.
        """
        return self._get(
            "/api/weibo/get-followers/v1",
            {
                "uid": uid,
                "page": page,
            },
        )

    def get_user_post_v1(
        self,
        *,
        uid: str,
        page: int | None = 1,
        since_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Retrieves posts published by a Weibo user identified by UID, using page numbers and a required sinceId cursor after the first page. Use it to browse an account's posting history or continue through its post feed.

        Args:
            uid: Weibo User ID (UID).
            page: Page number, starting with 1.
            since_id: Pagination cursor (since_id). Required if page > 1.
        """
        return self._get(
            "/api/weibo/get-user-post/v1",
            {
                "uid": uid,
                "page": page,
                "sinceId": since_id,
            },
        )

    def get_user_video_list_v1(
        self,
        *,
        uid: str,
        cursor: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Video List

        Retrieves a Weibo user's video waterfall feed by UID, with an optional cursor from a prior response. Use it to browse videos published by a known account or continue through its video feed.

        Args:
            uid: Weibo User ID (UID).
            cursor: Pagination cursor returned by the previous response.
        """
        return self._get(
            "/api/weibo/get-user-video-list/v1",
            {
                "uid": uid,
                "cursor": cursor,
            },
        )

    def tv_component_v1(
        self,
        *,
        oid: str,
    ) -> ApiResponse[Any]:
        """
        TV Video Details

        Retrieves Weibo TV video details for a colon-delimited object ID (OID). Use it to look up a known TV video for content review, cataloging, or downstream processing.

        Args:
            oid: Weibo video/object ID.
        """
        return self._get(
            "/api/weibo/tv-component/v1",
            {
                "oid": oid,
            },
        )

    def hot_search_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Hot Search

        Retrieves the current Weibo hot-search ranking. Use it to identify trending topics for newsroom monitoring, content planning, or timely topic discovery.
        """
        return self._get(
            "/api/weibo/hot-search/v1",
            {},
        )

    def get_post_comments_v1(
        self,
        *,
        mid: str,
        sort: str | None = "TIME",
        max_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Retrieves comments for a Weibo post identified by MID, with optional maxId cursor pagination and time or hot sorting. Use it to review audience discussion, continue through comment pages, or support moderation and feedback analysis.

        Args:
            mid: Weibo post mid.
            sort: Sort order for the result set.  Available Values: - `TIME`: Time - `HOT`: Hot
            max_id: Pagination cursor returned by the previous response.
        """
        return self._get(
            "/api/weibo/get-post-comments/v1",
            {
                "mid": mid,
                "sort": sort,
                "maxId": max_id,
            },
        )

    def search_profile_v1(
        self,
        *,
        uid: str,
        q: str,
        start_day: str | None = None,
        end_day: str | None = None,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Search User Published Posts

        Searches posts published by a specific Weibo user, using a keyword, optional date range, and page-based pagination. Use it to find historical posts from a known account for topic research or campaign review.

        Args:
            uid: Weibo User ID (UID).
            q: Search Keywords.
            start_day: Start Day (yyyy-MM-dd).
            end_day: End Day (yyyy-MM-dd).
            page: Page number, starting with 1.
        """
        return self._get(
            "/api/weibo/search-profile/v1",
            {
                "uid": uid,
                "q": q,
                "startDay": start_day,
                "endDay": end_day,
                "page": page,
            },
        )
