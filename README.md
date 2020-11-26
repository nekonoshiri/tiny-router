# tiny-router

[![PyPI](https://img.shields.io/pypi/v/tiny-router)](https://pypi.org/project/tiny-router/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tiny-router)](https://pypi.org/project/tiny-router/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/github/license/nekonoshiri/tiny-router)](https://github.com/nekonoshiri/tiny-router/blob/main/LICENSE)

A tiny HTTP router like this:

```Python
from tiny_router import SimpleRouter

router = SimpleRouter()


@router.get("/users")
def list_users():
    ...


@router.post("/users")
def create_user():
    ...


another_router = SimpleRouter()
router.include(another_router)

route = router.resolve("GET", "/users")
```

## Features

- `SimpleRouter`: exact-match router
- `SimpleRegexRouter`: simple regex-based router
- Abstract `Router`: user can implement their own routers
- Support for type hints

## Usage

See `examples/` directory of [repository](https://github.com/nekonoshiri/tiny-router).
