import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("isort tiny_router tests examples")
    c.run("black tiny_router tests examples")
    c.run("flake8 tiny_router tests examples")
    c.run("mypy tiny_router examples")
    c.run("pytest examples")
    c.run("pytest --cov=tiny_router --cov-branch tests")
