class RouteNotFound(Exception):
    pass


class ResourceNotFound(RouteNotFound):
    def __init__(self, resource: str) -> None:
        self.resource = resource


class MethodNotAllowed(RouteNotFound):
    def __init__(self, method: str) -> None:
        self.method = method
