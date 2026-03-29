from __future__ import annotations

from typing import Any

from justoneapi._response import ApiResponse


class JustOneAPIError(Exception):
    """Base exception for the SDK."""


class TransportError(JustOneAPIError):
    """Raised when an HTTP transport error occurs."""


class ProtocolError(JustOneAPIError):
    """Raised when the server response cannot be interpreted."""


class VersionDeprecatedError(JustOneAPIError):
    """Raised when the server marks the SDK version as deprecated."""


class BusinessError(JustOneAPIError):
    """Raised when the API returns a non-zero business code and error raising is enabled."""

    def __init__(self, response: ApiResponse[Any]):
        super().__init__(
            response.message or f"Request failed with code={response.code!r}"
        )
        self.response = response
