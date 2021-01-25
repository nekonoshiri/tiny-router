import invoke

module_name = "tiny_router"
src = "tiny_router"
tests = "tests"
examples = "examples"


@invoke.task
def lint(c):
    c.run(f"isort {src} {tests} {examples}")
    c.run(f"black {src} {tests} {examples}")
    c.run(f"flake8 {src} {tests} {examples}")
    c.run(f"mypy {src} {examples}")


@invoke.task
def test(c):
    c.run(f"pytest {tests}")


@invoke.task
def example(c):
    c.run(f"pytest {examples}")


@invoke.task
def cov(c):
    c.run(f"pytest --cov={module_name} --cov-branch tests")
