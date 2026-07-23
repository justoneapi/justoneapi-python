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

        Retrieves paginated Douban long-form reviews for a movie or TV subject, ordered by time or popularity. Use it to browse in-depth audience reviews for a known subject.

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

        Retrieves a single Douban long-form review by its review ID. Use it to inspect a known review after discovering it in a subject's review list.

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

        Retrieves paginated Douban short comments for a movie or TV subject, ordered by time or newest rating. Use it to review concise audience feedback for a known subject.

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

        Retrieves the public detail page data for a Douban movie or TV subject by subject ID. Use it to inspect a known title before requesting its reviews or comments.

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

        Retrieves a paginated list of movies currently featured in Douban's recent-hot collection. Use it to discover popular movie titles and continue through result pages.

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

        Retrieves a paginated list of TV titles currently featured in Douban's recent-hot collection. Use it to discover popular series and continue through result pages.

        Args:
            page: Page number for pagination.
        """
        return self._get(
            "/api/douban/get-recent-hot-tv/v1",
            {
                "page": page,
            },
        )
