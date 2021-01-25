from typing import Any, Dict

from ..router import Router

router = Router()


@router.post("/users")
def create_user() -> Dict[str, Any]:
    new_user = {"id": "002", "name": "user2"}
    return {"id": new_user["id"]}
