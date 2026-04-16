from __future__ import annotations

import copy
import json
import keyword
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC_URL = "https://api.justoneapi.com/v3/api-docs/public-api"
DEFAULT_RAW_SPEC_PATH = ROOT / "openapi" / "public-api.json"
DEFAULT_NORMALIZED_SPEC_PATH = ROOT / "openapi" / "public-api.normalized.json"
DEFAULT_OVERRIDES_PATH = ROOT / "openapi" / "sdk_overrides.yaml"
GENERATED_ROOT = ROOT / "justoneapi" / "generated"
GENERATED_RESOURCES_ROOT = GENERATED_ROOT / "resources"
GENERATED_MODELS_PATH = GENERATED_ROOT / "models.py"


@dataclass(frozen=True)
class ParameterInfo:
    api_name: str
    python_name: str
    python_type: str
    required: bool
    default_expr: str | None
    description: str


@dataclass(frozen=True)
class OperationInfo:
    operation_id: str
    method_name: str
    class_name: str
    namespace: str
    tag: str
    path: str
    summary: str
    description: str
    order: int
    parameters: tuple[ParameterInfo, ...]


@dataclass(frozen=True)
class ResourceInfo:
    namespace: str
    class_name: str
    tag: str
    operations: tuple[OperationInfo, ...]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def load_overrides(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text())
    return data or {}


def dump_json(data: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    )


def fetch_openapi(url: str, username: str, password: str) -> dict[str, Any]:
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        response = client.get(url, auth=(username, password))
        response.raise_for_status()
        return response.json()


_CAMEL_BOUNDARY_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_BOUNDARY_2 = re.compile(r"([a-z0-9])([A-Z])")
_NON_IDENTIFIER = re.compile(r"[^0-9a-zA-Z_]")
_VERSION_SEGMENT = re.compile(r"v\d+$")


def camel_to_snake(value: str) -> str:
    value = value.replace("-", "_")
    value = _CAMEL_BOUNDARY_1.sub(r"\1_\2", value)
    value = _CAMEL_BOUNDARY_2.sub(r"\1_\2", value)
    value = _NON_IDENTIFIER.sub("_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_").lower()


_IDENTIFIER_ALIASES = {
    "id": "id_",
}


def to_python_identifier(value: str) -> str:
    candidate = camel_to_snake(value)
    candidate = _IDENTIFIER_ALIASES.get(candidate, candidate)
    if not candidate:
        candidate = "value"
    if candidate[0].isdigit():
        candidate = f"field_{candidate}"
    if keyword.iskeyword(candidate):
        candidate = f"{candidate}_"
    return candidate


def snake_to_pascal(value: str) -> str:
    return "".join(part.capitalize() for part in value.split("_") if part)


def python_type_for_schema(schema: dict[str, Any], *, required: bool) -> str:
    schema_type = schema.get("type")
    base = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "number": "float",
        "array": "list[Any]",
        "object": "dict[str, Any]",
    }.get(schema_type, "Any")
    default = schema.get("default")
    if required and default is None:
        return base
    return f"{base} | None"


def python_default_for_schema(schema: dict[str, Any], *, required: bool) -> str | None:
    if "default" in schema:
        return repr(schema["default"])
    if required:
        return None
    return "None"


def namespace_from_path(path: str, overrides: dict[str, Any]) -> str:
    prefix = path.split("/")[2]
    resource_names = overrides.get("resource_names", {})
    return to_python_identifier(resource_names.get(prefix, prefix.replace("-", "_")))


def method_name_from_path(path: str) -> str:
    parts = [part for part in path.split("/") if part]
    method_parts = parts[2:]
    if len(method_parts) == 1 and _VERSION_SEGMENT.fullmatch(method_parts[0]):
        method_parts = [parts[1], method_parts[0]]
    return to_python_identifier("_".join(method_parts))


def operation_order(operation: dict[str, Any]) -> int:
    raw_order = operation.get("x-order")
    if raw_order is None:
        return sys.maxsize
    try:
        return int(raw_order)
    except (TypeError, ValueError):
        return sys.maxsize


def normalize_spec(spec: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(spec)
    hidden_query_parameters = set(overrides.get("hidden_query_parameters", []))
    seen_resource_methods: set[tuple[str, str]] = set()

    components = normalized.setdefault("components", {})
    components.setdefault("securitySchemes", {})["tokenAuth"] = {
        "type": "apiKey",
        "in": "query",
        "name": "token",
    }
    normalized["security"] = [{"tokenAuth": []}]

    for path, path_item in normalized.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.startswith("x-"):
                continue

            operation_id = operation.get("operationId")
            if not operation_id:
                raise ValueError(f"Missing operationId for {method.upper()} {path}")

            namespace = namespace_from_path(path, overrides)
            method_name = method_name_from_path(path)
            resource_method = (namespace, method_name)
            if resource_method in seen_resource_methods:
                raise ValueError(
                    f"Duplicate generated method {namespace}.{method_name} for {method.upper()} {path}"
                )
            seen_resource_methods.add(resource_method)
            operation["x-sdk-resource"] = namespace
            operation["x-sdk-class-name"] = f"{snake_to_pascal(namespace)}Resource"
            operation["x-sdk-method-name"] = method_name
            operation["security"] = [{"tokenAuth": []}]

            normalized_parameters = []
            for parameter in operation.get("parameters", []):
                if (
                    parameter.get("in") == "query"
                    and parameter.get("name") in hidden_query_parameters
                ):
                    continue
                copied_parameter = copy.deepcopy(parameter)
                copied_parameter["x-sdk-python-name"] = to_python_identifier(
                    parameter["name"]
                )
                normalized_parameters.append(copied_parameter)
            operation["parameters"] = normalized_parameters

    return normalized


def collect_resources(spec: dict[str, Any]) -> list[ResourceInfo]:
    resources: dict[str, dict[str, Any]] = {}

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.startswith("x-"):
                continue

            namespace = operation["x-sdk-resource"]
            tag = operation.get("tags", [namespace])[0]
            class_name = operation["x-sdk-class-name"]
            summary = operation.get("summary") or operation.get("operationId")
            description = (operation.get("description") or "").strip()
            parameters = []

            ordered_parameters = sorted(
                operation.get("parameters", []),
                key=lambda item: (
                    python_default_for_schema(
                        item.get("schema", {}), required=item.get("required", False)
                    )
                    is not None,
                ),
            )
            for parameter in ordered_parameters:
                schema = parameter.get("schema", {})
                parameters.append(
                    ParameterInfo(
                        api_name=parameter["name"],
                        python_name=parameter["x-sdk-python-name"],
                        python_type=python_type_for_schema(
                            schema, required=parameter.get("required", False)
                        ),
                        required=parameter.get("required", False),
                        default_expr=python_default_for_schema(
                            schema, required=parameter.get("required", False)
                        ),
                        description=(parameter.get("description") or "").strip(),
                    )
                )

            resources.setdefault(
                namespace,
                {
                    "class_name": class_name,
                    "tag": tag,
                    "operations": [],
                },
            )["operations"].append(
                OperationInfo(
                    operation_id=operation["operationId"],
                    method_name=operation["x-sdk-method-name"],
                    class_name=class_name,
                    namespace=namespace,
                    tag=tag,
                    path=path,
                    summary=summary,
                    description=description,
                    order=operation_order(operation),
                    parameters=tuple(parameters),
                )
            )

    ordered_resources = []
    for namespace, data in sorted(resources.items()):
        operations = tuple(
            sorted(
                data["operations"],
                key=lambda item: (item.order, item.path, item.method_name),
            )
        )
        ordered_resources.append(
            ResourceInfo(
                namespace=namespace,
                class_name=data["class_name"],
                tag=data["tag"],
                operations=operations,
            )
        )
    return ordered_resources


def render_docstring(
    summary: str, description: str, parameters: tuple[ParameterInfo, ...]
) -> str:
    lines = [summary]
    if description:
        lines.append("")
        lines.extend(description.splitlines())
    if parameters:
        lines.append("")
        lines.append("Args:")
        for parameter in parameters:
            param_description = (
                parameter.description.replace("\n", " ").strip() or "No description."
            )
            lines.append(f"    {parameter.python_name}: {param_description}")
    content = "\n".join(lines)
    indented = textwrap.indent(content, "        ")
    return f'        """\n{indented}\n        """\n'


def render_parameter_signature(parameters: tuple[ParameterInfo, ...]) -> str:
    if not parameters:
        return "self"
    rendered = ["self", "*"]
    for parameter in parameters:
        if parameter.default_expr is None:
            rendered.append(f"{parameter.python_name}: {parameter.python_type}")
        else:
            rendered.append(
                f"{parameter.python_name}: {parameter.python_type} = {parameter.default_expr}"
            )
    return ",\n        ".join(rendered)


def render_params_dict(parameters: tuple[ParameterInfo, ...]) -> str:
    if not parameters:
        return "{}"
    lines = ["{"]
    for parameter in parameters:
        lines.append(f'            "{parameter.api_name}": {parameter.python_name},')
    lines.append("        }")
    return "\n".join(lines)


def render_resource_module(resource: ResourceInfo) -> str:
    methods = []
    for operation in resource.operations:
        signature = render_parameter_signature(operation.parameters)
        params_dict = render_params_dict(operation.parameters)
        docstring = render_docstring(
            operation.summary, operation.description, operation.parameters
        )
        methods.append(
            f"    def {operation.method_name}(\n"
            f"        {signature},\n"
            f"    ) -> ApiResponse[Any]:\n"
            f"{docstring}"
            f"        return self._get(\n"
            f'            "{operation.path}",\n'
            f"            {params_dict},\n"
            f"        )\n"
        )

    return (
        "from __future__ import annotations\n\n"
        "from typing import Any\n\n"
        "from justoneapi._resource import BaseResource\n"
        "from justoneapi._response import ApiResponse\n\n\n"
        f"class {resource.class_name}(BaseResource):\n"
        f'    """Generated resource for {resource.tag}."""\n\n'
        + "\n".join(methods)
        + "\n"
    )


def render_resources_index(resources: list[ResourceInfo]) -> str:
    import_lines = [
        f"from justoneapi.generated.resources.{resource.namespace} import {resource.class_name}"
        for resource in resources
    ]
    mapping_lines = [
        f'    "{resource.namespace}": {resource.class_name},' for resource in resources
    ]
    all_names = ",\n    ".join(
        [repr(resource.class_name) for resource in resources]
        + [repr("RESOURCE_CLASSES")]
    )
    return (
        "from __future__ import annotations\n\n"
        + "\n".join(import_lines)
        + "\n\nRESOURCE_CLASSES = {\n"
        + "\n".join(mapping_lines)
        + "\n}\n\n__all__ = [\n    "
        + all_names
        + "\n]\n"
    )


def render_generated_init() -> str:
    return (
        "from justoneapi.generated.models import Code, Result\n"
        "from justoneapi.generated.resources import RESOURCE_CLASSES\n\n"
        '__all__ = ["Code", "RESOURCE_CLASSES", "Result"]\n'
    )


def ensure_generated_directories() -> None:
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    GENERATED_RESOURCES_ROOT.mkdir(parents=True, exist_ok=True)


def write_generated_resources(resources: list[ResourceInfo]) -> None:
    ensure_generated_directories()

    for existing in GENERATED_RESOURCES_ROOT.glob("*.py"):
        existing.unlink()

    for resource in resources:
        module_path = GENERATED_RESOURCES_ROOT / f"{resource.namespace}.py"
        module_path.write_text(render_resource_module(resource))

    (GENERATED_RESOURCES_ROOT / "__init__.py").write_text(
        render_resources_index(resources)
    )
    (GENERATED_ROOT / "__init__.py").write_text(render_generated_init())


def generate_models(spec_path: Path) -> None:
    ensure_generated_directories()
    subprocess.run(
        [
            sys.executable,
            "-m",
            "datamodel_code_generator",
            "--input",
            str(spec_path),
            "--input-file-type",
            "openapi",
            "--output",
            str(GENERATED_MODELS_PATH),
            "--output-model-type",
            "pydantic_v2.BaseModel",
            "--target-python-version",
            "3.10",
            "--disable-timestamp",
            "--use-annotated",
        ],
        check=True,
    )


def format_generated_code() -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "black",
            str(GENERATED_ROOT),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def generate_sdk(normalized_spec_path: Path) -> list[ResourceInfo]:
    normalized_spec = load_json(normalized_spec_path)
    resources = collect_resources(normalized_spec)
    generate_models(normalized_spec_path)
    write_generated_resources(resources)
    format_generated_code()
    return resources


def operation_map(spec: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.startswith("x-"):
                continue
            result[(method.upper(), path)] = {
                "operation_id": operation.get("operationId"),
                "path": path,
                "method": method.upper(),
                "body": operation,
            }
    return result


def build_diff_summary(old_spec: dict[str, Any], new_spec: dict[str, Any]) -> str:
    old_map = operation_map(old_spec)
    new_map = operation_map(new_spec)
    added = sorted(set(new_map) - set(old_map))
    removed = sorted(set(old_map) - set(new_map))
    changed = []
    for operation_key in sorted(set(old_map) & set(new_map)):
        old_entry = old_map[operation_key]
        new_entry = new_map[operation_key]
        if json.dumps(old_entry, sort_keys=True) != json.dumps(
            new_entry, sort_keys=True
        ):
            changed.append(operation_key)

    old_tags = len(old_spec.get("tags", []))
    new_tags = len(new_spec.get("tags", []))
    old_paths = len(old_spec.get("paths", {}))
    new_paths = len(new_spec.get("paths", {}))

    lines = [
        "# OpenAPI Sync Summary",
        "",
        f"- Paths: {old_paths} -> {new_paths}",
        f"- Tags: {old_tags} -> {new_tags}",
        f"- Added operationId count: {len(added)}",
        f"- Removed operationId count: {len(removed)}",
        f"- Changed operationId count: {len(changed)}",
        "",
        "## Added operationId",
    ]
    lines.extend(
        [f"- {new_map[item]['operation_id']} [{item[0]} {item[1]}]" for item in added]
        or ["- None"]
    )
    lines.append("")
    lines.append("## Removed operationId")
    lines.extend(
        [f"- {old_map[item]['operation_id']} [{item[0]} {item[1]}]" for item in removed]
        or ["- None"]
    )
    lines.append("")
    lines.append("## Changed operationId")
    lines.extend(
        [f"- {new_map[item]['operation_id']} [{item[0]} {item[1]}]" for item in changed]
        or ["- None"]
    )
    lines.append("")
    return "\n".join(lines)
