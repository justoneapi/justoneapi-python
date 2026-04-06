from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinResource(BaseResource):
    """Generated resource for WeChat Official Accounts."""

    def get_user_post(
        self,
        *,
        wxid: str,
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Get WeChat Official Accounts user Published Posts data, including titles, publish times, and summaries, for account monitoring.

        Args:
            wxid: The ID of the Weixin Official Account (e.g., 'rmrbwx').
        """
        return self._get(
            "/api/weixin/get-user-post/v1",
            {
                "wxid": wxid,
            },
        )

    def get_article_feedback(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Engagement Metrics

        Get WeChat Official Accounts article Engagement Metrics data, including like, share, and comment metrics, for article performance tracking and benchmarking.

        Args:
            article_url: The URL of the Weixin article.
        """
        return self._get(
            "/api/weixin/get-article-feedback/v1",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_comment(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Comments

        Get WeChat Official Accounts article Comments data, including commenter details, comment text, and timestamps, for feedback analysis.

        Args:
            article_url: The URL of the Weixin article.
        """
        return self._get(
            "/api/weixin/get-article-comment/v1",
            {
                "articleUrl": article_url,
            },
        )

    def search_v1(
        self,
        *,
        keyword: str,
        offset: int | None = 0,
        search_type: str | None = "_0",
        sort_type: str | None = "_0",
    ) -> ApiResponse[Any]:
        """
        Keyword Search

        Get WeChat Official Accounts keyword Search data, including account names, titles, and publish times, for content discovery.

        Args:
            keyword: The search keyword.
            offset: Pagination offset (starts with 0, increment by 20).
            search_type: Type of search results (accounts, articles, etc.).  Available Values: - `_0`: All - `_1`: WeChat Official Account - `_2`: Article - `_7`: WeChat Channel - `_262208`: Wechat Mini Program - `_384`: Emoji - `_16777728`: Encyclopedia - `_9`: Live - `_1024`: Book - `_512`: Music - `_16384`: News - `_8192`: Wechat Index - `_8`: Moments
            sort_type: Sorting criteria for search results.  Available Values: - `_0`: Default - `_2`: Latest - `_4`: Hot
        """
        return self._get(
            "/api/weixin/search/v1",
            {
                "keyword": keyword,
                "offset": offset,
                "searchType": search_type,
                "sortType": sort_type,
            },
        )

    def get_article_detail_v1(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Get WeChat Official Accounts article Details data, including body content, for article archiving, research, and content analysis.

        Args:
            article_url: The URL of the Weixin article.
        """
        return self._get(
            "/api/weixin/get-article-detail/v1",
            {
                "articleUrl": article_url,
            },
        )
