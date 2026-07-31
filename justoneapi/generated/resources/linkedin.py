from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class LinkedinResource(BaseResource):
    """Generated resource for LinkedIn."""

    def search_user_v1(
        self,
        *,
        name: str | None = "",
        first_name: str | None = "",
        last_name: str | None = "",
        title: str | None = "",
        company: str | None = "",
        school: str | None = "",
        page: int | None = 1,
        geocode_location: str | None = "",
        current_company: str | None = "",
        profile_language: str | None = "",
        industry: str | None = "",
        service_category: str | None = "",
    ) -> ApiResponse[Any]:
        """
        People Search

        This LinkedIn people-search endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            name: Name or general keyword to search for.
            first_name: First name filter.
            last_name: Last name filter.
            title: Professional title filter.
            company: Company name filter.
            school: School name filter.
            page: Page number, starting from 1.
            geocode_location: LinkedIn geographic location code.
            current_company: LinkedIn current company ID filter.
            profile_language: Profile language filter.
            industry: LinkedIn industry ID filter.
            service_category: LinkedIn service category ID filter.
        """
        return self._get(
            "/api/linkedin/search-user/v1",
            {
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
                "title": title,
                "company": company,
                "school": school,
                "page": page,
                "geocodeLocation": geocode_location,
                "currentCompany": current_company,
                "profileLanguage": profile_language,
                "industry": industry,
                "serviceCategory": service_category,
            },
        )

    def get_user_detail_v1(
        self,
        *,
        username: str,
    ) -> ApiResponse[Any]:
        """
        User Profile

        Retrieves a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's professional background or before requesting published posts.

        Args:
            username: LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack.
        """
        return self._get(
            "/api/linkedin/get-user-detail/v1",
            {
                "username": username,
            },
        )

    def get_company_employees_v1(
        self,
        *,
        company_id: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Company Employees

        This LinkedIn company-employee endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            company_id: LinkedIn company ID.
            page: Page number, starting from 1.
        """
        return self._get(
            "/api/linkedin/get-company-employees/v1",
            {
                "companyId": company_id,
                "page": page,
            },
        )

    def get_user_posts_v1(
        self,
        *,
        url: str,
        type: str | None = "posts",
        start: int | None = 0,
        pagination_token: str | None = "",
    ) -> ApiResponse[Any]:
        """
        User Published Posts

        Retrieves posts published, commented on, or reacted to by a LinkedIn member using a profile URL, activity type, offset, and pagination token. Use it to review public professional activity and continue through additional result pages.

        Args:
            url: Full LinkedIn profile URL.
            type: User activity type.  Available Values: - `POSTS`: Posts published by the user - `COMMENTS`: Posts commented on by the user - `REACTIONS`: Posts reacted to by the user
            start: Pagination offset starting from 0, normally increasing by 50.
            pagination_token: Pagination token returned by a previous response.
        """
        return self._get(
            "/api/linkedin/get-user-posts/v1",
            {
                "url": url,
                "type": type,
                "start": start,
                "paginationToken": pagination_token,
            },
        )

    def get_post_reactions_v1(
        self,
        *,
        post_id: str,
        page: int | None = 1,
        type: str | None = "all",
    ) -> ApiResponse[Any]:
        """
        Post Reactions

        This LinkedIn post-reaction-record endpoint is deprecated because the capability is no longer available. Existing integrations should stop sending requests.

        Args:
            post_id: LinkedIn post ID.
            page: Page number, starting from 1.
            type: Reaction type filter.  Available Values: - `ALL`: All reaction types - `LIKE`: Like reactions - `PRAISE`: Praise reactions - `EMPATHY`: Empathy reactions - `APPRECIATION`: Appreciation reactions - `INTEREST`: Interest reactions
        """
        return self._get(
            "/api/linkedin/get-post-reactions/v1",
            {
                "postId": post_id,
                "page": page,
                "type": type,
            },
        )

    def get_post_comments_v1(
        self,
        *,
        post_id: str,
        page: int | None = 1,
        sort_order: str | None = "relevance",
        pagination_token: str | None = "",
        share_urn: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Post Comments

        Retrieves LinkedIn comments for an activity post with relevance or recent sorting, page-based navigation, a pagination token, and optional share URN. Use it to review public discussion around known professional content.

        Args:
            post_id: LinkedIn post ID.
            page: Page number, starting from 1.
            sort_order: Comment sort order.  Available Values: - `RELEVANCE`: Sort comments by relevance - `RECENT`: Sort comments from most recent
            pagination_token: Pagination token returned by a previous response.
            share_urn: Optional share URN for a shared post.
        """
        return self._get(
            "/api/linkedin/get-post-comments/v1",
            {
                "postId": post_id,
                "page": page,
                "sortOrder": sort_order,
                "paginationToken": pagination_token,
                "shareUrn": share_urn,
            },
        )
