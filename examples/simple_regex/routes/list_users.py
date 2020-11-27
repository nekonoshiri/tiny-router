from typing import Any, Dict, Match

from ..router import Router

router = Router()


@router.get("/users")
def list_users(match: Match[str]) -> Dict[str, Any]:
    users = [{"id": "001", "name": "user1"}]
    return {"users": users}
