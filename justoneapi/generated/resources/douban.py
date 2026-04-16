from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DoubanResource(BaseResource):
    """Generated resource for Douban Movie."""

    def get_movie_reviews_v1(
        self,
        *,
        subject_id: str,
        sort: str | None = "time",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Movie Reviews

        Get Douban movie Reviews data, including review titles, ratings, and snippets, for audience sentiment analysis and review research.

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

    def get_movie_review_detail_v1(
        self,
        *,
        review_id: str,
    ) -> ApiResponse[Any]:
        """
        Review Details

        Get Douban movie Review Details data, including metadata, content fields, and engagement signals, for review archiving and detailed opinion analysis.

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
        Comments

        Get Douban movie Comments data, including ratings, snippets, and interaction counts, for quick sentiment sampling and review monitoring.

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
        Subject Details

        Get Douban subject Details data, including title, rating, and cast, for title enrichment and catalog research.

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
        Recent Hot Movie

        Get Douban recent Hot Movie data, including ratings, posters, and subject metadata, for movie discovery and trend monitoring.

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
        Recent Hot Tv

        Get Douban recent Hot Tv data, including ratings, posters, and subject metadata, for series discovery and trend monitoring.

        Args:
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-recent-hot-tv/v1",
            {
                "page": page,
            },
        )
