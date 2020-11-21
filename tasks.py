import invoke

module_name = "tiny_router"
src = "tiny_router"
tests = "tests"


@invoke.task
def lint(c):
    c.run(f"isort {src} {tests}")
    c.run(f"black {src} {tests}")
    c.run(f"flake8 {src} {tests}")
    c.run(f"mypy {src}")
    c.run(f"pydocstyle {src}")


@invoke.task
def test(c):
    c.run(f"pytest {tests}")


@invoke.task
def cov(c):
    c.run(f"pytest --cov={module_name} --cov-branch tests")
