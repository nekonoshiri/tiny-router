from typing import Any, Callable, Dict

from tiny_router import SimpleRouter

Route = Callable[[], Dict[str, Any]]

Router = SimpleRouter[Route]
