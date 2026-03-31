from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DoubanResource(BaseResource):
    """Generated resource for Douban."""

    def get_movie_reviews_v1(
        self,
        *,
        subject_id: str,
        sort: str | None = "time",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Movie Reviews (V1)

        Retrieves long-form user reviews for a specific movie subject (identified by subjectId).

        Typical use cases:
        - Analyzing detailed audience feedback for movies.
        - Long-term trend analysis of viewer sentiment.

        Args:
            subject_id: The unique ID for a movie or TV subject on Douban.
            sort: Sort order for the result set.  Available Values: - `time`: Time - `hotest`: Hotest
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-movie-reviews/v1",
            {
                "subjectId": subject_id,
                "sort": sort,
                "page": page,
            },
        )

    def get_movie_review_details_v1(
        self,
        *,
        review_id: str,
    ) -> ApiResponse[Any]:
        """
        Movie Review Details (V1)

        Retrieves the full content and metadata of a specific movie review (identified by reviewId).

        Typical use cases:
        - Fetching the complete text of a single long review.
        - Analyzing the structured data and user engagement (likes, replies) of a specific review.

        Args:
            review_id: The unique ID for a specific review on Douban.
        """
        return self._get(
            "/api/douban/get-movie-review-detail/v1",
            {
                "reviewId": review_id,
            },
        )

    def get_movie_comments_v1(
        self,
        *,
        subject_id: str,
        sort: str | None = "time",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Movie Comments (V1)

        Retrieves short user comments (short reviews) for a specific movie subject (identified by subjectId).

        Typical use cases:
        - Fast-paced sentiment analysis using quick viewer comments.
        - Monitoring initial audience reaction upon movie release.

        Args:
            subject_id: The unique ID for a movie or TV subject on Douban.
            sort: Sort order for the result set.  Available Values: - `time`: Time - `new_score`: New Score
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-movie-comments/v1",
            {
                "subjectId": subject_id,
                "sort": sort,
                "page": page,
            },
        )

    def get_subject_detail_v1(
        self,
        *,
        subject_id: str,
    ) -> ApiResponse[Any]:
        """
        Subject Details (V1)

        Retrieves detailed information for a specific subject identified by subjectId.

        Typical use cases:
        - Displaying complete subject metadata in applications or websites.
        - Supporting content analysis, cataloging, or detail page rendering.

        Args:
            subject_id: The unique ID for a movie or TV subject on Douban.
        """
        return self._get(
            "/api/douban/get-subject-detail/v1",
            {
                "subjectId": subject_id,
            },
        )

    def get_recent_hot_movie_v1(
        self,
        *,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Recent Hot Movie (V1)

        Retrieves the latest hot movies currently trending on the platform.

        Typical use cases:
        - Discovering recently popular movies.
        - Tracking current movie trends for content analysis or recommendation.

        Args:
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-recent-hot-movie/v1",
            {
                "page": page,
            },
        )

    def get_recent_hot_tv_v1(
        self,
        *,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Recent Hot Tv (V1)

        Retrieves the latest hot TV shows currently trending on the platform.

        Typical use cases:
        - Discovering recently popular TV shows.
        - Tracking current TV trends for content analysis or recommendation.

        Args:
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-recent-hot-tv/v1",
            {
                "page": page,
            },
        )
