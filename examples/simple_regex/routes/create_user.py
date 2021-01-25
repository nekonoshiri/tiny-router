import json
from typing import Any, Dict, Match

from ..request import Request
from ..response import Response
from ..router import ResolvedRoute, Router

router = Router()


@router.post("/users")
def create_user(match: Match[str]) -> ResolvedRoute:
    def _create_user(request: Request) -> Response:
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return Response(400, json.dumps({"message": "Invalid JSON"}))

        name = body.get("name")

        if not name:
            return Response(400, json.dumps({"message": "name is required"}))

        new_user = {"id": "002", "name": name}

        save_user(new_user)

        return Response(201, json.dumps(new_user))

    return _create_user


def save_user(user: Dict[str, Any]) -> None:
    # Here save user to database.
    pass
