try:
    from typing import TypedDict
except ImportError:
    from mypy_extensions import TypedDict

from typing import Optional, List


class Person(TypedDict):
    firstName: Optional[str]
    lastName: Optional[str]
    age: Optional[int]
