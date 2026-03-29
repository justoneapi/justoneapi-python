from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class ApiResponse(Generic[T]):
    success: bool
    code: Any | None
    message: str
    data: T | None
    raw_json: dict[str, Any]
