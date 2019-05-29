try:
    from typing import TypedDict
except ImportError:
    from mypy_extensions import TypedDict

from typing import Optional, List


class LongitudeandLatitudeValues(TypedDict):
    latitude: float
    longitude: float
