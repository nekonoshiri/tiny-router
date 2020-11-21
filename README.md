# tiny-router

A tiny HTTP router.

## Usage

```Python
from tiny_router import MethodNotAllowed, ResourceNotFound, Router
from tiny_router.routes import SimpleRoutes

router = Router(SimpleRoutes())


@router.get("/users")
def get_users():
    return {"users": [{"id": 0, "name": "user1"}]}


route = router.resolve("GET", "/users")
users = route()
print(users)

try:
    router.resolve("POST", "/users")
except MethodNotAllowed:
    print("Method Not Allowed")

try:
    router.resolve("GET", "/items")
except ResourceNotFound:
    print("Resource Not Found")
```

