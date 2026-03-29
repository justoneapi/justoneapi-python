from __future__ import annotations

from justoneapi._transport import Transport
from justoneapi.config import DEFAULT_BASE_URL
from justoneapi.generated.resources import RESOURCE_CLASSES


class JustOneAPIClient:
    def __init__(
        self,
        token: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = 60,
        raise_on_business_error: bool = False,
    ):
        if not token:
            raise ValueError("Token is required. Please contact us to obtain one.")

        self._transport = Transport(
            token=token,
            base_url=base_url,
            timeout=timeout,
            raise_on_business_error=raise_on_business_error,
        )
        self._resources: dict[str, object] = {}
        for namespace, resource_class in RESOURCE_CLASSES.items():
            resource = resource_class(self._transport)
            setattr(self, namespace, resource)
            self._resources[namespace] = resource

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "JustOneAPIClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
