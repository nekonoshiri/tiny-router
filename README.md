# tiny-router

[![PyPI](https://img.shields.io/pypi/v/tiny-router)](https://pypi.org/project/tiny-router/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tiny-router)](https://pypi.org/project/tiny-router/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/github/license/nekonoshiri/tiny-router)](https://github.com/nekonoshiri/tiny-router/blob/main/LICENSE)

Tiny HTTP router.

## Usage

```Python
from tiny_router.simple import SimpleRouter

router = SimpleRouter()


@router.get("/users/{user_id}")
def get_user(params):
    if params.get("user_id") == 1:
        return {"id": 1, "name": "Alice"}


route = router.resolve("GET", "/users/{user_id}")
user = route({"user_id": 1})

assert user == {"id": 1, "name": "Alice"}
```

More examples are in `examples/` directory of
[repository](https://github.com/nekonoshiri/tiny-router).

## Features

- `SimpleRouter`: exact-match router
- `SimpleRegexRouter`: simple regex-based router
- Abstract `Router`: user can implement their own routers
- Support for type hints

## API

### Module `tiny_router`

#### *abstract class* `Router[Route, ResolvedRoute]`

Router class, which can add and resolve routes.
Classes implementing this class must implement abstract method `add` and `resolve`.

##### *type parameter* `Route`

Type of routes passed to `add` method.

##### *type parameter* `ResolvedRoute`

Type of routes returned from `resolve` method.

##### *abstract method* `add(method: str, resource: str, route: Route) -> None`

Shall add a route to the router.

##### *abstract method* `resolve(method: str, resource: str) -> ResolvedRoute`

Shall resolve a route, i.e. retrieve an added route from the router.
Should raise `RouteNotFound` exception or its subclass if no routes are found.

##### *method* `route(method: str, resource: str) -> Callable[[Route], None]`

Return a decorator that adds the decorated object to the router.

For example,

```Python
@router.route("GET", "/users")
def route_func(params):
    ...
```

is the same as

```Python
def route_func(params):
    ...

router.add("GET", "/users", route_func)
```

where `router` is a router.

##### *method* `get(resource: str) -> Callable[[Route], None]`

Same as `route("GET", resource)`.

##### *method* `post(resource: str) -> Callable[[Route], None]`

Same as `route("POST", resource)`.

##### *method* `put(resource: str) -> Callable[[Route], None]`

Same as `route("PUT", resource)`.

##### *method* `patch(resource: str) -> Callable[[Route], None]`

Same as `route("PATCH", resource)`.

##### *method* `delete(resource: str) -> Callable[[Route], None]`

Same as `route("DELETE", resource)`.

##### *method* `head(resource: str) -> Callable[[Route], None]`

Same as `route("HEAD", resource)`.

#### *class* `RouteNotFound`

Subclass of `Exception`, representing that the route is not found.

#### *class* `MethodNotAllowed(method: str)`

Subclass of `RouteNotFound`, representing that the method is not allowed.

TODO: 引数なしで raise したらどうなるのか検証
TODO: メンバ変数について追記

#### *class* `ResourceNotFound(resource: str)`

Subclass of `RouteNotFound`, representing that the resource is not found.

TODO: 引数なしで raise したらどうなるのか検証
TODO: メンバ変数について追記

---

### Module `tiny_router.simple`

#### *class* `SimpleRouter[Route]()`

An implementation of `Router[Route, Route]`.

##### *type parameter* `Route`

Type of routes passed to `add` method or returned from `resolve` method.

##### *method* `add(method: str, resource: str, route: Route) -> None`

Add a route to the router.

##### *method* `resolve(method: str, resource: str) -> Route`

`add` メソッドや `route` メソッドで追加されたルートから、
`method` と `resource` のそれぞれが一致するルートを探して返します。

そのようなルートが存在せず、`resource` のみが一致するルートが存在する場合は、
`MethodNotAllowed(method)` exception を投げます。

Otherwise, raise `ResourceNotFound(resource)` exception.

---

### Module `tiny_router.simple_regex`

#### *class* `SimpleRegexRouter[ResolvedRoute](matching_precedence: Literal["first-in", "last-in"])`

An implementation of `Router[Callable[[Match[str]], ResolvedRoute], ResolvedRoute]`.

`matching_precedence` 引数は、`resolve` メソッドの挙動に影響を与えます。
`resolve` メソッドの説明を参照してください。

##### *type parameter* `ResolvedRoute`

Type of routes returned from `resolve` method.

##### *method* `add(method: str, resource: str, route: Callable[[Match[str]], ResolvedRoute]) -> None`

Add a route to the router.

`resource` には正規表現文字列を渡すことができます。
`resolve` メソッドの説明を参照してください。

##### *method* `resolve(method: str, resource: str) -> ResolvedRoute`

`add` メソッドや `route` メソッドで追加されたルートから、
`method` が一致し、かつこのメソッドの引数の `resource` が
そのルートの `resource` 正規表現文字列にマッチするようなルートを探して返します。

そのようなルートが存在せず、`resource` のみがマッチするようなルートが存在する場合は、
`MethodNotAllowed(method)` exception を投げます。

Otherwise, raise `ResourceNotFound(resource)` exception.

`matching_precedence` が `first-in` に指定されていた場合、
より最初に追加されたメソッドが優先してマッチします。
`last-in` の場合、より最後に追加されたメソッドが優先してマッチします。

返却されるルート (`ResolvedRoute`) は、
`add` メソッドなどで追加したルート (`Callable[[Match[str]], ResolvedRoute]`) に
引数としてマッチしたマッチオブジェクト (`Match[str]`) を渡してコールしたときの返り値です。

TODO: translate to english.
