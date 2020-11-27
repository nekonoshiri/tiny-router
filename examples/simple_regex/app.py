from typing import Any, Dict

from tiny_router import MethodNotAllowed, ResourceNotFound

from .routes import router


def run(method: str, resource: str) -> Dict[str, Any]:
    try:
        route = router.resolve(method, resource)
        return route()
    except MethodNotAllowed:
        return {"error_code": "MethodNotAllowed"}
    except ResourceNotFound:
        return {"error_code": "ResourceNotFound"}
