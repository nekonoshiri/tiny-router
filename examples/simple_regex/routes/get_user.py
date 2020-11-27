from typing import Any, Dict, Match

from ..router import Router

router = Router()


@router.get(r"/users/(?P<user_id>\d+)")
def get_user(match: Match[str]) -> Dict[str, Any]:
    user_id = match.group("user_id")
    return {"id": user_id, "name": f"user{user_id}"}
