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

        Search QQ Huxuan Video Account creators from the Tencent Huxuan marketplace for creator discovery, audience screening, and campaign planning.

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

        Search QQ Huxuan Official Account creators from the Tencent Huxuan marketplace for creator discovery, audience screening, and campaign planning.

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

        Get QQ Huxuan Video Account creator profile details, including core profile, pricing, recent content, and audience profile fields returned by Tencent Huxuan.

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
        show_type: int | None = 0,
        video_type: int | None = 0,
        page_index: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Video Account Recent Videos

        Get recent QQ Huxuan Video Account creator videos and display metrics from the Tencent Huxuan detail page.

        Args:
            app_id: Video Account creator app ID.
            begin_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            show_type: Tencent Huxuan show type filter.
            video_type: Tencent Huxuan video type filter.
            page_index: Zero-based page index.
        """
        return self._get(
            "/api/qq-huxuan/cgi-bin/advertiser/finder_publisher/get_finder_video_show/v1",
            {
                "appId": app_id,
                "beginDate": begin_date,
                "endDate": end_date,
                "showType": show_type,
                "videoType": video_type,
                "pageIndex": page_index,
            },
        )

    def cgi_bin_advertiser_mp_publisher_detail_v1(
        self,
        *,
        app_id: str,
    ) -> ApiResponse[Any]:
        """
        Official Account Creator Details

        Get QQ Huxuan Official Account creator profile details, including profile, pricing, read metrics, reader profile, and recent article fields returned by Tencent Huxuan.

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
        article_type: int | None = 0,
        page: int | None = 1,
        page_size: int | None = 9,
    ) -> ApiResponse[Any]:
        """
        Official Account Article List

        Get QQ Huxuan Official Account creator articles and read metrics from the Tencent Huxuan detail page.

        Args:
            app_id: Official Account creator app ID.
            start_date: Start date in yyyyMMdd format.
            end_date: End date in yyyyMMdd format.
            keyword: Article title keyword. Leave empty to return all matched articles.
            article_type: Tencent Huxuan article type filter.
            page: Page number. The first page is 1.
            page_size: Page size. Values from 1 to 100 are accepted.
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
                "pageSize": page_size,
            },
        )
