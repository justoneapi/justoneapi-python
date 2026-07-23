from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ImdbResource(BaseResource):
    """Generated resource for IMDb."""

    def title_release_expectation_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Release Expectation

        Retrieves IMDb release-expectation information for a title ID using selected language and country preferences. Use it to monitor a title's release context or support release-planning research.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-release-expectation-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_extended_details_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Extended Details

        Retrieves extended IMDb details for a title ID using selected language and country preferences. Use it to enrich a title catalog or perform deeper research after a basic lookup.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-extended-details-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_top_cast_and_crew_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Top Cast and Crew

        Retrieves IMDb top cast and crew information for a title ID using selected language and country preferences. Use it to research principal talent or enrich title credits.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-top-cast-and-crew/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_base_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Base Info

        Retrieves base IMDb information for a title ID using selected language and country preferences. Use it to perform a lightweight title lookup or populate basic catalog context.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-base-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_redux_overview_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Redux Overview

        Retrieves the IMDb Redux overview for a title ID using selected language and country preferences. Use it to obtain a consolidated title overview for catalog review or content research.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-redux-overview-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_did_you_know_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        'Did You Know' Insights

        Retrieves IMDb 'Did You Know' information for a title ID using selected language and country preferences. Use it to research title trivia and add editorial context.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-did-you-know-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_critics_review_summary_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Critics Review Summary

        Retrieves the IMDb critics-review summary for a title ID using selected language and country preferences. Use it to review critical reception or compare titles during research.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-critics-review-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_awards_summary_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Awards Summary

        Retrieves the IMDb awards summary for a title ID using selected language and country preferences. Use it to research a title's awards record or support awards-focused catalog review.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-awards-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_user_reviews_summary_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        User Reviews Summary

        Retrieves the IMDb user-reviews summary for a title ID using selected language and country preferences. Use it to review audience reception or support title comparison and research.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-user-reviews-summary-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_plot_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Plot Summary

        Retrieves IMDb plot information for a title ID using selected language and country preferences. Use it to review a movie or series storyline or enrich title descriptions.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-plot-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_contribution_questions_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Contribution Questions

        Retrieves IMDb contribution questions associated with a title ID using selected language and country preferences. Use it to review available prompts for title-data contribution workflows.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-contribution-questions/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_details_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Details

        Retrieves IMDb title details for a title ID using selected language and country preferences. Use it to support detailed title research or enrich a movie and television catalog.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-details-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_box_office_summary_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Box Office Summary

        Retrieves the IMDb box-office summary for a title ID using selected language and country preferences. Use it to research reported theatrical performance or compare titles.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-box-office-summary/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def title_more_like_this_query_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Recommendations

        Retrieves IMDb titles similar to a specified title ID using selected language and country preferences. Use it to support related-title discovery, recommendations, or catalog curation.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-more-like-this-query/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )

    def streaming_picks_query_v1(
        self,
        *,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Streaming Picks

        Retrieves IMDb streaming picks for Prime Video using selected language and country preferences. Use it to explore streaming titles for discovery, catalog review, or watchlist research.

        Args:
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/streaming-picks-query/v1",
            {
                "languageCountry": language_country,
            },
        )

    def news_by_category_query_v1(
        self,
        *,
        category: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        News by Category

        Retrieves IMDb news for a selected top, movie, TV, or celebrity category using language and country preferences. Use it to monitor entertainment news or research a specific category.

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

    def title_chart_rankings_v1(
        self,
        *,
        rankings_chart_type: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Chart Rankings

        Retrieves the IMDb Top 250 movie or TV chart selected by ranking type using language and country preferences. Use it to monitor chart positions or compare highly ranked titles.

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

    def title_countries_of_origin_v1(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
    ) -> ApiResponse[Any]:
        """
        Countries of Origin

        Retrieves countries of origin associated with an IMDb title ID using selected language and country preferences. Use it to enrich regional catalog metadata or support origin-based analysis.

        Args:
            id_: The IMDb title identifier in tt<digits> format.
            language_country: Language and country preferences.  Available Values: - `en_US`: English (US) - `fr_CA`: French (Canada) - `fr_FR`: French (France) - `de_DE`: German (Germany) - `hi_IN`: Hindi (India) - `it_IT`: Italian (Italy) - `pt_BR`: Portuguese (Brazil) - `es_ES`: Spanish (Spain) - `es_US`: Spanish (US) - `es_MX`: Spanish (Mexico)
        """
        return self._get(
            "/api/imdb/title-countries-of-origin/v1",
            {
                "id": id_,
                "languageCountry": language_country,
            },
        )
