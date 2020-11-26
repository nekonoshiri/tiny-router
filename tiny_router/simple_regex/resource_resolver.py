from typing import Callable, List, Match, Pattern, Tuple

from ..exceptions import ResourceNotFound

ResourceResolver = Callable[[List[Pattern[str]], str], Tuple[Pattern[str], Match]]


def first_in(
    patterns: List[Pattern[str]], resource: str
) -> Tuple[Pattern[str], Match[str]]:
    for pattern in patterns:
        match = pattern.fullmatch(resource)
        if match:
            return pattern, match
    raise ResourceNotFound(resource) from None


def last_in(
    patterns: List[Pattern[str]], resource: str
) -> Tuple[Pattern[str], Match[str]]:
    return first_in(list(reversed(patterns)), resource)
