from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinResource(BaseResource):
    """Generated resource for WeChat Official Accounts."""

    def get_account_today_articles_v1(
        self,
        *,
        biz: str | None = "",
        url: str | None = "",
        name: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Today Articles

        Returns articles published today by a WeChat Official Account. The account can be identified by biz id, article URL, account name, or wxid, making this endpoint useful for monitoring same-day account publishing activity.

        Args:
            biz: WeChat Official Account biz id. You can read it from the __biz query parameter in an article URL. Use one of biz, url, or name.
            url: WeChat Official Account article URL used to identify the account. Use one of biz, url, or name.
            name: WeChat Official Account name or wxid, for example People's Daily. Use one of biz, url, or name.
        """
        return self._get(
            "/api/weixin/get-account-today-articles/v1",
            {
                "biz": biz,
                "url": url,
                "name": name,
            },
        )

    def get_account_history_articles_v1(
        self,
        *,
        biz: str | None = "",
        url: str | None = "",
        name: str | None = "",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Account Historical Articles

        Returns paginated historical articles for a WeChat Official Account identified by biz id, article URL, account name, or wxid. This version uses page-number pagination for browsing an account's article archive.

        Args:
            biz: WeChat Official Account biz id. You can read it from the __biz query parameter in an article URL. Use one of biz, url, or name.
            url: WeChat Official Account article URL used to identify the account. Use one of biz, url, or name.
            name: WeChat Official Account name or wxid, for example People's Daily. Use one of biz, url, or name.
            page: Page number starting from 1 for paginated WeChat Official Account historical articles.
        """
        return self._get(
            "/api/weixin/get-account-history-articles/v1",
            {
                "biz": biz,
                "url": url,
                "name": name,
                "page": page,
            },
        )

    def get_account_history_articles_v2(
        self,
    ) -> ApiResponse[Any]:
        """
        Account Historical Articles

        Returns historical articles for a WeChat Official Account identified by ghid or article URL. This version uses the PagingInfo.Offset string cursor returned by the upstream response, which is better for stable continuous pagination.
        """
        return self._get(
            "/api/weixin/get-account-history-articles/v2",
            {},
        )

    def get_article_metrics_v1(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Metrics

        Returns basic interaction metrics for a WeChat Official Account article by article URL, including core signals such as reads and likes. Use it for lightweight article popularity checks.

        Args:
            article_url: WeChat Official Account article URL used to fetch basic interaction metrics such as reads and likes. It must end with #rd or #wechat_redirect.
        """
        return self._get(
            "/api/weixin/get-article-metrics/v1",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_metrics_v2(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Metrics

        Returns extended interaction metrics for a WeChat Official Account article by article URL, covering a richer set of read, like, and related engagement fields for article performance analysis.

        Args:
            article_url: WeChat Official Account article URL used to fetch extended interaction and article performance metrics.
        """
        return self._get(
            "/api/weixin/get-article-metrics/v2",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v1(
        self,
        *,
        article_url: str,
        mode: str | None = "TEXT",
    ) -> ApiResponse[Any]:
        """
        Article Details

        Returns WeChat Official Account article details by article URL. Version 1 supports the mode enum to choose plain text or rich text content when supported, and is suitable for collecting article body content with basic metadata.

        Args:
            article_url: WeChat Official Account article URL used to fetch article detail content and metadata.
            mode: Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported.  Available Values: - `TEXT`: Plain text article detail - `RICH_TEXT`: Rich text article detail
        """
        return self._get(
            "/api/weixin/get-article-detail/v1",
            {
                "articleUrl": article_url,
                "mode": mode,
            },
        )

    def get_article_detail_v2(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Returns structured WeChat Official Account article details by article URL. Version 2 focuses on fields such as title, cover image, author, publish time, original link, and content HTML fragment for parsing and storage.

        Args:
            article_url: WeChat Official Account article URL used to fetch structured article detail fields and an HTML content fragment.
        """
        return self._get(
            "/api/weixin/get-article-detail/v2",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v3(
        self,
        *,
        article_url: str,
        mode: str | None = "TEXT",
    ) -> ApiResponse[Any]:
        """
        Article Details

        Returns WeChat Official Account article details with additional video-related fields when available. Version 3 is useful for articles that contain video material or Channel-related media references.

        Args:
            article_url: WeChat Official Account article URL used to fetch article details with video-related fields when available.
            mode: Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported.  Available Values: - `TEXT`: Plain text article detail - `RICH_TEXT`: Rich text article detail
        """
        return self._get(
            "/api/weixin/get-article-detail/v3",
            {
                "articleUrl": article_url,
                "mode": mode,
            },
        )

    def get_article_detail_v4(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Returns a full HTML document for a WeChat Official Account article, including html, head, body, and article styles. Version 4 is suitable for rendering previews, archival storage, or page-level preservation.

        Args:
            article_url: WeChat Official Account article URL used to fetch a full HTML document for rendering or archiving.
        """
        return self._get(
            "/api/weixin/get-article-detail/v4",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v5(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Returns lightweight WeChat Official Account article information by article URL. Version 5 focuses on base metadata and status fields such as title, cover image, publish time, and account information.

        Args:
            article_url: WeChat Official Account article URL used to fetch lightweight article metadata and status information.
        """
        return self._get(
            "/api/weixin/get-article-detail/v5",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_comment_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Article Comments

        Returns top-level comments for a WeChat Official Account article by article URL. The response keeps comment data, total count, and buffer pagination fields for continuous comment collection.
        """
        return self._get(
            "/api/weixin/get-article-comment/v1",
            {},
        )

    def get_article_sub_comment_v1(
        self,
        *,
        article_url: str,
        content_id: str,
    ) -> ApiResponse[Any]:
        """
        Article Comment Replies

        Returns nested replies for a WeChat Official Account article comment. Use the article URL and top-level contentId to collect reply threads and complete the article comment conversation chain.

        Args:
            article_url: WeChat Official Account article URL used to fetch replies under a top-level comment.
            content_id: Top-level comment content id used to fetch nested comment replies.
        """
        return self._get(
            "/api/weixin/get-article-sub-comment/v1",
            {
                "articleUrl": article_url,
                "contentId": content_id,
            },
        )

    def search_article_hot_v1(
        self,
        *,
        start_day: str,
        end_day: str,
        keyword: str | None = "",
        publish_type: str | None = "IMAGE_TEXT",
        category: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Hot Article Search

        Searches hot and viral WeChat Official Account articles within a date range. It supports keyword, publish type, category, and page parameters for discovering high-performing account content.

        Args:
            start_day: Start date for hot article search in yyyy-MM-dd format.
            end_day: End date for hot article search in yyyy-MM-dd format.
            keyword: Optional keyword used to filter hot WeChat Official Account articles.
            publish_type: Publish type filter for hot WeChat Official Account article results.  Available Values: - `IMAGE_TEXT`: Image and text article - `VIDEO`: Pure video article - `AUDIO`: Pure audio or music article - `IMAGE`: Pure image article - `TEXT`: Pure text article - `REPRINT`: Reprinted article
            category: Category filter for hot WeChat Official Account article results.  Available Values: - `ALL`: All categories - `INTERNATIONAL`: International - `SPORTS`: Sports - `ENTERTAINMENT`: Entertainment - `SOCIETY`: Society - `FINANCE`: Finance - `CURRENT_AFFAIRS`: Current affairs - `TECHNOLOGY`: Technology - `EMOTION`: Emotion - `AUTOMOTIVE`: Automotive - `EDUCATION`: Education - `FASHION`: Fashion - `GAMES`: Games - `MILITARY`: Military - `TRAVEL`: Travel - `FOOD`: Food - `CULTURE`: Culture - `HEALTH`: Health - `HUMOR`: Humor - `HOME`: Home - `ANIMATION`: Animation - `PETS`: Pets - `PARENTING`: Parenting - `ASTROLOGY`: Astrology - `HISTORY`: History - `MUSIC`: Music - `UNCATEGORIZED`: Uncategorized - `COMPREHENSIVE`: Comprehensive - `WORKPLACE`: Workplace - `AGRICULTURE`: Agriculture - `ELDERLY_CARE`: Elderly care
            page: Page number starting from 1 for hot WeChat Official Account article results.
        """
        return self._get(
            "/api/weixin/search-article-hot/v1",
            {
                "startDay": start_day,
                "endDay": end_day,
                "keyword": keyword,
                "publishType": publish_type,
                "category": category,
                "page": page,
            },
        )

    def search_article_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Article Search

        Searches WeChat Official Account articles through the WeChat web search flow. Version 1 supports publish time filtering, sort type, offset, and cookies_buffer pagination for retrieving fresh web-side article results.
        """
        return self._get(
            "/api/weixin/search-article/v1",
            {},
        )

    def search_article_v2(
        self,
    ) -> ApiResponse[Any]:
        """
        Article Search

        Searches WeChat Official Account articles through the categorized WeChat web search flow. Version 2 uses subSearchType for focused result categories and keeps offset and cookies_buffer for continuous pagination.
        """
        return self._get(
            "/api/weixin/search-article/v2",
            {},
        )

    def search_miniprogram_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Mini Program Search

        Searches WeChat mini programs through the WeChat web search flow. It complements WeChat Official Account analysis by finding mini program entry points and related brand ecosystem signals.
        """
        return self._get(
            "/api/weixin/search-miniprogram/v1",
            {},
        )

    def search_wechat_index_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        WeChat Index Search

        Returns WeChat Index keyword search results. Use it with WeChat Official Account article and account analysis to observe keyword trend signals inside the WeChat ecosystem.

        Args:
            keyword: Keyword used to query WeChat Index trend signals.
        """
        return self._get(
            "/api/weixin/search-wechat-index/v1",
            {
                "keyword": keyword,
            },
        )

    def search_suggestions_v1(
        self,
        *,
        keyword: str,
        business_type: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Search Suggestions

        Returns WeChat search suggestions for a keyword. It is useful for autocomplete and query expansion in WeChat Official Account article search, account search, and content discovery workflows.

        Args:
            keyword: Keyword used to fetch WeChat search suggestions.
            business_type: WeChat search business type used to scope suggestion results.  Available Values: - `ALL`: All - `ACCOUNT`: Official accounts - `ARTICLE`: Articles - `CHANNEL`: Channels - `MOMENTS`: Moments - `LIVE`: Live - `EMOJI`: Emoji - `AUDIO`: Audio - `BOOK`: Books - `WECHAT_INDEX`: WeChat index - `NEWS`: News - `MINI_PROGRAM`: Mini programs - `ENCYCLOPEDIA`: Encyclopedia
        """
        return self._get(
            "/api/weixin/search-suggestions/v1",
            {
                "keyword": keyword,
                "businessType": business_type,
            },
        )

    def search_account_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Official Account profiles by keyword. Version 1 returns one account result per page with server-side fixed page size, which is useful for discovering accounts by name and basic identity signals.

        Args:
            keyword: Search keyword for WeChat Official Account profiles.
            page: Page number starting from 1 for WeChat Official Account profile search.
        """
        return self._get(
            "/api/weixin/search-account/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def search_account_v2(
        self,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Official Account profiles through the WeChat web search flow. Version 2 keeps offset and cookies_buffer pagination state for continuously retrieving broader account result sets.
        """
        return self._get(
            "/api/weixin/search-account/v2",
            {},
        )

    def get_account_original_count_v1(
        self,
        *,
        ghid: str | None = "",
        url: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Original Article Count

        Returns the original article count for a WeChat Official Account identified by ghid or article URL. Use it to evaluate account originality and long-term content quality.

        Args:
            ghid: WeChat Official Account original id, for example gh_363b924965e9. Use either ghid or url.
            url: WeChat Official Account article URL used to identify the account. Use either ghid or url.
        """
        return self._get(
            "/api/weixin/get-account-original-count/v1",
            {
                "ghid": ghid,
                "url": url,
            },
        )

    def get_account_principal_info_v1(
        self,
        *,
        biz: str | None = "",
        url: str | None = "",
        wxid: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Principal Info

        Returns principal and registration information for a WeChat Official Account. The account can be identified by biz id, article URL, or wxid, which helps verify ownership and operating entity details.

        Args:
            biz: WeChat Official Account biz id. Use one of biz, url, or wxid.
            url: WeChat Official Account article URL used to identify the account. Use one of biz, url, or wxid.
            wxid: WeChat Official Account wxid used to identify the account. Use one of biz, url, or wxid.
        """
        return self._get(
            "/api/weixin/get-account-principal-info/v1",
            {
                "biz": biz,
                "url": url,
                "wxid": wxid,
            },
        )

    def get_account_basic_info_v1(
        self,
        *,
        name: str,
    ) -> ApiResponse[Any]:
        """
        Account Basic Info

        Returns basic profile information for a WeChat Official Account by account name, including fields such as avatar and account type when available. Use it for quick account profile enrichment.

        Args:
            name: WeChat Official Account name used to fetch basic profile information.
        """
        return self._get(
            "/api/weixin/get-account-basic-info/v1",
            {
                "name": name,
            },
        )

    def convert_article_link_v1(
        self,
        *,
        link: str,
    ) -> ApiResponse[Any]:
        """
        Article Link Conversion

        Converts a WeChat Official Account article link into a normalized destination URL. It is useful for resolving short links or intermediate links before article collection.

        Args:
            link: WeChat Official Account article short link or intermediate link to convert.
        """
        return self._get(
            "/api/weixin/convert-article-link/v1",
            {
                "link": link,
            },
        )
