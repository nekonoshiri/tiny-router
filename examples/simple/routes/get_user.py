import json
from typing import Any, Dict

from ..request import Request
from ..response import Response
from ..router import Router

router = Router()


@router.get("/users/{user_id}")
def get_user(request: Request) -> Response:
    user_id = request.path_parameters.get("user_id")

    if not user_id:
        return Response(400, json.dumps({"message": "user_id is required"}))

    try:
        user = load_user(user_id)
        return Response(200, json.dumps(user))
    except Exception:
        return Response(404, json.dumps({"message": "User not found"}))


def load_user(user_id: str) -> Dict[str, Any]:
    # Here load user from database.
    if user_id == "001":
        return {"id": user_id, "name": "Alice"}
    else:
        raise Exception("User not found")
