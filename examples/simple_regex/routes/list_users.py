from typing import Any, Dict, Match

from ..router import ResolvedRoute, Router

router = Router()


@router.get("/users")
def list_users(match: Match[str]) -> ResolvedRoute:
    def _list_users() -> Dict[str, Any]:
        users = [{"id": "001", "name": "user1"}]
        return {"users": users}

    return _list_users
