import requests
from justoneapi import __version__

from justoneapi.log import logger


def _request(method: str, url: str, params: dict, timeout: int) -> requests.Response:
    headers = {
        "JUSTONEAPI_PYTHON_SKD_VERSION": __version__,
    }
    response = requests.request(method, url, params=params, timeout=timeout, headers=headers)

    log_message = response.headers.get("JUSTONEAPI_PYTHON_SDK_LOG_MESSAGE")
    if log_message:
        logger.warning(log_message)
    version_deprecated = response.headers.get("JUSTONEAPI_PYTHON_SDK_VERSION_DEPRECATED")
    if version_deprecated:
        raise RuntimeError(f"JustoneAPI Python SDK version {__version__} is deprecated, please update to the latest version.")

    return response


def get_request(url: str, params: dict):
    try:
        response_data = _request(method="GET", url=url, params=params, timeout=60).json()
        code = response_data["code"]
        data = response_data["data"]
        message = response_data["message"]

        if code == 0:
            return True, data, message
        if str(code).startswith('2'):
            return True, data, message
        return False, data, message
    except RuntimeError as re:
        raise re
    except Exception as e:
        logger.exception(e)
        return False, None, "request error"


def get_request_page(url: str, params: dict):
    try:
        response_data = _request(method="GET", url=url, params=params, timeout=60).json()
        code = response_data["code"]
        data = response_data["data"]
        message = response_data["message"]

        if code == 0:
            return True, data, message
        if str(code).startswith('2'):
            return True, data, message
        return False, data, message
    except RuntimeError as re:
        raise re
    except Exception as e:
        logger.exception(e)
        return False, None, "request error"