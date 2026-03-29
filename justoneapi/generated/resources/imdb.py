from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ImdbResource(BaseResource):
    """Generated resource for IMDb APIs."""

    def title_release_expectation_query(
        self,
        *,
        id_: str,
        language_country: str | None = "en_US",
        accept_cache: bool | None = False,
    ) -> ApiResponse[Any]:
        """
        Title Release Expectation (V1)

        Retrieve release expectation data for a specific title.

        Typical use cases:
        - Analyze audience anticipation for upcoming movie or TV show releases.

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
        Title Extended Details (V1)

        Retrieve comprehensive extended details for a specific title.

        Typical use cases:
        - Get in-depth metadata including production details, alternate titles, and more.

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
        Title Top Cast and Crew (V1)

        Retrieve information about the top cast and crew members of a title.

        Typical use cases:
        - List directors, writers, and main actors for a movie or TV show.

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
        Title Base Info (V1)

        Retrieve basic metadata for a specific title.

        Typical use cases:
        - Get essential information like title, year, and genre.

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
        Title Redux Overview (V1)

        Retrieve a redux overview of a specific title.

        Typical use cases:
        - Get a concise summary and overview of a movie or TV show's key attributes.

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
        Title 'Did You Know' Insights (V1)

        Retrieve interesting 'Did You Know' facts and trivia for a title.

        Typical use cases:
        - Enhance user engagement with fun facts and behind-the-scenes trivia.

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
        Title Critics Review Summary (V1)

        Retrieve a summary of critical reviews for a specific title.

        Typical use cases:
        - Display Metacritic scores and a compilation of professional critic feedback.

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
        Title Awards Summary (V1)

        Retrieve a summary of awards and nominations for a specific title.

        Typical use cases:
        - List Oscar wins, Golden Globe nominations, and other accolades.

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
        Title User Reviews Summary (V1)

        Retrieve a summary of user-submitted reviews for a specific title.

        Typical use cases:
        - Get average user ratings and a snapshot of audience sentiment.

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
        Title Plot Summary (V1)

        Retrieve the plot summary for a specific title.

        Typical use cases:
        - Display a detailed description of the storyline for a movie or TV show.

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
        Title Contribution Questions (V1)

        Retrieve contribution questions for a specific title.

        Typical use cases:
        - Facilitate user contributions by providing relevant metadata questions for a movie or TV show.

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
        Title Details (V1)

        Retrieve comprehensive details for a specific title.

        Typical use cases:
        - Get all standard information for a movie or TV show including summary, ratings, and more.

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
        Title Box Office Summary (V1)

        Retrieve box office summary for a specific title.

        Typical use cases:
        - Analyze financial performance including budget, opening weekend, and worldwide gross.

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
        Title Recommendations (V1)

        Retrieve title recommendations (More Like This) for a specific title.

        Typical use cases:
        - Provide users with similar content recommendations based on their interest in a specific title.

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
        Main Search (V1)

        Perform a general search on IMDb for titles, people, and more.

        Typical use cases:
        - Search for a movie by name or find a celebrity's profile.

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
        Streaming Picks (V1)

        Retrieve streaming recommendations curated by IMDb.

        Typical use cases:
        - Browse popular and recommended content available on streaming services.

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
        News by Category (V1)

        Retrieve entertainment news articles filtered by category.

        Typical use cases:
        - Stay updated on movie, TV, or celebrity news.

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
        Title Chart Rankings (V1)

        Retrieve title rankings from IMDb charts (e.g., Top 250).

        Typical use cases:
        - View the highest-rated movies and TV shows of all time.

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
        Title Countries of Origin (V1)

        Retrieve the countries of origin for a specific title.

        Typical use cases:
        - Identify the production locations and international roots of a movie or TV show.

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
