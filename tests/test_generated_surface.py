from __future__ import annotations

from pathlib import Path

from justoneapi import JustOneAPIClient
from justoneapi.generated.models import Result
from justoneapi.generated.resources import RESOURCE_CLASSES
from tools.sdk_codegen import load_json

NORMALIZED_SPEC_PATH = Path("openapi/public-api.normalized.json")


def expected_resource_namespaces() -> set[str]:
    spec = load_json(NORMALIZED_SPEC_PATH)
    return {
        operation["x-sdk-resource"]
        for path_item in spec.get("paths", {}).values()
        for method, operation in path_item.items()
        if not method.startswith("x-")
    }


def expected_resource_surface() -> dict[str, dict[str, object]]:
    spec = load_json(NORMALIZED_SPEC_PATH)
    resources: dict[str, dict[str, object]] = {}
    for path_item in spec.get("paths", {}).values():
        for method, operation in path_item.items():
            if method.startswith("x-"):
                continue

            namespace = operation["x-sdk-resource"]
            resource = resources.setdefault(
                namespace,
                {
                    "class_name": operation["x-sdk-class-name"],
                    "method_names": set(),
                },
            )
            resource["method_names"].add(operation["x-sdk-method-name"])
    return resources


def test_generated_resource_registry_matches_public_api_surface():
    expected_namespaces = expected_resource_namespaces()

    assert expected_namespaces
    assert set(RESOURCE_CLASSES) == expected_namespaces


def test_client_exposes_generated_resources():
    client = JustOneAPIClient(token="test-token")
    try:
        for namespace, expected in expected_resource_surface().items():
            assert hasattr(client, namespace)

            resource = getattr(client, namespace)
            assert type(resource).__name__ == expected["class_name"]
            for method_name in expected["method_names"]:
                assert hasattr(resource, method_name)
    finally:
        client.close()


def test_generated_result_model_accepts_generic_payload():
    result = Result.model_validate({"code": "0", "message": "ok", "data": {"x": 1}})
    assert result.message == "ok"
    assert result.data == {"x": 1}
