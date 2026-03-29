from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinResource(BaseResource):
    """Generated resource for Weixin APIs."""

    def get_user_post(
        self,
        *,
        wxid: str,
    ) -> ApiResponse[Any]:
        """
        User Published Posts (V1)

        Retrieves posts published by a specific Weixin Official Account, including title, author, publish time, content summary, and engagement metrics such as reads, likes, and shares.

        Typical use cases:
        - Monitoring recent activity of a specific account.
        - Analyzing publishing frequency and content types.

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
        Article Engagement Metrics (V1)

        Retrieves engagement metrics for a specific Weixin Official Account article, including read count, like count, share count, and comment count.

        Typical use cases:
        - Tracking performance of a specific post.
        - Comparing engagement levels across different articles.

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
        Article Comments (V1)

        Retrieves user comments from a specific Weixin Official Account article, including commenter name, comment content, like count, and timestamp.

        Typical use cases:
        - Analyzing community sentiment and feedback.
        - Identifying popular discussion points.

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
        Search (V1)

        Supports keyword-based search for both Weixin Official Accounts and their published articles. It returns matched accounts or posts with details such as account name, article title, publish time, and summary.

        Typical use cases:
        - Discovering new accounts related to specific topics.
        - Finding historical articles using keywords.

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
        Article Details (V1)

        Retrieves core metadata and content details for a specific Weixin Official Account article.

        Typical use cases:
        - Scraping detailed content for archival or analysis.
        - Verifying article metadata from a URL.

        Args:
            article_url: The URL of the Weixin article.
        """
        return self._get(
            "/api/weixin/get-article-detail/v1",
            {
                "articleUrl": article_url,
            },
        )
