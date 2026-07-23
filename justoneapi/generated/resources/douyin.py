from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinResource(BaseResource):
    """Generated resource for Douyin (TikTok China)."""

    def search_video_v4(
        self,
        *,
        keyword: str,
        sort_type: str | None = "_0",
        publish_time: str | None = "_0",
        duration: str | None = "_0",
        page: int | None = 1,
        search_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Searches Douyin (TikTok China) videos by keyword with sort, publish-time, duration, and page filters; later pages require the previous search ID. Use it to support content discovery and trend research.

        Args:
            keyword: The search keyword.
            sort_type: Sorting criteria for search results.  Available Values: - `_0`: General - `_1`: More likes - `_2`: Newest
            publish_time: Filter by video publish time range.  Available Values: - `_0`: No Limit - `_1`: Last 24 Hours - `_7`: Last 7 Days - `_180`: Last 6 Months
            duration: Filter by video duration.  Available Values: - `_0`: No Limit - `_1`: Under 1 Minute - `_2`: 1-5 Minutes - `_3`: Over 5 Minutes
            page: Page number (starting from 1).
            search_id: Search ID; required for pages > 1 (use the search_id value returned by the last response).
        """
        return self._get(
            "/api/douyin/search-video/v4",
            {
                "keyword": keyword,
                "sortType": sort_type,
                "publishTime": publish_time,
                "duration": duration,
                "page": page,
                "searchId": search_id,
            },
        )

    def hot_search_v1(
        self,
        *,
        keyword: str | None = None,
        content_type: str | None = "ALL",
        video_type: str | None = "ALL",
        sort_type: str | None = "COMPREHENSIVE",
        page: int | None = 1,
        like_count_min: int | None = None,
        like_count_max: int | None = None,
        comment_count_min: int | None = None,
        comment_count_max: int | None = None,
        share_count_min: int | None = None,
        share_count_max: int | None = None,
        interaction_count_min: int | None = None,
        interaction_count_max: int | None = None,
        follower_count_min: int | None = None,
        follower_count_max: int | None = None,
    ) -> ApiResponse[Any]:
        """
        Hot Search

        Searches Douyin (TikTok China) content with optional keyword, category, video-type, ranking, pagination, engagement, and creator-follower filters. Use it to support trend discovery and campaign research.

        Args:
            keyword: Optional search keyword.
            content_type: Top-level content type. Only one content type can be selected.  Available Values: - `ALL`: All content types. - `FASHION`: Fashion. - `TECHNOLOGY`: Technology. - `SCIENCE`: Science. - `PHOTOGRAPHY`: Photography and videography. - `FOOD`: Food. - `MOTHER_BABY`: Mother and baby. - `PARENTING`: Parenting. - `DRAMA`: Drama. - `GAME`: Game. - `AUTOMOTIVE`: Automotive. - `ANIMAL`: Animal. - `TRAVEL`: Travel. - `DANCE`: Dance. - `TRADITIONAL_CULTURE`: Traditional culture. - `ART`: Art. - `SPORTS`: Sports. - `MUSIC`: Music. - `LIFE_RECORD`: Life records. - `HOME_LIVING`: Home and living. - `LEISURE_ENTERTAINMENT`: Leisure entertainment. - `WORKPLACE`: Workplace. - `AGRICULTURE`: Agriculture. - `CASUAL`: Casual videos. - `ACG`: Animation, comics, and games. - `MOVIE`: Movie. - `TV_SERIES`: TV series. - `VARIETY_SHOW`: Variety show. - `CELEBRITY`: Celebrity. - `HUMANITIES_SOCIAL_SCIENCE`: Humanities and social science. - `EDUCATION_CAMPUS`: Education and campus. - `EMOTION`: Emotion. - `FINANCE`: Finance. - `PUBLIC_WELFARE`: Public welfare.
            video_type: Video type filter.  Available Values: - `ALL`: All video types. - `XINGTU_VIDEO`: Xingtu commercial videos. - `NATURAL_VIDEO`: Natural videos.
            sort_type: Sorting criteria for hot content results.  Available Values: - `COMPREHENSIVE`: Comprehensive ranking. - `HIGH_INTERACTION`: Highest interaction count. - `HIGH_LIKE`: Highest like count. - `HIGH_COMMENT`: Highest comment count. - `HIGH_SHARE`: Highest share count.
            page: Page number (starting from 1). Page size is fixed at 10.
            like_count_min: Minimum raw like count.
            like_count_max: Maximum raw like count.
            comment_count_min: Minimum raw comment count.
            comment_count_max: Maximum raw comment count.
            share_count_min: Minimum raw share count.
            share_count_max: Maximum raw share count.
            interaction_count_min: Minimum raw interaction count.
            interaction_count_max: Maximum raw interaction count.
            follower_count_min: Minimum raw creator follower count.
            follower_count_max: Maximum raw creator follower count.
        """
        return self._get(
            "/api/douyin/hot-search/v1",
            {
                "keyword": keyword,
                "contentType": content_type,
                "videoType": video_type,
                "sortType": sort_type,
                "page": page,
                "likeCountMin": like_count_min,
                "likeCountMax": like_count_max,
                "commentCountMin": comment_count_min,
                "commentCountMax": comment_count_max,
                "shareCountMin": share_count_min,
                "shareCountMax": share_count_max,
                "interactionCountMin": interaction_count_min,
                "interactionCountMax": interaction_count_max,
                "followerCountMin": follower_count_min,
                "followerCountMax": follower_count_max,
            },
        )

    def get_user_video_list_v1(
        self,
        *,
        sec_uid: str,
        max_cursor: str | None = "0",
        sort_type: str | None = "LATEST",
    ) -> ApiResponse[Any]:
        """
        User Published Videos

        Retrieves videos published by a Douyin (TikTok China) user, with cursor pagination and newest or most-popular sorting. Use it to browse or monitor a creator's public video output.

        Args:
            sec_uid: The unique user ID (sec_user_id) on Douyin.
            max_cursor: Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages.
            sort_type: Sort order: `LATEST` for newest first (default), or `MOST_POPULAR` for most popular first.  Available Values: - `LATEST`: Newest first (default) - `MOST_POPULAR`: Most popular first
        """
        return self._get(
            "/api/douyin/get-user-video-list/v1",
            {
                "secUid": sec_uid,
                "maxCursor": max_cursor,
                "sortType": sort_type,
            },
        )

    def search_user_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        user_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        User Search

        Searches Douyin (TikTok China) users by keyword with page-based pagination and optional account-type filtering. Use it to discover creators, brands, or verified accounts for research.

        Args:
            keyword: The search keyword.
            page: Page number (starting from 1).
            user_type: Filter by user type.  Available Values: - `common_user`: Common User - `enterprise_user`: Enterprise User - `personal_user`: Verified Individual User
        """
        return self._get(
            "/api/douyin/search-user/v2",
            {
                "keyword": keyword,
                "page": page,
                "userType": user_type,
            },
        )

    def get_user_video_list_v3(
        self,
        *,
        sec_uid: str,
        max_cursor: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        User Published Videos

        Retrieves videos published by a Douyin (TikTok China) user with cursor pagination. Use it to browse a known creator's public video history or continue through video pages.

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
            max_cursor: Pagination cursor; use 0 for the first page, and the `max_cursor` from the previous response for subsequent pages.
        """
        return self._get(
            "/api/douyin/get-user-video-list/v3",
            {
                "secUid": sec_uid,
                "maxCursor": max_cursor,
            },
        )

    def get_video_detail_v2(
        self,
        *,
        video_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Details

        Retrieves details for a Douyin (TikTok China) video by video ID. Use it to look up a known video before content review, archiving, or related analysis.

        Args:
            video_id: The unique video identifier (aweme_id or model_id).
        """
        return self._get(
            "/api/douyin/get-video-detail/v2",
            {
                "videoId": video_id,
            },
        )

    def get_video_comment_v1(
        self,
        *,
        aweme_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Video Comments

        Retrieves top-level comments for a Douyin (TikTok China) video by aweme ID with page-based pagination. Use it to review audience feedback or analyze discussion around a known video.

        Args:
            aweme_id: The unique video identifier (aweme_id).
            page: Page number (starting from 1).
        """
        return self._get(
            "/api/douyin/get-video-comment/v1",
            {
                "awemeId": aweme_id,
                "page": page,
            },
        )

    def get_video_sub_comment_v1(
        self,
        *,
        comment_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Comment Replies

        Retrieves replies to a top-level Douyin (TikTok China) video comment with page-based pagination. Use it to inspect threaded discussions and review feedback under a known comment.

        Args:
            comment_id: The unique identifier of the top-level comment.
            page: Page number (starting from 1).
        """
        return self._get(
            "/api/douyin/get-video-sub-comment/v1",
            {
                "commentId": comment_id,
                "page": page,
            },
        )

    def get_user_detail_v3(
        self,
        *,
        sec_uid: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a Douyin (TikTok China) user profile by secUid. Use it to review a known creator or account before monitoring related content or conducting account research.

        Args:
            sec_uid: The unique user ID (sec_uid) on Douyin.
        """
        return self._get(
            "/api/douyin/get-user-detail/v3",
            {
                "secUid": sec_uid,
            },
        )

    def share_url_transfer_v1(
        self,
        *,
        share_url: str,
    ) -> ApiResponse[Any]:
        """
        Share Link Resolution

        Resolve a supported Douyin (TikTok China) short share link that targets a video and return its public redirect URL. Use it to expand video links before subsequent Douyin content lookup or processing.

        Args:
            share_url: A Douyin short share URL beginning with https://v.douyin.com/.
        """
        return self._get(
            "/api/douyin/share-url-transfer/v1",
            {
                "shareUrl": share_url,
            },
        )
