from typing import Callable

from tiny_router.simple import SimpleRouter

from .request import Request
from .response import Response

Route = Callable[[Request], Response]

Router = SimpleRouter[Route]
