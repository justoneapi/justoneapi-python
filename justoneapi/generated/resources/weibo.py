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

        Get Weibo keyword Search data, including authors, publish times, and engagement signals, for trend monitoring.

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

        Get Weibo post Details data, including media, author metadata, and engagement counts, for post analysis, archiving, and campaign monitoring.

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

        Get Weibo user Profile data, including follower counts, verification status, and bio details, for creator research and account analysis.

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

        Get Weibo user Fans data, including profile metadata and verification signals, for audience analysis and influencer research.

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

        Get Weibo user Followers data, including profile metadata and verification signals, for network analysis and creator research.

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

        Get Weibo user Published Posts data, including text, media, and publish times, for account monitoring.

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

        Get Weibo user Video list data (waterfall), including pagination cursor for next page.

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

        Get Weibo tV Video Details data, including media URLs, author details, and engagement counts, for video research, archiving, and performance analysis.

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

        Get Weibo hot Search data, including ranking data, for trend monitoring, newsroom workflows, and topic discovery.
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

        Get Weibo post Comments data, including text, authors, and timestamps, for feedback analysis.

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

        Get Weibo search User Published Posts data, including matched results, metadata, and ranking signals, for author research and historical content discovery.

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
