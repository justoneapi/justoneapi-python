from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeiboResource(BaseResource):
    """Generated resource for Weibo APIs."""

    def search_all_v2(
        self,
        *,
        q: str,
        start_day: str,
        start_hour: int,
        end_day: str,
        end_hour: int,
        hot_sort: bool | None = False,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Keyword Search (V2)

        Enables advanced keyword-based search on Weibo posts, supporting filters such as time range.
        Returns matching posts with content, author info, publish time, and engagement metrics (likes, reposts, comments).

        Typical use cases:
        - Tracking discussions around specific brands or events
        - Gathering public opinion data for a specific time period

        Args:
            q: Search Keywords.
            start_day: Start Day (yyyy-MM-dd).
            start_hour: Start Hour (0-23).
            end_day: End Day (yyyy-MM-dd).
            end_hour: End Hour (0-23).
            hot_sort: Hot sort, true for hot sort, false for time sort. Default is false.
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
                "page": page,
            },
        )

    def get_weibo_details_v1(
        self,
        *,
        id_: str,
    ) -> ApiResponse[Any]:
        """
        Post Details (V1)

        Retrieves detailed information about a specific Weibo post, including full text content,
        media assets (images/videos), author information, publish time, and engagement metrics (likes, comments, and reposts).

        Typical use cases:
        - Detailed analysis of specific social media posts
        - Content archival and monitoring

        Args:
            id_: Weibo post ID.
        """
        return self._get(
            "/api/weibo/get-weibo-detail/v1",
            {
                "id": id_,
            },
        )

    def get_user_profile_v3(
        self,
        *,
        uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile (V3)

        Retrieves detailed profile information for a specified Weibo user, including nickname, avatar,
        user ID, follower/following counts, bio, and verification status.

        Typical use cases:
        - Creator/KOL identification and monitoring
        - Enriching user records for analytics and reporting

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
        User Fans (V1)

        Retrieves the follower list (fans) of a specified Weibo user with pagination.
        Includes user IDs, nicknames, avatars, and verification status of followers.

        Typical use cases:
        - Audience analysis and demographic research
        - Monitoring follower growth and community engagement

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
        User Followers (V1)

        Retrieves the list of accounts that a specified Weibo user is following.
        Includes user IDs, nicknames, avatars, and verification status of the followed accounts.

        Typical use cases:
        - Relationship mapping and network analysis
        - Identifying interests and associations of specific users

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

    def get_user_published_posts_v1(
        self,
        *,
        uid: str,
        page: int | None = 1,
        since_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Published Posts (V1)

        Retrieves the post list of a specified Weibo user with pagination.
        Each entry includes status ID, text, media assets, publish time, and engagement metrics.

        Typical use cases:
        - Creator monitoring and content tracking
        - Building content timelines for specific accounts

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

    def tv_component_v1(
        self,
        *,
        oid: str,
    ) -> ApiResponse[Any]:
        """
        TV Video Details (V1)

        Retrieves detailed information of a single Weibo TV video by its object ID.
        Includes video metadata, media URLs, cover images, author info, and engagement metrics.

        Typical use cases:
        - Video content analysis and archival
        - Monitoring performance of Weibo TV videos

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
        Hot Search (V1)

        Retrieves the current hot search (trending) topics from Weibo.

        Typical use cases:
        - Real-time trend monitoring
        - Identifying viral topics and news
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
        Post Comments (V1)

        Retrieves comments for a specified Weibo post with pagination.
          Returns comment content, comment ID, author information, publish time, and related engagement data when available.

          Typical use cases:
          - Collecting comment threads for a specific post
          - Sentiment analysis and audience feedback research
          - Monitoring engagement and discussion around a post

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
        Search User Published Posts (V1)

        Search Weibo posts published by a specific user by keywords and time range.

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
