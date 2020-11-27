from typing import Any, Callable, Dict

from tiny_router import SimpleRouter

from . import create_user, list_users

Route = Callable[[], Dict[str, Any]]

router = SimpleRouter[Route]()
router.include(create_user.router)
router.include(list_users.router)
