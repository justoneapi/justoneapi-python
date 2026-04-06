from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ImdbResource(BaseResource):
    """Generated resource for IMDb."""

    def title_release_expectation_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Release Expectation

        Get IMDb title Release Expectation data, including production status, release dates, and anticipation signals, for release monitoring and title research.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
            accept_cache: Whether to accept cached data.
        """
        return self._get(
            "/api/imdb/title-release-expectation-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
                "acceptCache": accept_cache,
            },
        )

    def title_extended_details_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Extended Details

        Get IMDb title Extended Details data, including title info, images, and genres, for title enrichment and catalog research.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-extended-details-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_top_cast_and_crew(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Top Cast and Crew

        Get IMDb title Top Cast and Crew data, including names, roles, and profile references, for talent research and title enrichment.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-top-cast-and-crew/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_base_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Base Info

        Get IMDb title Base Info data, including title text, release year, and type, for catalog enrichment and title lookup workflows.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-base-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_redux_overview_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Redux Overview

        Get IMDb title Redux Overview data, including key summary fields and linked metadata, for get a concise summary and overview of a movie or TV show's key attributes.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-redux-overview-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_did_you_know_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        'Did You Know' Insights

        Get IMDb title 'Did You Know' Insights data, including trivia, for editorial research and title insight enrichment.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-did-you-know-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_critics_review_summary_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Critics Review Summary

        Get IMDb title Critics Review Summary data, including review highlights, for review analysis and title comparison.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-critics-review-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_awards_summary_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Awards Summary

        Get IMDb title Awards Summary data, including nominations, for title benchmarking and awards research.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-awards-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_user_reviews_summary_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        User Reviews Summary

        Get IMDb title User Reviews Summary data, including aggregated review content and counts, for audience sentiment analysis.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-user-reviews-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_plot_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Plot Summary

        Get IMDb title Plot Summary data, including core metrics, trend signals, and performance indicators, for displaying a detailed description of the storyline for a movie or TV show.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-plot-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_contribution_questions(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Contribution Questions

        Get IMDb title Contribution Questions data, including specific IMDb title, for data maintenance workflows and title metadata review.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-contribution-questions/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_details_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Details

        Get IMDb title Details data, including metadata, release info, and cast, for deep title research and catalog enrichment.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-details-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_box_office_summary(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Box Office Summary

        Get IMDb title Box Office Summary data, including grosses and related performance indicators, for revenue tracking and title comparison.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-box-office-summary/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_more_like_this_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Recommendations

        Get IMDb title Recommendations data, including related titles and suggestion metadata, for content discovery and recommendation analysis.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-more-like-this-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def main_search_query(
        self,
        *,
        search_term: str,
        type: str | None = "Top",
        limit: int | None = 25,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Keyword Search

        Get IMDb keyword Search data, including matched results, metadata, and ranking signals, for entity discovery and entertainment research.

        Args:
            search_term: The term to search for (e.g., 'fire').
            type: Category of results to include in search.  Available Values: - `Top`: Top Results - `Movies`: Movies - `Shows`: TV Shows - `People`: People - `Interests`: Interests - `Episodes`: Episodes - `Podcast`: Podcasts - `Video_games`: Video Games
            limit: Maximum number of results to return (1-300).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/main-search-query/v1",
            {
                "searchTerm": search_term,
                "type": type,
                "limit": limit,
                "languageCountry": language_country,
            },
        )

    def streaming_picks_query(
        self,
        *,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Streaming Picks

        Get IMDb streaming Picks data, including curated titles available across streaming surfaces, for content discovery and watchlist research.

        Args:
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/streaming-picks-query/v1",
            {
                "languageCountry": language_country,
            },
        )

    def news_by_category_query(
        self,
        *,
        category: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        News by Category

        Get IMDb news by Category data, including headlines, summaries, and source metadata, for media monitoring and news research.

        Args:
            category: News category to filter by.  Available Values: - `TOP`: Top News - `MOVIE`: Movie News - `TV`: TV News - `CELEBRITY`: Celebrity News
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/news-by-category-query/v1",
            {
                "category": category,
                "languageCountry": language_country,
            },
        )

    def title_chart_rankings(
        self,
        *,
        rankings_chart_type: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Chart Rankings

        Get IMDb title Chart Rankings data, including positions in lists such as Top 250 and related charts, for ranking monitoring and title benchmarking.

        Args:
            rankings_chart_type: Type of rankings chart to retrieve.  Available Values: - `TOP_250`: Top 250 Movies - `TOP_250_TV`: Top 250 TV Shows
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-chart-rankings/v1",
            {
                "rankingsChartType": rankings_chart_type,
                "languageCountry": language_country,
            },
        )

    def title_countries_of_origin(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Countries of Origin

        Get IMDb title Countries of Origin data, including country names and regional metadata, for catalog enrichment and regional content analysis.

        Args:
            id_: The unique IMDb ID of the title (e.g., tt12037194).
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-countries-of-origin/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )
