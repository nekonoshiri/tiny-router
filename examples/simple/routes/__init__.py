from ..router import Router
from . import create_user, get_user

router = Router()
router.include(get_user.router)
router.include(create_user.router)
