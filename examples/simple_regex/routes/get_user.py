import json
from typing import Any, Dict, Match

from ..request import Request
from ..response import Response
from ..router import ResolvedRoute, Router

router = Router()


@router.get(r"/users/(?P<user_id>\d+)")
def get_user(match: Match[str]) -> ResolvedRoute:
    def _get_user(request: Request) -> Response:
        user_id = match.group("user_id")
        try:
            user = load_user(user_id)
            return Response(200, json.dumps(user))
        except Exception:
            return Response(404, json.dumps({"message": "User not found"}))

    return _get_user


def load_user(user_id: str) -> Dict[str, Any]:
    # Here load user from database.
    if user_id == "001":
        return {"id": user_id, "name": "Alice"}
    else:
        raise Exception("User not found")
