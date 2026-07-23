from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class QqHuxuanResource(BaseResource):
    """Generated resource for QQ Huxuan Creator Marketplace."""

    def cgi_bin_advertiser_finder_publisher_search_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Account Creator Search

        Searches or browses QQ Huxuan Video Account creators by optional nickname keyword with page-number pagination. Use it to discover and shortlist video creators for Tencent Huxuan campaign planning.

        Args:
            keyword: Creator nickname keyword. Leave empty to browse the default marketplace list.
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/search/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def cgi_bin_advertiser_mp_publisher_search_v1(
        self,
        *,
        keyword: str | None = "",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Official Account Creator Search

        Searches or browses QQ Huxuan Official Account creators by optional nickname or account keyword with page-number pagination. Use it to discover and shortlist publishers for Tencent Huxuan campaign planning.

        Args:
            keyword: Creator nickname or account keyword. Leave empty to browse the default marketplace list.
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/search/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def cgi_bin_advertiser_finder_publisher_detail_v1(
        self,
        *,
        app_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Account Creator Details

        Retrieves QQ Huxuan Video Account creator details for a known creator app ID. Use it to review a shortlisted video creator before Tencent Huxuan campaign selection.

        Args:
            app_id: Video Account creator app ID.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/detail/v1",
            {
                "appId": app_id,
            },
        )

    def cgi_bin_advertiser_finder_publisher_get_finder_video_show_v1(
        self,
        *,
        app_id: str,
        begin_date: str,
        end_date: str,
        video_type: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Account Recent Videos

        Lists videos from a QQ Huxuan Video Account creator within a required date range, with a choice of all, Huxuan order, hot, or personal videos. Use it to review a shortlisted creator's content for campaign planning.

        Args:
            app_id: Video Account creator app ID.
            begin_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            video_type: Tencent Huxuan video type filter.  Available Values: - `ALL`: All videos - `ORDER`: QQ Huxuan order videos - `HOT`: Hot videos - `PERSON`: Personal videos
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/get_finder_video_show/v1",
            {
                "appId": app_id,
                "beginDate": begin_date,
                "endDate": end_date,
                "videoType": video_type,
                "page": page,
            },
        )

    def cgi_bin_advertiser_mp_publisher_detail_v1(
        self,
        *,
        app_id: str,
    ) -> ApiResponse[Any]:
        """
        Official Account Creator Details

        Retrieves QQ Huxuan Official Account creator details for a known creator app ID. Use it to review a shortlisted publisher before Tencent Huxuan campaign selection.

        Args:
            app_id: Official Account creator app ID.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/detail/v1",
            {
                "appId": app_id,
            },
        )

    def cgi_bin_advertiser_mp_publisher_get_user_articles_v1(
        self,
        *,
        app_id: str,
        start_date: str,
        end_date: str,
        keyword: str | None = "",
        article_type: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Official Account Article List

        Lists articles from a QQ Huxuan Official Account creator within a required date range, with an optional title keyword and a choice between all articles and Huxuan order articles. Use it to review a publisher's content for campaign planning.

        Args:
            app_id: Official Account creator app ID.
            start_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            keyword: Article title keyword. Leave empty to return all matched articles.
            article_type: Tencent Huxuan article type filter.  Available Values: - `ALL`: All articles - `ORDER`: QQ Huxuan order articles
            page: Page number. The first page is 1.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/mp_publisher/get_user_articles/v1",
            {
                "appId": app_id,
                "startDate": start_date,
                "endDate": end_date,
                "keyword": keyword,
                "articleType": article_type,
                "page": page,
            },
        )
