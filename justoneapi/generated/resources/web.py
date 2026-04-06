from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WebResource(BaseResource):
    """Generated resource for Web Page."""

    def html_v1(
        self,
        *,
        url: str,
    ) -> ApiResponse[Any]:
        """
        HTML Content

        Get the HTML content of a web page.

        Args:
            url: The URL of the web page to fetch.
        """
        return self._get(
            "/api/web/html/v1",
            {
                "url": url,
            },
        )

    def rendered_html_v1(
        self,
        *,
        url: str,
    ) -> ApiResponse[Any]:
        """
        Rendered HTML Content

        Get the Rendered HTML content of a web page.

        Args:
            url: The URL of the web page to fetch.
        """
        return self._get(
            "/api/web/rendered-html/v1",
            {
                "url": url,
            },
        )

    def markdown_v1(
        self,
        *,
        url: str,
    ) -> ApiResponse[Any]:
        """
        Markdown Content

        Get the Markdown content of a web page.

        Args:
            url: The URL of the web page to fetch.
        """
        return self._get(
            "/api/web/markdown/v1",
            {
                "url": url,
            },
        )
