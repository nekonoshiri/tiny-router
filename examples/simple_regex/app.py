import json

from tiny_router import MethodNotAllowed, ResourceNotFound

from .request import Request
from .response import Response
from .routes import router


def run(method: str, resource: str, request: Request) -> Response:
    try:
        route = router.resolve(method, resource)
        return route(request)
    except MethodNotAllowed:
        return Response(405, json.dumps({"message": "Method not allowed"}))
    except ResourceNotFound:
        return Response(404, json.dumps({"message": "Resource not found"}))
