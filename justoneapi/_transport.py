from __future__ import annotations

from typing import Any

import httpx

from justoneapi._exceptions import (
    BusinessError,
    ProtocolError,
    TransportError,
)
from justoneapi._response import ApiResponse
from justoneapi._version import __version__
from justoneapi.log import logger


class Transport:
    def __init__(
        self,
        *,
        token: str,
        base_url: str,
        timeout: int,
        raise_on_business_error: bool,
    ):
        self._token = token
        self._base_url = base_url.rstrip("/")
        self._raise_on_business_error = raise_on_business_error
        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=timeout,
            follow_redirects=True,
            headers={"JUSTONEAPI_PYTHON_SKD_VERSION": __version__},
        )

    def close(self) -> None:
        self._client.close()

    def get(self, path: str, params: dict[str, Any]) -> ApiResponse[Any]:
        request_params = {"token": self._token, **self._clean_params(params)}
        try:
            response = self._client.get(path, params=request_params)
        except httpx.HTTPError as exc:
            raise TransportError(f"Request failed for GET {path}: {exc}") from exc

        log_message = response.headers.get("JUSTONEAPI_PYTHON_SDK_LOG_MESSAGE")
        if log_message:
            logger.warning(log_message)

        try:
            payload = response.json()
        except ValueError as exc:
            raise ProtocolError(
                f"Server returned a non-JSON response for GET {path}"
            ) from exc

        if not isinstance(payload, dict):
            raise ProtocolError(
                f"Server returned a non-object JSON payload for GET {path}"
            )

        api_response = ApiResponse(
            success=self._is_success_code(payload.get("code")),
            code=payload.get("code"),
            message=str(payload.get("message") or ""),
            data=payload.get("data"),
            raw_json=payload,
        )

        if self._raise_on_business_error and not api_response.success:
            raise BusinessError(api_response)
        return api_response

    @staticmethod
    def _is_success_code(code: Any) -> bool:
        return code == 0

    @staticmethod
    def _clean_params(params: dict[str, Any]) -> dict[str, Any]:
        cleaned: dict[str, Any] = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, bool):
                cleaned[key] = str(value).lower()
            else:
                cleaned[key] = value
        return cleaned
