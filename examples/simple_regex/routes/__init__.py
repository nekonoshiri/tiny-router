from ..router import Router
from . import get_user, list_users

router = Router()
router.include(get_user.router)
router.include(list_users.router)
