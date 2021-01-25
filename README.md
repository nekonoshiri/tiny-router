# tiny-router

[![PyPI](https://img.shields.io/pypi/v/tiny-router)](https://pypi.org/project/tiny-router/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tiny-router)](https://pypi.org/project/tiny-router/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/github/license/nekonoshiri/tiny-router)](https://github.com/nekonoshiri/tiny-router/blob/main/LICENSE)

Tiny HTTP router.

## Usage

```Python
from tiny_router import SimpleRouter

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

TODO

